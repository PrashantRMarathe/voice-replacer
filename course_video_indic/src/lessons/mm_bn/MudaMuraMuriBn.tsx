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
import words from "../../captions/mm_bn/words.json";

// Bengali version of MudaMuraMuriBn (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "ওয়েস্ট, অসমতা আর অতিরিক্ত বোঝা — তিনটেই সুধরান",
  outroLine: "সমান করুন। বাঁচান। সরান।",
  outroSub: "3M — স্থির ফ্লো, দ্রুত মানুষ নয়",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "ক্যামেরা পিছিয়ে, শিফট শেষের এক ঘণ্টা আগে",
    sub: "সবাই দৌড়াচ্ছে। টেস্টে ভুল জমছে।", until: "এই পাঠে",
  },
  recap: {
    problem: "সঞ্জয়ের লাইন রোজ দেরিতে চলত", before: 150, after: 0, unit: "প্রতিদিন ওভারটাইমের মিনিট",
    takeaways: [
      { text: "Muda ওয়েস্ট, Mura অসমতা, Muri অতিরিক্ত বোঝা", cue: "Muda হলো ওয়েস্ট" },
      { text: "এরা একে অপরকে বাড়ায়: একসঙ্গে সুধরান", cue: "এরা একে অপরকে" },
      { text: "স্থির ফ্লো, দ্রুত মানুষ নয়", cue: "আর লক্ষ্য হলো" },
    ],
    action: { text: "একটা প্রোডাক্টকে আপনার লাইন দিয়ে নিয়ে যেতে যেতে হাঁটুন, আর প্রতিটি M এর একটা উদাহরণ ট্যাগ করুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "N", title: "Next Inspection", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_BN_DURATION = PLAN.total;

export const MudaMuraMuriBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
