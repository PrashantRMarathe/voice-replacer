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

// All data comes from narration/muda_mura_muri.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "mm",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "Waste, unevenness and overburden — improve all three",
  outroLine: "Level. Protect. Remove.",
  outroSub: "The 3M — stable flow, not faster people",
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "cameras behind, one hour before the shift ends",
    sub: "Everyone rushes. Mistakes pile up at test.", until: "In this lesson",
  },
  recap: {
    problem: "Sanjay's line ran late every day", before: 150, after: 0, unit: "minutes of overtime a day",
    takeaways: [
      { text: "Muda waste, Mura unevenness, Muri overburden", cue: "Muda is waste" },
      { text: "They feed each other: improve them together", cue: "They feed each other" },
      { text: "Stable flow, not faster people", cue: "And the goal is" },
    ],
    action: { text: "Walk one product through your line, and tag one example of each M.", cue: "Here's your action" },
    next: { letter: "N", title: "Next Inspection", cue: "Next, you'll learn" },
  },
};

// Dub version (made by tools/make_dub.py): English video, no captions, sound on;
// narration from public/audio/<voice>/, or none (music + effects) when voice is null.
export const MudaMuraMuriDub: React.FC<{ voice?: string | null }> = ({ voice = null }) => {
  setUI("en");
  const blocks = voice ? PLAN.blocks : PLAN.blocks.map((b) => ({ ...b, clips: [] }));
  return (
    <PageLesson data={{ ...DATA, id: voice ?? DATA.id }} blocks={blocks} text={TEXT} captions={false}
      polish={{ ...POLISH, sound: true }} />
  );
};
