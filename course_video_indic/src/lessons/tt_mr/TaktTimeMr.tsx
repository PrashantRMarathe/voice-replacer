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
import words from "../../captions/tt_mr/words.json";

// Marathi version of TaktTimeMr (same design and polish as the English lesson).
// All data comes from narration/takt_time_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "तुमचा ग्राहक ठरवतो ते ठोके",
  outroLine: "मोजा. बॅलन्स करा. फ्लो बनवा.",
  outroSub: "TAKT Time — ग्राहकाचा वेग",
};

// Same polish as English TaktTime; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "कॅमेरे टेस्टच्या पुढे बनवले",
    sub: "प्रत्येक स्टेशन व्यस्त. ट्रक तरीही उशिरा निघाला.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "व्यस्त लाइन, तरीही ट्रक चुकतो", before: 0, after: 10, unit: "सेकंद: रोज 7,200 कॅमेऱ्यांचे ठोके",
    fixedLabel: "तो वेग ज्यावर सगळे चालतात",
    takeaways: [
      { text: "TAKT = नेट उपलब्ध वेळ ÷ डिमांड", cue: "TAKT म्हणजे नेट" },
      { text: "हवा असलेला वेग, स्टेशनचा वेळ नाही", cue: "हा तुम्हाला हवा" },
      { text: "खऱ्या नुकसानाने प्लान, सिद्धांताने नाही", cue: "आणि खऱ्या नुकसानानुसार" },
    ],
    action: { text: "एका लाइनचा TAKT काढा, आणि त्याची तुलना तुमच्या सर्वात हळू स्टेशनशी करा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "U", title: "Uniform Production", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_MR_DURATION = PLAN.total;

export const TaktTimeMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
