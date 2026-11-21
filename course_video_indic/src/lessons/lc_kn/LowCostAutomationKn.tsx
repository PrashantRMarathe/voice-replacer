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
import words from "../../captions/lc_kn/words.json";

// Kannada version of LowCostAutomationKn (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "ಕೆಲಸ ಮಾಡುವ ಅತ್ಯಂತ ಸರಳ ಸುರಕ್ಷಿತ ಡಿವೈಸ್",
  outroLine: "ಸರಳಗೊಳಿಸಿ. ಅಗತ್ಯವನ್ನು ಆಟೋಮೇಟ್ ಮಾಡಿ. ಸಾಬೀತುಪಡಿಸಿ.",
  outroSub: "Low Cost Automation — ಎಂದಿಗೂ ಕಡಿಮೆ ಸೇಫ್ಟಿ ಅಲ್ಲ",
};

// Same polish as English LowCostAutomation; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "ಗಂಟೆಗೆ ಮ್ಯಾಲೆಟ್ ಹೊಡೆತ, ಪ್ರತಿ ಆಪರೇಟರ್",
    sub: "ನೋಯುವ ಮಣಿಕಟ್ಟುಗಳು, ಮತ್ತು ಟೆಸ್ಟ್ನಲ್ಲಿ ಕಡಕಡಿಸುವ ಸಡಿಲ ಗ್ರಿಲ್ಗಳು.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಮ್ಯಾಲೆಟ್ನಿಂದ ಕೂರಿಸಿದಾಗ ಸಡಿಲ ಸ್ಪೀಕರ್ ಗ್ರಿಲ್", before: 18, after: 2, unit: "ಪ್ರತಿ 1,000 ಸ್ಪೀಕರ್ಗೆ",
    fixedLabel: "4 ತಿಂಗಳಲ್ಲಿ ವಸೂಲಿ",
    takeaways: [
      { text: "ಮೊದಲು ಸರಳಗೊಳಿಸಿ; ವೇಸ್ಟ್ ಎಂದಿಗೂ ಆಟೋಮೇಟ್ ಇಲ್ಲ", cue: "ಮೊದಲು ಸರಳಗೊಳಿಸಿ" },
      { text: "ಅತ್ಯಂತ ಸರಳ ಸುರಕ್ಷಿತ ಪರಿಹಾರ; ಸೇಫ್ಟಿ ಮೊದಲ ಗೇಟ್", cue: "ಕೆಲಸ ಮಾಡುವ ಅತ್ಯಂತ" },
      { text: "ನಿಜವಾದ ಲಾಭ ಸಾಬೀತುಪಡಿಸಿ, ನಂತರ ನಿರ್ವಹಣೆ", cue: "ಮತ್ತು ನಿಜವಾದ ಲಾಭವನ್ನು" },
    ],
    action: { text: "ಪುನರಾವರ್ತಿತ ಒಂದು ಚಲನೆಯನ್ನು ಹುಡುಕಿ, ಮತ್ತು ಆಟೋಮೇಟ್ ಮಾಡುವ ಮೊದಲು ಅದನ್ನು ತೆಗೆಯಬಹುದೇ ಎಂದು ಕೇಳಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_KN_DURATION = PLAN.total;

export const LowCostAutomationKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
