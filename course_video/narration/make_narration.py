"""Generate per-scene narration for the short 8 Wastes lesson with Edge TTS,
AND capture word-level timings (for synced captions).

Outputs, per scene, into course_video/public/audio/:
  <scene>.mp3            the narration audio
  <scene>.words.json     [{"w": word, "s": start_sec, "e": end_sec}, ...]
"""
import asyncio
import json
from pathlib import Path

import edge_tts

VOICE = "en-US-ChristopherNeural"
RATE = "-6%"

OUT = Path(__file__).resolve().parent.parent / "public" / "audio"
OUT.mkdir(parents=True, exist_ok=True)

SCENES = {
    "01_title": (
        "In this lesson, we'll uncover the eight wastes of lean. "
        "These are the hidden losses that quietly drain time, money and effort "
        "from every process. And you can remember all of them with one simple "
        "word. Downtime."
    ),
    "02_acronym": (
        "Downtime. Each letter stands for one of the eight wastes. "
        "Learn this one word, and you'll never forget them."
    ),
    "03_flow": (
        "Waste isn't always obvious. On an ordinary production line, "
        "a part sits waiting between steps, and inventory quietly piles up. "
        "These are losses that most people walk right past every single day."
    ),
    "04_grid": (
        "So here they are. Defects. Overproduction. Waiting. "
        "Non-utilized talent. Transportation. Inventory. Motion. "
        "And extra processing."
    ),
    "05_outro": (
        "Your job as a lean thinker is simple. Spot the waste, and remove the waste. "
        "In the next lesson, we'll explore the five S system."
    ),
}


async def gen():
    for name, text in SCENES.items():
        mp3 = OUT / f"{name}.mp3"
        words = []
        comm = edge_tts.Communicate(text, VOICE, rate=RATE, boundary="WordBoundary")
        with open(mp3, "wb") as fh:
            async for chunk in comm.stream():
                if chunk["type"] == "audio":
                    fh.write(chunk["data"])
                elif chunk["type"] == "WordBoundary":
                    s = chunk["offset"] / 1e7  # 100ns units -> seconds
                    e = s + chunk["duration"] / 1e7
                    words.append({"w": chunk["text"], "s": round(s, 3), "e": round(e, 3)})
        (OUT / f"{name}.words.json").write_text(
            json.dumps(words, ensure_ascii=False), encoding="utf-8")
        print(f"  wrote {mp3.name} (+{len(words)} word timings)")
    print("Narration + word timings done ->", OUT)


if __name__ == "__main__":
    asyncio.run(gen())
