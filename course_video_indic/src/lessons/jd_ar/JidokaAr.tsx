import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/jd_ar/words.json";

// Arabic version of JidokaAr (same design and polish as the English lesson).
// All data comes from narration/jidoka_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "الأتمتة بلمسة إنسانية",
  outroLine: "رَه. أوقفه. احلّه.",
  outroSub: "Jidoka: لا عيب يمر, ولا خلل مخفي",
};

// Same polish as English Jidoka; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "جهاز مراقبة مرضى بإحكام رقيق",
    sub: "عمل جهاز الصرف بشكل مثالي طوال الليل. وكانت فوهته نصف مسدودة.", until: "في هذا الدرس",
  },
  recap: {
    problem: "إحكامات رقيقة من فوهة لاصق مسدودة", before: 140, after: 1, unit: "أجهزة متأثرة لكل مشكلة فوهة",
    fixedLabel: "تُلتقط عند المصدر",
    takeaways: [
      { text: "عرّف الطبيعي أولًا", cue: "عرّف الوضع الطبيعي أولًا" },
      { text: "اكتشف, أوقف, احتوِ: لا عيب يمر", cue: "اكتشف وأوقف واحتوِ" },
      { text: "كل توقف درس: أصلح السبب الجذري", cue: "وتعامل مع كل توقف" },
    ],
    action: { text: "اختر عملية آلية واحدة, واكتب ما الذي يجب أن يوقفها.", cue: "وهذه مهمتك" },
    next: { letter: "K", title: "Kaizen", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_AR_DURATION = PLAN.total;

export const JidokaAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
