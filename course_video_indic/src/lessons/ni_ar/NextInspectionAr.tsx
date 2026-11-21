import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ni_ar/words.json";

// Arabic version of NextInspectionAr (same design and polish as the English lesson).
// All data comes from narration/next_inspection_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "العملية التالية هي عميلي",
  outroLine: "لا تصنع. لا تمرّر. لا تقبل.",
  outroSub: "Next Inspection: احمِ العملية التالية",
};

// Same polish as English NextInspection; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "موصل مرتخٍ في المحطة الثالثة",
    sub: "لم يلاحظه أحد. ثم فتح عميل الصندوق.", until: "في هذا الدرس",
  },
  recap: {
    problem: "عيوب تتسرب إلى محطات لاحقة", before: 18, after: 3, unit: "تسربات أسبوعيًا",
    takeaways: [
      { text: "لا تصنع, لا تمرّر, لا تقبل", cue: "لا تصنع" },
      { text: "افحص مبكرًا, واستجب بسرعة", cue: "افحص النقاط الحرجة" },
      { text: "واصل نقل الضوابط إلى الأمام", cue: "وواصل نقل ضوابطك" },
    ],
    action: { text: "اختر نقطة تسليم واحدة, واكتب ما تحتاجه العملية التالية منها.", cue: "وهذه مهمتك" },
    next: { letter: "O", title: "One Point Lesson", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_AR_DURATION = PLAN.total;

export const NextInspectionAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
