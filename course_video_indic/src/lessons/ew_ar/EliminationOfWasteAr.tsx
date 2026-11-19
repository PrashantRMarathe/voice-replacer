import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ew_ar/words.json";

// Arabic version of EliminationOfWasteAr (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_ar.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_ar",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "أزل ما لن يدفع عميلك ثمنه",
  outroLine: "رَه. أزل السبب. أثبته.",
  outroSub: "Elimination of Waste: قيمة أكثر, جهد أقل",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Arabic intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "ساوندبار يُعاد للعمل كل شهر",
    sub: "₹42 لإصلاح كل واحد. ولم يجمع أحد هذه التكلفة قط.", until: "في هذا الدرس",
  },
  recap: {
    problem: "ساوندبار يُعاد للعمل بسبب سلك سماعة يطنّ", before: 1500, after: 300, unit: "إعادة عمل شهريًا", fixedLabel: "إعادة العمل انخفضت 80%",
    takeaways: [
      { text: "الهدر: ما لن يدفع العميل ثمنه", cue: "الهدر هو كل ما" },
      { text: "اكتشفه بالحقائق في Gemba", cue: "اكتشفه بالحقائق في Gemba" },
      { text: "أزل السبب, وأثبته, وحافظ عليه", cue: "وأزل السبب" },
    ],
    action: { text: "تجوّل في خطك ثلاثين دقيقة, واكتب ثلاثة أنواع من الهدر كحقائق.", cue: "وهذه مهمتك" },
    next: { letter: "F", title: "FMEA", cue: "في الدرس التالي ستتعرف على" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_AR_DURATION = PLAN.total;

export const EliminationOfWasteAr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("ar");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
