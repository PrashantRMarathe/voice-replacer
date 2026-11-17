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
import words from "../../captions/jd_ml/words.json";

// Malayalam version of JidokaMl (same design and polish as the English lesson).
// All data comes from narration/jidoka_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "മനുഷ്യസ്പർശമുള്ള ഓട്ടോമേഷൻ",
  outroLine: "കാണുക. നിർത്തുക. പരിഹരിക്കുക.",
  outroSub: "Jidoka — ഒരു ഡിഫെക്റ്റും മുന്നോട്ടില്ല, ഒരു തകരാറും മറയ്ക്കില്ല",
};

// Same polish as English Jidoka; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "പേഷ്യന്റ് മോണിറ്ററുകളിൽ നേർത്ത സീൽ",
    sub: "ഡിസ്പെൻസർ രാത്രി മുഴുവൻ നന്നായി ഓടി. അതിന്റെ നോസിൽ പകുതി അടഞ്ഞിരുന്നു.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "അടഞ്ഞ അഡ്ഹീസീവ് നോസിലിൽ നിന്ന് നേർത്ത സീൽ", before: 140, after: 1, unit: "ബാധിച്ച മോണിറ്ററുകൾ, ഓരോ നോസിൽ പ്രശ്നത്തിനും",
    fixedLabel: "ഉറവിടത്തിൽ പിടിച്ചു",
    takeaways: [
      { text: "ആദ്യം സാധാരണ നിർവചിക്കുക", cue: "ആദ്യം സാധാരണ" },
      { text: "കണ്ടെത്തുക, നിർത്തുക, കണ്ടെയ്ൻ: ഒരു ഡിഫെക്റ്റും മുന്നോട്ടില്ല", cue: "ഉറവിടത്തിൽ തന്നെ" },
      { text: "ഓരോ നിർത്തലും ഒരു പാഠം: റൂട്ട് കോസ് ശരിയാക്കുക", cue: "ഓരോ നിർത്തലും" },
    ],
    action: { text: "ഒരു ഓട്ടോമാറ്റിക് പ്രോസസ് തിരഞ്ഞെടുത്ത്, അത് എന്തിൽ നിൽക്കണമെന്ന് എഴുതുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "K", title: "Kaizen", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_ML_DURATION = PLAN.total;

export const JidokaMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
