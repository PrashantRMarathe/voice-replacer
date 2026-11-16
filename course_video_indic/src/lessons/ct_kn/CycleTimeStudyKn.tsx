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
import words from "../../captions/ct_kn/words.json";

// Kannada version of CycleTimeStudyKn (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "ನಿಜವಾದ ಕೆಲಸ ಅಳೆಯಿರಿ, ನಿಜವಾದ ಬಾಟಲ್ನೆಕ್ ಹುಡುಕಿ",
  outroLine: "ವ್ಯಾಖ್ಯಾನ. ಅಳತೆ. ವಿಧಾನದಲ್ಲಿ ಸುಧಾರಣೆ.",
  outroSub: "Cycle Time Study — ವೇಗಕ್ಕಿಂತ ಮೊದಲು ಸಾಕ್ಷ್ಯ",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "ಸೆಕೆಂಡ್: ಪ್ರತಿ ಸ್ಟೇಷನ್ ಸಾಕಷ್ಟು ವೇಗವಾಗಿ ಕಾಣುತ್ತಿತ್ತು",
    sub: "ಆದರೂ ಮಾನಿಟರ್ ಲೈನ್ ಶಿಫ್ಟ್ ನಂತರ ಶಿಫ್ಟ್ ಗಂಟೆಯ ಟಾರ್ಗೆಟ್ ತಪ್ಪಿಸುತ್ತಲೇ ಇತ್ತು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಡಿಸ್ಪ್ಲೇ-ಟೆಸ್ಟ್ ಸ್ಟೇಷನ್ TAKT ಗಿಂತ ನಿಧಾನ", before: 28, after: 23, unit: "ಪ್ರತಿ ಮಾನಿಟರ್ಗೆ ಸೆಕೆಂಡ್, ಸ್ಟೇಷನ್ C ಯಲ್ಲಿ", fixedLabel: "ಈಗ TAKT ಒಳಗೆ",
    takeaways: [
      { text: "ಮೊದಲು ಬೌಂಡರಿ ನಿರ್ಧರಿಸಿ", cue: "ಮೊದಲು ಬೌಂಡರಿ" },
      { text: "ಸರಾಸರಿ ಮಾತ್ರವಲ್ಲ, ಹರಡಿಕೆ ನೋಡಿ", cue: "ಸರಾಸರಿ ಮಾತ್ರವಲ್ಲ" },
      { text: "ವಿಧಾನ ಸರಿಪಡಿಸಿ, ಕ್ವಾಲಿಟಿ ಚೆಕ್ ಎಂದಿಗೂ ಬಿಡಬೇಡಿ", cue: "ಮತ್ತು ಬಾಟಲ್ನೆಕ್ನಲ್ಲಿ" },
    ],
    action: { text: "ಒಂದು ಸ್ಟೇಷನ್ನಲ್ಲಿ ಹತ್ತು ಸೈಕಲ್ ಅಳೆಯಿರಿ, ಮತ್ತು ಅತ್ಯಂತ ದೀರ್ಘವಾದುದನ್ನು TAKT ಜೊತೆ ಹೋಲಿಸಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "D", title: "Design Thinking", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_KN_DURATION = PLAN.total;

export const CycleTimeStudyKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
