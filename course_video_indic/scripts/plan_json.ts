// Print a lesson's timeline as JSON (seconds), for tools/validate_video.py.
//
//   node scripts/plan_json.ts gb_hi
import { planLesson } from "../src/lessons/plan.ts";
import { PAGE_LESSONS, loadLesson } from "./lessons.ts";

const FPS = 30;
const id = process.argv[2];
if (!id || !(id in PAGE_LESSONS)) {
  console.error(`unknown lesson id "${id}" (see scripts/lessons.ts)`);
  process.exit(1);
}
const data = loadLesson(id);
const { blocks, total } = planLesson(data, FPS);
console.log(JSON.stringify({
  id,
  comp: PAGE_LESSONS[id],
  total: total / FPS,
  clips: Object.keys(data.timings).length,
  blocks: blocks.map((b) => ({ key: b.key, kind: b.kind, start: b.start / FPS, dur: b.dur / FPS })),
}));
