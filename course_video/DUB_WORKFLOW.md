# Clean Dub Workflow — no Demucs needed

You now have the lesson split into clean parts, so dubbing keeps the music
perfectly and never risks losing the background.

## The files
| File | What it is |
|---|---|
| `lesson-for-dub.mp4` | The video **without burned captions** (so the dub tool can add its own, timing-correct subtitles) |
| `stems/narration.wav` | The **voice only** (clean), already aligned to the video timeline |
| `stems/background.wav` | The **music + sound effects only**, at the right levels, aligned to the timeline |

> The original captioned lesson (`lesson-with-characters.mp4`) is untouched.

## How to dub (3 steps)

**1. Make the new voice**
Feed **`narration.wav`** into your voice_replacer / dub tool (clone or translate).
You get back, say, `narration_hindi.wav`.
*(No Demucs needed — the voice is already isolated.)*

**2. Mix new voice + background**
```bash
ffmpeg -y -i narration_hindi.wav -i stems/background.wav \
  -filter_complex "[0]volume=1.0[v];[1]volume=1.0[b];[v][b]amix=inputs=2:normalize=0" \
  dubbed_audio.wav
```

**3. Put the new audio onto the video**
```bash
ffmpeg -y -i lesson-for-dub.mp4 -i dubbed_audio.wav \
  -map 0:v -map 1:a -c:v copy -shortest lesson-hindi.mp4
```

Done — a fully dubbed lesson with the **original music and SFX intact**, and no
caption mismatch. Add translated subtitles separately if you want them.

## Why this is cleaner than uploading the finished video
Uploading the mixed video makes the dub tool *guess* the voice/music split with
Demucs (can smear music, needs a GPU). Here the split is **exact**, because I
exported it before mixing. So: better quality, faster, GPU-optional.
