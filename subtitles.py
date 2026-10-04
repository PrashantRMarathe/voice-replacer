"""Subtitle generation (SRT / WebVTT) from timed transcript segments."""

from __future__ import annotations

import logging
import os
import subprocess
from pathlib import Path
from typing import List

import config
from pipeline import Segment

logger = logging.getLogger(__name__)


def _fmt_timestamp(seconds: float, vtt: bool = False) -> str:
    """Format ``seconds`` as an SRT (``HH:MM:SS,mmm``) or VTT (``.mmm``) stamp."""
    if seconds < 0:
        seconds = 0.0
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    sep = "." if vtt else ","
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def build_srt(segments: List[Segment]) -> str:
    """Return the SRT text for ``segments``."""
    blocks = []
    for i, seg in enumerate(segments, start=1):
        if not seg.text.strip():
            continue
        start = _fmt_timestamp(seg.start)
        end = _fmt_timestamp(max(seg.end, seg.start + 0.1))
        blocks.append(f"{i}\n{start} --> {end}\n{seg.text.strip()}")
    return "\n\n".join(blocks) + ("\n" if blocks else "")


def build_vtt(segments: List[Segment]) -> str:
    """Return the WebVTT text for ``segments``."""
    lines = ["WEBVTT", ""]
    for seg in segments:
        if not seg.text.strip():
            continue
        start = _fmt_timestamp(seg.start, vtt=True)
        end = _fmt_timestamp(max(seg.end, seg.start + 0.1), vtt=True)
        lines.append(f"{start} --> {end}")
        lines.append(seg.text.strip())
        lines.append("")
    return "\n".join(lines)


def write_subtitles(
    segments: List[Segment], base_path: str, fmt: str = "both"
) -> List[str]:
    """Write subtitle file(s) for ``segments`` next to ``base_path``.

    Args:
        segments: Timed (and possibly translated) transcript segments.
        base_path: Output video path; subtitles share its stem (e.g. for
            ``out/clip.mp4`` -> ``out/clip.srt`` / ``out/clip.vtt``).
        fmt: ``"srt"``, ``"vtt"``, or ``"both"``.

    Returns:
        List of written subtitle file paths.
    """
    stem = Path(base_path).with_suffix("")
    written: List[str] = []
    if fmt in ("srt", "both"):
        p = f"{stem}.srt"
        Path(p).write_text(build_srt(segments), encoding="utf-8")
        written.append(p)
    if fmt in ("vtt", "both"):
        p = f"{stem}.vtt"
        Path(p).write_text(build_vtt(segments), encoding="utf-8")
        written.append(p)
    return written


def burn_into_video(video_path: str, srt_path: str, out_path: str) -> str:
    """Burn ``srt_path`` subtitles into ``video_path`` -> ``out_path``.

    Runs ffmpeg from the subtitle's own folder and references it by filename, so
    the ``subtitles`` filter works on Windows and Linux without path-escaping
    issues. Timing is exact (the .srt came from the final audio). Re-encodes
    video; audio is copied. Returns ``out_path``.
    """
    srt = Path(srt_path)
    style = getattr(config, "SUBTITLE_STYLE", "")
    vf = f"subtitles={srt.name}"
    if style:
        vf += f":force_style='{style}'"
    cmd = [
        "ffmpeg", "-y",
        "-i", os.path.abspath(video_path),
        "-vf", vf,
        "-c:a", "copy",
        os.path.abspath(out_path),
    ]
    proc = subprocess.run(cmd, cwd=str(srt.parent), capture_output=True, text=True)
    if proc.returncode != 0 or not Path(out_path).is_file():
        tail = "\n".join((proc.stderr or "").splitlines()[-6:])
        raise RuntimeError(f"ffmpeg failed to burn subtitles:\n{tail}")
    return out_path
