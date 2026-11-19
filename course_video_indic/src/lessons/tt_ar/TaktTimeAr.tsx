import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/tt_ar/words.json";

// Arabic version of TaktTimeAr (same design and polish as the English lesson).
// All data comes from narration/takt_time_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "الإيقاع الذي يحدده عميلك",
  outroLine: "قِس. وازن. تدفّق.",
  outroSub: "TAKT Time: إيقاع العميل",
};

// Same polish as English TaktTime; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "كاميرا جُمّعت قبل الاختبار",
    sub: "كل محطة مشغولة. والشاحنة غادرت متأخرة رغم ذلك.", until: "في هذا الدرس",
  },
  recap: {
    problem: "خط مشغول, ما زال يفوّت الشاحنة", before: 0, after: 10, unit: "ثانية: الإيقاع لـ7,200 كاميرا يوميًا",
    fixedLabel: "الإيقاع الذي يعمل به الجميع",
    takeaways: [
      { text: "TAKT = الوقت المتاح الصافي ÷ الطلب", cue: "TAKT هو الوقت المتاح الصافي" },
      { text: "الإيقاع الذي تحتاجه, لا زمن المحطة", cue: "إنه الإيقاع" },
      { text: "خطط للخسائر الحقيقية, لا للنظرية", cue: "وخطط للخسائر الحقيقية" },
    ],
    action: { text: "احسب TAKT لخط واحد, وقارنه بأبطأ محطة لديك.", cue: "وهذه مهمتك" },
    next: { letter: "U", title: "Uniform Production", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_AR_DURATION = PLAN.total;

export const TaktTimeAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
