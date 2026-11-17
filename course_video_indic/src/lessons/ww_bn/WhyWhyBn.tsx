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
import words from "../../captions/ww_bn/words.json";

// Bengali version of WhyWhyBn (same design and polish as the English lesson).
// All data comes from narration/why_why_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "সহজ উত্তর পেরিয়ে, এমন কারণ পর্যন্ত যা আপনি প্রমাণ করতে পারেন",
  outroLine: "সংজ্ঞায়িত করুন। প্রমাণ করুন। আটকান।",
  outroSub: "Why–Why — কারণ ঠিক করুন, মানুষ নয়",
};

// Same polish as English WhyWhy; cues are phrases from the Bengali intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "ফোন ফাইনাল টেস্টে চার্জিংয়ে ফেল",
    sub: "প্রথম উত্তর: অপারেটরের ভুল। দুই দিন পরে, আবার সেই একই জিনিস।", until: "এই পাঠে",
  },
  recap: {
    problem: "লাইন 2 এ চার্জিং ফেলিওর", before: 50, after: 15, unit: "চার্জিং ডিফেক্ট, একই ভলিউম",
    fixedLabel: "রুট কজ ঠিক: 70% কম",
    takeaways: [
      { text: "আগে ধারালো সমস্যা, তারপর কনটেইনমেন্ট", cue: "একটা ধারালো সমস্যা" },
      { text: "প্রতিটি কেনর প্রমাণ, তারপর যাচাই", cue: "প্রতিটি কেনর পেছনে" },
      { text: "কীভাবে ঘটল আর কেন বেরোল, দুটোই ঠিক করুন", cue: "আর দুটোই ঠিক" },
    ],
    action: { text: "বারবার হওয়া একটা ডিফেক্ট নিন, আর তার 5W2H স্টেটমেন্ট লিখুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "X", title: "X-Matrix", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_BN_DURATION = PLAN.total;

export const WhyWhyBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
