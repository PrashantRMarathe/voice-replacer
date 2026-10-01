"""Mode 2 CLI — create a narrated infographic video from a document.

Usage:
    python make_video.py mydoc.txt
    python make_video.py mydoc.txt --reference samples/monika.mp3
    python make_video.py notes.docx --language en

For a quick CPU test without the big LLM download, set ENABLE_LLM_BRAIN = False
in config.py (uses the fast built-in heuristic instead).
"""

from __future__ import annotations

import argparse
import sys

import config
import create


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="make-video",
        description="Create a narrated infographic video from a document.")
    p.add_argument("document", help="Path to .txt / .md / .docx / .pdf")
    p.add_argument("--reference", "-r", default=None,
                   help="Reference voice sample (defaults to samples/monika.mp3).")
    p.add_argument("--language", "-l", default=None, help="Narration language code.")
    args = p.parse_args(argv)

    config.configure_logging()

    def cb(msg: str) -> None:
        print(f"  {msg}")

    print(f"Creating video from: {args.document}")
    try:
        out = create.create_from_document(
            args.document,
            reference_path=args.reference,
            language=args.language,
            cb=cb,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1
    print(f"\nDONE -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
