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
import words from "../../captions/kz_bn/words.json";

// Bengali version of KaizenBn (same design and polish as the English lesson).
// All data comes from narration/kaizen_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "ছোট বদল, প্রতিদিন, কাজ করা মানুষদের থেকে",
  outroLine: "দেখুন। ছোট চেষ্টা করুন। স্ট্যান্ডার্ড করুন। আবার করুন।",
  outroSub: "Kaizen — আজকের সেরা পদ্ধতি, কালকের বেসলাইন",
};

// Same polish as English Kaizen; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "বার প্রতিটি মনিটর উল্টানো হতো",
    sub: "মুখ নিচে, তারপর মুখ ওপরে। সবসময় এমনই হয়ে আসছিল।", until: "এই পাঠে",
  },
  recap: {
    problem: "মনিটর উল্টানো থেকে প্যানেলে স্ক্র্যাচ", before: 15, after: 3, unit: "প্রতি 1,000 মনিটরে স্ক্র্যাচ",
    fixedLabel: "90 দিনেও টিকে রইল",
    takeaways: [
      { text: "Kaizen রোজকার অভ্যাস", cue: "Kaizen রোজকার" },
      { text: "ছোট পরখ করুন; যাচাই করুন অন্য কিছু খারাপ হয়নি", cue: "ছোট পরিসরে" },
      { text: "প্রতিটি লাভের স্ট্যান্ডার্ড বানান", cue: "আর প্রতিটি লাভের" },
    ],
    action: { text: "একজন অপারেটরকে জিজ্ঞেস করুন তাঁর কাজে কষ্ট কোথায়, আর একটা ছোট সমাধান পরখ করুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "L", title: "Low Cost Automation", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_BN_DURATION = PLAN.total;

export const KaizenBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
