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
import words from "../../captions/ni_te/words.json";

// Telugu version of NextInspectionTe (same design and polish as the English lesson).
// All data comes from narration/next_inspection_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "తర్వాతి ప్రాసెస్ నా కస్టమర్",
  outroLine: "తయారు చేయకండి. పంపకండి. స్వీకరించకండి.",
  outroSub: "Next Inspection — తర్వాతి ప్రాసెస్ ను కాపాడండి",
};

// Same polish as English NextInspection; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "వదులైన కనెక్టర్, స్టేషన్ మూడులో",
    sub: "ఎవరూ గమనించలేదు. తర్వాత ఒక కస్టమర్ బాక్స్ తెరిచారు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "తర్వాతి స్టేషన్ కు తప్పించుకునే డిఫెక్టులు", before: 18, after: 3, unit: "వారానికి ఎస్కేప్స్",
    takeaways: [
      { text: "తయారు చేయకండి, పంపకండి, స్వీకరించకండి", cue: "డిఫెక్ట్ తయారు చేయకండి" },
      { text: "త్వరగా చెక్ చేయండి, వేగంగా చర్య తీసుకోండి", cue: "ముఖ్యమైన పాయింట్లను వీలైనంత" },
      { text: "కంట్రోల్స్ ను పైకి జరుపుతూ ఉండండి", cue: "మరియు మీ కంట్రోల్స్" },
    ],
    action: { text: "ఒక హ్యాండాఫ్ ఎంచుకోండి, తర్వాతి ప్రాసెస్ కు దాని నుండి ఏం కావాలో రాయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "O", title: "One Point Lesson", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_TE_DURATION = PLAN.total;

export const NextInspectionTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
