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
import words from "../../captions/ni_bn/words.json";

// Bengali version of NextInspectionBn (same design and polish as the English lesson).
// All data comes from narration/next_inspection_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "পরের প্রসেস আমার গ্রাহক",
  outroLine: "বানাবেন না। পাঠাবেন না। নেবেন না।",
  outroSub: "Next Inspection — পরের প্রসেসকে বাঁচান",
};

// Same polish as English NextInspection; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "ঢিলে কানেক্টর, তিন নম্বর স্টেশনে",
    sub: "কেউ খেয়াল করেনি। তারপর একজন গ্রাহক বাক্স খুললেন।", until: "এই পাঠে",
  },
  recap: {
    problem: "পরের স্টেশনে বেরিয়ে যাওয়া ডিফেক্ট", before: 18, after: 3, unit: "প্রতি সপ্তাহে এস্কেপ",
    takeaways: [
      { text: "বানাবেন না, পাঠাবেন না, নেবেন না", cue: "ডিফেক্ট বানাবেন না" },
      { text: "তাড়াতাড়ি যাচাই করুন, দ্রুত পদক্ষেপ নিন", cue: "জরুরি পয়েন্ট যত" },
      { text: "কন্ট্রোল ওপরের দিকে সরাতে থাকুন", cue: "আর আপনার কন্ট্রোলকে" },
    ],
    action: { text: "একটা হ্যান্ডঅফ বাছুন, আর লিখুন পরের প্রসেসের তা থেকে কী দরকার।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "O", title: "One Point Lesson", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_BN_DURATION = PLAN.total;

export const NextInspectionBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
