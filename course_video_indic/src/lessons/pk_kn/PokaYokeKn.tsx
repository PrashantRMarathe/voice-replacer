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
import words from "../../captions/pk_kn/words.json";

// Kannada version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "ತಪ್ಪು ಕೆಲಸವನ್ನು ಅಸಾಧ್ಯವಾಗಿಸಿ",
  outroLine: "ತೆಗೆದುಹಾಕಿ. ತಡೆಯಿರಿ. ಹಿಡಿಯಿರಿ.",
  outroSub: "Poka Yoke — ಕ್ವಾಲಿಟಿಯನ್ನು ನೆನಪಿನ ಅವಲಂಬನೆಯಿಂದ ಮುಕ್ತಗೊಳಿಸಿ",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_KN_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "ಒಂದು ಸ್ಕ್ರೂ ಇಲ್ಲದೆ ರವಾನೆಯಾದ ರೆಕಾರ್ಡರ್ಗಳು",
    sub: "ಆಪರೇಟರ್ ನುರಿತವರು, ಜಾಗರೂಕರು. ಕೇವಲ ಮನುಷ್ಯರು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಸ್ಕ್ರೂ ಕಾಣೆಯಾಗಿ ರವಾನೆಯಾದ ರೆಕಾರ್ಡರ್ಗಳು", before: 18, after: 1, unit: "10,000 ಯೂನಿಟ್ಗೆ",
    takeaways: [
      { text: "ತಪ್ಪುಗಳನ್ನು ಊಹಿಸಬಹುದು: ಡಿಸೈನ್ ಮೂಲಕ ತೆಗೆದುಹಾಕಿ", cue: "ತಪ್ಪುಗಳನ್ನು ಮೊದಲೇ" },
      { text: "ಮೊದಲು ತಡೆಯಿರಿ, ನಂತರ ಹಿಡಿಯಿರಿ, ನಂತರ ಎಚ್ಚರಿಸಿ", cue: "ಎಚ್ಚರಿಕೆಗಿಂತ ಹಿಡಿಯುವುದು" },
      { text: "ಪ್ರತಿ ಡಿವೈಸ್ ಅನ್ನು ದೋಷಯುಕ್ತ ಸ್ಯಾಂಪಲ್ನಿಂದ ಪರೀಕ್ಷಿಸಿ", cue: "ಮತ್ತು ಪ್ರತಿ ಡಿವೈಸ್" },
    ],
    action: { text: "ನೆನಪಿನ ಮೇಲೆ ನಿಂತ ಒಂದು ಚೆಕ್ ಹುಡುಕಿ, ಮತ್ತು ಅದಕ್ಕೆ Poka Yoke ಸ್ಕೆಚ್ ಮಾಡಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "Q", title: "QRQC", cue: "ಮುಂದೆ, ನೀವು QRQC" },
  },
};

export const PokaYokeKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
