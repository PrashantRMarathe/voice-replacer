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
import words from "../../captions/qr_kn/words.json";

// Kannada version of QrqcKn (same design and polish as the English lesson).
// All data comes from narration/qrqc_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "ನಿಮಿಷಗಳಲ್ಲಿ ಕ್ರಮ — ಸಾಕ್ಷ್ಯದ ಜೊತೆ ಮುಚ್ಚುವುದು",
  outroLine: "ಹಿಡಿಯಿರಿ. ತಡೆಯಿರಿ. ಸಾಬೀತುಪಡಿಸಿ.",
  outroSub: "QRQC — ವೇಗದ ರೆಸ್ಪಾನ್ಸ್, ನಿಜವಾದ ಸಾಕ್ಷ್ಯ",
};

// Same polish as English QRQC; cues are phrases from the Kannada intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "ಮಧ್ಯಾಹ್ನದವರೆಗೆ ಫೋಕಸ್ ಟೆಸ್ಟ್ನಲ್ಲಿ ಫೇಲ್ ಆದ ಕ್ಯಾಮೆರಾ",
    sub: "ಯಾರೋ ಟೆಸ್ಟರ್ ರೀಸೆಟ್ ಮಾಡಿದರು, ಮತ್ತು ಲೈನ್ ನಡೆಯುತ್ತಲೇ ಇತ್ತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ವೇರ್ಹೌಸ್ ಕಡೆ ಹೋಗುತ್ತಿರುವ ಅನುಮಾನದ ಕ್ಯಾಮೆರಾಗಳು", before: 2000, after: 0, unit: "ಲೆಕ್ಕವಿಲ್ಲದ ಅನುಮಾನದ ಕ್ಯಾಮೆರಾ",
    takeaways: [
      { text: "ವೇಗವಾಗಿ ಕ್ರಮ, ಆದರೆ ಸಾಕ್ಷ್ಯದ ಜೊತೆ", cue: "ವೇಗವಾಗಿ ಕ್ರಮ" },
      { text: "ಮೊದಲು ಕಂಟೇನ್ಮೆಂಟ್, ಪ್ರತಿ ಯೂನಿಟ್ನ ಲೆಕ್ಕ", cue: "ಮೊದಲು ಕಂಟೇನ್ಮೆಂಟ್" },
      { text: "ಪರಿಹಾರ ಸಾಬೀತಾದಾಗ ಮಾತ್ರ ಮುಚ್ಚಿ", cue: "ಮತ್ತು ಯಾವುದೇ ಸಮಸ್ಯೆಯನ್ನು" },
    ],
    action: { text: "ಯಾವುದೇ ಒಂದು ಗಂಭೀರ ಡಿಫೆಕ್ಟ್ಗಾಗಿ ನಿಮ್ಮ ರೆಸ್ಪಾನ್ಸ್ ಪ್ಲಾನ್ನ ಮೊದಲ 30 ನಿಮಿಷ ಬರೆಯಿರಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_KN_DURATION = PLAN.total;

export const QrqcKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
