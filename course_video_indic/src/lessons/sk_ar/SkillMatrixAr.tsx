import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/sk_ar/words.json";

// Arabic version of SkillMatrixAr (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "من يستطيع فعلًا أداء أي عمل, وأين الفجوات",
  outroLine: "قيّم. درّب. غطِّ.",
  outroSub: "Skill Matrix: تحكم حي بالقدرات",
};

// Same polish as English SkillMatrix; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "شخص يستطيع ضبط تركيز العدسة",
    sub: "اتصل بالا مريضًا. وبحلول العاشرة, توقفت الخلية كلها.", until: "في هذا الدرس",
  },
  recap: {
    problem: "خبير واحد لتركيز العدسة, وكان مريضًا", before: 1, after: 2, unit: "خبراء مؤهلون لتركيز العدسة",
    takeaways: [
      { text: "قدرة مثبتة, لا حضور", cue: "مصفوفة المهارات تُظهر" },
      { text: "عُدّ البدلاء المؤهلين, في كل وردية", cue: "عُدّ البدلاء المؤهلين" },
      { text: "أبقِها حية, بالدليل", cue: "وأبقِها حية" },
    ],
    action: { text: "اسرد أكثر ثلاث محطات حرجة لديك, وعُدّ المؤهلين لكل منها.", cue: "وهذه مهمتك" },
    next: { letter: "T", title: "TAKT Time", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_AR_DURATION = PLAN.total;

export const SkillMatrixAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
