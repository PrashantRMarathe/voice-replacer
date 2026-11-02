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
import words from "../../captions/jd_hi/words.json";

// hi version of JidokaHi (same design and polish as the English lesson).
// All data comes from narration/jidoka_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "इंसानी स्पर्श वाला ऑटोमेशन",
  outroLine: "देखें। रोकें। सुलझाएँ।",
  outroSub: "Jidoka — कोई डिफ़ेक्ट आगे नहीं, कोई गड़बड़ी छिपी नहीं",
};

// Same polish as English Jidoka; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "पेशेंट मॉनिटर पर पतली सील",
    sub: "डिस्पेंसर पूरी रात बढ़िया चला। उसका नोज़ल आधा बंद था।", until: "इस लेसन में",
  },
  recap: {
    problem: "बंद एडहेसिव नोज़ल से पतली सील", before: 140, after: 1, unit: "मॉनिटर पर असर, प्रति नोज़ल समस्या",
    fixedLabel: "सोर्स पर पकड़ा गया",
    takeaways: [
      { text: "पहले सामान्य तय करें", cue: "पहले सामान्य" },
      { text: "पकड़ें, रोकें, कंटेन करें: कोई डिफ़ेक्ट आगे नहीं", cue: "सोर्स पर ही" },
      { text: "हर रुकावट एक सबक: रूट कॉज़ ठीक करें", cue: "और हर रुकावट" },
    ],
    action: { text: "एक ऑटोमैटिक प्रोसेस चुनें, और लिखें कि उसे किस बात पर रुकना चाहिए।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "K", title: "Kaizen", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_HI_DURATION = PLAN.total;

export const JidokaHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
