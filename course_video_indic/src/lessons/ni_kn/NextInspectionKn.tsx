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
import words from "../../captions/ni_kn/words.json";

// Kannada version of NextInspectionKn (same design and polish as the English lesson).
// All data comes from narration/next_inspection_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "ಮುಂದಿನ ಪ್ರೋಸೆಸ್ ನನ್ನ ಗ್ರಾಹಕ",
  outroLine: "ಮಾಡಬೇಡಿ. ಕಳುಹಿಸಬೇಡಿ. ಸ್ವೀಕರಿಸಬೇಡಿ.",
  outroSub: "Next Inspection — ಮುಂದಿನ ಪ್ರೋಸೆಸ್ ಅನ್ನು ರಕ್ಷಿಸಿ",
};

// Same polish as English NextInspection; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "ಸಡಿಲ ಕನೆಕ್ಟರ್, ಸ್ಟೇಷನ್ ಮೂರರಲ್ಲಿ",
    sub: "ಯಾರೂ ಗಮನಿಸಲಿಲ್ಲ. ನಂತರ ಒಬ್ಬ ಗ್ರಾಹಕರು ಬಾಕ್ಸ್ ತೆರೆದರು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಮುಂದಿನ ಸ್ಟೇಷನ್ವರೆಗೆ ಹೊರಹೋಗುವ ಡಿಫೆಕ್ಟ್ಗಳು", before: 18, after: 3, unit: "ಪ್ರತಿ ವಾರ ಎಸ್ಕೇಪ್",
    takeaways: [
      { text: "ಮಾಡಬೇಡಿ, ಕಳುಹಿಸಬೇಡಿ, ಸ್ವೀಕರಿಸಬೇಡಿ", cue: "ಡಿಫೆಕ್ಟ್ ಮಾಡಬೇಡಿ" },
      { text: "ಬೇಗ ಪರಿಶೀಲಿಸಿ, ವೇಗವಾಗಿ ಕ್ರಮ ತೆಗೆದುಕೊಳ್ಳಿ", cue: "ಮುಖ್ಯ ಪಾಯಿಂಟ್ಗಳನ್ನು ಸಾಧ್ಯವಾದಷ್ಟು" },
      { text: "ಕಂಟ್ರೋಲ್ ಮೇಲ್ಮುಖವಾಗಿ ಸರಿಸುತ್ತಿರಿ", cue: "ಮತ್ತು ನಿಮ್ಮ ಕಂಟ್ರೋಲ್ಗಳನ್ನು" },
    ],
    action: { text: "ಒಂದು ಹ್ಯಾಂಡ್ಆಫ್ ಆರಿಸಿ, ಮತ್ತು ಮುಂದಿನ ಪ್ರೋಸೆಸ್ಗೆ ಅದರಿಂದ ಏನು ಬೇಕು ಎಂದು ಬರೆಯಿರಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "O", title: "One Point Lesson", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_KN_DURATION = PLAN.total;

export const NextInspectionKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
