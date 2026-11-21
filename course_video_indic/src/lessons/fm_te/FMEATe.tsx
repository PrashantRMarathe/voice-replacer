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
import words from "../../captions/fm_te/words.json";

// Telugu version of FMEATe (same design and polish as the English lesson).
// All data comes from narration/fmea_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "ఫెయిల్యూర్ మోడ్ అండ్ ఎఫెక్ట్స్ అనాలిసిస్: ఫెయిల్యూర్ ముందే ఆలోచించండి",
  outroLine: "చైన్ తయారు చేయండి. స్కోర్ ఇవ్వండి. నివారించండి.",
  outroSub: "FMEA — సజీవ ప్లాన్, ఫారం కాదు",
};

// Same polish as English FMEA; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "అవుట్డోర్ రేడియోలు నీటితో నిండి తిరిగి వచ్చాయి",
    sub: "రెండింటిలో గాస్కెట్ లేదు, నాలుగింటిలో మడత. అన్నీ ఫైనల్ ఇన్స్పెక్షన్లో పాస్ అయ్యాయి.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "అవుట్డోర్ 5G రేడియో మీద గాస్కెట్ రిస్క్", before: 240, after: 32, unit: "రిస్క్ ప్రయారిటీ నంబర్",
    fixedLabel: "రిస్క్ తగ్గింది, ట్రయల్లో నిరూపితం",
    takeaways: [
      { text: "ఎఫెక్ట్ → ఫెయిల్యూర్ మోడ్ → కంట్రోల్ చేయగల కారణం", cue: "ఒక స్పష్టమైన" },
      { text: "రుజువుతో స్కోర్; నంబర్ కంటే తెలివి పైన", cue: "రుజువుతో స్కోర్" },
      { text: "ముందు నివారణ, నిరూపించండి, తర్వాత మళ్లీ స్కోర్", cue: "నివారణను ఎంచుకోండి" },
    ],
    action: { text: "ఒక ముఖ్యమైన అడుగు ఎంచుకుని, మీ టీముతో దాని ఫెయిల్యూర్ చైన్ రాయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "G", title: "Gemba", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_TE_DURATION = PLAN.total;

export const FMEATe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
