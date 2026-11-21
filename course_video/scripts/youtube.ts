// YouTube text for page lessons: title, description with chapters (from the same
// timeline the video uses), playlist order and the end-screen link.
//   node scripts/youtube.ts            all page lessons -> out/<Comp>_youtube.txt
//   node scripts/youtube.ts pk         one lesson
import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { planLesson } from "../src/lessons/plan.ts";
import { PAGE_LESSONS, ROOT, loadLesson } from "./lessons.ts";

// A-to-Z order (CLAUDE.md): letter + term per lesson id.
const SERIES: [string, string, string][] = [
  ["mm", "M", "Muda, Mura, Muri"], ["ni", "N", "Next Inspection"], ["op", "O", "One Point Lesson"],
  ["pk", "P", "Poka Yoke"], ["qr", "Q", "QRQC"], ["rc", "R", "Root Cause Analysis"],
  ["sk", "S", "Skill Training Matrix"], ["tt", "T", "TAKT Time"], ["up", "U", "Uniform Production"],
  ["vs", "V", "Value Stream Mapping"], ["ww", "W", "Why-Why Analysis"], ["xm", "X", "X-Matrix"],
  ["yz", "Y", "Yamazumi"], ["zd", "Z", "Zero Defects"],
];

const stamp = (frames: number) => {
  const s = Math.floor(frames / 30);
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;
};

const ids = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PAGE_LESSONS);
mkdirSync(join(ROOT, "out"), { recursive: true });

for (const id of ids) {
  const comp = PAGE_LESSONS[id];
  const pos = SERIES.findIndex(([i]) => i === id);
  if (!comp || pos < 0) {
    console.error(`skip ${id}: not a page lesson in the series`);
    continue;
  }
  const [, letter, term] = SERIES[pos];
  const next = SERIES[pos + 1];
  const { blocks } = planLesson(loadLesson(id), 30);

  // chapters: YouTube needs 0:00 first, 3+ chapters, each at least 10 s long
  const chapters: string[] = [];
  let lastStart = -Infinity;
  for (const b of blocks) {
    const name = b.kind === "intro" ? "Introduction"
      : b.kind === "outro" ? "Recap and your action"
      : b.kind === "quiz" ? `Quick check ${b.quiz!.num}`
      : b.page!.title;
    if (b.start - lastStart < 10 * 30) continue;
    chapters.push(`${stamp(b.start)} ${name}`);
    lastStart = b.start;
  }

  const text = [
    `TITLE: ${letter} is for ${term} | Lean Manufacturing A–Z`,
    "",
    "DESCRIPTION:",
    `${term}, explained with a real factory story in about ${Math.round(blocks[blocks.length - 1].start / 30 / 60) + 1} minutes.`,
    "Part of the Lean A–Z series by Factory Flow IQ.",
    "",
    "Chapters",
    ...chapters,
    "",
    next ? `Next: ${next[1]} is for ${next[2]}` : "This is the last letter of the series.",
    "",
    "PLAYLIST: Lean Manufacturing A–Z, position " + (pos + 1) + " of " + SERIES.length + " (in this order: " + SERIES.map((s) => s[1]).join(" ") + ")",
    `END SCREEN: link the ${next ? `${next[1]} (${next[2]})` : "playlist"} video over the last 20 seconds; the narration already announces it.`,
    "",
  ].join("\n");
  writeFileSync(join(ROOT, "out", `${comp}_youtube.txt`), text, "utf-8");
  console.log(`out/${comp}_youtube.txt  ${chapters.length} chapters`);
}
