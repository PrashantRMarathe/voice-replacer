import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/pk_ar/words.json";

// Arabic version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "اجعل الفعل الخاطئ مستحيلًا",
  outroLine: "أزِل. امنع. اكتشف.",
  outroSub: "Poka Yoke: أخرج الذاكرة من الجودة",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_AR_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "أجهزة تسجيل شُحنت ببرغي ناقص",
    sub: "كانت العاملة ماهرة وحريصة. بشر فقط.", until: "في هذا الدرس",
  },
  recap: {
    problem: "أجهزة تسجيل شُحنت ببرغي ناقص", before: 18, after: 1, unit: "لكل 10,000 وحدة",
    takeaways: [
      { text: "الأخطاء متوقعة: صمّم لمنعها", cue: "الأخطاء متوقعة" },
      { text: "المنع, ثم الاكتشاف, ثم التحذير", cue: "فضّل المنع" },
      { text: "اختبر كل جهاز بعينات معيبة", cue: "واختبر كل جهاز" },
    ],
    action: { text: "ابحث عن فحص يعتمد على الذاكرة, وارسم له Poka Yoke.", cue: "وهذه مهمتك" },
    next: { letter: "Q", title: "QRQC", cue: "في الدرس التالي ستتعرف على QRQC" },
  },
};

export const PokaYokeAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
