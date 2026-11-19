import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/hc_ar/words.json";

// Arabic version of HanchoAr (same design and polish as the English lesson).
// All data comes from narration/hancho_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "قيادة أرض المصنع, في كل ساعة من كل وردية",
  outroLine: "قُد في Gemba. طوّر الناس.",
  outroSub: "Hancho: استعد المعايير, وحسّن كل يوم",
};

// Same polish as English Hancho; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "جهاز TV أقل في الساعة, طوال وردية كاملة",
    sub: "لم يلاحظ أحد حتى تقرير الصباح التالي.", until: "في هذا الدرس",
  },
  recap: {
    problem: "فجوة إنتاج بعد تغيير طراز", before: 98, after: 120, unit: "جهاز TV في الساعة",
    fixedLabel: "استُعيد في الوردية نفسها",
    takeaways: [
      { text: "قُد من Gemba: المعيار مقابل الفعلي", cue: "قُد من Gemba" },
      { text: "اجعل الفجوات مرئية كل ساعة؛ وتصرّف في الوردية نفسها", cue: "اجعل كل فجوة مرئية" },
      { text: "ابنِ الناس, حتى لا يعتمد الخط عليك", cue: "وابنِ ناسك" },
    ],
    action: { text: "اكتب العمل القياسي للقائد الخاص بك, لوردية واحدة.", cue: "وهذه مهمتك" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_AR_DURATION = PLAN.total;

export const HanchoAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
