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
import words from "../../captions/lc_te/words.json";

// Telugu version of LowCostAutomationTe (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_te.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_te",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "పని చేసే అతి సులభమైన సురక్షిత డివైస్",
  outroLine: "సులభం చేయండి. అవసరాన్ని ఆటోమేట్ చేయండి. నిరూపించండి.",
  outroSub: "Low Cost Automation — ఎప్పుడూ తక్కువ సేఫ్టీ కాదు",
};

// Same polish as English LowCostAutomation; cues are phrases from the Telugu intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "గంటకు మ్యాలెట్ దెబ్బలు, ప్రతి ఆపరేటర్",
    sub: "నొప్పి పుట్టే మణికట్లు, టెస్టులో గిలగిలలాడే వదులు గ్రిల్స్.", until: "ఈ పాఠంలో",
  },
  recap: {
    problem: "మ్యాలెట్ తో కూర్చోబెడితే వదులు స్పీకర్ గ్రిల్స్", before: 18, after: 2, unit: "1,000 స్పీకర్లకు",
    fixedLabel: "4 నెలల్లో పేబ్యాక్",
    takeaways: [
      { text: "ముందు సులభం చేయండి; వేస్టును ఎప్పుడూ ఆటోమేట్ చేయకండి", cue: "ముందు సులభం" },
      { text: "అతి సులభమైన సురక్షిత పరిష్కారం; సేఫ్టీ మొదటి గేట్", cue: "పని చేసే అతి సులభమైన" },
      { text: "అసలు లాభం నిరూపించండి, తర్వాత నిర్వహణ", cue: "అసలు లాభం" },
    ],
    action: { text: "పునరావృతమయ్యే ఒక కదలిక కనుక్కుని, ఆటోమేట్ చేసే ముందు దాన్ని తీసేయవచ్చా అని అడగండి.", cue: "ఈ వారం మీ పని" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "తర్వాత, మీరు" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_TE_DURATION = PLAN.total;

export const LowCostAutomationTe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("te");
  setUI("te");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
