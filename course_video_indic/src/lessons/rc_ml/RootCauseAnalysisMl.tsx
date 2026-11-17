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
import words from "../../captions/rc_ml/words.json";

// Malayalam version of RootCauseAnalysisMl (same design and polish as the English lesson).
// All data comes from narration/root_cause_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "ലക്ഷണത്തിൽ നിന്ന് തെളിയിക്കാവുന്ന കാരണത്തിലേക്ക്",
  outroLine: "നിർവചിക്കുക. പരീക്ഷിക്കുക. തടയുക.",
  outroSub: "Root Cause Analysis — തെളിയിക്കുക, പിന്നെ ശരിയാക്കുക",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "ക്യാമറകൾ ഒരു രാവിലെ ഫോക്കസ് ടെസ്റ്റിൽ ഫെയിൽ",
    sub: "മൂന്ന് പേർ, മൂന്ന് വ്യത്യസ്ത ഉത്തരങ്ങൾ.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ചേഞ്ച്ഓവറിന് ശേഷം ഫോക്കസിൽ ഫെയിലായ ക്യാമറകൾ", before: 60, after: 12, unit: "20,000 ക്യാമറയ്ക്ക് ഡിഫെക്റ്റ്",
    takeaways: [
      { text: "മൂർച്ചയുള്ള നിർവചനം, കസ്റ്റമറെ സംരക്ഷിക്കുക", cue: "പ്രശ്നം മൂർച്ചയോടെ" },
      { text: "പരീക്ഷിക്കും വരെ ഓരോ കാരണവും ഹൈപ്പോതെസിസ്", cue: "ടെസ്റ്റ് തെളിയിക്കും" },
      { text: "എന്തുകൊണ്ട് സംഭവിച്ചു, എന്തുകൊണ്ട് പുറത്തുപോയി, രണ്ടും ശരിയാക്കുക", cue: "രണ്ടും ശരിയാക്കുക" },
    ],
    action: { text: "അടച്ച ഒരു പ്രശ്നം എടുത്ത്, അതിന്റെ റൂട്ട് കോസ് എപ്പോഴെങ്കിലും പരീക്ഷിച്ചോ എന്ന് പരിശോധിക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_ML_DURATION = PLAN.total;

export const RootCauseAnalysisMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
