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
import words from "../../captions/ww_ml/words.json";

// Malayalam version of WhyWhyMl (same design and polish as the English lesson).
// All data comes from narration/why_why_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "എളുപ്പമുള്ള ഉത്തരത്തിനപ്പുറം, തെളിയിക്കാവുന്ന കാരണം വരെ",
  outroLine: "നിർവചിക്കുക. തെളിയിക്കുക. തടയുക.",
  outroSub: "Why–Why — കാരണം ശരിയാക്കുക, ആളെയല്ല",
};

// Same polish as English WhyWhy; cues are phrases from the Malayalam intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "ഫോണുകൾ ഫൈനൽ ടെസ്റ്റിൽ ചാർജിങ്ങിൽ ഫെയിൽ",
    sub: "ആദ്യ ഉത്തരം: ഓപ്പറേറ്റർ തെറ്റ്. രണ്ട് ദിവസം കഴിഞ്ഞ്, വീണ്ടും അതുതന്നെ.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ലൈൻ 2-ൽ ചാർജിങ് ഫെയിലിയർ", before: 50, after: 15, unit: "ചാർജിങ് ഡിഫെക്റ്റ്, അതേ വോളിയം",
    fixedLabel: "റൂട്ട് കോസ് ശരിയാക്കി: 70% കുറവ്",
    takeaways: [
      { text: "ആദ്യം മൂർച്ചയുള്ള പ്രശ്നം, പിന്നെ കണ്ടെയ്ൻമെന്റ്", cue: "മൂർച്ചയുള്ള ഒരു പ്രശ്നത്തിൽ" },
      { text: "ഓരോ എന്തുകൊണ്ടിനും തെളിവ്, പിന്നെ പരീക്ഷിക്കുക", cue: "ഓരോ എന്തുകൊണ്ടിനും" },
      { text: "എങ്ങനെ സംഭവിച്ചു, എന്തുകൊണ്ട് പുറത്തുപോയി, രണ്ടും ശരിയാക്കുക", cue: "രണ്ടും ശരിയാക്കുക" },
    ],
    action: { text: "ആവർത്തിക്കുന്ന ഒരു ഡിഫെക്റ്റ് എടുത്ത്, അതിന്റെ 5W2H സ്റ്റേറ്റ്മെന്റ് എഴുതുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "X", title: "X-Matrix", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_ML_DURATION = PLAN.total;

export const WhyWhyMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
