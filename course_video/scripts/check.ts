// Pre-render safety check (run via `npm run check`, after tsc). Catches broken
// lessons in seconds instead of after a long render.
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { planLesson } from "../src/lessons/plan.ts";
import { PAGE_LESSONS, ROOT, loadLesson } from "./lessons.ts";

const errors: string[] = [];
const warnings: string[] = [];
const audio = (dir: string, key: string) => existsSync(join(ROOT, "public", "audio", dir, `${key}.mp3`));

for (const [id, comp] of Object.entries(PAGE_LESSONS)) {
  const err = (m: string) => errors.push(`${comp}: ${m}`);
  const warn = (m: string) => warnings.push(`${comp}: ${m}`);
  let data;
  try {
    data = loadLesson(id);
  } catch (e) {
    err(`cannot load lesson data (${(e as Error).message})`);
    continue;
  }
  const { blocks, total } = planLesson(data, 30);
  const used = new Set<string>();

  for (const k of ["intro", "outro"]) if (!(k in data.timings)) err(`no timing for "${k}"`);
  for (const p of data.pages) if (!(p.key in data.timings)) err(`no timing for page "${p.key}"`);
  for (const p of data.pages) {
    if (p.bullets.length < 2 || p.bullets.length > 6) err(`page "${p.key}" has ${p.bullets.length} bullets (2-6)`);
    if (!p.at || p.exampleAt === undefined) warn(`page "${p.key}" boxes are not synced to the voice (no cue timings)`);
    else if (p.at.length !== p.bullets.length) err(`page "${p.key}" has ${p.bullets.length} bullets but ${p.at.length} cue times`);
  }

  for (const b of blocks) {
    for (const c of b.clips) {
      used.add(c.key);
      if (!audio(id, c.key)) err(`missing audio public/audio/${id}/${c.key}.mp3`);
      if (b.captions && !data.words[c.key]?.length) err(`missing caption words for "${c.key}"`);
    }
  }

  const pageKeys = new Set(data.pages.map((p) => p.key));
  if (data.quizzes.length !== 2) err(`has ${data.quizzes.length} quizzes (every lesson needs 2)`);
  for (const q of data.quizzes) {
    if (!pageKeys.has(q.after)) err(`quiz "${q.key}" is placed after unknown page "${q.after}"`);
    if (q.correct < 0 || q.correct >= q.options.length) err(`quiz "${q.key}" correct index out of range`);
    const hasQ = `${q.key}_q` in data.timings, hasA = `${q.key}_a` in data.timings;
    if (hasQ !== hasA) err(`quiz "${q.key}" has only one of its _q/_a clips`);
    if (!hasQ) warn(`quiz "${q.key}" is silent (no ${q.key}_q/_a clips yet — clone and import them)`);
  }

  for (const k of Object.keys(data.timings)) if (!used.has(k)) warn(`timing "${k}" is not used by the timeline`);
  console.log(`${comp.padEnd(14)} ${blocks.length} blocks, ${(total / 30 / 60).toFixed(1)} min`);
}

// Root.tsx must register both the captioned and the Dub variant of each lesson.
const root = readFileSync(join(ROOT, "src", "Root.tsx"), "utf-8");
for (const comp of Object.values(PAGE_LESSONS)) {
  for (const id of [comp, `${comp}Dub`]) {
    if (!root.includes(`id="${id}"`)) errors.push(`Root.tsx: composition "${id}" is not registered`);
  }
}

for (const w of warnings) console.warn(`  warn  ${w}`);
for (const e of errors) console.error(`  ERROR ${e}`);
if (errors.length) {
  console.error(`\n${errors.length} error(s).`);
  process.exit(1);
}
console.log(`\nAll checks passed${warnings.length ? ` (${warnings.length} warning(s))` : ""}.`);
