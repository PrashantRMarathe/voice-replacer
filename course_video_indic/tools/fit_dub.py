"""Dub pilot: one English video, each language as its own audio track (like a dubbed film).

  python tools/fit_dub.py fit   zd te       # fit the language's clips to the English timings
  python tools/fit_dub.py track zd te       # that language's audio track (.m4a) + subtitles (.srt)
  python tools/fit_dub.py pack  zd hi te    # one mp4: video + every track + every subtitle -> final/dub/
  python tools/fit_dub.py all   zd hi te    # fit + track for each language, then pack

fit: public/audio/<id>_<lang>/<clip>.mp3 (the normal voiced lesson) -> public/audio/<id>_dub_<lang>/,
     end silence trimmed, sped up (atempo) only when longer than the English clip + 1 s
     (the scene holds 2.2 s after each clip, so 1 s of spill still leaves a pause).
track: needs out/dub/<Comp>_video.mp4 (src/dub/index.tsx <Comp>DubVideo: English video, music +
     effects, no voice). Places each clip where the English one starts (same maths as
     src/lessons/plan.ts), mixes it over the music/effects, normalises to -14 LUFS, and writes
     <lang>.srt from the lesson's caption words.
pack: video + all tracks + soft subtitles in one mp4 (players switch language), copied with the
     separate .m4a/.srt files to final/dub/ and Drive FFIQ_indic/final/dub/.
"""
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FPS = 30
PAD, QUIZ_LEAD = 2.2, 1.2          # src/lessons/plan.ts
SPILL = 1.0
COMP = json.loads((ROOT / "src/dub/lessons.json").read_text(encoding="utf-8"))
DRIVE = Path("G:/My Drive/FFIQ_indic/final/dub")
LANG3 = {"te": "tel", "hi": "hin", "ta": "tam", "mr": "mar"}
ENDS = ("।", ".", "?", "!")


def dur(f):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)]))


def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def english(lid):
    d = ROOT / "src/dub" / lid
    return (json.loads((d / "timings.json").read_text(encoding="utf-8")),
            json.loads((d / "content.json").read_text(encoding="utf-8"))["pages"],
            json.loads((d / "quizzes.json").read_text(encoding="utf-8"))["quizzes"])


def clip_starts(lid):
    """Absolute start (s) of every narration clip, as planLesson lays them out."""
    t, pages, quizzes = english(lid)
    frames = lambda s: math.ceil(s * FPS - 1e-9)
    seq = [("intro", None)]
    for p in pages:
        seq.append((p["key"], None))
        seq += [(q["key"], q) for q in quizzes if q["after"] == p["key"]]
    seq.append(("outro", None))
    start, out = 0, {}
    for key, q in seq:
        if q is None:
            out[key] = start / FPS
            start += frames(t[key] + PAD)
        else:
            think = q.get("think") or max(4, math.ceil(t[f"{key}_q"]))
            reveal = round((QUIZ_LEAD + think) * FPS)
            out[f"{key}_q"] = start / FPS
            out[f"{key}_a"] = (start + reveal) / FPS
            start += reveal + frames(t[f"{key}_a"] + PAD)
    return out, start


def fit(lid, lang):
    t, _, _ = english(lid)
    src, dst = ROOT / f"public/audio/{lid}_{lang}", ROOT / f"public/audio/{lid}_dub_{lang}"
    dst.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / "out/tmp/fit_dub.wav"
    speed = {}
    for k, e in t.items():
        ff("-i", str(src / f"{k}.mp3"), "-af",
           "areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse", str(tmp))
        r = max(1.0, dur(tmp) / (e + SPILL))
        ff("-i", str(tmp), "-af", f"atempo={r:.4f}", "-c:a", "libmp3lame", "-b:a", "128k", str(dst / f"{k}.mp3"))
        speed[k] = round(r, 4)
        print(f"{k:8} speed {r:.3f}  {dur(dst / f'{k}.mp3'):5.1f}s (English {e:.1f}s)")
    (dst / "speed.json").write_text(json.dumps(speed, indent=1), encoding="utf-8")


def srt_time(s):
    ms = round(s * 1000)
    return f"{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}"


def subtitles(lid, lang, starts, speed):
    """Sentence lines from the lesson's own caption words, moved to the dub timing."""
    words = json.loads((ROOT / f"src/captions/{lid}_{lang}/words.json").read_text(encoding="utf-8"))
    cues = []
    for k, ws in words.items():
        if k not in starts:
            continue
        line = []
        for i, w in enumerate(ws):
            line.append(w)
            if w["w"].endswith(ENDS) or len(line) >= 8 or i == len(ws) - 1:
                a = starts[k] + line[0]["s"] / speed[k]
                b = starts[k] + line[-1]["e"] / speed[k]
                cues.append((a, max(b, a + 1.0), " ".join(x["w"] for x in line)))
                line = []
    cues.sort()
    return "".join(f"{i}\n{srt_time(a)} --> {srt_time(min(b, cues[i][0] if i < len(cues) else b))}\n{txt}\n\n"
                   for i, (a, b, txt) in enumerate(cues, 1))


def track(lid, lang):
    comp = COMP[lid]
    out = ROOT / "out/dub"
    video = out / f"{comp}_video.mp4"
    clips = ROOT / f"public/audio/{lid}_dub_{lang}"
    speed = json.loads((clips / "speed.json").read_text(encoding="utf-8"))
    starts, total = clip_starts(lid)
    vlen = dur(video)
    assert abs(vlen - total / FPS) < 0.5, f"video {vlen:.1f}s, timeline {total / FPS:.1f}s"

    # voice stem: every clip delayed to its English start
    keys = list(starts)
    inputs, chains = [], []
    for i, k in enumerate(keys, 1):
        inputs += ["-i", str(clips / f"{k}.mp3")]
        ms = round(starts[k] * 1000)
        chains.append(f"[{i}:a]aresample=48000,adelay={ms}|{ms}[v{i}]")
    vo = "".join(f"[v{i}]" for i in range(1, len(keys) + 1))
    graph = ";".join(chains) + f";{vo}amix=inputs={len(keys)}:normalize=0[voice];"         "[0:a]aresample=48000[me];[me][voice]amix=inputs=2:normalize=0:duration=first,"         "loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    ff("-i", str(video), *inputs, "-filter_complex", graph, "-map", "[a]",
       "-ar", "48000", "-c:a", "aac", "-b:a", "192k", str(out / f"{comp}_{lang}.m4a"))
    (out / f"{comp}_{lang}.srt").write_text(subtitles(lid, lang, starts, speed), encoding="utf-8")
    print(f"{comp}_{lang}.m4a + .srt")


def pack(lid, langs):
    comp = COMP[lid]
    out = ROOT / "out/dub"
    final = ROOT / "final/dub"
    final.mkdir(parents=True, exist_ok=True)
    args, maps, meta = ["-i", str(out / f"{comp}_video.mp4")], ["-map", "0:v"], []
    for n, lang in enumerate(langs):
        args += ["-i", str(out / f"{comp}_{lang}.m4a")]
    for n, lang in enumerate(langs):
        args += ["-i", str(out / f"{comp}_{lang}.srt")]
    for n, lang in enumerate(langs):
        code = LANG3.get(lang, lang)
        maps += ["-map", f"{1 + n}:a"]
        meta += [f"-metadata:s:a:{n}", f"language={code}", f"-metadata:s:s:{n}", f"language={code}"]
    for n in range(len(langs)):
        maps += ["-map", f"{1 + len(langs) + n}:s"]
    dst = final / f"{comp}.mp4"
    ff(*args, *maps, "-c:v", "copy", "-c:a", "copy", "-c:s", "mov_text", *meta,
       "-disposition:a:0", "default", "-disposition:s:0", "0", str(dst))
    files = [dst] + [out / f"{comp}_{lang}{ext}" for lang in langs for ext in (".m4a", ".srt")]
    DRIVE.mkdir(parents=True, exist_ok=True)
    for f in files:
        shutil.copy2(f, final / f.name) if f.parent != final else None
        shutil.copy2(f, DRIVE / f.name)
    print(f"wrote final/dub/{comp}.mp4 ({dst.stat().st_size / 1e6:.0f} MB, tracks {' '.join(langs)}) + Drive")


if __name__ == "__main__":
    cmd, lid, *langs = sys.argv[1:]
    if cmd == "fit":
        fit(lid, langs[0])
    elif cmd == "track":
        track(lid, langs[0])
    elif cmd == "pack":
        pack(lid, langs)
    elif cmd == "all":
        for lang in langs:
            fit(lid, lang)
            track(lid, lang)
        pack(lid, langs)
