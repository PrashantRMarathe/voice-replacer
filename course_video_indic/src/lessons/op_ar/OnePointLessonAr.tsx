import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/op_ar/words.json";

// Arabic version of OnePointLessonAr (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "موضوع واحد. نقطة واحدة واضحة. فعل واحد أفضل.",
  outroLine: "بسيط. مرئي. صحيح.",
  outroSub: "One Point Lesson: علّم نقطة واحدة جيدًا",
};

// Same polish as English OnePointLesson; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "موصل رُكّب بالاتجاه الخاطئ, فانكسر",
    sub: "كانت الوردية النهارية تعرف الحيلة. لكن أحدًا لم يشاركها.", until: "في هذا الدرس",
  },
  recap: {
    problem: "الوردية الليلية تكسر الموصلات", before: 14, after: 1, unit: "موصلات مكسورة أسبوعيًا",
    takeaways: [
      { text: "موضوع واحد, نقطة واحدة, صورة قوية", cue: "موضوع واحد" },
      { text: "علّم في Gemba, ثم راقب العمل", cue: "علّمها في Gemba" },
      { text: "طابق المعيار الحالي دائمًا", cue: "وتحكّم فيها" },
    ],
    action: { text: "اختر خطأ واحدًا يتكرر, واكتب له مسودة One Point Lesson.", cue: "وهذه مهمتك" },
    next: { letter: "P", title: "Poka Yoke", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_AR_DURATION = PLAN.total;

export const OnePointLessonAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
