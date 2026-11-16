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
import words from "../../captions/gb_kn/words.json";

// Kannada version of GembaKn (same design and polish as the English lesson).
// All data comes from narration/gemba_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "ನಿಜವಾದ ಸ್ಥಳ, ನಿಜವಾದ ವಸ್ತು, ನಿಜವಾದ ಸತ್ಯಾಂಶ",
  outroLine: "ಹೋಗಿ. ನೋಡಿ. ಖಚಿತಪಡಿಸಿ.",
  outroSub: "Gemba, Genbutsu, Genjitsu — ನಿರ್ಧಾರಕ್ಕಿಂತ ಮೊದಲು ಸತ್ಯಾಂಶ",
};

// Same polish as English Gemba; cues are phrases from the Kannada intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× ಇಯರ್ಬಡ್ ಫೇಲ್ಯೂರ್, ಶಿಫ್ಟ್ B ಯಲ್ಲಿ",
    sub: "ಪ್ಲಾನ್: ಶಿಫ್ಟ್ B ಗೆ ಮತ್ತೆ ತರಬೇತಿ. ಯಾರೂ ಒಂದು ಫೇಲ್ ಇಯರ್ಬಡ್ ಕೂಡ ನೋಡಿರಲಿಲ್ಲ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಆಡಿಯೋ ಟೆಸ್ಟ್ನಲ್ಲಿ ಫೇಲ್ ಆಗುವ ಇಯರ್ಬಡ್ಗಳು", before: 20, after: 8, unit: "ಪ್ರತಿ 1,000 ಇಯರ್ಬಡ್ಗೆ ಫೇಲ್ಯೂರ್",
    fixedLabel: "ಕಾರಣದಲ್ಲೇ ಸರಿಪಡಿಸಲಾಯಿತು",
    takeaways: [
      { text: "ನಿಜವಾದ ಸ್ಥಳಕ್ಕೆ ಹೋಗಿ; ನಿಜವಾದ ಸೈಕಲ್ ನೋಡಿ", cue: "ನಿಜವಾದ ಸ್ಥಳಕ್ಕೆ ಹೋಗಿ" },
      { text: "ನಿಜವಾದ ವಸ್ತು ಕೈಯಲ್ಲಿ ಹಿಡಿಯಿರಿ; ಒಳ್ಳೆಯದರ ಜೊತೆ ಹೋಲಿಸಿ", cue: "ನಿಜವಾದ ವಸ್ತುವನ್ನು ಕೈಯಲ್ಲಿ" },
      { text: "ನಿಜವಾದ ಸತ್ಯಾಂಶ ಪರೀಕ್ಷಿಸಿ, ಛೇದದ ಜೊತೆ", cue: "ಮತ್ತು ನಿಜವಾದ ಸತ್ಯಾಂಶಗಳನ್ನು" },
    ],
    action: { text: "ಮತ್ತೆ ಮತ್ತೆ ಬರುವ ಒಂದು ಸಮಸ್ಯೆ ತೆಗೆದುಕೊಳ್ಳಿ, ಮತ್ತು ಮೂವತ್ತು ನಿಮಿಷದ 3G ವಿಸಿಟ್ ಮಾಡಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "H", title: "Hancho", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_KN_DURATION = PLAN.total;

export const GembaKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
