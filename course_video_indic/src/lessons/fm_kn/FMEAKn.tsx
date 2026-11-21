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
import words from "../../captions/fm_kn/words.json";

// Kannada version of FMEAKn (same design and polish as the English lesson).
// All data comes from narration/fmea_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "ಫೇಲ್ಯೂರ್ ಮೋಡ್ ಆ್ಯಂಡ್ ಇಫೆಕ್ಟ್ಸ್ ಅನಾಲಿಸಿಸ್: ಫೇಲ್ಯೂರ್ಗಿಂತ ಮೊದಲು ಯೋಚಿಸಿ",
  outroLine: "ಸರಪಳಿ ಕಟ್ಟಿ. ಸ್ಕೋರ್ ಕೊಡಿ. ತಡೆಯಿರಿ.",
  outroSub: "FMEA — ಒಂದು ಜೀವಂತ ಪ್ಲಾನ್, ಫಾರ್ಮ್ ಅಲ್ಲ",
};

// Same polish as English FMEA; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "ಔಟ್ಡೋರ್ ರೇಡಿಯೋಗಳು ನೀರು ತುಂಬಿಕೊಂಡು ಮರಳಿದವು",
    sub: "ಎರಡರಲ್ಲಿ ಗ್ಯಾಸ್ಕೆಟ್ ಕಾಣೆ, ನಾಲ್ಕರಲ್ಲಿ ಮಡಚಿದೆ. ಎಲ್ಲವೂ ಫೈನಲ್ ಇನ್ಸ್ಪೆಕ್ಷನ್ನಲ್ಲಿ ಪಾಸ್ ಆಗಿದ್ದವು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಔಟ್ಡೋರ್ 5G ರೇಡಿಯೋದಲ್ಲಿ ಗ್ಯಾಸ್ಕೆಟ್ ರಿಸ್ಕ್", before: 240, after: 32, unit: "ರಿಸ್ಕ್ ಪ್ರಯಾರಿಟಿ ನಂಬರ್",
    fixedLabel: "ರಿಸ್ಕ್ ಕಡಿಮೆ, ಟ್ರಯಲ್ನಲ್ಲಿ ಸಾಬೀತು",
    takeaways: [
      { text: "ಪರಿಣಾಮ → ಫೇಲ್ಯೂರ್ ಮೋಡ್ → ನಿಯಂತ್ರಿಸಬಹುದಾದ ಕಾರಣ", cue: "ಒಂದು ಸ್ಪಷ್ಟ ಸರಪಳಿ" },
      { text: "ಸಾಕ್ಷ್ಯದಿಂದ ಸ್ಕೋರ್; ನಂಬರ್ಗಿಂತ ತಿಳುವಳಿಕೆ ಮೇಲು", cue: "ಸಾಕ್ಷ್ಯದ ಜೊತೆ" },
      { text: "ಮೊದಲು ತಡೆಗಟ್ಟುವಿಕೆ, ಸಾಬೀತುಪಡಿಸಿ, ನಂತರ ಮತ್ತೆ ಸ್ಕೋರ್", cue: "ಮತ್ತು ತಡೆಗಟ್ಟುವಿಕೆಯನ್ನು" },
    ],
    action: { text: "ಒಂದು ಮುಖ್ಯ ಹೆಜ್ಜೆ ಆರಿಸಿ, ಮತ್ತು ನಿಮ್ಮ ತಂಡದ ಜೊತೆ ಅದರ ಫೇಲ್ಯೂರ್ ಸರಪಳಿ ಬರೆಯಿರಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "G", title: "Gemba", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_KN_DURATION = PLAN.total;

export const FMEAKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
