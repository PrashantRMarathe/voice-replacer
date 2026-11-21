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
import words from "../../captions/qr_bn/words.json";

// Bengali version of QrqcBn (same design and polish as the English lesson).
// All data comes from narration/qrqc_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "মিনিটে পদক্ষেপ — প্রমাণ নিয়ে বন্ধ",
  outroLine: "ধরুন। আটকান। প্রমাণ করুন।",
  outroSub: "QRQC — দ্রুত রেসপন্স, আসল প্রমাণ",
};

// Same polish as English QRQC; cues are phrases from the Bengali intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "ক্যামেরা দুপুর পর্যন্ত ফোকাস টেস্টে ফেল",
    sub: "কেউ টেস্টার রিসেট করল, আর লাইন চলতে থাকল।", until: "এই পাঠে",
  },
  recap: {
    problem: "ওয়্যারহাউসের দিকে যাওয়া সন্দেহজনক ক্যামেরা", before: 2000, after: 0, unit: "হিসাব ছাড়া সন্দেহজনক ক্যামেরা",
    takeaways: [
      { text: "দ্রুত পদক্ষেপ, কিন্তু প্রমাণ নিয়ে", cue: "দ্রুত পদক্ষেপ" },
      { text: "আগে কনটেইনমেন্ট, প্রতিটি ইউনিটের হিসাব", cue: "আগে কনটেইনমেন্ট" },
      { text: "সমাধান প্রমাণিত হলেই বন্ধ করুন", cue: "আর কোনো সমস্যা" },
    ],
    action: { text: "কোনো একটি গুরুতর ডিফেক্টের জন্য আপনার রেসপন্স প্ল্যানের প্রথম 30 মিনিট লিখুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_BN_DURATION = PLAN.total;

export const QrqcBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
