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
import words from "../../captions/gb_bn/words.json";

// Bengali version of GembaBn (same design and polish as the English lesson).
// All data comes from narration/gemba_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "আসল জায়গা, আসল জিনিস, আসল তথ্য",
  outroLine: "যান। দেখুন। নিশ্চিত করুন।",
  outroSub: "Gemba, Genbutsu, Genjitsu — সিদ্ধান্তের আগে তথ্য",
};

// Same polish as English Gemba; cues are phrases from the Bengali intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× ইয়ারবাড ফেলিওর, শিফট B তে",
    sub: "প্ল্যান: শিফট B কে আবার ট্রেনিং। কেউ একটা ফেল ইয়ারবাডও দেখেনি।", until: "এই পাঠে",
  },
  recap: {
    problem: "অডিও টেস্টে ফেল করা ইয়ারবাড", before: 20, after: 8, unit: "প্রতি 1,000 ইয়ারবাডে ফেলিওর",
    fixedLabel: "কারণে ঠিক করা হলো",
    takeaways: [
      { text: "আসল জায়গায় যান; আসল সাইকেল দেখুন", cue: "আসল জায়গায় যান" },
      { text: "আসল জিনিস হাতে নিন; ভালোর সঙ্গে তুলনা করুন", cue: "আসল জিনিস হাতে" },
      { text: "আসল তথ্য যাচাই করুন, হর সহ", cue: "আর আসল তথ্য" },
    ],
    action: { text: "বারবার ফিরে আসা একটা সমস্যা নিন, আর তিরিশ মিনিটের একটা 3G ভিজিট করুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "H", title: "Hancho", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_BN_DURATION = PLAN.total;

export const GembaBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
