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

// All data comes from narration/skill_matrix.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "sk",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "Who can really do which job — and where the gaps are",
  outroLine: "Assess. Train. Cover.",
  outroSub: "Skill Matrix — a live capability control",
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "person who can set up lens focus",
    sub: "Bala called in sick. By ten, the whole cell had stopped.", until: "In this lesson",
  },
  recap: {
    problem: "One lens focus expert, and he was off sick", before: 1, after: 2, unit: "qualified lens focus experts",
    takeaways: [
      { text: "Demonstrated ability, not attendance", cue: "A skill matrix shows" },
      { text: "Count qualified backups, every shift", cue: "Count qualified backups" },
      { text: "Keep it live, with evidence", cue: "And keep it live" },
    ],
    action: { text: "List your three most critical stations, and count the qualified people for each.", cue: "Here's your action" },
    next: { letter: "T", title: "TAKT Time", cue: "Next, you'll learn" },
  },
};

// Dub version (made by tools/make_dub.py): English video, no captions, sound on;
// narration from public/audio/<voice>/, or none (music + effects) when voice is null.
export const SkillMatrixDub: React.FC<{ voice?: string | null }> = ({ voice = null }) => {
  setUI("en");
  const blocks = voice ? PLAN.blocks : PLAN.blocks.map((b) => ({ ...b, clips: [] }));
  return (
    <PageLesson data={{ ...DATA, id: voice ?? DATA.id }} blocks={blocks} text={TEXT} captions={false}
      polish={{ ...POLISH, sound: true }} />
  );
};
