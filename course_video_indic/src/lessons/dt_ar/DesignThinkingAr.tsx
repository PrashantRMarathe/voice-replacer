import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/dt_ar/words.json";

// Arabic version of DesignThinkingAr (same design and polish as the English lesson).
// All data comes from narration/design_thinking_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "حل المشكلة الصحيحة, مع الناس الذين يؤدون العمل",
  outroLine: "راقب. عرّف. اختبر صغيرًا.",
  outroSub: "Design Thinking: الناس أولًا, والدليل دائمًا",
};

// Same polish as English DesignThinking; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "أخطاء ملصقات في كل 1,000 مضخة",
    sub: "الفكرة الأولى: طابعة أسرع ومكلفة. ولم يسأل أحد عمال التعبئة.", until: "في هذا الدرس",
  },
  recap: {
    problem: "أخطاء الملصقات في تعبئة مضخات التسريب", before: 12, after: 2, unit: "لكل 1,000 مضخة",
    takeaways: [
      { text: "ابدأ بالناس؛ راقب قبل أن تقرر", cue: "ابدأ بالناس" },
      { text: "عرّف الحاجة, دون حل داخلها", cue: "عرّف الحاجة" },
      { text: "اختبر صغيرًا: النتائج والاستخدام الحقيقي", cue: "واختبر على نطاق صغير" },
    ],
    action: { text: "راقب عشر دورات لعمل مُتعب واحد, وتحدث مع ثلاثة أشخاص يؤدونه.", cue: "وهذه مهمتك" },
    next: { letter: "E", title: "Elimination of Waste", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_AR_DURATION = PLAN.total;

export const DesignThinkingAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
