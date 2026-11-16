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
import words from "../../captions/dt_kn/words.json";

// Kannada version of DesignThinkingKn (same design and polish as the English lesson).
// All data comes from narration/design_thinking_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "ಸರಿಯಾದ ಸಮಸ್ಯೆ ಬಗೆಹರಿಸಿ, ಕೆಲಸ ಮಾಡುವವರ ಜೊತೆ",
  outroLine: "ನೋಡಿ. ವ್ಯಾಖ್ಯಾನಿಸಿ. ಸಣ್ಣದಾಗಿ ಪರೀಕ್ಷಿಸಿ.",
  outroSub: "Design Thinking — ಮೊದಲು ಜನರು, ಯಾವಾಗಲೂ ಸಾಕ್ಷ್ಯ",
};

// Same polish as English DesignThinking; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "ಪ್ರತಿ 1,000 ಪಂಪ್ಗಳಲ್ಲಿ ಲೇಬಲ್ ತಪ್ಪುಗಳು",
    sub: "ಮೊದಲ ಐಡಿಯಾ: ಒಂದು ದುಬಾರಿ ವೇಗದ ಪ್ರಿಂಟರ್. ಪ್ಯಾಕರ್ಗಳನ್ನು ಯಾರೂ ಕೇಳಿಯೇ ಇರಲಿಲ್ಲ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಇನ್ಫ್ಯೂಷನ್ ಪಂಪ್ ಪ್ಯಾಕಿಂಗ್ನಲ್ಲಿ ಲೇಬಲ್ ತಪ್ಪುಗಳು", before: 12, after: 2, unit: "ಪ್ರತಿ 1,000 ಪಂಪ್ಗೆ",
    takeaways: [
      { text: "ಜನರಿಂದ ಶುರು ಮಾಡಿ; ನಿರ್ಧಾರಕ್ಕಿಂತ ಮೊದಲು ನೋಡಿ", cue: "ಕೆಲಸ ಮಾಡುವ ಜನರಿಂದ" },
      { text: "ಅಗತ್ಯವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ, ಅದರಲ್ಲಿ ಪರಿಹಾರವಿಲ್ಲದೆ", cue: "ಅಗತ್ಯವನ್ನು ಅದರಲ್ಲಿ" },
      { text: "ಸಣ್ಣದಾಗಿ ಪರೀಕ್ಷಿಸಿ: ಫಲಿತಾಂಶ ಮತ್ತು ನಿಜವಾದ ಬಳಕೆ", cue: "ಮತ್ತು ಸಣ್ಣ ಮಟ್ಟದಲ್ಲಿ" },
    ],
    action: { text: "ಕಷ್ಟವಾದ ಒಂದು ಕೆಲಸದ ಹತ್ತು ಸೈಕಲ್ ನೋಡಿ, ಮತ್ತು ಅದನ್ನು ಮಾಡುವ ಮೂವರ ಜೊತೆ ಮಾತನಾಡಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "E", title: "Elimination of Waste", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_KN_DURATION = PLAN.total;

export const DesignThinkingKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
