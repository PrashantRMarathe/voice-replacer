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
import words from "../../captions/dt_te/words.json";

// Telugu version of DesignThinkingTe (same design and polish as the English lesson).
// All data comes from narration/design_thinking_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "సరైన సమస్యను పరిష్కరించండి, పని చేసేవాళ్ళతో కలిసి",
  outroLine: "చూడండి. నిర్వచించండి. చిన్నగా పరీక్షించండి.",
  outroSub: "Design Thinking — ముందు మనుషులు, ఎప్పుడూ రుజువు",
};

// Same polish as English DesignThinking; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "ప్రతి 1,000 పంపుల్లో లేబుల్ తప్పులు",
    sub: "మొదటి ఆలోచన: ఒక ఖరీదైన వేగమైన ప్రింటర్. ప్యాకర్లను ఎవరూ అడగనే లేదు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "ఇన్ఫ్యూజన్ పంప్ ప్యాకింగ్ వద్ద లేబుల్ తప్పులు", before: 12, after: 2, unit: "1,000 పంపులకు",
    takeaways: [
      { text: "మనుషులతో మొదలుపెట్టండి; నిర్ణయానికి ముందు చూడండి", cue: "పని చేసే మనుషులతో" },
      { text: "అవసరాన్ని నిర్వచించండి, అందులో పరిష్కారం లేదు", cue: "అవసరాన్ని అందులో" },
      { text: "చిన్నగా పరీక్షించండి: ఫలితాలు, అసలు వాడకం", cue: "చిన్న స్థాయిలో" },
    ],
    action: { text: "ఇబ్బందిగా ఉన్న ఒక పనిలో పది సైకిళ్ళు చూడండి, అది చేసే ముగ్గురితో మాట్లాడండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "E", title: "Elimination of Waste", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_TE_DURATION = PLAN.total;

export const DesignThinkingTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
