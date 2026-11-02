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
import words from "../../captions/ct_hi/words.json";

// hi version of CycleTimeStudyHi (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "असली काम मापें, असली बॉटलनेक ढूँढें",
  outroLine: "परिभाषा। माप। तरीके में सुधार।",
  outroSub: "Cycle Time Study — रफ़्तार से पहले सबूत",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "सेकंड: हर स्टेशन काफ़ी तेज़ दिखता था",
    sub: "फिर भी मॉनिटर लाइन शिफ़्ट दर शिफ़्ट घंटे का टारगेट चूकती रही।", until: "इस लेसन में",
  },
  recap: {
    problem: "डिस्प्ले-टेस्ट स्टेशन TAKT से धीमा", before: 28, after: 23, unit: "सेकंड प्रति मॉनिटर, स्टेशन C पर", fixedLabel: "अब TAKT के अंदर",
    takeaways: [
      { text: "पहले बाउंड्री तय करें", cue: "पहले बाउंड्री" },
      { text: "सिर्फ़ औसत नहीं, फैलाव देखें", cue: "सिर्फ़ औसत नहीं" },
      { text: "तरीका ठीक करें, क्वालिटी चेक कभी न छोड़ें", cue: "और बॉटलनेक पर" },
    ],
    action: { text: "एक स्टेशन पर दस साइकिल मापें, और सबसे लंबे की तुलना TAKT से करें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "D", title: "Design Thinking", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_HI_DURATION = PLAN.total;

export const CycleTimeStudyHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
