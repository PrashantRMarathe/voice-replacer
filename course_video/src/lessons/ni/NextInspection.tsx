import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ni/words.json";

// All data comes from narration/next_inspection.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "ni",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "The next process is my customer",
  outroLine: "Don't make. Don't pass. Don't accept.",
  outroSub: "Next Inspection — protect the next process",
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "loose connector at station three",
    sub: "Nobody noticed. Then a customer opened the box.", until: "In this lesson",
  },
  recap: {
    problem: "Defects escaping to later stations", before: 18, after: 3, unit: "escapes a week",
    takeaways: [
      { text: "Don't make, don't pass, don't accept", cue: "Don't make" },
      { text: "Check early, and react fast", cue: "Check critical points" },
      { text: "Keep moving controls upstream", cue: "And keep moving" },
    ],
    action: { text: "Pick one hand-off, and write down what the next process needs from it.", cue: "Here's your action" },
    next: { letter: "O", title: "One Point Lesson", cue: "Next, you'll learn" },
  },
};

export const NextInspection: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
