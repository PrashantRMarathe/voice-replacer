// Loads page-lesson data from disk for Node scripts (same JSON the video imports).
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import type { LessonData } from "../src/lessons/plan.ts";

export const ROOT = join(import.meta.dirname, "..");

// id -> composition name. Add a line here for every new page lesson.
export const PAGE_LESSONS: Record<string, string> = {
  zd: "ZeroDefects",
  yz: "Yamazumi",
  xm: "XMatrix",
  up: "UniformProduction",
  vs: "ValueStreamMapping",
  ww: "WhyWhy",
  mm: "MudaMuraMuri",
  ni: "NextInspection",
  op: "OnePointLesson",
  pk: "PokaYoke",
  qr: "QRQC",
  rc: "RootCauseAnalysis",
  sk: "SkillMatrix",
  tt: "TaktTime",
  a3: "A3ProblemSolving",
  bd: "BurnDownChart",
  ct: "CycleTimeStudy",
  dt: "DesignThinking",
  ew: "EliminationOfWaste",
  fm: "FMEA",
  gb: "Gemba",
  hc: "Hancho",
  ik: "Ishikawa",
  jd: "Jidoka",
  kz: "Kaizen",
  lc: "LowCostAutomation",
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
