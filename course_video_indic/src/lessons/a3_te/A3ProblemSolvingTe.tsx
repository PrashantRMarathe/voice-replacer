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
import words from "../../captions/a3_te/words.json";

// Telugu version of A3ProblemSolvingTe (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "సమస్య మొత్తం కథ, ఒకే పేజీలో",
  outroLine: "గ్యాప్ చూడండి. కారణం నిరూపించండి. నిలబెట్టండి.",
  outroSub: "A3 — మెరుగైన ఆలోచన, ఒకే షీటులో",
};

// Same polish as English A3ProblemSolving; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "సర్వర్లు మొదటి బూట్ టెస్టులో ఫెయిల్",
    sub: "నాలుగు వారాల్లో. మొదటి సూచన: ఇంకో ఇద్దరు ఇన్‌స్పెక్టర్లు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "మొదటి బూట్ టెస్టులో ఫెయిల్ అవుతున్న సర్వర్లు", before: 48, after: 16, unit: "ప్రతి 1,000 సర్వర్లకు", fixedLabel: "టార్గెట్ పూర్తి: 48 కంటే తక్కువ",
    takeaways: [
      { text: "కొలవగలిగే గ్యాపుతో మొదలుపెట్టండి", cue: "మొదట కొలవగలిగే" },
      { text: "వెళ్లి చూడండి; ప్రతి కారణం నిరూపించండి", cue: "వెళ్లి చూడండి" },
      { text: "పైలట్ నిరూపించినదే స్టాండర్డ్", cue: "మీ పైలట్ నిజంగా" },
    ],
    action: { text: "పదే పదే వచ్చే ఒక సమస్యను ఎంచుకుని, దాని ప్రాబ్లమ్ స్టేట్‌మెంటును A3 మీద రాయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "B", title: "Burn Down Chart", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_TE_DURATION = PLAN.total;

export const A3ProblemSolvingTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
