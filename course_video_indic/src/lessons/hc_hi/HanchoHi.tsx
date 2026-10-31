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
import words from "../../captions/hc_hi/words.json";

// Hindi version of HanchoHi (same design and polish as the English lesson).
// All data comes from narration/hancho_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "शॉप-फ़्लोर लीडरशिप, हर शिफ़्ट के हर घंटे",
  outroLine: "Gemba पर लीड करें। लोगों को तैयार करें।",
  outroSub: "Hancho — स्टैंडर्ड वापस लाएँ, हर दिन सुधारें",
};

// Same polish as English Hancho; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TV हर घंटे कम, पूरी एक शिफ़्ट तक",
    sub: "अगली सुबह की रिपोर्ट तक किसी को पता नहीं चला।", until: "इस लेसन में",
  },
  recap: {
    problem: "मॉडल चेंज के बाद आउटपुट गैप", before: 98, after: 120, unit: "TV प्रति घंटा",
    fixedLabel: "उसी शिफ़्ट में वापस",
    takeaways: [
      { text: "Gemba से लीड करें: स्टैंडर्ड बनाम असल", cue: "Gemba से लीड" },
      { text: "गैप हर घंटे दिखाएँ; उसी शिफ़्ट में कदम", cue: "हर गैप को" },
      { text: "लोगों को तैयार करें, ताकि लाइन आप पर न टिके", cue: "और अपने लोगों" },
    ],
    action: { text: "एक शिफ़्ट के लिए अपना लीडर स्टैंडर्ड वर्क लिखें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_HI_DURATION = PLAN.total;

export const HanchoHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
