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
import words from "../../captions/ww_te/words.json";

// Telugu version of WhyWhyTe (same design and polish as the English lesson).
// All data comes from narration/why_why_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "సులభమైన జవాబు దాటి, మీరు నిరూపించగల కారణం వరకు",
  outroLine: "నిర్వచించండి. నిరూపించండి. ఆపండి.",
  outroSub: "Why–Why — కారణాన్ని సరిచేయండి, వ్యక్తిని కాదు",
};

// Same polish as English WhyWhy; cues are phrases from the Telugu intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "ఫైనల్ టెస్టులో ఛార్జింగ్ లో ఫెయిల్ అయిన ఫోన్లు",
    sub: "మొదటి జవాబు: ఆపరేటర్ తప్పు. రెండు రోజుల తర్వాత, మళ్లీ అదే జరిగింది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "లైన్ 2 లో ఛార్జింగ్ ఫెయిల్యూర్లు", before: 50, after: 15, unit: "ఛార్జింగ్ డిఫెక్టులు, అదే వాల్యూమ్",
    fixedLabel: "రూట్ కాజ్ సరిచేశారు: 70% తక్కువ",
    takeaways: [
      { text: "ముందు పదునైన సమస్య, తర్వాత కంటైన్‌మెంట్", cue: "ఒక పదునైన సమస్యతో" },
      { text: "ప్రతి ఎందుకుకూ సాక్ష్యం, తర్వాత పరీక్షించండి", cue: "ప్రతి ఎందుకు వెనక" },
      { text: "ఎలా జరిగింది, ఎందుకు తప్పించుకుంది, రెండూ సరిచేయండి", cue: "మరియు రెండూ సరిచేయండి" },
    ],
    action: { text: "పదే పదే వచ్చే ఒక డిఫెక్ట్ తీసుకోండి, దాని 5W2H స్టేట్‌మెంట్ రాయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "X", title: "X-Matrix", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_TE_DURATION = PLAN.total;

export const WhyWhyTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
