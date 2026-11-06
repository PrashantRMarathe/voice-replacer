import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/gb/words.json";

// All data comes from narration/gemba.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "gb",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "Real place, real thing, real facts",
  outroLine: "Go. See. Confirm.",
  outroSub: "Gemba, Genbutsu, Genjitsu — facts before decisions",
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const GEMBA_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× the earbud failures on shift B",
    sub: "The plan: retrain shift B. Nobody had looked at a failed earbud.", until: "In this lesson",
  },
  recap: {
    problem: "Earbuds failing audio test", before: 20, after: 5, unit: "failures per 1,000 earbuds",
    fixedLabel: "Fixed at the cause",
    takeaways: [
      { text: "Go to the real place; watch real cycles", cue: "Go to the real place" },
      { text: "Hold the real thing; compare with a good one", cue: "Hold the real thing" },
      { text: "Check the real facts, with a denominator", cue: "And check the real facts" },
    ],
    action: { text: "Take one recurring problem, and do a thirty-minute 3G visit.", cue: "Here's your action" },
    next: { letter: "H", title: "Hancho", cue: "Next, you'll learn" },
  },
};

export const Gemba: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...GEMBA_POLISH, sound: captions }} />
);
