# Quickstart

Get a dubbed/voice-replaced video in a few minutes. For full details see
[README.md](README.md).

---

## 0. Prerequisites (once)

- **Python 3.10 or 3.11**
- **ffmpeg** on your PATH (`ffmpeg -version` should work)
- A **reference voice** at `samples/monika.mp3` (2–3 min of clean single-speaker
  audio) — or upload one at run time.

```bash
pip install -r requirements.txt
```

> **No GPU?** Edit `config.py` and set `WHISPER_MODEL = "small"` (or `"medium"`).
> The default `large-v3` is accurate but slow on CPU.

---

## 1. Pick how you want to run it

### Web UI — easiest, lets you fix the transcript

```bash
python app.py
```

Then at **http://localhost:7860**:

1. **Upload** your MP4.
2. (Optional) Upload a different reference voice.
3. Choose **Spoken language** (leave on *Auto-detect*).
4. To **dub**, pick a **Dub into** target language; otherwise leave *Keep original*.
5. Click **Transcribe** → edit any wrong words (keep **one line per segment**).
6. Click **Generate Video** → **preview & download**.

### Command line — best for batches

```bash
python cli.py input.mp4                      # replace voice, same language
python cli.py input.mp4 --target es          # dub into Spanish
python cli.py ./clips --batch --target hi    # whole folder, dubbed to Hindi
```

Results are saved in `output/`. See `python cli.py --help`.

### REST API — for integrating into another app

```bash
uvicorn api:app --port 8000
```

```bash
curl -F video=@input.mp4 -F target_lang=es http://localhost:8000/jobs  # -> {id}
curl http://localhost:8000/jobs/<id>                                   # status
curl -OJ http://localhost:8000/jobs/<id>/result                        # download
```

Docs at **http://localhost:8000/docs**.

### Docker — zero host setup

```bash
docker compose up api     # API on :8000
docker compose up ui      # UI  on :7860
```

---

## 2. What each choice does

| I want to… | Do this |
| ---------- | ------- |
| Just change the voice | Upload → Transcribe → Generate |
| Translate to another language | Set a **target language** / `--target <code>` |
| Process many videos | CLI with `--batch` |
| Build a product on it | API + set `TTS_BACKEND = "f5"` (commercial-safe) |

**Languages:** English, Spanish, French, German, Italian, Portuguese, Polish,
Turkish, Russian, Dutch, Czech, Arabic, Chinese, Japanese, Hungarian, Korean,
Hindi.

---

## 3. First-run note

The **first** run downloads the Whisper and voice models (~2 GB) — this is a
one-time cost. Later runs reuse the cached models and are much faster.

---

## 4. Optional power features (need extra setup — see README)

- **Multiple speakers** — detect & clone each speaker separately (pyannote +
  free Hugging Face token). Available via `--diarize`.
- **Lip-sync** — re-animate the mouth to match the new voice (Wav2Lip).
  Available via `--lipsync`.
- **Commercial-safe voice** — `pip install f5-tts`, set `TTS_BACKEND = "f5"`.

All optional features are off by default and skip gracefully if not set up.

---

## 5. Troubleshooting

| Problem | Fix |
| ------- | --- |
| Very slow on CPU | Set `WHISPER_MODEL = "small"` in `config.py` |
| `ffmpeg not found` | Install ffmpeg and add it to PATH; restart the terminal |
| No speech detected | Check the video has clear speech; set the right source language |
| Reference missing | Put a clip at `samples/monika.mp3` or upload one in the UI |
