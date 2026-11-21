// Export .srt subtitle files for page lessons, timed to the exact video
// timeline (same planLesson + caption line splitting as the burned captions).
// Upload these next to the ...Dub (no-caption) render on course platforms.
//
//   node scripts/srt.ts            all page lessons
//   node scripts/srt.ts zd yz      just these
import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { planLesson, toLines } from "../src/lessons/plan.ts";
import { PAGE_LESSONS, ROOT, loadLesson } from "./lessons.ts";

const FPS = 30;
const TAIL = 0.4; // seconds a line lingers after its last word

const stamp = (t: number) => {
  const ms = Math.max(0, Math.round(t * 1000));
  const p = (n: number, w = 2) => String(n).padStart(w, "0");
  return `${p(Math.floor(ms / 3600000))}:${p(Math.floor(ms / 60000) % 60)}:${p(Math.floor(ms / 1000) % 60)},${p(ms % 1000, 3)}`;
};

const ids = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PAGE_LESSONS);
mkdirSync(join(ROOT, "out"), { recursive: true });

for (const id of ids) {
  const data = loadLesson(id);
  const { blocks } = planLesson(data, FPS);
  const cues: { s: number; e: number; text: string }[] = [];
  for (const b of blocks) {
    const blockEnd = (b.start + b.dur) / FPS;
    for (const c of b.clips) {
      const words = data.words[c.key];
      if (!words) continue; // includes quiz q/a narration, for accessibility
      const t0 = (b.start + c.from) / FPS;
      for (const l of toLines(words)) cues.push({ s: t0 + l.s, e: Math.min(t0 + l.e + TAIL, blockEnd), text: l.text });
    }
  }
  cues.sort((a, b) => a.s - b.s);
  for (let i = 0; i < cues.length - 1; i++) cues[i].e = Math.min(cues[i].e, cues[i + 1].s);

  const srt = cues.map((c, i) => `${i + 1}\n${stamp(c.s)} --> ${stamp(c.e)}\n${c.text}\n`).join("\n");
  const file = join(ROOT, "out", `${PAGE_LESSONS[id] ?? id}.srt`);
  writeFileSync(file, srt, "utf-8");
  console.log(`${file}  (${cues.length} cues)`);
}
