import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/xm_ar/words.json";

// Arabic version of XMatrixAr (same design and polish as the English lesson).
// All data comes from narration/x_matrix_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "حوّل الاستراتيجية إلى عمل بـHoshin Kanri",
  outroLine: "واءم. انشر. راجع.",
  outroSub: "X-Matrix: استراتيجية يمكنك تنفيذها فعلًا",
};

// Same polish as English XMatrix; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "مشروع تحسين, كل فريق مشغول",
    sub: "ومع ذلك ظل التسليم يتأخر, ربعًا بعد ربع.", until: "في هذا الدرس",
  },
  recap: {
    problem: "محفظة مشغولة, وتسليم متأخر", before: 40, after: 3, unit: "مشروع, كل منها مرتبط بهدف وKPI",
    fixedLabel: "محفظة مركّزة",
    takeaways: [
      { text: "بضع أولويات حقيقية, لا قائمة أمنيات", cue: "اختر بضع أولويات حقيقية" },
      { text: "الهدف ← المشروع ← KPI ← مسؤول واحد", cue: "اربط كل هدف" },
      { text: "راجع بصدق: الأرقام يجب أن تتحرك", cue: "وراجع بصدق" },
    ],
    action: { text: "اكتب هدفًا واحدًا لمنطقتك كنتيجة, لا كنشاط.", cue: "وهذه مهمتك" },
    next: { letter: "Y", title: "Yamazumi", cue: "إلى اللقاء في الدرس التالي" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_AR_DURATION = PLAN.total;

export const XMatrixAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
