"""Shared pipeline for page lessons (intro -> pages + quizzes -> outro).

A lesson module (e.g. zero_defects.py, yamazumi.py) only holds DATA:
  ID            folder name under public/audio and src/captions, e.g. "zd"
  NAME          clone-script / clones folder name, e.g. "zero_defects"
  INTRO_SCRIPT, OUTRO_SCRIPT, PAGES, QUIZZES
  say(text)     optional spoken-only pronunciation fixes

and calls `lesson_lib.main(sys.modules[__name__])`. Everything else lives here:

  python narration/<lesson>.py            bootstrap MISSING clips with edge-tts
  python narration/<lesson>.py --force    re-voice every clip with edge-tts
  python narration/import_clones.py <lesson> [clones_dir]   import cloned voice

Outputs per lesson:
  public/audio/<ID>/<key>.mp3          narration clip per scene / quiz q+a
  src/captions/<ID>/words.json         {key: [{w,s,e}]} caption word timings
  src/lessons/<ID>/timings.json        seconds per clip (drives the timeline)
  src/lessons/<ID>/content.json        on-screen page text
  src/lessons/<ID>/quizzes.json        on-screen quiz data (+ think seconds)
  out/<NAME>.json                      {key: spoken text} for the clone notebook
"""
import asyncio
import json
import math
import re
import subprocess
import sys
from pathlib import Path

VOICE = "en-US-ChristopherNeural"
RATE = "-6%"

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
DEFAULT_CLONES = Path(r"C:/Users/PrashantMarathe-AIL/Downloads/clones/clones")
# Every imported clip is set to this loudness (gain only, no EQ/compression),
# matching the user's reference clip reference_30s.mp3 (-29.2 LUFS), which
# produced the good Oct 19 voice. Keeps every lesson at the same level whatever Colab outputs.
TARGET_LUFS = -29.0
MAX_PEAK_DB = -3.0


def paths(mod):
    audio = ROOT / "public" / "audio" / mod.ID
    caps = ROOT / "src" / "captions" / mod.ID
    data = ROOT / "src" / "lessons" / mod.ID
    for d in (audio, caps, data, OUT):
        d.mkdir(parents=True, exist_ok=True)
    return audio, caps, data


def say(mod, text: str) -> str:
    return mod.say(text) if hasattr(mod, "say") else text


def scenes(mod):
    """All narrated clips as (key, on-screen text). Quiz clips are <key>_q / <key>_a."""
    yield ("intro", mod.INTRO_SCRIPT)
    for p in mod.PAGES:
        yield (p["key"], p["script"])
        for q in mod.QUIZZES:
            if q["after"] == p["key"]:
                yield (f"{q['key']}_q", q["q_script"])
                yield (f"{q['key']}_a", q["a_script"])
    yield ("outro", mod.OUTRO_SCRIPT)


def dur(mp3: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(mp3)],
        capture_output=True, text=True, check=True)
    return round(float(out.stdout.strip()), 3)


def word_times(text: str, duration: float):
    """Spread words across [0, duration] proportional to length (+1 per word).
    Captions are shown per sentence/line, so accurate line starts are enough;
    punctuation is kept so the caption splitter finds sentence ends."""
    words = text.split()
    weights = [len(w) + 1 for w in words]
    total = sum(weights) or 1
    res, cur = [], 0.0
    for w, wt in zip(words, weights):
        s = cur
        cur += duration * wt / total
        res.append({"w": w, "s": round(s, 3), "e": round(cur, 3)})
    return res


def silences(mp3: Path, noise="-35dB", min_len=0.2):
    """Pauses in a clip as [(start, end)] seconds, via ffmpeg silencedetect."""
    err = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(mp3), "-af",
         f"silencedetect=noise={noise}:d={min_len}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    out, start = [], None
    for line in err.splitlines():
        if "silence_start:" in line:
            start = float(line.split("silence_start:")[1].split()[0])
        elif "silence_end:" in line and start is not None:
            out.append((max(0.0, start), float(line.split("silence_end:")[1].split()[0])))
            start = None
    if start is not None:  # trailing silence runs to the end of the clip
        out.append((start, float("inf")))
    return out


def _match_sentence_ends(breaks, cum, inner, s0, s1):
    """Pick which pause follows each sentence end, for the WHOLE clip at once.

    Dynamic programming over (sentence end -> pause) pairs, in order. A choice
    is good when the speaking pace between consecutive anchors stays close to
    the clip's average pace; leaving a sentence end unmatched, or talking
    through a long pause, costs a penalty. This avoids the drift of matching
    one sentence at a time (one miss shifting every later caption)."""
    if not breaks or not inner:
        return {}
    speech = (s1 - s0) - sum(b - a for a, b in inner)
    rate = cum[-1] / max(speech, 1e-6)                # chars per second
    UNMATCHED = 1.5                                   # sentence end with no pause
    SKIP = 1.2                                        # per second of pause talked through
    PACE = 40.0                                       # weight of pace deviation

    # nodes: start, every (break i, pause j), end. Each has (k, end_t, next_start_t, i, j)
    start = (0, s0, s0, -1, -1)
    end = (len(cum) - 1, s1, s1, len(breaks), len(inner))
    nodes = [start] + [(breaks[i], a, b, i, j) for i in range(len(breaks))
                       for j, (a, b) in enumerate(inner)] + [end]

    def cost(u, v):
        if not (v[3] > u[3] and v[4] > u[4]):
            return None
        skipped = inner[u[4] + 1:v[4]]
        t = (v[1] - u[2]) - sum(b - a for a, b in skipped)
        if t <= 0.05:
            return None
        chars = cum[v[0]] - cum[u[0]]
        dev = math.log(max(chars, 1) / t / rate)
        return (PACE * dev * dev * chars / cum[-1]
                + UNMATCHED * (v[3] - u[3] - 1)
                + SKIP * sum(b - a for a, b in skipped))

    best = {0: (0.0, None)}
    order = sorted(range(1, len(nodes)), key=lambda x: (nodes[x][3], nodes[x][4]))
    for vi in order:
        v = nodes[vi]
        cand = None
        for ui, (c0, _) in best.items():
            c = cost(nodes[ui], v)
            if c is not None and (cand is None or c0 + c < cand[0]):
                cand = (c0 + c, ui)
        if cand:
            best[vi] = cand
    out, vi = {}, len(nodes) - 1
    if vi not in best:
        return {}
    vi = best[vi][1]
    while vi:
        k, a, b, _, _ = nodes[vi]
        out[k] = (a, b)
        vi = best[vi][1]
    return out


def aligned_word_times(text: str, mp3: Path):
    """Word timings snapped to the clip's REAL pauses, so captions change when
    the voice actually starts the next sentence/phrase.

    1. Sentence ends (. ! ?) are matched to pauses for the whole clip at once
       (_match_sentence_ends: keeps the speaking pace even between anchors).
    2. Commas/semicolons/colons/dashes then snap to a remaining pause within
       0.6 s of where they're expected between those anchors.
    3. Words between anchors are spread by character length."""
    d = dur(mp3)
    words = text.split()
    n = len(words)
    if n == 0:
        return []
    weights = [len(w) + 1 for w in words]
    cum = [0]
    for wt in weights:
        cum.append(cum[-1] + wt)

    sil = silences(mp3)
    s0 = sil[0][1] if sil and sil[0][0] <= 0.05 else 0.0           # lead-in
    s1 = sil[-1][0] if sil and sil[-1][1] >= d - 0.05 else d        # tail
    inner = [(a, min(b, d)) for a, b in sil if a > s0 + 0.05 and b < s1 - 0.05]

    ends = lambda k, pat: words[k - 1].rstrip("\"”'")[-1:] in pat
    breaks = [k for k in range(1, n) if ends(k, ".!?")]

    # anchors: word boundary k (between words k-1 and k) -> (end of k-1, start of k)
    anchors = {0: (s0, s0), n: (s1, s1)}
    anchors.update(_match_sentence_ends(breaks, cum, inner, s0, s1))
    used = {inner.index(v) for k, v in anchors.items() if v in inner}

    def expected(k):
        lo = max(a for a in anchors if a <= k)
        hi = min(a for a in anchors if a >= k)
        t_lo, t_hi = anchors[lo][1], anchors[hi][0]
        f = (cum[k] - cum[lo]) / (cum[hi] - cum[lo])
        return t_lo + f * (t_hi - t_lo), t_lo, t_hi

    for k in range(1, n):
        if k in anchors or not ends(k, ",;:—–"):
            continue
        est, t_lo, t_hi = expected(k)
        best = None
        for i, (a, b) in enumerate(inner):
            mid = (a + b) / 2
            if i in used or not (t_lo < a and b < t_hi):
                continue
            if abs(mid - est) <= 0.6 and (best is None or abs(mid - est) < abs(sum(inner[best]) / 2 - est)):
                best = i
        if best is not None:
            used.add(best)
            anchors[k] = inner[best]

    res = []
    keys = sorted(anchors)
    for lo, hi in zip(keys, keys[1:]):
        t, t_end = anchors[lo][1], anchors[hi][0]
        for j in range(lo, hi):
            e = t + (t_end - t) * weights[j] / (cum[hi] - cum[j]) if j < hi - 1 else t_end
            res.append({"w": words[j], "s": round(t, 3), "e": round(e, 3)})
            t = e
    return res


def realign(mod):
    """Rebuild caption words for every existing clip from its real pauses."""
    audio, _, _ = paths(mod)
    words = load_words(mod)
    for key, text in scenes(mod):
        mp3 = audio / f"{key}.mp3"
        if mp3.exists():
            words[key] = aligned_word_times(text, mp3)
    write_outputs(mod, words)


def load_words(mod) -> dict:
    _, caps, _ = paths(mod)
    f = caps / "words.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def _norm(s: str) -> list:
    return [w for w in (re.sub(r"[^\w'-]", "", x).lower() for x in s.split()) if w]


def cue_index(script: str, cue: str) -> int:
    """Index of the script word where `cue` (an exact phrase from the script) starts."""
    sw, cw = _norm(script), _norm(cue)
    if not cw:
        raise ValueError("missing cue")
    for i in range(len(sw) - len(cw) + 1):
        if sw[i:i + len(cw)] == cw:
            return i
    raise ValueError(f"cue not found in script: {cue!r}")


def page_content(p: dict, words) -> dict:
    """On-screen page data. Each point is (text, cue): the box appears when the
    voice reaches its cue, and the example box when it reaches example_cue, so
    the screen always shows what is being said."""
    out = {k: p[k] for k in ("key", "num", "title", "example")}
    if "visual" in p:
        out["visual"] = p["visual"]
    points = p["points"]
    out["bullets"] = [t for t, _ in points]
    # word index -> time; only valid when the timings follow the script word for
    # word (cloned clips always do; an edge-tts draft may not, then no sync).
    if words and len(words) == len(p["script"].split()):
        out["at"] = [words[cue_index(p["script"], c)]["s"] for _, c in points]
        out["exampleAt"] = words[cue_index(p["script"], p["example_cue"])]["s"]
    return out


def write_outputs(mod, words: dict):
    """Rebuild timings/content/quizzes/words/clone-script from the clips on disk."""
    audio, caps, data = paths(mod)
    keys = [k for k, _ in scenes(mod)]
    # clips not voiced yet (e.g. quiz clips awaiting a clone) are left out; the
    # timeline then shows those quizzes silently.
    timings = {k: dur(audio / f"{k}.mp3") for k in keys if (audio / f"{k}.mp3").exists()}
    (data / "timings.json").write_text(json.dumps(timings, indent=2), encoding="utf-8")

    ordered = {k: words[k] for k in keys if k in words}
    (caps / "words.json").write_text(json.dumps(ordered, ensure_ascii=False), encoding="utf-8")

    content = {"pages": [page_content(p, words.get(p["key"])) for p in mod.PAGES]}
    (data / "content.json").write_text(json.dumps(content, indent=2, ensure_ascii=False), encoding="utf-8")

    # think countdown sized to the question clip, so the question is fully read.
    quizzes = [{k: q[k] for k in ("key", "num", "after", "question", "options", "correct", "explanation")}
               | ({"think": max(4, math.ceil(timings[f"{q['key']}_q"]))} if f"{q['key']}_q" in timings else {})
               for q in mod.QUIZZES]
    (data / "quizzes.json").write_text(json.dumps({"quizzes": quizzes}, indent=2, ensure_ascii=False),
                                       encoding="utf-8")

    # clone script: {key: spoken text}. Kept in out/ (gitignored) -> content stays off GitHub.
    clone = {k: say(mod, t) for k, t in scenes(mod)}
    (OUT / f"{mod.NAME}.json").write_text(json.dumps(clone, indent=2, ensure_ascii=False), encoding="utf-8")

    total = sum(timings.values())
    print(f"timings/content/quizzes/words written. Clone script -> out/{mod.NAME}.json")
    print(f"Total narration ~ {total:.1f}s ({total/60:.1f} min) across {len(timings)} clips")


async def _voice(mod, key: str, text: str, mp3: Path):
    import edge_tts
    words = []
    comm = edge_tts.Communicate(say(mod, text), VOICE, rate=RATE, boundary="WordBoundary")
    with open(mp3, "wb") as fh:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                fh.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                s = chunk["offset"] / 1e7
                words.append({"w": chunk["text"], "s": round(s, 3), "e": round(s + chunk["duration"] / 1e7, 3)})
    # Spoken words may differ from on-screen text ("tact" vs "TAKT"): when the
    # counts match, keep edge-tts timing but show the on-screen spelling.
    shown = text.split()
    if len(shown) == len(words):
        words = [w | {"w": s} for w, s in zip(words, shown)]
    return words


def bootstrap(mod, force: bool):
    """Voice clips with edge-tts. Without --force, only MISSING clips are voiced,
    so already-imported cloned clips are never overwritten."""
    audio, _, _ = paths(mod)
    words = load_words(mod)
    for key, text in scenes(mod):
        mp3 = audio / f"{key}.mp3"
        if mp3.exists() and not force:
            if key not in words:
                words[key] = word_times(text, dur(mp3))
            continue
        words[key] = asyncio.run(_voice(mod, key, text, mp3))
        print("  voiced", key, f"(+{len(words[key])} words)")
    write_outputs(mod, words)


def loudness(path: Path):
    """(integrated LUFS, sample peak dBFS) of a clip."""
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af",
                          "ebur128=peak=sample", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    summary = err[err.rfind("Summary:"):]
    i = float(summary.split("I:")[1].split()[0])
    peak = float(summary.split("Peak:")[1].split()[0]) if "Peak:" in summary else 0.0
    return i, peak


def match_gain(path: Path) -> float:
    """dB of gain that brings a clip to TARGET_LUFS without peaks over MAX_PEAK_DB."""
    i, peak = loudness(path)
    return round(min(TARGET_LUFS - i, MAX_PEAK_DB - peak), 2)


def import_clones(mod, clones: Path):
    """Transcode cloned WAVs to the lesson's mp3s and rebuild every timing from
    the real cloned durations (no drift, no repeats)."""
    audio, _, _ = paths(mod)
    # A partial batch is fine (e.g. only the new quiz clips): clips without a
    # .wav keep their existing mp3. Only a clip with neither is an error.
    missing = [k for k, _ in scenes(mod)
               if not (clones / f"{k}.wav").exists() and not (audio / f"{k}.mp3").exists()]
    if missing:
        raise SystemExit(f"Missing cloned clips: {missing}\nLooked in: {clones}")
    words = load_words(mod)
    for key, text in scenes(mod):  # on-screen text, e.g. proper "TAKT"
        mp3 = audio / f"{key}.mp3"
        if not (clones / f"{key}.wav").exists():
            if key not in words:
                words[key] = word_times(text, dur(mp3))
            print(f"  kept     {key}  (no new clip)")
            continue
        wav = clones / f"{key}.wav"
        gain = match_gain(wav)
        subprocess.run(["ffmpeg", "-y", "-i", str(wav), "-af", f"volume={gain}dB", "-ar", "44100",
                        "-b:a", "192k", str(mp3)], check=True, capture_output=True)
        words[key] = aligned_word_times(text, mp3)
        print(f"  imported {key}  ({dur(mp3):.2f}s, gain {gain:+.1f} dB)")
    write_outputs(mod, words)


def main(mod):
    bootstrap(mod, force="--force" in sys.argv)
