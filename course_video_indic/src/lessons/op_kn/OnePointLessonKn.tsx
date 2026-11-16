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
import words from "../../captions/op_kn/words.json";

// Kannada version of OnePointLessonKn (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "ಒಂದು ವಿಷಯ. ಒಂದು ಸ್ಪಷ್ಟ ಪಾಯಿಂಟ್. ಒಂದು ಉತ್ತಮ ಕೆಲಸ.",
  outroLine: "ಸುಲಭ. ವಿಶುವಲ್. ಸರಿ.",
  outroSub: "One Point Lesson — ಒಂದು ಪಾಯಿಂಟ್ ಅನ್ನು ಚೆನ್ನಾಗಿ ಕಲಿಸಿ",
};

// Same polish as English OnePointLesson; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "ಕನೆಕ್ಟರ್ ತಲೆಕೆಳಗಾಗಿ ಹಾಕಲಾಯಿತು, ಮತ್ತು ಮುರಿಯಿತು",
    sub: "ಡೇ ಶಿಫ್ಟ್ಗೆ ವಿಧಾನ ಗೊತ್ತಿತ್ತು. ಯಾರೂ ಹೇಳಿರಲಿಲ್ಲ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ನೈಟ್ ಶಿಫ್ಟ್ನಲ್ಲಿ ಮುರಿಯುವ ಕನೆಕ್ಟರ್ಗಳು", before: 14, after: 1, unit: "ವಾರಕ್ಕೆ ಮುರಿದ ಕನೆಕ್ಟರ್",
    takeaways: [
      { text: "ಒಂದು ವಿಷಯ, ಒಂದು ಪಾಯಿಂಟ್, ಒಂದು ಬಲಿಷ್ಠ ವಿಶುವಲ್", cue: "ಒಂದು ವಿಷಯ" },
      { text: "Gemba ಸ್ಥಳದಲ್ಲಿ ಕಲಿಸಿ, ನಂತರ ಕೆಲಸ ನೋಡಿ", cue: "ಇದನ್ನು Gemba ಸ್ಥಳದಲ್ಲಿ" },
      { text: "ಇದನ್ನು ಈಗಿನ ಸ್ಟ್ಯಾಂಡರ್ಡ್ಗೆ ಹೊಂದಿಸಿ ಇಡಿ", cue: "ಮತ್ತು ಇದನ್ನು ಕಂಟ್ರೋಲ್ನಲ್ಲಿ" },
    ],
    action: { text: "ಪದೇ ಪದೇ ಆಗುವ ಒಂದು ತಪ್ಪನ್ನು ಆರಿಸಿ, ಮತ್ತು ಅದಕ್ಕಾಗಿ ಒಂದು One Point Lesson ಡ್ರಾಫ್ಟ್ ಮಾಡಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "P", title: "Poka Yoke", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_KN_DURATION = PLAN.total;

export const OnePointLessonKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
