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
import words from "../../captions/bd_ml/words.json";

// Malayalam version of BurnDownChartMl (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "ഡെഡ്ലൈനിന് മുമ്പ് ബാക്കി ജോലി കാണുക",
  outroLine: "ലൈൻ നിശ്ചയിക്കുക. ഗ്യാപ് കാണുക. ഇന്ന് നടപടി എടുക്കുക.",
  outroSub: "Burn Down Chart — ഇനി വെള്ളിയാഴ്ച ഞെട്ടലുകളില്ല",
};

// Same polish as English BurnDownChart; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "റൂട്ടറുകൾ ട്രക്കിൽ കയറിയില്ല",
    sub: "വെള്ളിയാഴ്ച ഉച്ച വരെ ആർക്കും സൂചന പോലും ഉണ്ടായിരുന്നില്ല.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ഡിസ്പാച്ചിൽ കുറഞ്ഞ റൂട്ടറുകൾ", before: 80, after: 0, unit: "റൂട്ടറുകൾ കുറവ്",
    takeaways: [
      { text: "ആദ്യം ഐഡിയൽ ലൈൻ; ഒരിക്കലും വീണ്ടും വരയ്ക്കരുത്", cue: "ആദ്യം ഐഡിയൽ ലൈൻ" },
      { text: "പൂർത്തിയായതും നല്ലതുമായ ജോലി മാത്രം എണ്ണുക", cue: "ശരിക്കും പൂർത്തിയായതും" },
      { text: "ഐഡിയലിന് മുകളിൽ? അന്നുതന്നെ നടപടി, ഓണറോടെ", cue: "ലൈൻ ഐഡിയലിന്" },
    ],
    action: { text: "ഡെഡ്ലൈനുള്ള ഒരു ജോലി തിരഞ്ഞെടുത്ത്, നാളത്തെ ഷിഫ്റ്റിന് മുമ്പ് അതിന്റെ ബേൺ-ഡൗൺ ഉണ്ടാക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "C", title: "Cycle Time Study", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_ML_DURATION = PLAN.total;

export const BurnDownChartMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
