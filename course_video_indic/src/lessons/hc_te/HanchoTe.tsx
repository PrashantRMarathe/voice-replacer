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
import words from "../../captions/hc_te/words.json";

// Telugu version of HanchoTe (same design and polish as the English lesson).
// All data comes from narration/hancho_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "షాప్ ఫ్లోర్ లీడర్షిప్, ప్రతి షిఫ్ట్ ప్రతి గంటా",
  outroLine: "Gemba లో లీడ్ చేయండి. మనుషులను సిద్ధం చేయండి.",
  outroSub: "Hancho — స్టాండర్డును తిరిగి తెండి, ప్రతి రోజూ మెరుగుపరచండి",
};

// Same polish as English Hancho; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TV లు ప్రతి గంటా తక్కువ, ఒక షిఫ్ట్ మొత్తం",
    sub: "మరుసటి ఉదయం రిపోర్ట్ వరకు ఎవరికీ తెలియలేదు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "మోడల్ చేంజ్ తర్వాత అవుట్పుట్ గ్యాప్", before: 98, after: 120, unit: "గంటకు TV లు",
    fixedLabel: "అదే షిఫ్టులో తిరిగి",
    takeaways: [
      { text: "Gemba నుంచి లీడ్ చేయండి: స్టాండర్డ్ వర్సెస్ అసలు", cue: "Gemba నుంచి లీడ్" },
      { text: "గ్యాప్ ప్రతి గంటా చూపించండి; అదే షిఫ్టులో చర్య", cue: "ప్రతి గ్యాపును" },
      { text: "మనుషులను సిద్ధం చేయండి, లైన్ మీ మీద ఆధారపడకుండా", cue: "మీ మనుషులను" },
    ],
    action: { text: "ఒక షిఫ్ట్ కోసం మీ లీడర్ స్టాండర్డ్ వర్క్ రాయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_TE_DURATION = PLAN.total;

export const HanchoTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
