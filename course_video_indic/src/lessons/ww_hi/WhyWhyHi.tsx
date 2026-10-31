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
import words from "../../captions/ww_hi/words.json";

// Hindi version of WhyWhyHi (same design and polish as the English lesson).
// All data comes from narration/why_why_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "आसान जवाब से आगे, ऐसी वजह तक जिसे आप साबित कर सकें",
  outroLine: "परिभाषित करें। साबित करें। रोकें।",
  outroSub: "Why–Why — वजह ठीक करें, व्यक्ति नहीं",
};

// Same polish as English WhyWhy; cues are phrases from the Hindi intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "power", label: "फ़ोन फ़ाइनल टेस्ट में चार्जिंग में फ़ेल",
    sub: "पहला जवाब: ऑपरेटर की गलती। दो दिन बाद, फिर वही हुआ।", until: "इस लेसन में",
  },
  recap: {
    problem: "लाइन 2 पर चार्जिंग फ़ेल्योर", before: 50, after: 15, unit: "चार्जिंग डिफ़ेक्ट, वही वॉल्यूम",
    fixedLabel: "रूट कॉज़ ठीक: 70% कम",
    takeaways: [
      { text: "पहले धारदार समस्या, फिर कंटेनमेंट", cue: "एक धारदार समस्या" },
      { text: "हर क्यों का सबूत, फिर परखें", cue: "हर क्यों के पीछे" },
      { text: "कैसे हुआ और क्यों निकला, दोनों ठीक करें", cue: "और दोनों ठीक" },
    ],
    action: { text: "बार-बार होने वाला एक डिफ़ेक्ट लें, और उसका 5W2H स्टेटमेंट लिखें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "X", title: "X-Matrix", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_HI_DURATION = PLAN.total;

export const WhyWhyHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
