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
import words from "../../captions/ct_mr/words.json";

// Marathi version of CycleTimeStudyMr (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "खरं काम मोजा, खरा बॉटलनेक शोधा",
  outroLine: "व्याख्या. माप. पद्धतीत सुधारणा.",
  outroSub: "Cycle Time Study — वेगाआधी पुरावा",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "सेकंद: प्रत्येक स्टेशन पुरेसं जलद दिसत होतं",
    sub: "तरीही मॉनिटर लाइन शिफ्टमागून शिफ्ट तासाचं टार्गेट चुकवत होती.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "डिस्प्ले-टेस्ट स्टेशन TAKT पेक्षा हळू", before: 28, after: 23, unit: "सेकंद प्रति मॉनिटर, स्टेशन C वर", fixedLabel: "आता TAKT च्या आत",
    takeaways: [
      { text: "आधी बाउंड्री ठरवा", cue: "आधी बाउंड्री" },
      { text: "फक्त सरासरी नाही, फैलाव पाहा", cue: "फक्त सरासरी नाही" },
      { text: "पद्धत दुरुस्त करा, क्वालिटी चेक कधीही सोडू नका", cue: "आणि बॉटलनेकवर" },
    ],
    action: { text: "एका स्टेशनवर दहा सायकल मोजा, आणि सर्वात लांबच्याची तुलना TAKT शी करा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "D", title: "Design Thinking", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_MR_DURATION = PLAN.total;

export const CycleTimeStudyMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
