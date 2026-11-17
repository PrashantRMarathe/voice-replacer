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
import words from "../../captions/lc_bn/words.json";

// Bengali version of LowCostAutomationBn (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "কাজ করে এমন সবচেয়ে সরল নিরাপদ ডিভাইস",
  outroLine: "সহজ করুন। দরকার অটোমেট করুন। প্রমাণ করুন।",
  outroSub: "Low Cost Automation — কখনও কম সেফটি নয়",
};

// Same polish as English LowCostAutomation; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "ঘণ্টায় ম্যালেটের ঠোকা, প্রত্যেক অপারেটর",
    sub: "ব্যথা হওয়া কবজি, আর টেস্টে খড়খড় করা ঢিলে গ্রিল।", until: "এই পাঠে",
  },
  recap: {
    problem: "ম্যালেট দিয়ে বসানোয় ঢিলে স্পিকার গ্রিল", before: 18, after: 2, unit: "প্রতি 1,000 স্পিকারে",
    fixedLabel: "4 মাসে ফেরত",
    takeaways: [
      { text: "আগে সহজ করুন; ওয়েস্ট কখনও অটোমেট নয়", cue: "আগে সহজ করুন" },
      { text: "সবচেয়ে সরল নিরাপদ সমাধান; সেফটি প্রথম গেট", cue: "এমন সবচেয়ে সরল" },
      { text: "আসল লাভ প্রমাণ করুন, তারপর রক্ষণাবেক্ষণ", cue: "আর আসল লাভ" },
    ],
    action: { text: "পুনরাবৃত্তির একটা নড়াচড়া খুঁজুন, আর জিজ্ঞেস করুন অটোমেট করার আগে তা সরানো যায় কি না।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_BN_DURATION = PLAN.total;

export const LowCostAutomationBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
