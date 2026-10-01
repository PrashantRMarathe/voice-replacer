# Voice Replacer / AI dubbing platform — CPU image.
#
# Builds a reproducible environment with ffmpeg + all Python deps baked in.
# Models (Whisper, XTTS) are NOT baked in; they download on first use into a
# mounted cache volume so the image stays lean and the license prompt is handled
# via COQUI_TOS_AGREED.
#
# Build:
#   docker build -t voice-replacer .
#
# Run the REST API (default):
#   docker run --rm -p 8000:8000 \
#     -v vr-models:/root/.cache \
#     -v "$PWD/samples:/app/samples" \
#     -v "$PWD/output:/app/output" voice-replacer
#
# Run the Gradio UI instead:
#   docker run --rm -p 7860:7860 -v vr-models:/root/.cache \
#     -v "$PWD/samples:/app/samples" voice-replacer \
#     python app.py
#
# Run the CLI on a mounted video:
#   docker run --rm -v vr-models:/root/.cache \
#     -v "$PWD:/data" voice-replacer \
#     python cli.py /data/input.mp4 --target es
#
# For GPU, use an nvidia/cuda base image + a CUDA build of torch and run with
# `--gpus all`; config.py auto-detects CUDA.

FROM python:3.11-slim

# System deps: ffmpeg for all audio/video work, libsndfile for soundfile,
# git for any VCS-based pip deps. Clean apt lists to keep the layer small.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ffmpeg \
        libsndfile1 \
        git \
    && rm -rf /var/lib/apt/lists/*

# Accept the Coqui XTTS non-commercial license non-interactively, and keep
# Python output unbuffered so container logs stream in real time.
ENV COQUI_TOS_AGREED=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HF_HUB_DISABLE_SYMLINKS_WARNING=1

WORKDIR /app

# Install Python deps first (better layer caching). Install a CPU build of
# torch/torchaudio explicitly so pip doesn't pull the much larger CUDA wheels.
COPY requirements.txt .
RUN pip install --no-cache-dir \
        torch torchaudio --index-url https://download.pytorch.org/whl/cpu \
    && pip install --no-cache-dir -r requirements.txt

# Copy the application code.
COPY . .

# Ensure runtime data dirs exist (config.py also creates them at import time).
RUN mkdir -p input output temp samples

# API (8000) and UI (7860).
EXPOSE 8000 7860

# Default: serve the REST API. Override the command to run app.py or cli.py.
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
