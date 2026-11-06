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
import words from "../../captions/ct_te/words.json";

// Telugu version of CycleTimeStudyTe (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "అసలు పని కొలవండి, అసలు బాటిల్నెక్ కనుక్కోండి",
  outroLine: "నిర్వచనం. కొలత. పద్ధతిలో మెరుగుదల.",
  outroSub: "Cycle Time Study — వేగానికి ముందు రుజువు",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "సెకన్లు: ప్రతి స్టేషన్ తగినంత వేగంగా కనిపించింది",
    sub: "అయినా మానిటర్ లైన్ షిఫ్ట్ తర్వాత షిఫ్ట్ గంట టార్గెట్ అందుకోలేకపోయింది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "డిస్ప్లే-టెస్ట్ స్టేషన్ TAKT కంటే నెమ్మది", before: 28, after: 23, unit: "మానిటరుకు సెకన్లు, స్టేషన్ C లో", fixedLabel: "ఇప్పుడు TAKT లోపల",
    takeaways: [
      { text: "ముందు బౌండరీ నిర్ణయించండి", cue: "ముందు బౌండరీ" },
      { text: "సగటు మాత్రమే కాదు, వ్యాప్తి చూడండి", cue: "సగటు మాత్రమే" },
      { text: "పద్ధతి సరిచేయండి, క్వాలిటీ చెక్ ఎప్పుడూ వదలకండి", cue: "బాటిల్నెక్ వద్ద" },
    ],
    action: { text: "ఒక స్టేషన్లో పది సైకిళ్ళ సమయం కొలిచి, అతి పొడవైన దాన్ని TAKT తో పోల్చండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "D", title: "Design Thinking", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_TE_DURATION = PLAN.total;

export const CycleTimeStudyTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
