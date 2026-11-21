import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/mm_ar/words.json";

// Arabic version of MudaMuraMuriAr (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "الهدر والتفاوت والإجهاد الزائد: حسّن الثلاثة",
  outroLine: "سوِّ. احمِ. أزل.",
  outroSub: "3M: تدفق مستقر, لا ناس أسرع",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "كاميرا متأخرة, قبل ساعة من نهاية الوردية",
    sub: "الجميع يستعجلون. والأخطاء تتراكم عند الاختبار.", until: "في هذا الدرس",
  },
  recap: {
    problem: "خط سانجاي يتأخر كل يوم", before: 150, after: 0, unit: "دقيقة ساعات إضافية يوميًا",
    takeaways: [
      { text: "Muda الهدر, Mura التفاوت, Muri الإجهاد الزائد", cue: "Muda هو الهدر" },
      { text: "إنها تغذي بعضها: حسّنها معًا", cue: "إنها تغذي بعضها" },
      { text: "تدفق مستقر, لا ناس أسرع", cue: "والهدف تدفق مستقر" },
    ],
    action: { text: "تتبّع منتجًا واحدًا عبر خطك, وسجّل مثالًا واحدًا لكل M.", cue: "وهذه مهمتك" },
    next: { letter: "N", title: "Next Inspection", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_AR_DURATION = PLAN.total;

export const MudaMuraMuriAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
