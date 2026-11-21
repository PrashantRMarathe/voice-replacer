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
import words from "../../captions/bd_kn/words.json";

// Kannada version of BurnDownChartKn (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "ಡೆಡ್ಲೈನ್ಗಿಂತ ಮೊದಲು ಉಳಿದ ಕೆಲಸ ನೋಡಿ",
  outroLine: "ಲೈನ್ ನಿರ್ಧರಿಸಿ. ಗ್ಯಾಪ್ ನೋಡಿ. ಇಂದೇ ಕ್ರಮ ತೆಗೆದುಕೊಳ್ಳಿ.",
  outroSub: "Burn Down Chart — ಇನ್ನು ಶುಕ್ರವಾರದ ಆಘಾತಗಳಿಲ್ಲ",
};

// Same polish as English BurnDownChart; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "ರೌಟರ್ಗಳು ಟ್ರಕ್ ತಪ್ಪಿಸಿಕೊಂಡವು",
    sub: "ಶುಕ್ರವಾರ ಮಧ್ಯಾಹ್ನದವರೆಗೆ ಯಾರಿಗೂ ಅಂದಾಜೇ ಇರಲಿಲ್ಲ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಡಿಸ್ಪ್ಯಾಚ್ನಲ್ಲಿ ಕಡಿಮೆ ಬಿದ್ದ ರೌಟರ್ಗಳು", before: 80, after: 0, unit: "ರೌಟರ್ಗಳು ಕಡಿಮೆ",
    takeaways: [
      { text: "ಮೊದಲು ಐಡಿಯಲ್ ಲೈನ್; ಅದನ್ನು ಮತ್ತೆ ಎಂದಿಗೂ ಇಲ್ಲ", cue: "ಮೊದಲು ಐಡಿಯಲ್ ಲೈನ್" },
      { text: "ಪೂರ್ಣವಾದ ಮತ್ತು ಒಳ್ಳೆಯ ಕೆಲಸ ಮಾತ್ರ ಎಣಿಸಿ", cue: "ನಿಜವಾಗಿ ಪೂರ್ಣವಾದ" },
      { text: "ಐಡಿಯಲ್ಗಿಂತ ಮೇಲೆ? ಅದೇ ದಿನ ಕ್ರಮ, ಓನರ್ ಜೊತೆ", cue: "ಮತ್ತು ಲೈನ್" },
    ],
    action: { text: "ಡೆಡ್ಲೈನ್ ಇರುವ ಒಂದು ಕೆಲಸ ಆರಿಸಿ, ಮತ್ತು ನಾಳಿನ ಶಿಫ್ಟ್ಗಿಂತ ಮೊದಲು ಅದರ ಬರ್ನ್-ಡೌನ್ ಮಾಡಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "C", title: "Cycle Time Study", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_KN_DURATION = PLAN.total;

export const BurnDownChartKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
