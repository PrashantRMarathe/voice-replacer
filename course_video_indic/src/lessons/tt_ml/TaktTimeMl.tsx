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
import words from "../../captions/tt_ml/words.json";

// Malayalam version of TaktTimeMl (same design and polish as the English lesson).
// All data comes from narration/takt_time_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "നിങ്ങളുടെ കസ്റ്റമർ നിശ്ചയിക്കുന്ന ഹൃദയമിടിപ്പ്",
  outroLine: "അളക്കുക. ബാലൻസ് ചെയ്യുക. ഫ്ലോ ഉണ്ടാക്കുക.",
  outroSub: "TAKT Time — കസ്റ്റമറുടെ വേഗം",
};

// Same polish as English TaktTime; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "ക്യാമറകൾ ടെസ്റ്റിന് മുന്നിൽ ഉണ്ടാക്കി",
    sub: "ഓരോ സ്റ്റേഷനും തിരക്കിൽ. ട്രക്ക് എന്നിട്ടും വൈകി.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "തിരക്കുള്ള ലൈൻ, എന്നിട്ടും ട്രക്ക് തെറ്റുന്നു", before: 0, after: 10, unit: "സെക്കൻഡ്: ദിവസം 7,200 ക്യാമറയുടെ ഹൃദയമിടിപ്പ്",
    fixedLabel: "എല്ലാവരും ഓടുന്ന വേഗം",
    takeaways: [
      { text: "TAKT = നെറ്റ് ലഭ്യമായ സമയം ÷ ഡിമാൻഡ്", cue: "TAKT എന്നാൽ നെറ്റ്" },
      { text: "വേണ്ട വേഗം, സ്റ്റേഷന്റെ സമയമല്ല", cue: "ഇത് നിങ്ങൾക്ക് വേണ്ട" },
      { text: "യഥാർത്ഥ നഷ്ടം കൊണ്ട് പ്ലാൻ, സിദ്ധാന്തം കൊണ്ടല്ല", cue: "യഥാർത്ഥ നഷ്ടങ്ങൾ" },
    ],
    action: { text: "ഒരു ലൈനിന്റെ TAKT കണക്കാക്കി, അതിനെ ഏറ്റവും പതുക്കെയുള്ള സ്റ്റേഷനുമായി താരതമ്യം ചെയ്യുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "U", title: "Uniform Production", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_ML_DURATION = PLAN.total;

export const TaktTimeMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
