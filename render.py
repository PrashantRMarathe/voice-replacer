"""Render an infographic HTML file to a PNG image.

Uses Playwright (headless Chromium) so the output is pixel-accurate to a real
browser — crisp text, proper fonts, exact layout. Works locally and on Colab.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional


def is_available() -> tuple[bool, str]:
    """Return ``(available, reason)`` for HTML->image rendering."""
    import importlib.util

    try:
        if importlib.util.find_spec("playwright") is None:
            return False, "Playwright not installed (pip install playwright; playwright install chromium)."
    except ModuleNotFoundError:
        return False, "Playwright not installed."
    return True, "ok"


def html_to_png(
    html_path: str,
    png_path: str,
    width: int = 1320,
    scale: float = 2.0,
    full_page: bool = True,
) -> str:
    """Render ``html_path`` to ``png_path`` and return the PNG path.

    Args:
        html_path: Local HTML file to render.
        png_path: Output PNG path.
        width: Viewport width in CSS px (infographics are designed at 1320).
        scale: Device scale factor (2.0 = crisp, retina-quality output).
        full_page: Capture the whole page height, not just the viewport.
    """
    available, reason = is_available()
    if not available:
        raise RuntimeError(f"HTML rendering unavailable: {reason}")

    from playwright.sync_api import sync_playwright

    url = Path(html_path).resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": width, "height": 900},
                                device_scale_factor=scale)
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(200)  # let fonts settle
        # Screenshot the .page element if present, else the full page.
        el = page.query_selector(".page")
        if el is not None:
            el.screenshot(path=png_path)
        else:
            page.screenshot(path=png_path, full_page=full_page)
        browser.close()
    return png_path
