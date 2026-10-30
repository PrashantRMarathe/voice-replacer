"""Import the user's CLONED voice clips for any page lesson and rebuild timing.

  python narration/import_clones.py <lesson> [clones_dir]
  python narration/import_clones.py <lesson> --realign   # captions only, from current clips

<lesson> is the lesson module name in narration/ (e.g. yamazumi, zero_defects).
Default clones_dir: Downloads/clones/clones/<lesson>  (one <key>.wav per clip).
"""
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

if len(sys.argv) < 2:
    raise SystemExit(__doc__)
mod = importlib.import_module(sys.argv[1])
if "--realign" in sys.argv:
    lesson_lib.realign(mod)
    raise SystemExit
clones = Path(sys.argv[2]) if len(sys.argv) > 2 else lesson_lib.DEFAULT_CLONES / mod.NAME
lesson_lib.import_clones(mod, clones)
