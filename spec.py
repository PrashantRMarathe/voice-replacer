"""The AI 'brain' for Mode 2: turn document text into an infographic spec.

Given raw text about a topic, produce:
  - a content spec (dict) that design.py renders into an infographic, and
  - a narration script (str) that XTTS speaks.

Primary brain: a free, open-source LLM (e.g. Qwen2.5) run locally/on the Colab
GPU via `transformers` — so it "uses its brain" per topic, for free. If no LLM
is available, a deterministic heuristic fallback builds a reasonable spec from
the text's own structure, so the pipeline always works.
"""

from __future__ import annotations

import json
import logging
import re
from typing import Callable, Dict, Optional, Tuple

import config

logger = logging.getLogger(__name__)
ProgressCb = Optional[Callable[[str], None]]

_llm = None  # cached (tokenizer, model)

# Free, GPU-friendly instruction model. Override via config.LLM_MODEL.
DEFAULT_LLM_MODEL = "Qwen/Qwen2.5-3B-Instruct"

_PROMPT = """You are an instructional designer. From the SOURCE TEXT, create a \
"Single Point Lesson" infographic spec AND a narration script.

Return ONLY valid JSON with this exact shape:
{{
 "spec": {{
   "title": "short topic title",
   "subtitle": "(optional one-line subtitle)",
   "tagline": "one-sentence description",
   "what_is_it": "2-3 sentence definition",
   "why": ["benefit 1","benefit 2","benefit 3","benefit 4"],
   "categories": [{{"title":"1. Name","items":["point","point","point"]}}],
   "steps": ["step 1","step 2","step 3","step 4","step 5"],
   "takeaway": "one key takeaway sentence",
   "remember": "one short memorable rule"
 }},
 "narration": "a clear spoken script (~150-200 words) explaining the topic"
}}
Use 3-6 categories. Keep bullet points short. SOURCE TEXT:
---
{text}
---"""


def _emit(cb: ProgressCb, msg: str) -> None:
    logger.info(msg)
    if cb is not None:
        cb(msg)


def is_llm_available() -> Tuple[bool, str]:
    """Return ``(available, reason)`` for the LLM brain."""
    import importlib.util

    try:
        if importlib.util.find_spec("transformers") is None:
            return False, "transformers not installed."
    except ModuleNotFoundError:
        return False, "transformers not installed."
    return True, "ok"


def _load_llm():
    global _llm
    if _llm is None:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer

        name = getattr(config, "LLM_MODEL", DEFAULT_LLM_MODEL)
        logger.info("Loading LLM '%s' on %s ...", name, config.DEVICE)
        tok = AutoTokenizer.from_pretrained(name)
        model = AutoModelForCausalLM.from_pretrained(
            name,
            torch_dtype=torch.float16 if config.DEVICE == "cuda" else torch.float32,
            device_map=config.DEVICE if config.DEVICE == "cuda" else None,
        )
        _llm = (tok, model)
    return _llm


def _generate_llm(text: str) -> dict:
    """Run the LLM and parse its JSON output."""
    tok, model = _load_llm()
    prompt = _PROMPT.format(text=text[:6000])
    messages = [{"role": "user", "content": prompt}]
    inputs = tok.apply_chat_template(messages, add_generation_prompt=True,
                                     return_tensors="pt").to(model.device)
    out = model.generate(inputs, max_new_tokens=1200, temperature=0.7,
                         do_sample=True, top_p=0.9)
    reply = tok.decode(out[0][inputs.shape[1]:], skip_special_tokens=True)
    return _extract_json(reply)


def _extract_json(reply: str) -> dict:
    """Pull the first JSON object out of an LLM reply."""
    m = re.search(r"\{.*\}", reply, re.DOTALL)
    if not m:
        raise ValueError("LLM did not return JSON.")
    return json.loads(m.group(0))


def build_spec(
    text: str, cb: ProgressCb = None
) -> Tuple[Dict, str]:
    """Return ``(spec, narration)`` for ``text``.

    Uses the LLM brain if available; otherwise a heuristic fallback. Never
    raises for content reasons — always returns a usable spec + narration.
    """
    available, reason = is_llm_available()
    if available:
        try:
            _emit(cb, "AI is designing the infographic + script...")
            data = _generate_llm(text)
            spec = data.get("spec") or {}
            narration = (data.get("narration") or "").strip()
            if spec.get("title") and narration:
                return spec, narration
            _emit(cb, "LLM output incomplete; using heuristic fallback.")
        except Exception as exc:  # noqa: BLE001 - fall back gracefully
            _emit(cb, f"LLM brain failed ({exc}); using heuristic fallback.")
    else:
        _emit(cb, f"LLM brain unavailable ({reason}); using heuristic fallback.")

    return _heuristic_spec(text)


def _heuristic_spec(text: str) -> Tuple[Dict, str]:
    """Deterministic fallback: build a spec from the text's own structure."""
    lines = [ln.strip(" -•\t") for ln in text.splitlines() if ln.strip()]
    title = lines[0][:60] if lines else "Topic"
    body = lines[1:] if len(lines) > 1 else lines
    what = " ".join(body[:2])[:300] if body else title
    bullets = [b[:70] for b in body if len(b) > 3][:12]
    # Chunk bullets into up to 4 categories of 3.
    categories = []
    for i in range(0, min(len(bullets), 12), 3):
        chunk = bullets[i:i + 3]
        if chunk:
            categories.append({"title": f"{len(categories)+1}. Key Points",
                               "items": chunk})
    narration = (what + " " + " ".join(bullets[:6])).strip() or title
    spec = {
        "title": title,
        "tagline": "",
        "what_is_it": what,
        "why": bullets[:4] or [title],
        "categories": categories or [{"title": "1. Overview", "items": [title]}],
        "steps": bullets[:5],
        "takeaway": body[-1][:160] if body else title,
        "remember": "",
    }
    return spec, narration
