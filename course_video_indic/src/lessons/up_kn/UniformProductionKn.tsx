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
import words from "../../captions/up_kn/words.json";

// Kannada version of UniformProductionKn (same design and polish as the English lesson).
// All data comes from narration/uniform_production_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "ವಾಲ್ಯೂಮ್ ಮತ್ತು ಮಿಕ್ಸ್ ಲೆವೆಲ್ ಮಾಡಿ, ಸ್ಥಿರ ಮತ್ತು ನಂಬಲರ್ಹ ಫ್ಲೋಗಾಗಿ",
  outroLine: "ಲೆವೆಲ್ ಮಾಡಿ. ಕ್ರಮ ನಿರ್ಧರಿಸಿ. ಸ್ಥಿರಗೊಳಿಸಿ.",
  outroSub: "Uniform Production — ನಿಮ್ಮ ಲೈನ್ ಉಳಿಸಿಕೊಳ್ಳಬಲ್ಲ ವೇಗ",
};

// Same polish as English UniformProduction; cues are phrases from the Kannada intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "ಫೋನ್ ಸೋಮವಾರ. ಮಂಗಳವಾರ ಸುಮಾರು ಏನೂ ಇಲ್ಲ.",
    sub: "ಬುಧವಾರದ ಹೊತ್ತಿಗೆ, ಟೆಸ್ಟ್ ಬೆಂಚ್ ಕೆಲಸದಲ್ಲಿ ಮುಳುಗಿದೆ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ತುಂಬಾ ಏರುಪೇರಿನ ಒಂದು ಶೆಡ್ಯೂಲ್", before: 0, after: 6000, unit: "ದಿನಕ್ಕೆ ಒಳ್ಳೆಯ ಯೂನಿಟ್, ಪ್ರತಿದಿನ",
    fixedLabel: "ಒಂದು ಸ್ಥಿರ, ಲೆವೆಲ್ ವೇಗ",
    takeaways: [
      { text: "ವಾಲ್ಯೂಮ್ ಮತ್ತು ಮಿಕ್ಸ್, ಎರಡನ್ನೂ ಲೆವೆಲ್ ಮಾಡಿ", cue: "ವಾಲ್ಯೂಮ್ ಮತ್ತು ಮಿಕ್ಸ್, ಎರಡನ್ನೂ" },
      { text: "ಮೊದಲು ಬಾಟಲ್ನೆಕ್ ಮತ್ತು ಚೇಂಜ್ಓವರ್ ಪರಿಶೀಲಿಸಿ", cue: "ಯಾವುದೇ ಪ್ಯಾಟರ್ನ್ ಅನ್ನು" },
      { text: "ಕಾಣುವ ಪ್ಲಾನ್, ಬದಲಾವಣೆಯ ಸ್ಪಷ್ಟ ನಿಯಮಗಳು", cue: "ಮತ್ತು ಪ್ಲಾನ್ ಅನ್ನು" },
    ],
    action: { text: "ದೊಡ್ಡ ಬ್ಯಾಚ್ನಲ್ಲಿ ಆಗುವ ಒಂದು ಪ್ರಾಡಕ್ಟ್ ಹುಡುಕಿ, ಮತ್ತು ಚಿಕ್ಕ, ಪುನರಾವರ್ತಿತ ಪ್ಯಾಟರ್ನ್ನ ಸ್ಕೆಚ್ ಮಾಡಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_KN_DURATION = PLAN.total;

export const UniformProductionKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
