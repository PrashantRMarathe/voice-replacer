import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/rc_ar/words.json";

// Arabic version of RootCauseAnalysisAr (same design and polish as the English lesson).
// All data comes from narration/root_cause_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "من العَرَض إلى سبب يمكنك إثباته",
  outroLine: "عرّف. اختبر. امنع.",
  outroSub: "Root Cause Analysis: أثبته, ثم أصلحه",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "كاميرات فشلت في اختبار التركيز في صباح واحد",
    sub: "ثلاثة أشخاص, ثلاث إجابات مختلفة.", until: "في هذا الدرس",
  },
  recap: {
    problem: "كاميرات تفشل في التركيز بعد تغيير", before: 60, after: 12, unit: "عيوب لكل 20,000 كاميرا",
    takeaways: [
      { text: "عرّفها بحدة, واحمِ العميل", cue: "عرّف المشكلة بحدة" },
      { text: "كل سبب فرضية حتى يُختبر", cue: "تعامل مع كل سبب" },
      { text: "أصلح لماذا حدث, ولماذا تسرب", cue: "وأصلح الأمرين" },
    ],
    action: { text: "خذ مشكلة مغلقة واحدة, وتحقق هل اختُبر سببها الجذري فعلًا.", cue: "وهذه مهمتك" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_AR_DURATION = PLAN.total;

export const RootCauseAnalysisAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
