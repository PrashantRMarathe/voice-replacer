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
import words from "../../captions/mm_te/words.json";

// Telugu version of MudaMuraMuriTe (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "వేస్ట్, అసమానత, అధిక భారం — మూడూ సరిచేయండి",
  outroLine: "లెవెల్ చేయండి. కాపాడండి. తీసేయండి.",
  outroSub: "3M — స్థిరమైన ఫ్లో, వేగమైన మనుషులు కాదు",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "కెమెరాలు వెనకబడ్డాయి, షిఫ్ట్ ముగియడానికి ఒక గంట ముందు",
    sub: "అందరూ పరుగెడుతున్నారు. టెస్ట్ దగ్గర తప్పులు పేరుకుపోతున్నాయి.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "సంజయ్ లైన్ రోజూ ఆలస్యంగా నడిచేది", before: 150, after: 0, unit: "నిమిషాల ఓవర్‌టైమ్ రోజుకు",
    takeaways: [
      { text: "Muda వేస్ట్, Mura అసమానత, Muri అధిక భారం", cue: "Muda అంటే వేస్ట్" },
      { text: "ఇవి ఒకదాన్ని ఒకటి పెంచుతాయి: కలిపి సరిచేయండి", cue: "ఇవి ఒకదాన్ని ఒకటి" },
      { text: "స్థిరమైన ఫ్లో, వేగమైన మనుషులు కాదు", cue: "మరియు లక్ష్యం" },
    ],
    action: { text: "ఒక ప్రొడక్టుతో పాటు మీ లైన్ మొత్తం నడవండి, ప్రతి M కి ఒక ఉదాహరణ ట్యాగ్ చేయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "N", title: "Next Inspection", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_TE_DURATION = PLAN.total;

export const MudaMuraMuriTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
