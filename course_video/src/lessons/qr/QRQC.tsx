import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/qr/words.json";

// All data comes from narration/qrqc.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "qr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "React in minutes — close with evidence",
  outroLine: "Detect. Contain. Prove.",
  outroSub: "QRQC — fast reaction, real evidence",
};

const PLAN = planLesson(DATA, fps);
export const QRQC_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "camera", label: "cameras failing focus test by noon",
    sub: "Someone reset the tester, and the line ran on.", until: "In this lesson",
  },
  recap: {
    problem: "Suspect cameras heading for the warehouse", before: 2000, after: 0, unit: "suspect cameras unaccounted for",
    takeaways: [
      { text: "React fast, but with evidence", cue: "React fast" },
      { text: "Contain first, reconcile every unit", cue: "Contain first" },
      { text: "Close only when the fix is proven", cue: "And close an issue" },
    ],
    action: { text: "Write the first 30 minutes of your reaction plan for one critical defect.", cue: "Here's your action" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "Next, you'll go deeper" },
  },
};

export const QRQC: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
