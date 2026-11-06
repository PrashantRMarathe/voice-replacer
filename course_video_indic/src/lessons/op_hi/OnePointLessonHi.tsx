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
import words from "../../captions/op_hi/words.json";

// Hindi version of OnePointLessonHi (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "एक विषय। एक साफ़ पॉइंट। एक बेहतर काम।",
  outroLine: "आसान। विज़ुअल। सही।",
  outroSub: "One Point Lesson — एक पॉइंट अच्छे से सिखाएँ",
};

// Same polish as English OnePointLesson; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "कनेक्टर उल्टा लगा, और टूट गया",
    sub: "डे शिफ़्ट को तरीका पता था। किसी ने बताया नहीं था।", until: "इस लेसन में",
  },
  recap: {
    problem: "नाइट शिफ़्ट में टूटते कनेक्टर", before: 14, after: 1, unit: "टूटे कनेक्टर प्रति हफ़्ता",
    takeaways: [
      { text: "एक विषय, एक पॉइंट, एक दमदार विज़ुअल", cue: "एक विषय" },
      { text: "Gemba पर सिखाएँ, फिर काम देखें", cue: "इसे Gemba पर" },
      { text: "इसे मौजूदा स्टैंडर्ड से मिलाकर रखें", cue: "और इसे कंट्रोल" },
    ],
    action: { text: "बार-बार होने वाली एक गलती चुनें, और उसके लिए One Point Lesson का ड्राफ़्ट बनाएँ।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "P", title: "Poka Yoke", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_HI_DURATION = PLAN.total;

export const OnePointLessonHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
