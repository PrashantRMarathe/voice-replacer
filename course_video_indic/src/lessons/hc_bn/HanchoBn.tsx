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
import words from "../../captions/hc_bn/words.json";

// Bengali version of HanchoBn (same design and polish as the English lesson).
// All data comes from narration/hancho_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "শপ-ফ্লোর নেতৃত্ব, প্রতিটি শিফটের প্রতিটি ঘণ্টায়",
  outroLine: "Gemba তে নেতৃত্ব দিন। মানুষকে তৈরি করুন।",
  outroSub: "Hancho — স্ট্যান্ডার্ড ফেরান, প্রতিদিন উন্নতি করুন",
};

// Same polish as English Hancho; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "প্রতি ঘণ্টায় TV কম, পুরো একটা শিফট ধরে",
    sub: "পরের দিন সকালের রিপোর্টের আগে কেউ জানতে পারেনি।", until: "এই পাঠে",
  },
  recap: {
    problem: "মডেল চেঞ্জের পর আউটপুট গ্যাপ", before: 98, after: 120, unit: "প্রতি ঘণ্টায় TV",
    fixedLabel: "সেই শিফটেই ফিরল",
    takeaways: [
      { text: "Gemba থেকে নেতৃত্ব: স্ট্যান্ডার্ড বনাম আসল", cue: "Gemba থেকে নেতৃত্ব" },
      { text: "গ্যাপ প্রতি ঘণ্টায় দেখান; সেই শিফটেই পদক্ষেপ", cue: "প্রতিটি গ্যাপ" },
      { text: "মানুষকে তৈরি করুন, যাতে লাইন আপনার ওপর না দাঁড়ায়", cue: "আর আপনার লোকদের" },
    ],
    action: { text: "একটা শিফটের জন্য আপনার লিডার স্ট্যান্ডার্ড ওয়ার্ক লিখুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_BN_DURATION = PLAN.total;

export const HanchoBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
