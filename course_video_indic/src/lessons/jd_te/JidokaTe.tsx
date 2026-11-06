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
import words from "../../captions/jd_te/words.json";

// Telugu version of JidokaTe (same design and polish as the English lesson).
// All data comes from narration/jidoka_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "మానవ స్పర్శ ఉన్న ఆటోమేషన్",
  outroLine: "చూడండి. ఆపండి. పరిష్కరించండి.",
  outroSub: "Jidoka — ఏ డిఫెక్టూ ముందుకు కాదు, ఏ అసాధారణతా దాగదు",
};

// Same polish as English Jidoka; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "పేషెంట్ మానిటర్ల మీద పలుచని సీల్",
    sub: "డిస్పెన్సర్ రాత్రంతా బాగా నడిచింది. దాని నాజిల్ సగం మూసుకుపోయింది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "మూసుకున్న అడ్హెసివ్ నాజిల్ వల్ల పలుచని సీల్", before: 140, after: 1, unit: "మానిటర్ల మీద ప్రభావం, ఒక్కో నాజిల్ సమస్యకు",
    fixedLabel: "సోర్స్ వద్ద పట్టుబడింది",
    takeaways: [
      { text: "ముందు సాధారణం నిర్ణయించండి", cue: "ముందు సాధారణం" },
      { text: "పట్టుకోండి, ఆపండి, కంటైన్ చేయండి: ఏ డిఫెక్టూ ముందుకు కాదు", cue: "సోర్స్ వద్దే" },
      { text: "ప్రతి ఆగిపోవడం ఒక పాఠం: రూట్ కాజ్ సరిచేయండి", cue: "ప్రతి ఆగిపోవడాన్ని" },
    ],
    action: { text: "ఒక ఆటోమేటిక్ ప్రాసెస్ ఎంచుకుని, అది దేని మీద ఆగాలో రాయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "K", title: "Kaizen", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_TE_DURATION = PLAN.total;

export const JidokaTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
