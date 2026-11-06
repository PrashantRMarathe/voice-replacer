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
import words from "../../captions/qr_te/words.json";

// Telugu version of QrqcTe (same design and polish as the English lesson).
// All data comes from narration/qrqc_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "నిమిషాల్లో చర్య — సాక్ష్యంతో మూసివేత",
  outroLine: "పట్టుకోండి. ఆపండి. నిరూపించండి.",
  outroSub: "QRQC — వేగమైన రెస్పాన్స్, నిజమైన సాక్ష్యం",
};

// Same polish as English QRQC; cues are phrases from the Telugu intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "మధ్యాహ్నానికి కెమెరాలు ఫోకస్ టెస్టులో ఫెయిల్",
    sub: "ఎవరో టెస్టర్ ను రీసెట్ చేశారు, లైన్ నడుస్తూనే ఉంది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "వేర్‌హౌస్ వైపు వెళ్తున్న అనుమానిత కెమెరాలు", before: 2000, after: 0, unit: "లెక్క తేలని అనుమానిత కెమెరాలు",
    takeaways: [
      { text: "వేగంగా చర్య, కానీ సాక్ష్యంతో", cue: "వేగంగా చర్య తీసుకోండి" },
      { text: "ముందు కంటైన్‌మెంట్, ప్రతి యూనిట్ లెక్క", cue: "ముందు కంటైన్‌మెంట్" },
      { text: "పరిష్కారం నిరూపించాకే మూసేయండి", cue: "మరియు ఏ సమస్యనైనా" },
    ],
    action: { text: "ఏదైనా ఒక తీవ్రమైన డిఫెక్ట్ కోసం మీ రెస్పాన్స్ ప్లాన్ లో మొదటి 30 నిమిషాలు రాయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_TE_DURATION = PLAN.total;

export const QrqcTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
