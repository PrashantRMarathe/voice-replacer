"""Re-voice ONLY the clips whose spoken text changed, then level + caption-sync them.

  python tools/revoice.py gemba_hi qrqc_hi ...      # or: all_hi
  python tools/revoice.py gemba_hi --dry            # just list what would change

What the voice last said is kept in public/audio/<id>/spoken.json. A lesson without
that file yet (voiced before this tool existed) counts a clip as changed only when it
contains a word from narration/pronounce.py; every other clip is taken as current.
"""
import importlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "narration"))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
dry = "--dry" in sys.argv
if not args:
    sys.exit(__doc__)
if args == ["all_hi"]:
    args = sorted(p.stem for p in (ROOT / "narration").glob("*_hi.py"))

for name in args:
    mod = importlib.import_module(name)
    audio, _, _ = lesson_lib.paths(mod)
    manifest = audio / "spoken.json"
    said = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else None
    pron = pronounce.PRON.get(getattr(mod, "LANG", ""), {})
    now, changed = {}, []
    for key, text in lesson_lib.scenes(mod):
        now[key] = lesson_lib.say(mod, text)
        mp3 = audio / f"{key}.mp3"
        if not mp3.exists():
            changed.append(key)
        elif said is None:
            if any(w in text for w in pron):
                changed.append(key)
        elif said.get(key) != now[key]:
            changed.append(key)
    print(f"{name}: {len(changed)} clip(s) to re-voice {changed}")
    if dry:
        continue
    if changed:
        for key in changed:
            (audio / f"{key}.mp3").unlink(missing_ok=True)
        lesson_lib.bootstrap(mod, force=False)          # voices just the missing clips
        wavs = ROOT / "out" / f"revoice_{mod.ID}"
        wavs.mkdir(parents=True, exist_ok=True)
        for old in wavs.glob("*.wav"):
            old.unlink()
        for key in changed:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(audio / f"{key}.mp3"),
                            "-ar", "24000", "-ac", "1", str(wavs / f"{key}.wav")], check=True)
        lesson_lib.import_clones(mod, wavs)             # level to -29 LUFS + sync captions
    manifest.write_text(json.dumps(now, ensure_ascii=False, indent=1), encoding="utf-8")
