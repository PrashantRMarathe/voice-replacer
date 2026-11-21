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
import words from "../../captions/mm_kn/words.json";

// Kannada version of MudaMuraMuriKn (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "ವೇಸ್ಟ್, ಅಸಮಾನತೆ ಮತ್ತು ಅತಿಯಾದ ಹೊರೆ — ಮೂರನ್ನೂ ಸುಧಾರಿಸಿ",
  outroLine: "ಲೆವೆಲ್ ಮಾಡಿ. ರಕ್ಷಿಸಿ. ತೆಗೆಯಿರಿ.",
  outroSub: "3M — ಸ್ಥಿರ ಫ್ಲೋ, ವೇಗದ ಜನರಲ್ಲ",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "ಕ್ಯಾಮೆರಾ ಹಿಂದೆ, ಶಿಫ್ಟ್ ಮುಗಿಯುವ ಒಂದು ಗಂಟೆ ಮೊದಲು",
    sub: "ಎಲ್ಲರೂ ಓಡುತ್ತಿದ್ದಾರೆ. ಟೆಸ್ಟ್ನಲ್ಲಿ ತಪ್ಪುಗಳು ರಾಶಿಯಾಗುತ್ತಿವೆ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಸಂಜಯ್ ಅವರ ಲೈನ್ ಪ್ರತಿದಿನ ತಡವಾಗಿ ನಡೆಯುತ್ತಿತ್ತು", before: 150, after: 0, unit: "ದಿನಕ್ಕೆ ಓವರ್ಟೈಮ್ ನಿಮಿಷ",
    takeaways: [
      { text: "Muda ವೇಸ್ಟ್, Mura ಅಸಮಾನತೆ, Muri ಅತಿಯಾದ ಹೊರೆ", cue: "Muda ಎಂದರೆ ವೇಸ್ಟ್" },
      { text: "ಇವು ಒಂದನ್ನೊಂದು ಹೆಚ್ಚಿಸುತ್ತವೆ: ಒಟ್ಟಿಗೆ ಸುಧಾರಿಸಿ", cue: "ಇವು ಒಂದನ್ನೊಂದು" },
      { text: "ಸ್ಥಿರ ಫ್ಲೋ, ವೇಗದ ಜನರಲ್ಲ", cue: "ಮತ್ತು ಗುರಿ" },
    ],
    action: { text: "ಒಂದು ಪ್ರಾಡಕ್ಟ್ ಜೊತೆ ನಿಮ್ಮ ಲೈನಿನಲ್ಲಿ ನಡೆಯಿರಿ, ಮತ್ತು ಪ್ರತಿ M ನ ಒಂದು ಉದಾಹರಣೆಗೆ ಟ್ಯಾಗ್ ಹಾಕಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "N", title: "Next Inspection", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_KN_DURATION = PLAN.total;

export const MudaMuraMuriKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
