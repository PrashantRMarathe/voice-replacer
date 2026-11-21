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
import words from "../../captions/bd_te/words.json";

// Telugu version of BurnDownChartTe (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "డెడ్లైన్ ముందు మిగిలిన పని చూడండి",
  outroLine: "లైన్ నిర్ణయించండి. గ్యాప్ చూడండి. ఈ రోజే చర్య తీసుకోండి.",
  outroSub: "Burn Down Chart — ఇక శుక్రవారం షాకులు లేవు",
};

// Same polish as English BurnDownChart; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "రౌటర్లు ట్రక్ అందుకోలేదు",
    sub: "శుక్రవారం మధ్యాహ్నం వరకు ఎవరికీ తెలియదు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "డిస్పాచ్ వద్ద తక్కువైన రౌటర్లు", before: 80, after: 0, unit: "రౌటర్లు తక్కువ",
    takeaways: [
      { text: "ముందు ఐడియల్ లైన్; దాన్ని మళ్లీ ఎప్పుడూ కాదు", cue: "ముందు ఐడియల్" },
      { text: "పూర్తయిన, మంచి పని మాత్రమే లెక్కించండి", cue: "నిజంగా పూర్తయిన" },
      { text: "ఐడియల్ కంటే పైన? అదే రోజు చర్య, ఓనర్ తో", cue: "లైన్ ఐడియల్" },
    ],
    action: { text: "డెడ్లైన్ ఉన్న ఒక పని ఎంచుకోండి, రేపటి షిఫ్ట్ ముందు దాని బర్న్-డౌన్ గీయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "C", title: "Cycle Time Study", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_TE_DURATION = PLAN.total;

export const BurnDownChartTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
