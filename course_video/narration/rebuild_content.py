"""Rebuild src/lessons/<ID>/content.json from narration/<lesson>.py and the words
already on disk (no re-voicing). Use after editing a lesson's on-screen text,
points or visuals.
  python narration/rebuild_content.py muda_mura_muri
"""
import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
for name in sys.argv[1:]:
    m = importlib.import_module(name)
    words = json.loads((ROOT / f"src/captions/{m.ID}/words.json").read_text(encoding="utf-8"))
    pages = [lesson_lib.page_content(p, words.get(p["key"])) for p in m.PAGES]
    out = ROOT / f"src/lessons/{m.ID}/content.json"
    out.write_text(json.dumps({"pages": pages}, indent=2, ensure_ascii=False), encoding="utf-8")
    synced = sum(1 for p in pages if "at" in p)
    pics = sum(1 for p in pages if "visual" in p)
    print(f"src/lessons/{m.ID}/content.json: {len(pages)} pages, {synced} synced, {pics} with a picture")
