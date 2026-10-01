"""Command-line interface for the Voice Replacer / dubbing pipeline.

Examples
--------
Replace the voice in one video with the default reference sample::

    python cli.py input.mp4

Dub a video into Spanish using a specific reference voice::

    python cli.py input.mp4 --reference voice.wav --target es

Batch-process every video in a folder, with diarization + lip-sync::

    python cli.py ./clips --batch --diarize --lipsync --target hi

Run ``python cli.py --help`` for all options.
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import List, Optional

import config
import core

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}


def _gather_videos(target: Path, batch: bool) -> List[Path]:
    """Return the list of video files to process from a file or directory."""
    if target.is_dir():
        if not batch:
            raise SystemExit(
                f"{target} is a directory. Pass --batch to process all videos in it."
            )
        return sorted(p for p in target.iterdir()
                      if p.suffix.lower() in VIDEO_EXTS)
    if not target.is_file():
        raise SystemExit(f"Not found: {target}")
    return [target]


def _read_transcript(path: Optional[str]) -> Optional[List[str]]:
    """Read a transcript-override file (one corrected line per segment)."""
    if not path:
        return None
    return Path(path).read_text(encoding="utf-8").splitlines()


def build_parser() -> argparse.ArgumentParser:
    """Construct the CLI argument parser."""
    p = argparse.ArgumentParser(
        prog="voice-replacer",
        description="Replace or dub a video's voice with a cloned AI voice.",
    )
    p.add_argument("input", help="Input video file, or a folder with --batch.")
    p.add_argument("--batch", action="store_true",
                   help="Treat INPUT as a folder and process every video in it.")
    p.add_argument("--reference", "-r", default=None,
                   help="Reference voice sample (defaults to samples/monika.mp3).")
    p.add_argument("--source", "-s", default=config.AUTO_DETECT,
                   help="Spoken language code, or 'auto' (default).")
    p.add_argument("--target", "-t", default=None,
                   help="Dub into this language code (omit to keep original).")
    p.add_argument("--transcript", default=None,
                   help="Path to a corrected transcript (one line per segment). "
                        "Single-file mode only.")
    p.add_argument("--diarize", action="store_true",
                   help="Detect multiple speakers and clone each separately.")
    p.add_argument("--lipsync", action="store_true",
                   help="Re-animate the mouth to match the new voice (Wav2Lip).")
    p.add_argument("--quiet", "-q", action="store_true",
                   help="Only print final output paths and errors.")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point. Returns a process exit code."""
    args = build_parser().parse_args(argv)
    config.configure_logging()
    if args.quiet:
        logging.getLogger().setLevel(logging.WARNING)

    videos = _gather_videos(Path(args.input), args.batch)
    if not videos:
        print("No video files found to process.", file=sys.stderr)
        return 1

    transcript = _read_transcript(args.transcript)
    if transcript is not None and len(videos) > 1:
        raise SystemExit("--transcript can only be used with a single video.")

    def cb(msg: str) -> None:
        if not args.quiet:
            print(f"  {msg}")

    failures = 0
    for i, video in enumerate(videos, 1):
        print(f"[{i}/{len(videos)}] Processing {video.name} ...")
        try:
            out = core.process_video(
                str(video),
                reference_path=args.reference,
                source_lang=args.source,
                target_lang=args.target,
                transcript_override=transcript,
                use_diarization=args.diarize,
                use_lipsync=args.lipsync,
                cb=cb,
            )
            print(f"[ok] {video.name} -> {out}")
        except Exception as exc:  # noqa: BLE001 - report and keep going in batch
            failures += 1
            print(f"[ERROR] {video.name}: {exc}", file=sys.stderr)
            logging.getLogger("cli").debug("Failure detail", exc_info=True)

    if failures:
        print(f"\nDone with {failures} failure(s) of {len(videos)}.",
              file=sys.stderr)
        return 1
    print(f"\nAll {len(videos)} video(s) processed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
