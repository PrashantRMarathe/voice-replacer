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
import words from "../../captions/rc_te/words.json";

// Telugu version of RootCauseAnalysisTe (same design and polish as the English lesson).
// All data comes from narration/root_cause_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "లక్షణం నుండి నిరూపించగల కారణం వరకు",
  outroLine: "నిర్వచించండి. పరీక్షించండి. ఆపండి.",
  outroSub: "Root Cause Analysis — నిరూపించండి, తర్వాత సరిచేయండి",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "ఒకే ఉదయం ఫోకస్ టెస్టులో ఫెయిల్ అయిన కెమెరాలు",
    sub: "ముగ్గురు మనుషులు, మూడు వేర్వేరు జవాబులు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "చేంజోవర్ తర్వాత ఫోకస్ లో ఫెయిల్ అయిన కెమెరాలు", before: 60, after: 12, unit: "20,000 కెమెరాలకు డిఫెక్టులు",
    takeaways: [
      { text: "పదునైన నిర్వచనం, కస్టమరును కాపాడండి", cue: "సమస్యను పదునుగా" },
      { text: "పరీక్షించే వరకు ప్రతి కారణం హైపోథెసిస్", cue: "ప్రతి కారణాన్నీ" },
      { text: "ఎందుకు జరిగింది, ఎందుకు తప్పించుకుంది, రెండూ సరిచేయండి", cue: "మరియు రెండూ సరిచేయండి" },
    ],
    action: { text: "మూసేసిన ఒక సమస్యను తీసుకోండి, దాని రూట్ కాజ్ ను ఎప్పుడైనా పరీక్షించారా అని చెక్ చేయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_TE_DURATION = PLAN.total;

export const RootCauseAnalysisTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
