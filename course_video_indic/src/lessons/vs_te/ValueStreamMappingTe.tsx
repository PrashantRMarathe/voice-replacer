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
import words from "../../captions/vs_te/words.json";

// Telugu version of ValueStreamMappingTe (same design and polish as the English lesson).
// All data comes from narration/value_stream_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "ఆర్డర్ నుండి డెలివరీ వరకు, పూర్తి ఫ్లో చూడండి",
  outroLine: "చూడండి. కొలవండి. ఫ్లో చేయండి.",
  outroSub: "Value Stream Mapping — వెయిటింగ్ వెతకండి, ఫ్లో డిజైన్ చేయండి",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "నిమిషాలు, ఒక సెట్-టాప్ బాక్స్ తయారీ, టెస్ట్ కు",
    sub: "అయినా కస్టమరును చేరడానికి దాదాపు నాలుగు రోజులు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "నిమిషాల పనికి రోజుల వెయిటింగ్", before: 4200, after: 2100, unit: "మూడు బఫర్లలో వేచి ఉన్న యూనిట్లు",
    fixedLabel: "ఫ్యూచర్ స్టేట్: సగం వెయిటింగ్",
    takeaways: [
      { text: "అసలు మెటీరియల్ + సమాచార ఫ్లో మ్యాప్", cue: "అసలు ఫ్లో మ్యాప్" },
      { text: "లీడ్ టైమ్ వెయిటింగ్ లో దాగి ఉంది, పనిలో కాదు", cue: "మీ లీడ్ టైమ్" },
      { text: "స్టాక్ తగ్గించే ముందు ఫ్యూచర్ స్టేట్ నిరూపించండి", cue: "మరియు ఏ స్టాక్" },
    ],
    action: { text: "ఒక ప్రొడక్ట్ ఫ్యామిలీతో డిస్పాచ్ నుండి వెనక్కి నడవండి, ప్రతి కుప్పను లెక్కించండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_TE_DURATION = PLAN.total;

export const ValueStreamMappingTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
