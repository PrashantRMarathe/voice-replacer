"""Mode 2 orchestrator: a document becomes a narrated infographic video.

Flow:
    read document -> AI builds spec + narration -> render infographic image ->
    narrate (cloned voice) -> clean audio -> build video -> subtitles

Mirrors core.py (Mode 1) but for created-from-scratch content. Every optional
stage degrades gracefully, so a run always produces a video.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Callable, Optional

import config
import design
import docread
import pipeline
import render
import spec as spec_mod
import subtitles
import videogen

logger = logging.getLogger(__name__)
ProgressCb = Optional[Callable[[str], None]]


def _narrate(text: str, reference: str, language: str, run_id: str,
             cb: ProgressCb) -> str:
    """Synthesize narration audio for ``text`` and clean it up."""
    import tts as tts_backends

    def _emit(m):
        logger.info(m)
        if cb:
            cb(m)

    backend = tts_backends.get_backend()
    _emit(f"Narrating with TTS backend: {backend.name}")
    raw = config.TEMP_DIR / f"{run_id}_narration_raw.wav"
    backend.synth_to_file(text=text, speaker_wav=reference,
                          language=language, out_path=str(raw))

    stage = raw
    if config.ENABLE_VOICE_ENHANCE:
        import enhance as voice_enhance

        ok, _ = voice_enhance.is_available()
        if ok:
            try:
                enh = config.TEMP_DIR / f"{run_id}_narration_enh.wav"
                voice_enhance.enhance_audio(str(raw), str(enh), cb)
                stage = enh
            except Exception as exc:  # noqa: BLE001
                _emit(f"Enhancement skipped ({exc}).")

    out = config.TEMP_DIR / f"{run_id}_narration.wav"
    if config.ENABLE_AUDIO_CLEANUP and config.AUDIO_FILTER_CHAIN.strip():
        pipeline._master_audio(stage, out)
    else:
        pipeline._copy_wav(stage, out)
    return str(out)


def create_from_document(
    doc_path: str,
    reference_path: Optional[str] = None,
    language: Optional[str] = None,
    cb: ProgressCb = None,
) -> str:
    """Create a narrated infographic video from a document. Returns MP4 path."""
    def _emit(m):
        logger.info(m)
        if cb:
            cb(m)

    if not Path(doc_path).is_file():
        raise FileNotFoundError(f"Document not found: {doc_path}")
    reference = reference_path or str(config.DEFAULT_REFERENCE_SAMPLE)
    if not Path(reference).is_file():
        raise FileNotFoundError(f"Reference voice not found: {reference}")
    language = language or config.LANGUAGE

    run_id = pipeline.new_run_id()
    try:
        _emit("Reading document...")
        text = docread.read_document(doc_path)
        if not text.strip():
            raise ValueError("The document appears to be empty.")

        # AI brain: content spec + narration script.
        spec_dict, narration = spec_mod.build_spec(text, cb)
        # Free the LLM before loading the voice model — avoids out-of-memory
        # (which shows up as a Colab 'runtime disconnected').
        spec_mod.unload_llm()

        # Cap the narration length so TTS stays fast (long scripts = many slow
        # TTS batches). Keep the first ~max words at a sentence boundary.
        max_words = getattr(config, "MAX_NARRATION_WORDS", 180)
        words = narration.split()
        if len(words) > max_words:
            trimmed = " ".join(words[:max_words])
            cut = max(trimmed.rfind("."), trimmed.rfind("!"), trimmed.rfind("?"))
            narration = trimmed[:cut + 1] if cut > 40 else trimmed
            _emit(f"Narration trimmed to ~{max_words} words for speed.")

        # Render the infographic to an image.
        _emit("Rendering infographic...")
        html_path = config.TEMP_DIR / f"{run_id}_info.html"
        html_path.write_text(design.render_spec_to_html(spec_dict),
                             encoding="utf-8")
        png_path = config.TEMP_DIR / f"{run_id}_info.png"
        available, reason = render.is_available()
        if not available:
            raise RuntimeError(
                f"Cannot render infographic image: {reason} "
                f"(install with: pip install playwright && playwright install chromium)"
            )
        render.html_to_png(str(html_path), str(png_path))

        # Narrate.
        narration_wav = _narrate(narration, reference, language, run_id, cb)
        duration = pipeline._wav_duration(narration_wav)

        # Build the video (single infographic for now, Ken Burns motion).
        out_path = str(config.OUTPUT_DIR / f"{run_id}_created.mp4")
        videogen.build_video([(str(png_path), duration)], narration_wav,
                             out_path, cb)

        # Subtitles: transcribe the narration we just made for accurate timing.
        if config.GENERATE_SUBTITLES:
            try:
                segs, _ = pipeline.transcribe(narration_wav, language, cb)
                if segs:
                    paths = subtitles.write_subtitles(
                        segs, out_path, config.SUBTITLE_FORMAT)
                    _emit(f"Subtitles: {', '.join(Path(p).name for p in paths)}")
                    if config.BURN_SUBTITLES:
                        srt = next((p for p in paths if p.endswith(".srt")), None)
                        if srt:
                            _emit("Burning subtitles into the video...")
                            burned = str(Path(out_path).with_name(
                                Path(out_path).stem + "_sub.mp4"))
                            subtitles.burn_into_video(out_path, srt, burned)
                            import os
                            os.replace(burned, out_path)
                            _emit("Subtitles burned in.")
            except Exception as exc:  # noqa: BLE001
                _emit(f"Subtitles step issue ({exc}); continuing.")

        _emit(f"Done -> {out_path}")
        return out_path
    finally:
        pipeline.cleanup(run_id, cb)
