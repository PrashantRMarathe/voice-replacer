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
import words from "../../captions/tt_hi/words.json";

// hi version of TaktTimeHi (same design and polish as the English lesson).
// All data comes from narration/takt_time_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "वह धड़कन जो आपका ग्राहक तय करता है",
  outroLine: "मापें। बैलेंस करें। फ़्लो बनाएँ।",
  outroSub: "TAKT Time — ग्राहक की रफ़्तार",
};

// Same polish as English TaktTime; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "कैमरे टेस्ट से आगे बना दिए",
    sub: "हर स्टेशन व्यस्त। ट्रक फिर भी लेट निकला।", until: "इस लेसन में",
  },
  recap: {
    problem: "व्यस्त लाइन, फिर भी ट्रक चूकती", before: 0, after: 10, unit: "सेकंड: रोज़ 7,200 कैमरों की धड़कन",
    fixedLabel: "वह रफ़्तार जिस पर सब चलते हैं",
    takeaways: [
      { text: "TAKT = नेट उपलब्ध समय ÷ डिमांड", cue: "TAKT यानी नेट" },
      { text: "जो रफ़्तार चाहिए, स्टेशन का समय नहीं", cue: "यह वह रफ़्तार" },
      { text: "असली नुकसान से प्लान, सिद्धांत से नहीं", cue: "और असली नुकसान" },
    ],
    action: { text: "एक लाइन का TAKT निकालें, और उसकी तुलना अपने सबसे धीमे स्टेशन से करें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "U", title: "Uniform Production", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_HI_DURATION = PLAN.total;

export const TaktTimeHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
