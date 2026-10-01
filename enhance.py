"""Deep voice enhancement (studio-grade denoise/clean-up).

Uses DeepFilterNet — a deep-learning real-time speech enhancer — to clean the
generated voice far more thoroughly than classic ffmpeg filters: it removes
background noise, hiss and reverb while keeping the voice crisp and natural.

DeepFilterNet is optional (and heavy), so it is guarded and loaded lazily. If it
isn't installed, the pipeline falls back to the ffmpeg mastering pass alone.
Runs best on a GPU.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Callable, Optional, Tuple

import config

logger = logging.getLogger(__name__)

ProgressCb = Optional[Callable[[str], None]]

_df = None  # cached (model, df_state)


def _emit(cb: ProgressCb, message: str) -> None:
    logger.info(message)
    if cb is not None:
        cb(message)


def is_available() -> Tuple[bool, str]:
    """Return ``(available, reason)`` describing whether enhancement can run."""
    if not config.ENABLE_VOICE_ENHANCE:
        return False, "Voice enhancement disabled (ENABLE_VOICE_ENHANCE=False)."
    if config.VOICE_ENHANCE_BACKEND != "deepfilternet":
        return False, f"Unknown enhance backend '{config.VOICE_ENHANCE_BACKEND}'."
    import importlib.util

    try:
        if importlib.util.find_spec("df") is None:
            return False, "DeepFilterNet not installed (pip install deepfilternet)."
    except ModuleNotFoundError:
        return False, "DeepFilterNet not installed (pip install deepfilternet)."
    return True, "ok"


def _load():
    """Load and cache the DeepFilterNet model + state."""
    global _df
    if _df is None:
        from df.enhance import init_df

        logger.info("Loading DeepFilterNet enhancement model ...")
        model, df_state, _ = init_df()
        _df = (model, df_state)
    return _df


def enhance_audio(src: str, dst: str, cb: ProgressCb = None) -> str:
    """Deep-clean the speech in ``src``, writing the result to ``dst``.

    Args:
        src: Input WAV path (the concatenated generated voice).
        dst: Output WAV path for the enhanced audio.
        cb: Optional progress callback.

    Returns:
        ``dst`` on success.

    Raises:
        RuntimeError: if enhancement is unavailable (callers should catch and
            fall back to the un-enhanced audio).
    """
    available, reason = is_available()
    if not available:
        raise RuntimeError(f"Voice enhancement unavailable: {reason}")

    from df.enhance import enhance, load_audio, save_audio

    _emit(cb, "Enhancing voice (DeepFilterNet deep denoise)...")
    model, df_state = _load()
    audio, _ = load_audio(str(src), sr=df_state.sr())
    enhanced = enhance(model, df_state, audio)
    save_audio(str(dst), enhanced, df_state.sr())
    return str(dst)
