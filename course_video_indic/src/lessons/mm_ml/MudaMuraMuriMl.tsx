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
import words from "../../captions/mm_ml/words.json";

// Malayalam version of MudaMuraMuriMl (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "വേസ്റ്റ്, അസമത്വം, അമിതഭാരം — മൂന്നും ശരിയാക്കുക",
  outroLine: "ലെവൽ ചെയ്യുക. സംരക്ഷിക്കുക. നീക്കുക.",
  outroSub: "3M — സ്ഥിരമായ ഫ്ലോ, വേഗമുള്ള ആളുകളല്ല",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "ക്യാമറ പിന്നിൽ, ഷിഫ്റ്റ് തീരാൻ ഒരു മണിക്കൂർ ബാക്കി",
    sub: "എല്ലാവരും ഓടുകയാണ്. ടെസ്റ്റിൽ തെറ്റുകൾ കൂടുന്നു.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "സഞ്ജയിന്റെ ലൈൻ ദിവസവും വൈകി ഓടി", before: 150, after: 0, unit: "മിനിറ്റ് ഓവർടൈം ദിവസവും",
    takeaways: [
      { text: "Muda വേസ്റ്റ്, Mura അസമത്വം, Muri അമിതഭാരം", cue: "Muda വേസ്റ്റ്" },
      { text: "ഇവ പരസ്പരം വളർത്തുന്നു: ഒന്നിച്ച് ശരിയാക്കുക", cue: "ഇവ പരസ്പരം" },
      { text: "സ്ഥിരമായ ഫ്ലോ, വേഗമുള്ള ആളുകളല്ല", cue: "ലക്ഷ്യം സ്ഥിരമായ" },
    ],
    action: { text: "ഒരു പ്രോഡക്റ്റിനൊപ്പം നിങ്ങളുടെ ലൈനിലൂടെ നടന്ന്, ഓരോ M-ന്റെയും ഒരു ഉദാഹരണം ടാഗ് ചെയ്യുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "N", title: "Next Inspection", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_ML_DURATION = PLAN.total;

export const MudaMuraMuriMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
