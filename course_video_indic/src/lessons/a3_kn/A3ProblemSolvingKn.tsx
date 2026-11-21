import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { ensureIndicFont } from "../../indicFonts";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/a3_kn/words.json";

// Kannada version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "ಸಮಸ್ಯೆಯ ಪೂರ್ತಿ ಕಥೆ, ಒಂದು ಪುಟದಲ್ಲಿ",
  outroLine: "ಗ್ಯಾಪ್ ನೋಡಿ. ಕಾರಣ ಸಾಬೀತುಪಡಿಸಿ. ಸ್ಥಿರಗೊಳಿಸಿ.",
  outroSub: "A3 — ಉತ್ತಮ ಯೋಚನೆ, ಒಂದು ಶೀಟಿನಲ್ಲಿ",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_KN_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "ಸರ್ವರ್ಗಳು ತಮ್ಮ ಮೊದಲ ಬೂಟ್ ಟೆಸ್ಟ್ನಲ್ಲಿ ಫೇಲ್",
    sub: "ನಾಲ್ಕು ವಾರಗಳಲ್ಲಿ. ಮೊದಲು ಸೂಚಿಸಿದ ಪರಿಹಾರ: ಇನ್ನೂ ಇಬ್ಬರು ಇನ್ಸ್ಪೆಕ್ಟರ್.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಮೊದಲ ಬೂಟ್ ಟೆಸ್ಟ್ನಲ್ಲಿ ಫೇಲ್ ಆಗುತ್ತಿರುವ ಸರ್ವರ್ಗಳು", before: 48, after: 16, unit: "ಪ್ರತಿ 1,000 ಸರ್ವರ್ಗೆ", fixedLabel: "ಟಾರ್ಗೆಟ್ ಪೂರ್ಣ: 48 ಕ್ಕಿಂತ ಕೆಳಗೆ",
    takeaways: [
      { text: "ಅಳೆಯಬಹುದಾದ ಒಂದು ಗ್ಯಾಪ್ನಿಂದ ಆರಂಭಿಸಿ", cue: "ಅಳೆಯಬಹುದಾದ ಒಂದು ಗ್ಯಾಪ್ನಿಂದ" },
      { text: "ಹೋಗಿ ನೋಡಿ; ಪ್ರತಿ ಕಾರಣ ಸಾಬೀತುಪಡಿಸಿ", cue: "ಹೋಗಿ ನೋಡಿ" },
      { text: "ಪೈಲಟ್ನಲ್ಲಿ ಸಾಬೀತಾದದ್ದಕ್ಕೆ ಮಾತ್ರ ಸ್ಟ್ಯಾಂಡರ್ಡ್", cue: "ಮತ್ತು ನಿಮ್ಮ ಪೈಲಟ್" },
    ],
    action: { text: "ಮತ್ತೆ ಮತ್ತೆ ಬರುವ ಒಂದು ಸಮಸ್ಯೆ ಆರಿಸಿ, ಮತ್ತು ಅದರ ಪ್ರಾಬ್ಲಮ್ ಸ್ಟೇಟ್ಮೆಂಟ್ A3 ಮೇಲೆ ಬರೆಯಿರಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "B", title: "Burn Down Chart", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

export const A3ProblemSolvingKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
