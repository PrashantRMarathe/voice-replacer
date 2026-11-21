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
import words from "../../captions/jd_bn/words.json";

// Bengali version of JidokaBn (same design and polish as the English lesson).
// All data comes from narration/jidoka_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "মানুষের ছোঁয়া সহ অটোমেশন",
  outroLine: "দেখুন। থামান। সমাধান করুন।",
  outroSub: "Jidoka — কোনো ডিফেক্ট সামনে নয়, কোনো গোলমাল লুকানো নয়",
};

// Same polish as English Jidoka; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "পেশেন্ট মনিটরে পাতলা সিল",
    sub: "ডিসপেন্সার সারা রাত দারুণ চলল। তার নজল অর্ধেক বন্ধ ছিল।", until: "এই পাঠে",
  },
  recap: {
    problem: "বন্ধ অ্যাডহেসিভ নজল থেকে পাতলা সিল", before: 140, after: 1, unit: "মনিটরে প্রভাব, প্রতি নজল সমস্যায়",
    fixedLabel: "উৎসেই ধরা পড়ল",
    takeaways: [
      { text: "আগে স্বাভাবিক ঠিক করুন", cue: "আগে স্বাভাবিক" },
      { text: "ধরুন, থামান, কন্টেন করুন: কোনো ডিফেক্ট সামনে নয়", cue: "উৎসেই ধরুন" },
      { text: "প্রতিটি থামা একটা শিক্ষা: রুট কজ ঠিক করুন", cue: "আর প্রতিটি থামাকে" },
    ],
    action: { text: "একটা অটোমেটিক প্রসেস বাছুন, আর লিখুন কীসে তার থামা উচিত।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "K", title: "Kaizen", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_BN_DURATION = PLAN.total;

export const JidokaBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
