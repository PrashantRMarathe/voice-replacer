"""Core processing pipeline for the Voice Replacer tool.

Flow:
    extract_audio -> transcribe -> generate_voice -> merge_audio_video

Each function is independent and typed so it can be tested in isolation.
Heavy models (Whisper, XTTS) are lazily loaded and cached so repeated calls
within a session do not reload weights.
"""

from __future__ import annotations

import logging
import subprocess
import uuid
import wave
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List, Optional, Tuple

import ffmpeg

import config

logger = logging.getLogger(__name__)

# Type alias for an optional progress/status callback: (message) -> None
ProgressCb = Optional[Callable[[str], None]]


@dataclass
class Segment:
    """A single transcribed span of speech."""

    start: float  # seconds
    end: float    # seconds
    text: str
    speaker: Optional[str] = None  # diarization label, e.g. "SPEAKER_00"


# --------------------------------------------------------------------------- #
# Lazy model caches
# --------------------------------------------------------------------------- #
_whisper_model = None
_whisper_backend = None  # which backend the cached model is ("faster"/"openai")


def _emit(cb: ProgressCb, message: str) -> None:
    """Log and forward a status message to an optional UI callback."""
    logger.info(message)
    if cb is not None:
        cb(message)


def new_run_id() -> str:
    """Return a short unique id used to namespace temp files for a run."""
    return uuid.uuid4().hex[:8]


# --------------------------------------------------------------------------- #
# Step 1: extract audio
# --------------------------------------------------------------------------- #
def extract_audio(video_path: str, run_id: str, cb: ProgressCb = None) -> str:
    """Extract the audio track of ``video_path`` to a mono WAV file.

    Args:
        video_path: Path to the source MP4 video.
        run_id: Unique id used to name the temp output file.
        cb: Optional progress callback.

    Returns:
        Path to the extracted WAV file (sample rate = ``config.SAMPLE_RATE``).
    """
    _emit(cb, "Extracting audio from video...")
    out_path = config.TEMP_DIR / f"{run_id}_extracted.wav"
    try:
        (
            ffmpeg.input(video_path)
            .output(
                str(out_path),
                acodec="pcm_s16le",
                ac=1,
                ar=config.SAMPLE_RATE,
                vn=None,
            )
            .overwrite_output()
            .run(quiet=True)
        )
    except ffmpeg.Error as exc:  # pragma: no cover - depends on ffmpeg
        stderr = exc.stderr.decode(errors="ignore") if exc.stderr else str(exc)
        raise RuntimeError(f"ffmpeg failed to extract audio: {stderr}") from exc
    return str(out_path)


# --------------------------------------------------------------------------- #
# Step 2: transcribe
# --------------------------------------------------------------------------- #
def _resolve_whisper_backend() -> str:
    """Return the usable transcription backend, honoring config + fallback.

    Prefers ``config.WHISPER_BACKEND``; if its package isn't importable, falls
    back to the other backend so transcription still works.
    """
    import importlib.util

    preferred = config.WHISPER_BACKEND
    pkg = {"faster": "faster_whisper", "openai": "whisper"}
    if importlib.util.find_spec(pkg.get(preferred, "")) is not None:
        return preferred

    other = "openai" if preferred == "faster" else "faster"
    if importlib.util.find_spec(pkg[other]) is not None:
        logger.warning("Whisper backend '%s' unavailable; using '%s'.",
                       preferred, other)
        return other
    raise RuntimeError(
        "No Whisper backend available. Install one of: "
        "'faster-whisper' or 'openai-whisper'."
    )


def _load_whisper():
    """Load and cache the Whisper model for the resolved backend."""
    global _whisper_model, _whisper_backend
    backend = _resolve_whisper_backend()
    if _whisper_model is not None and _whisper_backend == backend:
        return _whisper_model

    if backend == "faster":
        from faster_whisper import WhisperModel

        logger.info("Loading faster-whisper '%s' on %s (%s) ...",
                    config.WHISPER_MODEL, config.DEVICE,
                    config.WHISPER_COMPUTE_TYPE)
        _whisper_model = WhisperModel(
            config.WHISPER_MODEL,
            device=config.DEVICE,
            compute_type=config.WHISPER_COMPUTE_TYPE,
        )
    else:
        import whisper  # imported lazily to keep startup fast

        logger.info("Loading openai-whisper '%s' on %s ...",
                    config.WHISPER_MODEL, config.DEVICE)
        _whisper_model = whisper.load_model(
            config.WHISPER_MODEL, device=config.DEVICE
        )
    _whisper_backend = backend
    return _whisper_model


def transcribe(
    audio_path: str,
    language: Optional[str] = None,
    cb: ProgressCb = None,
) -> Tuple[List[Segment], Optional[str]]:
    """Transcribe ``audio_path`` with Whisper, returning timed segments.

    Args:
        audio_path: Path to a WAV file to transcribe.
        language: XTTS/Whisper source language code, or ``None`` /
            ``config.AUTO_DETECT`` to let Whisper auto-detect it. ``None`` means
            auto-detect.
        cb: Optional progress callback.

    Returns:
        A ``(segments, detected_language)`` tuple. ``detected_language`` is the
        Whisper 2-letter code (e.g. ``"en"``), either the one passed in or the
        one Whisper detected; it may be ``None`` if unavailable.
    """
    if language in (None, config.AUTO_DETECT):
        whisper_lang = None  # Whisper auto-detects when language is None.
        _emit(cb, "Transcribing audio with Whisper (auto-detecting language)...")
    else:
        whisper_lang = config.to_whisper_code(language)
        _emit(cb, f"Transcribing audio with Whisper ({whisper_lang})...")

    model = _load_whisper()
    if _whisper_backend == "faster":
        segments, detected = _transcribe_faster(model, audio_path, whisper_lang)
    else:
        segments, detected = _transcribe_openai(model, audio_path, whisper_lang)

    if whisper_lang is None and detected:
        _emit(cb, f"Detected source language: {detected}")
    _emit(cb, f"Transcription complete: {len(segments)} segment(s).")
    return segments, (detected or whisper_lang)


def _transcribe_openai(
    model, audio_path: str, whisper_lang: Optional[str]
) -> Tuple[List[Segment], Optional[str]]:
    """Run the openai-whisper backend and normalize its output."""
    result = model.transcribe(audio_path, language=whisper_lang, verbose=False)
    segments = [
        Segment(start=float(s["start"]), end=float(s["end"]),
                text=str(s["text"]).strip())
        for s in result.get("segments", [])
        if str(s["text"]).strip()
    ]
    return segments, result.get("language")


def _transcribe_faster(
    model, audio_path: str, whisper_lang: Optional[str]
) -> Tuple[List[Segment], Optional[str]]:
    """Run the faster-whisper backend and normalize its output.

    faster-whisper returns a lazy generator of segment objects plus an ``info``
    object carrying the detected language; iterate to materialize them.
    """
    seg_iter, info = model.transcribe(audio_path, language=whisper_lang)
    segments = [
        Segment(start=float(s.start), end=float(s.end), text=s.text.strip())
        for s in seg_iter
        if s.text.strip()
    ]
    detected = getattr(info, "language", None)
    return segments, detected


# --------------------------------------------------------------------------- #
# Step 3: generate voice
# --------------------------------------------------------------------------- #

def _write_silence(path: Path, duration_s: float) -> None:
    """Write ``duration_s`` seconds of mono silence as a WAV file."""
    n_frames = max(0, int(duration_s * config.SAMPLE_RATE))
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(config.SAMPLE_RATE)
        wf.writeframes(b"\x00\x00" * n_frames)


def _wav_duration(path: str) -> float:
    """Return the duration in seconds of a WAV file."""
    with wave.open(path, "rb") as wf:
        return wf.getnframes() / float(wf.getframerate())


def _atempo_chain(tempo: float) -> List[str]:
    """Return a list of ``atempo=<f>`` factors whose product equals ``tempo``.

    ffmpeg's ``atempo`` filter only accepts a factor in ``[0.5, 2.0]`` per
    instance, so larger changes must be split across chained filters. In this
    project ``tempo`` is already clamped to a narrow range, but the split keeps
    the helper correct for any input.
    """
    factors: List[float] = []
    remaining = tempo
    while remaining > 2.0:
        factors.append(2.0)
        remaining /= 2.0
    while remaining < 0.5:
        factors.append(0.5)
        remaining /= 0.5
    factors.append(remaining)
    return [f"atempo={f:.6f}" for f in factors]


def _fit_duration(src: Path, dst: Path, target_s: float) -> float:
    """Time-stretch ``src`` (pitch-preserving) to ~``target_s`` seconds.

    The stretch factor is clamped to ``config.MIN_TEMPO``/``config.MAX_TEMPO``
    so corrections never distort the voice; a segment needing more than the
    clamp allows is fit as close as possible. To keep the voice natural, a
    segment is left completely untouched when it is already within either
    ``config.FIT_MIN_DELTA_S`` seconds or ``config.FIT_TOLERANCE_RATIO`` of its
    slot — only clearly-off segments get a gentle nudge.

    Returns the duration of the written file in seconds.
    """
    actual = _wav_duration(str(src))
    if target_s <= 0 or actual <= 0:
        _copy_wav(src, dst)
        return actual
    if abs(actual - target_s) < config.FIT_MIN_DELTA_S:
        _copy_wav(src, dst)
        return actual
    # Within the tolerance band -> play at XTTS's natural pace (no stretch).
    if abs(actual - target_s) <= config.FIT_TOLERANCE_RATIO * target_s:
        _copy_wav(src, dst)
        return actual

    # tempo > 1 speeds up (shortens); output duration = actual / tempo.
    tempo = actual / target_s
    tempo = max(config.MIN_TEMPO, min(config.MAX_TEMPO, tempo))

    af = ",".join(_atempo_chain(tempo))
    try:
        (
            ffmpeg.input(str(src))
            .output(str(dst), af=af, acodec="pcm_s16le", ac=1,
                    ar=config.SAMPLE_RATE)
            .overwrite_output()
            .run(quiet=True)
        )
    except ffmpeg.Error as exc:  # pragma: no cover
        stderr = exc.stderr.decode(errors="ignore") if exc.stderr else str(exc)
        raise RuntimeError(f"ffmpeg failed to time-stretch audio: {stderr}") from exc
    return _wav_duration(str(dst))


def _copy_wav(src: Path, dst: Path) -> None:
    """Copy ``src`` to ``dst`` (no-op if they are the same path)."""
    if src.resolve() == dst.resolve():
        return
    import shutil

    shutil.copyfile(src, dst)


def generate_voice(
    segments: List[Segment],
    reference_sample_path: str,
    run_id: str,
    language: Optional[str] = None,
    cb: ProgressCb = None,
    speaker_refs: Optional[dict] = None,
) -> str:
    """Generate cloned-voice audio for ``segments`` and concatenate it.

    Audio is generated one segment at a time to preserve rough timing.
    Silence is inserted between segments to match the gaps present in the
    original transcript timestamps.

    Args:
        segments: Timed transcript segments (text may be user-edited).
        reference_sample_path: Default reference voice sample (MP3/WAV), used
            for any segment without a per-speaker reference.
        run_id: Unique id used to name temp files.
        language: XTTS language code to synthesize in (defaults to config).
        cb: Optional progress callback.
        speaker_refs: Optional ``{speaker_label: reference_wav}`` map. When a
            segment's ``speaker`` has an entry, that per-speaker reference is
            used so multi-speaker videos clone each voice separately.

    Returns:
        Path to the concatenated WAV file in the cloned voice.
    """
    if not segments:
        raise ValueError("No segments to synthesize.")

    import tts as tts_backends

    lang = language or config.LANGUAGE
    speaker_refs = speaker_refs or {}
    backend = tts_backends.get_backend()
    _emit(cb, f"Using TTS backend: {backend.name}")
    part_paths: List[Path] = []
    # Position on the OUTPUT timeline so far. We align each new segment to where
    # it starts in the original video, so drift from earlier segments is never
    # carried forward — the output stays locked to the source timeline.
    timeline_pos = 0.0
    total_stretch = 0.0  # cumulative seconds of correction applied (for logging)

    for i, seg in enumerate(segments):
        _emit(cb, f"Generating voice {i + 1}/{len(segments)} ...")

        # Insert a silence gap so this segment begins at its original start time,
        # measured against what we have actually emitted so far.
        gap = seg.start - timeline_pos
        if gap > 0.01:
            silence_path = config.TEMP_DIR / f"{run_id}_gap_{i:04d}.wav"
            _write_silence(silence_path, gap)
            part_paths.append(silence_path)
            timeline_pos += gap

        raw_path = config.TEMP_DIR / f"{run_id}_raw_{i:04d}.wav"
        # Use this segment's speaker-specific reference if we have one.
        ref = speaker_refs.get(seg.speaker, reference_sample_path)
        backend.synth_to_file(
            text=seg.text,
            speaker_wav=ref,
            language=lang,
            out_path=str(raw_path),
        )

        seg_path = config.TEMP_DIR / f"{run_id}_seg_{i:04d}.wav"
        slot = seg.end - seg.start
        if config.FIT_SEGMENT_TIMING and slot > 0:
            raw_dur = _wav_duration(str(raw_path))
            fitted_dur = _fit_duration(raw_path, seg_path, slot)
            total_stretch += abs(raw_dur - fitted_dur)
        else:
            _copy_wav(raw_path, seg_path)
            fitted_dur = _wav_duration(str(seg_path))

        part_paths.append(seg_path)
        timeline_pos += fitted_dur

    if config.FIT_SEGMENT_TIMING:
        _emit(cb, f"Timing fit applied (~{total_stretch:.2f}s total correction).")

    # Concatenate all parts (silences + speech) into a single WAV.
    _emit(cb, "Concatenating generated audio...")
    out_path = config.TEMP_DIR / f"{run_id}_generated.wav"
    _concat_wavs(part_paths, out_path)
    return str(out_path)


def _concat_wavs(parts: List[Path], out_path: Path) -> None:
    """Concatenate a list of same-format WAV files into ``out_path``.

    Uses ffmpeg's concat demuxer for robustness across sample rates/codecs.
    """
    list_file = out_path.with_suffix(".txt")
    with open(list_file, "w", encoding="utf-8") as fh:
        for p in parts:
            # ffmpeg concat list requires forward slashes / escaped quotes.
            safe = str(p).replace("\\", "/").replace("'", "'\\''")
            fh.write(f"file '{safe}'\n")
    try:
        (
            ffmpeg.input(str(list_file), format="concat", safe=0)
            .output(str(out_path), acodec="pcm_s16le", ac=1,
                    ar=config.SAMPLE_RATE)
            .overwrite_output()
            .run(quiet=True)
        )
    except ffmpeg.Error as exc:  # pragma: no cover
        stderr = exc.stderr.decode(errors="ignore") if exc.stderr else str(exc)
        raise RuntimeError(f"ffmpeg failed to concat audio: {stderr}") from exc
    finally:
        list_file.unlink(missing_ok=True)


# --------------------------------------------------------------------------- #
# Step 4: merge audio + video
# --------------------------------------------------------------------------- #
def merge_audio_video(
    video_path: str,
    new_audio_path: str,
    run_id: str,
    cb: ProgressCb = None,
) -> str:
    """Replace the audio track of ``video_path`` with ``new_audio_path``.

    The video stream is copied untouched. If the new audio is shorter than
    the video it is padded with silence; if longer, it is trimmed. The output
    is written to ``config.OUTPUT_DIR``.

    Args:
        video_path: Source MP4 whose video stream is kept.
        new_audio_path: WAV file to use as the new audio track.
        run_id: Unique id used to name the output file.
        cb: Optional progress callback.

    Returns:
        Path to the final MP4 file.
    """
    _emit(cb, "Merging new audio with original video...")
    out_path = config.OUTPUT_DIR / f"{run_id}_final.mp4"

    video_in = ffmpeg.input(video_path)
    audio_in = ffmpeg.input(new_audio_path)

    try:
        # -shortest ensures the muxer stops at whichever stream ends first;
        # apad pads the audio so it is never shorter than the video, and
        # -shortest then trims any overrun -> audio matches video length.
        audio_padded = audio_in.audio.filter("apad")
        (
            ffmpeg.output(
                video_in.video,
                audio_padded,
                str(out_path),
                vcodec="copy",
                acodec="aac",
                shortest=None,
            )
            .overwrite_output()
            .run(quiet=True)
        )
    except ffmpeg.Error as exc:  # pragma: no cover
        stderr = exc.stderr.decode(errors="ignore") if exc.stderr else str(exc)
        raise RuntimeError(f"ffmpeg failed to merge audio/video: {stderr}") from exc

    return str(out_path)


# --------------------------------------------------------------------------- #
# Cleanup
# --------------------------------------------------------------------------- #
def cleanup(run_id: str, cb: ProgressCb = None) -> None:
    """Remove all temp files created for ``run_id``.

    Args:
        run_id: The run id whose intermediate temp files should be deleted.
        cb: Optional progress callback.
    """
    removed = 0
    for path in config.TEMP_DIR.glob(f"{run_id}_*"):
        try:
            path.unlink()
            removed += 1
        except OSError:
            logger.warning("Could not remove temp file: %s", path)
    _emit(cb, f"Cleaned up {removed} temp file(s).")
