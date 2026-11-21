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
import words from "../../captions/yz_kn/words.json";

// Kannada version of YamazumiKn (same design and polish as the English lesson).
// All data comes from narration/yamazumi_kn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_kn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "ನಿಜವಾದ ಡೇಟಾದಿಂದ, TAKT ಎದುರು ಲೈನ್ ಬ್ಯಾಲೆನ್ಸ್ ಮಾಡಿ",
  outroLine: "ಅಳೆಯಿರಿ. ರಾಶಿ ಮಾಡಿ. ಬ್ಯಾಲೆನ್ಸ್ ಮಾಡಿ.",
  outroSub: "Yamazumi — ವಿನ್ಯಾಸದಿಂದಲೇ ಉಳಿಯುವ ಫ್ಲೋ",
};

// Same polish as English Yamazumi; cues are phrases from the Kannada intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "ಆಪರೇಟರ್‌ಗಳು ಕಾಯುತ್ತಿದ್ದಾರೆ, ಒಬ್ಬರು ಸ್ಕ್ರೂಗಳಲ್ಲಿ ಮುಳುಗಿರುವಾಗ",
    sub: "ಯಾರೂ ಸೋಮಾರಿಗಳಲ್ಲ. ಕೆಲಸ ಕೇವಲ ಅಸಮಾನವಾಗಿ ರಾಶಿಯಾಗಿದೆ.", until: "ಈ ಪಾಠದಲ್ಲಿ",
  },
  recap: {
    problem: "ಸ್ಟೇಷನ್ B, TAKT ಗಿಂತ ಮೇಲೆ", before: 35, after: 30, unit: "ಸ್ಟೇಷನ್ B ಯಲ್ಲಿ ಕೆಲಸದ ಸೆಕೆಂಡ್",
    fixedLabel: "ನಂತರ TAKT ನಲ್ಲಿ",
    takeaways: [
      { text: "ನಿಜವಾದ ಕೆಲಸ ಅಳೆಯಿರಿ, ಅತ್ಯುತ್ತಮ ಕೇಸ್ ಅಲ್ಲ", cue: "ನಿಜವಾದ ಕೆಲಸ ಅಳೆಯಿರಿ" },
      { text: "TAKT ಎದುರು ರಾಶಿ ಮಾಡಿ, ರಾಶಿ ನೋಡಿ", cue: "ಅದನ್ನು TAKT ಎದುರು" },
      { text: "ಸೇಫ್ಟಿ ಅಥವಾ ಕ್ವಾಲಿಟಿ ಪಣಕ್ಕಿಡದೆ ಬ್ಯಾಲೆನ್ಸ್", cue: "ಮತ್ತು ಎಚ್ಚರಿಕೆಯಿಂದ" },
    ],
    action: { text: "ನಿಮ್ಮ ಲೈನಿನ ಒಂದು ಸ್ಟೇಷನ್‌ನ ಸಮಯ ಅಳೆಯಿರಿ, ಮತ್ತು TAKT ಎದುರು ಅದರ ಬಾರ್ ಮಾಡಿ.", cue: "ಈ ವಾರ ನಿಮ್ಮ ಕೆಲಸ" },
    next: { letter: "Z", title: "Zero Defects", cue: "ಮುಂದೆ, ನೀವು" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_KN_DURATION = PLAN.total;

export const YamazumiKn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("kn");
  setUI("kn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
