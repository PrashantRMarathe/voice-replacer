import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/yz_ar/words.json";

// Arabic version of YamazumiAr (same design and polish as the English lesson).
// All data comes from narration/yamazumi_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "وازن الخط مقابل TAKT, ببيانات حقيقية",
  outroLine: "قِس. كدّس. وازن.",
  outroSub: "Yamazumi: تدفق يصمد, بالتصميم",
};

// Same polish as English Yamazumi; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "عمال ينتظرون, بينما يغرق واحد في البراغي",
    sub: "لا أحد كسول. العمل مكدّس بشكل غير متساوٍ فقط.", until: "في هذا الدرس",
  },
  recap: {
    problem: "المحطة B فوق TAKT", before: 35, after: 30, unit: "ثوانٍ من العمل في المحطة B",
    fixedLabel: "عاد تحت TAKT",
    takeaways: [
      { text: "قِس العمل الحقيقي, لا أفضل حالة", cue: "قِس العمل الحقيقي" },
      { text: "كدّسه مقابل TAKT لترى التكدّسات", cue: "كدّسه مقابل TAKT" },
      { text: "أعد الموازنة دون المخاطرة بالسلامة أو الجودة", cue: "وأعد الموازنة بعناية" },
    ],
    action: { text: "وقّت محطة واحدة في خطك, وارسم عمودها مقابل TAKT.", cue: "مهمتك هذا الأسبوع" },
    next: { letter: "Z", title: "Zero Defects", cue: "إلى اللقاء في الدرس التالي" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_AR_DURATION = PLAN.total;

export const YamazumiAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
