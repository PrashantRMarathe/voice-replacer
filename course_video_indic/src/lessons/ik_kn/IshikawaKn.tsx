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
import words from "../../captions/ik_kn/words.json";

// Kannada version of IshikawaKn (same design and polish as the English lesson).
// All data comes from narration/ishikawa_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "ಫಿಶ್ಬೋನ್ನಿಂದ ಮುಕ್ತವಾಗಿ ಹುಡುಕಿ, ನಂತರ ಕಾರಣ ಸಾಬೀತುಪಡಿಸಿ",
  outroLine: "ಮುಕ್ತವಾಗಿ ಹುಡುಕಿ. ನಿಖರವಾಗಿ ಸಾಬೀತುಪಡಿಸಿ.",
  outroSub: "Ishikawa — ಪರೀಕ್ಷಿಸುವವರೆಗೆ ಪ್ರತಿ ಮೂಳೆ ಒಂದು ಊಹೆ",
};

// Same polish as English Ishikawa; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "ಪ್ರತಿ 1,000 ಸ್ವಿಚ್ಗೆ ಪೋರ್ಟ್ ಟೆಸ್ಟ್ನಲ್ಲಿ ಫೇಲ್",
    sub: "5 ರಿಂದ ಏರಿಕೆ. ಮೀಟಿಂಗ್ನ ಉತ್ತರ: ಹೊಸ ಟೆಸ್ಟರ್ ಖರೀದಿಸಿ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಸ್ವಿಚ್ ಲೈನಿನಲ್ಲಿ ಪೋರ್ಟ್-ಲಿಂಕ್ ಫೇಲ್ಯೂರ್ಗಳು", before: 32, after: 4, unit: "ಪ್ರತಿ 1,000 ಸ್ವಿಚ್ಗೆ",
    fixedLabel: "ಎರಡೂ ಕಾರಣಗಳು ಸರಿಯಾದವು",
    takeaways: [
      { text: "ತಲೆಯಲ್ಲಿ ಹರಿತವಾದ, ಅಳೆಯಬಹುದಾದ ಪರಿಣಾಮ", cue: "ತಲೆಯಲ್ಲಿ ಒಂದು" },
      { text: "6M ನಲ್ಲಿ ಮುಕ್ತವಾಗಿ ಹುಡುಕಿ, ದೂಷಣೆ ಇಲ್ಲದೆ", cue: "ಆರು ಎಂಗಳಲ್ಲಿ" },
      { text: "ಸಾಬೀತಾಗುವವರೆಗೆ ಪ್ರತಿ ಮೂಳೆ ಊಹೆ", cue: "ಮತ್ತು ಪ್ರತಿ ಮೂಳೆಯನ್ನು" },
    ],
    action: { text: "ಮತ್ತೆ ಮತ್ತೆ ಬರುವ ಒಂದು ಸಮಸ್ಯೆಯ ಫಿಶ್ಬೋನ್ ಮಾಡಿ, ಮತ್ತು ಪರೀಕ್ಷಿಸಲು ಮೂರು ಕಾರಣಗಳನ್ನು ಆರಿಸಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "J", title: "Jidoka", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_KN_DURATION = PLAN.total;

export const IshikawaKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
