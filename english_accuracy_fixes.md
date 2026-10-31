# English course: accuracy fixes (30 Oct 2026)

Patch: `english_accuracy_fixes.patch` (script files in `course_video/narration/` only).
Apply in your copy: `git apply --3way english_accuracy_fixes.patch`. If a hunk fails because
you already changed that page, apply the fix below by hand.
Lint (`python narration/lint_scripts.py`) passes for all 26 lessons with these changes.

## What changed
1. QRQC p05: now 24 of 800 (was 18 of 600), same as the p12 case. QRQC p12 cause is now the
   wrong focus recipe (matches its own p08 fix), not the spacer used in Root Cause.
2. Why-Why: p03 now 21 of 700 phones (3%); p12 now 50 → 15, 70% drop, ₹30,000/month,
   4-month payback. These no longer duplicate the QRQC and Root Cause numbers.
3. Design Thinking p12: hypothesis is now "cycle time inside TAKT, label errors cut by at least
   three quarters". The p13 results meet it.
4. X-Matrix quiz2: "A plant's" delivery goal (Arjun's IS linked on p11).
5. Yamazumi quiz1: Station 4 / Station 1 (Meera's Station C is 27 s).
6. Cycle Time p06: station C breakdown now includes the serial label
   (4 + 3 + 13 + 4 + 3 + 1 = 28 s), matching p11 and p13.
7. Polish:
   - QRQC p11: "not done"
   - Yamazumi p12: "two measures … mean"
   - Skill Matrix p01: board assembly, lens focus
   - TAKT p03: 420 net minutes
   - Waste p15: "eleven days"
   - American spelling throughout (color, behavior, favorite, center, practice, trialed,
     Standardize)

## Clips to re-clone (spoken text changed)
| Lesson | Clips |
|---|---|
| cycle_time_study | p06 |
| design_thinking | p12 |
| elimination_of_waste | p15 |
| gemba | p14 (spelling only) |
| hancho | p07 (spelling only) |
| one_point_lesson | p05, p08, p13 (spelling only) |
| qrqc | p05, p07, p11, p12 (p07 spelling only) |
| skill_matrix | p01, p08 (p08 spelling only) |
| takt_time | p03 |
| why_why | p03, p12 |
| x_matrix | quiz2_q |
| yamazumi | p12, quiz1_q, quiz1_a |
| zero_defects | p13 (spelling only) |

poka_yoke changed on screen only, so no clone is needed; just re-render.
"Spelling only" clips sound the same. You can keep their audio and run
`import_clones.py <lesson> --realign` to redo the captions instead of re-cloning.

Marathi `qrqc_mr` already has fixes 1–2, is re-voiced (female, Aarohi) and is re-rendered.

---

# Second full check (31 Oct 2026)

All 26 English lessons re-read end to end (intro, pages, points, examples, diagram labels,
chart numbers, quizzes, outro). Every calculation and every story number checks out across
pages, and captions match the current scripts in all lessons. Fixes made:

1. **Why-Why intro**: "Twenty-four phones" → "Twenty-one phones" (p03 says 21 of 700; the
   intro was missed in the first pass). **Re-clone `why_why` intro.**
   The Hindi `why_why_hi` intro has the same slip (चौबीस → इक्कीस).
2. **A3 p02**: "Operators are careless is a blame" → "is blame". **Re-clone `a3_problem_solving` p02.**
3. Screen only (no re-clone): Design Thinking p14 example now says the packers were
   left-handed (matches the voice); Hancho p12 example says operators "bent" the cable (matches the voice).
4. American spelling (sounds the same, captions realigned, no re-clone): labor (Poka Yoke p02,
   LCA p13), millimeters (Jidoka p05), meters (Muda p10), traveled (Next Inspection intro),
   theater (QRQC p07), judgment (FMEA p12 + outro), DEFENSE (Next Inspection p03 diagram).

Captions and screen data rebuilt with `import_clones.py <lesson> --realign`; `npm run check` passes.
