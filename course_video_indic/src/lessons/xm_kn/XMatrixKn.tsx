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
import words from "../../captions/xm_kn/words.json";

// Kannada version of XMatrixKn (same design and polish as the English lesson).
// All data comes from narration/x_matrix_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Hoshin Kanri ಮೂಲಕ ತಂತ್ರವನ್ನು ಆ್ಯಕ್ಷನ್ ಆಗಿ ಬದಲಾಯಿಸಿ",
  outroLine: "ಜೋಡಿಸಿ. ಜಾರಿಗೊಳಿಸಿ. ರಿವ್ಯೂ ಮಾಡಿ.",
  outroSub: "X-Matrix — ನೀವು ನಿಜವಾಗಿ ಜಾರಿಗೊಳಿಸಬಲ್ಲ ತಂತ್ರ",
};

// Same polish as English XMatrix; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "ಇಂಪ್ರೂವ್‌ಮೆಂಟ್ ಪ್ರಾಜೆಕ್ಟ್, ಪ್ರತಿ ತಂಡ ಬ್ಯುಸಿ",
    sub: "ಆದರೂ ಡೆಲಿವರಿ ಪ್ರತಿ ತ್ರೈಮಾಸಿಕ ಜಾರುತ್ತಲೇ ಇತ್ತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಬ್ಯುಸಿ ಪೋರ್ಟ್‌ಫೋಲಿಯೋ, ಜಾರುವ ಡೆಲಿವರಿ", before: 40, after: 3, unit: "ಪ್ರಾಜೆಕ್ಟ್, ಪ್ರತಿಯೊಂದೂ ಒಂದು ಗುರಿ ಮತ್ತು KPI ಗೆ ಜೋಡಣೆ",
    fixedLabel: "ಫೋಕಸ್ಡ್ ಪೋರ್ಟ್‌ಫೋಲಿಯೋ",
    takeaways: [
      { text: "ಕೆಲವು ನಿಜವಾದ ಆದ್ಯತೆಗಳು, ಆಸೆಗಳ ಪಟ್ಟಿ ಅಲ್ಲ", cue: "ಕೆಲವು ನಿಜವಾದ ಆದ್ಯತೆಗಳನ್ನು" },
      { text: "ಗುರಿ → ಪ್ರಾಜೆಕ್ಟ್ → KPI → ಒಬ್ಬ ಓನರ್", cue: "ಪ್ರತಿ ಗುರಿಯನ್ನು" },
      { text: "ಪ್ರಾಮಾಣಿಕ ರಿವ್ಯೂ: ನಂಬರ್‌ಗಳು ಚಲಿಸಬೇಕು", cue: "ಮತ್ತು ಪ್ರಾಮಾಣಿಕವಾಗಿ" },
    ],
    action: { text: "ನಿಮ್ಮ ಏರಿಯಾಗಾಗಿ ಒಂದು ಉದ್ದೇಶ ಬರೆಯಿರಿ, ಫಲಿತಾಂಶದ ರೂಪದಲ್ಲಿ, ಕೆಲಸದ ರೂಪದಲ್ಲಿ ಅಲ್ಲ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "Y", title: "Yamazumi", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_KN_DURATION = PLAN.total;

export const XMatrixKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
