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
import words from "../../captions/hc_mr/words.json";

// Marathi version of HanchoMr (same design and polish as the English lesson).
// All data comes from narration/hancho_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "शॉप-फ्लोअर नेतृत्व, प्रत्येक शिफ्टच्या प्रत्येक तासाला",
  outroLine: "Gemba वर नेतृत्व करा. लोकांना तयार करा.",
  outroSub: "Hancho — स्टँडर्ड परत आणा, दररोज सुधारा",
};

// Same polish as English Hancho; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TV दर तासाला कमी, पूर्ण एका शिफ्टभर",
    sub: "दुसऱ्या सकाळच्या रिपोर्टपर्यंत कोणालाच कळलं नाही.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "मॉडेल चेंजनंतर आउटपुट गॅप", before: 98, after: 120, unit: "TV प्रति तास",
    fixedLabel: "त्याच शिफ्टमध्ये परत",
    takeaways: [
      { text: "Gemba वरून नेतृत्व: स्टँडर्ड विरुद्ध प्रत्यक्ष", cue: "Gemba वरून नेतृत्व" },
      { text: "गॅप दर तासाला दाखवा; त्याच शिफ्टमध्ये कृती", cue: "प्रत्येक गॅप" },
      { text: "लोकांना तयार करा, म्हणजे लाइन तुमच्यावर टिकणार नाही", cue: "आणि तुमच्या लोकांना" },
    ],
    action: { text: "एका शिफ्टसाठी तुमचं लीडर स्टँडर्ड वर्क लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_MR_DURATION = PLAN.total;

export const HanchoMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
