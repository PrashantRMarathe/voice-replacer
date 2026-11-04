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
import words from "../../captions/zd_te/words.json";

// Telugu version of ZeroDefectsTe (same design and polish as the English lesson).
// All data comes from narration/zero_defects_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "డిఫెక్టులను ఆపండి — కేవలం చెక్ చేయకండి",
  outroLine: "ఆపండి. కొలవండి. మెరుగుపరచండి.",
  outroSub: "Zero Defects — రోజువారీ మేనేజ్‌మెంట్ లో భాగం",
};

// Same polish as English ZeroDefects; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "రీవర్క్ కోసం తిరిగి వచ్చిన ఫోన్లు",
    sub: "ఒక కనెక్టర్, తప్పుగా కూర్చుంది. అది ప్రతి విజువల్ చెక్ లో పాస్ అయింది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "తప్పుగా కూర్చున్న కనెక్టర్ వల్ల ఛార్జింగ్ ఫెయిల్యూర్లు", before: 1200, after: 200,
    unit: "ఫెయిల్ అయిన ఫోన్లు, 40,000 లో", fixedLabel: "పునరావృతం కష్టం: 83% తక్కువ",
    takeaways: [
      { text: "డిఫెక్టులను ఆపండి, కేవలం చెక్ కాదు", cue: "డిఫెక్టులను ఆపండి" },
      { text: "స్పష్టమైన నిర్వచనాలతో నిజాయితీగా కొలవండి", cue: "స్పష్టమైన నిర్వచనాలతో" },
      { text: "సిస్టమ్ ను సరిచేయండి, వ్యక్తిని కాదు", cue: "మరియు ఏదైనా ఫెయిల్" },
    ],
    action: { text: "పదే పదే తిరిగి వచ్చే ఒక డిఫెక్ట్ ఎంచుకోండి, దాన్ని అసాధ్యం ఎలా చేయాలో అడగండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "Z", title: "Zero Defects", kicker: "పాఠం పూర్తి", cue: "ఇప్పుడు వెళ్ళండి" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_TE_DURATION = PLAN.total;

export const ZeroDefectsTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
