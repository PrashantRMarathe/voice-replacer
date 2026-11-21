import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/up_ar/words.json";

// Arabic version of UniformProductionAr (same design and polish as the English lesson).
// All data comes from narration/uniform_production_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "سوِّ الكمية والمزيج لتدفق ثابت وموثوق",
  outroLine: "سوِّ. رتّب. ثبّت.",
  outroSub: "Uniform Production: إيقاع ثابت يستطيع خطك الحفاظ عليه",
};

// Same polish as English UniformProduction; cues are phrases from the Arabic intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "هاتف يوم الاثنين. لا شيء تقريبًا يوم الثلاثاء.",
    sub: "بحلول الأربعاء, تغرق طاولة الاختبار.", until: "في هذا الدرس",
  },
  recap: {
    problem: "جدول شديد الاضطراب", before: 0, after: 6000, unit: "وحدة سليمة يوميًا, كل يوم",
    fixedLabel: "إيقاع ثابت ومسوّى",
    takeaways: [
      { text: "سوِّ الكمية والمزيج معًا", cue: "سوِّ الكمية والمزيج" },
      { text: "افحص عنق الزجاجة والتغييرات أولًا", cue: "افحص عنق الزجاجة" },
      { text: "خطة مرئية, وقواعد تغيير واضحة", cue: "واجعل الخطة مرئية" },
    ],
    action: { text: "جد منتجًا واحدًا يُصنع في دفعة كبيرة, وارسم نمطًا أصغر ومتكررًا.", cue: "وهذه مهمتك" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "في الدرس التالي سترسم" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_AR_DURATION = PLAN.total;

export const UniformProductionAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
