"""Voice Replacer — native desktop launcher.

Runs the existing Gradio app (app.py) as a local server in a background
thread, then displays it inside a native OS window via pywebview instead of a
browser tab. All UI and processing logic is reused unchanged from app.py.

HOW TO LAUNCH
-------------
    1. Install deps:  pip install -r requirements.txt
    2. Install ffmpeg system-wide and ensure it is on your PATH.
    3. Run:           python desktop.py

A native window opens; no browser or URL needed.
"""

from __future__ import annotations

import logging
import socket
import threading
import time

import webview  # pywebview

import app as gradio_app
import config

config.configure_logging()
logger = logging.getLogger("desktop")

HOST = "127.0.0.1"
PORT = 7860
WINDOW_TITLE = "Voice Replacer — Monika Edition"


def _port_is_open(host: str, port: int) -> bool:
    """Return True once something is listening on host:port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex((host, port)) == 0


def _start_server() -> None:
    """Launch the Gradio app headless (no auto-opened browser tab)."""
    demo = gradio_app.build_ui()
    # prevent_thread_lock keeps launch() non-blocking so the window can open;
    # inbrowser=False because we render inside the native window ourselves.
    demo.launch(
        server_name=HOST,
        server_port=PORT,
        inbrowser=False,
        prevent_thread_lock=True,
        show_error=True,
    )


def _wait_for_server(timeout: float = 120.0) -> None:
    """Block until the Gradio server is accepting connections."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if _port_is_open(HOST, PORT):
            return
        time.sleep(0.3)
    raise RuntimeError(
        f"Gradio server did not start on {HOST}:{PORT} within {timeout:.0f}s."
    )


def main() -> None:
    logger.info("Starting Gradio server in background thread...")
    threading.Thread(target=_start_server, daemon=True).start()
    _wait_for_server()
    logger.info("Server ready — opening native window.")

    webview.create_window(
        WINDOW_TITLE,
        f"http://{HOST}:{PORT}",
        width=1280,
        height=900,
        min_size=(900, 650),
    )
    # Blocks until the window is closed; the daemon server thread exits with it.
    webview.start()


if __name__ == "__main__":
    main()
