import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/xm/words.json";

// All data comes from narration/x_matrix.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "xm",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Turn strategy into action with Hoshin Kanri",
  outroLine: "Align. Deploy. Review.",
  outroSub: "X-Matrix — strategy you can actually execute",
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "improvement projects, every team busy",
    sub: "Yet delivery still slipped, quarter after quarter.", until: "In this lesson",
  },
  recap: {
    problem: "A busy portfolio, slipping delivery", before: 40, after: 3, unit: "projects, each linked to a goal and a KPI",
    fixedLabel: "Focused portfolio",
    takeaways: [
      { text: "A few real priorities, not a wish list", cue: "Pick a few real priorities" },
      { text: "Goal → project → KPI → one owner", cue: "Link every goal" },
      { text: "Review honestly: the numbers must move", cue: "And review honestly" },
    ],
    action: { text: "Write one objective for your area as an outcome, not an activity.", cue: "Here's your action" },
    next: { letter: "Y", title: "Yamazumi", cue: "See you in the next one" },
  },
};

export const XMatrix: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
