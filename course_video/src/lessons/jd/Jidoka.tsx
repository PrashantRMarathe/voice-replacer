import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/jd/words.json";

// All data comes from narration/jidoka.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "jd",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "Automation with a human touch",
  outroLine: "See it. Stop it. Solve it.",
  outroSub: "Jidoka — no defect forward, no abnormality hidden",
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const JIDOKA_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "patient monitors with a thin seal",
    sub: "The dispenser ran perfectly all night. Its nozzle was half blocked.", until: "In this lesson",
  },
  recap: {
    problem: "Thin seals from a blocked adhesive nozzle", before: 140, after: 1, unit: "monitors affected per nozzle problem",
    fixedLabel: "Caught at the source",
    takeaways: [
      { text: "Define normal first", cue: "Define normal first" },
      { text: "Detect, stop, contain: no defect forward", cue: "Detect, stop and contain" },
      { text: "Every stop is a lesson: fix the root cause", cue: "And treat every stop" },
    ],
    action: { text: "Pick one automatic process, and write down what should make it stop.", cue: "Here's your action" },
    next: { letter: "K", title: "Kaizen", cue: "Next, you'll learn" },
  },
};

export const Jidoka: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...JIDOKA_POLISH, sound: captions }} />
);
