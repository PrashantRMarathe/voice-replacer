import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/kz_ar/words.json";

// Arabic version of KaizenAr (same design and polish as the English lesson).
// All data comes from narration/kaizen_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "تغييرات صغيرة, كل يوم, ممن يؤدون العمل",
  outroLine: "رَ. جرّب صغيرًا. وحّد. كرّر.",
  outroSub: "Kaizen: أفضل طريقة اليوم هي خط أساس الغد",
};

// Same polish as English Kaizen; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "قلبات لكل شاشة",
    sub: "للأسفل, ثم للأعلى. هكذا كان يُفعل دائمًا.", until: "في هذا الدرس",
  },
  recap: {
    problem: "خدوش الشاشات من القلب", before: 15, after: 3, unit: "خدوش لكل 1,000 شاشة",
    fixedLabel: "صمد عند 90 يومًا",
    takeaways: [
      { text: "Kaizen عادة يومية", cue: "Kaizen عادة يومية" },
      { text: "اختبر صغيرًا؛ تأكد أن شيئًا آخر لم يسُؤ", cue: "اختبر على نطاق صغير" },
      { text: "وحّد كل مكسب", cue: "ووحّد كل مكسب" },
    ],
    action: { text: "اسأل عاملًا واحدًا ما الذي يجعل عمله صعبًا, واختبر حلًا صغيرًا واحدًا.", cue: "وهذه مهمتك" },
    next: { letter: "L", title: "Low Cost Automation", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_AR_DURATION = PLAN.total;

export const KaizenAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
