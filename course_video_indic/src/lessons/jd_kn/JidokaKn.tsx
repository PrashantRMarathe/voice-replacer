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
import words from "../../captions/jd_kn/words.json";

// Kannada version of JidokaKn (same design and polish as the English lesson).
// All data comes from narration/jidoka_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "ಮಾನವ ಸ್ಪರ್ಶದ ಆಟೋಮೇಷನ್",
  outroLine: "ನೋಡಿ. ನಿಲ್ಲಿಸಿ. ಬಗೆಹರಿಸಿ.",
  outroSub: "Jidoka — ಯಾವುದೇ ಡಿಫೆಕ್ಟ್ ಮುಂದೆ ಇಲ್ಲ, ಯಾವುದೇ ಅಸಹಜತೆ ಮುಚ್ಚಿಟ್ಟಿಲ್ಲ",
};

// Same polish as English Jidoka; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "ಪೇಷೆಂಟ್ ಮಾನಿಟರ್ಗಳ ಮೇಲೆ ತೆಳು ಸೀಲ್",
    sub: "ಡಿಸ್ಪೆನ್ಸರ್ ರಾತ್ರಿಯಿಡೀ ಚೆನ್ನಾಗಿ ನಡೆಯಿತು. ಅದರ ನಾಜಲ್ ಅರ್ಧ ಮುಚ್ಚಿಹೋಗಿತ್ತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಮುಚ್ಚಿದ ಅಡ್ಹೆಸಿವ್ ನಾಜಲ್ನಿಂದ ತೆಳು ಸೀಲ್", before: 140, after: 1, unit: "ಮಾನಿಟರ್ಗಳ ಮೇಲೆ ಪರಿಣಾಮ, ಪ್ರತಿ ನಾಜಲ್ ಸಮಸ್ಯೆಗೆ",
    fixedLabel: "ಮೂಲದಲ್ಲೇ ಸಿಕ್ಕಿತು",
    takeaways: [
      { text: "ಮೊದಲು ಸಾಮಾನ್ಯ ನಿರ್ಧರಿಸಿ", cue: "ಮೊದಲು ಸಾಮಾನ್ಯವನ್ನು" },
      { text: "ಹಿಡಿಯಿರಿ, ನಿಲ್ಲಿಸಿ, ಕಂಟೇನ್ ಮಾಡಿ: ಯಾವುದೇ ಡಿಫೆಕ್ಟ್ ಮುಂದೆ ಇಲ್ಲ", cue: "ಮೂಲದಲ್ಲೇ ಹಿಡಿಯಿರಿ" },
      { text: "ಪ್ರತಿ ನಿಲುಗಡೆ ಒಂದು ಪಾಠ: ರೂಟ್ ಕಾಸ್ ಸರಿಪಡಿಸಿ", cue: "ಮತ್ತು ಪ್ರತಿ ನಿಲುಗಡೆಯನ್ನು" },
    ],
    action: { text: "ಒಂದು ಆಟೋಮ್ಯಾಟಿಕ್ ಪ್ರೋಸೆಸ್ ಆರಿಸಿ, ಮತ್ತು ಅದು ಯಾವುದಕ್ಕೆ ನಿಲ್ಲಬೇಕು ಎಂದು ಬರೆಯಿರಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "K", title: "Kaizen", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_KN_DURATION = PLAN.total;

export const JidokaKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
