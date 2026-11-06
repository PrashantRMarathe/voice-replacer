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
import words from "../../captions/xm_te/words.json";

// Telugu version of XMatrixTe (same design and polish as the English lesson).
// All data comes from narration/x_matrix_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Hoshin Kanri తో వ్యూహాన్ని యాక్షన్ గా మార్చండి",
  outroLine: "కలపండి. అమలు చేయండి. రివ్యూ చేయండి.",
  outroSub: "X-Matrix — మీరు నిజంగా అమలు చేయగల వ్యూహం",
};

// Same polish as English XMatrix; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "ఇంప్రూవ్‌మెంట్ ప్రాజెక్టులు, ప్రతి టీమ్ బిజీ",
    sub: "అయినా డెలివరీ ప్రతి త్రైమాసికం జారిపోతూనే ఉంది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "బిజీ పోర్ట్‌ఫోలియో, జారిపోతున్న డెలివరీ", before: 40, after: 3, unit: "ప్రాజెక్టులు, ప్రతి దానికీ ఒక లక్ష్యం, KPI తో అనుసంధానం",
    fixedLabel: "ఫోకస్డ్ పోర్ట్‌ఫోలియో",
    takeaways: [
      { text: "కొన్ని నిజమైన ప్రాధాన్యతలు, కోరికల జాబితా కాదు", cue: "కొన్ని నిజమైన ప్రాధాన్యతలు" },
      { text: "లక్ష్యం → ప్రాజెక్ట్ → KPI → ఒక ఓనర్", cue: "ప్రతి లక్ష్యాన్ని" },
      { text: "నిజాయితీ రివ్యూ: నంబర్లు కదలాలి", cue: "మరియు నిజాయితీగా" },
    ],
    action: { text: "మీ ఏరియా కోసం ఒక ఉద్దేశం రాయండి, ఫలితంగా, పనిగా కాదు.", cue: "ఈ వారం మీ పని" },
    next: { letter: "Y", title: "Yamazumi", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_TE_DURATION = PLAN.total;

export const XMatrixTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
