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
import words from "../../captions/up_te/words.json";

// Telugu version of UniformProductionTe (same design and polish as the English lesson).
// All data comes from narration/uniform_production_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "స్థిరమైన, నమ్మదగిన ఫ్లో కోసం వాల్యూమ్, మిక్స్ లెవెల్ చేయండి",
  outroLine: "లెవెల్ చేయండి. క్రమం పెట్టండి. స్థిరపరచండి.",
  outroSub: "Uniform Production — మీ లైన్ నిలబెట్టుకోగల వేగం",
};

// Same polish as English UniformProduction; cues are phrases from the Telugu intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "ఫోన్లు సోమవారం. మంగళవారం దాదాపు ఏమీ లేదు.",
    sub: "బుధవారానికి, టెస్ట్ బెంచ్ పనిలో మునిగిపోయింది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "చాలా ఎగుడుదిగుడు షెడ్యూల్", before: 0, after: 6000, unit: "రోజుకు మంచి యూనిట్లు, ప్రతి రోజు",
    fixedLabel: "ఒక స్థిరమైన, లెవెల్ వేగం",
    takeaways: [
      { text: "వాల్యూమ్, మిక్స్, రెండూ లెవెల్ చేయండి", cue: "వాల్యూమ్, మిక్స్, రెండింటినీ" },
      { text: "ముందు బాటిల్‌నెక్, చేంజోవర్లు చెక్ చేయండి", cue: "ఏ ప్యాటర్న్ నైనా" },
      { text: "కనిపించే ప్లాన్, మార్పుకు స్పష్టమైన నియమాలు", cue: "మరియు ప్లాన్ ను" },
    ],
    action: { text: "పెద్ద బ్యాచ్ లలో తయారయ్యే ఒక ప్రొడక్ట్ ను వెతకండి, చిన్న, పునరావృత ప్యాటర్న్ స్కెచ్ వేయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_TE_DURATION = PLAN.total;

export const UniformProductionTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
