// Pure timeline math shared by every page-based lesson, the SRT exporter and
// the check script. No React / Remotion imports, so Node can run it directly
// (node scripts/*.ts) and the video, captions and checks can never disagree.

export type Word = { w: string; s: number; e: number };
export type Page = {
  key: string; num: number; title: string; bullets: string[]; example: string;
  at?: number[];       // seconds into the page clip when each bullet is spoken
  exampleAt?: number;  // seconds into the page clip when the example is spoken
  visual?: Visual;     // picture beside the boxes (components/PageVisual.tsx)
};

// A page's picture: one layout + items that appear with their box (`with` =
// box index or "example"). Written in narration/<lesson>.py as `visual`.
export type VisualItem = {
  label: string;
  sub?: string;
  icon?: string;                       // name from components/visualIcons.tsx
  tone?: "good" | "bad" | "neutral";
  with?: number | "example";
  span?: number;                       // timeline: relative phase length
  value?: number;                      // bars: the bar's value
  cells?: (number | null)[];           // matrix: this row's levels (null = not trained/listed)
};
export type Visual = {
  type: "flow" | "ladder" | "icons" | "steps" | "versus" | "compare" | "stat" | "timeline" | "assembly" | "bars" | "doc" | "matrix";
  items?: VisualItem[];
  stop?: { after: number; label: string; with?: number | "example" };  // flow
  top?: string; bottom?: string;                                         // ladder
  before?: { label: string; value: number };                             // compare
  after?: { label: string; value: number };
  value?: number; label?: string; icon?: string;                         // stat
  prefix?: string; suffix?: string; decimals?: number; unit?: string; note?: string;
  with?: number | "example";                                             // compare/stat cue
  then?: Visual;    // switch to this picture at its own `with` cue (default: the example)
  cols?: string[];  // matrix: column headings (skills)
};
export type Quiz = {
  key: string;
  num: number;
  after: string;          // page key this quiz follows
  question: string;
  options: string[];
  correct: number;        // index of the correct option
  explanation: string;
  think?: number;         // seconds before the answer reveals
};

export type LessonData = {
  id: string;                         // audio/caption folder, e.g. "zd"
  timings: Record<string, number>;    // seconds per narrated clip
  pages: Page[];
  quizzes: Quiz[];
  words: Record<string, Word[]>;      // caption words per clip key
};

export const PAD = 2.2;          // seconds of hold after each narrated scene
export const QUIZ_LEAD = 1.2;    // seconds before the think countdown starts
export const QUIZ_HOLD = 7;      // seconds on the answer for a silent quiz
export const DEFAULT_THINK = 6;

export type Clip = { key: string; from: number };   // `from` = frames into block
export type Block = {
  key: string;
  kind: "intro" | "page" | "quiz" | "outro";
  start: number;     // absolute frame
  dur: number;       // frames
  clips: Clip[];     // narration clips that play in this block
  captions: boolean; // burn captions for this block's clips
  page?: Page;
  quiz?: Quiz & { think: number };
};

const frames = (s: number, fps: number) => Math.ceil(s * fps);
export const quizRevealFrame = (think: number, fps: number) => Math.round((QUIZ_LEAD + think) * fps);

// A quiz is narrated when its question clip (<key>_q) has a timing; otherwise it
// is a silent fixed-length block (e.g. before its clone clips are imported).
const quizBlock = (q: Quiz, t: Record<string, number>, fps: number) => {
  const qKey = `${q.key}_q`;
  const aKey = `${q.key}_a`;
  const narrated = qKey in t && aKey in t;
  const think = q.think ?? (narrated ? Math.max(4, Math.ceil(t[qKey])) : DEFAULT_THINK);
  const reveal = quizRevealFrame(think, fps);
  return {
    key: q.key,
    kind: "quiz" as const,
    dur: narrated ? reveal + frames(t[aKey] + PAD, fps) : reveal + Math.round(QUIZ_HOLD * fps),
    clips: narrated ? [{ key: qKey, from: 0 }, { key: aKey, from: reveal }] : [],
    captions: false, // quiz text is already on screen
    quiz: { ...q, think },
  };
};

export const planLesson = (d: LessonData, fps: number): { blocks: Block[]; total: number } => {
  const narrated = (key: string, kind: Block["kind"], page?: Page) => ({
    key, kind, page,
    dur: frames((d.timings[key] ?? 5) + PAD, fps),
    clips: [{ key, from: 0 }],
    captions: true,
  });

  const seq: Omit<Block, "start">[] = [narrated("intro", "intro")];
  for (const p of d.pages) {
    seq.push(narrated(p.key, "page", p));
    for (const q of d.quizzes) if (q.after === p.key) seq.push(quizBlock(q, d.timings, fps));
  }
  seq.push(narrated("outro", "outro"));

  let start = 0;
  const blocks = seq.map((b) => {
    const out = { ...b, start };
    start += b.dur;
    return out;
  });
  return { blocks, total: start };
};

// ---------- caption lines ----------
// Groups words into sentences, then splits long sentences into readable lines
// (prefer a comma/semicolon/dash near the middle) so each caption fits one line.
export type Line = { text: string; s: number; e: number };
export const MAX_LINE_CHARS = 72; // ~one line in the caption bar

// Never end a line on a little linking word ("how a | stacked chart").
const WEAK_END = /^(a|an|the|to|of|in|on|at|by|for|with|and|or|but|how|that|is|are|we|you|it|its|this|your)$/i;

const splitLong = (ws: Word[], max: number): Word[][] => {
  if (ws.length < 6 || ws.map((x) => x.w).join(" ").length <= max) return [ws];
  // score each cut by how evenly it splits the characters (in ~word units),
  // with a bonus for a cut after punctuation and a penalty for leaving a weak
  // word dangling at the end of the first line.
  const len = (xs: Word[]) => xs.map((x) => x.w).join(" ").length;
  const half = len(ws) / 2;
  let cut = Math.round(ws.length / 2);
  let best = Infinity;
  for (let i = 3; i <= ws.length - 3; i++) {
    const prev = ws[i - 1].w;
    const score = Math.abs(len(ws.slice(0, i)) - half) / 6
      - (/[,;:—–]$/.test(prev) ? 2.5 : 0)
      + (WEAK_END.test(prev.replace(/[^\w']/g, "")) ? 10 : 0);
    if (score < best) {
      best = score;
      cut = i;
    }
  }
  return [...splitLong(ws.slice(0, cut), max), ...splitLong(ws.slice(cut), max)];
};

export const toLines = (words: Word[], max = MAX_LINE_CHARS): Line[] => {
  const sentences: Word[][] = [];
  let buf: Word[] = [];
  for (const w of words) {
    buf.push(w);
    if (/[.!?।]["”']?$/.test(w.w)) {  // । = danda (Hindi, Marathi)
      sentences.push(buf);
      buf = [];
    }
  }
  if (buf.length) sentences.push(buf);
  return sentences
    .flatMap((s) => splitLong(s, max))
    .map((ws) => ({ text: ws.map((x) => x.w).join(" "), s: ws[0].s, e: ws[ws.length - 1].e }));
};
