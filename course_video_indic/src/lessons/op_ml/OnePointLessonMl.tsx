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
import words from "../../captions/op_ml/words.json";

// Malayalam version of OnePointLessonMl (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "ഒരു വിഷയം. ഒരു വ്യക്തമായ പോയിന്റ്. ഒരു മികച്ച ജോലി.",
  outroLine: "ലളിതം. വിഷ്വൽ. ശരി.",
  outroSub: "One Point Lesson — ഒരു പോയിന്റ് നന്നായി പഠിപ്പിക്കുക",
};

// Same polish as English OnePointLesson; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "കണക്ടർ തലതിരിച്ച് വെച്ചു, പൊട്ടി",
    sub: "ഡേ ഷിഫ്റ്റിന് രീതി അറിയാമായിരുന്നു. ആരും പറഞ്ഞില്ല.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "നൈറ്റ് ഷിഫ്റ്റിൽ പൊട്ടുന്ന കണക്ടറുകൾ", before: 14, after: 1, unit: "ആഴ്ചയിൽ പൊട്ടിയ കണക്ടർ",
    takeaways: [
      { text: "ഒരു വിഷയം, ഒരു പോയിന്റ്, ഒരു ശക്തമായ വിഷ്വൽ", cue: "ഒരു വിഷയം" },
      { text: "Gemba-യിൽ പഠിപ്പിക്കുക, പിന്നെ ജോലി നിരീക്ഷിക്കുക", cue: "ഇത് Gemba-യിൽ" },
      { text: "ഇത് നിലവിലെ സ്റ്റാൻഡേർഡുമായി യോജിപ്പിച്ച് നിർത്തുക", cue: "ഇത് കൺട്രോളിൽ" },
    ],
    action: { text: "ആവർത്തിക്കുന്ന ഒരു തെറ്റ് തിരഞ്ഞെടുത്ത്, അതിനായി ഒരു One Point Lesson-ന്റെ ഡ്രാഫ്റ്റ് ഉണ്ടാക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "P", title: "Poka Yoke", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_ML_DURATION = PLAN.total;

export const OnePointLessonMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
