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
import words from "../../captions/xm_mr/words.json";

// Marathi version of XMatrixMr (same design and polish as the English lesson).
// All data comes from narration/x_matrix_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Hoshin Kanri ने धोरण ॲक्शनमध्ये बदला",
  outroLine: "जोडा. लागू करा. रिव्ह्यू करा.",
  outroSub: "X-Matrix — असं धोरण, जे तुम्ही खरंच लागू करू शकता",
};

// Same polish as English XMatrix; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "इम्प्रूव्हमेंट प्रोजेक्ट, प्रत्येक टीम व्यस्त",
    sub: "तरीही डिलिव्हरी दर तिमाहीला घसरत राहिली.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "व्यस्त पोर्टफोलिओ, घसरती डिलिव्हरी", before: 40, after: 3, unit: "प्रोजेक्ट, प्रत्येक एखाद्या ध्येय आणि KPI शी जोडलेला",
    fixedLabel: "फोकस्ड पोर्टफोलिओ",
    takeaways: [
      { text: "काही खरी प्राधान्यं, इच्छांची यादी नाही", cue: "काही खरी प्राधान्यं" },
      { text: "ध्येय → प्रोजेक्ट → KPI → एक ओनर", cue: "प्रत्येक ध्येय" },
      { text: "प्रामाणिक रिव्ह्यू: आकडे हलायला हवेत", cue: "आणि प्रामाणिकपणे" },
    ],
    action: { text: "तुमच्या एरियासाठी एक उद्दिष्ट लिहा, निकालाच्या रूपात, कामाच्या रूपात नाही.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "Y", title: "Yamazumi", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_MR_DURATION = PLAN.total;

export const XMatrixMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
