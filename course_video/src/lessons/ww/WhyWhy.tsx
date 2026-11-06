import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ww/words.json";

// All data comes from narration/why_why.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "ww",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "Dig past the easy answer to a cause you can prove",
  outroLine: "Define. Prove. Prevent.",
  outroSub: "Why–Why — fix the cause, not the person",
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "power", label: "phones failed charging at final test",
    sub: "First answer: operator error. Two days later, it happened again.", until: "In this lesson",
  },
  recap: {
    problem: "Charging failures on Line 2", before: 60, after: 12, unit: "charging defects, same volume",
    fixedLabel: "Root cause fixed: 80% fewer",
    takeaways: [
      { text: "Sharp problem first, then contain", cue: "Start with a sharp problem" },
      { text: "Evidence for every why, then test it", cue: "Back every why" },
      { text: "Fix how it happened and why it escaped", cue: "And fix both" },
    ],
    action: { text: "Take one repeat defect, and write its 5W2H statement.", cue: "Here's your action" },
    next: { letter: "X", title: "X-Matrix", cue: "Next, you'll learn" },
  },
};

export const WhyWhy: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
