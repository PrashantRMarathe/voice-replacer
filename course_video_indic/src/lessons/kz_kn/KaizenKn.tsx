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
import words from "../../captions/kz_kn/words.json";

// Kannada version of KaizenKn (same design and polish as the English lesson).
// All data comes from narration/kaizen_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "ಚಿಕ್ಕ ಬದಲಾವಣೆಗಳು, ಪ್ರತಿದಿನ, ಕೆಲಸ ಮಾಡುವ ಜನರಿಂದ",
  outroLine: "ನೋಡಿ. ಚಿಕ್ಕದಾಗಿ ಪ್ರಯತ್ನಿಸಿ. ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಮಾಡಿ. ಪುನರಾವರ್ತಿಸಿ.",
  outroSub: "Kaizen — ಇಂದಿನ ಅತ್ಯುತ್ತಮ ವಿಧಾನ, ನಾಳೆಯ ಬೇಸ್ಲೈನ್",
};

// Same polish as English Kaizen; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "ಬಾರಿ ಪ್ರತಿ ಮಾನಿಟರ್ ತಿರುಗಿಸಲಾಗುತ್ತಿತ್ತು",
    sub: "ಮುಖ ಕೆಳಗೆ, ನಂತರ ಮುಖ ಮೇಲೆ. ಯಾವಾಗಲೂ ಹೀಗೆಯೇ ನಡೆದುಕೊಂಡು ಬಂದಿತ್ತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಮಾನಿಟರ್ ತಿರುಗಿಸುವುದರಿಂದ ಪ್ಯಾನಲ್ ಗೀರು", before: 15, after: 3, unit: "ಪ್ರತಿ 1,000 ಮಾನಿಟರ್ಗೆ ಗೀರು",
    fixedLabel: "90 ದಿನದಲ್ಲೂ ಉಳಿಯಿತು",
    takeaways: [
      { text: "Kaizen ದಿನನಿತ್ಯದ ಅಭ್ಯಾಸ", cue: "Kaizen ದಿನನಿತ್ಯದ" },
      { text: "ಚಿಕ್ಕದಾಗಿ ಪರೀಕ್ಷಿಸಿ; ಬೇರೇನೂ ಕೆಡಲಿಲ್ಲ ಎಂದು ಪರಿಶೀಲಿಸಿ", cue: "ಸಣ್ಣ ಮಟ್ಟದಲ್ಲಿ" },
      { text: "ಪ್ರತಿ ಲಾಭವನ್ನು ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಮಾಡಿ", cue: "ಮತ್ತು ಪ್ರತಿ ಲಾಭವನ್ನು" },
    ],
    action: { text: "ಒಬ್ಬ ಆಪರೇಟರ್ ಅನ್ನು ಅವರ ಕೆಲಸದಲ್ಲಿ ಏನು ಕಷ್ಟ ಎಂದು ಕೇಳಿ, ಮತ್ತು ಒಂದು ಚಿಕ್ಕ ಪರಿಹಾರ ಪರೀಕ್ಷಿಸಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "L", title: "Low Cost Automation", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_KN_DURATION = PLAN.total;

export const KaizenKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
