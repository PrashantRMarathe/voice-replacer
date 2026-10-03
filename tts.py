"""Pluggable text-to-speech (voice-cloning) backends.

Two engines are supported behind one interface so the rest of the pipeline
doesn't care which is used:

- **XTTS v2** (``xtts``): 17 languages, excellent cloning, but a NON-COMMERCIAL
  license. Default.
- **F5-TTS** (``f5``): MIT-licensed (commercially usable), but its base model is
  mainly English/Chinese.

Pick one with ``config.TTS_BACKEND``. If the chosen engine isn't installed, the
other is used automatically. Models are loaded lazily and cached.
"""

from __future__ import annotations

import logging
import re
from typing import Optional

import config

logger = logging.getLogger(__name__)

_backend = None  # cached Backend instance

_DIGIT_RE = re.compile(r"\d+(?:[.,]\d+)?")


def _audio_duration(path: str) -> float:
    """Return the duration of an audio file in seconds (0.0 if unknown)."""
    try:
        import ffmpeg

        info = ffmpeg.probe(path)
        return float(info["format"]["duration"])
    except Exception:  # noqa: BLE001
        return 0.0


def _expand_numbers(text: str, lang: str) -> str:
    """Spell out digit sequences as words.

    XTTS's own number-expansion (via ``num2words``) crashes with
    ``NotImplementedError`` for languages ``num2words`` doesn't support (e.g.
    Hindi). Expanding numbers ourselves first, falling back to English
    spelling when the target language isn't supported, avoids that crash.
    """
    from num2words import num2words

    def _replace(match: re.Match) -> str:
        raw = match.group(0)
        try:
            value = float(raw.replace(",", "")) if "." in raw or "," in raw else int(raw)
        except ValueError:
            return raw
        try:
            return num2words(value, lang=lang)
        except NotImplementedError:
            return num2words(value, lang="en")

    return _DIGIT_RE.sub(_replace, text)


# --------------------------------------------------------------------------- #
# Backend implementations
# --------------------------------------------------------------------------- #
class _XttsBackend:
    """Coqui XTTS v2 backend (multilingual, non-commercial license).

    Speed-optimized: the per-reference voice fingerprint (conditioning latents)
    is computed ONCE and cached, instead of XTTS re-encoding the whole reference
    clip on every segment. References are also trimmed to a short clip first.
    Falls back to the standard high-level API if the fast path isn't available.
    """

    name = "xtts"

    def __init__(self) -> None:
        self._model = None
        self._xtts = None            # underlying Xtts model (for the fast path)
        self._latents: dict = {}     # reference path -> (gpt_cond_latent, spk_emb)
        self._trimmed: dict = {}     # reference path -> trimmed reference path

    def _load(self):
        if self._model is None:
            from TTS.api import TTS

            logger.info("Loading XTTS model '%s' on %s ...",
                        config.XTTS_MODEL, config.DEVICE)
            self._model = TTS(config.XTTS_MODEL).to(config.DEVICE)
            # Reach the underlying Xtts model for the fast (cached-latent) path.
            self._xtts = getattr(
                getattr(self._model, "synthesizer", None), "tts_model", None)
        return self._model

    def _prepare_reference(self, speaker_wav: str) -> str:
        """Return a cleaned, ~ideal-length reference for best cloning (cached).

        XTTS clones best from ~15-30s of clean, well-leveled speech. A very long
        or quiet clip clones poorly. This takes a window of the reference and
        normalizes loudness + removes rumble, producing the strongest clone.
        """
        if speaker_wav in self._trimmed:
            return self._trimmed[speaker_wav]
        max_s = getattr(config, "XTTS_MAX_REF_SECONDS", 30) or 30
        try:
            import ffmpeg

            dur = _audio_duration(speaker_wav)
            # Skip a short intro on long clips, then take a `max_s` window.
            offset = 3.0 if dur > (max_s + 6) else 0.0
            inp = ffmpeg.input(speaker_wav, ss=offset, t=max_s)
            out = config.TEMP_DIR / f"xtts_ref_{abs(hash(speaker_wav)) & 0xffffff:06x}.wav"
            (
                inp.output(
                    str(out),
                    af="highpass=f=60,dynaudnorm=f=200:g=11",  # clean + even out level
                    acodec="pcm_s16le", ac=1, ar=config.SAMPLE_RATE,
                )
                .overwrite_output()
                .run(quiet=True)
            )
            self._trimmed[speaker_wav] = str(out)
        except Exception as exc:  # noqa: BLE001 - preparation is best-effort
            logger.warning("Reference prep failed (%s); using original clip.", exc)
            self._trimmed[speaker_wav] = speaker_wav
        return self._trimmed[speaker_wav]

    def _get_latents(self, speaker_wav: str):
        """Compute (and cache) the conditioning latents for a reference."""
        if speaker_wav not in self._latents:
            ref = self._prepare_reference(speaker_wav)
            self._latents[speaker_wav] = self._xtts.get_conditioning_latents(
                audio_path=[ref])
        return self._latents[speaker_wav]

    def _gen_kwargs(self) -> dict:
        return dict(
            temperature=config.XTTS_TEMPERATURE,
            repetition_penalty=config.XTTS_REPETITION_PENALTY,
            length_penalty=config.XTTS_LENGTH_PENALTY,
            top_k=config.XTTS_TOP_K,
            top_p=config.XTTS_TOP_P,
            speed=config.XTTS_SPEED,
            enable_text_splitting=config.XTTS_ENABLE_TEXT_SPLITTING,
        )

    def synth_to_file(
        self, text: str, speaker_wav: str, language: str, out_path: str
    ) -> None:
        self._load()
        spoken = _expand_numbers(text, language)

        # Fast path (opt-in): reuse a cached voice fingerprint from a trimmed
        # reference. Faster, but the shorter reference can weaken the voice
        # match, so it's OFF by default. Enable with config.XTTS_FAST_PATH.
        if getattr(config, "XTTS_FAST_PATH", False) and self._xtts is not None:
            try:
                gpt_cond_latent, speaker_embedding = self._get_latents(speaker_wav)
                out = self._xtts.inference(
                    spoken, language, gpt_cond_latent, speaker_embedding,
                    **self._gen_kwargs())
                self._write_wav(out["wav"], out_path)
                return
            except Exception as exc:  # noqa: BLE001 - fall back to the safe path
                logger.warning("XTTS fast path failed (%s); using standard API.",
                               exc)

        # Standard high-quality path: clone from the PREPARED reference (clean,
        # ideal-length, normalized) — this is what makes the output match best.
        self._model.tts_to_file(
            text=spoken, speaker_wav=self._prepare_reference(speaker_wav),
            language=language, file_path=out_path, **self._gen_kwargs())

    @staticmethod
    def _write_wav(wav, out_path: str) -> None:
        """Write XTTS float waveform to a 16-bit mono WAV at the native rate."""
        import numpy as np
        import soundfile as sf

        data = np.asarray(wav, dtype=np.float32)
        sf.write(out_path, data, config.SAMPLE_RATE, subtype="PCM_16")


class _F5Backend:  # pragma: no cover - requires the f5-tts model download
    """F5-TTS backend (MIT-licensed, commercially usable)."""

    name = "f5"

    def __init__(self) -> None:
        self._model = None

    def _load(self):
        if self._model is None:
            from f5_tts.api import F5TTS

            logger.info("Loading F5-TTS model '%s' on %s ...",
                        config.F5_MODEL, config.DEVICE)
            self._model = F5TTS(model=config.F5_MODEL, device=config.DEVICE)
        return self._model

    def synth_to_file(
        self, text: str, speaker_wav: str, language: str, out_path: str
    ) -> None:
        # F5-TTS infers the reference transcript itself when ref_text is "".
        # It is reference-driven rather than language-coded, so ``language`` is
        # not passed; coverage depends on the loaded model.
        self._load().infer(
            ref_file=speaker_wav,
            ref_text="",
            gen_text=text,
            file_wave=out_path,
        )


# --------------------------------------------------------------------------- #
# Selection with graceful fallback
# --------------------------------------------------------------------------- #
def _is_installed(backend: str) -> bool:
    import importlib.util

    pkg = {"xtts": "TTS", "f5": "f5_tts"}.get(backend)
    if not pkg:
        return False
    try:
        return importlib.util.find_spec(pkg) is not None
    except ModuleNotFoundError:
        return False


def _resolve_backend_name() -> str:
    """Return the usable TTS backend, honoring config with automatic fallback."""
    preferred = config.TTS_BACKEND
    if _is_installed(preferred):
        return preferred
    other = "f5" if preferred == "xtts" else "xtts"
    if _is_installed(other):
        logger.warning("TTS backend '%s' unavailable; using '%s'.",
                       preferred, other)
        return other
    raise RuntimeError(
        "No TTS backend available. Install 'coqui-tts' (xtts) or 'f5-tts' (f5)."
    )


def get_backend():
    """Return the cached TTS backend instance for the resolved engine."""
    global _backend
    name = _resolve_backend_name()
    if _backend is not None and _backend.name == name:
        return _backend
    _backend = _F5Backend() if name == "f5" else _XttsBackend()
    return _backend


def active_backend_name() -> str:
    """Return the name of the backend that would be used ('xtts' or 'f5')."""
    return _resolve_backend_name()
