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

// All data comes from narration/ishikawa.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "ik",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "Search wide with the fishbone, then prove the cause",
  outroLine: "Search wide. Prove narrow.",
  outroSub: "Ishikawa — every bone is a guess until tested",
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const ISHIKAWA_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "switches per 1,000 failing port test",
    sub: "Up from 5. The meeting's answer: buy a new tester.", until: "In this lesson",
  },
  recap: {
    problem: "Port-link failures on the switch line", before: 32, after: 4, unit: "per 1,000 switches",
    fixedLabel: "Both causes fixed",
    takeaways: [
      { text: "A sharp, measurable effect at the head", cue: "Start with a sharp" },
      { text: "Search widely across the 6M, no blame", cue: "Search widely" },
      { text: "Every bone is a guess until proven", cue: "And treat every bone" },
    ],
    action: { text: "Draw a fishbone for one recurring problem, and pick three causes to test.", cue: "Here's your action" },
    next: { letter: "J", title: "Jidoka", cue: "Next, you'll learn" },
  },
};

// Dub version (made by tools/make_dub.py): English video, no captions, sound on;
// narration from public/audio/<voice>/, or none (music + effects) when voice is null.
export const IshikawaDub: React.FC<{ voice?: string | null }> = ({ voice = null }) => {
  setUI("en");
  const blocks = voice ? PLAN.blocks : PLAN.blocks.map((b) => ({ ...b, clips: [] }));
  return (
    <PageLesson data={{ ...DATA, id: voice ?? DATA.id }} blocks={blocks} text={TEXT} captions={false}
      polish={{ ...ISHIKAWA_POLISH, sound: true }} />
  );
};
