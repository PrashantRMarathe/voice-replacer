import React from "react";
import { AbsoluteFill, Audio, Sequence, staticFile, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { Background } from "../components/Background";
import { RiseIn, GlowCard } from "../components/ui";
import { WASTE_ICONS } from "../components/icons";
import { Scene } from "../scenes/Scene";
import { Captions, Word } from "../components/Captions";
import { Guide, Worker } from "../components/characters";
import { theme } from "../theme";
import "../fonts";

import w01 from "../captions/01_title.words.json";
import w02 from "../captions/02_acronym.words.json";
import w03 from "../captions/03_flow.words.json";
import w04 from "../captions/04_grid.words.json";
import w05 from "../captions/05_outro.words.json";

const sfx = (f: string) => staticFile(`audio/sfx/${f}.mp3`);

const WASTES = [
  { l: "D", name: "Defects", desc: "Errors that need rework or scrap." },
  { l: "O", name: "Overproduction", desc: "Making more than is needed, too early." },
  { l: "W", name: "Waiting", desc: "Idle time between steps." },
  { l: "N", name: "Non-utilized talent", desc: "Not using people's skills." },
  { l: "T", name: "Transportation", desc: "Needless movement of materials." },
  { l: "I", name: "Inventory", desc: "Excess stock tying up cash." },
  { l: "M", name: "Motion", desc: "Needless movement of people." },
  { l: "E", name: "Extra processing", desc: "More work than the customer needs." },
];

// ---- Scene 1: Title ----
const TitleScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const line = spring({ frame, fps, config: { damping: 20 } });
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 30, letterSpacing: 8, textAlign: "center" }}>
          {theme.brand.courseName.toUpperCase()}
        </div>
      </RiseIn>
      <RiseIn delay={10}>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 104, fontWeight: 700, textAlign: "center", marginTop: 10, textShadow: `0 0 40px ${theme.colors.accent}55` }}>
          The 8 Wastes of Lean
        </div>
      </RiseIn>
      <div style={{ height: 6, width: interpolate(line, [0, 1], [0, 460]), background: theme.colors.accent, borderRadius: 4, marginTop: 30, boxShadow: `0 0 24px ${theme.colors.accent}` }} />
      <RiseIn delay={26}>
        <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 32, marginTop: 28 }}>
          Remember them with one word: <b style={{ color: theme.colors.accentSoft }}>DOWNTIME</b>
        </div>
      </RiseIn>
      {/* the guide introduces the lesson */}
      <div style={{ position: "absolute", left: 90, bottom: 40 }}>
        <Guide size={320} delay={20} fromX={-180} />
      </div>
    </Scene>
  );
};

// ---- Scene 2: DOWNTIME acronym ----
const AcronymScene: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <Scene>
      <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 34, marginBottom: 46 }}>
        Every waste hides inside this one word:
      </div>
      <div style={{ display: "flex", gap: 18 }}>
        {"DOWNTIME".split("").map((ch, i) => {
          const glow = 0.5 + 0.5 * Math.sin(frame / 12 - i);
          return (
            <RiseIn key={i} delay={i * 7}>
              <div
                style={{
                  width: 124, height: 156,
                  background: theme.colors.panel,
                  border: `2px solid ${theme.colors.accent}`,
                  borderRadius: 16,
                  color: theme.colors.accentSoft,
                  fontFamily: theme.font.heading, fontSize: 90, fontWeight: 700,
                  display: "flex", alignItems: "center", justifyContent: "center",
                  boxShadow: `0 0 ${20 + 16 * glow}px ${theme.colors.accent}55`,
                }}
              >
                {ch}
              </div>
            </RiseIn>
          );
        })}
      </div>
    </Scene>
  );
};

// ---- Scene 3: Animated process flow (shows waste happening on a line) ----
const FlowScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const steps = ["Cut", "Weld", "Paint", "Pack"];
  const partX = interpolate(frame, [20, 340], [260, 1500], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const tagPop = (d: number) => spring({ frame: frame - d, fps, config: { damping: 14 } });
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 52, fontWeight: 600, marginBottom: 70 }}>
          Waste hides inside everyday work
        </div>
      </RiseIn>
      <div style={{ position: "relative", width: 1500, height: 320 }}>
        {/* the conveyor line */}
        <div style={{ position: "absolute", top: 150, left: 120, width: 1300, height: 4, background: theme.colors.panelBorder }} />
        {steps.map((s, i) => {
          const cx = 220 + i * 360;
          return (
            <RiseIn key={s} delay={i * 8}>
              <div style={{ position: "absolute", left: cx - 80, top: 90, width: 160, height: 120, background: theme.colors.panel, border: `2px solid ${theme.colors.accent2}`, borderRadius: 14, display: "flex", alignItems: "center", justifyContent: "center", color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 30, boxShadow: `0 0 20px ${theme.colors.accent2}33` }}>
                {s}
              </div>
            </RiseIn>
          );
        })}
        {/* moving part */}
        <div style={{ position: "absolute", left: partX, top: 134, width: 36, height: 36, borderRadius: 8, background: theme.colors.accentSoft, boxShadow: `0 0 22px ${theme.colors.accentSoft}` }} />
        {/* waste tags pop up */}
        <div style={{ position: "absolute", left: 540, top: 10, transform: `scale(${tagPop(120)})`, opacity: tagPop(120), color: theme.colors.danger, fontFamily: theme.font.body, fontWeight: 700, fontSize: 28 }}>
          ⏳ Waiting
        </div>
        <div style={{ position: "absolute", left: 980, top: 250, transform: `scale(${tagPop(240)})`, opacity: tagPop(240), color: theme.colors.danger, fontFamily: theme.font.body, fontWeight: 700, fontSize: 28 }}>
          📦 Inventory piling up
        </div>
      </div>
      {/* a worker stands idle beside the line, acting out the waste */}
      <div style={{ position: "absolute", left: 140, bottom: 20 }}>
        <Worker size={260} delay={60} fromX={-160} pose="crossed" expr="tired" />
      </div>
    </Scene>
  );
};

// ---- Scene 4: The 8 waste cards reveal ----
const WastesGridScene: React.FC = () => {
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 56, fontWeight: 600, marginBottom: 36 }}>
          The 8 Wastes
        </div>
      </RiseIn>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 22, maxWidth: 1640 }}>
        {WASTES.map((w, i) => (
          <GlowCard key={w.l} index={w.l} title={w.name} desc={w.desc} Icon={WASTE_ICONS[i]} delay={i * 9} />
        ))}
      </div>
    </Scene>
  );
};

// ---- Scene 5: Outro ----
const OutroScene: React.FC = () => {
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 76, fontWeight: 700, textAlign: "center", textShadow: `0 0 40px ${theme.colors.accent}55` }}>
          Spot the waste. Remove the waste.
        </div>
      </RiseIn>
      <RiseIn delay={14}>
        <div style={{ color: theme.colors.accentSoft, fontFamily: theme.font.body, fontSize: 36, marginTop: 26, textAlign: "center" }}>
          Next lesson: The 5S System →
        </div>
      </RiseIn>
      {/* the guide waves goodbye */}
      <div style={{ position: "absolute", right: 110, bottom: 40 }}>
        <Guide size={300} delay={18} fromX={200} expr="smile" />
      </div>
    </Scene>
  );
};

// Narration audio per scene (durations measured from the generated files).
const narr = (f: string) => staticFile(`audio/${f}`);

// `captions`: burn karaoke captions (off for a dub-ready master so the dub tool
// can add its own, timing-correct subtitles).
export const EightWastes: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  const Cap = (words: Word[]) => (captions ? <Captions words={words} /> : null);
  return (
    <AbsoluteFill style={{ background: theme.colors.bg }}>
      <Background />

      {/* soft background music under the whole lesson */}
      <Audio src={narr("music.mp3")} volume={0.16} />

      <Sequence durationInFrames={500}>
        <TitleScene />
        <Audio src={narr("01_title.mp3")} />
        <Audio src={sfx("whoosh")} volume={0.5} />
        {Cap(w01 as Word[])}
      </Sequence>
      <Sequence from={500} durationInFrames={300}>
        <AcronymScene />
        <Audio src={narr("02_acronym.mp3")} />
        <Audio src={sfx("whoosh")} volume={0.5} />
        <Audio src={sfx("ding")} volume={0.35} />
        {Cap(w02 as Word[])}
      </Sequence>
      <Sequence from={800} durationInFrames={485}>
        <FlowScene />
        <Audio src={narr("03_flow.mp3")} />
        <Audio src={sfx("whoosh")} volume={0.5} />
        {Cap(w03 as Word[])}
      </Sequence>
      <Sequence from={1285} durationInFrames={550}>
        <WastesGridScene />
        <Audio src={narr("04_grid.mp3")} />
        <Audio src={sfx("whoosh")} volume={0.5} />
        {Cap(w04 as Word[])}
      </Sequence>
      <Sequence from={1835} durationInFrames={350}>
        <OutroScene />
        <Audio src={narr("05_outro.mp3")} />
        <Audio src={sfx("whoosh")} volume={0.5} />
        {Cap(w05 as Word[])}
      </Sequence>
    </AbsoluteFill>
  );
};

export const EIGHT_WASTES_DURATION = 2185; // frames (~73s @ 30fps)
