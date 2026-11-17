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
import words from "../../captions/dt_ml/words.json";

// Malayalam version of DesignThinkingMl (same design and polish as the English lesson).
// All data comes from narration/design_thinking_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "ശരിയായ പ്രശ്നം പരിഹരിക്കുക, ജോലി ചെയ്യുന്നവരോടൊപ്പം",
  outroLine: "നിരീക്ഷിക്കുക. നിർവചിക്കുക. ചെറുതായി പരീക്ഷിക്കുക.",
  outroSub: "Design Thinking — ആദ്യം ആളുകൾ, എപ്പോഴും തെളിവ്",
};

// Same polish as English DesignThinking; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "ഓരോ 1,000 പമ്പിലും ലേബൽ തെറ്റുകൾ",
    sub: "ആദ്യ ആശയം: വിലയേറിയ ഒരു വേഗമേറിയ പ്രിന്റർ. പാക്കർമാരോട് ആരും ചോദിച്ചില്ല.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ഇൻഫ്യൂഷൻ പമ്പ് പാക്കിങ്ങിൽ ലേബൽ തെറ്റുകൾ", before: 12, after: 2, unit: "1,000 പമ്പിന്",
    takeaways: [
      { text: "ആളുകളിൽ നിന്ന് തുടങ്ങുക; തീരുമാനത്തിന് മുമ്പ് നിരീക്ഷിക്കുക", cue: "ജോലി ചെയ്യുന്നവരിൽ നിന്ന്" },
      { text: "ആവശ്യം നിർവചിക്കുക, അതിൽ പരിഹാരമില്ലാതെ", cue: "ഒരു പരിഹാരവും ഒളിപ്പിക്കാത്ത" },
      { text: "ചെറുതായി പരീക്ഷിക്കുക: ഫലവും യഥാർത്ഥ ഉപയോഗവും", cue: "ചെറിയ തോതിൽ പരീക്ഷിക്കുക" },
    ],
    action: { text: "ബുദ്ധിമുട്ടുള്ള ഒരു ജോലിയുടെ പത്ത് സൈക്കിൾ നിരീക്ഷിച്ച്, അത് ചെയ്യുന്ന മൂന്ന് പേരോട് സംസാരിക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "E", title: "Elimination of Waste", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_ML_DURATION = PLAN.total;

export const DesignThinkingMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
