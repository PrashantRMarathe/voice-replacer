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
import words from "../../captions/fm_ml/words.json";

// Malayalam version of FMEAMl (same design and polish as the English lesson).
// All data comes from narration/fmea_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "ഫെയിലിയർ മോഡ് ആൻഡ് ഇഫക്റ്റ്സ് അനാലിസിസ്: ഫെയിലിയറിന് മുമ്പ് ചിന്തിക്കുക",
  outroLine: "ചെയിൻ ഉണ്ടാക്കുക. സ്കോർ നൽകുക. തടയുക.",
  outroSub: "FMEA — ജീവനുള്ള പ്ലാൻ, ഫോമല്ല",
};

// Same polish as English FMEA; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "ഔട്ട്ഡോർ റേഡിയോകൾ വെള്ളം നിറഞ്ഞ് തിരിച്ചുവന്നു",
    sub: "രണ്ടിൽ ഗാസ്കറ്റില്ല, നാലിൽ മടങ്ങി. എല്ലാം ഫൈനൽ ഇൻസ്പെക്ഷൻ പാസായിരുന്നു.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ഔട്ട്ഡോർ 5G റേഡിയോയിൽ ഗാസ്കറ്റ് റിസ്ക്", before: 240, after: 32, unit: "റിസ്ക് പ്രയോറിറ്റി നമ്പർ",
    fixedLabel: "റിസ്ക് കുറഞ്ഞു, ട്രയലിൽ തെളിഞ്ഞു",
    takeaways: [
      { text: "ഇഫക്റ്റ് → ഫെയിലിയർ മോഡ് → നിയന്ത്രിക്കാവുന്ന കാരണം", cue: "വ്യക്തമായ ഒരു ചെയിൻ" },
      { text: "തെളിവോടെ സ്കോർ; നമ്പറിന് മുകളിൽ വിവേകം", cue: "തെളിവോടെ സ്കോർ" },
      { text: "ആദ്യം പ്രതിരോധം, തെളിയിക്കുക, പിന്നെ വീണ്ടും സ്കോർ", cue: "പ്രതിരോധം തിരഞ്ഞെടുക്കുക" },
    ],
    action: { text: "ഒരു പ്രധാന പടി തിരഞ്ഞെടുത്ത്, ടീമിനൊപ്പം അതിന്റെ ഫെയിലിയർ ചെയിൻ എഴുതുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "G", title: "Gemba", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_ML_DURATION = PLAN.total;

export const FMEAMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
