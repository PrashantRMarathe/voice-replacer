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
import words from "../../captions/ew_ml/words.json";

// Malayalam version of EliminationOfWasteMl (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "കസ്റ്റമർ പണം നൽകാത്തത് നീക്കുക",
  outroLine: "കാണുക. കാരണം നീക്കുക. തെളിയിക്കുക.",
  outroSub: "Elimination of Waste — കൂടുതൽ മൂല്യം, കുറവ് അധ്വാനം",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "സൗണ്ട്ബാറുകൾ ഓരോ മാസവും റീവർക്ക്",
    sub: "ഓരോന്നും ശരിയാക്കാൻ ₹42. ആരും ഇത് ഒരിക്കലും കൂട്ടിനോക്കിയില്ല.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "മൂളുന്ന സ്പീക്കർ വയർ കാരണം റീവർക്ക് ചെയ്യുന്ന സൗണ്ട്ബാറുകൾ", before: 1500, after: 300, unit: "മാസം റീവർക്ക്", fixedLabel: "റീവർക്ക് 80% കുറഞ്ഞു",
    takeaways: [
      { text: "വേസ്റ്റ്: കസ്റ്റമർ പണം നൽകാത്തത്", cue: "കസ്റ്റമർ പണം നൽകാത്തതെല്ലാം" },
      { text: "ഇത് Gemba-യിൽ വസ്തുതകൾ കൊണ്ട് കണ്ടെത്തുക", cue: "ഇത് Gemba-യിൽ" },
      { text: "കാരണം നീക്കുക, തെളിയിക്കുക, നിലനിർത്തുക", cue: "കാരണം നീക്കി" },
    ],
    action: { text: "മുപ്പത് മിനിറ്റ് നിങ്ങളുടെ ലൈനിൽ നടന്ന്, മൂന്ന് വേസ്റ്റുകൾ വസ്തുതകളായി എഴുതുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "F", title: "FMEA", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_ML_DURATION = PLAN.total;

export const EliminationOfWasteMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
