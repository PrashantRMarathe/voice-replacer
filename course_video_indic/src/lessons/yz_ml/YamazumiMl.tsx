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
import words from "../../captions/yz_ml/words.json";

// Malayalam version of YamazumiMl (same design and polish as the English lesson).
// All data comes from narration/yamazumi_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "യഥാർത്ഥ ഡാറ്റ കൊണ്ട്, TAKT-നെതിരെ ലൈൻ ബാലൻസ് ചെയ്യുക",
  outroLine: "അളക്കുക. അടുക്കുക. ബാലൻസ് ചെയ്യുക.",
  outroSub: "Yamazumi — ഡിസൈൻ കൊണ്ട് നിലനിൽക്കുന്ന ഫ്ലോ",
};

// Same polish as English Yamazumi; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "ഓപ്പറേറ്റർമാർ കാത്തിരിക്കുന്നു, ഒരാൾ സ്ക്രൂകളിൽ മുങ്ങുമ്പോൾ",
    sub: "ആരും മടിയന്മാരല്ല. ജോലി അസമമായി കൂടിക്കിടക്കുന്നു എന്ന് മാത്രം.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "സ്റ്റേഷൻ B, TAKT-ന് മുകളിൽ", before: 35, after: 30, unit: "സ്റ്റേഷൻ B-യിലെ ജോലിയുടെ സെക്കൻഡ്",
    fixedLabel: "പിന്നെ TAKT-ൽ",
    takeaways: [
      { text: "യഥാർത്ഥ ജോലി അളക്കുക, ഏറ്റവും നല്ല കേസല്ല", cue: "യഥാർത്ഥ ജോലി അളക്കുക" },
      { text: "TAKT-നെതിരെ അടുക്കുക, കൂമ്പാരം കാണുക", cue: "അതിനെ TAKT-നെതിരെ" },
      { text: "സേഫ്റ്റിയോ ക്വാളിറ്റിയോ പണയം വെക്കാതെ ബാലൻസ്", cue: "ശ്രദ്ധയോടെ വീണ്ടും" },
    ],
    action: { text: "നിങ്ങളുടെ ലൈനിലെ ഒരു സ്റ്റേഷന്റെ സമയം അളന്ന്, TAKT-നെതിരെ അതിന്റെ ബാർ വരയ്ക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "Z", title: "Zero Defects", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_ML_DURATION = PLAN.total;

export const YamazumiMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
