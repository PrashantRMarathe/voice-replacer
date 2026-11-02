"""Pronunciation check BEFORE voicing a language: the lesson's voice reads every English
term and every narration/pronounce.py word in the shortest lesson sentence that uses it,
after its number, exactly as the lessons will say it (the lesson's own say()).

  python tools/say_words.py all_hi           -> out/pron_test/hi_words.mp3 + hi_words.txt
  python tools/say_words.py gemba_hi qrqc_hi

Listen, note the numbers that sound wrong, fix them in pronounce.py, run again.
"""
import asyncio
import importlib
import re
import subprocess
import sys
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "narration"))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

LATIN = r"[A-Za-z0-9][A-Za-z0-9'-]*(?: [A-Za-z][A-Za-z0-9'-]*)*"   # "SOP", "A3", "Burn Down Chart"

names = [a for a in sys.argv[1:] if not a.startswith("--")]
if not names:
    sys.exit(__doc__)
if len(names) == 1 and names[0].startswith("all_"):
    names = sorted(p.stem for p in (ROOT / "narration").glob(f"*_{names[0][4:]}.py"))
mods = [importlib.import_module(n) for n in names]
lang, voice = mods[0].LANG, mods[0].VOICE

# term -> (shortest sentence that uses it, as shown on screen / as the voice says it)
found = {}
for mod in mods:
    for _, text in lesson_lib.scenes(mod):
        for s in re.split(r"(?<=[.!?।])\s+", text.strip()):
            terms = [t for t in re.findall(LATIN, s) if re.search("[A-Za-z]", t)]
            terms += [w for w in pronounce.PRON.get(lang, {}) if w in s]
            for t in terms:
                if t not in found or len(s) < len(found[t][0]):
                    found[t] = (s, lesson_lib.say(mod, s))
items = sorted(found.items(), key=lambda kv: kv[0].lower())

out = ROOT / "out" / "pron_test"
tmp = out / f"{lang}_words"
tmp.mkdir(parents=True, exist_ok=True)


async def speak(i, text, sem):
    async with sem:
        await edge_tts.Communicate(f"{i}. {text}", voice, rate=lesson_lib.RATE).save(str(tmp / f"{i:03}.mp3"))


async def main():
    sem = asyncio.Semaphore(6)
    await asyncio.gather(*(speak(i, said, sem) for i, (_, (_, said)) in enumerate(items, 1)))

asyncio.run(main())
gap = tmp / "gap.mp3"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", "0.9", "-i", "anullsrc=r=24000:cl=mono",
                "-c:a", "libmp3lame", "-b:a", "48k", str(gap)], check=True)
(tmp / "list.txt").write_text("".join(f"file '{i:03}.mp3'\nfile 'gap.mp3'\n" for i in range(1, len(items) + 1)))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"),
                "-c:a", "libmp3lame", "-b:a", "64k", str(out / f"{lang}_words.mp3")], check=True)
with open(out / f"{lang}_words.txt", "w", encoding="utf-8") as fh:
    for i, (term, (s, said)) in enumerate(items, 1):
        fh.write(f"{i:3}  {term}\n     screen: {s}\n     voice:  {said}\n")
print(f"{len(items)} words -> {out / f'{lang}_words.mp3'}")
