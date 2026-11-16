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
import words from "../../captions/ew_kn/words.json";

// Kannada version of EliminationOfWasteKn (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "ಗ್ರಾಹಕರು ಹಣ ಕೊಡದ್ದನ್ನು ತೆಗೆಯಿರಿ",
  outroLine: "ನೋಡಿ. ಕಾರಣ ತೆಗೆಯಿರಿ. ಸಾಬೀತುಪಡಿಸಿ.",
  outroSub: "Elimination of Waste — ಹೆಚ್ಚು ವ್ಯಾಲ್ಯೂ, ಕಡಿಮೆ ಶ್ರಮ",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "ಸೌಂಡ್ಬಾರ್ಗಳ ಪ್ರತಿ ತಿಂಗಳ ರೀವರ್ಕ್",
    sub: "ಪ್ರತಿಯೊಂದನ್ನು ಸರಿಪಡಿಸಲು ₹42. ಯಾರೂ ಇದನ್ನು ಎಂದಿಗೂ ಕೂಡಿಸಿರಲೇ ಇಲ್ಲ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಗುಂಯ್ಗುಡುವ ಸ್ಪೀಕರ್ ತಂತಿಯಿಂದ ರೀವರ್ಕ್ ಆಗುವ ಸೌಂಡ್ಬಾರ್ಗಳು", before: 1500, after: 300, unit: "ತಿಂಗಳಿಗೆ ರೀವರ್ಕ್", fixedLabel: "ರೀವರ್ಕ್ 80% ಕಡಿಮೆ",
    takeaways: [
      { text: "ವೇಸ್ಟ್: ಗ್ರಾಹಕರು ಹಣ ಕೊಡದ್ದು", cue: "ವೇಸ್ಟ್ ಎಂದರೆ ಗ್ರಾಹಕರು" },
      { text: "ಇದನ್ನು Gemba ಸ್ಥಳದಲ್ಲಿ ಸತ್ಯಾಂಶಗಳಿಂದ ಹುಡುಕಿ", cue: "ಇದನ್ನು Gemba ಸ್ಥಳದಲ್ಲಿ" },
      { text: "ಕಾರಣ ತೆಗೆಯಿರಿ, ಸಾಬೀತುಪಡಿಸಿ, ಉಳಿಸಿಕೊಳ್ಳಿ", cue: "ಮತ್ತು ಕಾರಣವನ್ನು ತೆಗೆಯಿರಿ" },
    ],
    action: { text: "ಮೂವತ್ತು ನಿಮಿಷ ನಿಮ್ಮ ಲೈನಿನಲ್ಲಿ ನಡೆಯಿರಿ, ಮತ್ತು ಮೂರು ವೇಸ್ಟ್ಗಳನ್ನು ಸತ್ಯಾಂಶಗಳ ರೂಪದಲ್ಲಿ ಬರೆಯಿರಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "F", title: "FMEA", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_KN_DURATION = PLAN.total;

export const EliminationOfWasteKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
