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
import words from "../../captions/sk_kn/words.json";

// Kannada version of SkillMatrixKn (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "ಯಾರು ನಿಜವಾಗಿ ಯಾವ ಕೆಲಸ ಮಾಡಬಲ್ಲರು — ಮತ್ತು ಗ್ಯಾಪ್ಗಳು ಎಲ್ಲಿವೆ",
  outroLine: "ಪರಿಶೀಲಿಸಿ. ತರಬೇತಿ ಕೊಡಿ. ಕವರ್ ಮಾಡಿ.",
  outroSub: "Skill Matrix — ಸಾಮರ್ಥ್ಯದ ಜೀವಂತ ಕಂಟ್ರೋಲ್",
};

// Same polish as English SkillMatrix; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "ವ್ಯಕ್ತಿ ಲೆನ್ಸ್ ಫೋಕಸ್ ಸೆಟ್ ಮಾಡಬಲ್ಲರು",
    sub: "ಬಾಲಾ ಅನಾರೋಗ್ಯದಲ್ಲಿದ್ದರು. ಹತ್ತು ಗಂಟೆಯ ಹೊತ್ತಿಗೆ, ಇಡೀ ಸೆಲ್ ನಿಂತಿತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಒಬ್ಬರೇ ಲೆನ್ಸ್ ಫೋಕಸ್ ಎಕ್ಸ್ಪರ್ಟ್, ಮತ್ತು ಅವರು ಅನಾರೋಗ್ಯದಲ್ಲಿ", before: 1, after: 2, unit: "ಅರ್ಹ ಲೆನ್ಸ್ ಫೋಕಸ್ ಎಕ್ಸ್ಪರ್ಟ್ಗಳು",
    takeaways: [
      { text: "ಸಾಬೀತಾದ ಸಾಮರ್ಥ್ಯ, ಹಾಜರಿ ಅಲ್ಲ", cue: "ಸ್ಕಿಲ್ ಮ್ಯಾಟ್ರಿಕ್ಸ್ ಸಾಬೀತಾದ" },
      { text: "ಪ್ರತಿ ಶಿಫ್ಟ್ ಅರ್ಹ ಬ್ಯಾಕಪ್ ಎಣಿಸಿ", cue: "ಪ್ರತಿ ಮುಖ್ಯ ಕೆಲಸಕ್ಕೆ" },
      { text: "ಇದನ್ನು ಜೀವಂತವಾಗಿಡಿ, ಸಾಕ್ಷ್ಯದ ಜೊತೆ", cue: "ಮತ್ತು ಇದನ್ನು ಜೀವಂತವಾಗಿಡಿ" },
    ],
    action: { text: "ನಿಮ್ಮ ಮೂರು ಅತ್ಯಂತ ಮುಖ್ಯ ಸ್ಟೇಷನ್ಗಳನ್ನು ಬರೆಯಿರಿ, ಮತ್ತು ಪ್ರತಿಯೊಂದಕ್ಕೂ ಅರ್ಹ ಜನರನ್ನು ಎಣಿಸಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "T", title: "TAKT Time", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_KN_DURATION = PLAN.total;

export const SkillMatrixKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
