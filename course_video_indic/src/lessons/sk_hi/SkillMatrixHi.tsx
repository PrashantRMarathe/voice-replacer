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
import words from "../../captions/sk_hi/words.json";

// hi version of SkillMatrixHi (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "कौन सच में कौन-सा काम कर सकता है — और गैप कहाँ हैं",
  outroLine: "जाँचें। ट्रेन करें। कवर करें।",
  outroSub: "Skill Matrix — क्षमता का जीवित कंट्रोल",
};

// Same polish as English SkillMatrix; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "व्यक्ति जो लेंस फ़ोकस सेट कर सकता है",
    sub: "बाला बीमार था। दस बजे तक, पूरा सेल रुक गया।", until: "इस लेसन में",
  },
  recap: {
    problem: "एक लेंस फ़ोकस एक्सपर्ट, और वह बीमार", before: 1, after: 2, unit: "योग्य लेंस फ़ोकस एक्सपर्ट",
    takeaways: [
      { text: "साबित क्षमता, हाज़िरी नहीं", cue: "स्किल मैट्रिक्स साबित" },
      { text: "हर शिफ़्ट योग्य बैकअप गिनें", cue: "हर ज़रूरी काम" },
      { text: "इसे ज़िंदा रखें, सबूत के साथ", cue: "और इसे ज़िंदा" },
    ],
    action: { text: "अपने तीन सबसे ज़रूरी स्टेशन लिखें, और हर एक के लिए योग्य लोग गिनें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "T", title: "TAKT Time", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_HI_DURATION = PLAN.total;

export const SkillMatrixHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
