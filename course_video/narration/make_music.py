"""Generate a soft, royalty-free ambient music bed (no license risk).

Creates a calm, slowly-evolving chord pad. It is deliberately quiet so it sits
under narration without competing. Output: course_video/public/audio/music.mp3
"""
import subprocess
from pathlib import Path

import numpy as np

SR = 44100
DUR = 75.0  # seconds
OUT = Path(__file__).resolve().parent.parent / "public" / "audio"
OUT.mkdir(parents=True, exist_ok=True)

t = np.linspace(0, DUR, int(SR * DUR), endpoint=False)

# A gentle progression of soft chords (frequencies in Hz), each held a while.
# Cmaj -> Amin -> Fmaj -> Gmaj feel, low and warm.
chords = [
    [130.81, 164.81, 196.00],  # C E G
    [110.00, 130.81, 164.81],  # A C E
    [87.31, 110.00, 130.81],   # F A C
    [98.00, 123.47, 146.83],   # G B D
]
seg = DUR / len(chords)

audio = np.zeros_like(t)
for i, chord in enumerate(chords):
    start, end = i * seg, (i + 1) * seg
    mask = (t >= start) & (t < end)
    local = t[mask] - start
    # smooth fade in/out of each chord so transitions are seamless
    env = np.sin(np.pi * local / seg) ** 0.6
    tone = np.zeros_like(local)
    for f in chord:
        # slight detune layers for warmth + a soft shimmer an octave up
        tone += np.sin(2 * np.pi * f * local)
        tone += 0.6 * np.sin(2 * np.pi * f * 1.003 * local)
        tone += 0.25 * np.sin(2 * np.pi * f * 2 * local)
    audio[mask] += env * tone

# slow amplitude shimmer (breathing) + gentle low-pass via moving average
lfo = 0.85 + 0.15 * np.sin(2 * np.pi * 0.05 * t)
audio *= lfo
kernel = np.ones(40) / 40
audio = np.convolve(audio, kernel, mode="same")

# normalize and keep it quiet (it's a background bed)
audio /= np.max(np.abs(audio)) + 1e-9
audio *= 0.22

# global fade in/out
fade = int(SR * 2.0)
audio[:fade] *= np.linspace(0, 1, fade)
audio[-fade:] *= np.linspace(1, 0, fade)

wav = OUT / "music.wav"
# write a simple 16-bit PCM wav
import wave
with wave.open(str(wav), "w") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((audio * 32767).astype(np.int16).tobytes())

mp3 = OUT / "music.mp3"
subprocess.run(["ffmpeg", "-y", "-i", str(wav), "-b:a", "128k", str(mp3)],
               check=True, capture_output=True)
wav.unlink(missing_ok=True)
print("Music bed ->", mp3)
