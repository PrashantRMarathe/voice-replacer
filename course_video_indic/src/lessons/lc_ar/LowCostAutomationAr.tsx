import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/lc_ar/words.json";

// Arabic version of LowCostAutomationAr (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "أبسط جهاز آمن يؤدي المهمة",
  outroLine: "بسّط. أتمت الحاجة. أثبت.",
  outroSub: "Low Cost Automation: لا سلامة منخفضة أبدًا",
};

// Same polish as English LowCostAutomation; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "ضربة مطرقة في الساعة, لكل عامل",
    sub: "معاصم مؤلمة, وشبكات مرتخية تخشخش عند الاختبار.", until: "في هذا الدرس",
  },
  recap: {
    problem: "شبكات سماعات مرتخية من التثبيت بالمطرقة", before: 18, after: 2, unit: "لكل 1,000 سماعة",
    fixedLabel: "الاسترداد في 4 أشهر",
    takeaways: [
      { text: "بسّط أولًا؛ لا تؤتمت الهدر أبدًا", cue: "بسّط أولًا" },
      { text: "أبسط حل آمن؛ السلامة هي البوابة الأولى", cue: "اختر أبسط" },
      { text: "أثبت الفائدة الحقيقية, ثم صُنها", cue: "وأثبت الفائدة الحقيقية" },
    ],
    action: { text: "ابحث عن حركة متكررة واحدة, واسأل هل يمكن إزالتها قبل أتمتتها.", cue: "وهذه مهمتك" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_AR_DURATION = PLAN.total;

export const LowCostAutomationAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
