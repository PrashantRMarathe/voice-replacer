# 🎙️ Course voice: standard, checks and history

The voice is the most sensitive part of the course. This file records the
approved setup, how to check a batch, and what went wrong before, so it never
has to be rediscovered.

## The approved setup (23 Oct 2026)

| Item | Value | Why |
|---|---|---|
| Engine | **F5-TTS 1.1.22**, locked in the notebooks | the version that made the approved voice |
| Voice clip | **`voice_reference_A.wav`** (md5 `b57f89e392e2f589bdfd0eacfba8c443`) | 11.2 s of the approved Oct 19 voice |
| Where | `G:\My Drive\FFIQ_voice\`, `course_video/out/voice_reference/`, Desktop `audio/` | |
| Loudness after import | −29 LUFS, peaks ≤ −3 dB (gain only) | matches the approved voice |
| Random seed | **`F5_SEED = 1019`** in `config.py` | same text → same delivery on every run (from 23 Oct) |
| Pronunciations | PLAYBOOK §4b rule 12 table | |

`voice_reference_A.wav` was cut from `course_video/out/zero-defects-perfect.mp4`
(start 24.35 s, length 11.2 s, mono 24 kHz, no processing): clean speech with
real silence between sentences and no music. 11 s is the right length: F5 uses
only ~12 s of any reference.

## What a good batch measures like

| Measure | Good (voice A) | Too bright (raw-recording clone) | Harsh (XTTS) |
|---|---|---|---|
| Loudness of raw clips | −27 to −32 LUFS | about −29 | about −17 |
| Peaks | −6 to −13 dB | −6 to −11 dB | **exactly 0 dB (32767) on every clip** |
| Brightness (spectral centroid) | **~900 Hz** (A: 930) | ~1110 Hz | n/a |
| Pace | 99–138 wpm | similar | similar |

The watcher (`narration/watch_drive.py`) checks all of this automatically and
holds any batch that doesn't match.

## History: what went wrong and the fix

1. **Oct 19:** good voice. F5 cloned from `reference_30s.mp3` (the user's own
   30 s recording, −29 LUFS). This is the sound the user approved ("A").
2. **Oct 21–22:** voice became loud, clipped, "spiky" and different. The cause
   was not the clip and not our code: Colab installed `f5-tts` in a separate
   `pip` call, which upgraded `transformers` to v5. That can't import with the
   installed `huggingface_hub` (`cannot import name 'is_offline_mode'`), so F5
   never loaded. The notebook hid the error (`2>/dev/null || print('skipped')`)
   and `tts.py` silently fell back to **XTTS**, a different voice that saves at
   full scale.
   *Proof:* every clip peaked at exactly 32767.
   *Fix:* one `pip` call that keeps `transformers<5` for both engines; the
   notebooks stop with the real error if F5 doesn't import, and refuse to clone
   if the engine isn't F5.
   *Wrong turns first:* I blamed a different voice clip, then an F5 loudness
   bug, before the 32767 peaks showed it was XTTS.
3. **Oct 22:** with F5 working again (1.1.22), cloning from `reference_30s.mp3`
   gave a correct but **brighter, thinner** voice ("E", 1137 Hz vs A's 930 Hz):
   1.1.22 copies the raw recording more literally than the Oct 19 version did.
   EQ on E got closer but wasn't the same.
4. **Oct 23:** cloning from 11 s of voice A itself (`voice_reference_A.wav`)
   reproduced it (895 Hz). The user approved it: "I sounds like the old video".
   F5 was locked to 1.1.22.

## Safety nets now in place
- **Notebooks:** one `pip` call, `f5-tts==1.1.22`, stop if F5 doesn't import,
  stop if the engine isn't F5, print the F5 version.
- **`tts.py`:** the F5 backend rescales output to the reference loudness and
  caps peaks before writing (guards against any F5 level change).
- **Fixed seed (`config.F5_SEED`):** re-cloning the same text gives the same
  emphasis and pauses. Batches cloned before 23 Oct used random seeds.
- **Import (`lesson_lib.py`):** every clip set to −29 LUFS, peaks ≤ −3 dB.
- **Watcher quality gate:** engine, voice md5, full-scale peaks, brightness,
  pace. A failing batch is held, never imported.

## Changing the voice on purpose
Only if the user asks. Change one thing at a time (engine version OR voice
clip), clone 2 pages first (a test `.json` with `p01` and `p03`), and compare
level-matched samples against voice A before cloning whole lessons. Update the
md5 and brightness limit in `watch_drive.py` and this file.
