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
import words from "../../captions/a3_ml/words.json";

// Malayalam version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "പ്രശ്നത്തിന്റെ മുഴുവൻ കഥ, ഒരു പേജിൽ",
  outroLine: "ഗ്യാപ് കാണുക. കാരണം തെളിയിക്കുക. നിലനിർത്തുക.",
  outroSub: "A3 — മികച്ച ചിന്ത, ഒരു ഷീറ്റിൽ",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_ML_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "സെർവറുകൾ ആദ്യ ബൂട്ട് ടെസ്റ്റിൽ ഫെയിൽ",
    sub: "നാല് ആഴ്ചയിൽ. ആദ്യ നിർദ്ദേശം: രണ്ട് ഇൻസ്പെക്ടർമാർ കൂടി.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ആദ്യ ബൂട്ട് ടെസ്റ്റിൽ ഫെയിലാകുന്ന സെർവറുകൾ", before: 48, after: 16, unit: "1,000 സെർവറിന്", fixedLabel: "ടാർഗറ്റ് നേടി: 48-ന് താഴെ",
    takeaways: [
      { text: "അളക്കാവുന്ന ഒരു ഗ്യാപിൽ നിന്ന് തുടങ്ങുക", cue: "അളക്കാവുന്ന ഒരു ഗ്യാപിൽ" },
      { text: "പോയി കാണുക; ഓരോ കാരണവും തെളിയിക്കുക", cue: "പോയി കാണുക" },
      { text: "പൈലറ്റിൽ തെളിഞ്ഞത് മാത്രം സ്റ്റാൻഡേർഡ്", cue: "പൈലറ്റ് ശരിക്കും തെളിയിച്ചത്" },
    ],
    action: { text: "ആവർത്തിക്കുന്ന ഒരു പ്രശ്നം തിരഞ്ഞെടുത്ത്, അതിന്റെ പ്രോബ്ലം സ്റ്റേറ്റ്മെന്റ് A3-യിൽ എഴുതുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "B", title: "Burn Down Chart", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

export const A3ProblemSolvingMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
