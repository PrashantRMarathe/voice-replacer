"""Script lint: checks every page lesson's narration against the style guide
(docs/PLAYBOOK.md §4b). Run by `npm run check`; style issues are warnings, so
they never block a render.

  python narration/lint_scripts.py              all lessons, summary + details
  python narration/lint_scripts.py zero_defects  one lesson
  python narration/lint_scripts.py --strict      exit 1 on any issue
"""
import importlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

MAX_SENT_WORDS = 20
PAGE_WORDS = (60, 90)          # guide target is 65-80
MAX_FOR_EXAMPLE = 3
MAX_NUMBER_WORDS = 5
NUMBER = re.compile(
    r"^(\d[\d,.]*%?|zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|"
    r"fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|percent|point|half)$", re.I)
YOU = re.compile(r"\byou(r|rs|'ll|'re|'ve)?\b", re.I)


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def number_words(sentence):
    n = 0
    for w in re.findall(r"[\w,.%'-]+", sentence):
        n += sum(1 for part in w.strip(".,").split("-") if NUMBER.match(part))
    return n


def lint(mod):
    issues = []
    add = lambda where, msg: issues.append(f"{where}: {msg}")

    if re.match(r"\s*welcome to (this|the|our) lesson", mod.INTRO_SCRIPT, re.I):
        add("intro", 'opens with "Welcome to this lesson" (start with a hook)')

    clips = [("intro", mod.INTRO_SCRIPT), ("outro", mod.OUTRO_SCRIPT)]
    clips += [(p["key"], p["script"]) for p in mod.PAGES]
    for q in mod.QUIZZES:
        clips += [(f"{q['key']}_q", q["q_script"]), (f"{q['key']}_a", q["a_script"])]

    # What the voice will actually read: after the lesson's say() fixes. Any
    # ALL-CAPS word still there has an unconfirmed pronunciation -> ask the user.
    spoken = mod.say if hasattr(mod, "say") else (lambda t: t)
    # also terms mixing digits and capitals ("A3", "5W2H"), which the voice may misread
    unclear = sorted({w for _, t in clips
                      for w in re.findall(r"\b[A-Z]{2,}\b|\b(?=\w*\d)(?=\w*[A-Z])\w+\b", spoken(t))})
    if unclear:
        add("lesson", f"ask the user how to pronounce: {', '.join(unclear)} "
                      "(then spell it out, e.g. 'P-P-M', or add it to say())")

    for key, text in clips:
        for s in sentences(text):
            words = len(s.split())
            if words > MAX_SENT_WORDS:
                add(key, f"{words}-word sentence (max {MAX_SENT_WORDS}): \"{' '.join(s.split()[:8])}...\"")
            if number_words(s) > MAX_NUMBER_WORDS:
                add(key, f"number-heavy sentence ({number_words(s)} number words); let the screen show the math")

    # On-screen boxes must match the voice: each point's cue is a phrase the
    # narration really says, in spoken order, and so is the example's cue.
    from lesson_lib import cue_index
    for p in mod.PAGES:
        points = p.get("points", [])
        if not 2 <= len(points) <= 6:
            add(p["key"], f"{len(points)} points (use 2-6, each one spoken in the script)")
        try:
            at = [cue_index(p["script"], c) for _, c in points]
            if at != sorted(at):
                add(p["key"], "points are not in the order the narration says them")
            cue_index(p["script"], p.get("example_cue", ""))
        except ValueError as e:
            add(p["key"], str(e))

    for p in mod.PAGES:
        words = len(p["script"].split())
        if not PAGE_WORDS[0] <= words <= PAGE_WORDS[1]:
            add(p["key"], f"{words} words (aim 65-80)")
        if not YOU.search(p["script"]) and "?" not in p["script"]:
            add(p["key"], 'no "you"/"your" and no question; talk to the learner')

    fe = sum(len(re.findall(r"\bfor example\b", t, re.I)) for _, t in clips)
    if fe > MAX_FOR_EXAMPLE:
        add("lesson", f'"For example" used {fe} times (max {MAX_FOR_EXAMPLE}); vary the rhythm')
    return issues


def lesson_modules():
    for f in sorted(HERE.glob("*.py")):
        src = f.read_text(encoding="utf-8")
        if "lesson_lib.main(sys.modules" in src and re.search(r"^PAGES = ", src, re.M):
            yield f.stem


def main():
    args =[a for a in sys.argv[1:] if not a.startswith("--")]
    names = args or list(lesson_modules())
    total = 0
    for name in names:
        issues = lint(importlib.import_module(name))
        total += len(issues)
        print(f"script  {name:16} {'OK' if not issues else f'{len(issues)} style issue(s)'}")
        for i in issues:
            print(f"  style {i}")
    if total and "--strict" in sys.argv:
        sys.exit(1)


if __name__ == "__main__":
    main()
