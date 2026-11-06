// Preview stills for a page lesson: the hook, the end of every page (all boxes
// and the picture in), mid-quiz, and the three outro beats. Renders them with
// `remotion still` and tiles them into out/preview/<Comp>_sheet.jpg.
//   node scripts/preview.ts mm [port]
import { execFileSync } from "node:child_process";
import { mkdirSync } from "node:fs";
import { join } from "node:path";
import { planLesson } from "../src/lessons/plan.ts";
import { PAGE_LESSONS, ROOT, loadLesson } from "./lessons.ts";

const [id, port = "3919"] = process.argv.slice(2);
const comp = PAGE_LESSONS[id];
if (!comp) throw new Error(`unknown lesson id "${id}"`);
const { blocks } = planLesson(loadLesson(id), 30);

const shots: [string, number][] = [["00_hook", 160]];
for (const b of blocks) {
  if (b.kind === "page") shots.push([b.key, b.start + b.dur - 30]);
  if (b.kind === "quiz") shots.push([b.key, b.start + 120]);
  if (b.kind === "outro") {
    shots.push(["zz_outro1", b.start + Math.round(b.dur * 0.35)]);
    shots.push(["zz_outro2", b.start + Math.round(b.dur * 0.62)]);
    shots.push(["zz_outro3", b.start + b.dur - 40]);
  }
}

const dir = join(ROOT, "out", "preview", comp);
mkdirSync(dir, { recursive: true });
// Build once into out/bundle_preview and keep Remotion's working files in
// out/tmp: something on this PC clears %TEMP%, which broke stills and renders.
const tmp = join(ROOT, "out", "tmp");
mkdirSync(tmp, { recursive: true });
const env = { ...process.env, TMP: tmp, TEMP: tmp, TMPDIR: tmp };
const run = (args: string[]) =>
  execFileSync("npx", args, { cwd: ROOT, env, stdio: ["ignore", "ignore", "inherit"], shell: true });
const bundle = join(ROOT, "out", "bundle_preview");
run(["remotion", "bundle", `--out-dir=${bundle}`, "--log=error"]);

const files = shots.map(([name]) => join(dir, `${name}.png`));
// a fresh port per still: reusing one port back to back sometimes read the
// previous server's half-closed reply (a JSON parse error) and failed
shots.forEach(([, frame], i) => {
  run(["remotion", "still", bundle, comp, files[i], `--frame=${frame}`, `--port=${Number(port) + 10 + i}`, "--log=error"]);
});

// contact sheet: 4 across
const cols = 4;
const rows = Math.ceil(files.length / cols);
const sheet = join(ROOT, "out", "preview", `${comp}_sheet.jpg`);
execFileSync("ffmpeg", [
  "-v", "error", "-y", ...files.flatMap((f) => ["-i", f]),
  "-filter_complex", `${files.map((_, i) => `[${i}]`).join("")}concat=n=${files.length}:v=1:a=0,scale=640:-1,tile=${cols}x${rows}:padding=6`,
  "-frames:v", "1", sheet,
]);
console.log(`${files.length} stills in out/preview/${comp}/, sheet: out/preview/${comp}_sheet.jpg`);
