"""Background music / SFX preservation via Demucs source separation.

Splits the original audio into the vocal track and everything-else. We discard
the original vocals (replaced by the cloned voice) and keep the isolated
music/SFX stem, which is clean (no voice bleed) — so the final mix has the
original background under the new voice.

Demucs is optional and heavy, so it is guarded and invoked as a subprocess
(it ships a CLI). Runs best on a GPU. If not installed, callers skip it.
"""

from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path
from typing import Callable, Optional, Tuple

import config

logger = logging.getLogger(__name__)

ProgressCb = Optional[Callable[[str], None]]


def _emit(cb: ProgressCb, message: str) -> None:
    logger.info(message)
    if cb is not None:
        cb(message)


def is_available() -> Tuple[bool, str]:
    """Return ``(available, reason)`` for background preservation."""
    if not config.PRESERVE_BACKGROUND:
        return False, "Background preservation disabled (PRESERVE_BACKGROUND=False)."
    import importlib.util

    try:
        if importlib.util.find_spec("demucs") is None:
            return False, "Demucs not installed (pip install demucs)."
    except ModuleNotFoundError:
        return False, "Demucs not installed (pip install demucs)."
    return True, "ok"


def separate_background(
    audio_path: str, run_id: str, cb: ProgressCb = None
) -> str:
    """Return the path to the isolated music/SFX stem of ``audio_path``.

    Uses Demucs ``--two-stems=vocals`` (vocals vs. no_vocals) and returns the
    ``no_vocals`` stem. Runs Demucs as a subprocess into a per-run folder.

    Raises:
        RuntimeError: if separation is unavailable or fails (callers fall back
            to a voice-only track).
    """
    available, reason = is_available()
    if not available:
        raise RuntimeError(f"Background separation unavailable: {reason}")

    _emit(cb, "Separating background music from voice (Demucs)...")
    out_dir = config.TEMP_DIR / f"{run_id}_demucs"
    cmd = [
        sys.executable, "-m", "demucs",
        "--two-stems", "vocals",
        "-d", config.DEVICE,
        "-o", str(out_dir),
        str(audio_path),
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
    except OSError as exc:  # pragma: no cover
        raise RuntimeError(f"Failed to launch Demucs: {exc}") from exc
    if proc.returncode != 0:
        tail = "\n".join((proc.stderr or proc.stdout or "").splitlines()[-6:])
        raise RuntimeError(f"Demucs failed:\n{tail}")

    # Demucs writes <out_dir>/<model>/<track_name>/no_vocals.wav
    matches = list(out_dir.rglob("no_vocals.wav"))
    if not matches:
        raise RuntimeError("Demucs produced no 'no_vocals' stem.")
    _emit(cb, "Background music isolated.")
    return str(matches[0])
