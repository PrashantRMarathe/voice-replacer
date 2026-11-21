import React from "react";
import { PageLesson, LessonText } from "../../lessons/shared/PageLesson";
import type { Polish } from "../../lessons/shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../../lessons/plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "./words.json";

// All data comes from narration/burn_down_chart.py (+ import_clones.py for the
// cloned voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "bd",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "See the work that's left, before the deadline",
  outroLine: "Plan the line. Track the gap. Act today.",
  outroSub: "Burn Down Chart — no more Friday surprises",
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const BURN_DOWN_CHART_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "routers missed the truck",
    sub: "Nobody saw it coming, until Friday afternoon.", until: "In this lesson",
  },
  recap: {
    problem: "Routers short at dispatch", before: 80, after: 0, unit: "routers short",
    takeaways: [
      { text: "Draw the ideal line first; never redraw it", cue: "Draw the ideal line" },
      { text: "Count only work that's complete and good", cue: "Count only work" },
      { text: "Above ideal? Act that day, with an owner", cue: "And when the line" },
    ],
    action: { text: "Pick one job with a deadline, and draw its burn-down before tomorrow's shift.", cue: "Here's your action" },
    next: { letter: "C", title: "Cycle Time Study", cue: "Next, you'll learn" },
  },
};

// Dub version (made by tools/make_dub.py): English video, no captions, sound on;
// narration from public/audio/<voice>/, or none (music + effects) when voice is null.
export const BurnDownChartDub: React.FC<{ voice?: string | null }> = ({ voice = null }) => {
  setUI("en");
  const blocks = voice ? PLAN.blocks : PLAN.blocks.map((b) => ({ ...b, clips: [] }));
  return (
    <PageLesson data={{ ...DATA, id: voice ?? DATA.id }} blocks={blocks} text={TEXT} captions={false}
      polish={{ ...BURN_DOWN_CHART_POLISH, sound: true }} />
  );
};
