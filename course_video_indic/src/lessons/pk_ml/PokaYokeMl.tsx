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
import words from "../../captions/pk_ml/words.json";

// Malayalam version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "തെറ്റായ ജോലി അസാധ്യമാക്കുക",
  outroLine: "ഒഴിവാക്കുക. തടയുക. പിടിക്കുക.",
  outroSub: "Poka Yoke — ക്വാളിറ്റിയെ ഓർമ്മയിൽ നിന്ന് മോചിപ്പിക്കുക",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_ML_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "റെക്കോർഡറുകൾ ഒരു സ്ക്രൂ ഇല്ലാതെ അയച്ചു",
    sub: "ഓപ്പറേറ്റർ കഴിവുള്ളവളും ശ്രദ്ധയുള്ളവളും. വെറും മനുഷ്യൻ.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "റെക്കോർഡറുകൾ സ്ക്രൂ ഇല്ലാതെ അയച്ചു", before: 18, after: 1, unit: "10,000 യൂണിറ്റിൽ",
    takeaways: [
      { text: "തെറ്റുകൾ മുൻകൂട്ടി കാണാം: ഡിസൈനിലൂടെ ഒഴിവാക്കുക", cue: "തെറ്റുകൾ മുൻകൂട്ടി കാണാം" },
      { text: "ആദ്യം തടയുക, പിന്നെ പിടിക്കുക, പിന്നെ മുന്നറിയിപ്പ്", cue: "മുന്നറിയിപ്പിനേക്കാൾ നല്ലത്" },
      { text: "ഓരോ ഡിവൈസും മോശം സാമ്പിൾ കൊണ്ട് പരിശോധിക്കുക", cue: "ഓരോ ഡിവൈസും" },
    ],
    action: { text: "ഓർമ്മയെ ആശ്രയിക്കുന്ന ഒരു ചെക്ക് കണ്ടെത്തി, അതിനൊരു Poka Yoke സ്കെച്ച് ചെയ്യുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "Q", title: "QRQC", cue: "അടുത്തതായി, നിങ്ങൾ QRQC" },
  },
};

export const PokaYokeMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
