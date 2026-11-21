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
import words from "../../captions/hc_kn/words.json";

// Kannada version of HanchoKn (same design and polish as the English lesson).
// All data comes from narration/hancho_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "ಶಾಪ್-ಫ್ಲೋರ್ ಲೀಡರ್ಶಿಪ್, ಪ್ರತಿ ಶಿಫ್ಟ್ನ ಪ್ರತಿ ಗಂಟೆ",
  outroLine: "Gemba ಸ್ಥಳದಲ್ಲಿ ಲೀಡ್ ಮಾಡಿ. ಜನರನ್ನು ಸಿದ್ಧಪಡಿಸಿ.",
  outroSub: "Hancho — ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಮರಳಿ ತನ್ನಿ, ಪ್ರತಿದಿನ ಸುಧಾರಿಸಿ",
};

// Same polish as English Hancho; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "ಪ್ರತಿ ಗಂಟೆ TV ಕಡಿಮೆ, ಇಡೀ ಒಂದು ಶಿಫ್ಟ್ವರೆಗೆ",
    sub: "ಮರುದಿನ ಬೆಳಗ್ಗೆಯ ವರದಿಯವರೆಗೆ ಯಾರಿಗೂ ಗೊತ್ತಾಗಲಿಲ್ಲ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಮಾಡೆಲ್ ಚೇಂಜ್ ನಂತರ ಔಟ್ಪುಟ್ ಗ್ಯಾಪ್", before: 98, after: 120, unit: "ಗಂಟೆಗೆ TV",
    fixedLabel: "ಅದೇ ಶಿಫ್ಟ್ನಲ್ಲಿ ಮರಳಿ",
    takeaways: [
      { text: "Gemba ಸ್ಥಳದಿಂದ ಲೀಡ್ ಮಾಡಿ: ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಎದುರು ನಿಜಸ್ಥಿತಿ", cue: "Gemba ಸ್ಥಳದಿಂದ ಲೀಡ್" },
      { text: "ಗ್ಯಾಪ್ ಪ್ರತಿ ಗಂಟೆ ತೋರಿಸಿ; ಅದೇ ಶಿಫ್ಟ್ನಲ್ಲಿ ಕ್ರಮ", cue: "ಪ್ರತಿ ಗ್ಯಾಪ್ ಅನ್ನು" },
      { text: "ಜನರನ್ನು ಸಿದ್ಧಪಡಿಸಿ, ಲೈನ್ ನಿಮ್ಮ ಮೇಲೆ ನಿಲ್ಲದಂತೆ", cue: "ಮತ್ತು ನಿಮ್ಮ ಜನರನ್ನು" },
    ],
    action: { text: "ಒಂದು ಶಿಫ್ಟ್ಗಾಗಿ ನಿಮ್ಮ ಲೀಡರ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ವರ್ಕ್ ಬರೆಯಿರಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_KN_DURATION = PLAN.total;

export const HanchoKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
