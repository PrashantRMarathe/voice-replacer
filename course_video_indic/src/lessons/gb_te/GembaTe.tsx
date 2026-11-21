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
import words from "../../captions/gb_te/words.json";

// Telugu version of GembaTe (same design and polish as the English lesson).
// All data comes from narration/gemba_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "అసలు స్థలం, అసలు వస్తువు, అసలు వాస్తవాలు",
  outroLine: "వెళ్ళండి. చూడండి. నిర్ధారించండి.",
  outroSub: "Gemba, Genbutsu, Genjitsu — నిర్ణయానికి ముందు వాస్తవాలు",
};

// Same polish as English Gemba; cues are phrases from the Telugu intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× ఇయర్ బడ్ ఫెయిల్యూర్లు, షిఫ్ట్ B లో",
    sub: "ప్లాన్: షిఫ్ట్ B కి మళ్లీ ట్రైనింగ్. ఎవరూ ఒక ఫెయిల్ ఇయర్ బడ్ కూడా చూడలేదు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "ఆడియో టెస్టులో ఫెయిల్ అయ్యే ఇయర్ బడ్లు", before: 20, after: 8, unit: "1,000 ఇయర్ బడ్లకు ఫెయిల్యూర్లు",
    fixedLabel: "కారణం దగ్గర సరిచేశారు",
    takeaways: [
      { text: "అసలు స్థలానికి వెళ్ళండి; అసలు సైకిళ్ళు చూడండి", cue: "అసలు స్థలానికి వెళ్ళండి" },
      { text: "అసలు వస్తువు చేతిలోకి; మంచిదానితో పోల్చండి", cue: "అసలు వస్తువును చేతిలోకి" },
      { text: "అసలు వాస్తవాలు పరీక్షించండి, హారంతో", cue: "అసలు వాస్తవాలను" },
    ],
    action: { text: "పదే పదే వచ్చే ఒక సమస్య తీసుకుని, ముప్పై నిమిషాల 3G విజిట్ చేయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "H", title: "Hancho", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_TE_DURATION = PLAN.total;

export const GembaTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
