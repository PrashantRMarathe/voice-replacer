import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/gb_ar/words.json";

// Arabic version of GembaAr (same design and polish as the English lesson).
// All data comes from narration/gemba_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "المكان الحقيقي, الشيء الحقيقي, الحقائق الحقيقية",
  outroLine: "اذهب. انظر. تأكد.",
  outroSub: "Gemba, Genbutsu, Genjitsu: الحقائق قبل القرارات",
};

// Same polish as English Gemba; cues are phrases from the Arabic intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× أعطال السماعات في الوردية B",
    sub: "الخطة: إعادة تدريب الوردية B. ولم ينظر أحد إلى سماعة معطلة.", until: "في هذا الدرس",
  },
  recap: {
    problem: "سماعات تفشل في اختبار الصوت", before: 20, after: 8, unit: "أعطال لكل 1,000 سماعة",
    fixedLabel: "أُصلح عند السبب",
    takeaways: [
      { text: "اذهب إلى المكان الحقيقي؛ راقب دورات حقيقية", cue: "اذهب إلى المكان الحقيقي" },
      { text: "أمسك الشيء الحقيقي؛ قارنه بشيء سليم", cue: "أمسك الشيء الحقيقي" },
      { text: "تحقق من الحقائق الحقيقية, بمقام واضح", cue: "وتحقق من الحقائق الحقيقية" },
    ],
    action: { text: "خذ مشكلة متكررة واحدة, وقم بزيارة 3G لمدة ثلاثين دقيقة.", cue: "وهذه مهمتك" },
    next: { letter: "H", title: "Hancho", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_AR_DURATION = PLAN.total;

export const GembaAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
