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
import words from "../../captions/xm_bn/words.json";

// Bengali version of XMatrixBn (same design and polish as the English lesson).
// All data comes from narration/x_matrix_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Hoshin Kanri দিয়ে কৌশলকে অ্যাকশনে বদলান",
  outroLine: "জুড়ুন। চালু করুন। রিভিউ করুন।",
  outroSub: "X-Matrix — এমন কৌশল, যা আপনি সত্যিই চালু করতে পারেন",
};

// Same polish as English XMatrix; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "ইমপ্রুভমেন্ট প্রজেক্ট, প্রতিটি টিম ব্যস্ত",
    sub: "তবুও ডেলিভারি প্রতি তিন মাসে পিছলে যাচ্ছিল।", until: "এই পাঠে",
  },
  recap: {
    problem: "ব্যস্ত পোর্টফোলিও, পিছলে যাওয়া ডেলিভারি", before: 40, after: 3, unit: "প্রজেক্ট, প্রতিটি কোনো লক্ষ্য আর KPI এর সঙ্গে যুক্ত",
    fixedLabel: "ফোকাসড পোর্টফোলিও",
    takeaways: [
      { text: "কয়েকটা আসল অগ্রাধিকার, ইচ্ছের তালিকা নয়", cue: "কয়েকটা আসল অগ্রাধিকার" },
      { text: "লক্ষ্য → প্রজেক্ট → KPI → একজন ওনার", cue: "প্রতিটি লক্ষ্যকে" },
      { text: "সৎ রিভিউ: সংখ্যা নড়া উচিত", cue: "আর সৎভাবে" },
    ],
    action: { text: "আপনার এরিয়ার জন্য একটা উদ্দেশ্য লিখুন, ফল হিসেবে, কাজ হিসেবে নয়।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "Y", title: "Yamazumi", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_BN_DURATION = PLAN.total;

export const XMatrixBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
