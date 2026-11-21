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
import words from "../../captions/xm_ml/words.json";

// Malayalam version of XMatrixMl (same design and polish as the English lesson).
// All data comes from narration/x_matrix_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Hoshin Kanri കൊണ്ട് തന്ത്രത്തെ ആക്ഷനാക്കുക",
  outroLine: "ബന്ധിപ്പിക്കുക. നടപ്പാക്കുക. റിവ്യൂ ചെയ്യുക.",
  outroSub: "X-Matrix — നിങ്ങൾക്ക് ശരിക്കും നടപ്പാക്കാവുന്ന തന്ത്രം",
};

// Same polish as English XMatrix; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "ഇംപ്രൂവ്മെന്റ് പ്രോജക്റ്റുകൾ, ഓരോ ടീമും തിരക്കിൽ",
    sub: "എന്നിട്ടും ഡെലിവറി ഓരോ ക്വാർട്ടറിലും വഴുതി.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "തിരക്കുള്ള പോർട്ട്ഫോളിയോ, വഴുതുന്ന ഡെലിവറി", before: 40, after: 3, unit: "പ്രോജക്റ്റുകൾ, ഓരോന്നും ഒരു ലക്ഷ്യവുമായും KPI-യുമായും ബന്ധിപ്പിച്ചത്",
    fixedLabel: "ഫോക്കസ്ഡ് പോർട്ട്ഫോളിയോ",
    takeaways: [
      { text: "ചില യഥാർത്ഥ മുൻഗണനകൾ, ആഗ്രഹങ്ങളുടെ പട്ടികയല്ല", cue: "ചില യഥാർത്ഥ മുൻഗണനകൾ" },
      { text: "ലക്ഷ്യം → പ്രോജക്റ്റ് → KPI → ഒരു ഓണർ", cue: "ഓരോ ലക്ഷ്യത്തെയും" },
      { text: "സത്യസന്ധമായ റിവ്യൂ: നമ്പറുകൾ നീങ്ങണം", cue: "സത്യസന്ധമായി റിവ്യൂ" },
    ],
    action: { text: "നിങ്ങളുടെ ഏരിയയ്ക്ക് ഒരു ഉദ്ദേശ്യം എഴുതുക, ഫലമായി, ജോലിയായല്ല.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "Y", title: "Yamazumi", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_ML_DURATION = PLAN.total;

export const XMatrixMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
