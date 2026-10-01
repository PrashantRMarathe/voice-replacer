"""Optional speaker diarization via pyannote.audio.

Splits the audio into speaker turns so multi-speaker videos can clone each
person separately. The "best" part: each speaker's cloning reference is
extracted automatically from their own longest, cleanest turns in the source
audio — so no manual per-speaker voice uploads are needed.

The pyannote model is gated on Hugging Face (needs a token + accepted license),
so the model call is isolated and guarded. The assignment and reference-
extraction logic below are pure/ffmpeg-only so they can be tested without the
gated model. If diarization is unavailable, callers fall back to single-speaker.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

import ffmpeg

import config
from pipeline import Segment

logger = logging.getLogger(__name__)

ProgressCb = Optional[Callable[[str], None]]

# A diarization "turn": (start_s, end_s, speaker_label).
Turn = Tuple[float, float, str]

_pipeline = None  # cached pyannote pipeline


def _emit(cb: ProgressCb, message: str) -> None:
    logger.info(message)
    if cb is not None:
        cb(message)


def is_available() -> Tuple[bool, str]:
    """Return ``(available, reason)`` describing whether diarization can run."""
    if not config.ENABLE_DIARIZATION:
        return False, "Diarization is disabled (set ENABLE_DIARIZATION = True)."
    import importlib.util

    # find_spec on a submodule imports the parent, which raises (not returns
    # None) when the parent package is absent — treat either as "not installed".
    try:
        spec = importlib.util.find_spec("pyannote.audio")
    except ModuleNotFoundError:
        spec = None
    if spec is None:
        return False, "pyannote.audio is not installed (pip install pyannote.audio)."
    if not config.HF_TOKEN:
        return False, ("No Hugging Face token set (config.HF_TOKEN or the "
                       "HF_TOKEN env var). The diarization model is gated.")
    return True, "ok"


# --------------------------------------------------------------------------- #
# Pure assignment logic (testable without pyannote)
# --------------------------------------------------------------------------- #
def _overlap(a_start: float, a_end: float, b_start: float, b_end: float) -> float:
    """Return the overlap in seconds between intervals [a] and [b]."""
    return max(0.0, min(a_end, b_end) - max(a_start, b_start))


def assign_from_turns(
    segments: List[Segment], turns: List[Turn]
) -> Tuple[List[Segment], List[str]]:
    """Label each segment with the speaker it overlaps most, in-place.

    Args:
        segments: Transcript segments (``speaker`` is set on each).
        turns: Diarization turns as ``(start, end, speaker)`` tuples.

    Returns:
        ``(segments, speakers)`` where ``speakers`` is the sorted list of
        distinct speaker labels actually assigned.
    """
    for seg in segments:
        best_spk, best_ov = None, 0.0
        for t_start, t_end, spk in turns:
            ov = _overlap(seg.start, seg.end, t_start, t_end)
            if ov > best_ov:
                best_ov, best_spk = ov, spk
        # If no turn overlapped (rare), inherit nothing; left as None and the
        # caller falls back to the default reference voice for that segment.
        seg.speaker = best_spk
    speakers = sorted({s.speaker for s in segments if s.speaker})
    return segments, speakers


def plan_speaker_references(
    segments: List[Segment], max_seconds: float
) -> Dict[str, List[Tuple[float, float]]]:
    """Choose which time spans to use as each speaker's cloning reference.

    For each speaker, picks their longest segments (cleanest, most speech)
    until ``max_seconds`` of audio is collected. Pure — returns a plan of
    ``{speaker: [(start, end), ...]}`` that ``extract_speaker_references`` cuts.
    """
    by_speaker: Dict[str, List[Segment]] = {}
    for seg in segments:
        if seg.speaker:
            by_speaker.setdefault(seg.speaker, []).append(seg)

    plan: Dict[str, List[Tuple[float, float]]] = {}
    for spk, segs in by_speaker.items():
        segs_sorted = sorted(segs, key=lambda s: s.end - s.start, reverse=True)
        spans: List[Tuple[float, float]] = []
        total = 0.0
        for s in segs_sorted:
            if total >= max_seconds:
                break
            spans.append((s.start, s.end))
            total += s.end - s.start
        # Keep spans in chronological order for a natural-sounding reference.
        plan[spk] = sorted(spans)
    return plan


# --------------------------------------------------------------------------- #
# ffmpeg reference extraction (testable without pyannote)
# --------------------------------------------------------------------------- #
def extract_speaker_references(
    audio_path: str,
    segments: List[Segment],
    run_id: str,
    cb: ProgressCb = None,
) -> Dict[str, str]:
    """Cut a per-speaker reference WAV from ``audio_path`` using each speaker's
    own turns. Returns ``{speaker: reference_wav_path}``.
    """
    plan = plan_speaker_references(segments, config.SPEAKER_REF_SECONDS)
    refs: Dict[str, str] = {}
    for spk, spans in plan.items():
        if not spans:
            continue
        out_path = config.TEMP_DIR / f"{run_id}_ref_{spk}.wav"
        _cut_and_concat(audio_path, spans, out_path)
        refs[spk] = str(out_path)
        _emit(cb, f"Built reference for {spk} ({len(spans)} span(s)).")
    return refs


def _cut_and_concat(
    audio_path: str, spans: List[Tuple[float, float]], out_path: Path
) -> None:
    """Extract ``spans`` from ``audio_path`` and concatenate them into one WAV."""
    inp = ffmpeg.input(audio_path)
    clips = [
        inp.filter("atrim", start=s, end=e).filter("asetpts", "PTS-STARTPTS")
        for s, e in spans
    ]
    try:
        if len(clips) == 1:
            stream = clips[0]
        else:
            stream = ffmpeg.concat(*clips, v=0, a=1)
        (
            stream.output(str(out_path), acodec="pcm_s16le", ac=1,
                          ar=config.SAMPLE_RATE)
            .overwrite_output()
            .run(quiet=True)
        )
    except ffmpeg.Error as exc:  # pragma: no cover
        stderr = exc.stderr.decode(errors="ignore") if exc.stderr else str(exc)
        raise RuntimeError(f"ffmpeg failed to build speaker reference: {stderr}") from exc


# --------------------------------------------------------------------------- #
# Gated model call (not unit-tested here)
# --------------------------------------------------------------------------- #
def _load_pipeline():  # pragma: no cover - requires gated model + token
    """Load and cache the pyannote diarization pipeline."""
    global _pipeline
    if _pipeline is None:
        from pyannote.audio import Pipeline

        logger.info("Loading diarization model '%s' ...", config.DIARIZATION_MODEL)
        _pipeline = Pipeline.from_pretrained(
            config.DIARIZATION_MODEL, use_auth_token=config.HF_TOKEN
        )
        try:
            import torch

            _pipeline.to(torch.device(config.DEVICE))
        except Exception:  # noqa: BLE001 - stay on CPU if moving fails
            logger.warning("Could not move diarization pipeline to %s.",
                           config.DEVICE)
    return _pipeline


def diarize(audio_path: str, cb: ProgressCb = None) -> List[Turn]:  # pragma: no cover
    """Run diarization on ``audio_path``, returning speaker turns."""
    available, reason = is_available()
    if not available:
        raise RuntimeError(f"Diarization unavailable: {reason}")

    _emit(cb, "Detecting speakers (diarization)...")
    pipeline = _load_pipeline()
    annotation = pipeline(audio_path)
    turns: List[Turn] = [
        (float(turn.start), float(turn.end), str(speaker))
        for turn, _, speaker in annotation.itertracks(yield_label=True)
    ]
    return turns


def assign_speakers(
    segments: List[Segment], audio_path: str, cb: ProgressCb = None
) -> Tuple[List[Segment], List[str]]:  # pragma: no cover - wraps gated model
    """Run diarization and label each segment with its speaker."""
    turns = diarize(audio_path, cb)
    segments, speakers = assign_from_turns(segments, turns)
    _emit(cb, f"Diarization complete: {len(speakers)} speaker(s) detected.")
    return segments, speakers
