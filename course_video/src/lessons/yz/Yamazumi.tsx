import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/yz/words.json";

// All data comes from narration/yamazumi.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "yz",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "Balance the line against TAKT — with real data",
  outroLine: "Measure. Stack. Balance.",
  outroSub: "Yamazumi — flow that holds, by design",
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "operators waiting, while one is buried in screws",
    sub: "Nobody is lazy. The work is just stacked unevenly.", until: "In this lesson",
  },
  recap: {
    problem: "Station B above TAKT", before: 35, after: 30, unit: "seconds of work at Station B",
    fixedLabel: "Back on TAKT",
    takeaways: [
      { text: "Measure the real work, not the best case", cue: "Measure the real work" },
      { text: "Stack it against TAKT to see the piles", cue: "Stack it against" },
      { text: "Rebalance without risking safety or quality", cue: "And rebalance with care" },
    ],
    action: { text: "Time one station on your line, and draw its bar against TAKT.", cue: "Your action this week" },
    next: { letter: "Z", title: "Zero Defects", cue: "See you in the next one" },
  },
};

export const Yamazumi: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
