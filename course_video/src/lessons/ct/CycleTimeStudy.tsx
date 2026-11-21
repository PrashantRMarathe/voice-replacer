import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ct/words.json";

// All data comes from narration/cycle_time_study.py (+ import_clones.py for the
// cloned voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "ct",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "Time the real work, find the real bottleneck",
  outroLine: "Define. Measure. Improve the method.",
  outroSub: "Cycle Time Study — evidence before speed",
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const CYCLE_TIME_STUDY_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "seconds: every station looked fast enough",
    sub: "Yet the monitor line missed its hourly target, shift after shift.", until: "In this lesson",
  },
  recap: {
    problem: "Display-test station slower than TAKT", before: 28, after: 23, unit: "seconds per monitor at station C", fixedLabel: "Now inside TAKT",
    takeaways: [
      { text: "Define the boundary first", cue: "Define the boundary" },
      { text: "Look at the spread, not just the average", cue: "Look at the spread" },
      { text: "Fix the method, never skip quality checks", cue: "And fix the method" },
    ],
    action: { text: "Time ten cycles at one station, and compare the longest with TAKT.", cue: "Here's your action" },
    next: { letter: "D", title: "Design Thinking", cue: "Next, you'll learn" },
  },
};

export const CycleTimeStudy: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...CYCLE_TIME_STUDY_POLISH, sound: captions }} />
);
