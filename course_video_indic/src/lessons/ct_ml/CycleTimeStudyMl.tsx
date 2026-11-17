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
import words from "../../captions/ct_ml/words.json";

// Malayalam version of CycleTimeStudyMl (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "യഥാർത്ഥ ജോലി അളക്കുക, യഥാർത്ഥ ബോട്ടിൽനെക്ക് കണ്ടെത്തുക",
  outroLine: "നിർവചനം. അളവ്. രീതിയിൽ മെച്ചം.",
  outroSub: "Cycle Time Study — വേഗത്തിന് മുമ്പ് തെളിവ്",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "സെക്കൻഡ്: ഓരോ സ്റ്റേഷനും വേണ്ടത്ര വേഗമെന്ന് തോന്നി",
    sub: "എന്നിട്ടും മോണിറ്റർ ലൈൻ ഷിഫ്റ്റുകൾ തോറും മണിക്കൂർ ടാർഗറ്റ് തെറ്റിച്ചു.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "ഡിസ്പ്ലേ-ടെസ്റ്റ് സ്റ്റേഷൻ TAKT-നേക്കാൾ പതുക്കെ", before: 28, after: 23, unit: "മോണിറ്ററിന് സെക്കൻഡ്, സ്റ്റേഷൻ C-യിൽ", fixedLabel: "ഇപ്പോൾ TAKT-ന് ഉള്ളിൽ",
    takeaways: [
      { text: "ആദ്യം ബൗണ്ടറി നിശ്ചയിക്കുക", cue: "ആദ്യം ബൗണ്ടറി" },
      { text: "ശരാശരി മാത്രമല്ല, വ്യാപനം നോക്കുക", cue: "ശരാശരി മാത്രമല്ല" },
      { text: "രീതി ശരിയാക്കുക, ക്വാളിറ്റി ചെക്ക് ഒരിക്കലും ഒഴിവാക്കരുത്", cue: "ബോട്ടിൽനെക്കിൽ രീതി" },
    ],
    action: { text: "ഒരു സ്റ്റേഷനിൽ പത്ത് സൈക്കിൾ അളന്ന്, ഏറ്റവും നീണ്ടതിനെ TAKT-മായി താരതമ്യം ചെയ്യുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "D", title: "Design Thinking", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_ML_DURATION = PLAN.total;

export const CycleTimeStudyMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
