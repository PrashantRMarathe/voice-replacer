// Loads page-lesson data from disk for Node scripts (same JSON the video imports).
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import type { LessonData } from "../src/lessons/plan.ts";

export const ROOT = join(import.meta.dirname, "..");

// id -> composition name. Add a line here for every new page lesson.
export const PAGE_LESSONS: Record<string, string> = {
  a3_hi: "A3ProblemSolvingHi",
  dt_hi: "DesignThinkingHi",
  gb_hi: "GembaHi",
  hc_hi: "HanchoHi",
  op_hi: "OnePointLessonHi",
  pk_hi: "PokaYokeHi",
  qr_hi: "QrqcHi",
  up_hi: "UniformProductionHi",
  vs_hi: "ValueStreamMappingHi",
  ww_hi: "WhyWhyHi",
  xm_hi: "XMatrixHi",
  yz_hi: "YamazumiHi",
  zd_hi: "ZeroDefectsHi",
  pk_mr: "PokaYokeMr",
  qr_mr: "QrqcMr",
  a3_te: "A3ProblemSolvingTe",
  a3_ta: "A3ProblemSolvingTa",
};

const json = (p: string) => JSON.parse(readFileSync(join(ROOT, p), "utf-8"));

export const loadLesson = (id: string): LessonData => ({
  id,
  timings: json(`src/lessons/${id}/timings.json`),
  pages: json(`src/lessons/${id}/content.json`).pages,
  quizzes: existsSync(join(ROOT, `src/lessons/${id}/quizzes.json`))
    ? json(`src/lessons/${id}/quizzes.json`).quizzes
    : [],
  words: json(`src/captions/${id}/words.json`),
});
