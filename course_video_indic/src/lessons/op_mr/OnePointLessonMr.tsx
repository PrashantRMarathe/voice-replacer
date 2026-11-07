import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { ensureIndicFont } from "../../indicFonts";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/op_mr/words.json";

// Marathi version of OnePointLessonMr (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "एक विषय. एक स्पष्ट पॉइंट. एक चांगलं काम.",
  outroLine: "सोपं. व्हिज्युअल. बरोबर.",
  outroSub: "One Point Lesson — एक पॉइंट नीट शिकवा",
};

// Same polish as English OnePointLesson; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "कनेक्टर उलटा लागला, आणि तुटला",
    sub: "डे शिफ्टला पद्धत माहीत होती. कोणी सांगितलं नव्हतं.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "नाइट शिफ्टमध्ये तुटणारे कनेक्टर", before: 14, after: 1, unit: "तुटलेले कनेक्टर प्रति आठवडा",
    takeaways: [
      { text: "एक विषय, एक पॉइंट, एक प्रभावी व्हिज्युअल", cue: "एक विषय" },
      { text: "Gemba वर शिकवा, मग काम पाहा", cue: "हे Gemba वर" },
      { text: "हे सध्याच्या स्टँडर्डशी जुळवून ठेवा", cue: "आणि हे कंट्रोलमध्ये" },
    ],
    action: { text: "वारंवार होणारी एक चूक निवडा, आणि तिच्यासाठी One Point Lesson चा ड्राफ्ट बनवा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "P", title: "Poka Yoke", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_MR_DURATION = PLAN.total;

export const OnePointLessonMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
