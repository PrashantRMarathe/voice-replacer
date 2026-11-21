import React from "react";
import {
  AbsoluteFill, Audio, Sequence, staticFile,
  interpolate, spring, useCurrentFrame, useVideoConfig,
} from "remotion";
import { Background } from "../../components/Background";
import { RiseIn } from "../../components/ui";
import { Scene } from "../../scenes/Scene";
import { Captions } from "../../components/Captions";
import { QuizScene } from "../../components/Quiz";
import { Guide } from "../../components/characters";
import { BrandMark } from "../../components/BrandMark";
import { PageVisual } from "../../components/PageVisual";
import { Polish, PolishProvider, usePolish, Sfx, CountText, ActingGuide, IntroHook, RecapOutro, cueTime } from "./polish";
import { theme } from "../../theme";
import type { Block, LessonData, Page } from "../plan";
import "../../fonts";

// Shared building blocks for "page" lessons (intro → N pages + quizzes → outro).
// A lesson file supplies its data + titles; it can still pass its own scene
// node for any block via `renderBlock` when it needs a custom visual.

export type LessonText = {
  label: string;      // page header, e.g. "ZERO DEFECTS"
  title: string;      // intro title
  subtitle: string;   // intro subtitle
  outroLine: string;  // outro headline
  outroSub: string;   // outro sub-line
};

// ---------- Intro ----------
export const IntroScene: React.FC<{ text: LessonText }> = ({ text }) => {
  const { polish, words } = usePolish();
  if (polish.hook) {
    const until = cueTime(words.intro, polish.hook.until) ?? 12;
    return <IntroHook hook={polish.hook} until={until}><IntroTitle text={text} /></IntroHook>;
  }
  return <IntroTitle text={text} />;
};

const IntroTitle: React.FC<{ text: LessonText }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const line = spring({ frame: frame - 16, fps, config: { damping: 20 } });
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 30, letterSpacing: 8, textAlign: "center" }}>
          {theme.brand.courseName.toUpperCase()}
        </div>
      </RiseIn>
      <RiseIn delay={10}>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 112, fontWeight: 700, textAlign: "center", marginTop: 8, textShadow: `0 0 40px ${theme.colors.accent}55` }}>
          {text.title}
        </div>
      </RiseIn>
      <div style={{ height: 6, width: interpolate(line, [0, 1], [0, 460]), background: theme.colors.accent, borderRadius: 4, marginTop: 28, boxShadow: `0 0 24px ${theme.colors.accent}` }} />
      <RiseIn delay={26}>
        <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 32, marginTop: 26 }}>
          {text.subtitle}
        </div>
      </RiseIn>
      <div style={{ position: "absolute", left: 90, bottom: 40 }}>
        <Guide size={320} delay={20} fromX={-180} />
      </div>
    </Scene>
  );
};

// ---------- A page (data-driven) ----------
// Each bullet rises in when the voice reaches it (page.at, from its cue in the
// script) and the one being explained is outlined; the example follows the same
// rule. Without timings (an unsynced draft) they fall back to a fixed stagger.
const LEAD = 4; // frames a box starts rising before its word is spoken

export const PageScene: React.FC<{ page: Page; label: string; total: number }> = ({ page, label, total }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const n = page.bullets.length;
  const bulletAt = page.bullets.map((_, i) =>
    page.at ? Math.max(16 + i * 4, Math.round(page.at[i] * fps) - LEAD) : 16 + i * 10);
  const exampleAt = page.exampleAt !== undefined
    ? Math.max(bulletAt[0] + 8, Math.round(page.exampleAt * fps) - LEAD)
    : 16 + n * 10 + 8;
  // the bullet being explained: the latest one revealed, unless the example
  // came after it (then the example is what's being said)
  const latest = bulletAt.reduce((a, t, i) => (frame >= t ? i : a), -1);
  const active = page.at && latest >= 0 && !(frame >= exampleAt && exampleAt > bulletAt[latest])
    ? latest : -1;
  if (page.visual) {
    return <VisualPage page={page} label={label} total={total} bulletAt={bulletAt} exampleAt={exampleAt} active={active} />;
  }
  return (
  <Scene>
    <div style={{ width: 1640, display: "flex", flexDirection: "column" }}>
      {/* header */}
      <RiseIn>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
          <div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 24, fontWeight: 700, letterSpacing: 3 }}>
            {label}
          </div>
          <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 24, fontWeight: 600 }}>
            {String(page.num).padStart(2, "0")} / {total}
          </div>
        </div>
      </RiseIn>
      <RiseIn delay={6}>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 64, fontWeight: 700, marginTop: 6 }}>
          {page.title}
        </div>
      </RiseIn>
      <div style={{ height: 2, background: theme.colors.panelBorder, margin: "24px 0 30px" }} />

      {/* key points: 2 or 3 in one row, 4 as 2x2, 5-6 in 3 columns */}
      <div style={{ display: "grid", gridTemplateColumns: `repeat(${n === 4 ? 2 : Math.min(n, 3)}, 1fr)`, gap: 18 }}>
        {page.bullets.map((b, i) => (
          <RiseIn key={i} delay={bulletAt[i]} style={{ display: "flex" }}>
            <div style={{ flex: 1, display: "flex", gap: 16, alignItems: "flex-start", background: theme.colors.panel, border: `1.5px solid ${i === active ? theme.colors.accent : theme.colors.panelBorder}`, boxShadow: i === active ? `0 0 18px ${theme.colors.accent}33` : "none", borderRadius: 14, padding: "20px 24px" }}>
              <div style={{ color: theme.colors.accent, fontSize: 26, lineHeight: 1.2 }}>{"▸"}</div>
              <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: n > 4 ? 25 : 28, lineHeight: 1.35 }}>{b}</div>
            </div>
          </RiseIn>
        ))}
      </div>

      {/* worked example callout */}
      <RiseIn delay={exampleAt}>
        <div style={{ marginTop: 26, background: `${theme.colors.accent2}14`, border: `1.5px solid ${theme.colors.accent2}`, borderRadius: 16, padding: "20px 26px", display: "flex", gap: 18, alignItems: "center" }}>
          <div style={{ color: theme.colors.accent2, fontFamily: theme.font.body, fontSize: 20, fontWeight: 700, letterSpacing: 2, minWidth: 110 }}>EXAMPLE</div>
          <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 26, lineHeight: 1.4 }}>{page.example}</div>
        </div>
      </RiseIn>
    </div>

    {/* guide reacting in the corner */}
    <div style={{ position: "absolute", right: 44, bottom: 20 }}>
      <Guide size={200} delay={24} fromX={160} expr="smile" />
    </div>
  </Scene>
  );
};

// ---------- A page with a picture ----------
// Big text on the left (readable on a phone), the page's visual on the right,
// both following the voice. Used when the page has `visual` in its data.
const VisualPage: React.FC<{
  page: Page; label: string; total: number;
  bulletAt: number[]; exampleAt: number; active: number;
}> = ({ page, label, total, bulletAt, exampleAt, active }) => {
  const n = page.bullets.length;
  const many = n > 4; // 5-6 boxes: two columns, slightly smaller text
  const frame = useCurrentFrame();
  const { polish } = usePolish();
  // polish.focus: what is being said stays bright, the rest dims
  const onExample = frame >= exampleAt && active < 0 && page.at !== undefined;
  const dimmed = (i: number) => polish.focus && frame >= bulletAt[i] && (onExample || (active >= 0 && i !== active));
  return (
    <Scene>
      <div style={{ width: 1720, height: 1080, boxSizing: "border-box", padding: "128px 0 140px", display: "flex", flexDirection: "column" }}>
        <RiseIn>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
            <div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 26, fontWeight: 700, letterSpacing: 3 }}>{label}</div>
            <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 26, fontWeight: 600 }}>
              {String(page.num).padStart(2, "0")} / {total}
            </div>
          </div>
        </RiseIn>
        <RiseIn delay={6}>
          <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 76, fontWeight: 700, lineHeight: 1.1, marginTop: 4 }}>{page.title}</div>
        </RiseIn>
        <div style={{ height: 2, background: theme.colors.panelBorder, margin: "22px 0 28px" }} />

        <div style={{ flex: 1, display: "flex", gap: 44, minHeight: 0 }}>
          {/* left: the boxes + example */}
          <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center", gap: 20 }}>
            <div style={{ display: "grid", gridTemplateColumns: many ? "1fr 1fr" : "1fr", gap: many ? 14 : 16 }}>
              {page.bullets.map((b, i) => (
                <RiseIn key={i} delay={bulletAt[i]} style={{ display: "flex" }}>
                  <div style={{ opacity: dimmed(i) ? 0.45 : 1, flex: 1, display: "flex", gap: 16, alignItems: "center", background: theme.colors.panel, border: `2px solid ${i === active ? theme.colors.accent : theme.colors.panelBorder}`, boxShadow: i === active ? `0 0 22px ${theme.colors.accent}44` : "none", borderRadius: 16, padding: many ? "16px 20px" : "18px 26px" }}>
                    <div style={{ color: theme.colors.accent, fontSize: many ? 28 : 34, lineHeight: 1 }}>{"▸"}</div>
                    <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: many ? 30 : 38, fontWeight: 500, lineHeight: 1.25 }}>{b}</div>
                  </div>
                </RiseIn>
              ))}
            </div>
            <RiseIn delay={exampleAt}>
              <div style={{ background: `${theme.colors.accent2}14`, border: `2px solid ${theme.colors.accent2}`, boxShadow: polish.focus && onExample ? `0 0 24px ${theme.colors.accent2}44` : "none", borderRadius: 16, padding: "16px 24px" }}>
                <div style={{ color: theme.colors.accent2, fontFamily: theme.font.body, fontSize: 20, fontWeight: 700, letterSpacing: 2, marginBottom: 6 }}>EXAMPLE</div>
                <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 30, lineHeight: 1.35 }}>
                  {polish.focus ? <CountText text={page.example} at={exampleAt} /> : page.example}
                </div>
              </div>
            </RiseIn>
          </div>

          {/* right: the picture */}
          <RiseIn delay={10} style={{ width: 720, display: "flex" }}>
            <PageVisual visual={page.visual!} bulletAt={bulletAt} exampleAt={exampleAt} />
          </RiseIn>
        </div>
      </div>

      {/* guide presenting the picture from its corner */}
      <div style={{ position: "absolute", right: 14, bottom: 6 }}>
        {polish.acting
          ? <ActingGuide size={170} delay={24} expr={frame >= exampleAt && frame < exampleAt + 30 ? "surprised" : "smile"} facing="left" hops={[...bulletAt, exampleAt]} />
          : <Guide size={170} delay={24} fromX={160} expr="smile" />}
      </div>
      {bulletAt.map((t, i) => <Sfx key={i} name="card" at={t} volume={0.3} />)}
      <Sfx name="card" at={exampleAt} volume={0.3} />
    </Scene>
  );
};

// ---------- Outro ----------
export const OutroScene: React.FC<{ text: LessonText }> = ({ text }) => {
  const { polish, words } = usePolish();
  if (polish.recap) return <RecapOutro recap={polish.recap} words={words.outro} outroLine={text.outroLine} />;
  return <PlainOutro text={text} />;
};

const PlainOutro: React.FC<{ text: LessonText }> = ({ text }) => (
  <Scene>
    <RiseIn>
      <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 74, fontWeight: 700, textAlign: "center", textShadow: `0 0 40px ${theme.colors.accent}55` }}>
        {text.outroLine}
      </div>
    </RiseIn>
    <RiseIn delay={14}>
      <div style={{ color: theme.colors.accentSoft, fontFamily: theme.font.body, fontSize: 34, marginTop: 24, textAlign: "center" }}>
        {text.outroSub}
      </div>
    </RiseIn>
    <div style={{ position: "absolute", right: 110, bottom: 40 }}>
      <Guide size={300} delay={16} fromX={200} />
    </div>
  </Scene>
);

// ---------- Timeline ----------
// VOICE-ONLY: the only audio is each block's narration clips. No music, no SFX.
export const PageLesson: React.FC<{
  data: LessonData;
  blocks: Block[];
  text: LessonText;
  captions: boolean;
  renderBlock?: (b: Block) => React.ReactNode | undefined;
  polish?: Polish;
}> = ({ data, blocks, text, captions, renderBlock, polish = {} }) => {
  const total = blocks.length ? blocks[blocks.length - 1].start + blocks[blocks.length - 1].dur : 0;
  const defaultNode = (b: Block) => {
    if (b.kind === "intro") return <IntroScene text={text} />;
    if (b.kind === "outro") return <OutroScene text={text} />;
    if (b.kind === "quiz") return <QuizScene data={b.quiz!} />;
    return <PageScene page={b.page!} label={text.label} total={data.pages.length} />;
  };
  return (
    <PolishProvider value={{ polish, words: data.words }}>
    <AbsoluteFill style={{ background: theme.colors.bg }}>
      <Background />
      {polish.sound && (
        // quiet bed under the voice, faded in and out (trial only, see polish.tsx)
        <Audio src={staticFile("audio/music.mp3")} loop
          volume={(f) => 0.07 * interpolate(f, [0, 60, total - 90, total], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })} />
      )}
      {blocks.map((b) => (
        <Sequence key={b.key} from={b.start} durationInFrames={b.dur}>
          {renderBlock?.(b) ?? defaultNode(b)}
          {b.clips.map((c) => (
            <Sequence key={c.key} from={c.from}>
              <Audio src={staticFile(`audio/${data.id}/${c.key}.mp3`)} />
              {captions && b.captions && data.words[c.key] && <Captions words={data.words[c.key]} />}
            </Sequence>
          ))}
        </Sequence>
      ))}
      <BrandMark />
    </AbsoluteFill>
    </PolishProvider>
  );
};
