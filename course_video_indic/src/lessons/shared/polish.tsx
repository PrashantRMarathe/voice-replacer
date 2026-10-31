import React from "react";
import { UI } from "../../ui";
import { Audio, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Character, Expr } from "../../components/characters";
import { VisualIcon } from "../../components/visualIcons";
import { RiseIn } from "../../components/ui";
import { Scene } from "../../scenes/Scene";
import { theme } from "../../theme";
import type { Word } from "../plan";

// "Polish" layer for page lessons (approved from the Oct 2026 Poka Yoke demo).
// A lesson opts in by passing `polish`; without it the lesson renders as before.
// `sound` is for the normal version only: `...Dub` stays voice-only (CLAUDE.md rule 4).

export type Polish = {
  sound?: boolean;    // quiet music bed + soft card / quiz sounds
  acting?: boolean;   // the guide reacts: points at the content, hops, changes face
  focus?: boolean;    // the card being spoken stays bright, the others dim
  bigQuiz?: boolean;  // countdown ring on quick checks
  hook?: {            // the intro's opening problem, shown before the title
    value: number; label: string; sub?: string; icon?: string;
    until: string;    // phrase in the intro where the title takes over
  };
  recap?: {           // the outro: the opening problem fixed, takeaways, next letter
    problem: string; before: number; after: number; unit: string;
    fixedLabel?: string; // replaces "Problem fixed" (e.g. when the number is a result, not a fix)
    takeaways: { text: string; cue: string }[];
    action: { text: string; cue: string };
    next: { letter: string; title: string; cue: string; kicker?: string }; // kicker replaces "NEXT LESSON"
  };
};

const PolishCtx = React.createContext<{ polish: Polish; words: Record<string, Word[]> }>({ polish: {}, words: {} });
export const PolishProvider = PolishCtx.Provider;
export const usePolish = () => React.useContext(PolishCtx);

// seconds into a clip where `phrase` starts (first match), or undefined
const norm = (s: string) => s.toLowerCase().replace(/[^\p{L}\p{N}\p{M}']/gu, "");
export const cueTime = (words: Word[] | undefined, phrase: string): number | undefined => {
  if (!words) return undefined;
  const p = phrase.split(/\s+/).map(norm).filter(Boolean);
  for (let i = 0; i + p.length <= words.length; i++) {
    if (p.every((w, j) => norm(words[i + j].w) === w)) return words[i].s;
  }
  return undefined;
};

// ---------- sound ----------
export const Sfx: React.FC<{ name: string; at: number; volume?: number }> = ({ name, at, volume = 0.5 }) => {
  const { polish } = usePolish();
  if (!polish.sound || at < 0) return null;
  return (
    <Sequence from={Math.round(at)} durationInFrames={45} layout="none">
      <Audio src={staticFile(`audio/sfx/${name}.mp3`)} volume={volume} />
    </Sequence>
  );
};

// ---------- numbers that count up inside a sentence ----------
const NUM = /\d[\d,]*(?:\.\d+)?/g;
export const CountText: React.FC<{ text: string; at: number; dur?: number }> = ({ text, at, dur = 36 }) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame - at, [0, dur], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const ease = 1 - Math.pow(1 - p, 3);
  const parts: React.ReactNode[] = [];
  let last = 0;
  for (const m of text.matchAll(NUM)) {
    const raw = m[0];
    const i = m.index ?? 0;
    // leave clock times ("10:00") alone: counting them reads as "10:0"
    if (text[i - 1] === ":" || text[i + raw.length] === ":") continue;
    const dec = raw.includes(".") ? raw.split(".")[1].length : 0;
    const val = parseFloat(raw.replace(/,/g, ""));
    const shown = (val * ease).toLocaleString("en-US", {
      minimumFractionDigits: dec, maximumFractionDigits: dec, useGrouping: raw.includes(","),
      // keep a written leading zero ("05"); other numbers count up unpadded
      minimumIntegerDigits: /^0\d/.test(raw) ? raw.split(".")[0].length : 1,
    });
    parts.push(text.slice(last, m.index), <span key={m.index} style={{ color: theme.colors.accentSoft, fontWeight: 700 }}>{shown}</span>);
    last = (m.index ?? 0) + raw.length;
  }
  parts.push(text.slice(last));
  return <>{parts}</>;
};

// ---------- the guide, acting ----------
// Faces the content (mirrored when standing on the right), hops a little each
// time something new appears, and takes the face of the moment.
export const ActingGuide: React.FC<{
  size?: number; expr?: Expr; facing?: "left" | "right"; hops?: number[]; fromX?: number; delay?: number;
}> = ({ size = 200, expr = "smile", facing = "right", hops = [], fromX = 160, delay = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const enter = spring({ frame: frame - delay, fps, config: { damping: 18 } });
  const hop = hops.reduce((h, t) => {
    const d = frame - t;
    return d >= 0 && d < 14 ? Math.min(h, -Math.sin((d / 14) * Math.PI) * 16) : h;
  }, 0);
  const bob = Math.sin(frame / 18) * 4;
  return (
    <div style={{ opacity: enter, transform: `translate(${interpolate(enter, [0, 1], [fromX, 0])}px, ${bob + hop}px) scaleX(${facing === "left" ? -1 : 1})` }}>
      <Character size={size} gender="f" outfit={theme.colors.accent} hairColor="#3a2416" expr={expr} pose="pointing" top="blazer" />
    </div>
  );
};

// ---------- intro: the opening problem, then the title ----------
export const IntroHook: React.FC<{ hook: NonNullable<Polish["hook"]>; until: number; children: React.ReactNode }> = ({ hook, until, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const swap = Math.round(until * fps);
  const out = interpolate(frame, [swap - 10, swap + 4], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const n = spring({ frame: frame - 30, fps, config: { damping: 30 }, durationInFrames: 40 });
  return (
    <>
      {frame < swap + 6 && (
        <Scene>
          <div style={{ opacity: out, display: "flex", flexDirection: "column", alignItems: "center", gap: 18 }}>
            <RiseIn><VisualIcon name={hook.icon} color={theme.colors.danger} size={150} /></RiseIn>
            <div style={{ color: theme.colors.danger, fontFamily: theme.font.heading, fontSize: 210, fontWeight: 700, lineHeight: 1, textShadow: `0 0 50px ${theme.colors.danger}55` }}>
              {Math.round(hook.value * n).toLocaleString("en-US")}
            </div>
            <RiseIn delay={20}><div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 54, fontWeight: 600 }}>{hook.label}</div></RiseIn>
            {hook.sub && <RiseIn delay={150}><div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 36 }}>{hook.sub}</div></RiseIn>}
          </div>
          <div style={{ position: "absolute", left: 90, bottom: 40 }}>
            <ActingGuide size={300} expr="concerned" facing="right" fromX={-180} delay={10} />
          </div>
        </Scene>
      )}
      {frame >= swap - 4 && <Sequence from={swap - 4} layout="none">{children}</Sequence>}
    </>
  );
};

// ---------- outro: problem fixed -> takeaways -> action -> next letter ----------
export const RecapOutro: React.FC<{ recap: NonNullable<Polish["recap"]>; words?: Word[]; outroLine: string }> = ({ recap, words, outroLine }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const f = (phrase: string, fallback: number) => Math.round((cueTime(words, phrase) ?? fallback) * fps);
  const tk = recap.takeaways.map((t, i) => f(t.cue, 3 + i * 4));
  const actionAt = f(recap.action.cue, 20);
  const nextAt = f(recap.next.cue, 32);
  const phase = frame < actionAt - 6 ? 0 : frame < nextAt - 30 ? 1 : 2;
  const fixed = spring({ frame: frame - 10, fps, config: { damping: 30 }, durationInFrames: 45 });
  const shown = Math.round(interpolate(fixed, [0, 1], [recap.before, recap.after]));
  const active = tk.reduce((a, t, i) => (frame >= t ? i : a), -1);

  return (
    <Scene>
      {phase === 0 && (
        <div style={{ width: 1600, display: "flex", gap: 60, alignItems: "center" }}>
          <RiseIn style={{ width: 620 }}>
            <div style={{ background: theme.colors.panel, border: `2px solid ${theme.colors.good}`, borderRadius: 24, padding: "36px 34px", display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center", gap: 10 }}>
              <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 26, fontWeight: 700, letterSpacing: 0 }}>{UI.rememberStart}</div>
              <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 34, fontWeight: 600 }}>{recap.problem}</div>
              <div style={{ color: shown <= recap.after ? theme.colors.good : theme.colors.danger, fontFamily: theme.font.heading, fontSize: 170, fontWeight: 700, lineHeight: 1.05 }}>{shown.toLocaleString("en-US")}</div>
              <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 28 }}>{recap.unit}</div>
              <RiseIn delay={60}>
                <div style={{ marginTop: 10, display: "flex", alignItems: "center", gap: 12, color: theme.colors.good, fontFamily: theme.font.heading, fontSize: 34, fontWeight: 700 }}>
                  <VisualIcon name="check" color={theme.colors.good} size={44} /> {recap.fixedLabel ?? UI.problemFixed}
                </div>
              </RiseIn>
            </div>
          </RiseIn>
          <div style={{ flex: 1, display: "flex", flexDirection: "column", gap: 20 }}>
            <RiseIn delay={4}><div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 28, fontWeight: 700, letterSpacing: 0 }}>{UI.threeThings}</div></RiseIn>
            {recap.takeaways.map((t, i) => (
              <RiseIn key={i} delay={tk[i] - 4}>
                <div style={{ display: "flex", gap: 20, alignItems: "center", background: theme.colors.panel, border: `2px solid ${i === active ? theme.colors.accent : theme.colors.panelBorder}`, opacity: active >= 0 && i !== active ? 0.55 : 1, borderRadius: 16, padding: "22px 26px" }}>
                  <div style={{ width: 54, height: 54, borderRadius: 54, background: theme.colors.accent, color: theme.colors.bg, fontFamily: theme.font.heading, fontSize: 28, fontWeight: 700, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>{i + 1}</div>
                  <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 38, fontWeight: 500 }}>{t.text}</div>
                </div>
              </RiseIn>
            ))}
            {tk.map((t, i) => <Sfx key={i} name="card" at={t - 4} volume={0.35} />)}
          </div>
        </div>
      )}
      {phase === 1 && (
        <Sequence from={actionAt - 6} layout="none">
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 26, width: 1300, textAlign: "center" }}>
            <RiseIn><div style={{ color: theme.colors.accent2, fontFamily: theme.font.body, fontSize: 30, fontWeight: 700, letterSpacing: 0 }}>{UI.actionThisWeek}</div></RiseIn>
            <RiseIn delay={8}>
              <div style={{ background: `${theme.colors.accent2}14`, border: `2px solid ${theme.colors.accent2}`, borderRadius: 24, padding: "40px 50px", color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 58, fontWeight: 600, lineHeight: 1.25 }}>
                {recap.action.text}
              </div>
            </RiseIn>
          </div>
        </Sequence>
      )}
      {phase === 2 && (
        <Sequence from={nextAt - 30} layout="none">
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24 }}>
            <RiseIn><div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 64, fontWeight: 700, textShadow: `0 0 40px ${theme.colors.accent}55` }}>{outroLine}</div></RiseIn>
            <RiseIn delay={30}>
              <div style={{ display: "flex", alignItems: "center", gap: 34, marginTop: 30, background: theme.colors.panel, border: `2px solid ${theme.colors.accent}`, borderRadius: 28, padding: "26px 44px 26px 26px", boxShadow: `0 0 40px ${theme.colors.accent}33` }}>
                <div style={{ width: 150, height: 150, borderRadius: 24, background: theme.colors.accent, color: theme.colors.bg, fontFamily: theme.font.heading, fontSize: 110, fontWeight: 700, display: "flex", alignItems: "center", justifyContent: "center" }}>{recap.next.letter}</div>
                <div>
                  <div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 26, fontWeight: 700, letterSpacing: 0 }}>{recap.next.kicker ?? UI.nextLesson}</div>
                  <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 56, fontWeight: 700 }}>{recap.next.title}</div>
                </div>
              </div>
            </RiseIn>
            <Sfx name="sting" at={30} volume={0.4} />
          </div>
        </Sequence>
      )}
      <div style={{ position: "absolute", right: 60, bottom: 30 }}>
        <ActingGuide size={260} expr={phase === 0 && frame < 40 ? "surprised" : "smile"} facing="left" hops={[...tk, actionAt, nextAt]} delay={16} fromX={200} />
      </div>
    </Scene>
  );
};

// ---------- quiz: countdown ring ----------
export const CountdownRing: React.FC<{ start: number; end: number }> = ({ start, end }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  if (frame < start || frame >= end) return null;
  const left = (end - frame) / fps;
  const p = (frame - start) / (end - start);
  const R = 54;
  const C = 2 * Math.PI * R;
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 22 }}>
      <svg width={140} height={140} viewBox="0 0 140 140">
        <circle cx={70} cy={70} r={R} stroke={theme.colors.panelBorder} strokeWidth={10} fill="none" />
        <circle cx={70} cy={70} r={R} stroke={theme.colors.accent} strokeWidth={10} fill="none" strokeLinecap="round"
          strokeDasharray={C} strokeDashoffset={C * p} transform="rotate(-90 70 70)" />
        <text x={70} y={86} textAnchor="middle" fill={theme.colors.text} fontFamily="Poppins" fontWeight={700} fontSize={48}>{Math.ceil(left)}</text>
      </svg>
      <div style={{ color: theme.colors.accentSoft, fontFamily: theme.font.heading, fontSize: 40, fontWeight: 600 }}>Think{"…"}</div>
    </div>
  );
};
