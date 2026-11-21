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
import words from "../../captions/bd_bn/words.json";

// Bengali version of BurnDownChartBn (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "ডেডলাইনের আগে বাকি কাজ দেখুন",
  outroLine: "লাইন ঠিক করুন। গ্যাপ দেখুন। আজই পদক্ষেপ নিন।",
  outroSub: "Burn Down Chart — আর শুক্রবারের ধাক্কা নয়",
};

// Same polish as English BurnDownChart; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "রাউটার ট্রাক থেকে বাদ পড়ল",
    sub: "শুক্রবার দুপুর পর্যন্ত কেউ টেরও পায়নি।", until: "এই পাঠে",
  },
  recap: {
    problem: "ডিসপ্যাচে কম পড়া রাউটার", before: 80, after: 0, unit: "রাউটার কম",
    takeaways: [
      { text: "আগে আইডিয়াল লাইন; তা আর কখনও নয়", cue: "আগে আইডিয়াল লাইন" },
      { text: "শুধু শেষ আর ভালো কাজ গুনুন", cue: "শুধু সেই কাজ" },
      { text: "আইডিয়ালের ওপরে? সেদিনই পদক্ষেপ, ওনার সহ", cue: "আর যখন লাইন" },
    ],
    action: { text: "ডেডলাইন আছে এমন একটা কাজ বাছুন, আর কালকের শিফটের আগে তার বার্ন-ডাউন বানান।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "C", title: "Cycle Time Study", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_BN_DURATION = PLAN.total;

export const BurnDownChartBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
