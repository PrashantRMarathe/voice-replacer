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
import words from "../../captions/kz_te/words.json";

// Telugu version of KaizenTe (same design and polish as the English lesson).
// All data comes from narration/kaizen_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "చిన్న మార్పులు, ప్రతి రోజూ, పని చేసే మనుషుల నుంచి",
  outroLine: "చూడండి. చిన్నగా ప్రయత్నించండి. స్టాండర్డ్ చేయండి. మళ్లీ చేయండి.",
  outroSub: "Kaizen — ఈ రోజు అత్యుత్తమ పద్ధతి, రేపటి బేస్లైన్",
};

// Same polish as English Kaizen; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "సార్లు ప్రతి మానిటర్ తిప్పేవారు",
    sub: "ముఖం కిందకు, తర్వాత ముఖం పైకి. ఎప్పటి నుంచో ఇలాగే జరుగుతోంది.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "మానిటర్ తిప్పడం వల్ల ప్యానెల్ గీతలు", before: 15, after: 3, unit: "1,000 మానిటర్లకు గీతలు",
    fixedLabel: "90 రోజులకూ నిలిచింది",
    takeaways: [
      { text: "Kaizen రోజువారీ అలవాటు", cue: "Kaizen రోజువారీ" },
      { text: "చిన్నగా పరీక్షించండి; ఇంకేదీ చెడిపోలేదని చెక్ చేయండి", cue: "చిన్న స్థాయిలో" },
      { text: "ప్రతి లాభాన్ని స్టాండర్డ్ చేయండి", cue: "ప్రతి లాభాన్ని" },
    ],
    action: { text: "ఒక ఆపరేటరును తమ పనిలో కష్టం ఏమిటో అడిగి, ఒక చిన్న పరిష్కారం పరీక్షించండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "L", title: "Low Cost Automation", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_TE_DURATION = PLAN.total;

export const KaizenTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
