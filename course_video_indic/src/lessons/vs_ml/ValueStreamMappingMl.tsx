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
import words from "../../captions/vs_ml/words.json";

// Malayalam version of ValueStreamMappingMl (same design and polish as the English lesson).
// All data comes from narration/value_stream_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "ഓർഡർ മുതൽ ഡെലിവറി വരെ, മുഴുവൻ ഫ്ലോ കാണുക",
  outroLine: "കാണുക. അളക്കുക. ഫ്ലോ ഉണ്ടാക്കുക.",
  outroSub: "Value Stream Mapping — കാത്തിരിപ്പ് കണ്ടെത്തുക, ഫ്ലോ ഡിസൈൻ ചെയ്യുക",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "മിനിറ്റ്, ഒരു സെറ്റ് ടോപ്പ് ബോക്സ് ഉണ്ടാക്കാനും ടെസ്റ്റ് ചെയ്യാനും",
    sub: "എന്നിട്ടും കസ്റ്റമറിൽ എത്താൻ ഏകദേശം നാല് ദിവസം.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "മിനിറ്റുകളുടെ ജോലിക്ക് ദിവസങ്ങളുടെ കാത്തിരിപ്പ്", before: 4200, after: 2100, unit: "മൂന്ന് ബഫറിൽ കാത്തിരിക്കുന്ന യൂണിറ്റുകൾ",
    fixedLabel: "ഫ്യൂച്ചർ സ്റ്റേറ്റ്: പകുതി കാത്തിരിപ്പ്",
    takeaways: [
      { text: "യഥാർത്ഥ മെറ്റീരിയൽ + വിവര ഫ്ലോയുടെ മാപ്പ്", cue: "യഥാർത്ഥ ഫ്ലോയുടെ മാപ്പ്" },
      { text: "ലീഡ് ടൈം കാത്തിരിപ്പിൽ ഒളിച്ചിരിക്കുന്നു, ജോലിയിലല്ല", cue: "നിങ്ങളുടെ മിക്ക ലീഡ്" },
      { text: "സ്റ്റോക്ക് കുറയ്ക്കും മുമ്പ് ഫ്യൂച്ചർ സ്റ്റേറ്റ് തെളിയിക്കുക", cue: "ഏത് സ്റ്റോക്കും" },
    ],
    action: { text: "ഒരു പ്രോഡക്റ്റ് ഫാമിലിയോടൊപ്പം ഡിസ്പാച്ചിൽ നിന്ന് പിന്നോട്ട് നടന്ന്, ഓരോ കൂമ്പാരവും എണ്ണുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_ML_DURATION = PLAN.total;

export const ValueStreamMappingMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
