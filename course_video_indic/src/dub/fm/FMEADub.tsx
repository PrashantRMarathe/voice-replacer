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

// All data comes from narration/fmea.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "fm",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "Failure Mode and Effects Analysis: think before failure",
  outroLine: "Chain it. Score it. Prevent it.",
  outroSub: "FMEA — a living plan, not a form",
};

const PLAN = planLesson(DATA, fps);
export const FMEA_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const FMEA_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "outdoor radios came back full of water",
    sub: "Gasket missing in two, twisted in four. All passed final inspection.", until: "In this lesson",
  },
  recap: {
    problem: "Gasket risk on the outdoor 5G radio", before: 240, after: 32, unit: "risk priority number",
    fixedLabel: "Risk cut, proven in a trial",
    takeaways: [
      { text: "Effect → failure mode → controllable cause", cue: "Build a clear chain" },
      { text: "Score with evidence; judgement over numbers", cue: "Score with evidence" },
      { text: "Prevent first, prove it, then rescore", cue: "And prefer prevention" },
    ],
    action: { text: "Pick one critical step, and write its failure chain with your team.", cue: "Here's your action" },
    next: { letter: "G", title: "Gemba", cue: "Next, you'll learn" },
  },
};

// Dub version (made by tools/make_dub.py): English video, no captions, sound on;
// narration from public/audio/<voice>/, or none (music + effects) when voice is null.
export const FMEADub: React.FC<{ voice?: string | null }> = ({ voice = null }) => {
  setUI("en");
  const blocks = voice ? PLAN.blocks : PLAN.blocks.map((b) => ({ ...b, clips: [] }));
  return (
    <PageLesson data={{ ...DATA, id: voice ?? DATA.id }} blocks={blocks} text={TEXT} captions={false}
      polish={{ ...FMEA_POLISH, sound: true }} />
  );
};
