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
import words from "../../captions/sk_mr/words.json";

// Marathi version of SkillMatrixMr (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "कोण खरंच कोणतं काम करू शकतं — आणि गॅप कुठे आहेत",
  outroLine: "तपासा. ट्रेन करा. कव्हर करा.",
  outroSub: "Skill Matrix — क्षमतेचं जिवंत कंट्रोल",
};

// Same polish as English SkillMatrix; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "व्यक्ती जी लेन्स फोकस सेट करू शकते",
    sub: "बाला आजारी होता. दहा वाजेपर्यंत, पूर्ण सेल थांबला.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "एक लेन्स फोकस एक्सपर्ट, आणि तो आजारी", before: 1, after: 2, unit: "पात्र लेन्स फोकस एक्सपर्ट",
    takeaways: [
      { text: "सिद्ध क्षमता, हजेरी नाही", cue: "स्किल मॅट्रिक्स सिद्ध" },
      { text: "प्रत्येक शिफ्टवर पात्र बॅकअप मोजा", cue: "प्रत्येक महत्त्वाच्या कामासाठी" },
      { text: "तो जिवंत ठेवा, पुराव्यासह", cue: "आणि तो जिवंत" },
    ],
    action: { text: "तुमची तीन सर्वात महत्त्वाची स्टेशन लिहा, आणि प्रत्येकासाठी पात्र लोक मोजा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "T", title: "TAKT Time", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_MR_DURATION = PLAN.total;

export const SkillMatrixMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
