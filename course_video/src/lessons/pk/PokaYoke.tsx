import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/pk/words.json";

// All data comes from narration/poka_yoke.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "pk",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "Make the wrong action impossible",
  outroLine: "Eliminate. Prevent. Detect.",
  outroSub: "Poka Yoke — take memory out of quality",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx), approved from the Oct 2026 demo. The Dub
// version keeps it but without sound: its audio is the clean voice stem.
export const POKA_YOKE_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "recorders shipped with a screw missing",
    sub: "The operator was skilled, and careful. Simply human.", until: "In this lesson",
  },
  recap: {
    problem: "Recorders shipped with a missing screw", before: 18, after: 1, unit: "per 10,000 units",
    takeaways: [
      { text: "Errors are predictable: design them out", cue: "Errors are predictable" },
      { text: "Prevent, then detect, then warn", cue: "Prefer prevention" },
      { text: "Challenge every device with bad samples", cue: "And challenge every" },
    ],
    action: { text: "Find one check that relies on memory, and sketch a Poka Yoke for it.", cue: "Here's your action" },
    next: { letter: "Q", title: "QRQC", cue: "Next, you'll learn" },
  },
};

export const PokaYoke: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POKA_YOKE_POLISH, sound: captions }} />
);

export const POKA_YOKE_DATA = DATA;
export const POKA_YOKE_TEXT = TEXT;
