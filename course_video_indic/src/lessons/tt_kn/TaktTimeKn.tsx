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
import words from "../../captions/tt_kn/words.json";

// Kannada version of TaktTimeKn (same design and polish as the English lesson).
// All data comes from narration/takt_time_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "ನಿಮ್ಮ ಗ್ರಾಹಕರು ನಿರ್ಧರಿಸುವ ಹೃದಯಬಡಿತ",
  outroLine: "ಅಳೆಯಿರಿ. ಬ್ಯಾಲೆನ್ಸ್ ಮಾಡಿ. ಫ್ಲೋ ಕಟ್ಟಿ.",
  outroSub: "TAKT Time — ಗ್ರಾಹಕರ ವೇಗ",
};

// Same polish as English TaktTime; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "ಟೆಸ್ಟ್ಗಿಂತ ಮುಂದೆ ಮಾಡಿದ ಕ್ಯಾಮೆರಾ",
    sub: "ಪ್ರತಿ ಸ್ಟೇಷನ್ ಬ್ಯುಸಿ. ಆದರೂ ಟ್ರಕ್ ತಡವಾಗಿ ಹೊರಟಿತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಬ್ಯುಸಿ ಲೈನ್, ಆದರೂ ಟ್ರಕ್ ತಪ್ಪುತ್ತದೆ", before: 0, after: 10, unit: "ಸೆಕೆಂಡ್: ದಿನಕ್ಕೆ 7,200 ಕ್ಯಾಮೆರಾಗಳ ಬಡಿತ",
    fixedLabel: "ಎಲ್ಲರೂ ನಡೆಯುವ ವೇಗ",
    takeaways: [
      { text: "TAKT = ನೆಟ್ ಲಭ್ಯ ಸಮಯ ÷ ಡಿಮ್ಯಾಂಡ್", cue: "TAKT ಅಂದರೆ ನೆಟ್" },
      { text: "ಬೇಕಾದ ವೇಗ, ಸ್ಟೇಷನ್ನ ಸಮಯವಲ್ಲ", cue: "ಇದು ನಿಮಗೆ ಬೇಕಾದ ವೇಗ" },
      { text: "ನಿಜವಾದ ನಷ್ಟದಿಂದ ಪ್ಲಾನ್, ಸಿದ್ಧಾಂತದಿಂದ ಅಲ್ಲ", cue: "ಮತ್ತು ನಿಜವಾದ ನಷ್ಟಗಳ" },
    ],
    action: { text: "ಒಂದು ಲೈನಿನ TAKT ಲೆಕ್ಕ ಹಾಕಿ, ಮತ್ತು ಅದನ್ನು ನಿಮ್ಮ ಅತ್ಯಂತ ನಿಧಾನ ಸ್ಟೇಷನ್ ಜೊತೆ ಹೋಲಿಸಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "U", title: "Uniform Production", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_KN_DURATION = PLAN.total;

export const TaktTimeKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
