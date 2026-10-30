"""Generate a soft, royalty-free ambient music bed (no license risk).

A calm, continuously-evolving chord pad. Chords CROSS-FADE (overlap-add with
Hann windows) so the audio never dips to silence between chords, and the bed is
long enough to cover a full lesson without looping. Deliberately quiet.

Output: course_video/public/audio/music.mp3
"""
import subprocess
import wave
from pathlib import Path

import numpy as np

SR = 44100
DUR = 600.0  # seconds (covers lessons up to ~10 min with no looping)
OUT = Path(__file__).resolve().parent.parent / "public" / "audio"
OUT.mkdir(parents=True, exist_ok=True)

# Gentle progression (low, warm): Cmaj -> Amin -> Fmaj -> Gmaj feel.
chords = [
    [130.81, 164.81, 196.00],  # C E G
    [110.00, 130.81, 164.81],  # A C E
    [87.31, 110.00, 130.81],   # F A C
    [98.00, 123.47, 146.83],   # G B D
]

hop = 16.0            # seconds between chord changes
win_len = 2 * hop     # each chord window (50% overlap -> Hann windows sum to ~1)
L = int(SR * win_len)
hann = np.sin(np.pi * np.arange(L) / L) ** 2   # smooth, sums to 1 at 50% overlap
local = np.arange(L) / SR

n_total = int(SR * DUR)
audio = np.zeros(n_total + L, dtype=np.float32)

nseg = int(np.ceil(DUR / hop)) + 1
for i in range(nseg):
    chord = chords[i % len(chords)]
    tone = np.zeros(L, dtype=np.float32)
    for f in chord:
        tone += np.sin(2 * np.pi * f * local)
        tone += 0.6 * np.sin(2 * np.pi * f * 1.003 * local)   # detune warmth
        tone += 0.25 * np.sin(2 * np.pi * f * 2 * local)      # soft octave shimmer
    start = int(i * hop * SR)
    end = start + L
    if start >= len(audio):
        break
    seg = (hann * tone)[: len(audio) - start]
    audio[start:start + len(seg)] += seg

audio = audio[:n_total]

# slow breathing + gentle low-pass smoothing
t = np.arange(n_total) / SR
audio *= (0.9 + 0.1 * np.sin(2 * np.pi * 0.04 * t)).astype(np.float32)
k = np.ones(40, dtype=np.float32) / 40
audio = np.convolve(audio, k, mode="same")

# normalize, keep quiet, and fade only at the very start/end
audio /= (np.max(np.abs(audio)) + 1e-9)
audio *= 0.9
fade = int(SR * 2.0)
audio[:fade] *= np.linspace(0, 1, fade)
audio[-fade:] *= np.linspace(1, 0, fade)

wav = OUT / "music.wav"
with wave.open(str(wav), "w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((audio * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-y", "-i", str(wav), "-b:a", "128k", str(OUT / "music.mp3")],
               check=True, capture_output=True)
wav.unlink(missing_ok=True)
print(f"Music bed -> {OUT / 'music.mp3'}  ({DUR:.0f}s, continuous)")
