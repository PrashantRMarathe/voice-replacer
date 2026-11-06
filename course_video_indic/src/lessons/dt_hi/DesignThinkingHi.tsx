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
import words from "../../captions/dt_hi/words.json";

// Hindi version of DesignThinkingHi (same design and polish as the English lesson).
// All data comes from narration/design_thinking_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "सही समस्या सुलझाएँ, काम करने वालों के साथ",
  outroLine: "देखें। परिभाषित करें। छोटा परखें।",
  outroSub: "Design Thinking — पहले लोग, हमेशा सबूत",
};

// Same polish as English DesignThinking; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "हर 1,000 पंपों में लेबल गलतियाँ",
    sub: "पहला आइडिया: एक महँगा तेज़ प्रिंटर। पैकर्स से किसी ने पूछा ही नहीं।", until: "इस लेसन में",
  },
  recap: {
    problem: "इन्फ़्यूज़न पंप पैकिंग पर लेबल गलतियाँ", before: 12, after: 2, unit: "प्रति 1,000 पंप",
    takeaways: [
      { text: "लोगों से शुरू करें; फ़ैसले से पहले देखें", cue: "काम करने वाले लोगों से" },
      { text: "ज़रूरत परिभाषित करें, उसमें कोई हल नहीं", cue: "ज़रूरत को ऐसे" },
      { text: "छोटा परखें: नतीजे और असली इस्तेमाल", cue: "और छोटे स्तर पर" },
    ],
    action: { text: "किसी तकलीफ़ वाले काम के दस साइकिल देखें, और उसे करने वाले तीन लोगों से बात करें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "E", title: "Elimination of Waste", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_HI_DURATION = PLAN.total;

export const DesignThinkingHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
