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
import words from "../../captions/fm_bn/words.json";

// Bengali version of FMEABn (same design and polish as the English lesson).
// All data comes from narration/fmea_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "ফেলিওর মোড অ্যান্ড এফেক্টস অ্যানালিসিস: ফেলিওরের আগে ভাবুন",
  outroLine: "চেইন বানান। স্কোর দিন। আটকান।",
  outroSub: "FMEA — একটা জীবন্ত প্ল্যান, ফর্ম নয়",
};

// Same polish as English FMEA; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "আউটডোর রেডিও জলে ভরে ফিরল",
    sub: "দুটোয় গ্যাসকেট নেই, চারটেয় ভাঁজ। সবই ফাইনাল ইন্সপেকশনে পাস ছিল।", until: "এই পাঠে",
  },
  recap: {
    problem: "আউটডোর 5G রেডিওতে গ্যাসকেটের ঝুঁকি", before: 240, after: 32, unit: "রিস্ক প্রায়োরিটি নম্বর",
    fixedLabel: "ঝুঁকি কমল, ট্রায়ালে প্রমাণিত",
    takeaways: [
      { text: "প্রভাব → ফেলিওর মোড → নিয়ন্ত্রণযোগ্য কারণ", cue: "একটা স্পষ্ট চেইন" },
      { text: "প্রমাণ দিয়ে স্কোর; নম্বরের ওপরে বোঝা", cue: "প্রমাণ সহ" },
      { text: "আগে প্রতিরোধ, প্রমাণ করুন, তারপর আবার স্কোর", cue: "আর প্রতিরোধ বাছুন" },
    ],
    action: { text: "একটা জরুরি ধাপ বাছুন, আর আপনার টিমের সঙ্গে তার ফেলিওর চেইন লিখুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "G", title: "Gemba", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_BN_DURATION = PLAN.total;

export const FMEABn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
