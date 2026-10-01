"""Professional infographic rendering (content spec -> polished HTML).

This is the design engine for Mode 2. The AI organizes any topic into a simple
``spec`` dict; this module renders it as a clean, branded "Single Point Lesson"
style infographic (crisp text, colored category cards, steps, takeaway). Keeping
the design here (not in the AI) guarantees consistent professional quality for
every topic, while the AI supplies the per-topic content.

A spec looks like::

    {
      "title": "5S Workplace Organization",
      "subtitle": "(Sort, Set in Order, Shine, Standardize, Sustain)",
      "tagline": "A Lean method for a clean, safe, efficient workplace",
      "what_is_it": "5S is a workplace organization method ...",
      "why": ["Reduces wasted time", "Improves safety", ...],
      "categories": [
         {"title": "1. Sort", "items": ["Remove unneeded", "Red-tag", ...]},
         ... up to 6 ...
      ],
      "steps": ["Sort the area", "Set in order", ...],
      "takeaway": "5S is a daily discipline ...",
      "remember": "A place for everything ...",
      "ref": "LA-012",            # optional
      "brand": "FACTORY FLOW IQ"  # optional
    }
"""

from __future__ import annotations

import html
from typing import Dict, List

_CAT_COLORS = ["#1769c4", "#1a9e5a", "#e8721b", "#6a3fa0", "#118a8a", "#d6286e"]


def _esc(s) -> str:
    return html.escape(str(s if s is not None else ""))


def _li(items: List[str]) -> str:
    return "".join(f"<li>{_esc(x)}</li>" for x in (items or []))


def _checks(items: List[str]) -> str:
    return "".join(f'<li>{_esc(x)}</li>' for x in (items or []))


def _category_cards(categories: List[Dict]) -> str:
    cards = []
    for i, cat in enumerate((categories or [])[:6]):
        color = _CAT_COLORS[i % len(_CAT_COLORS)]
        cards.append(
            f'<div class="cat"><div class="chead" style="background:{color}">'
            f'{_esc(cat.get("title", f"Category {i+1}"))}</div>'
            f'<ul>{_li(cat.get("items", []))}</ul></div>'
        )
    return "".join(cards)


def _steps(steps: List[str]) -> str:
    out = []
    for i, s in enumerate(steps or [], start=1):
        out.append(f'<li><span class="n">{i}</span>{_esc(s)}</li>')
    return "".join(out)


def render_spec_to_html(spec: Dict) -> str:
    """Render a content ``spec`` dict into a complete infographic HTML string."""
    title = _esc(spec.get("title", "Untitled Topic"))
    subtitle = _esc(spec.get("subtitle", ""))
    tagline = _esc(spec.get("tagline", ""))
    what = _esc(spec.get("what_is_it", ""))
    ref = _esc(spec.get("ref", ""))
    brand = _esc(spec.get("brand", "FACTORY FLOW IQ"))
    why_html = _checks(spec.get("why", []))
    cats_html = _category_cards(spec.get("categories", []))
    steps_html = _steps(spec.get("steps", []))
    takeaway = _esc(spec.get("takeaway", ""))
    remember = _esc(spec.get("remember", ""))

    subtitle_block = f"<h2>{subtitle}</h2>" if subtitle else ""
    tagline_block = f'<div class="ribbon">{tagline}</div>' if tagline else ""
    steps_block = (
        f'<div><div class="h">🧭 HOW TO USE?</div><ul class="steps">{steps_html}</ul></div>'
        if steps_html else ""
    )
    remember_block = (
        f'<div class="remember"><div class="rh">✅ REMEMBER</div><p>{remember}</p></div>'
        if remember else ""
    )

    return _TEMPLATE.format(
        title=title, subtitle_block=subtitle_block, tagline_block=tagline_block,
        what=what, why_html=why_html, cats_html=cats_html,
        steps_block=steps_block, takeaway=takeaway, remember_block=remember_block,
        ref=ref, brand=brand,
    )


_TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=1320, initial-scale=1"><title>{title}</title>
<style>
 :root{{--navy:#0f2b5b;--blue:#1769c4;--green:#1a9e5a;--ink:#13213b;--muted:#4a5a73;--line:#d9e1ee}}
 *{{box-sizing:border-box;margin:0;padding:0;font-family:"Segoe UI",Arial,sans-serif}}
 body{{background:#fff;color:var(--ink)}}
 .page{{width:1320px;background:#fff;border:3px solid var(--navy)}}
 .top{{display:grid;grid-template-columns:1.5fr 2fr 0.9fr;border-bottom:3px solid var(--navy)}}
 .top>div{{padding:10px 16px;border-right:2px solid var(--navy)}} .top>div:last-child{{border-right:none}}
 .spl-tag{{background:var(--navy);color:#fff;font-weight:800;font-size:19px;padding:6px 12px;border-radius:4px}}
 .ref{{font-weight:700;font-size:16px;margin-top:6px}} .rev{{font-weight:800;font-size:16px;text-align:center}}
 .logo{{font-weight:900;color:var(--blue);font-size:20px;text-align:center}}
 .logo small{{display:block;font-size:10px;color:var(--green);letter-spacing:2px}}
 .titleband{{text-align:center;padding:16px 10px 10px}}
 .titleband h1{{color:var(--navy);font-size:46px;font-weight:900;line-height:1.02}}
 .titleband h2{{color:var(--blue);font-size:23px;font-weight:800;margin-top:6px}}
 .ribbon{{display:inline-block;margin-top:12px;background:var(--navy);color:#fff;font-weight:700;font-size:16px;padding:8px 22px;border-radius:20px}}
 .intro{{display:grid;grid-template-columns:1fr 1fr;border-top:3px solid var(--navy);border-bottom:3px solid var(--navy);margin-top:12px}}
 .intro>div{{padding:14px 22px}} .intro>div:first-child{{border-right:2px solid var(--line)}}
 .h{{display:flex;align-items:center;gap:9px;font-size:21px;font-weight:900;color:var(--navy);margin-bottom:8px}}
 .intro p{{font-size:16px;color:var(--muted);line-height:1.5}}
 .checks li{{list-style:none;font-size:15px;margin:5px 0;padding-left:26px;position:relative;line-height:1.35}}
 .checks li:before{{content:"\\2714";position:absolute;left:0;color:var(--green);font-weight:900}}
 .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:16px 22px}}
 .cat{{border:1px solid var(--line);border-radius:10px;overflow:hidden;box-shadow:0 2px 6px rgba(20,40,80,.06)}}
 .cat .chead{{color:#fff;font-weight:800;font-size:17px;padding:9px 14px}}
 .cat ul{{padding:10px 14px 12px 30px}} .cat li{{font-size:14.5px;margin:4px 0;line-height:1.3}}
 .foot{{display:grid;grid-template-columns:1.1fr 1fr;border-top:3px solid var(--navy)}}
 .foot>div{{padding:14px 22px}} .foot>div:first-child{{border-right:2px solid var(--line)}}
 .steps li{{margin:7px 0;font-size:15px;list-style:none;padding-left:34px;position:relative;line-height:1.35}}
 .steps li .n{{position:absolute;left:0;top:0;background:var(--blue);color:#fff;font-weight:800;width:23px;height:23px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px}}
 .take{{background:#eaf4ff;border:1px solid #bcdcff;border-radius:10px;padding:14px 16px}}
 .take .h{{font-size:19px}} .take p{{font-size:15px;color:var(--muted);line-height:1.45}}
 .remember{{margin-top:12px;background:#e9f8ef;border:1px solid #b7e6c9;border-radius:10px;padding:12px 16px}}
 .remember .rh{{color:var(--green);font-weight:900;font-size:17px;margin-bottom:4px}}
 .remember p{{font-size:15px;font-weight:600}}
</style></head>
<body><div class="page">
 <div class="top">
  <div><span class="spl-tag">Single Point Lesson</span><div class="ref">{ref}</div></div>
  <div><div class="ref" style="font-size:18px;color:var(--navy)">{title}</div></div>
  <div><div class="rev">REV. - A</div><div class="logo" style="margin-top:4px">FFIQ<small>{brand}</small></div></div>
 </div>
 <div class="titleband"><h1>{title}</h1>{subtitle_block}{tagline_block}</div>
 <div class="intro">
  <div><div class="h">🎯 WHAT IS IT?</div><p>{what}</p></div>
  <div><div class="h">💡 WHY USE IT?</div><ul class="checks">{why_html}</ul></div>
 </div>
 <div class="grid">{cats_html}</div>
 <div class="foot">
  {steps_block}
  <div><div class="h">🏅 KEY TAKEAWAY</div><div class="take"><p>{takeaway}</p></div>{remember_block}</div>
 </div>
</div></body></html>"""
