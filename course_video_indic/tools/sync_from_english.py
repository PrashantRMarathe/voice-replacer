"""Bring this project up to date with the English course's design, then re-apply
the Indian-language changes. READS ../course_video only; never writes there.

  python tools/sync_from_english.py

Every change is an exact-match replacement: if the English code changed at one
of these spots, the script stops and names it (fix the anchor here, re-run)."""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent          # course_video_indic
EN = HERE.parent / "course_video"                      # the English project (read only)

# Shared code and assets copied as-is from English. Lesson files, Root.tsx,
# scripts/lessons.ts, src/ui.ts and src/indicFonts.ts are this project's own.
COPY = [
    "src/components", "src/scenes", "src/lessons/shared", "src/lessons/plan.ts",
    "src/theme.ts", "src/fonts.ts", "src/index.ts",
    "scripts/check.ts", "scripts/srt.ts",
    "narration/lesson_lib.py", "narration/lint_scripts.py", "narration/import_clones.py",
    "public/audio/sfx", "public/audio/music.mp3", "public/fonts",
]

errors = []


def patch(rel, old, new, count=1):
    p = HERE / rel
    s = p.read_text(encoding="utf-8")
    if s.count(old) != count:
        errors.append(f"{rel}: expected {count}x, found {s.count(old)}x: {old[:70]!r}")
        return
    p.write_text(s.replace(old, new), encoding="utf-8")


def use_ui(rel, depth):
    """Import UI (src/ui.ts) after the file's first import line."""
    p = HERE / rel
    s = p.read_text(encoding="utf-8")
    first = s.index("\n", s.index("import ")) + 1
    p.write_text(s[:first] + f'import {{ UI }} from "{"../" * depth}ui";\n' + s[first:], encoding="utf-8")


def main():
    for rel in COPY:
        src, dst = EN / rel, HERE / rel
        if dst.is_dir():
            shutil.rmtree(dst)
        dst.parent.mkdir(parents=True, exist_ok=True)
        (shutil.copytree if src.is_dir() else shutil.copy2)(src, dst)
    print(f"copied {len(COPY)} items from {EN}")

    # --- on-screen words -> src/ui.ts ---
    q = "src/components/Quiz.tsx"
    use_ui(q, 1)
    patch(q, "QUICK CHECK #{data.num}", "{UI.quickCheck} #{data.num}")
    patch(q, 'Think{"…"} {countdown}', "{UI.think} {countdown}")
    patch(q, ">ANSWER</div>", ">{UI.answer}</div>")

    pl = "src/lessons/shared/PageLesson.tsx"
    use_ui(pl, 2)
    patch(pl, ">EXAMPLE</div>", ">{UI.example}</div>", count=2)

    pv = "src/components/PageVisual.tsx"
    use_ui(pv, 1)
    patch(pv, '{v.top ?? "STRONGEST"}', "{v.top ?? UI.strongest}")
    patch(pv, '{v.bottom ?? "WEAKEST"}', "{v.bottom ?? UI.weakest}")
    patch(pv, '{good ? "GOOD" : "NOT GOOD"}', "{good ? UI.good : UI.notGood}")
    patch(pv, '${v.label ?? "Average"}', "${v.label ?? UI.average}")
    # assembly counter: translated words, and the theme fonts (Poppins/Inter alone
    # have no Indian-script glyphs, so this SVG text would draw empty boxes)
    patch(pv, 'fontFamily="Poppins" fontWeight={700} fontSize={44}>\n          {`Screws ${screws}/6`}',
          "fontFamily={theme.font.heading} fontWeight={700} fontSize={44}>\n          {UI.screws(screws)}")
    patch(pv, 'fontFamily="Inter" fontSize={26}>\n          {done ? "All good: fixture releases" : "Fixture locked until 6/6"}',
          "fontFamily={theme.font.body} fontSize={26}>\n          {done ? UI.fixtureReleases : UI.fixtureLocked}")

    po = "src/lessons/shared/polish.tsx"
    use_ui(po, 2)
    patch(po, ">REMEMBER THE START?</div>", ">{UI.rememberStart}</div>")
    patch(po, ">THREE THINGS TO REMEMBER</div>", ">{UI.threeThings}</div>")
    patch(po, ">YOUR ACTION THIS WEEK</div>", ">{UI.actionThisWeek}</div>")
    patch(po, 'recap.next.kicker ?? "NEXT LESSON"', "recap.next.kicker ?? UI.nextLesson")
    patch(po, 'recap.fixedLabel ?? "Problem fixed"', "recap.fixedLabel ?? UI.problemFixed")
    # cue matching kept only a-z/0-9, so every Hindi word became "" and all cues
    # fired at the start: keep letters, digits and vowel signs of any script
    patch(po, """const norm = (s: string) => s.toLowerCase().replace(/[^a-z0-9']/g, "");""",
          """const norm = (s: string) => s.toLowerCase().replace(/[^\\p{L}\\p{N}\\p{M}']/gu, "");""")

    # --- letter spacing splits Indian-script letters apart ("अ ग ला"): turn it off ---
    import re
    for f in list((HERE / "src/components").glob("*.tsx")) + list((HERE / "src/lessons/shared").glob("*.tsx")):
        s = f.read_text(encoding="utf-8")
        f.write_text(re.sub(r"letterSpacing: [0-9.]+", "letterSpacing: 0", s), encoding="utf-8")

    # --- fonts: Indian scripts after the course fonts (loaded by src/indicFonts.ts) ---
    patch("src/theme.ts", """    heading: '"Poppins", system-ui, sans-serif',
    body: '"Inter", system-ui, sans-serif',""",
          """    heading: '"Poppins", "Noto Sans Devanagari", "Noto Sans Tamil", "Noto Sans Kannada", "Noto Sans Telugu", system-ui, sans-serif',
    body: '"Inter", "Noto Sans Devanagari", "Noto Sans Tamil", "Noto Sans Kannada", "Noto Sans Telugu", system-ui, sans-serif',""")

    # --- sentence ends: Hindi/Marathi danda ---
    patch("src/lessons/plan.ts", "    if (/[.!?][\"”']?$/.test(w.w)) {",
          "    if (/[.!?।][\"”']?$/.test(w.w)) {  // । = danda (Hindi, Marathi)")
    patch("narration/lesson_lib.py", 'breaks = [k for k in range(1, n) if ends(k, ".!?")]',
          'breaks = [k for k in range(1, n) if ends(k, ".!?।")]  # । = danda (Hindi, Marathi)')
    patch("narration/lesson_lib.py",
          '    comm = edge_tts.Communicate(say(mod, text), VOICE, rate=RATE, boundary="WordBoundary")',
          '    # each lesson sets its own voice (e.g. hi-IN-MadhurNeural)\n'
          '    comm = edge_tts.Communicate(say(mod, text), getattr(mod, "VOICE", VOICE), rate=RATE, boundary="WordBoundary")')

    # --- script lint: Indian-language mode ---
    L = "narration/lint_scripts.py"
    patch(L, "MAX_SENT_WORDS = 20\n",
          "MAX_SENT_WORDS = 20\nMAX_SENT_WORDS_INDIC = 26  # Hindi etc. spell postpositions as separate words\n")
    patch(L, 'return [s for s in re.split(r"(?<=[.!?])\\s+", text.strip()) if s]',
          'return [s for s in re.split(r"(?<=[.!?।])\\s+", text.strip()) if s]  # । = danda')
    patch(L, '''    add = lambda where, msg: issues.append(f"{where}: {msg}")

    if re.match(''', '''    add = lambda where, msg: issues.append(f"{where}: {msg}")
    # A translated lesson (LANG = "hi", ...) skips the English-only style rules.
    en = getattr(mod, "LANG", "en") == "en"

    if en and re.match(''')
    patch(L, '''    unclear = sorted({w for _, t in clips for w in re.findall(r"\\b[A-Z]{2,}\\b", spoken(t))})
    if unclear:''', '''    if not en:
        # the Indian-language voice reads its own script only: every English
        # term needs a native-script form in say() (captions keep the English)
        latin = sorted({w for _, t in clips for w in re.findall(r"[A-Za-z][A-Za-z'-]*", spoken(t))})
        if latin:
            add("lesson", f"English left in the spoken text: {', '.join(latin)} (add it to say())")
    unclear = sorted({w for _, t in clips for w in re.findall(r"\\b[A-Z]{2,}\\b", spoken(t))})
    if en and unclear:''')
    patch(L, '''            words = len(s.split())
            if words > MAX_SENT_WORDS:
                add(key, f"{words}-word sentence (max {MAX_SENT_WORDS}): \\"{' '.join(s.split()[:8])}...\\"")
            if number_words(s) > MAX_NUMBER_WORDS:''', '''            words, cap = len(s.split()), MAX_SENT_WORDS if en else MAX_SENT_WORDS_INDIC
            if words > cap:
                add(key, f"{words}-word sentence (max {cap}): \\"{' '.join(s.split()[:8])}...\\"")
            if en and number_words(s) > MAX_NUMBER_WORDS:''')
    # the second "for p in mod.PAGES:" is the English-only words/"you" check
    p = HERE / L
    s = p.read_text(encoding="utf-8")
    i = s.index("    for p in mod.PAGES:", s.index("    for p in mod.PAGES:") + 1)
    p.write_text(s[:i] + "    if not en:\n        return issues\n" + s[i:], encoding="utf-8")
    patch(L, "def main():\n", 'def main():\n    sys.stdout.reconfigure(encoding="utf-8")  # Hindi on a cp1252 console\n')

    if errors:
        print("STOP: the English code changed at these spots; update the anchors in this script:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("Indian-language changes applied. Next: npm run check")


if __name__ == "__main__":
    main()
