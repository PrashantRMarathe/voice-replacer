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
import words from "../../captions/ww_kn/words.json";

// Kannada version of WhyWhyKn (same design and polish as the English lesson).
// All data comes from narration/why_why_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "ಸುಲಭ ಉತ್ತರದಿಂದ ಮುಂದೆ, ನೀವು ಸಾಬೀತುಪಡಿಸಬಲ್ಲ ಕಾರಣದವರೆಗೆ",
  outroLine: "ವ್ಯಾಖ್ಯಾನಿಸಿ. ಸಾಬೀತುಪಡಿಸಿ. ತಡೆಯಿರಿ.",
  outroSub: "Why–Why — ಕಾರಣ ಸರಿಪಡಿಸಿ, ವ್ಯಕ್ತಿಯನ್ನಲ್ಲ",
};

// Same polish as English WhyWhy; cues are phrases from the Kannada intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "ಫೋನ್‌ಗಳು ಫೈನಲ್ ಟೆಸ್ಟ್‌ನಲ್ಲಿ ಚಾರ್ಜಿಂಗ್‌ನಲ್ಲಿ ಫೇಲ್",
    sub: "ಮೊದಲ ಉತ್ತರ: ಆಪರೇಟರ್‌ನ ತಪ್ಪು. ಎರಡು ದಿನದ ನಂತರ, ಮತ್ತೆ ಅದೇ ಆಯಿತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಲೈನ್ 2 ರಲ್ಲಿ ಚಾರ್ಜಿಂಗ್ ಫೇಲ್ಯೂರ್", before: 50, after: 15, unit: "ಚಾರ್ಜಿಂಗ್ ಡಿಫೆಕ್ಟ್, ಅದೇ ವಾಲ್ಯೂಮ್",
    fixedLabel: "ರೂಟ್ ಕಾಸ್ ಸರಿ: 70% ಕಡಿಮೆ",
    takeaways: [
      { text: "ಮೊದಲು ಸ್ಪಷ್ಟ ಸಮಸ್ಯೆ, ನಂತರ ಕಂಟೇನ್‌ಮೆಂಟ್", cue: "ಒಂದು ಸ್ಪಷ್ಟವಾದ ಸಮಸ್ಯೆಯಿಂದ" },
      { text: "ಪ್ರತಿ ಏಕೆಗೆ ಸಾಕ್ಷ್ಯ, ನಂತರ ಪರೀಕ್ಷಿಸಿ", cue: "ಪ್ರತಿ ಏಕೆ ಹಿಂದೆ" },
      { text: "ಹೇಗೆ ಆಯಿತು ಮತ್ತು ಏಕೆ ತಪ್ಪಿಸಿಕೊಂಡಿತು, ಎರಡನ್ನೂ ಸರಿಪಡಿಸಿ", cue: "ಮತ್ತು ಎರಡನ್ನೂ ಸರಿಪಡಿಸಿ" },
    ],
    action: { text: "ಪದೇ ಪದೇ ಬರುವ ಒಂದು ಡಿಫೆಕ್ಟ್ ತೆಗೆದುಕೊಳ್ಳಿ, ಮತ್ತು ಅದರ 5W2H ಸ್ಟೇಟ್‌ಮೆಂಟ್ ಬರೆಯಿರಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "X", title: "X-Matrix", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_KN_DURATION = PLAN.total;

export const WhyWhyKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
