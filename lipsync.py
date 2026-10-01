"""Optional lip-sync post-processing via Wav2Lip.

After the cloned voice is generated, this re-animates the speaker's mouth in the
video to match the new audio, so dubbed/edited videos look natural instead of
mouthing the original words.

Wav2Lip is a separate, non-commercially-licensed project with its own model
checkpoint, so it is invoked as an external subprocess rather than imported.
This keeps its (often conflicting) dependencies out of this project's
environment. See ``config.py`` for the one-time setup, and ``is_available``
for the guard the UI uses to decide whether to offer lip-sync.
"""

from __future__ import annotations

import logging
import subprocess
import sys
from pathlib import Path
from typing import Callable, List, Optional, Tuple

import config

logger = logging.getLogger(__name__)

ProgressCb = Optional[Callable[[str], None]]


def _emit(cb: ProgressCb, message: str) -> None:
    logger.info(message)
    if cb is not None:
        cb(message)


def is_available() -> Tuple[bool, str]:
    """Return ``(available, reason)`` describing whether lip-sync can run.

    Lip-sync is available only when it is enabled in config *and* the Wav2Lip
    directory, inference script, and checkpoint all exist on disk. ``reason``
    explains what is missing so the UI can show an actionable message.
    """
    if not config.ENABLE_LIPSYNC:
        return False, "Lip-sync is disabled (set ENABLE_LIPSYNC = True in config.py)."
    if config.WAV2LIP_DIR is None or not Path(config.WAV2LIP_DIR).is_dir():
        return False, f"Wav2Lip directory not found: {config.WAV2LIP_DIR}"

    inference = Path(config.WAV2LIP_DIR) / "inference.py"
    if not inference.is_file():
        return False, f"Wav2Lip inference.py not found in {config.WAV2LIP_DIR}"
    if config.WAV2LIP_CHECKPOINT is None or not Path(config.WAV2LIP_CHECKPOINT).is_file():
        return False, f"Wav2Lip checkpoint not found: {config.WAV2LIP_CHECKPOINT}"
    return True, "ok"


def _build_command(video_path: str, audio_path: str, out_path: Path) -> List[str]:
    """Construct the Wav2Lip inference command line."""
    python_exe = config.WAV2LIP_PYTHON or sys.executable
    cmd = [
        python_exe,
        str(Path(config.WAV2LIP_DIR) / "inference.py"),
        "--checkpoint_path", str(config.WAV2LIP_CHECKPOINT),
        "--face", str(video_path),
        "--audio", str(audio_path),
        "--outfile", str(out_path),
    ]
    if config.WAV2LIP_RESIZE_FACTOR is not None:
        cmd += ["--resize_factor", str(config.WAV2LIP_RESIZE_FACTOR)]
    return cmd


def apply_lipsync(
    video_path: str,
    audio_path: str,
    run_id: str,
    cb: ProgressCb = None,
) -> str:
    """Re-animate the mouth in ``video_path`` to match ``audio_path``.

    Runs Wav2Lip as a subprocess. The produced MP4 already contains the new
    audio muxed in, so this fully replaces the separate merge step.

    Args:
        video_path: Source video whose face(s) will be re-animated.
        audio_path: The generated cloned-voice WAV to sync the mouth to.
        run_id: Unique id used to name the output file.
        cb: Optional progress callback.

    Returns:
        Path to the lip-synced MP4 in ``config.OUTPUT_DIR``.

    Raises:
        RuntimeError: if lip-sync is unavailable or Wav2Lip fails (e.g. no face
            detected). Callers should catch this and fall back to plain merge.
    """
    available, reason = is_available()
    if not available:
        raise RuntimeError(f"Lip-sync unavailable: {reason}")

    _emit(cb, "Lip-syncing video to the new voice (Wav2Lip)...")
    out_path = config.OUTPUT_DIR / f"{run_id}_lipsync.mp4"
    cmd = _build_command(video_path, audio_path, out_path)

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(config.WAV2LIP_DIR),  # Wav2Lip resolves assets relative to itself
            capture_output=True,
            text=True,
        )
    except OSError as exc:  # pragma: no cover - depends on local setup
        raise RuntimeError(f"Failed to launch Wav2Lip: {exc}") from exc

    if proc.returncode != 0 or not out_path.is_file():
        tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-8:]
        detail = "\n".join(tail)
        if "face" in detail.lower() and "detect" in detail.lower():
            raise RuntimeError(
                "Wav2Lip could not detect a face in the video. Lip-sync needs a "
                "clearly visible face. Falling back to plain audio replacement.\n"
                f"{detail}"
            )
        raise RuntimeError(f"Wav2Lip failed:\n{detail}")

    _emit(cb, "Lip-sync complete.")
    return str(out_path)
