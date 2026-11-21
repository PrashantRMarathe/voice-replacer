import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ik_ar/words.json";

// Arabic version of IshikawaAr (same design and polish as the English lesson).
// All data comes from narration/ishikawa_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "ابحث على نطاق واسع بعظم السمكة, ثم أثبت السبب",
  outroLine: "ابحث على نطاق واسع. أثبت بدقة.",
  outroSub: "Ishikawa: كل عظمة تخمين حتى تُختبر",
};

// Same polish as English Ishikawa; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "محوّلات لكل 1,000 تفشل في اختبار المنافذ",
    sub: "ارتفاعًا من 5. وجواب الاجتماع: شراء جهاز اختبار جديد.", until: "في هذا الدرس",
  },
  recap: {
    problem: "أعطال ربط المنافذ على خط المحوّلات", before: 32, after: 4, unit: "لكل 1,000 محوّل",
    fixedLabel: "السببان أُصلحا",
    takeaways: [
      { text: "أثر حاد وقابل للقياس في الرأس", cue: "ابدأ بأثر حاد" },
      { text: "ابحث على نطاق واسع عبر 6M, دون لوم", cue: "ابحث على نطاق واسع" },
      { text: "كل عظمة تخمين حتى تثبت", cue: "وتعامل مع كل عظمة" },
    ],
    action: { text: "ارسم عظم سمكة لمشكلة متكررة واحدة, واختر ثلاثة أسباب لتختبرها.", cue: "وهذه مهمتك" },
    next: { letter: "J", title: "Jidoka", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_AR_DURATION = PLAN.total;

export const IshikawaAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
