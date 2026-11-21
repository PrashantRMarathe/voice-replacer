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
import words from "../../captions/sk_bn/words.json";

// Bengali version of SkillMatrixBn (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "কে সত্যিই কোন কাজ পারে — আর গ্যাপ কোথায়",
  outroLine: "যাচাই করুন। ট্রেনিং দিন। কভার করুন।",
  outroSub: "Skill Matrix — দক্ষতার জীবন্ত কন্ট্রোল",
};

// Same polish as English SkillMatrix; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "যে মানুষ লেন্স ফোকাস সেট করতে পারেন",
    sub: "বালা অসুস্থ ছিলেন। দশটার মধ্যে, পুরো সেল থেমে গেল।", until: "এই পাঠে",
  },
  recap: {
    problem: "একজন লেন্স ফোকাস এক্সপার্ট, আর তিনি অসুস্থ", before: 1, after: 2, unit: "যোগ্য লেন্স ফোকাস এক্সপার্ট",
    takeaways: [
      { text: "প্রমাণিত দক্ষতা, উপস্থিতি নয়", cue: "স্কিল ম্যাট্রিক্স প্রমাণিত" },
      { text: "প্রতি শিফটে যোগ্য ব্যাকআপ গুনুন", cue: "প্রতিটি জরুরি কাজের" },
      { text: "এটা জীবন্ত রাখুন, প্রমাণ সহ", cue: "আর এটা জীবন্ত" },
    ],
    action: { text: "আপনার তিনটি সবচেয়ে জরুরি স্টেশন লিখুন, আর প্রতিটির জন্য যোগ্য লোক গুনুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "T", title: "TAKT Time", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_BN_DURATION = PLAN.total;

export const SkillMatrixBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
