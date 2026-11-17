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
import words from "../../captions/pk_bn/words.json";

// Bengali version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "ভুল কাজকে অসম্ভব করুন",
  outroLine: "সরান। আটকান। ধরুন।",
  outroSub: "Poka Yoke — কোয়ালিটিকে স্মৃতির ভরসা থেকে বের করুন",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_BN_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "রেকর্ডার একটি স্ক্রু ছাড়াই পাঠানো হয়েছিল",
    sub: "অপারেটর দক্ষ আর সতর্ক ছিলেন। শুধু মানুষ।", until: "এই পাঠে",
  },
  recap: {
    problem: "হারানো স্ক্রু সহ রেকর্ডার পাঠানো হয়েছিল", before: 18, after: 1, unit: "প্রতি 10,000 ইউনিটে",
    takeaways: [
      { text: "ভুল আন্দাজ করা যায়: ডিজাইন দিয়ে সরিয়ে দিন", cue: "ভুল আগে থেকে আন্দাজ" },
      { text: "আগে আটকান, তারপর ধরুন, তারপর সতর্ক করুন", cue: "সতর্ক করার চেয়ে" },
      { text: "প্রতিটি ডিভাইসকে খারাপ স্যাম্পল দিয়ে পরীক্ষা করুন", cue: "আর প্রতিটি ডিভাইসকে" },
    ],
    action: { text: "স্মৃতির ওপর নির্ভর একটা চেক খুঁজুন, আর তার জন্য Poka Yoke এর স্কেচ বানান।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "Q", title: "QRQC", cue: "এরপর, আপনি QRQC" },
  },
};

export const PokaYokeBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
