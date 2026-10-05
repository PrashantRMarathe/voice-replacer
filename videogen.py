"""Assemble a narrated infographic video from image(s) + narration audio.

Builds a professional slideshow-style video (the kind used for explainer/SPL
content): each infographic image is shown for the duration of its narration,
with a gentle Ken Burns zoom so it isn't static, then the narration is muxed in.
Pure ffmpeg — no GPU needed. Subtitles are handled separately by subtitles.py.
"""

from __future__ import annotations

import logging
import uuid
from pathlib import Path
from typing import Callable, List, Optional, Tuple

import ffmpeg

import config

logger = logging.getLogger(__name__)
ProgressCb = Optional[Callable[[str], None]]


def _emit(cb: ProgressCb, msg: str) -> None:
    logger.info(msg)
    if cb is not None:
        cb(msg)


def _slide_clip(image_path: str, duration: float, out_path: Path,
                width: int = 1920, height: int = 1080, fps: int = 30,
                ken_burns: bool = True) -> None:
    """Make a silent video clip of ``image_path`` for ``duration`` seconds.

    With ``ken_burns`` a slow zoom is applied (nice, but slow on CPU). Without
    it, the image is shown statically (fast — recommended CPU path).
    """
    if ken_burns:
        frames = max(1, int(duration * fps))
        vf = (
            f"scale={width*2}:-1,"
            f"zoompan=z='min(zoom+0.0005,1.15)':d={frames}:"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={width}x{height}:fps={fps},"
            f"setsar=1"
        )
    else:
        # Static: just fit the image onto the frame. Very fast to encode.
        vf = (f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
              f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:white,setsar=1,fps={fps}")
    (
        ffmpeg.input(image_path, loop=1, t=duration)
        .output(str(out_path), vf=vf, pix_fmt="yuv420p", r=fps, an=None,
                vcodec="libx264", crf=18, preset="slow")
        .overwrite_output()
        .run(quiet=True)
    )


def build_video(
    slides: List[Tuple[str, float]],
    audio_path: str,
    out_path: str,
    cb: ProgressCb = None,
    width: int = 1920,
    height: int = 1080,
    fps: int = 30,
) -> str:
    """Build a narrated video from ``slides`` and ``audio_path``.

    Args:
        slides: list of ``(image_path, duration_seconds)`` in order.
        audio_path: the full narration audio to mux over the slideshow.
        out_path: output MP4 path.
        cb: progress callback.

    Returns:
        ``out_path``.
    """
    if not slides:
        raise ValueError("No slides to build a video from.")

    _emit(cb, f"Building video from {len(slides)} slide(s)...")
    ken_burns = getattr(config, "KEN_BURNS", True)
    tmp = Path(config.TEMP_DIR)
    uid = uuid.uuid4().hex[:8]  # unique prefix so concurrent runs never collide
    clip_paths: List[Path] = []
    for i, (img, dur) in enumerate(slides):
        clip = tmp / f"vg_{uid}_clip_{i:03d}.mp4"
        _slide_clip(img, max(0.5, dur), clip, width, height, fps, ken_burns)
        clip_paths.append(clip)

    # Concatenate the clips (video only), then add the narration audio.
    list_file = tmp / f"vg_{uid}_list.txt"
    with open(list_file, "w", encoding="utf-8") as fh:
        for c in clip_paths:
            fh.write(f"file '{str(c).replace(chr(92), '/')}'\n")

    try:
        video = ffmpeg.input(str(list_file), format="concat", safe=0)
        audio = ffmpeg.input(audio_path)
        (
            ffmpeg.output(video.video, audio.audio, out_path,
                          vcodec="libx264", acodec="aac", pix_fmt="yuv420p",
                          crf=18, preset="slow", shortest=None, r=fps)
            .overwrite_output()
            .run(quiet=True)
        )
    except ffmpeg.Error as exc:  # pragma: no cover
        stderr = exc.stderr.decode(errors="ignore") if exc.stderr else str(exc)
        raise RuntimeError(f"ffmpeg failed to build video: {stderr}") from exc
    finally:
        list_file.unlink(missing_ok=True)
        for c in clip_paths:
            c.unlink(missing_ok=True)

    _emit(cb, "Video assembled.")
    return out_path
