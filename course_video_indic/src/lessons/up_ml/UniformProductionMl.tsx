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
import words from "../../captions/up_ml/words.json";

// Malayalam version of UniformProductionMl (same design and polish as the English lesson).
// All data comes from narration/uniform_production_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "സ്ഥിരവും വിശ്വസനീയവുമായ ഫ്ലോയ്ക്ക് വോളിയവും മിക്സും ലെവൽ ചെയ്യുക",
  outroLine: "ലെവൽ ചെയ്യുക. ക്രമം നിശ്ചയിക്കുക. സ്ഥിരമാക്കുക.",
  outroSub: "Uniform Production — നിങ്ങളുടെ ലൈനിന് നിലനിർത്താവുന്ന വേഗം",
};

// Same polish as English UniformProduction; cues are phrases from the Malayalam intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "ഫോൺ തിങ്കളാഴ്ച. ചൊവ്വാഴ്ച ഏതാണ്ട് ഒന്നുമില്ല.",
    sub: "ബുധനാഴ്ചയോടെ, ടെസ്റ്റ് ബെഞ്ച് ജോലിയിൽ മുങ്ങി.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "വളരെ കുണ്ടും കുഴിയുമുള്ള ഒരു ഷെഡ്യൂൾ", before: 0, after: 6000, unit: "ദിവസം നല്ല യൂണിറ്റ്, ഓരോ ദിവസവും",
    fixedLabel: "സ്ഥിരമായ, ലെവൽ വേഗം",
    takeaways: [
      { text: "വോളിയവും മിക്സും, രണ്ടും ലെവൽ ചെയ്യുക", cue: "വോളിയവും മിക്സും, രണ്ടും" },
      { text: "ആദ്യം ബോട്ടിൽനെക്കും ചേഞ്ച്ഓവറും പരിശോധിക്കുക", cue: "ഒരു പാറ്റേണിനെ" },
      { text: "കാണാവുന്ന പ്ലാൻ, മാറ്റത്തിന് വ്യക്തമായ നിയമങ്ങൾ", cue: "പ്ലാൻ കാണാവുന്നതാക്കുക" },
    ],
    action: { text: "വലിയ ബാച്ചിൽ ഉണ്ടാക്കുന്ന ഒരു പ്രോഡക്റ്റ് കണ്ടെത്തി, ചെറിയ, ആവർത്തിക്കുന്ന പാറ്റേൺ സ്കെച്ച് ചെയ്യുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_ML_DURATION = PLAN.total;

export const UniformProductionMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
