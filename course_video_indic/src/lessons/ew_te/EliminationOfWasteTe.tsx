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
import words from "../../captions/ew_te/words.json";

// Telugu version of EliminationOfWasteTe (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "కస్టమర్ డబ్బు ఇవ్వనిదాన్ని తీసేయండి",
  outroLine: "చూడండి. కారణం తీసేయండి. నిరూపించండి.",
  outroSub: "Elimination of Waste — ఎక్కువ వాల్యూ, తక్కువ శ్రమ",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "సౌండ్ బార్లు ప్రతి నెల రీవర్క్",
    sub: "ఒక్కొక్కటి సరిచేయడానికి ₹42. ఎవరూ దీన్ని ఎప్పుడూ కూడలేదు.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "శబ్దం చేసే స్పీకర్ వైరు వల్ల రీవర్క్ అయ్యే సౌండ్ బార్లు", before: 1500, after: 300, unit: "నెలకు రీవర్క్", fixedLabel: "రీవర్క్ 80% తగ్గింది",
    takeaways: [
      { text: "వేస్ట్: కస్టమర్ డబ్బు ఇవ్వనిది", cue: "వేస్ట్ అంటే" },
      { text: "దీన్ని Gemba లో వాస్తవాలతో కనుక్కోండి", cue: "దీన్ని Gemba లో" },
      { text: "కారణం తీసేయండి, నిరూపించండి, నిలబెట్టండి", cue: "కారణం తీసేయండి" },
    ],
    action: { text: "ముప్పై నిమిషాలు మీ లైన్లో నడిచి, మూడు వేస్టులను వాస్తవాలుగా రాయండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "F", title: "FMEA", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_TE_DURATION = PLAN.total;

export const EliminationOfWasteTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
