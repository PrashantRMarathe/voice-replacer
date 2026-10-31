"""Generate the soft UI sounds used by the demo polish layer (no license risk).
(make_sfx.py keeps the original whoosh/ding/pop set.)

  card.mp3    a card appearing (short, soft blip)
  tick.mp3    one second of a quiz countdown (wood-block click)
  sting.mp3   a quick check starting (two rising notes)
  reveal.mp3  a quiz answer revealed (soft major chord)

Output: course_video/public/audio/sfx/. Deliberately quiet; mixed low in video.
NOTE: CLAUDE.md rule 4 keeps lessons voice-only. These are used only when a
composition opts in with `polish.sound` (the PokaYokeDemo trial).
"""
import subprocess
import wave
from pathlib import Path

import numpy as np

SR = 44100
OUT = Path(__file__).resolve().parent.parent / "public" / "audio" / "sfx"
OUT.mkdir(parents=True, exist_ok=True)


def tone(freq, dur, decay, harmonics=(1.0, 0.3, 0.1)):
    t = np.arange(int(SR * dur)) / SR
    wave_ = sum(a * np.sin(2 * np.pi * freq * (i + 1) * t) for i, a in enumerate(harmonics))
    env = np.exp(-t / decay) * np.minimum(1, t / 0.004)  # 4 ms attack, no click
    return wave_ * env


def save(name, x, peak=0.5):
    x = x / np.max(np.abs(x)) * peak
    wav = OUT / f"{name}.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav), "-b:a", "128k", str(OUT / f"{name}.mp3")], check=True)
    wav.unlink()


def pad(x, dur):
    n = int(SR * dur)
    return np.concatenate([x, np.zeros(max(0, n - len(x)))])[:n]


save("card", tone(880, 0.14, 0.035, (1.0, 0.2)), peak=0.35)
save("tick", tone(1600, 0.05, 0.008, (1.0, 0.5, 0.2)), peak=0.3)
a = pad(tone(659.25, 0.35, 0.12), 0.7)
b = np.concatenate([np.zeros(int(SR * 0.12)), tone(987.77, 0.58, 0.2)])
save("sting", a + pad(b, 0.7), peak=0.45)
save("reveal", sum(pad(tone(f, 0.9, 0.3), 0.9) for f in (523.25, 659.25, 783.99)), peak=0.45)
print("wrote", sorted(p.name for p in OUT.glob("*.mp3")))
