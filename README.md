# Voice Replacer — Monika Edition

Replace the audio in a video with a **cloned AI voice** that speaks the same
words. Upload an MP4, transcribe the original audio with Whisper, edit the
transcript for 100% accuracy, then regenerate the speech in a cloned voice
(Coqui XTTS v2) and merge it back over the original video — all through a local
Gradio web UI.

```
Upload MP4  ->  Transcribe (Whisper)  ->  Edit transcript  ->
Generate cloned voice (XTTS v2)  ->  Merge with video  ->  Download MP4
```

## Features

- **AI dubbing (translation)** — auto-detect the spoken language, then dub the
  video into any of the 17 languages XTTS v2 supports, **in the original
  speaker's cloned voice**. Pick a *target* language and each line is translated
  and re-spoken; leave it on "Keep original" for same-language voice replacement.
  Translation is free and keyless (Google with automatic MyMemory fallback;
  optional fully-offline `argos` backend).
- **Multi-speaker (optional)** — detect multiple speakers (pyannote) and clone
  **each one separately**, using a reference clip auto-extracted from that
  speaker's own longest turns in the video — no manual per-speaker uploads. Off
  by default; falls back to single-speaker cloning if not set up.
- **Lip-sync (optional)** — re-animate the speaker's mouth to match the new
  voice with Wav2Lip, so dubbed videos look native instead of mouthing the old
  words. Off by default; set up once (see below). If it isn't configured or no
  face is found, the app falls back to plain audio replacement automatically.
- **UI, CLI, and REST API** — use the Gradio web UI, batch-process folders from
  the command line (`cli.py`), or run it as a background-job HTTP service
  (`api.py`). All three share one headless pipeline (`core.py`).
- **Keep background music/SFX (optional)** — instead of wiping the original
  audio, split it with AI (Demucs) into voice vs. music, keep the isolated clean
  music/SFX, and lay the cloned voice over it. Enable with `PRESERVE_BACKGROUND`
  (`pip install demucs`).
- **Auto subtitles** — writes timed `.srt` / `.vtt` files next to the output
  video from the transcript (`GENERATE_SUBTITLES`, `SUBTITLE_FORMAT`).
- **Editable transcript step** — fix Whisper mistakes before synthesis.
- **Timing preservation + anti-drift** — audio is generated per-segment using
  the original timestamps, and each synthesized segment is time-stretched
  (pitch-preserving) to match its original time slot. Because every segment is
  re-anchored to where it starts in the source video, timing differences never
  accumulate, so the audio stays in sync with a long video instead of drifting.
  Tunable via `FIT_SEGMENT_TIMING` / `MAX_TEMPO` in `config.py`.
- **Pluggable voice engine** — **XTTS v2** by default (17 languages, best for
  dubbing, but non-commercial license). Switch to **F5-TTS** (MIT / commercially
  usable, mainly English/Chinese) by installing `f5-tts` and setting
  `TTS_BACKEND = "f5"` in `config.py` — no other code changes. The active engine
  and its license are shown at the top of the UI.
- **Fast transcription** — uses **faster-whisper** (CTranslate2) by default:
  roughly 4× faster and lighter on memory than reference Whisper, with automatic
  fallback to `openai-whisper` if faster-whisper isn't installed.
- **GPU auto-detect** — uses CUDA if available, otherwise falls back to CPU.
- **Progress feedback** — a status log shows each step and elapsed time.
- **Robust error handling** — failures surface in the UI instead of crashing.
- **Idempotent temp files** — each run uses a unique id, so parallel runs never
  clash, and temp files are cleaned up on success.

## Project structure

```
voice_replacer/
├── app.py            # Gradio UI
├── cli.py            # Command-line interface (single file + --batch)
├── api.py            # FastAPI REST service (background jobs)
├── core.py           # Headless pipeline shared by UI/CLI/API
├── pipeline.py       # Core processing steps (extract/transcribe/synth/merge)
├── tts.py            # Pluggable TTS backends (XTTS / F5-TTS)
├── translate.py      # Translation for dubbing (Google/MyMemory/argos)
├── diarize.py        # Optional speaker diarization (pyannote)
├── lipsync.py        # Optional lip-sync (Wav2Lip)
├── config.py         # Paths, model settings, device, feature toggles
├── Dockerfile        # CPU container image (ffmpeg + deps baked in)
├── docker-compose.yml# `docker compose up api|ui`
├── requirements.txt
├── README.md
├── test_pipeline.py  # Smoke test
├── samples/          # Reference voice sample (you provide monika.mp3)
├── input/            # Uploaded videos
├── output/           # Final videos
└── temp/             # Intermediate files (auto-cleaned)
```

## Install

1. **Python 3.10 or 3.11** is recommended.
   > ⚠️ This project uses **`coqui-tts`** (the maintained fork of Coqui TTS),
   > not the original `TTS` package. The original `TTS` has no prebuilt Windows
   > wheel and tries to compile a C extension, which fails unless you have the
   > Microsoft C++ Build Tools installed. `coqui-tts` ships a prebuilt wheel for
   > Python 3.10/3.11 on Windows and exposes the identical `from TTS.api import
   > TTS` API and XTTS v2 model, so no code changes are needed.

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   For a CUDA build of PyTorch, install torch/torchaudio from the official
   selector at https://pytorch.org/get-started/locally/ **before** the rest.

3. Install **ffmpeg** system-wide and make sure it is on your `PATH`:
   - **Windows:** download from https://www.gyan.dev/ffmpeg/builds/, unzip, and
     add the `bin` folder to your PATH (or `winget install Gyan.FFmpeg`).
   - **macOS:** `brew install ffmpeg`
   - **Linux:** `sudo apt install ffmpeg`

   Verify with `ffmpeg -version`.

## Add your reference voice sample

Place a **clean 2–3 minute** voice recording (single speaker, minimal
background noise) at:

```
samples/monika.mp3
```

You can also upload a different reference file in the UI at run time. Longer,
cleaner samples generally clone better.

## Run

```bash
python app.py
```

This opens your browser at **http://localhost:7860**. Then:

1. Upload an MP4 video.
2. (Optional) Upload a reference voice sample, or use the default
   `samples/monika.mp3`.
3. Choose the **spoken language** (or leave on *Auto-detect*). To **dub**, pick a
   **target language**; to just replace the voice in the same language, leave the
   target on *Keep original*.
4. Click **Transcribe** — the editable transcript appears on the right.
5. Fix any transcription errors. **Keep one line per segment** — edit the words,
   don't add or remove lines. (When dubbing, lines are translated automatically
   at Generate time; the transcript box shows the *original* language for editing.)
6. Click **Generate Video** — watch the status log for progress.
7. Preview and **download** the final MP4.

### Supported languages (XTTS v2)

English, Spanish, French, German, Italian, Portuguese, Polish, Turkish, Russian,
Dutch, Czech, Arabic, Chinese (Mandarin), Japanese, Hungarian, Korean, Hindi.

## Choosing the voice engine (commercial use)

| Engine | Languages | License | Use when |
| ------ | --------- | ------- | -------- |
| **XTTS v2** (default) | 17 | Non-commercial (Coqui CPML) | Personal use, dubbing into many languages |
| **F5-TTS** | Mainly EN/ZH | MIT (commercial-OK) | You need a commercially usable engine |

To switch to the commercial-safe engine:

```bash
pip install f5-tts
```

```python
# config.py
TTS_BACKEND = "f5"
```

That's the only change — the rest of the pipeline (timing fit, diarization,
lip-sync) works the same. The active engine and its license are shown at the top
of the UI. If F5-TTS isn't installed, the app automatically falls back to XTTS.

> **Note:** for a fully commercial stack, also replace Wav2Lip lip-sync (its
> license is non-commercial) and use the offline `argos` translation backend.

## Multi-speaker setup (optional)

Diarization splits the audio by speaker so each person in the video is cloned in
their own voice — the reference for each speaker is extracted automatically from
their longest turns, so you don't upload anything per speaker. It uses
**pyannote.audio**, whose model is gated on Hugging Face:

1. `pip install pyannote.audio`
2. Create a free token at https://hf.co/settings/tokens
3. Accept the model conditions at
   https://hf.co/pyannote/speaker-diarization-3.1 (and `segmentation-3.0`).
4. Set the token and enable it:
   ```python
   # config.py
   ENABLE_DIARIZATION = True
   # HF_TOKEN is read from the HF_TOKEN / HUGGINGFACE_TOKEN env var by default,
   # or set it here:  HF_TOKEN = "hf_..."
   ```

Then tick **"Detect multiple speakers"** before Transcribe. Detected speaker
labels appear in the transcript (e.g. `[SPEAKER_00 | 0.00 -> 2.00] ...`). If
diarization isn't set up, the run falls back to single-speaker cloning.

## Lip-sync setup (optional)

Lip-sync makes dubbed/edited videos look natural by re-animating the mouth to
the new audio. It uses **Wav2Lip**, a separate project with its own
(research/non-commercial) license and model checkpoint, so it is off by default
and set up once:

1. Clone Wav2Lip (or a maintained fork) somewhere on disk:
   ```bash
   git clone https://github.com/Rudrabha/Wav2Lip
   ```
2. Download the **`wav2lip_gan.pth`** checkpoint into `Wav2Lip/checkpoints/`
   (see that repo's README for the current download link) and the face-detection
   model it requires.
3. Wav2Lip's dependencies differ from this project's, so it's cleanest to give
   it its own virtualenv.
4. Point `config.py` at your setup and enable it:
   ```python
   ENABLE_LIPSYNC = True
   WAV2LIP_DIR = Path(r"C:\tools\Wav2Lip")
   WAV2LIP_CHECKPOINT = WAV2LIP_DIR / "checkpoints" / "wav2lip_gan.pth"
   WAV2LIP_PYTHON = r"C:\tools\Wav2Lip\.venv\Scripts\python.exe"  # optional
   ```

Then the **"Lip-sync mouth to the new voice"** checkbox becomes enabled in the
UI. Faces must be clearly visible; if none is detected, the run falls back to
plain audio replacement and tells you in the status log. Lip-sync is noticeably
faster on a GPU.

## Command-line usage (batch)

For automation and bulk jobs, use the CLI instead of the web UI — same pipeline,
no browser:

```bash
# Replace the voice in one video with the default reference sample
python cli.py input.mp4

# Dub into Spanish with a specific reference voice
python cli.py input.mp4 --reference voice.wav --target es

# Batch every video in a folder, with diarization + lip-sync, dubbed to Hindi
python cli.py ./clips --batch --diarize --lipsync --target hi
```

Run `python cli.py --help` for all options. In `--batch` mode each file is
processed independently; one failure doesn't stop the rest, and the exit code is
non-zero if any failed.

## REST API

Expose the pipeline as a service other apps can call. Jobs run in the background
and clients poll for status (processing takes minutes).

```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

| Method & path            | Purpose                                   |
| ------------------------ | ----------------------------------------- |
| `POST /jobs`             | Upload a video (+ optional reference) → job id |
| `GET  /jobs/{id}`        | Status + progress log                     |
| `GET  /jobs/{id}/result` | Download the finished MP4                  |
| `GET  /languages`        | Supported language codes                   |
| `GET  /health`           | Liveness + which backends are active       |

Example:

```bash
# Start a dubbing job (English video -> Spanish)
curl -F video=@input.mp4 -F target_lang=es http://localhost:8000/jobs
# -> {"id":"ab12cd34ef56","status":"queued",...}

curl http://localhost:8000/jobs/ab12cd34ef56            # poll status
curl -OJ http://localhost:8000/jobs/ab12cd34ef56/result # download when done
```

Interactive docs are auto-generated at `http://localhost:8000/docs`.

> The bundled job registry is in-memory (single process). For production scale,
> back it with Redis/RQ or a database — `core.process_video` is the reusable
> entry point the CLI, API, and UI all share.

## Docker (one-command deploy)

Run the whole platform in a container with ffmpeg and all deps baked in — no
Python/ffmpeg setup needed on the host. Models download on first use into a
named volume, so they're fetched only once.

```bash
# REST API on http://localhost:8000
docker compose up api

# Gradio UI on http://localhost:7860
docker compose up ui
```

Or with plain Docker:

```bash
docker build -t voice-replacer .

# API
docker run --rm -p 8000:8000 -v vr-models:/root/.cache \
  -v "$PWD/samples:/app/samples" -v "$PWD/output:/app/output" voice-replacer

# CLI on a mounted video
docker run --rm -v vr-models:/root/.cache -v "$PWD:/data" \
  voice-replacer python cli.py /data/input.mp4 --target es
```

- `samples/` (your reference voice) and `output/` are bind-mounted to the host.
- The image is **CPU-only** by default. For GPU, switch the base image to
  `nvidia/cuda`, install a CUDA build of torch, and run with `--gpus all` —
  `config.py` auto-detects CUDA.

## Hardware notes

| Hardware | Approx. time (9-min video) |
| -------- | -------------------------- |
| CPU      | ~10 min                    |
| GPU      | ~2 min                     |

The first run also downloads the Whisper `large-v3` (~3 GB) and XTTS v2 models,
which takes extra time and disk space.

## Making it faster

Speed, biggest lever first:

1. **Use a GPU.** By far the biggest win (5–20×). `config.py` auto-detects CUDA;
   install a CUDA build of torch and it just works. No GPU? Rent one by the hour
   (RunPod, Vast.ai) when you have a big batch.
2. **Smaller transcription model.** `WHISPER_MODEL = "small"` (or `"base"`) is
   much faster on CPU than `large-v3`, with good accuracy for clear speech.
3. **Keep the reference short.** XTTS computes the voice fingerprint from the
   whole reference clip, so a 5-minute sample is slow for no benefit. The app now
   trims it to `XTTS_MAX_REF_SECONDS` (default 20s) automatically — lower it to
   ~10s for a bit more speed.
4. **Voice fingerprint is cached** per reference, so it's computed once instead
   of once per segment (automatic — no setting).
5. **First run is slow once.** Models download (~2 GB) on the first run only;
   later runs reuse the cache.

## Studio-grade voice cleanup

Two cleanup stages run after synthesis for clean, professional output:

1. **Deep voice enhancement (DeepFilterNet)** — a deep-learning speech enhancer
   that removes noise/hiss/reverb and makes the voice crisp. Optional and heavy;
   runs best on a GPU. Enable by installing it (auto-activates when present):
   ```bash
   pip install deepfilternet
   ```
   Toggle with `ENABLE_VOICE_ENHANCE` in `config.py`. Skipped gracefully if not
   installed.
2. **ffmpeg mastering** — high-pass, denoise, de-click, and EBU R128 loudness
   normalization (`AUDIO_FILTER_CHAIN`, `ENABLE_AUDIO_CLEANUP`).

Still the biggest factor: a **clean reference sample** (quiet, single speaker,
15-30s). The cleaner the reference, the cleaner the clone.

## Tuning voice quality

If the output sounds **robotic or sped-up**, or the **timing feels off**, these
`config.py` settings are the levers (no code changes needed):

- **Robotic / synthetic voice:**
  - Raise/lower `XTTS_TEMPERATURE` (try `0.7`–`0.85`) for more natural variation.
  - Keep `XTTS_REPETITION_PENALTY` around `3`–`5` to avoid monotone delivery.
  - Use a **cleaner, longer reference sample** (2–3 min, single speaker, no
    background noise) — reference quality matters more than any setting.
  - Time-stretching is the other cause: it's already gentle, but you can set
    `FIT_SEGMENT_TIMING = False` to disable it entirely for the most natural
    voice (at the cost of some drift on long videos).
- **Timing feels off / audio drifts:**
  - Lower `FIT_TOLERANCE_RATIO` (e.g. `0.08`) to correct timing more tightly
    (slightly less natural), or raise it (e.g. `0.25`) for more natural pacing
    with looser sync.
  - Raise `MAX_TEMPO` (e.g. `1.2`) to let badly-off segments fit more tightly.

## Troubleshooting

- **CUDA out of memory** — switch to CPU by editing `config.py` and setting
  `DEVICE = "cpu"`, or use a smaller Whisper model (e.g. `WHISPER_MODEL =
  "medium"`). Close other GPU applications.
- **ffmpeg not found** — ensure ffmpeg is installed and on your `PATH`. Restart
  your terminal after adding it. Test with `ffmpeg -version`.
- **XTTS license acceptance** — on first use Coqui XTTS v2 prompts you to accept
  its non-commercial license (Coqui Public Model License). Answer `y` when
  prompted, or set the environment variable
  `COQUI_TOS_AGREED=1` before launching to accept it non-interactively.
- **`Microsoft Visual C++ 14.0 or greater is required` when installing** — this
  happens with the original `TTS` package. Use `coqui-tts` instead (already set
  in `requirements.txt`), which has a prebuilt wheel and needs no compiler.
- **`TTS` / `coqui-tts` won't install (Python 3.12+)** — use a Python 3.10/3.11
  virtual environment (see Install step 1).
- **No speech detected** — the video may have no clear speech, or the wrong
  language. Set `LANGUAGE` in `config.py` to match the source audio.

## Testing

Run the smoke test (requires ffmpeg + a reference sample at
`samples/monika.mp3`):

```bash
pytest test_pipeline.py -v
```

It generates a short synthetic 10-second video, runs the full pipeline, and
verifies a valid MP4 is produced. It skips automatically if ffmpeg or the
reference sample is missing.

## Configuration

All tunables live in `config.py`:

| Setting                | Default                                          |
| ---------------------- | ------------------------------------------------ |
| `TTS_BACKEND`          | `xtts` (17 langs, non-commercial) / `f5` (MIT)    |
| `WHISPER_BACKEND`      | `faster` (faster-whisper; `openai` as fallback)  |
| `WHISPER_MODEL`        | `large-v3`                                        |
| `WHISPER_COMPUTE_TYPE` | `float16` on GPU, `int8` on CPU                   |
| `XTTS_MODEL`           | `tts_models/multilingual/multi-dataset/xtts_v2`  |
| `SAMPLE_RATE`          | `24000` (XTTS native)                             |
| `LANGUAGE`             | `en`                                              |
| `DEVICE`               | `cuda` if available, else `cpu`                   |
| `XTTS_TEMPERATURE`     | `0.75` (voice expressiveness / naturalness)      |
| `XTTS_REPETITION_PENALTY` | `5.0` (reduces monotone delivery)             |
| `FIT_SEGMENT_TIMING`   | `True` (anti-drift time-stretch)                 |
| `FIT_TOLERANCE_RATIO`  | `0.15` (don't stretch within ±15% of slot)       |
| `MAX_TEMPO`            | `1.12` (gentle stretch cap — keeps voice natural)|
| `XTTS_MAX_REF_SECONDS` | `20` (trim reference for speed; 0 = full clip)   |
| `ENABLE_LIPSYNC`       | `False` (Wav2Lip, set up separately)             |
