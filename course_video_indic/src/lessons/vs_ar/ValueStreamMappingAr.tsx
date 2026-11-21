import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/vs_ar/words.json";

// Arabic version of ValueStreamMappingAr (same design and polish as the English lesson).
// All data comes from narration/value_stream_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "رَ التدفق كله, من الطلب إلى التسليم",
  outroLine: "رَ. قِس. تدفّق.",
  outroSub: "Value Stream Mapping: جد الانتظار, وصمّم التدفق",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "دقيقة لتجميع جهاز استقبال واختباره",
    sub: "ومع ذلك نحو أربعة أيام ليصل إلى العميل.", until: "في هذا الدرس",
  },
  recap: {
    problem: "أيام من الانتظار مقابل دقائق من العمل", before: 4200, after: 2100, unit: "وحدة تنتظر عبر ثلاثة مخازن مؤقتة",
    fixedLabel: "الحالة المستقبلية: نصف الانتظار",
    takeaways: [
      { text: "ارسم التدفق الحقيقي للمواد + المعلومات", cue: "ارسم التدفق الحقيقي" },
      { text: "زمن التوريد يختبئ في الانتظار, لا في العمل", cue: "معظم زمن التوريد" },
      { text: "أثبت الحالة المستقبلية قبل خفض المخزون", cue: "وصمّم حالة مستقبلية" },
    ],
    action: { text: "امشِ مع عائلة منتجات واحدة للخلف من الشحن, وعُدّ كل كومة تمر بها.", cue: "وهذه مهمتك" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_AR_DURATION = PLAN.total;

export const ValueStreamMappingAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
