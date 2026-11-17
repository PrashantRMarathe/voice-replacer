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
import words from "../../captions/op_bn/words.json";

// Bengali version of OnePointLessonBn (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "একটা বিষয়। একটা স্পষ্ট পয়েন্ট। একটা ভালো কাজ।",
  outroLine: "সহজ। ভিজ্যুয়াল। সঠিক।",
  outroSub: "One Point Lesson — একটা পয়েন্ট ভালোভাবে শেখান",
};

// Same polish as English OnePointLesson; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "কানেক্টর উল্টো লাগল, আর ভাঙল",
    sub: "ডে শিফট কৌশল জানত। কেউ বলেনি।", until: "এই পাঠে",
  },
  recap: {
    problem: "নাইট শিফটে ভাঙা কানেক্টর", before: 14, after: 1, unit: "প্রতি সপ্তাহে ভাঙা কানেক্টর",
    takeaways: [
      { text: "একটা বিষয়, একটা পয়েন্ট, একটা জোরালো ভিজ্যুয়াল", cue: "একটা বিষয়" },
      { text: "Gemba তে শেখান, তারপর কাজ দেখুন", cue: "এটা Gemba তে" },
      { text: "এটা বর্তমান স্ট্যান্ডার্ডের সঙ্গে মিলিয়ে রাখুন", cue: "আর এটা নিয়ন্ত্রণে" },
    ],
    action: { text: "বারবার হওয়া একটা ভুল বাছুন, আর তার জন্য One Point Lesson এর খসড়া বানান।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "P", title: "Poka Yoke", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_BN_DURATION = PLAN.total;

export const OnePointLessonBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
