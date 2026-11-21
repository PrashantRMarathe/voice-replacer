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
import words from "../../captions/ct_bn/words.json";

// Bengali version of CycleTimeStudyBn (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "আসল কাজ মাপুন, আসল বটলনেক খুঁজুন",
  outroLine: "সংজ্ঞা। মাপ। পদ্ধতির উন্নতি।",
  outroSub: "Cycle Time Study — গতির আগে প্রমাণ",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "সেকেন্ড: প্রতিটি স্টেশন যথেষ্ট দ্রুত দেখাত",
    sub: "তবুও মনিটর লাইন শিফটের পর শিফট ঘণ্টার টার্গেট ফসকাতে থাকল।", until: "এই পাঠে",
  },
  recap: {
    problem: "ডিসপ্লে-টেস্ট স্টেশন TAKT এর চেয়ে ধীর", before: 28, after: 23, unit: "প্রতি মনিটরে সেকেন্ড, স্টেশন C তে", fixedLabel: "এখন TAKT এর মধ্যে",
    takeaways: [
      { text: "আগে বাউন্ডারি ঠিক করুন", cue: "আগে বাউন্ডারি" },
      { text: "শুধু গড় নয়, ছড়ানো দেখুন", cue: "শুধু গড় নয়" },
      { text: "পদ্ধতি ঠিক করুন, কোয়ালিটি চেক কখনও বাদ নয়", cue: "আর বটলনেকে" },
    ],
    action: { text: "একটা স্টেশনে দশটা সাইকেল মাপুন, আর সবচেয়ে লম্বাটার তুলনা TAKT এর সঙ্গে করুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "D", title: "Design Thinking", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_BN_DURATION = PLAN.total;

export const CycleTimeStudyBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
