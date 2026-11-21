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
import words from "../../captions/tt_bn/words.json";

// Bengali version of TaktTimeBn (same design and polish as the English lesson).
// All data comes from narration/takt_time_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "সেই হৃৎস্পন্দন যা আপনার গ্রাহক ঠিক করেন",
  outroLine: "মাপুন। ব্যালান্স করুন। ফ্লো তৈরি করুন।",
  outroSub: "TAKT Time — গ্রাহকের গতি",
};

// Same polish as English TaktTime; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "টেস্টের আগে ক্যামেরা বানিয়ে ফেলা",
    sub: "প্রতিটি স্টেশন ব্যস্ত। ট্রাক তবুও লেট বেরোল।", until: "এই পাঠে",
  },
  recap: {
    problem: "ব্যস্ত লাইন, তবুও ট্রাক মিস", before: 0, after: 10, unit: "সেকেন্ড: রোজ 7,200 ক্যামেরার হৃৎস্পন্দন",
    fixedLabel: "সেই গতি যাতে সবাই চলে",
    takeaways: [
      { text: "TAKT = নেট উপলব্ধ সময় ÷ ডিমান্ড", cue: "TAKT মানে নেট" },
      { text: "যে গতি দরকার, স্টেশনের সময় নয়", cue: "এটা সেই গতি" },
      { text: "আসল ক্ষতি ধরে প্ল্যান, তত্ত্ব ধরে নয়", cue: "আর আসল ক্ষতি" },
    ],
    action: { text: "একটা লাইনের TAKT বের করুন, আর আপনার সবচেয়ে ধীর স্টেশনের সঙ্গে তার তুলনা করুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "U", title: "Uniform Production", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_BN_DURATION = PLAN.total;

export const TaktTimeBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
