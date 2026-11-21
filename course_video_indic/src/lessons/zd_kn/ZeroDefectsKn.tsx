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
import words from "../../captions/zd_kn/words.json";

// Kannada version of ZeroDefectsKn (same design and polish as the English lesson).
// All data comes from narration/zero_defects_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "ಡಿಫೆಕ್ಟ್ ತಡೆಯಿರಿ — ಕೇವಲ ಅವುಗಳನ್ನು ಪರಿಶೀಲಿಸಬೇಡಿ",
  outroLine: "ತಡೆಯಿರಿ. ಅಳೆಯಿರಿ. ಸುಧಾರಿಸಿ.",
  outroSub: "Zero Defects — ದಿನದ ಮ್ಯಾನೇಜ್‌ಮೆಂಟ್‌ನಲ್ಲಿ ಸೇರಿದೆ",
};

// Same polish as English ZeroDefects; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "ಫೋನ್‌ಗಳು ರೀವರ್ಕ್‌ಗಾಗಿ ಹಿಂದಿರುಗಿದವು",
    sub: "ಒಂದು ಕನೆಕ್ಟರ್, ತಪ್ಪಾಗಿ ಕೂತಿದೆ. ಅದು ಪ್ರತಿ ವಿಶುವಲ್ ಚೆಕ್‌ನಲ್ಲೂ ಪಾಸ್ ಆಯಿತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ತಪ್ಪಾಗಿ ಕೂತ ಕನೆಕ್ಟರ್‌ನಿಂದ ಚಾರ್ಜಿಂಗ್ ಫೇಲ್ಯೂರ್", before: 1200, after: 200,
    unit: "ಫೇಲ್ ಫೋನ್, 40,000 ರಲ್ಲಿ", fixedLabel: "ಮರುಕಳಿಸುವುದು ಕಷ್ಟ: 83% ಕಡಿಮೆ",
    takeaways: [
      { text: "ಡಿಫೆಕ್ಟ್ ತಡೆಯಿರಿ, ಕೇವಲ ಪರಿಶೀಲನೆ ಅಲ್ಲ", cue: "ಡಿಫೆಕ್ಟ್‌ಗಳನ್ನು ತಡೆಯಿರಿ" },
      { text: "ಸ್ಪಷ್ಟ ವ್ಯಾಖ್ಯಾನಗಳ ಜೊತೆ ಪ್ರಾಮಾಣಿಕವಾಗಿ ಅಳೆಯಿರಿ", cue: "ಸ್ಪಷ್ಟ ವ್ಯಾಖ್ಯಾನಗಳ ಜೊತೆ" },
      { text: "ಸಿಸ್ಟಮ್ ಸರಿಪಡಿಸಿ, ವ್ಯಕ್ತಿಯನ್ನಲ್ಲ", cue: "ಮತ್ತು ಏನಾದರೂ ಫೇಲ್" },
    ],
    action: { text: "ಪದೇ ಪದೇ ಮರಳುವ ಒಂದು ಡಿಫೆಕ್ಟ್ ಆರಿಸಿ, ಮತ್ತು ಅದನ್ನು ಅಸಾಧ್ಯವಾಗಿ ಹೇಗೆ ಮಾಡುವುದು ಎಂದು ಕೇಳಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "Z", title: "Zero Defects", kicker: "ಪಾಠ ಮುಗಿಸಿದ್ದಕ್ಕೆ", cue: "ಈಗ ಹೋಗಿ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_KN_DURATION = PLAN.total;

export const ZeroDefectsKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
