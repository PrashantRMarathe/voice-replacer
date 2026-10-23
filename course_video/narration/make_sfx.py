"""Generate tiny royalty-free sound effects (no license risk):
  whoosh.mp3  - soft transition swoosh
  ding.mp3    - gentle highlight chime
  pop.mp3     - subtle reveal tick
Output: course_video/public/audio/sfx/
"""
import subprocess
import wave
from pathlib import Path

import numpy as np

SR = 44100
OUT = Path(__file__).resolve().parent.parent / "public" / "audio" / "sfx"
OUT.mkdir(parents=True, exist_ok=True)


def save(name, audio):
    audio = audio / (np.max(np.abs(audio)) + 1e-9)
    wav = OUT / f"{name}.wav"
    with wave.open(str(wav), "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((audio * 32767 * 0.7).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-y", "-i", str(wav), "-b:a", "128k",
                    str(OUT / f"{name}.mp3")], check=True, capture_output=True)
    wav.unlink(missing_ok=True)
    print("  wrote", name)


# whoosh: filtered noise with a fast swell + decay, slight pitch sweep feel
d = 0.5
t = np.linspace(0, d, int(SR * d), endpoint=False)
noise = np.random.randn(len(t))
# moving-average low-pass that opens up then closes
env = np.sin(np.pi * t / d) ** 2
k = np.ones(60) / 60
whoosh = np.convolve(noise, k, mode="same") * env
save("whoosh", whoosh)

# ding: two soft sine partials with exponential decay
d = 0.8
t = np.linspace(0, d, int(SR * d), endpoint=False)
ding = (np.sin(2 * np.pi * 880 * t) + 0.5 * np.sin(2 * np.pi * 1320 * t)) * np.exp(-5 * t)
save("ding", ding)

# pop: short soft click/tick
d = 0.12
t = np.linspace(0, d, int(SR * d), endpoint=False)
pop = np.sin(2 * np.pi * 420 * t) * np.exp(-30 * t)
save("pop", pop)

print("SFX done ->", OUT)
