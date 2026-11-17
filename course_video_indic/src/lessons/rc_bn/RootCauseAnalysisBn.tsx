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
import words from "../../captions/rc_bn/words.json";

// Bengali version of RootCauseAnalysisBn (same design and polish as the English lesson).
// All data comes from narration/root_cause_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "লক্ষণ থেকে প্রমাণ করা যায় এমন কারণে",
  outroLine: "সংজ্ঞায়িত করুন। যাচাই করুন। আটকান।",
  outroSub: "Root Cause Analysis — প্রমাণ করুন, তারপর ঠিক করুন",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "এক সকালে ক্যামেরা ফোকাস টেস্টে ফেল",
    sub: "তিনজন, তিনটে আলাদা উত্তর।", until: "এই পাঠে",
  },
  recap: {
    problem: "চেঞ্জওভারের পরে ফোকাসে ফেল ক্যামেরা", before: 60, after: 12, unit: "প্রতি 20,000 ক্যামেরায় ডিফেক্ট",
    takeaways: [
      { text: "ধারালো সংজ্ঞা, গ্রাহককে বাঁচান", cue: "সমস্যাকে ধারালোভাবে" },
      { text: "যাচাই পর্যন্ত প্রতিটি কারণ হাইপোথিসিস", cue: "প্রতিটি কারণকে" },
      { text: "কেন ঘটল আর কেন বেরোল, দুটোই ঠিক করুন", cue: "আর দুটোই ঠিক" },
    ],
    action: { text: "একটা বন্ধ হওয়া সমস্যা নিন, আর দেখুন তার রুট কজ কখনো যাচাই হয়েছিল কিনা।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_BN_DURATION = PLAN.total;

export const RootCauseAnalysisBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
