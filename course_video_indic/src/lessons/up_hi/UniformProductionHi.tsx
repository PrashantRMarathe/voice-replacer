import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { ensureIndicFont } from "../../indicFonts";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/up_hi/words.json";

// Hindi version of Uniform Production. All data comes from
// narration/uniform_production_hi.py (+ import_clones.py for the cloned voice).
const DATA: LessonData = {
  id: "up_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "यूनिफ़ॉर्म प्रोडक्शन",
  title: "यूनिफ़ॉर्म प्रोडक्शन",
  subtitle: "वॉल्यूम और मिक्स को लेवल करें — स्थिर, भरोसेमंद फ़्लो के लिए",
  outroLine: "लेवल करें। क्रम तय करें। स्थिर बनाएँ।",
  outroSub: "यूनिफ़ॉर्म प्रोडक्शन — ऐसी रफ़्तार, जो आपकी लाइन बनाए रख सके",
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_HI_DURATION = PLAN.total;

export const UniformProductionHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions} />;
};
