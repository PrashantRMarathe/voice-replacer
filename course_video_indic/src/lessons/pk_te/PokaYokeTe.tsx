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
import words from "../../captions/pk_te/words.json";

// Telugu version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "తప్పు పనిని అసాధ్యం చేయండి",
  outroLine: "తీసేయండి. ఆపండి. పట్టుకోండి.",
  outroSub: "Poka Yoke — క్వాలిటీని జ్ఞాపకశక్తి నుండి విడిపించండి",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_TE_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "రికార్డర్లు ఒక స్క్రూ లేకుండా పంపబడ్డాయి",
    sub: "ఆపరేటర్ నైపుణ్యం, జాగ్రత్త ఉన్నది. కేవలం మనిషి.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "తప్పిపోయిన స్క్రూతో పంపిన రికార్డర్లు", before: 18, after: 1, unit: "10,000 యూనిట్లకు",
    takeaways: [
      { text: "తప్పులను ఊహించవచ్చు: వాటిని డిజైన్ తో తీసేయండి", cue: "తప్పులను ముందే" },
      { text: "ముందు ఆపండి, తర్వాత పట్టుకోండి, తర్వాత హెచ్చరిక", cue: "హెచ్చరిక కంటే" },
      { text: "ప్రతి డివైస్ ను చెడ్డ శాంపిల్ తో పరీక్షించండి", cue: "మరియు ప్రతి డివైస్" },
    ],
    action: { text: "జ్ఞాపకశక్తి మీద ఆధారపడిన ఒక చెక్ వెతకండి, దానికోసం Poka Yoke స్కెచ్ వేయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "Q", title: "QRQC", cue: "తర్వాత, మీరు QRQC" },
  },
};

export const PokaYokeTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
