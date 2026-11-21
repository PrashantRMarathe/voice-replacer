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
import words from "../../captions/sk_te/words.json";

// Telugu version of SkillMatrixTe (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "నిజంగా ఎవరు ఏ పని చేయగలరు — గ్యాప్స్ ఎక్కడ ఉన్నాయి",
  outroLine: "అసెస్ చేయండి. ట్రైనింగ్ ఇవ్వండి. కవర్ చేయండి.",
  outroSub: "Skill Matrix — సామర్థ్యానికి సజీవ కంట్రోల్",
};

// Same polish as English SkillMatrix; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "లెన్స్ ఫోకస్ సెట్ చేయగల వ్యక్తి",
    sub: "బాలా అనారోగ్యంతో ఉన్నాడు. పది గంటలకల్లా, మొత్తం సెల్ ఆగిపోయింది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "ఒకే లెన్స్ ఫోకస్ ఎక్స్‌పర్ట్, అతను అనారోగ్యంతో", before: 1, after: 2, unit: "అర్హులైన లెన్స్ ఫోకస్ ఎక్స్‌పర్ట్",
    takeaways: [
      { text: "నిరూపించిన సామర్థ్యం, హాజరు కాదు", cue: "స్కిల్ మ్యాట్రిక్స్ నిరూపించిన" },
      { text: "ప్రతి షిఫ్టులో అర్హులైన బ్యాకప్ లను లెక్కించండి", cue: "ప్రతి ముఖ్యమైన పనికి" },
      { text: "దీన్ని సజీవంగా ఉంచండి, సాక్ష్యంతో", cue: "మరియు దీన్ని సజీవంగా" },
    ],
    action: { text: "మీ మూడు అత్యంత ముఖ్యమైన స్టేషన్లు రాయండి, ప్రతి దానికీ అర్హులైన మనుషులను లెక్కించండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "T", title: "TAKT Time", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_TE_DURATION = PLAN.total;

export const SkillMatrixTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
