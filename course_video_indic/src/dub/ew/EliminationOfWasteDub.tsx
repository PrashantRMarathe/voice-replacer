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

// All data comes from narration/elimination_of_waste.py (+ import_clones.py for the
// cloned voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "ew",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "Remove what your customer won't pay for",
  outroLine: "See it. Remove the cause. Prove it.",
  outroSub: "Elimination of Waste — more value, less effort",
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const ELIMINATION_OF_WASTE_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "soundbars reworked every month",
    sub: "₹42 each to fix. Nobody had ever added it up.", until: "In this lesson",
  },
  recap: {
    problem: "Soundbars reworked for a buzzing speaker wire", before: 1500, after: 300, unit: "reworks a month", fixedLabel: "Rework cut by 80%",
    takeaways: [
      { text: "Waste: what the customer won't pay for", cue: "Waste is anything" },
      { text: "Find it with facts at the gemba", cue: "Find it with facts" },
      { text: "Remove the cause, prove it, hold it", cue: "And remove the cause" },
    ],
    action: { text: "Walk your line for thirty minutes, and write down three wastes as facts.", cue: "Here's your action" },
    next: { letter: "F", title: "FMEA", cue: "Next, you'll learn" },
  },
};

// Dub version (made by tools/make_dub.py): English video, no captions, sound on;
// narration from public/audio/<voice>/, or none (music + effects) when voice is null.
export const EliminationOfWasteDub: React.FC<{ voice?: string | null }> = ({ voice = null }) => {
  setUI("en");
  const blocks = voice ? PLAN.blocks : PLAN.blocks.map((b) => ({ ...b, clips: [] }));
  return (
    <PageLesson data={{ ...DATA, id: voice ?? DATA.id }} blocks={blocks} text={TEXT} captions={false}
      polish={{ ...ELIMINATION_OF_WASTE_POLISH, sound: true }} />
  );
};
