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
import words from "../../captions/vs_bn/words.json";

// Bengali version of ValueStreamMappingBn (same design and polish as the English lesson).
// All data comes from narration/value_stream_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "অর্ডার থেকে ডেলিভারি, পুরো ফ্লো দেখুন",
  outroLine: "দেখুন। মাপুন। ফ্লো তৈরি করুন।",
  outroSub: "Value Stream Mapping — অপেক্ষা খুঁজুন, ফ্লো ডিজাইন করুন",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "মিনিট, একটা সেট-টপ বক্স বানাতে আর টেস্ট করতে",
    sub: "তবুও গ্রাহকের কাছে পৌঁছাতে প্রায় চার দিন।", until: "এই পাঠে",
  },
  recap: {
    problem: "মিনিটের কাজের জন্য দিনের অপেক্ষা", before: 4200, after: 2100, unit: "তিনটি বাফারে অপেক্ষায় থাকা ইউনিট",
    fixedLabel: "ফিউচার স্টেট: অর্ধেক অপেক্ষা",
    takeaways: [
      { text: "আসল ম্যাটেরিয়াল + তথ্য ফ্লোর ম্যাপ", cue: "আসল ফ্লোর ম্যাপ" },
      { text: "লিড টাইম লুকিয়ে আছে অপেক্ষায়, কাজে নয়", cue: "আপনার বেশিরভাগ লিড" },
      { text: "স্টক কমানোর আগে ফিউচার স্টেট প্রমাণ করুন", cue: "আর কোনো স্টক" },
    ],
    action: { text: "একটা প্রোডাক্ট ফ্যামিলি নিয়ে ডিসপ্যাচ থেকে উল্টো হাঁটুন, আর প্রতিটি স্তূপ গুনুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_BN_DURATION = PLAN.total;

export const ValueStreamMappingBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
