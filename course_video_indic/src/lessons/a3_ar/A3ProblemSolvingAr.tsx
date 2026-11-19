import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/a3_ar/words.json";

// Arabic version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "قصة المشكلة كاملة في صفحة واحدة",
  outroLine: "رَ الفجوة. أثبت السبب. حافظ.",
  outroSub: "A3: تفكير أفضل, في ورقة واحدة",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_AR_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "خوادم فشلت في اختبار الإقلاع الأول",
    sub: "في أربعة أسابيع. والحل الأول المقترح: مفتشان آخران.", until: "في هذا الدرس",
  },
  recap: {
    problem: "خوادم تفشل في اختبار الإقلاع الأول", before: 48, after: 16, unit: "لكل 1,000 خادم", fixedLabel: "تحقق الهدف: انخفاض من 48",
    takeaways: [
      { text: "ابدأ بفجوة قابلة للقياس", cue: "ابدأ بفجوة قابلة للقياس" },
      { text: "اذهب وانظر؛ أثبت كل سبب", cue: "اذهب وانظر بنفسك" },
      { text: "عمّم فقط ما أثبتته التجربة", cue: "ولا تعمّم إلا" },
    ],
    action: { text: "اختر مشكلة واحدة متكررة, واكتب بيان مشكلتها على ورقة A3.", cue: "وهذه مهمتك" },
    next: { letter: "B", title: "Burn Down Chart", cue: "في الدرس التالي ستتعرف على" },
  },
};

export const A3ProblemSolvingAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
