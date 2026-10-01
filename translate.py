"""Text translation for the dubbing flow.

Translates transcript segments from a source language into a target language
while preserving the one-line-per-segment structure, so the downstream timing
fit can stretch each translated line into its original time slot.

Backend
-------
Online by default: tries ``deep-translator``'s Google backend first, then
automatically falls back to MyMemory if Google rate-limits or fails. Both are
free and need no API key, but require an internet connection. For a fully
offline alternative, install ``argostranslate`` and set
``TRANSLATE_BACKEND = "argos"``; the public API here stays the same.
"""

from __future__ import annotations

import logging
import time
from typing import Callable, List, Optional

import config
from pipeline import Segment

logger = logging.getLogger(__name__)

ProgressCb = Optional[Callable[[str], None]]

# Which backend(s) to use: "online" (Google then MyMemory fallback, default)
# or "argos" (offline).
TRANSLATE_BACKEND: str = "online"

# The free Google endpoint allows ~5 requests/second. Pace requests under that
# and retry with exponential backoff when it rate-limits us anyway.
_MIN_INTERVAL_S = 0.25   # ~4 req/s, safely under the limit
_MAX_RETRIES = 4
_BACKOFF_BASE_S = 2.0

# MyMemory needs region-qualified codes; map our XTTS base codes to them.
_MYMEMORY_CODES: dict[str, str] = {
    "en": "en-GB", "es": "es-ES", "fr": "fr-FR", "de": "de-DE",
    "it": "it-IT", "pt": "pt-PT", "pl": "pl-PL", "tr": "tr-TR",
    "ru": "ru-RU", "nl": "nl-NL", "cs": "cs-CZ", "ar": "ar-SA",
    "zh": "zh-CN", "ja": "ja-JP", "hu": "hu-HU", "ko": "ko-KR",
    "hi": "hi-IN",
}


def _emit(cb: ProgressCb, message: str) -> None:
    logger.info(message)
    if cb is not None:
        cb(message)


def translate_segments(
    segments: List[Segment],
    source_lang: str,
    target_lang: str,
    cb: ProgressCb = None,
) -> List[Segment]:
    """Return copies of ``segments`` with ``text`` translated to ``target_lang``.

    Args:
        segments: Transcript segments (timings are preserved untouched).
        source_lang: XTTS/Whisper source code, or ``config.AUTO_DETECT``.
        target_lang: XTTS target language code.
        cb: Optional progress callback.

    Returns:
        New list of :class:`Segment` with translated text and identical timings.
    """
    if not segments:
        return []

    src = (
        "auto"
        if source_lang == config.AUTO_DETECT
        else config.base_lang(source_lang)
    )
    tgt = config.base_lang(target_lang)

    _emit(cb, f"Translating {len(segments)} segment(s) {src} -> {tgt} ...")
    texts = [s.text for s in segments]

    if TRANSLATE_BACKEND == "argos":
        translated = _translate_argos(texts, src, tgt)
    else:
        translated = _translate_online(texts, src, tgt, cb)

    out: List[Segment] = []
    for seg, new_text in zip(segments, translated):
        out.append(Segment(start=seg.start, end=seg.end,
                           text=new_text.strip() or seg.text))
    _emit(cb, "Translation complete.")
    return out


def _translate_online(
    texts: List[str], src: str, tgt: str, cb: ProgressCb = None
) -> List[str]:
    """Try Google first, then fall back to MyMemory on any failure."""
    try:
        return _translate_google(texts, src, tgt, cb)
    except RuntimeError as exc:
        _emit(cb, f"Google backend unavailable ({exc}). "
                  f"Falling back to MyMemory...")
        return _translate_mymemory(texts, src, tgt, cb)


def _translate_mymemory(
    texts: List[str], src: str, tgt: str, cb: ProgressCb = None
) -> List[str]:
    """Translate ``texts`` with deep-translator's free MyMemory backend."""
    try:
        from deep_translator import MyMemoryTranslator
        from deep_translator.exceptions import TooManyRequests
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "Translation requires 'deep-translator'. "
            "Install it with: pip install deep-translator"
        ) from exc

    if src == "auto" or src not in _MYMEMORY_CODES:
        raise RuntimeError(
            "MyMemory fallback needs an explicit, supported source language "
            f"(got '{src}'). Select the spoken language instead of Auto-detect."
        )
    if tgt not in _MYMEMORY_CODES:
        raise RuntimeError(f"MyMemory does not support target language '{tgt}'.")

    translator = MyMemoryTranslator(
        source=_MYMEMORY_CODES[src], target=_MYMEMORY_CODES[tgt]
    )
    out: List[str] = []
    for idx, text in enumerate(texts):
        if not text.strip():
            out.append(text)
            continue
        out.append(_translate_one(translator, text, TooManyRequests, cb))
        if idx + 1 < len(texts):
            time.sleep(_MIN_INTERVAL_S)
    return out


def _translate_google(
    texts: List[str], src: str, tgt: str, cb: ProgressCb = None
) -> List[str]:
    """Translate ``texts`` with deep-translator's Google backend.

    Translates one line at a time (preserving order) with request pacing and
    exponential-backoff retry, because the free Google endpoint rate-limits
    bursts and ``translate_batch`` fires with no delay between calls.
    """
    try:
        from deep_translator import GoogleTranslator
        from deep_translator.exceptions import TooManyRequests
    except ImportError as exc:  # pragma: no cover - depends on install
        raise RuntimeError(
            "Translation requires the 'deep-translator' package. "
            "Install it with: pip install deep-translator"
        ) from exc

    translator = GoogleTranslator(source=src, target=tgt)
    out: List[str] = []
    for idx, text in enumerate(texts):
        if not text.strip():
            out.append(text)
            continue
        out.append(_translate_one(translator, text, TooManyRequests, cb))
        if idx + 1 < len(texts):
            time.sleep(_MIN_INTERVAL_S)
    return out


def _translate_one(translator, text: str, rate_limit_exc, cb: ProgressCb):
    """Translate a single line, retrying with backoff on rate-limit errors."""
    for attempt in range(_MAX_RETRIES):
        try:
            return translator.translate(text)
        except rate_limit_exc:
            wait = _BACKOFF_BASE_S * (2 ** attempt)
            _emit(cb, f"Rate-limited by translator; retrying in {wait:.0f}s "
                      f"(attempt {attempt + 1}/{_MAX_RETRIES})...")
            time.sleep(wait)
        except Exception as exc:  # noqa: BLE001 - surface a clear error upward
            raise RuntimeError(f"Translation failed: {exc}") from exc
    raise RuntimeError(
        "Translation failed: the free translator kept rate-limiting requests. "
        "Wait a minute and try again, or switch to the offline 'argos' backend."
    )


def _translate_argos(texts: List[str], src: str, tgt: str) -> List[str]:  # pragma: no cover
    """Offline translation via argostranslate (optional backend).

    Requires ``pip install argostranslate`` and the relevant language package
    to be installed once. ``src`` must be a concrete code (not "auto").
    """
    try:
        import argostranslate.translate as at
    except ImportError as exc:
        raise RuntimeError(
            "Offline translation requires 'argostranslate'. "
            "Install it with: pip install argostranslate"
        ) from exc

    if src == "auto":
        raise RuntimeError(
            "The offline (argos) backend cannot auto-detect the source "
            "language. Select the source language explicitly."
        )
    return [at.translate(t, src, tgt) for t in texts]
