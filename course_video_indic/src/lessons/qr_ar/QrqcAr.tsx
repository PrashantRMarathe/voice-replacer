import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/qr_ar/words.json";

// Arabic version of QrqcAr (same design and polish as the English lesson).
// All data comes from narration/qrqc_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "استجب في دقائق, وأغلق بالدليل",
  outroLine: "اكتشف. احتوِ. أثبت.",
  outroSub: "QRQC: استجابة سريعة, دليل حقيقي",
};

// Same polish as English QRQC; cues are phrases from the Arabic intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "كاميرات تفشل في اختبار التركيز بحلول الظهر",
    sub: "أعاد أحدهم ضبط جهاز الاختبار, واستمر الخط.", until: "في هذا الدرس",
  },
  recap: {
    problem: "كاميرات مشتبه بها في طريقها إلى المستودع", before: 2000, after: 0, unit: "كاميرا مشتبه بها غير محصورة",
    takeaways: [
      { text: "استجب بسرعة, لكن بالدليل", cue: "استجب بسرعة" },
      { text: "احتوِ أولًا, وطابق كل وحدة", cue: "احتوِ أولًا" },
      { text: "أغلق فقط عندما يثبت الحل", cue: "ولا تُغلق مشكلة" },
    ],
    action: { text: "اكتب أول 30 دقيقة من خطة استجابتك لعيب حرج واحد.", cue: "وهذه مهمتك" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "في الدرس التالي ستتعمق في" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_AR_DURATION = PLAN.total;

export const QrqcAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
