"""Batch dubbing for many videos with one shared reference voice.

Built for large jobs (hundreds of videos) that may span multiple Colab
sessions, so it is RESUMABLE: outputs are named after each input file and any
video whose output already exists is skipped. Re-running continues where it
left off. Failures are logged and don't stop the rest.
"""

from __future__ import annotations

import logging
import shutil
from pathlib import Path
from typing import Callable, List, Optional

import config
import core

logger = logging.getLogger(__name__)
ProgressCb = Optional[Callable[[str], None]]

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}


def _emit(cb: ProgressCb, msg: str) -> None:
    logger.info(msg)
    if cb is not None:
        cb(msg)


def list_videos(input_dir: str) -> List[Path]:
    """Return sorted video files in ``input_dir``."""
    d = Path(input_dir)
    return sorted(p for p in d.iterdir()
                  if p.is_file() and p.suffix.lower() in VIDEO_EXTS)


def process_folder(
    input_dir: str,
    output_dir: str,
    reference_path: str,
    source_lang: str = config.AUTO_DETECT,
    target_lang: Optional[str] = None,
    cb: ProgressCb = None,
) -> dict:
    """Dub every video in ``input_dir`` with one shared ``reference_path``.

    Outputs go to ``output_dir`` named ``<original_stem>_dubbed.mp4`` (plus
    matching .srt/.vtt). Videos already done are skipped (resumable).

    Returns a summary dict: {total, done, skipped, failed, failures}.
    """
    out_root = Path(output_dir)
    out_root.mkdir(parents=True, exist_ok=True)

    videos = list_videos(input_dir)
    summary = {"total": len(videos), "done": 0, "skipped": 0,
               "failed": 0, "failures": []}
    if not videos:
        _emit(cb, f"No videos found in {input_dir}")
        return summary

    _emit(cb, f"Found {len(videos)} video(s). Reference: {Path(reference_path).name}")

    for i, video in enumerate(videos, 1):
        final_out = out_root / f"{video.stem}_dubbed.mp4"
        if final_out.exists():
            summary["skipped"] += 1
            _emit(cb, f"[{i}/{len(videos)}] SKIP (already done): {video.name}")
            continue

        _emit(cb, f"[{i}/{len(videos)}] Processing: {video.name}")
        try:
            produced = core.process_video(
                str(video),
                reference_path=reference_path,
                source_lang=source_lang,
                target_lang=target_lang,
                cb=cb,
            )
            # Move the produced MP4 + sidecar subtitles to stable names in Drive.
            shutil.move(produced, final_out)
            prod_stem = Path(produced).with_suffix("")
            for ext in (".srt", ".vtt"):
                side = Path(f"{prod_stem}{ext}")
                if side.is_file():
                    shutil.move(str(side), str(out_root / f"{video.stem}{ext}"))
            summary["done"] += 1
            _emit(cb, f"[{i}/{len(videos)}] DONE -> {final_out.name}")
        except Exception as exc:  # noqa: BLE001 - keep going on failure
            summary["failed"] += 1
            summary["failures"].append(video.name)
            logger.error("Failed on %s", video.name, exc_info=True)
            _emit(cb, f"[{i}/{len(videos)}] FAILED: {video.name} ({exc})")

    _emit(cb, f"Batch complete. Done={summary['done']} "
              f"Skipped={summary['skipped']} Failed={summary['failed']}")
    return summary
