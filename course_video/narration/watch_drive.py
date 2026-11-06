"""Drive watcher: turns finished Colab clone batches into final lesson videos.

Colab (colab_clone_drive.ipynb) writes cloned clips to
  G:/My Drive/FFIQ_voice/output/<lesson>/*.wav  + _DONE.json when complete.
This watcher picks each finished batch up and, unattended:
  1. quality gate: engine is F5, cloned from the approved voice_reference_A.wav,
     not XTTS (full-scale peaks), tone close to voice A, natural pace
  2. imports the clips (loudness match + caption sync to real pauses)
  3. npm run check
  4. renders the MP4 + SRT and copies them to FFIQ_voice/final/
  5. keeps FFIQ_voice/status.txt and watcher.log up to date (readable on a phone)

A batch that fails the gate is HELD (output/<lesson>/_HELD.json says why) and
nothing is imported. A failure later on is marked _FAILED.json. Delete that
file to retry, or use --force to accept a held batch. A lesson that failed in
Colab itself (output/<lesson>/_ERROR.json, no _DONE.json) is shown as FAILED
with the clip and error; the next successful Colab run clears it.

  python narration/watch_drive.py              watch forever (checks every 60 s)
  python narration/watch_drive.py --once       process what's ready, then exit
  python narration/watch_drive.py --force <lesson>   skip the gate for one lesson
"""
import ctypes
import datetime
import hashlib
import importlib
import json
import re
import shutil
import subprocess
import sys
import time
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lesson_lib  # noqa: E402

ROOT = lesson_lib.ROOT
BASE = Path(r"G:/My Drive/FFIQ_voice")
OUTPUT, FINAL = BASE / "output", BASE / "final"
STATUS, LOG = BASE / "status.txt", BASE / "watcher.log"
STATE = ROOT / "out" / "watch_state.json"

APPROVED_VOICE_MD5 = "b57f89e392e2f589bdfd0eacfba8c443"   # voice_reference_A.wav
MAX_BRIGHTNESS_HZ = 1050      # voice A ~930 Hz; raw-recording clone ~1110 Hz
PACE_WPM = (85, 180)          # outside this, a clip probably repeated/skipped words
POLL_SECONDS = 60


# ---------------------------------------------------------------- reporting
def log(msg: str) -> None:
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}  {msg}"
    print(line, flush=True)
    try:
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass


def set_status(lesson: str, state: str, detail: str = "") -> None:
    """Remember each lesson's state and rewrite the human-readable status.txt."""
    data = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    data[lesson] = {"state": state, "detail": detail,
                    "updated": f"{datetime.datetime.now():%d %b %H:%M}"}
    STATE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    icon = {"DONE": "✅", "HELD": "⚠️", "FAILED": "❌"}.get
    lines = [f"FFIQ lesson pipeline - updated {datetime.datetime.now():%d %b %Y %H:%M}", ""]
    for name, s in sorted(data.items(), key=lambda kv: kv[1]["updated"], reverse=True):
        lines.append(f"{icon(s['state'], '⏳')} {name}: {s['state']}  ({s['updated']})")
        if s["detail"]:
            lines.append(f"    {s['detail']}")
    try:
        STATUS.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError:
        pass
    log(f"{lesson}: {state} {detail}")


def keep_awake(on: bool) -> None:
    """Stop Windows idle-sleeping while a lesson renders (no settings change)."""
    # Display too: on Modern Standby laptops, the screen timing out puts the
    # whole PC into standby and suspends the render (seen 24 Oct, events 506/507).
    ES_CONTINUOUS, ES_SYSTEM_REQUIRED, ES_DISPLAY_REQUIRED = 0x80000000, 0x00000001, 0x00000002
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | (ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED if on else 0))
    except AttributeError:
        pass  # not Windows


# ---------------------------------------------------------------- checks
def _mono(path: Path, seconds: float = 60) -> "np.ndarray":
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-t", str(seconds), "-i", str(path),
                          "-ac", "1", "-ar", "24000", "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def brightness(paths) -> float:
    """Spectral centroid (Hz) of the clips: voice A ~930, a thin/bright clone ~1110."""
    import numpy as np
    x = np.concatenate([_mono(p) for p in paths])
    spec = np.abs(np.fft.rfft(x)) ** 2
    freqs = np.fft.rfftfreq(len(x), 1 / 24000)
    return float((spec * freqs).sum() / spec.sum())


def quality_gate(batch: Path, mod, done: dict) -> list:
    problems = []
    scenes = dict(lesson_lib.scenes(mod))
    missing = [k for k in scenes if not (batch / f"{k}.wav").exists()]
    if missing:
        return [f"missing clips: {', '.join(missing)}"]
    if done.get("engine") != "f5":
        problems.append(f"engine was {done.get('engine')!r}, not F5")
    if done.get("voice_md5") != APPROVED_VOICE_MD5:
        problems.append(f"not cloned from voice_reference_A.wav (got {done.get('voice')})")
    peaks = [lesson_lib.loudness(batch / f"{k}.wav")[1] for k in scenes]
    if sum(p > -0.1 for p in peaks) > len(peaks) / 2:
        problems.append("most clips peak at full scale: this is the XTTS voice, not F5")
    pages = sorted(k for k in scenes if re.fullmatch(r"p\d+", k))[:4]
    b = brightness([batch / f"{k}.wav" for k in pages])
    if b > MAX_BRIGHTNESS_HZ:
        problems.append(f"tone too bright for voice A ({b:.0f} Hz, max {MAX_BRIGHTNESS_HZ})")
    for k, text in scenes.items():
        wpm = len(text.split()) / lesson_lib.dur(batch / f"{k}.wav") * 60
        if not PACE_WPM[0] <= wpm <= PACE_WPM[1]:
            problems.append(f"{k}: unusual pace {wpm:.0f} wpm (repeated or skipped words?)")
    return problems


def composition(mod) -> str:
    """Composition name for a lesson module, from scripts/lessons.ts."""
    src = (ROOT / "scripts" / "lessons.ts").read_text(encoding="utf-8")
    m = re.search(rf'\b{re.escape(mod.ID)}:\s*"(\w+)"', src)
    if not m:
        raise RuntimeError(f"lesson id {mod.ID!r} is not registered in scripts/lessons.ts")
    return m.group(1)


def run(cmd: list, log_name: str) -> None:
    with open(ROOT / "out" / log_name, "w", encoding="utf-8") as fh:
        res = subprocess.run(cmd, cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
    if res.returncode:
        tail = (ROOT / "out" / log_name).read_text(encoding="utf-8", errors="replace")[-600:]
        raise RuntimeError(f"{' '.join(cmd[:3])} failed (exit {res.returncode}): {tail.strip()}")


# ---------------------------------------------------------------- pipeline
def process(batch: Path, force: bool = False) -> None:
    name = batch.name
    if not (HERE / f"{name}.py").exists():
        (batch / "_HELD.json").write_text(json.dumps({"problems": [f"no narration/{name}.py"]}))
        set_status(name, "HELD", f"no lesson module narration/{name}.py")
        return
    # reload: a script fixed and re-queued while the watcher runs must not be stale
    mod = importlib.reload(sys.modules[name]) if name in sys.modules else importlib.import_module(name)
    done =json.loads((batch / "_DONE.json").read_text(encoding="utf-8"))

    set_status(name, "CHECKING", "quality gate")
    problems = [] if force else quality_gate(batch, mod, done)
    if problems:
        (batch / "_HELD.json").write_text(json.dumps({"problems": problems}, indent=2))
        set_status(name, "HELD", "; ".join(problems))
        return

    comp = composition(mod)
    slug = name.replace("_", "-")
    keep_awake(True)
    try:
        set_status(name, "IMPORTING", "loudness match + caption sync")
        lesson_lib.import_clones(mod, batch)
        set_status(name, "CHECKING", "npm run check")
        run(["npm.cmd", "run", "-s", "check"], "watch_check.log")
        run(["node", "--disable-warning=MODULE_TYPELESS_PACKAGE_JSON", "scripts/srt.ts", mod.ID],
            "watch_srt.log")
        for attempt in (1, 2):
            set_status(name, "RENDERING", f"{comp} (attempt {attempt}, ~35 min)")
            try:
                run(["npx.cmd", "remotion", "render", comp, f"out/{slug}.mp4", "--log=error"],
                    f"render_{mod.ID}.log")
                break
            except RuntimeError:
                if attempt == 2:
                    raise
                log(f"{name}: render failed, retrying once")
        FINAL.mkdir(exist_ok=True)
        shutil.copy(ROOT / "out" / f"{slug}.mp4", FINAL / f"{comp}.mp4")
        shutil.copy(ROOT / "out" / f"{comp}.srt", FINAL / f"{comp}.srt")
        mins = lesson_lib.dur(ROOT / "out" / f"{slug}.mp4") / 60
        (batch / "_IMPORTED.json").write_text(json.dumps(
            {"finished": datetime.datetime.now().isoformat(timespec="seconds"),
             "video": f"final/{comp}.mp4", "minutes": round(mins, 1)}, indent=2))
        set_status(name, "DONE", f"final/{comp}.mp4 ({mins:.1f} min) + .srt")
    except Exception as exc:  # noqa: BLE001 - report every failure in status.txt
        (batch / "_FAILED.json").write_text(json.dumps(
            {"error": str(exc), "trace": traceback.format_exc()}, indent=2))
        set_status(name, "FAILED", str(exc)[:300])
    finally:
        keep_awake(False)


def report_clone_errors() -> None:
    """Show Colab-side failures (output/<lesson>/_ERROR.json) in status.txt, once each."""
    if not OUTPUT.exists():
        return
    known = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    for d in OUTPUT.iterdir():
        err = d / "_ERROR.json"
        if not d.is_dir() or not err.exists() or (d / "_DONE.json").exists():
            continue
        e = json.loads(err.read_text(encoding="utf-8"))
        detail = f"clone error in Colab at clip {e.get('clip')}: {e.get('error', '')[:200]}"
        if known.get(d.name, {}).get("detail") != detail:
            set_status(d.name, "FAILED", detail)


def ready():
    if not OUTPUT.exists():
        return []
    return [d for d in sorted(OUTPUT.iterdir())
            if d.is_dir() and not d.name.startswith("_")
            and (d / "_DONE.json").exists()
            and not any((d / m).exists() for m in ("_IMPORTED.json", "_HELD.json", "_FAILED.json"))]


def main():
    args = sys.argv[1:]
    if "--force" in args:
        name = args[args.index("--force") + 1]
        batch = OUTPUT / name
        for marker in ("_HELD.json", "_FAILED.json"):
            (batch / marker).unlink(missing_ok=True)
        process(batch, force=True)
        return
    log(f"watcher started, watching {OUTPUT}")
    while True:
        report_clone_errors()
        for batch in ready():
            process(batch)
        if "--once" in args:
            break
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
