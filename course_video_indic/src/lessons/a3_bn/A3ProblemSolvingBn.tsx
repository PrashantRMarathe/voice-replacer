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
import words from "../../captions/a3_bn/words.json";

// Bengali version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "সমস্যার পুরো গল্প, এক পাতায়",
  outroLine: "গ্যাপ দেখুন। কারণ প্রমাণ করুন। টিকিয়ে রাখুন।",
  outroSub: "A3 — ভালো চিন্তা, এক শিটে",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_BN_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "সার্ভার তাদের প্রথম বুট টেস্টে ফেল",
    sub: "চার সপ্তাহে। প্রথম প্রস্তাবিত সমাধান: আরও দুজন ইন্সপেক্টর।", until: "এই পাঠে",
  },
  recap: {
    problem: "প্রথম বুট টেস্টে ফেল করা সার্ভার", before: 48, after: 16, unit: "প্রতি 1,000 সার্ভারে", fixedLabel: "টার্গেট পূরণ: 48 এর নিচে",
    takeaways: [
      { text: "একটা মাপা যায় এমন গ্যাপ দিয়ে শুরু করুন", cue: "শুরু করুন একটা মাপা" },
      { text: "গিয়ে দেখুন; প্রতিটি কারণ প্রমাণ করুন", cue: "গিয়ে দেখুন" },
      { text: "শুধু পাইলটে প্রমাণিত জিনিসের স্ট্যান্ডার্ড", cue: "আর শুধু সেটাই" },
    ],
    action: { text: "বারবার ফিরে আসা একটা সমস্যা বাছুন, আর তার প্রবলেম স্টেটমেন্ট A3 তে লিখুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "B", title: "Burn Down Chart", cue: "এরপর, আপনি" },
  },
};

export const A3ProblemSolvingBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
