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
import words from "../../captions/vs_kn/words.json";

// Kannada version of ValueStreamMappingKn (same design and polish as the English lesson).
// All data comes from narration/value_stream_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "ಆರ್ಡರ್ನಿಂದ ಡೆಲಿವರಿವರೆಗೆ, ಇಡೀ ಫ್ಲೋ ನೋಡಿ",
  outroLine: "ನೋಡಿ. ಅಳೆಯಿರಿ. ಫ್ಲೋ ಕಟ್ಟಿ.",
  outroSub: "Value Stream Mapping — ಕಾಯುವಿಕೆ ಹುಡುಕಿ, ಫ್ಲೋ ಡಿಸೈನ್ ಮಾಡಿ",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "ನಿಮಿಷ, ಒಂದು ಸೆಟ್-ಟಾಪ್ ಬಾಕ್ಸ್ ತಯಾರಿಸಲು ಮತ್ತು ಟೆಸ್ಟ್ ಮಾಡಲು",
    sub: "ಆದರೂ ಗ್ರಾಹಕರನ್ನು ತಲುಪಲು ಸುಮಾರು ನಾಲ್ಕು ದಿನ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ನಿಮಿಷಗಳ ಕೆಲಸಕ್ಕೆ ದಿನಗಳ ಕಾಯುವಿಕೆ", before: 4200, after: 2100, unit: "ಮೂರು ಬಫರ್ಗಳಲ್ಲಿ ಕಾಯುತ್ತಿರುವ ಯೂನಿಟ್",
    fixedLabel: "ಫ್ಯೂಚರ್ ಸ್ಟೇಟ್: ಅರ್ಧ ಕಾಯುವಿಕೆ",
    takeaways: [
      { text: "ನಿಜವಾದ ಮೆಟೀರಿಯಲ್ + ಮಾಹಿತಿ ಫ್ಲೋವಿನ ನಕ್ಷೆ", cue: "ನಿಜವಾದ ಫ್ಲೋವಿನ ನಕ್ಷೆ" },
      { text: "ಲೀಡ್ ಟೈಮ್ ಕಾಯುವಿಕೆಯಲ್ಲಿ ಅಡಗಿದೆ, ಕೆಲಸದಲ್ಲಿ ಅಲ್ಲ", cue: "ನಿಮ್ಮ ಹೆಚ್ಚಿನ ಲೀಡ್" },
      { text: "ಸ್ಟಾಕ್ ಕಡಿಮೆ ಮಾಡುವ ಮೊದಲು ಫ್ಯೂಚರ್ ಸ್ಟೇಟ್ ಸಾಬೀತುಪಡಿಸಿ", cue: "ಮತ್ತು ಯಾವುದೇ ಸ್ಟಾಕ್" },
    ],
    action: { text: "ಒಂದು ಪ್ರಾಡಕ್ಟ್ ಫ್ಯಾಮಿಲಿಯ ಜೊತೆ ಡಿಸ್ಪ್ಯಾಚ್ನಿಂದ ಹಿಮ್ಮುಖವಾಗಿ ನಡೆಯಿರಿ, ಮತ್ತು ಪ್ರತಿ ರಾಶಿ ಎಣಿಸಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_KN_DURATION = PLAN.total;

export const ValueStreamMappingKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
