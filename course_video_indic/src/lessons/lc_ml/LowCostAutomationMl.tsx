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
import words from "../../captions/lc_ml/words.json";

// Malayalam version of LowCostAutomationMl (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "ജോലി ചെയ്യുന്ന ഏറ്റവും ലളിതമായ സുരക്ഷിത ഉപകരണം",
  outroLine: "ലളിതമാക്കുക. ആവശ്യം ഓട്ടോമേറ്റ് ചെയ്യുക. തെളിയിക്കുക.",
  outroSub: "Low Cost Automation — ഒരിക്കലും കുറഞ്ഞ സേഫ്റ്റിയല്ല",
};

// Same polish as English LowCostAutomation; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "മാലറ്റ് അടി മണിക്കൂറിൽ, ഓരോ ഓപ്പറേറ്ററും",
    sub: "വേദനിക്കുന്ന കൈത്തണ്ടകൾ, ടെസ്റ്റിൽ കിലുങ്ങുന്ന അയഞ്ഞ ഗ്രില്ലുകൾ.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "മാലറ്റ് കൊണ്ട് ഇരുത്തിയ അയഞ്ഞ സ്പീക്കർ ഗ്രില്ലുകൾ", before: 18, after: 2, unit: "1,000 സ്പീക്കറിന്",
    fixedLabel: "4 മാസത്തിൽ തിരിച്ചുകിട്ടൽ",
    takeaways: [
      { text: "ആദ്യം ലളിതമാക്കുക; വേസ്റ്റ് ഒരിക്കലും ഓട്ടോമേറ്റ് ചെയ്യരുത്", cue: "ആദ്യം ലളിതമാക്കുക" },
      { text: "ഏറ്റവും ലളിതമായ സുരക്ഷിത പരിഹാരം; സേഫ്റ്റി ആദ്യ ഗേറ്റ്", cue: "ജോലി ചെയ്യുന്ന ഏറ്റവും" },
      { text: "യഥാർത്ഥ നേട്ടം തെളിയിക്കുക, പിന്നെ പരിപാലിക്കുക", cue: "യഥാർത്ഥ നേട്ടം" },
    ],
    action: { text: "ആവർത്തിക്കുന്ന ഒരു ചലനം കണ്ടെത്തി, ഓട്ടോമേറ്റ് ചെയ്യും മുമ്പ് അത് ഒഴിവാക്കാനാകുമോ എന്ന് ചോദിക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_ML_DURATION = PLAN.total;

export const LowCostAutomationMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
