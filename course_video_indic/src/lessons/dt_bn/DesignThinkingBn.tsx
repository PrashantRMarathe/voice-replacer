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
import words from "../../captions/dt_bn/words.json";

// Bengali version of DesignThinkingBn (same design and polish as the English lesson).
// All data comes from narration/design_thinking_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "সঠিক সমস্যা সমাধান করুন, কাজ করা মানুষদের সঙ্গে",
  outroLine: "দেখুন। সংজ্ঞায়িত করুন। ছোট পরখ করুন।",
  outroSub: "Design Thinking — আগে মানুষ, সবসময় প্রমাণ",
};

// Same polish as English DesignThinking; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "প্রতি 1,000 পাম্পে লেবেলের ভুল",
    sub: "প্রথম আইডিয়া: একটা দামি দ্রুত প্রিন্টার। প্যাকারদের কেউ জিজ্ঞেসই করেনি।", until: "এই পাঠে",
  },
  recap: {
    problem: "ইনফিউশন পাম্প প্যাকিংয়ে লেবেলের ভুল", before: 12, after: 2, unit: "প্রতি 1,000 পাম্পে",
    takeaways: [
      { text: "মানুষ দিয়ে শুরু করুন; সিদ্ধান্তের আগে দেখুন", cue: "কাজ করা মানুষদের দিয়ে" },
      { text: "দরকার সংজ্ঞায়িত করুন, তাতে কোনো সমাধান নয়", cue: "দরকারকে এমনভাবে" },
      { text: "ছোট পরখ করুন: ফলাফল আর আসল ব্যবহার", cue: "আর ছোট পরিসরে" },
    ],
    action: { text: "কোনো কষ্টের কাজের দশটা সাইকেল দেখুন, আর যাঁরা সেটা করেন তাঁদের তিনজনের সঙ্গে কথা বলুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "E", title: "Elimination of Waste", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_BN_DURATION = PLAN.total;

export const DesignThinkingBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
