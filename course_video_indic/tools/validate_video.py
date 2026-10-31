"""Check one finished lesson video before it goes to final/ (Gate 4 in docs/WORKPLAN.md).

  python tools/validate_video.py <id> <video.mp4> [<video.srt>]

Checks: length matches the planned timeline, loudness -14 LUFS, true peak, no long
silence, .srt present and inside the video. Also saves one frame per page/quiz as a
contact sheet in out/check/<Comp>_sheet.jpg for a by-eye check. Exit code 1 on any FAIL.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LUFS, LUFS_TOL = -14.0, 1.5
MAX_TRUE_PEAK = -1.0
LEN_TOL = 1.5          # seconds
MAX_SILENCE = 8.0      # seconds (the quiz think time has the music bed, so real gaps are a fault)


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def main(id_, mp4, srt=None):
    mp4 = Path(mp4)
    srt = Path(srt) if srt else mp4.with_suffix(".srt")
    fails, notes = [], []

    p = run("node", "--disable-warning=MODULE_TYPELESS_PACKAGE_JSON", str(ROOT / "scripts" / "plan_json.ts"), id_)
    if p.returncode:
        sys.exit(f"FAIL  cannot read lesson plan: {p.stderr.strip()}")
    plan = json.loads(p.stdout)
    if not mp4.exists():
        sys.exit(f"FAIL  {mp4} not found")

    dur = float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp4)).stdout)
    if abs(dur - plan["total"]) > LEN_TOL:
        fails.append(f"length {dur:.1f}s, planned {plan['total']:.1f}s")
    notes.append(f"length {dur / 60:.1f} min (planned {plan['total'] / 60:.1f})")

    a = run("ffmpeg", "-hide_banner", "-nostats", "-i", str(mp4), "-vn",
            "-af", f"ebur128=peak=true,silencedetect=n=-50dB:d={MAX_SILENCE}", "-f", "null", "-").stderr
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", a)
    tp = re.findall(r"Peak:\s+(-?[\d.]+|-inf) dBFS", a)
    lufs = float(i[-1]) if i else None
    peak = float(tp[-1]) if tp and tp[-1] != "-inf" else None
    if lufs is None or abs(lufs - LUFS) > LUFS_TOL:
        fails.append(f"loudness {lufs} LUFS (want {LUFS}±{LUFS_TOL})")
    if peak is not None and peak > MAX_TRUE_PEAK:
        fails.append(f"true peak {peak} dBTP (max {MAX_TRUE_PEAK})")
    gaps = re.findall(r"silence_duration: ([\d.]+)", a)
    if gaps:
        fails.append(f"{len(gaps)} silent gap(s) over {MAX_SILENCE:.0f}s")
    notes.append(f"loudness {lufs} LUFS, peak {peak} dBTP")

    if not srt.exists():
        fails.append(f"no captions file {srt.name}")
    else:
        stamps = re.findall(r"--> (\d+):(\d+):(\d+),(\d+)", srt.read_text(encoding="utf-8"))
        if len(stamps) < plan["clips"]:
            fails.append(f"only {len(stamps)} caption lines for {plan['clips']} clips")
        if stamps:
            h, m, s, ms = map(int, stamps[-1])
            if h * 3600 + m * 60 + s + ms / 1000 > dur + 0.5:
                fails.append("last caption runs past the end of the video")
        notes.append(f"{len(stamps)} caption lines")

    # one frame per page / quiz (70% in, after the boxes have animated) -> contact sheet
    check = ROOT / "out" / "check" / plan["comp"]
    shutil.rmtree(check, ignore_errors=True)
    check.mkdir(parents=True)
    shots = [b for b in plan["blocks"] if b["kind"] in ("page", "quiz")]
    for n, b in enumerate(shots):
        t = b["start"] + b["dur"] * 0.7
        run("ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(mp4), "-frames:v", "1",
            "-vf", "scale=640:-1", str(check / f"{n:02d}.jpg"))
    (check / "keys.txt").write_text("\n".join(f"{n:02d} {b['key']}" for n, b in enumerate(shots)), encoding="utf-8")
    got = len(list(check.glob("*.jpg")))
    if got != len(shots):
        fails.append(f"only {got} of {len(shots)} page frames could be read")
    sheet = check.parent / f"{plan['comp']}_sheet.jpg"
    run("ffmpeg", "-v", "error", "-y", "-start_number", "0", "-i", str(check / "%02d.jpg"),
        "-vf", "tile=4x5:padding=4", "-frames:v", "1", str(sheet))
    notes.append(f"{got} page frames in {check.relative_to(ROOT)}")

    for n in notes:
        print(f"  ok    {n}")
    for f in fails:
        print(f"  FAIL  {f}")
    print(f"{'FAIL' if fails else 'PASS'}  {plan['comp']}")
    return 1 if fails else 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:4]))
