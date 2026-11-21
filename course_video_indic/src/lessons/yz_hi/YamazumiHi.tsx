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
import words from "../../captions/yz_hi/words.json";

// Hindi version of YamazumiHi (same design and polish as the English lesson).
// All data comes from narration/yamazumi_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "असली डेटा से, TAKT के सामने लाइन बैलेंस करें",
  outroLine: "मापें। जमाएँ। बैलेंस करें।",
  outroSub: "Yamazumi — ऐसा फ़्लो, जो डिज़ाइन से टिके",
};

// Same polish as English Yamazumi; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "ऑपरेटर इंतज़ार में, जबकि एक स्क्रू में दबा है",
    sub: "कोई आलसी नहीं है। काम बस असमान रूप से जमा है।", until: "इस लेसन में",
  },
  recap: {
    problem: "स्टेशन B, TAKT से ऊपर", before: 35, after: 30, unit: "स्टेशन B पर काम के सेकंड",
    fixedLabel: "फिर TAKT पर",
    takeaways: [
      { text: "असली काम मापें, सबसे अच्छा केस नहीं", cue: "असली काम मापें" },
      { text: "TAKT के सामने जमाएँ, ढेर देखें", cue: "उसे TAKT के सामने" },
      { text: "सेफ़्टी या क्वालिटी दाँव पर लगाए बिना बैलेंस", cue: "और सावधानी से" },
    ],
    action: { text: "अपनी लाइन के एक स्टेशन का समय मापें, और TAKT के सामने उसका बार बनाएँ।", cue: "इस हफ़्ते आपका काम" },
    next: { letter: "Z", title: "Zero Defects", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_HI_DURATION = PLAN.total;

export const YamazumiHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
