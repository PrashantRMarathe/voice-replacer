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
import words from "../../captions/gb_ml/words.json";

// Malayalam version of GembaMl (same design and polish as the English lesson).
// All data comes from narration/gemba_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "യഥാർത്ഥ സ്ഥലം, യഥാർത്ഥ വസ്തു, യഥാർത്ഥ വസ്തുതകൾ",
  outroLine: "പോകുക. കാണുക. ഉറപ്പാക്കുക.",
  outroSub: "Gemba, Genbutsu, Genjitsu — തീരുമാനത്തിന് മുമ്പ് വസ്തുതകൾ",
};

// Same polish as English Gemba; cues are phrases from the Malayalam intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× ഇയർബഡ് ഫെയിലിയർ, ഷിഫ്റ്റ് B-യിൽ",
    sub: "പ്ലാൻ: ഷിഫ്റ്റ് B-യെ വീണ്ടും ട്രെയിൻ ചെയ്യുക. ആരും ഒരു ഫെയിൽ ഇയർബഡ് പോലും കണ്ടില്ല.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ഓഡിയോ ടെസ്റ്റിൽ ഫെയിലാകുന്ന ഇയർബഡുകൾ", before: 20, after: 8, unit: "1,000 ഇയർബഡിന് ഫെയിലിയർ",
    fixedLabel: "കാരണത്തിൽ ശരിയാക്കി",
    takeaways: [
      { text: "യഥാർത്ഥ സ്ഥലത്ത് പോകുക; യഥാർത്ഥ സൈക്കിളുകൾ കാണുക", cue: "യഥാർത്ഥ സ്ഥലത്ത് പോകുക" },
      { text: "യഥാർത്ഥ വസ്തു കൈയിലെടുക്കുക; നല്ലതുമായി താരതമ്യം", cue: "യഥാർത്ഥ വസ്തു കൈയിലെടുക്കുക" },
      { text: "യഥാർത്ഥ വസ്തുതകൾ ഉറപ്പാക്കുക, ഹാരകത്തോടെ", cue: "യഥാർത്ഥ വസ്തുതകൾ ഉറപ്പാക്കുക" },
    ],
    action: { text: "ആവർത്തിക്കുന്ന ഒരു പ്രശ്നം എടുത്ത്, മുപ്പത് മിനിറ്റിന്റെ ഒരു 3G സന്ദർശനം നടത്തുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "H", title: "Hancho", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_ML_DURATION = PLAN.total;

export const GembaMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
