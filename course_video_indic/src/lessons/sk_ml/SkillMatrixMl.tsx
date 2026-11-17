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
import words from "../../captions/sk_ml/words.json";

// Malayalam version of SkillMatrixMl (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "ആർക്ക് ശരിക്കും ഏത് ജോലി ചെയ്യാം — ഗ്യാപുകൾ എവിടെ",
  outroLine: "പരിശോധിക്കുക. ട്രെയിൻ ചെയ്യുക. കവർ ചെയ്യുക.",
  outroSub: "Skill Matrix — കഴിവിന്റെ ജീവനുള്ള കൺട്രോൾ",
};

// Same polish as English SkillMatrix; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "ലെൻസ് ഫോക്കസ് സെറ്റ് ചെയ്യാൻ കഴിയുന്ന ആൾ",
    sub: "ബാലയ്ക്ക് അസുഖമായിരുന്നു. പത്ത് മണിയോടെ, മുഴുവൻ സെല്ലും നിന്നു.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ഒരു ലെൻസ് ഫോക്കസ് വിദഗ്ധൻ, അയാൾക്ക് അസുഖം", before: 1, after: 2, unit: "യോഗ്യരായ ലെൻസ് ഫോക്കസ് വിദഗ്ധർ",
    takeaways: [
      { text: "തെളിഞ്ഞ കഴിവ്, ഹാജരല്ല", cue: "സ്കിൽ മാട്രിക്സ് തെളിയിച്ച" },
      { text: "ഓരോ ഷിഫ്റ്റിലും യോഗ്യ ബാക്കപ്പുകൾ എണ്ണുക", cue: "ഓരോ പ്രധാന ജോലിക്കും" },
      { text: "ഇതിനെ ജീവനോടെ നിർത്തുക, തെളിവോടെ", cue: "ഇതിനെ ജീവനോടെ" },
    ],
    action: { text: "നിങ്ങളുടെ ഏറ്റവും പ്രധാനപ്പെട്ട മൂന്ന് സ്റ്റേഷനുകൾ എഴുതി, ഓരോന്നിനും യോഗ്യരായവരെ എണ്ണുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "T", title: "TAKT Time", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_ML_DURATION = PLAN.total;

export const SkillMatrixMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
