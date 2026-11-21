import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ww_ar/words.json";

// Arabic version of WhyWhyAr (same design and polish as the English lesson).
// All data comes from narration/why_why_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "تجاوز الجواب السهل إلى سبب يمكنك إثباته",
  outroLine: "عرّف. أثبت. امنع.",
  outroSub: "Why-Why: أصلح السبب, لا الشخص",
};

// Same polish as English WhyWhy; cues are phrases from the Arabic intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "هواتف فشلت في الشحن عند الاختبار النهائي",
    sub: "الجواب الأول: خطأ العامل. وبعد يومين, تكرر الأمر.", until: "في هذا الدرس",
  },
  recap: {
    problem: "أعطال الشحن على الخط 2", before: 50, after: 15, unit: "عيوب الشحن, الكمية نفسها",
    fixedLabel: "السبب الجذري أُصلح: أقل 70%",
    takeaways: [
      { text: "المشكلة الحادة أولًا, ثم الاحتواء", cue: "ابدأ بمشكلة حادة" },
      { text: "دليل لكل لماذا, ثم اختبرها", cue: "ادعم كل لماذا" },
      { text: "أصلح كيف حدث ولماذا تسرب", cue: "وأصلح الأمرين" },
    ],
    action: { text: "خذ عيبًا متكررًا واحدًا, واكتب بيان 5W2H له.", cue: "وهذه مهمتك" },
    next: { letter: "X", title: "X-Matrix", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_AR_DURATION = PLAN.total;

export const WhyWhyAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
