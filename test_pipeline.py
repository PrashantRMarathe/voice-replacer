"""Smoke test for the Voice Replacer pipeline.

Runs the full pipeline on a short (~10s) synthetic sample video and verifies
the output exists and is a valid MP4. Models (Whisper, XTTS) and ffmpeg are
required; the test skips gracefully if ffmpeg or the heavy deps are missing so
it can still be collected in a lightweight CI environment.

Run with:
    pytest test_pipeline.py -v
or standalone:
    python test_pipeline.py
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

import config
import pipeline

FFMPEG_AVAILABLE = shutil.which("ffmpeg") is not None


def _make_sample_video(path: Path, seconds: int = 10) -> None:
    """Create a short test MP4 with a color pattern + spoken-tone audio.

    Uses ffmpeg's lavfi sources so no external asset is needed. The audio is a
    sine tone (not real speech) — enough to exercise extract/merge; Whisper may
    return zero segments for it, which the test accounts for.
    """
    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", f"testsrc=duration={seconds}:size=320x240:rate=15",
            "-f", "lavfi", "-i", f"sine=frequency=220:duration={seconds}",
            "-c:v", "libx264", "-c:a", "aac", "-shortest",
            str(path),
        ],
        check=True,
        capture_output=True,
    )


def _is_valid_mp4(path: Path) -> bool:
    """Return True if ffprobe can read a video stream from ``path``."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=codec_type", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    return "video" in result.stdout


@pytest.mark.skipif(not FFMPEG_AVAILABLE, reason="ffmpeg not installed")
def test_full_pipeline_smoke(tmp_path: Path) -> None:
    """End-to-end smoke test: extract -> transcribe -> generate -> merge."""
    reference = config.DEFAULT_REFERENCE_SAMPLE
    if not reference.is_file():
        pytest.skip(f"Reference sample missing: {reference}")

    sample_video = tmp_path / "sample.mp4"
    _make_sample_video(sample_video, seconds=10)
    assert sample_video.is_file()

    run_id = pipeline.new_run_id()

    # Step 1: extract audio
    audio_path = pipeline.extract_audio(str(sample_video), run_id)
    assert Path(audio_path).is_file()

    # Step 2: transcribe (may be empty for a pure tone)
    segments, _detected = pipeline.transcribe(audio_path)

    # If no speech was detected, synthesize a fixed line so we still exercise
    # generate_voice + merge_audio_video end to end.
    if not segments:
        segments = [pipeline.Segment(start=0.0, end=3.0,
                                     text="This is a smoke test.")]

    # Step 3: generate cloned voice
    generated = pipeline.generate_voice(segments, str(reference), run_id)
    assert Path(generated).is_file()

    # Step 4: merge
    final = pipeline.merge_audio_video(str(sample_video), generated, run_id)
    assert Path(final).is_file(), "Final MP4 was not created"
    assert _is_valid_mp4(Path(final)), "Output is not a valid MP4"

    # Cleanup temp files
    pipeline.cleanup(run_id)

    # Remove the produced output so tests stay idempotent.
    Path(final).unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
