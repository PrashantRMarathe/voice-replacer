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
import words from "../../captions/zd_bn/words.json";

// Bengali version of ZeroDefectsBn (same design and polish as the English lesson).
// All data comes from narration/zero_defects_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "ডিফেক্ট আটকান — শুধু তাদের যাচাই করবেন না",
  outroLine: "আটকান। মাপুন। উন্নত করুন।",
  outroSub: "Zero Defects — রোজের ম্যানেজমেন্টে যুক্ত",
};

// Same polish as English ZeroDefects; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "ফোন রিওয়ার্কের জন্য ফিরে এল",
    sub: "একটা কানেক্টর, ভুলভাবে বসানো। সেটা প্রতিটি ভিজ্যুয়াল চেকে পাস করল।", until: "এই পাঠে",
  },
  recap: {
    problem: "ভুলভাবে বসা কানেক্টর থেকে চার্জিং ফেলিওর", before: 1200, after: 200,
    unit: "ফেল ফোন, 40,000 এর মধ্যে", fixedLabel: "পুনরাবৃত্তি কঠিন: 83% কম",
    takeaways: [
      { text: "ডিফেক্ট আটকান, শুধু যাচাই নয়", cue: "ডিফেক্ট আটকান" },
      { text: "পরিষ্কার সংজ্ঞা সহ সৎভাবে মাপুন", cue: "পরিষ্কার সংজ্ঞা সহ" },
      { text: "সিস্টেম ঠিক করুন, মানুষকে নয়", cue: "আর যখন কিছু ফেল" },
    ],
    action: { text: "বারবার ফিরে আসা একটা ডিফেক্ট বাছুন, আর জিজ্ঞেস করুন তাকে অসম্ভব কীভাবে করবেন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "Z", title: "Zero Defects", kicker: "পাঠটি শেষ", cue: "এবার যান" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_BN_DURATION = PLAN.total;

export const ZeroDefectsBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
