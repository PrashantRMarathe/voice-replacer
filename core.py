"""Headless orchestration of the full voice-replacement / dubbing pipeline.

This is the single code path shared by the CLI (``cli.py``) and the REST API
(``api.py``), and it mirrors what the Gradio UI does in ``app.py`` — minus the
interactive transcript-editing step. Given a video it runs:

    extract audio -> transcribe -> [diarize] -> [translate] ->
    synthesize cloned voice -> [lip-sync] / merge -> final MP4

Every optional stage degrades gracefully: if diarization/lip-sync isn't set up,
or a stage fails, it falls back to the simpler behavior instead of aborting.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Callable, List, Optional

import config
import diarize
import lipsync
import pipeline
import translate
from pipeline import Segment

logger = logging.getLogger(__name__)

ProgressCb = Optional[Callable[[str], None]]


def _apply_transcript_override(
    segments: List[Segment], lines: List[str]
) -> List[Segment]:
    """Replace segment text with ``lines`` (one per segment), keeping timings."""
    lines = [ln for ln in lines if ln.strip()]
    if len(lines) != len(segments):
        raise ValueError(
            f"Transcript override has {len(lines)} line(s) but there are "
            f"{len(segments)} segment(s). Provide exactly one line per segment."
        )
    return [
        Segment(start=s.start, end=s.end, text=ln.strip(), speaker=s.speaker)
        for s, ln in zip(segments, lines)
    ]


def process_video(
    video_path: str,
    reference_path: Optional[str] = None,
    source_lang: str = config.AUTO_DETECT,
    target_lang: Optional[str] = None,
    transcript_override: Optional[List[str]] = None,
    use_diarization: bool = False,
    use_lipsync: bool = False,
    cb: ProgressCb = None,
) -> str:
    """Run the full pipeline on one video and return the final MP4 path.

    Args:
        video_path: Source video file.
        reference_path: Reference voice sample; defaults to
            ``config.DEFAULT_REFERENCE_SAMPLE``. Ignored per-speaker when
            diarization provides speaker-specific references.
        source_lang: Spoken language code, or ``config.AUTO_DETECT``.
        target_lang: Dub target language code, or ``None`` to keep the original.
        transcript_override: Optional list of corrected lines (one per segment).
        use_diarization: Detect speakers and clone each separately if available.
        use_lipsync: Re-animate the mouth with Wav2Lip if available.
        cb: Optional progress callback receiving status strings.

    Returns:
        Path to the final MP4 in ``config.OUTPUT_DIR``.
    """
    def _emit(msg: str) -> None:
        logger.info(msg)
        if cb is not None:
            cb(msg)

    if not Path(video_path).is_file():
        raise FileNotFoundError(f"Video not found: {video_path}")

    reference = reference_path or str(config.DEFAULT_REFERENCE_SAMPLE)
    if not Path(reference).is_file():
        raise FileNotFoundError(
            f"Reference voice sample not found: {reference}. Provide one or "
            f"place it at {config.DEFAULT_REFERENCE_SAMPLE}."
        )

    run_id = pipeline.new_run_id()
    try:
        audio_path = pipeline.extract_audio(video_path, run_id, cb)
        segments, detected = pipeline.transcribe(audio_path, source_lang, cb)
        if not segments:
            raise ValueError("No speech detected in the video.")

        # Optional diarization.
        if use_diarization:
            available, reason = diarize.is_available()
            if available:
                segments, speakers = diarize.assign_speakers(
                    segments, audio_path, cb)
                _emit(f"Speakers detected: {', '.join(speakers) or 'none'}")
            else:
                _emit(f"Diarization skipped: {reason}")

        # Optional transcript correction.
        if transcript_override is not None:
            segments = _apply_transcript_override(segments, transcript_override)

        # Decide language / translation.
        effective_source = (
            detected if source_lang == config.AUTO_DETECT else source_lang
        )
        want_translation = bool(target_lang) and (
            config.base_lang(target_lang)
            != config.base_lang(effective_source or config.LANGUAGE)
        )
        if want_translation:
            segments = translate.translate_segments(
                segments, effective_source or config.AUTO_DETECT,
                target_lang, cb)
            synth_lang = target_lang
        else:
            synth_lang = effective_source or config.LANGUAGE

        xtts_lang = config.to_xtts_code(synth_lang)
        if xtts_lang is None:
            raise ValueError(
                f"The voice engine cannot speak language '{synth_lang}'. "
                f"Choose a supported target language."
            )

        # Per-speaker references when diarized.
        speaker_refs = None
        if any(getattr(s, "speaker", None) for s in segments):
            try:
                speaker_refs = diarize.extract_speaker_references(
                    audio_path, segments, run_id, cb)
            except RuntimeError as exc:
                _emit(f"Speaker reference build failed ({exc}); using default voice.")

        generated = pipeline.generate_voice(
            segments, reference, run_id, xtts_lang, cb, speaker_refs)

        # Lip-sync or plain merge.
        final_path = None
        if use_lipsync:
            available, reason = lipsync.is_available()
            if available:
                try:
                    final_path = lipsync.apply_lipsync(
                        video_path, generated, run_id, cb)
                except RuntimeError as exc:
                    _emit(f"Lip-sync failed ({exc}); merging audio only.")
            else:
                _emit(f"Lip-sync skipped: {reason}")
        if final_path is None:
            final_path = pipeline.merge_audio_video(
                video_path, generated, run_id, cb)

        return final_path
    finally:
        pipeline.cleanup(run_id, cb)
        # The extracted source audio uses the same run_id prefix, so cleanup
        # above already removed it.
