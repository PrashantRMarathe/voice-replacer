"""Central configuration for the Voice Replacer tool.

All tunable constants (model names, paths, sample rate, language, device)
live here so behaviour can be changed without touching pipeline or UI code.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

try:
    import torch

    _CUDA_AVAILABLE = torch.cuda.is_available()
except Exception:  # torch not importable yet
    _CUDA_AVAILABLE = False

# --------------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------------- #
BASE_DIR: Path = Path(__file__).resolve().parent
SAMPLES_DIR: Path = BASE_DIR / "samples"
INPUT_DIR: Path = BASE_DIR / "input"
OUTPUT_DIR: Path = BASE_DIR / "output"
TEMP_DIR: Path = BASE_DIR / "temp"

# Default reference voice sample (user provides this file).
DEFAULT_REFERENCE_SAMPLE: Path = SAMPLES_DIR / "monika.mp3"

# Ensure the working directories exist at import time.
for _d in (SAMPLES_DIR, INPUT_DIR, OUTPUT_DIR, TEMP_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------- #
# Models
# --------------------------------------------------------------------------- #
WHISPER_MODEL = "small"

# Text-to-speech backend (voice cloning engine):
#   "xtts" -> Coqui XTTS v2: 17 languages, but NON-COMMERCIAL license. Default.
#   "f5"   -> F5-TTS: MIT (commercial-OK), but the base model covers mainly
#             English + Chinese. Best when you need a commercially-usable engine.
# If the chosen backend can't be imported, the other is used automatically.
TTS_BACKEND: str = "xtts"

XTTS_MODEL: str = "tts_models/multilingual/multi-dataset/xtts_v2"

# XTTS v2 generation tuning — these strongly affect how natural vs robotic the
# cloned voice sounds. Defaults below are tuned for natural, expressive speech.
#   XTTS_TEMPERATURE       higher = more expressive/varied (too high = unstable)
#   XTTS_REPETITION_PENALTY discourages monotone/looping delivery
#   XTTS_LENGTH_PENALTY     <1 slightly shortens, >1 lengthens phrasing
#   XTTS_TOP_K / XTTS_TOP_P sampling breadth (naturalness vs consistency)
#   XTTS_SPEED              global speaking rate (1.0 = natural)
#   XTTS_ENABLE_TEXT_SPLITTING  split long lines into sentences so the voice
#                               breathes naturally instead of rushing one breath
XTTS_TEMPERATURE: float = 0.75
XTTS_REPETITION_PENALTY: float = 5.0
XTTS_LENGTH_PENALTY: float = 1.0
XTTS_TOP_K: int = 50
XTTS_TOP_P: float = 0.85
XTTS_SPEED: float = 1.0
XTTS_ENABLE_TEXT_SPLITTING: bool = True

# Speed: XTTS computes the voice fingerprint from the WHOLE reference clip on
# every segment, so a long reference is very slow for no quality gain. Trim the
# reference to this many seconds before cloning (~6-20s is ideal for XTTS).
XTTS_MAX_REF_SECONDS: float = 20.0

# F5-TTS model to load (see the f5-tts package for available model names). The
# default base model is English-centric.
F5_MODEL: str = "F5TTS_v1_Base"

# Transcription backend:
#   "faster"  -> faster-whisper (CTranslate2): ~4x faster, lower VRAM. Default.
#   "openai"  -> the original openai-whisper reference implementation.
# If the chosen backend can't be imported, the other is used automatically.
WHISPER_BACKEND: str = "faster"

# Compute precision for faster-whisper. "float16" is best on a CUDA GPU; "int8"
# is fast and light on CPU. Ignored by the openai backend.
WHISPER_COMPUTE_TYPE: str = "float16" if _CUDA_AVAILABLE else "int8"

# --------------------------------------------------------------------------- #
# Audio / language settings
# --------------------------------------------------------------------------- #
SAMPLE_RATE: int = 24_000          # XTTS v2 native output sample rate
LANGUAGE: str = "en"               # default/fallback XTTS language code
DEVICE: str = "cuda" if _CUDA_AVAILABLE else "cpu"

# --------------------------------------------------------------------------- #
# Multi-language / dubbing
# --------------------------------------------------------------------------- #
# The 17 languages Coqui XTTS v2 can speak. Maps the XTTS language code to a
# human-readable name shown in the UI. Whisper uses the same 2-letter codes
# except for Chinese (Whisper: "zh", XTTS: "zh-cn"); WHISPER_LANG_OVERRIDES
# below bridges that difference.
LANGUAGES: dict[str, str] = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "pl": "Polish",
    "tr": "Turkish",
    "ru": "Russian",
    "nl": "Dutch",
    "cs": "Czech",
    "ar": "Arabic",
    "zh-cn": "Chinese (Mandarin)",
    "ja": "Japanese",
    "hu": "Hungarian",
    "ko": "Korean",
    "hi": "Hindi",
}

# XTTS code -> the language code Whisper expects (when different).
WHISPER_LANG_OVERRIDES: dict[str, str] = {"zh-cn": "zh"}

# Sentinel used in the UI to mean "let Whisper detect the source language".
AUTO_DETECT: str = "auto"

# Amount of leading/trailing padding tolerance (seconds) when aligning audio
# to the original video length before merging.
DURATION_TOLERANCE_S: float = 0.5

# --------------------------------------------------------------------------- #
# Timing fit (anti-drift)
# --------------------------------------------------------------------------- #
# The cloned voice rarely speaks each line in exactly the same duration as the
# original. Left uncorrected, these differences accumulate and the audio drifts
# out of sync with the video. When FIT_SEGMENT_TIMING is True, each synthesized
# segment is time-stretched (pitch-preserving) toward its original time slot.
#
# IMPORTANT: time-stretching is the main thing that can make the voice sound
# robotic/sped-up. The settings below keep it GENTLE — segments within
# FIT_TOLERANCE_RATIO of their slot are left completely untouched (natural), and
# the clamp is modest so corrections stay subtle. Set FIT_SEGMENT_TIMING = False
# to disable stretching entirely (most natural voice, but long videos may drift).
FIT_SEGMENT_TIMING: bool = True

# Don't stretch at all unless a segment is off by more than this fraction of its
# slot. 0.15 = ignore up to ±15% mismatch, so the vast majority of segments play
# at XTTS's natural pace and only badly-off ones get a gentle nudge.
FIT_TOLERANCE_RATIO: float = 0.15

# Clamp the time-stretch factor. Kept gentle (1.12 = at most 12% faster/slower)
# so corrections are inaudible rather than "chipmunk". Segments needing more are
# fit as close as the clamp allows (slight residual drift) instead of distorted.
MAX_TEMPO: float = 1.12          # fastest allowed (generated longer than slot)
MIN_TEMPO: float = 1.0 / 1.12    # slowest allowed (generated shorter than slot)

# Only bother stretching when the mismatch is at least this many seconds;
# tiny differences aren't worth an extra ffmpeg pass.
FIT_MIN_DELTA_S: float = 0.05

# --------------------------------------------------------------------------- #
# Speaker diarization (optional)
# --------------------------------------------------------------------------- #
# When enabled, the audio is split by speaker so that multi-person videos clone
# each speaker separately — each speaker is voiced using a reference clip
# automatically extracted from their own longest turns in the source audio.
#
# Uses pyannote.audio, whose model is gated on Hugging Face, so one-time setup:
#   1. pip install pyannote.audio
#   2. Create a free Hugging Face token at https://hf.co/settings/tokens
#   3. Accept the model conditions at
#      https://hf.co/pyannote/speaker-diarization-3.1  (and segmentation-3.0)
#   4. Set HF_TOKEN below, or the HUGGINGFACE_TOKEN / HF_TOKEN env var.
#
# If unavailable, the app falls back to single-speaker cloning automatically.
import os

ENABLE_DIARIZATION: bool = False
DIARIZATION_MODEL: str = "pyannote/speaker-diarization-3.1"
HF_TOKEN: str | None = os.environ.get("HF_TOKEN") or os.environ.get(
    "HUGGINGFACE_TOKEN"
)
# Seconds of a speaker's own audio to use as their cloning reference.
SPEAKER_REF_SECONDS: float = 15.0

# --------------------------------------------------------------------------- #
# Lip-sync (optional post-processing)
# --------------------------------------------------------------------------- #
# When enabled, after the cloned voice is generated the video's mouth is
# re-animated to match the new audio using Wav2Lip. This makes dubbed videos
# look natural instead of having the lips move to the old words.
#
# Wav2Lip is a separate project with its own (research/non-commercial) license
# and model checkpoint, so it is OFF by default and must be set up once:
#
#   1. git clone https://github.com/Rudrabha/Wav2Lip   (or a maintained fork)
#   2. Download the "wav2lip_gan.pth" checkpoint into its checkpoints/ folder.
#   3. Point WAV2LIP_DIR and WAV2LIP_CHECKPOINT below at those locations.
#   4. (Optional) WAV2LIP_PYTHON: a separate Python executable for Wav2Lip's own
#      virtualenv, since its deps differ from this project's. Defaults to the
#      current interpreter.
#
# If any path is missing, lip-sync is skipped gracefully and the app falls back
# to plain audio replacement. Faces must be visible for Wav2Lip to work.
ENABLE_LIPSYNC: bool = False
WAV2LIP_DIR: Path | None = None          # e.g. Path(r"C:\tools\Wav2Lip")
WAV2LIP_CHECKPOINT: Path | None = None   # e.g. WAV2LIP_DIR / "checkpoints" / "wav2lip_gan.pth"
WAV2LIP_PYTHON: str | None = None        # e.g. r"C:\tools\Wav2Lip\.venv\Scripts\python.exe"

# Wav2Lip can be slow on high-res video; optionally cap the resize factor it
# uses (higher = faster, lower quality). None leaves Wav2Lip's default.
WAV2LIP_RESIZE_FACTOR: int | None = None

# --------------------------------------------------------------------------- #
# Logging
# --------------------------------------------------------------------------- #
LOG_LEVEL: int = logging.INFO
LOG_FORMAT: str = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"


def configure_logging() -> None:
    """Configure root logging once, using the module-level format/level."""
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)


def to_whisper_code(xtts_code: str) -> str:
    """Convert an XTTS language code to the code Whisper expects."""
    return WHISPER_LANG_OVERRIDES.get(xtts_code, xtts_code)


def base_lang(xtts_code: str) -> str:
    """Return the 2-letter base code (e.g. 'zh-cn' -> 'zh'), for translators."""
    return xtts_code.split("-", 1)[0]


def to_xtts_code(code: Optional[str]) -> Optional[str]:
    """Resolve any language code to a supported XTTS code, or ``None``.

    Accepts an XTTS code directly, or a Whisper/base code (e.g. ``"zh"`` ->
    ``"zh-cn"``). Returns ``None`` if XTTS v2 cannot speak the language.
    """
    if not code:
        return None
    if code in LANGUAGES:
        return code
    base = base_lang(code)
    for xtts_code in LANGUAGES:
        if base_lang(xtts_code) == base:
            return xtts_code
    return None
