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
import words from "../../captions/ni_ml/words.json";

// Malayalam version of NextInspectionMl (same design and polish as the English lesson).
// All data comes from narration/next_inspection_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "അടുത്ത പ്രോസസ് എന്റെ കസ്റ്റമറാണ്",
  outroLine: "ഉണ്ടാക്കരുത്. അയയ്ക്കരുത്. സ്വീകരിക്കരുത്.",
  outroSub: "Next Inspection — അടുത്ത പ്രോസസിനെ സംരക്ഷിക്കുക",
};

// Same polish as English NextInspection; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "അയഞ്ഞ കണക്ടർ, സ്റ്റേഷൻ മൂന്നിൽ",
    sub: "ആരും ശ്രദ്ധിച്ചില്ല. പിന്നെ ഒരു കസ്റ്റമർ ബോക്സ് തുറന്നു.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "അടുത്ത സ്റ്റേഷനുകളിലേക്ക് പുറത്തുപോകുന്ന ഡിഫെക്റ്റുകൾ", before: 18, after: 3, unit: "ഓരോ ആഴ്ചയും എസ്കേപ്പ്",
    takeaways: [
      { text: "ഉണ്ടാക്കരുത്, അയയ്ക്കരുത്, സ്വീകരിക്കരുത്", cue: "ഡിഫെക്റ്റ് ഉണ്ടാക്കരുത്" },
      { text: "നേരത്തെ പരിശോധിക്കുക, വേഗം നടപടി", cue: "പ്രധാന പോയിന്റുകൾ എത്രയും" },
      { text: "കൺട്രോളുകൾ മുകളിലേക്ക് നീക്കിക്കൊണ്ടിരിക്കുക", cue: "നിങ്ങളുടെ കൺട്രോളുകൾ" },
    ],
    action: { text: "ഒരു ഹാൻഡ്ഓഫ് തിരഞ്ഞെടുത്ത്, അടുത്ത പ്രോസസിന് അതിൽ നിന്ന് എന്ത് വേണമെന്ന് എഴുതുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "O", title: "One Point Lesson", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_ML_DURATION = PLAN.total;

export const NextInspectionMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
