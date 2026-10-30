# 🤖 Automated lesson pipeline (Google Drive)

How a lesson goes from script to finished video with almost no manual steps.
Written for the course owner; the technical details are in `PLAYBOOK.md` §6a.

```
YOU                         GOOGLE DRIVE  (G:\My Drive\FFIQ_voice)         YOUR PC
───                         ──────────────────────────────────────         ───────
"Make lessons X, Y"   →                                               →   Claude writes scripts,
                            input/x.json   ←─────────────────────────────  checks, previews
Colab: Run all        →     output/x/*.wav + _DONE.json
(1 click)                                │ syncs down automatically
                                         ▼
                            watcher sees _DONE  →  quality check, import, caption
                                                   sync, render
                            final/X.mp4 + X.srt  ←──────────────────────  finished video
Watch on PC or phone  ←     status.txt (progress)
```

---

## One-time setup (done on 23 Oct 2026)
1. **Google Drive for desktop** installed, signed in with the same Google
   account used in Colab, "Stream files" mode → Drive appears as `G:`.
2. Folder **`G:\My Drive\FFIQ_voice`** with `input`, `output`, `final` inside.
3. Right-click `FFIQ_voice` → **Offline access → Available offline**.
4. **`voice_reference_A.wav`** (the approved course voice) copied into
   `FFIQ_voice`. Don't replace or rename it: the watcher checks its fingerprint.

## The folder

| Path | What it is |
|---|---|
| `voice_reference_A.wav` | the course voice. Never change it. |
| `input/` | lessons waiting to be cloned. Claude puts the `.json` files here. |
| `input/done/` | lessons Colab has finished. |
| `output/<lesson>/` | cloned clips, saved one by one. `_DONE.json` = lesson complete. |
| `output/_archive/` | older clones, kept when a lesson is cloned again. |
| `final/` | **finished videos** (`.mp4`) and subtitles (`.srt`). |
| `status.txt` | current state of every lesson. Open it on your phone. |
| `watcher.log` | detailed history, for troubleshooting. |

## Your routine for new lessons
1. Tell Claude the lesson topics (or give the PPT). Claude writes the scripts,
   checks them, and puts the clone files in `input/`.
2. Open the clone notebook in Colab:
   **https://colab.research.google.com/github/PrashantRMarathe/voice-replacer/blob/add-course-video/colab_clone_drive.ipynb**
3. **Runtime → Change runtime type → T4 GPU → Save**, then **Runtime → Run all**.
   Click **Allow** when Colab asks for Google Drive.
4. Wait. Colab clones every lesson in `input/` (~15–25 min each). The watcher
   then checks, imports and renders each one (~35 min each).
5. Watch the finished video in **`final/`**.

Several lessons can go through in one Colab run: everything in `input/` is done.

## If Colab stops or errors halfway (nothing is wasted)
Say `input/` has 10 lessons, 8 finish and lesson 9 hits an error:
- **Lessons 1–8 are safe.** Each finished lesson gets `_DONE.json` and moves to
  `input/done/` immediately, and the watcher starts rendering it right away (it
  doesn't wait for the whole Colab run).
- **Lesson 9's finished clips are saved** in `output/lesson9/`; nothing is
  imported until the lesson is complete.
- **A disconnect / stuck Colab:** just **Run all** again. Finished lessons are
  skipped and lesson 9 continues from its next missing clip.
- **An error in the lesson itself** (e.g. a sentence the voice engine can't
  handle): Colab records it in `output/lesson9/_ERROR.json`, **skips to lesson
  10**, and finishes the rest. `status.txt` shows ❌ lesson9 with the clip and
  error. Claude fixes the script and puts it back in `input/`; the next Run all
  finishes it and clears the error.
- **Colab stopped right after a lesson finished** (before moving its file):
  Run all recognises the finished lesson and just moves it to `done/`.

## Reading status.txt

| Shows | Meaning |
|---|---|
| ⏳ WAITING | in `input/`, waiting for Colab |
| ⏳ CHECKING / IMPORTING / RENDERING | the watcher is working on it |
| ✅ DONE | the video is in `final/` |
| ⚠️ HELD | the quality check refused the clones; the reason is shown. Nothing was changed. |
| ❌ FAILED | something broke during import or render; the reason is shown |

## What the quality check refuses (and why)
- **Not the F5 engine**, or clips that peak at full volume: that is the harsh
  XTTS voice (the Oct 21–22 problem).
- **Not cloned from `voice_reference_A.wav`**.
- **Tone too bright** (above 1050 Hz): sounds like a clone of the raw recording,
  not the approved voice.
- **Odd pace** in a clip (under 85 or over 180 words a minute): the voice
  probably repeated or skipped words.

A held lesson is never imported, so a wrong voice can't reach a video.

## When something goes wrong

| Problem | What to do |
|---|---|
| Colab disconnects or gets stuck | **Runtime → Disconnect and delete runtime**, reconnect, **Run all** again. Finished clips are kept; it continues where it stopped. |
| Colab says "Cannot connect to GPU" | The free daily GPU time is used up. Try again in a few hours, or use Colab Pro. |
| Cell 1 shows `STOP: F5-TTS did not import` | Paste the whole message (including the package versions above it) to Claude. |
| `status.txt` shows ⚠️ HELD | Tell Claude; it reads `output/<lesson>/_HELD.json`. To clone again, Claude puts the `.json` back in `input/` and you **Run all**. |
| `status.txt` shows ❌ FAILED "clone error in Colab" | That lesson broke in Colab; the others carried on. Tell Claude: it reads `output/<lesson>/_ERROR.json`, fixes the script and re-queues it. |
| `status.txt` shows ❌ FAILED (import/render) | Tell Claude. After the fix, deleting `output/<lesson>/_FAILED.json` makes the watcher retry. |
| Nothing happens after Colab finished | The watcher only runs while Claude's session and the PC are on. Ask Claude to start it. |
| Render stopped overnight | The PC slept or the lid was closed. The watcher keeps the PC awake while rendering, but a closed lid still sleeps. |

## Limits today
- The watcher runs inside a Claude Code session, so that session and the PC must
  be on. (Next step: start it automatically when the PC boots.)
- Colab still needs one click (**Run all**): the free tier can't be started
  automatically. Colab Pro+ or a paid cloud GPU could remove even that.
