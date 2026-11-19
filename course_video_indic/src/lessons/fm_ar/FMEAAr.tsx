import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/fm_ar/words.json";

// Arabic version of FMEAAr (same design and polish as the English lesson).
// All data comes from narration/fmea_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "تحليل أنماط الفشل وآثارها: فكّر قبل الفشل",
  outroLine: "اربط السلسلة. قيّمها. امنعها.",
  outroSub: "FMEA: خطة حية, لا نموذج",
};

// Same polish as English FMEA; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "أجهزة راديو خارجية عادت مليئة بالماء",
    sub: "الحشية مفقودة في اثنتين, ملتوية في أربع. وكلها اجتازت الفحص النهائي.", until: "في هذا الدرس",
  },
  recap: {
    problem: "خطر الحشية في راديو 5G الخارجي", before: 240, after: 32, unit: "رقم أولوية المخاطر",
    fixedLabel: "المخاطرة انخفضت, مثبتة في تجربة",
    takeaways: [
      { text: "الأثر ← نمط الفشل ← سبب قابل للتحكم", cue: "ابنِ سلسلة واضحة" },
      { text: "قيّم بالدليل؛ الحكم فوق الأرقام", cue: "قيّم بالدليل" },
      { text: "امنع أولًا, أثبته, ثم أعد التقييم", cue: "وفضّل المنع" },
    ],
    action: { text: "اختر خطوة حرجة واحدة, واكتب سلسلة فشلها مع فريقك.", cue: "وهذه مهمتك" },
    next: { letter: "G", title: "Gemba", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_AR_DURATION = PLAN.total;

export const FMEAAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
