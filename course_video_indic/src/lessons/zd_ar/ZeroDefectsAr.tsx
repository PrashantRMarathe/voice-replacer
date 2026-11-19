import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/zd_ar/words.json";

// Arabic version of ZeroDefectsAr (same design and polish as the English lesson).
// All data comes from narration/zero_defects_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "امنع العيوب, لا تكتفِ بالفحص عنها",
  outroLine: "امنع. قِس. حسّن.",
  outroSub: "Zero Defects: مدمجة في الإدارة اليومية",
};

// Same polish as English ZeroDefects; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "هاتف عاد لإعادة العمل",
    sub: "موصل واحد, مثبت بشكل سيئ. اجتاز كل فحص بصري.", until: "في هذا الدرس",
  },
  recap: {
    problem: "أعطال الشحن من موصل مثبت بشكل سيئ", before: 1200, after: 200,
    unit: "هاتف يفشل, من 40,000", fixedLabel: "صعب التكرار: أقل 83%",
    takeaways: [
      { text: "امنع العيوب, لا تكتفِ بالفحص", cue: "امنع العيوب" },
      { text: "قِس بصدق, بتعريفات واضحة", cue: "قِس بصدق" },
      { text: "أصلح النظام, لا الشخص", cue: "وعندما يفشل شيء" },
    ],
    action: { text: "اختر عيبًا واحدًا يعود باستمرار, واسأل كيف تجعله مستحيلًا.", cue: "وهذه مهمتك" },
    next: { letter: "Z", title: "Zero Defects", kicker: "اكتمل الدرس", cue: "إلى اللقاء في الدرس التالي" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_AR_DURATION = PLAN.total;

export const ZeroDefectsAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
