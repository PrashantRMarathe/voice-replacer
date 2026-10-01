"""Read source documents (.txt / .md / .docx / .pdf) into plain text.

Used by the "Create from Document" mode (Mode 2) to turn an uploaded writing
into text the AI can organize into an infographic + narration. Optional
dependencies (python-docx, pypdf) are imported lazily and guarded, so plain
text always works even without them.
"""

from __future__ import annotations

from pathlib import Path


def read_document(path: str) -> str:
    """Return the plain text of ``path`` based on its extension.

    Supports .txt/.md (always), .docx (needs python-docx), .pdf (needs pypdf).
    Raises a clear error if an optional dependency is missing.
    """
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Document not found: {path}")

    ext = p.suffix.lower()
    if ext in (".txt", ".md", ""):
        return p.read_text(encoding="utf-8", errors="ignore").strip()
    if ext == ".docx":
        return _read_docx(p)
    if ext == ".pdf":
        return _read_pdf(p)
    # Unknown extension: best-effort as text.
    return p.read_text(encoding="utf-8", errors="ignore").strip()


def _read_docx(path: Path) -> str:
    try:
        import docx  # python-docx
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "Reading .docx needs python-docx (pip install python-docx)."
        ) from exc
    doc = docx.Document(str(path))
    return "\n".join(par.text for par in doc.paragraphs if par.text.strip()).strip()


def _read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("Reading .pdf needs pypdf (pip install pypdf).") from exc
    reader = PdfReader(str(path))
    parts = [(page.extract_text() or "") for page in reader.pages]
    return "\n".join(parts).strip()
