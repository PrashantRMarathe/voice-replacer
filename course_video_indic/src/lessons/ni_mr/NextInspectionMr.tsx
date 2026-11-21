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
import words from "../../captions/ni_mr/words.json";

// Marathi version of NextInspectionMr (same design and polish as the English lesson).
// All data comes from narration/next_inspection_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "पुढची प्रोसेस माझा ग्राहक आहे",
  outroLine: "बनवू नका. पाठवू नका. स्वीकारू नका.",
  outroSub: "Next Inspection — पुढच्या प्रोसेसला वाचवा",
};

// Same polish as English NextInspection; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "सैल कनेक्टर, स्टेशन तीनवर",
    sub: "कोणाच्या लक्षात आलं नाही. मग एका ग्राहकाने बॉक्स उघडला.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "पुढच्या स्टेशनपर्यंत निसटणारे डिफेक्ट", before: 18, after: 3, unit: "एस्केप दर आठवड्याला",
    takeaways: [
      { text: "बनवू नका, पाठवू नका, स्वीकारू नका", cue: "डिफेक्ट बनवू नका" },
      { text: "लवकर तपासा, पटकन कृती करा", cue: "महत्त्वाचे पॉइंट शक्य" },
      { text: "कंट्रोल वरच्या दिशेने नेत राहा", cue: "आणि तुमचे कंट्रोल" },
    ],
    action: { text: "एक हँडऑफ निवडा, आणि पुढच्या प्रोसेसला त्यातून काय हवं ते लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "O", title: "One Point Lesson", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_MR_DURATION = PLAN.total;

export const NextInspectionMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
