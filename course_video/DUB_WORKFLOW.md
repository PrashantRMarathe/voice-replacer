# Dub Workflow (voice-only lessons)

The **`...Dub` composition is voice-only** (no music, no SFX, even though the
normal version now has a music bed and soft sounds), so the clean narration stem
is simply the audio of the Dub composition, exactly on the video timeline.

## The files
| File | How to make it |
|---|---|
| `out/<comp>-dub.mp4` | `npx remotion render <Comp>Dub out/<comp>-dub.mp4` (no burned captions) |
| `out/<comp>-voice.wav` | `npx remotion render <Comp>Dub out/<comp>-voice.wav --codec=wav` (voice only) |
| `out/<Comp>.srt` | `npm run srt` (subtitles timed to the same timeline) |

## How to dub (2 steps)
**1. Make the new voice.** Feed `<comp>-voice.wav` to the dub tool (clone or
translate) and get back, say, `voice_hindi.wav`. No Demucs needed: the voice is
already isolated.

**2. Put the new audio onto the video.**
```bash
ffmpeg -y -i out/<comp>-dub.mp4 -i voice_hindi.wav -map 0:v -map 1:a -c:v copy -shortest lesson-hindi.mp4
```

For the standard English course you don't need this at all: the cloned voice
goes in through the clone-only pipeline (`docs/PLAYBOOK.md` §6), which keeps
every page in sync.
