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
import words from "../../captions/yz_bn/words.json";

// Bengali version of YamazumiBn (same design and polish as the English lesson).
// All data comes from narration/yamazumi_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "আসল ডেটা দিয়ে, TAKT এর সামনে লাইন ব্যালান্স করুন",
  outroLine: "মাপুন। সাজান। ব্যালান্স করুন।",
  outroSub: "Yamazumi — এমন ফ্লো, যা ডিজাইনেই টেকে",
};

// Same polish as English Yamazumi; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "অপারেটর অপেক্ষায়, যখন একজন স্ক্রুর কাজে চাপা",
    sub: "কেউ অলস নন। কাজটা শুধু অসমানভাবে জমে আছে।", until: "এই পাঠে",
  },
  recap: {
    problem: "স্টেশন B, TAKT এর ওপরে", before: 35, after: 30, unit: "স্টেশন B তে কাজের সেকেন্ড",
    fixedLabel: "তারপর TAKT এ",
    takeaways: [
      { text: "আসল কাজ মাপুন, সবচেয়ে ভালো কেস নয়", cue: "আসল কাজ মাপুন" },
      { text: "TAKT এর সামনে সাজান, স্তূপ দেখুন", cue: "সেটা TAKT এর সামনে" },
      { text: "সেফটি বা কোয়ালিটি বাজি না রেখে ব্যালান্স", cue: "আর সাবধানে" },
    ],
    action: { text: "আপনার লাইনের একটা স্টেশনের সময় মাপুন, আর TAKT এর সামনে তার বার বানান।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "Z", title: "Zero Defects", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_BN_DURATION = PLAN.total;

export const YamazumiBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
