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
import words from "../../captions/yz_te/words.json";

// Telugu version of YamazumiTe (same design and polish as the English lesson).
// All data comes from narration/yamazumi_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "అసలు డేటాతో, TAKT ఎదుట లైన్ బ్యాలెన్స్ చేయండి",
  outroLine: "కొలవండి. పేర్చండి. బ్యాలెన్స్ చేయండి.",
  outroSub: "Yamazumi — డిజైన్ తో నిలిచే ఫ్లో",
};

// Same polish as English Yamazumi; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "ఆపరేటర్లు వేచి ఉన్నారు, ఒకరు స్క్రూలలో మునిగి ఉన్నారు",
    sub: "ఎవరూ సోమరి కాదు. పని కేవలం అసమానంగా పేరుకుపోయింది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "స్టేషన్ B, TAKT కంటే పైన", before: 35, after: 30, unit: "స్టేషన్ B లో పని సెకన్లు",
    fixedLabel: "తర్వాత TAKT దగ్గర",
    takeaways: [
      { text: "అసలు పనిని కొలవండి, అత్యుత్తమ కేస్ కాదు", cue: "అసలు పనిని కొలవండి" },
      { text: "TAKT ఎదుట పేర్చండి, కుప్ప చూడండి", cue: "దాన్ని TAKT ఎదుట" },
      { text: "సేఫ్టీ లేదా క్వాలిటీని పణంగా పెట్టకుండా బ్యాలెన్స్", cue: "మరియు జాగ్రత్తగా" },
    ],
    action: { text: "మీ లైన్లో ఒక స్టేషన్ సమయం కొలవండి, TAKT ఎదుట దాని బార్ గీయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "Z", title: "Zero Defects", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_TE_DURATION = PLAN.total;

export const YamazumiTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
