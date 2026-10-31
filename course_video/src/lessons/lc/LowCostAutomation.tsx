import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/lc/words.json";

// All data comes from narration/low_cost_automation.py (+ import_clones.py for the
// cloned voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "lc",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "The simplest safe device that does the job",
  outroLine: "Simplify. Automate the need. Prove it.",
  outroSub: "Low Cost Automation — never low safety",
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
// L closes the first half; its end card points to M (Muda, Mura, Muri).
export const LOW_COST_AUTOMATION_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "mallet taps an hour, per operator",
    sub: "Sore wrists, and loose grilles rattling at test.", until: "In this lesson",
  },
  recap: {
    problem: "Loose speaker grilles from mallet seating", before: 18, after: 2, unit: "per 1,000 speakers",
    fixedLabel: "Paid back in 4 months",
    takeaways: [
      { text: "Simplify first; never automate waste", cue: "Simplify first" },
      { text: "Simplest safe solution; safety is the first gate", cue: "Choose the simplest" },
      { text: "Prove the real benefit, then maintain it", cue: "And prove the real benefit" },
    ],
    action: { text: "Find one repetitive motion, and ask if it can be eliminated before it's automated.", cue: "Here's your action" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "Next, you'll learn" },
  },
};

export const LowCostAutomation: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...LOW_COST_AUTOMATION_POLISH, sound: captions }} />
);
