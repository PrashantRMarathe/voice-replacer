import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/bd_ar/words.json";

// Arabic version of BurnDownChartAr (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "رَ العمل المتبقي, قبل الموعد النهائي",
  outroLine: "خطّط الخط. تابع الفجوة. تصرّف اليوم.",
  outroSub: "Burn Down Chart: لا مفاجآت يوم الجمعة بعد الآن",
};

// Same polish as English BurnDownChart; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "جهاز راوتر فاتتها الشاحنة",
    sub: "لم يتوقع أحد ذلك, حتى ظهر يوم الجمعة.", until: "في هذا الدرس",
  },
  recap: {
    problem: "نقص في أجهزة الراوتر عند الشحن", before: 80, after: 0, unit: "جهاز راوتر ناقص",
    takeaways: [
      { text: "ارسم الخط المثالي أولًا؛ ولا تُعد رسمه أبدًا", cue: "ارسم الخط المثالي" },
      { text: "لا تعدّ إلا العمل المكتمل والسليم", cue: "لا تعدّ إلا العمل" },
      { text: "فوق المثالي? تصرّف في اليوم نفسه, مع مسؤول", cue: "وعندما يرتفع الخط" },
    ],
    action: { text: "اختر عملًا واحدًا له موعد نهائي, وارسم مخطط العمل المتبقي له قبل وردية الغد.", cue: "وهذه مهمتك" },
    next: { letter: "C", title: "Cycle Time Study", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_AR_DURATION = PLAN.total;

export const BurnDownChartAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
