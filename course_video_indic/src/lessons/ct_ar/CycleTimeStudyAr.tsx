import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ct_ar/words.json";

// Arabic version of CycleTimeStudyAr (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "وقّت العمل الحقيقي, وجد عنق الزجاجة الحقيقي",
  outroLine: "حدّد. قِس. حسّن الطريقة.",
  outroSub: "Cycle Time Study: الدليل قبل السرعة",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "ثانية: بدت كل محطة سريعة بما يكفي",
    sub: "ومع ذلك فات خط الشاشات هدفه في كل ساعة, وردية بعد وردية.", until: "في هذا الدرس",
  },
  recap: {
    problem: "محطة اختبار الشاشة أبطأ من TAKT", before: 28, after: 23, unit: "ثانية لكل شاشة في المحطة C", fixedLabel: "الآن ضمن TAKT",
    takeaways: [
      { text: "حدّد الحدود أولًا", cue: "حدّد الحدود" },
      { text: "انظر إلى التشتت, لا إلى المتوسط فقط", cue: "انظر إلى التشتت" },
      { text: "أصلح الطريقة, ولا تتخطَّ فحوص الجودة أبدًا", cue: "وأصلح الطريقة" },
    ],
    action: { text: "وقّت عشر دورات في محطة واحدة, وقارن أطولها مع TAKT.", cue: "وهذه مهمتك" },
    next: { letter: "D", title: "Design Thinking", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_AR_DURATION = PLAN.total;

export const CycleTimeStudyAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
