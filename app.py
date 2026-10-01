"""Voice Replacer (Gradio UI + main flow).

HOW TO LAUNCH
-------------
    1. Install deps:      pip install -r requirements.txt
    2. Install ffmpeg system-wide and ensure it is on your PATH.
    3. Put a reference voice sample at samples/monika.mp3 (2-3 min clean audio).
    4. Run:               python app.py
    5. Open the printed URL (default http://localhost:7860) in a browser.

The UI walks you through: upload video -> Transcribe -> edit transcript ->
Generate Video -> preview & download the final MP4.

All heavy processing lives in pipeline.py; this file only wires the UI.
"""

from __future__ import annotations

import logging
import time
import traceback
from pathlib import Path
from typing import List, Optional, Tuple

import gradio as gr

import config
import diarize
import lipsync
import pipeline
import translate
from pipeline import Segment

config.configure_logging()
logger = logging.getLogger("app")


# --------------------------------------------------------------------------- #
# Transcript <-> text helpers
# --------------------------------------------------------------------------- #
def _segments_to_text(segments: List[Segment]) -> str:
    """Render segments as an editable, timestamp-annotated transcript.

    Each line is:  [start -> end] text
    The timestamps let the user see timing but only the text is used for
    synthesis (timing comes from the stored segment objects).
    """
    def _prefix(s: Segment) -> str:
        spk = f"{s.speaker} | " if s.speaker else ""
        return f"[{spk}{s.start:.2f} -> {s.end:.2f}]"

    return "\n".join(f"{_prefix(s)} {s.text}" for s in segments)


def _text_to_segments(text: str, original: List[Segment]) -> List[Segment]:
    """Merge user-edited text back onto the original segment timings.

    We keep the original start/end times (line order must be preserved) and
    only replace the spoken text, stripping the ``[start -> end]`` prefix if
    the user left it in place.
    """
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if len(lines) != len(original):
        raise ValueError(
            f"Edited transcript has {len(lines)} line(s) but the original had "
            f"{len(original)}. Keep one line per segment (do not add/remove "
            f"lines); only edit the words."
        )
    new_segments: List[Segment] = []
    for line, seg in zip(lines, original):
        cleaned = line
        if cleaned.startswith("[") and "]" in cleaned:
            cleaned = cleaned.split("]", 1)[1]
        cleaned = cleaned.strip()
        new_segments.append(Segment(start=seg.start, end=seg.end, text=cleaned,
                                    speaker=seg.speaker))
    return new_segments


# --------------------------------------------------------------------------- #
# UI callbacks
# --------------------------------------------------------------------------- #
def on_transcribe(
    video_file: Optional[str],
    source_lang: str,
    use_diarization: bool,
    status: str,
) -> Tuple[str, str, List[dict], str, str]:
    """Handle the Transcribe button: extract audio, run Whisper, (diarize).

    Returns updated (transcript_text, status_log, stored_segments_state,
    detected_language_state, audio_path_state).
    """
    log_lines: List[str] = status.splitlines() if status else []

    def cb(msg: str) -> None:
        log_lines.append(f"  {msg}")

    if not video_file:
        log_lines.append("[!] Please upload a video first.")
        return "", "\n".join(log_lines), [], "", ""

    run_id = pipeline.new_run_id()
    try:
        t0 = time.time()
        log_lines.append(f"=== Transcribe (run {run_id}) on {config.DEVICE} ===")
        audio_path = pipeline.extract_audio(video_file, run_id, cb)
        segments, detected = pipeline.transcribe(audio_path, source_lang, cb)
        if not segments:
            log_lines.append("[!] No speech detected in the video.")
            return "", "\n".join(log_lines), [], "", ""

        # Optional speaker diarization: label each segment with its speaker.
        if use_diarization:
            available, reason = diarize.is_available()
            if not available:
                log_lines.append(f"  [diarization] Skipped: {reason}")
            else:
                try:
                    segments, speakers = diarize.assign_speakers(
                        segments, audio_path, cb)
                    log_lines.append(f"  [diarization] {len(speakers)} "
                                     f"speaker(s): {', '.join(speakers)}")
                except RuntimeError as exc:
                    log_lines.append(f"  [diarization] {exc}")

        elapsed = time.time() - t0
        log_lines.append(f"[ok] Transcribed in {elapsed:.1f}s. "
                         f"Edit the text below, then Generate Video.")
        transcript = _segments_to_text(segments)
        state = [s.__dict__ for s in segments]
        return transcript, "\n".join(log_lines), state, detected or "", audio_path
    except Exception as exc:  # noqa: BLE001 - surface any failure to the UI
        logger.error("Transcription failed", exc_info=True)
        log_lines.append(f"[ERROR] Transcription failed: {exc}")
        log_lines.append(traceback.format_exc())
        return "", "\n".join(log_lines), [], "", ""


def on_generate(
    video_file: Optional[str],
    reference_file: Optional[str],
    transcript_text: str,
    stored_segments: List[dict],
    source_lang: str,
    target_lang: str,
    detected_lang: str,
    use_lipsync: bool,
    audio_path: str,
    status: str,
) -> Tuple[Optional[str], Optional[str], str]:
    """Handle the Generate Video button: (translate) + synth voice + merge.

    Returns updated (video_preview_path, download_path, status_log).
    """
    log_lines: List[str] = status.splitlines() if status else []

    def cb(msg: str) -> None:
        log_lines.append(f"  {msg}")

    if not video_file:
        log_lines.append("[!] Please upload a video first.")
        return None, None, "\n".join(log_lines)
    if not stored_segments:
        log_lines.append("[!] Please run Transcribe before generating.")
        return None, None, "\n".join(log_lines)

    reference = reference_file or str(config.DEFAULT_REFERENCE_SAMPLE)
    if not _reference_exists(reference):
        log_lines.append(
            f"[!] Reference voice sample not found: {reference}. "
            f"Upload one or place it at {config.DEFAULT_REFERENCE_SAMPLE}."
        )
        return None, None, "\n".join(log_lines)

    # Resolve the effective source language: the explicit choice, or whatever
    # Whisper detected when the user left it on Auto-detect.
    effective_source = (
        detected_lang if source_lang == config.AUTO_DETECT else source_lang
    )

    run_id = pipeline.new_run_id()
    try:
        t0 = time.time()
        log_lines.append(f"=== Generate (run {run_id}) on {config.DEVICE} ===")
        original = [Segment(**d) for d in stored_segments]
        segments = _text_to_segments(transcript_text, original)

        # --- Decide whether this is a dub (translate) or same-language run. ---
        want_translation = bool(target_lang) and (
            config.base_lang(target_lang) != config.base_lang(
                effective_source or config.LANGUAGE)
        )
        if want_translation:
            segments = translate.translate_segments(
                segments, effective_source or config.AUTO_DETECT,
                target_lang, cb)
            synth_lang = target_lang
        else:
            synth_lang = effective_source or config.LANGUAGE

        # XTTS needs one of its 17 supported codes; map/validate before synth.
        xtts_lang = config.to_xtts_code(synth_lang)
        if xtts_lang is None:
            log_lines.append(
                f"[!] XTTS v2 cannot speak language '{synth_lang}'. "
                f"Choose a target language from the supported list."
            )
            return None, None, "\n".join(log_lines)
        log_lines.append(f"  Synthesizing in: {config.LANGUAGES[xtts_lang]}")

        # If segments were diarized, build a per-speaker cloning reference from
        # each speaker's own voice in the source audio.
        speaker_refs = None
        has_speakers = any(getattr(s, "speaker", None) for s in segments)
        if has_speakers and audio_path and Path(audio_path).is_file():
            try:
                speaker_refs = diarize.extract_speaker_references(
                    audio_path, segments, run_id, cb)
            except RuntimeError as exc:
                log_lines.append(f"  [diarization] Reference build failed: {exc}")
                log_lines.append("  [diarization] Using the default voice for all.")

        generated = pipeline.generate_voice(segments, reference, run_id,
                                            xtts_lang, cb, speaker_refs)

        # Lip-sync if requested and set up; otherwise (or on failure) fall back
        # to plain audio replacement so the run always produces a video.
        final_path = None
        if use_lipsync:
            available, reason = lipsync.is_available()
            if not available:
                log_lines.append(f"  [lip-sync] Skipped: {reason}")
            else:
                try:
                    final_path = lipsync.apply_lipsync(video_file, generated,
                                                       run_id, cb)
                except RuntimeError as exc:
                    log_lines.append(f"  [lip-sync] {exc}")
                    log_lines.append("  [lip-sync] Falling back to audio-only merge.")
        if final_path is None:
            final_path = pipeline.merge_audio_video(video_file, generated,
                                                    run_id, cb)
        pipeline.cleanup(run_id, cb)

        elapsed = time.time() - t0
        log_lines.append(f"[ok] Done in {elapsed:.1f}s -> {final_path}")
        return final_path, final_path, "\n".join(log_lines)
    except Exception as exc:  # noqa: BLE001
        logger.error("Generation failed", exc_info=True)
        log_lines.append(f"[ERROR] Generation failed: {exc}")
        log_lines.append(traceback.format_exc())
        # Best-effort cleanup even on failure.
        try:
            pipeline.cleanup(run_id, cb)
        except Exception:  # noqa: BLE001
            pass
        return None, None, "\n".join(log_lines)


def _reference_exists(path: str) -> bool:
    """Return True if the reference sample file exists on disk."""
    return Path(path).is_file()


# --------------------------------------------------------------------------- #
# UI definition
# --------------------------------------------------------------------------- #
def build_ui() -> gr.Blocks:
    """Construct and return the Gradio Blocks app."""
    device_note = (
        f"Device: **{config.DEVICE.upper()}**"
        + ("" if config.DEVICE == "cuda"
           else "  (no CUDA GPU detected — expect slower CPU processing)")
    )

    import tts as _tts
    backend_name = _tts.active_backend_name()
    tts_note = {
        "xtts": "TTS engine: **XTTS v2** (17 languages · non-commercial license)",
        "f5": "TTS engine: **F5-TTS** (MIT / commercial-OK · mainly EN/ZH)",
    }.get(backend_name, f"TTS engine: **{backend_name}**")

    with gr.Blocks(title="Voice Replacer") as demo:
        gr.Markdown("# Voice Replacer")
        gr.Markdown(device_note)
        gr.Markdown(tts_note)

        segments_state = gr.State([])
        detected_lang_state = gr.State("")
        audio_path_state = gr.State("")

        # Dropdown choices as (label, value) pairs.
        source_choices = [("Auto-detect", config.AUTO_DETECT)] + [
            (name, code) for code, name in config.LANGUAGES.items()
        ]
        target_choices = [("Keep original (no translation)", "")] + [
            (name, code) for code, name in config.LANGUAGES.items()
        ]

        with gr.Row():
            with gr.Column():
                video_in = gr.Video(label="Input video (MP4)")
                reference_in = gr.Audio(
                    label="Reference voice sample (MP3/WAV)",
                    type="filepath",
                    value=str(config.DEFAULT_REFERENCE_SAMPLE)
                    if config.DEFAULT_REFERENCE_SAMPLE.is_file() else None,
                )
                with gr.Row():
                    source_lang_in = gr.Dropdown(
                        choices=source_choices,
                        value=config.AUTO_DETECT,
                        label="Spoken language (source)",
                    )
                    target_lang_in = gr.Dropdown(
                        choices=target_choices,
                        value="",
                        label="Dub into (target) — translate + clone voice",
                    )
                # Diarization and lip-sync are opt-in features that require
                # separate model setup (see README). Their UI checkboxes are
                # hidden until set up; these State holders keep the flags False
                # so the generate flow (and its wiring) stays unchanged.
                diarization_in = gr.State(False)
                lipsync_in = gr.State(False)
                transcribe_btn = gr.Button("Transcribe", variant="secondary")
                generate_btn = gr.Button("Generate Video", variant="primary")
            with gr.Column():
                transcript_box = gr.Textbox(
                    label="Transcript (edit before generating)",
                    lines=12,
                    placeholder="Transcript will appear here after you click "
                                "Transcribe. Edit the words to fix any errors, "
                                "but keep one line per segment.",
                )
                video_out = gr.Video(label="Final output")
                download_out = gr.File(label="Download final MP4")

        status_box = gr.Textbox(
            label="Status log",
            lines=12,
            value="",
            interactive=False,
        )

        transcribe_btn.click(
            fn=on_transcribe,
            inputs=[video_in, source_lang_in, diarization_in, status_box],
            outputs=[transcript_box, status_box, segments_state,
                     detected_lang_state, audio_path_state],
        )
        generate_btn.click(
            fn=on_generate,
            inputs=[video_in, reference_in, transcript_box, segments_state,
                    source_lang_in, target_lang_in, detected_lang_state,
                    lipsync_in, audio_path_state, status_box],
            outputs=[video_out, download_out, status_box],
        )

    return demo


def main() -> None:
    """Launch the Gradio app.

    Binds to 127.0.0.1 by default (local only). Set GRADIO_SERVER_NAME=0.0.0.0
    to expose it on all interfaces, e.g. when running inside a container.
    """
    import os

    host = os.environ.get("GRADIO_SERVER_NAME", "127.0.0.1")
    port = int(os.environ.get("GRADIO_SERVER_PORT", "7860"))
    # Don't try to open a browser when bound to all interfaces (e.g. in Docker).
    open_browser = host == "127.0.0.1"
    demo = build_ui()
    demo.launch(server_name=host, server_port=port,
                inbrowser=open_browser, pwa=True)


if __name__ == "__main__":
    main()
