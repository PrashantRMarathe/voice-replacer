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
import words from "../../captions/ik_te/words.json";

// Telugu version of IshikawaTe (same design and polish as the English lesson).
// All data comes from narration/ishikawa_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "ఫిష్ బోన్ తో విశాలంగా వెతకండి, తర్వాత కారణం నిరూపించండి",
  outroLine: "విశాలంగా వెతకండి. కచ్చితంగా నిరూపించండి.",
  outroSub: "Ishikawa — పరీక్షించే వరకు ప్రతి ఎముక ఒక అంచనా",
};

// Same polish as English Ishikawa; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "1,000 స్విచ్ లకు పోర్ట్ టెస్టులో ఫెయిల్",
    sub: "5 నుంచి పెరిగింది. మీటింగ్ జవాబు: కొత్త టెస్టర్ కొనండి.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "స్విచ్ లైన్లో పోర్ట్-లింక్ ఫెయిల్యూర్లు", before: 32, after: 4, unit: "1,000 స్విచ్ లకు",
    fixedLabel: "రెండు కారణాలు సరి",
    takeaways: [
      { text: "తల మీద పదునైన, కొలవగలిగే ఎఫెక్ట్", cue: "తల మీద ఒక" },
      { text: "6M లో విశాలంగా వెతకండి, నింద లేకుండా", cue: "ఆరు ఎమ్ లలో" },
      { text: "నిరూపణ వరకు ప్రతి ఎముక అంచనా", cue: "ప్రతి ఎముకను" },
    ],
    action: { text: "పదే పదే వచ్చే ఒక సమస్యకు ఫిష్ బోన్ గీసి, పరీక్షించడానికి మూడు కారణాలు ఎంచుకోండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "J", title: "Jidoka", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_TE_DURATION = PLAN.total;

export const IshikawaTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
