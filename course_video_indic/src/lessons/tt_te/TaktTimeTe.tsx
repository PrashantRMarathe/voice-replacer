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
import words from "../../captions/tt_te/words.json";

// Telugu version of TaktTimeTe (same design and polish as the English lesson).
// All data comes from narration/takt_time_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "మీ కస్టమర్ నిర్ణయించే గుండె చప్పుడు",
  outroLine: "కొలవండి. బ్యాలెన్స్ చేయండి. ఫ్లో చేయండి.",
  outroSub: "TAKT Time — కస్టమర్ వేగం",
};

// Same polish as English TaktTime; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "టెస్ట్ కంటే ముందు తయారైన కెమెరాలు",
    sub: "ప్రతి స్టేషన్ బిజీ. ట్రక్ అయినా ఆలస్యంగా వెళ్ళింది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "బిజీ లైన్, అయినా ట్రక్ మిస్", before: 0, after: 10, unit: "సెకన్లు: రోజుకు 7,200 కెమెరాల గుండె చప్పుడు",
    fixedLabel: "అందరూ నడిచే వేగం",
    takeaways: [
      { text: "TAKT = నెట్ అందుబాటు సమయం ÷ డిమాండ్", cue: "TAKT అంటే నెట్" },
      { text: "కావాల్సిన వేగం, స్టేషన్ సమయం కాదు", cue: "ఇది మీకు కావాల్సిన" },
      { text: "అసలు నష్టాలతో ప్లాన్, సిద్ధాంతంతో కాదు", cue: "మరియు అసలు నష్టాల" },
    ],
    action: { text: "ఒక లైన్ TAKT లెక్కించండి, దాన్ని మీ అత్యంత నెమ్మదైన స్టేషన్ తో పోల్చండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "U", title: "Uniform Production", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_TE_DURATION = PLAN.total;

export const TaktTimeTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
