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
import words from "../../captions/up_bn/words.json";

// Bengali version of UniformProductionBn (same design and polish as the English lesson).
// All data comes from narration/uniform_production_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "ভলিউম আর মিক্স লেভেল করুন, স্থির আর ভরসাযোগ্য ফ্লোর জন্য",
  outroLine: "লেভেল করুন। ক্রম ঠিক করুন। স্থির করুন।",
  outroSub: "Uniform Production — এমন গতি, যা আপনার লাইন ধরে রাখতে পারে",
};

// Same polish as English UniformProduction; cues are phrases from the Bengali intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "সোমবার ফোন। মঙ্গলবার প্রায় কিছুই না।",
    sub: "বুধবারের মধ্যে, টেস্ট বেঞ্চ কাজে ডুবে আছে।", until: "এই পাঠে",
  },
  recap: {
    problem: "এক খুব এবড়োখেবড়ো শিডিউল", before: 0, after: 6000, unit: "রোজ ভালো ইউনিট, প্রতিদিন",
    fixedLabel: "একটা স্থির, লেভেল গতি",
    takeaways: [
      { text: "ভলিউম আর মিক্স, দুটোই লেভেল করুন", cue: "ভলিউম আর মিক্স, দুটোই" },
      { text: "আগে বটলনেক আর চেঞ্জওভার যাচাই করুন", cue: "কোনো প্যাটার্নে" },
      { text: "দৃশ্যমান প্ল্যান, পরিবর্তনের পরিষ্কার নিয়ম", cue: "আর প্ল্যানকে" },
    ],
    action: { text: "বড় ব্যাচে বানানো একটা প্রোডাক্ট খুঁজুন, আর ছোট, পুনরাবৃত্ত প্যাটার্নের স্কেচ করুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_BN_DURATION = PLAN.total;

export const UniformProductionBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
