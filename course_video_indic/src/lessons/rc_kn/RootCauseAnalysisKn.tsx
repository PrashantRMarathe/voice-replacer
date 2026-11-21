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
import words from "../../captions/rc_kn/words.json";

// Kannada version of RootCauseAnalysisKn (same design and polish as the English lesson).
// All data comes from narration/root_cause_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "ಲಕ್ಷಣದಿಂದ ಸಾಬೀತುಪಡಿಸಬಹುದಾದ ಕಾರಣದವರೆಗೆ",
  outroLine: "ವ್ಯಾಖ್ಯಾನಿಸಿ. ಪರೀಕ್ಷಿಸಿ. ತಡೆಯಿರಿ.",
  outroSub: "Root Cause Analysis — ಸಾಬೀತುಪಡಿಸಿ, ನಂತರ ಸರಿಪಡಿಸಿ",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "ಒಂದು ಬೆಳಗ್ಗೆ ಫೋಕಸ್ ಟೆಸ್ಟ್ನಲ್ಲಿ ಫೇಲ್ ಆದ ಕ್ಯಾಮೆರಾ",
    sub: "ಮೂವರು ಜನ, ಮೂರು ಬೇರೆ ಉತ್ತರ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಚೇಂಜ್ಓವರ್ ನಂತರ ಫೋಕಸ್ನಲ್ಲಿ ಫೇಲ್ ಆದ ಕ್ಯಾಮೆರಾಗಳು", before: 60, after: 12, unit: "ಪ್ರತಿ 20,000 ಕ್ಯಾಮೆರಾಗೆ ಡಿಫೆಕ್ಟ್",
    takeaways: [
      { text: "ಹರಿತವಾದ ವ್ಯಾಖ್ಯಾನ, ಗ್ರಾಹಕರನ್ನು ರಕ್ಷಿಸಿ", cue: "ಸಮಸ್ಯೆಯನ್ನು ಹರಿತವಾಗಿ" },
      { text: "ಪರೀಕ್ಷಿಸುವವರೆಗೆ ಪ್ರತಿ ಕಾರಣ ಹೈಪೋಥಿಸಿಸ್", cue: "ಪ್ರತಿ ಕಾರಣವನ್ನು" },
      { text: "ಏಕೆ ಆಯಿತು ಮತ್ತು ಏಕೆ ಹೊರಹೋಯಿತು, ಎರಡನ್ನೂ ಸರಿಪಡಿಸಿ", cue: "ಮತ್ತು ಎರಡನ್ನೂ ಸರಿಪಡಿಸಿ" },
    ],
    action: { text: "ಮುಚ್ಚಿದ ಒಂದು ಸಮಸ್ಯೆ ತೆಗೆದುಕೊಳ್ಳಿ, ಮತ್ತು ಅದರ ರೂಟ್ ಕಾಸ್ ಎಂದಾದರೂ ಪರೀಕ್ಷಿಸಲ್ಪಟ್ಟಿತ್ತೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_KN_DURATION = PLAN.total;

export const RootCauseAnalysisKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
