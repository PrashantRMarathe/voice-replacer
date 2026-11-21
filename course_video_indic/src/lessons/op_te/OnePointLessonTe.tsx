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
import words from "../../captions/op_te/words.json";

// Telugu version of OnePointLessonTe (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "ఒక అంశం. ఒక స్పష్టమైన పాయింట్. ఒక మెరుగైన పని.",
  outroLine: "సులభం. విజువల్. సరైనది.",
  outroSub: "One Point Lesson — ఒక పాయింట్ బాగా నేర్పండి",
};

// Same polish as English OnePointLesson; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "కనెక్టర్ తలకిందులుగా పెట్టారు, అది విరిగింది",
    sub: "డే షిఫ్ట్ కు పద్ధతి తెలుసు. ఎవరూ చెప్పలేదు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "నైట్ షిఫ్ట్ లో విరిగే కనెక్టర్లు", before: 14, after: 1, unit: "వారానికి విరిగిన కనెక్టర్లు",
    takeaways: [
      { text: "ఒక అంశం, ఒక పాయింట్, ఒక బలమైన విజువల్", cue: "ఒక అంశం" },
      { text: "Gemba లో నేర్పండి, తర్వాత పని చూడండి", cue: "దీన్ని Gemba లో" },
      { text: "ప్రస్తుత స్టాండర్డ్ తో సరిపోయేలా ఉంచండి", cue: "మరియు దీన్ని కంట్రోల్" },
    ],
    action: { text: "పదే పదే జరిగే ఒక తప్పును ఎంచుకోండి, దాని కోసం One Point Lesson డ్రాఫ్ట్ చేయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "P", title: "Poka Yoke", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_TE_DURATION = PLAN.total;

export const OnePointLessonTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
