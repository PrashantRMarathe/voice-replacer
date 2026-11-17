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
import words from "../../captions/ew_bn/words.json";

// Bengali version of EliminationOfWasteBn (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "যার জন্য গ্রাহক টাকা দেন না, তা সরান",
  outroLine: "দেখুন। কারণ সরান। প্রমাণ করুন।",
  outroSub: "Elimination of Waste — বেশি ভ্যালু, কম পরিশ্রম",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "সাউন্ডবারের প্রতি মাসে রিওয়ার্ক",
    sub: "প্রতিটা ঠিক করতে ₹42। কেউ কখনও এটা যোগই করেনি।", until: "এই পাঠে",
  },
  recap: {
    problem: "গুনগুন করা স্পিকার তার থেকে রিওয়ার্ক হওয়া সাউন্ডবার", before: 1500, after: 300, unit: "প্রতি মাসে রিওয়ার্ক", fixedLabel: "রিওয়ার্ক 80% কমল",
    takeaways: [
      { text: "ওয়েস্ট: যার জন্য গ্রাহক টাকা দেন না", cue: "ওয়েস্ট হলো সব কিছু" },
      { text: "একে Gemba তে তথ্য দিয়ে খুঁজুন", cue: "একে Gemba তে" },
      { text: "কারণ সরান, প্রমাণ করুন, টিকিয়ে রাখুন", cue: "আর কারণ সরান" },
    ],
    action: { text: "তিরিশ মিনিট আপনার লাইনে হাঁটুন, আর তিনটে ওয়েস্ট তথ্য হিসেবে লিখুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "F", title: "FMEA", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_BN_DURATION = PLAN.total;

export const EliminationOfWasteBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
