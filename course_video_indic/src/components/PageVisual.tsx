import React from "react";
import { UI } from "../ui";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { RiseIn } from "./ui";
import { VisualIcon } from "./visualIcons";
import { CountText } from "../lessons/shared/polish";
import { theme } from "../theme";
import type { Visual, VisualItem } from "../lessons/plan";

// The picture beside a page's boxes. A page's `visual` (from narration/<lesson>.py)
// picks one of a few layouts; each item appears with the box it belongs to
// (`with` = box index, or "example"), so the picture follows the voice too.

type Cue = { bulletAt: number[]; exampleAt: number };

const toneColor = (tone?: VisualItem["tone"]) =>
  tone === "bad" ? theme.colors.danger : tone === "good" ? theme.colors.good : theme.colors.accent;

// frame an item appears: its `with` cue, else matched 1:1 to the boxes, else a stagger
const revealAt = (cue: Cue, n: number) => (it: { with?: number | "example" }, i: number) => {
  if (it.with === "example") return cue.exampleAt;
  if (typeof it.with === "number") return cue.bulletAt[it.with] ?? cue.bulletAt[cue.bulletAt.length - 1];
  if (n === cue.bulletAt.length) return cue.bulletAt[i];
  return 20 + i * 12;
};

// items sharing one cue appear one after another instead of all at once
const reveals = (items: VisualItem[], cue: Cue) => {
  const at = items.map(revealAt(cue, items.length));
  for (let i = 1; i < at.length; i++) if (at[i] <= at[i - 1]) at[i] = at[i - 1] + 15;
  return at;
};

// the item being talked about: the latest one that has appeared
const latestOf = (at: number[], frame: number) => at.reduce((a, t, i) => (frame >= t && t >= (at[a] ?? -1) ? i : a), -1);

const Label: React.FC<{ text: string; size?: number; color?: string; weight?: number }> = ({ text, size = 30, color = theme.colors.text, weight = 600 }) => (
  <div style={{ color, fontFamily: theme.font.heading, fontSize: size, fontWeight: weight, lineHeight: 1.2 }}>{text}</div>
);
const Sub: React.FC<{ text?: string }> = ({ text }) =>
  text ? <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 25, lineHeight: 1.3, marginTop: 4 }}>{text}</div> : null;

const useDraw = (at: number, len = 20) => {
  const frame = useCurrentFrame();
  return interpolate(frame - at, [0, len], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
};

const Badge: React.FC<{ good: boolean; size?: number }> = ({ good, size = 44 }) => (
  <div style={{ width: size, height: size, borderRadius: size, background: good ? theme.colors.good : theme.colors.danger, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
    <VisualIcon name={good ? "check" : "cross"} color={theme.colors.bg} size={size * 0.7} />
  </div>
);

// ---------- layouts ----------

// Vertical chain of boxes with arrows; optional STOP bar after one of them.
const Flow: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const frame = useCurrentFrame();
  const items = v.items ?? [];
  const at = reveals(items, cue);
  const active = latestOf(at, frame);
  const stopAt = v.stop ? revealAt(cue, -1)({ with: v.stop.with }, 0) : 0;
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", width: "100%" }}>
      {items.map((it, i) => {
        const c = toneColor(it.tone);
        return (
          <React.Fragment key={i}>
            {i > 0 && (
              <RiseIn delay={at[i] - 4}>
                {v.stop && v.stop.after === i - 1 ? (
                  <div style={{ opacity: frame >= stopAt ? 1 : 0.25, margin: "10px 0", display: "flex", alignItems: "center", gap: 14, color: theme.colors.danger, fontFamily: theme.font.body, fontWeight: 800, fontSize: 28, letterSpacing: 0 }}>
                    <div style={{ width: 120, height: 4, background: theme.colors.danger, borderRadius: 2 }} />
                    {v.stop.label}
                    <div style={{ width: 120, height: 4, background: theme.colors.danger, borderRadius: 2 }} />
                  </div>
                ) : (
                  <div style={{ color: theme.colors.textDim, fontSize: 40, lineHeight: 1, margin: "6px 0" }}>{"↓"}</div>
                )}
              </RiseIn>
            )}
            <RiseIn delay={at[i]} style={{ width: "100%" }}>
              <div style={{ display: "flex", alignItems: "center", gap: 20, background: theme.colors.panel, border: `2px solid ${i === active ? c : theme.colors.panelBorder}`, boxShadow: i === active ? `0 0 22px ${c}44` : "none", borderRadius: 16, padding: "18px 26px" }}>
                <VisualIcon name={it.icon} color={c} size={64} />
                <div><Label text={it.label} size={36} /><Sub text={it.sub} /></div>
              </div>
            </RiseIn>
          </React.Fragment>
        );
      })}
    </div>
  );
};

// Strongest at the top, each level narrower and shifting from good to danger.
const Ladder: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const frame = useCurrentFrame();
  const items = v.items ?? [];
  const at = reveals(items, cue);
  const active = latestOf(at, frame);
  const tones = [theme.colors.good, theme.colors.good, theme.colors.accent, theme.colors.accent2, theme.colors.danger, theme.colors.danger];
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 12, width: "100%" }}>
      <div style={{ color: theme.colors.good, fontFamily: theme.font.body, fontSize: 20, fontWeight: 700, letterSpacing: 0 }}>{v.top ?? UI.strongest}</div>
      {items.map((it, i) => {
        const c = it.tone ? toneColor(it.tone) : tones[Math.round((i / Math.max(1, items.length - 1)) * 4)];
        return (
          <RiseIn key={i} delay={at[i]} style={{ width: `${96 - i * (40 / Math.max(1, items.length - 1))}%` }}>
            <div style={{ display: "flex", alignItems: "center", gap: 16, background: `${c}${i === active ? "33" : "1a"}`, border: `2px solid ${i === active ? c : `${c}66`}`, borderRadius: 14, padding: "15px 22px" }}>
              <div style={{ color: c, fontFamily: theme.font.heading, fontSize: 30, fontWeight: 700, width: 30 }}>{i + 1}</div>
              <VisualIcon name={it.icon} color={c} size={48} />
              <Label text={it.label} size={34} />
            </div>
          </RiseIn>
        );
      })}
      <div style={{ color: theme.colors.danger, fontFamily: theme.font.body, fontSize: 20, fontWeight: 700, letterSpacing: 0 }}>{v.bottom ?? UI.weakest}</div>
    </div>
  );
};

// Big icons with a short label: 2-3 in a row, 4 as 2x2, 5-6 as 3 columns.
const Icons: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const frame = useCurrentFrame();
  const items = v.items ?? [];
  const at = reveals(items, cue);
  const active = latestOf(at, frame);
  const cols = items.length === 4 ? 2 : Math.min(3, items.length);
  const iconSize = items.length > 4 ? 90 : 130;
  return (
    <div style={{ display: "grid", gridTemplateColumns: `repeat(${cols}, 1fr)`, gap: 22, width: "100%" }}>
      {items.map((it, i) => {
        const c = toneColor(it.tone);
        const p = useDraw(at[i]);
        return (
          <RiseIn key={i} delay={at[i]} style={{ display: "flex" }}>
            <div style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center", gap: 12, background: theme.colors.panel, border: `2px solid ${i === active ? c : theme.colors.panelBorder}`, boxShadow: i === active ? `0 0 22px ${c}44` : "none", borderRadius: 18, padding: "34px 14px" }}>
              <VisualIcon name={it.icon} color={c} size={iconSize} progress={p} />
              <Label text={it.label} size={items.length > 4 ? 28 : 34} />
              <Sub text={it.sub} />
            </div>
          </RiseIn>
        );
      })}
    </div>
  );
};

// Numbered steps in a 2-column grid (e.g. an 8-step method).
const Steps: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const frame = useCurrentFrame();
  const items = v.items ?? [];
  const at = reveals(items, cue);
  const active = latestOf(at, frame);
  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gridAutoFlow: "column", gridTemplateRows: `repeat(${Math.ceil(items.length / 2)}, auto)`, gap: 14, width: "100%" }}>
      {items.map((it, i) => (
        <RiseIn key={i} delay={at[i]}>
          <div style={{ display: "flex", alignItems: "center", gap: 16, background: theme.colors.panel, border: `2px solid ${frame >= at[i] && active >= 0 && at[i] === at[active] ? theme.colors.accent : theme.colors.panelBorder}`, borderRadius: 14, padding: "20px 18px" }}>
            <div style={{ width: 50, height: 50, borderRadius: 50, background: theme.colors.accent, color: theme.colors.bg, fontFamily: theme.font.heading, fontWeight: 700, fontSize: 24, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>{it.sub ?? i + 1}</div>
            <Label text={it.label} size={31} />
          </div>
        </RiseIn>
      ))}
    </div>
  );
};

// Weak way vs strong way, side by side (first item = the weak one).
const Versus: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const items = (v.items ?? []).slice(0, 2);
  const at = reveals(items, cue);
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 18, width: "100%" }}>
      {items.map((it, i) => {
        const good = i === 1;
        const c = good ? theme.colors.good : theme.colors.danger;
        const p = useDraw(at[i]);
        return (
          <React.Fragment key={i}>
            {i === 1 && <RiseIn delay={at[1] - 6}><div style={{ color: theme.colors.textDim, fontSize: 48 }}>{"→"}</div></RiseIn>}
            <RiseIn delay={at[i]} style={{ flex: 1 }}>
              <div style={{ position: "relative", display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center", gap: 16, background: `${c}12`, border: `2px solid ${c}`, borderRadius: 20, padding: "36px 18px 30px" }}>
                <div style={{ position: "absolute", top: -22, right: -14 }}><Badge good={good} /></div>
                <VisualIcon name={it.icon} color={c} size={160} progress={p} />
                <Label text={it.label} size={36} />
                <Sub text={it.sub} />
              </div>
            </RiseIn>
          </React.Fragment>
        );
      })}
    </div>
  );
};

const fmt = (n: number, decimals = 0) =>
  n.toLocaleString("en-IN", { minimumFractionDigits: decimals, maximumFractionDigits: decimals });

const useCount = (to: number, at: number) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return to * spring({ frame: frame - at, fps, config: { damping: 30 }, durationInFrames: 40 });
};

// Before vs after as two bars with counting numbers.
const Compare: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const at = revealAt(cue, -1)({ with: v.with ?? "example" }, 0);
  const sides = [v.before!, v.after!];
  const max = Math.max(...sides.map((s) => s.value));
  const H = 330;
  const grow = [useCount(1, at), useCount(1, at + 20)];
  return (
    <RiseIn delay={at - 6} style={{ width: "100%" }}>
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 18 }}>
        <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "center", gap: 70, height: H + 70 }}>
          {sides.map((s, i) => {
            const c = i === 0 ? theme.colors.danger : theme.colors.good;
            return (
              <div key={i} style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 10 }}>
                <div style={{ color: c, fontFamily: theme.font.heading, fontSize: 52, fontWeight: 700 }}>
                  {v.prefix ?? ""}{fmt(s.value * grow[i], v.decimals)}{v.suffix ?? ""}
                </div>
                <div style={{ width: 150, height: Math.max(6, (H * s.value / max) * grow[i]), background: `linear-gradient(${c}, ${c}88)`, borderRadius: "12px 12px 4px 4px", boxShadow: `0 0 24px ${c}44` }} />
              </div>
            );
          })}
        </div>
        <div style={{ display: "flex", gap: 70 }}>
          {sides.map((s, i) => <div key={i} style={{ width: 150, textAlign: "center" }}><Label text={s.label} size={26} color={theme.colors.textDim} weight={500} /></div>)}
        </div>
        {v.unit && <Sub text={v.unit} />}
        {v.note && (
          <RiseIn delay={at + 36}>
            <div style={{ marginTop: 6, background: `${theme.colors.good}22`, border: `2px solid ${theme.colors.good}`, borderRadius: 40, padding: "10px 28px", color: theme.colors.good, fontFamily: theme.font.heading, fontSize: 30, fontWeight: 700 }}><CountText text={v.note} at={at + 36} /></div>
          </RiseIn>
        )}
      </div>
    </RiseIn>
  );
};

// One big counting number.
const Stat: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const at = revealAt(cue, -1)({ with: v.with ?? "example" }, 0);
  const n = useCount(v.value ?? 0, at);
  const p = useDraw(at);
  return (
    <RiseIn delay={at - 6}>
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center", gap: 18 }}>
        {v.icon && <VisualIcon name={v.icon} color={theme.colors.accent} size={130} progress={p} />}
        <div style={{ color: theme.colors.accent, fontFamily: theme.font.heading, fontSize: 130, fontWeight: 700, lineHeight: 1, textShadow: `0 0 40px ${theme.colors.accent}55` }}>
          {v.prefix ?? ""}{fmt(n, v.decimals)}{v.suffix ?? ""}
        </div>
        {v.label && <Label text={v.label} size={32} />}
        <Sub text={v.unit} />
      </div>
    </RiseIn>
  );
};

// A horizontal time bar split into phases (`span` = relative length).
const Timeline: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const frame = useCurrentFrame();
  const items = v.items ?? [];
  const at = reveals(items, cue);
  const active = latestOf(at, frame);
  const colors = [theme.colors.accent2, theme.colors.accent, theme.colors.good, theme.colors.accentSoft];
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 24, width: "100%" }}>
      <div style={{ display: "flex", gap: 6, height: 90, marginBottom: 10 }}>
        {items.map((it, i) => {
          const fill = useDraw(at[i], 18);
          const c = colors[i % colors.length];
          return (
            <div key={i} style={{ flex: it.span ?? 1, background: theme.colors.panel, borderRadius: 10, overflow: "hidden", border: `2px solid ${i === active ? c : theme.colors.panelBorder}` }}>
              <div style={{ width: `${fill * 100}%`, height: "100%", background: `${c}aa`, display: "flex", alignItems: "center", justifyContent: "center", color: theme.colors.bg, fontFamily: theme.font.heading, fontWeight: 700, fontSize: 26, whiteSpace: "nowrap" }}>{it.sub}</div>
            </div>
          );
        })}
      </div>
      {items.map((it, i) => (
        <RiseIn key={i} delay={at[i]}>
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <div style={{ width: 18, height: 18, borderRadius: 18, background: colors[i % colors.length], flexShrink: 0 }} />
            <VisualIcon name={it.icon} color={colors[i % colors.length]} size={52} />
            <Label text={it.label} size={33} color={i === active ? theme.colors.text : theme.colors.textDim} />
          </div>
        </RiseIn>
      ))}
    </div>
  );
};

// A small story sketch: units ride a conveyor into a fixture that counts the
// screws, turns green at 6/6 and only then releases the unit.
const Assembly: React.FC<{ v: Visual; cue: Cue }> = ({ v }) => {
  const frame = useCurrentFrame();
  const CYCLE = 150;
  const ph = frame % CYCLE;
  const x = ph < 35 ? interpolate(ph, [0, 35], [-330, 0]) : ph < 115 ? 0 : interpolate(ph, [115, CYCLE], [0, 330]);
  const screws = ph < 40 ? 0 : Math.min(6, Math.floor((ph - 40) / 11) + 1);
  const done = screws === 6;
  const lamp = done ? theme.colors.good : theme.colors.danger;
  const belt = -(frame * 4) % 40;
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 16, width: "100%" }}>
      <svg width="100%" viewBox="0 0 640 400">
        {/* fixture */}
        <rect x={200} y={40} width={240} height={26} rx={6} fill={theme.colors.panelBorder} />
        <rect x={206} y={66} width={14} height={150} fill={theme.colors.panelBorder} />
        <rect x={420} y={66} width={14} height={150} fill={theme.colors.panelBorder} />
        <circle cx={320} cy={22} r={14} fill={lamp} style={{ filter: `drop-shadow(0 0 10px ${lamp})` }} />
        {/* torque head */}
        <rect x={300} y={66} width={40} height={done ? 40 : 40 + 18 * Math.abs(Math.sin(frame / 4)) * (screws > 0 ? 1 : 0)} rx={6} fill={theme.colors.accent2} />
        {/* unit */}
        <g transform={`translate(${x}, 0)`}>
          <rect x={235} y={170} width={170} height={60} rx={8} fill="#1b2438" stroke={theme.colors.textDim} strokeWidth={2} />
          {Array.from({ length: 6 }, (_, i) => (
            <circle key={i} cx={255 + i * 26} cy={186} r={6} fill={i < screws ? theme.colors.good : "#0a0e1a"} stroke={theme.colors.textDim} strokeWidth={1.5} />
          ))}
          <rect x={250} y={208} width={50} height={8} rx={3} fill={theme.colors.accent} />
        </g>
        {/* conveyor */}
        <rect x={20} y={232} width={600} height={22} rx={11} fill={theme.colors.panel} stroke={theme.colors.panelBorder} strokeWidth={2} />
        <line x1={30} y1={243} x2={610} y2={243} stroke={theme.colors.panelBorder} strokeWidth={4} strokeDasharray="20 20" strokeDashoffset={belt} />
        {Array.from({ length: 8 }, (_, i) => <circle key={i} cx={50 + i * 77} cy={262} r={8} fill={theme.colors.panelBorder} />)}
        {/* counter */}
        <text x={320} y={320} textAnchor="middle" fill={done ? theme.colors.good : theme.colors.text} fontFamily={theme.font.heading} fontWeight={700} fontSize={44}>
          {UI.screws(screws)}
        </text>
        <text x={320} y={362} textAnchor="middle" fill={done ? theme.colors.good : theme.colors.textDim} fontFamily={theme.font.body} fontSize={26}>
          {done ? UI.fixtureReleases : UI.fixtureLocked}
        </text>
      </svg>
      {v.label && <Sub text={v.label} />}
    </div>
  );
};

// Bars that grow one by one, with a dashed average line: shows how an
// average hides the peaks and valleys. `label: ""` drops the average (e.g. a
// Pareto); `note` then shows on its own. `value` draws the line there instead
// (e.g. TAKT or a target), named by `label`.
const Bars: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const frame = useCurrentFrame();
  const items = v.items ?? [];
  const at = reveals(items, cue);
  const vals = items.map((it) => it.value ?? 0);
  const max = Math.max(...vals, v.value ?? 0) * 1.1;
  const avg = v.value ?? vals.reduce((a, b) => a + b, 0) / Math.max(1, vals.length);
  const H = 360;
  const avgIn = useDraw(at[at.length - 1] + 20, 20);
  const showAvg = v.label !== "";
  const W = items.length > 4 ? 92 : 110;
  const GAP = items.length > 4 ? 20 : 34;
  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 14, width: "100%" }}>
      <div style={{ position: "relative", zIndex: 0, display: "flex", alignItems: "flex-end", justifyContent: "center", gap: GAP, height: H + 60, width: "100%" }}>
        {items.map((it, i) => {
          const g = useCount(1, at[i]);
          const c = it.tone ? toneColor(it.tone) : theme.colors.accent2;
          return (
            <div key={i} style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 8, opacity: frame >= at[i] ? 1 : 0 }}>
              <div style={{ color: c, fontFamily: theme.font.heading, fontSize: 40, fontWeight: 700 }}>{fmt((it.value ?? 0) * g)}</div>
              <div style={{ width: W, height: (H * (it.value ?? 0) / max) * g, background: `linear-gradient(${c}, ${c}77)`, borderRadius: "10px 10px 3px 3px" }} />
            </div>
          );
        })}
        {showAvg && <div style={{ position: "absolute", left: 0, right: 0, bottom: H * avg / max, opacity: avgIn * 0.8, borderTop: `3px dashed ${theme.colors.good}`, zIndex: -1 }} />}
      </div>
      <div style={{ display: "flex", gap: GAP }}>
        {items.map((it, i) => <div key={i} style={{ width: W, textAlign: "center" }}><Label text={it.label} size={24} color={theme.colors.textDim} weight={500} /></div>)}
      </div>
      <div style={{ opacity: avgIn, display: "flex", alignItems: "center", gap: 12, color: theme.colors.good, fontFamily: theme.font.heading, fontSize: 28, fontWeight: 700 }}>
        {showAvg && <div style={{ width: 40, borderTop: `3px dashed ${theme.colors.good}` }} />}
        {showAvg ? `${v.label ?? UI.average} ${fmt(avg)}${v.suffix ?? ""}${v.note ? `: ${v.note}` : ""}` : v.note}
      </div>
      <Sub text={v.unit} />
    </div>
  );
};

// A one-page document (e.g. a One Point Lesson sheet) whose sections appear in
// turn. An item with icon "goodbad" draws a good / not-good photo pair.
const Doc: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const frame = useCurrentFrame();
  const items = v.items ?? [];
  const at = reveals(items, cue);
  const active = latestOf(at, frame);
  const paper = "#e9eef6";
  const ink = "#1b2438";
  return (
    <div style={{ width: "88%", background: paper, borderRadius: 10, padding: "20px 22px", display: "flex", flexDirection: "column", gap: 12, boxShadow: "0 18px 40px #0008", transform: "rotate(-1deg)" }}>
      {items.map((it, i) => (
        <RiseIn key={i} delay={at[i]}>
          <div style={{ border: `3px solid ${i === active ? theme.colors.accent : "transparent"}`, borderRadius: 8, padding: 4 }}>
            {it.icon === "goodbad" ? (
              <div style={{ display: "flex", gap: 12 }}>
                {[true, false].map((good) => (
                  <div key={String(good)} style={{ flex: 1, height: 120, borderRadius: 8, background: good ? "#cdeedd" : "#f6d4d4", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 6 }}>
                    <Badge good={good} size={48} />
                    <div style={{ color: ink, fontFamily: theme.font.heading, fontSize: 22, fontWeight: 700 }}>{good ? UI.good : UI.notGood}</div>
                  </div>
                ))}
              </div>
            ) : (
              <div style={{ display: "flex", alignItems: "center", gap: 12, background: i === 0 ? ink : "#d7dfeb", borderRadius: 6, padding: "10px 14px" }}>
                {it.icon && <VisualIcon name={it.icon} color={i === 0 ? theme.colors.accent : ink} size={34} />}
                <div style={{ color: i === 0 ? "#fff" : ink, fontFamily: theme.font.heading, fontSize: 26, fontWeight: 700 }}>{it.label}</div>
              </div>
            )}
          </div>
        </RiseIn>
      ))}
    </div>
  );
};

// A skill matrix: people in rows, skills in columns, a level (0-4) per cell.
// Each row appears with its item's cue; higher levels are stronger colours.
// `prefix: "check"` shows a tick instead of the level (e.g. products x processes).
const Matrix: React.FC<{ v: Visual; cue: Cue }> = ({ v, cue }) => {
  const frame = useCurrentFrame();
  const items = v.items ?? [];
  const cols = v.cols ?? [];
  const at = reveals(items, cue);
  const active = latestOf(at, frame);
  const fill = (lv: number | null | undefined) =>
    lv == null ? "transparent" : lv >= 4 ? theme.colors.accent : lv === 3 ? theme.colors.good : lv === 2 ? theme.colors.accent2 : `${theme.colors.accent2}55`;
  const cell = 96;
  return (
    <div style={{ display: "grid", gridTemplateColumns: `150px repeat(${cols.length}, ${cell}px)`, gap: 10, alignItems: "center" }}>
      <div />
      {cols.map((c, j) => (
        <RiseIn key={j} delay={at[0] ?? 0}>
          <div style={{ textAlign: "center", color: theme.colors.textDim, fontFamily: theme.font.heading, fontSize: 24, fontWeight: 600 }}>{c}</div>
        </RiseIn>
      ))}
      {items.map((it, i) => (
        <React.Fragment key={i}>
          <RiseIn delay={at[i]}>
            <div style={{ color: i === active ? theme.colors.text : theme.colors.textDim, fontFamily: theme.font.heading, fontSize: 28, fontWeight: 700 }}>{it.label}</div>
          </RiseIn>
          {cols.map((_, j) => {
            const lv = it.cells?.[j];
            return (
              <RiseIn key={j} delay={at[i] + 4 + j * 3}>
                <div style={{ height: 64, borderRadius: 12, border: `2px solid ${lv == null ? theme.colors.panelBorder : fill(lv)}`, background: lv == null ? "transparent" : `${fill(lv)}${lv >= 3 ? "cc" : "88"}`, display: "flex", alignItems: "center", justifyContent: "center", color: lv != null && lv >= 3 ? theme.colors.bg : theme.colors.text, fontFamily: theme.font.heading, fontSize: 28, fontWeight: 700 }}>
                  {lv == null ? "–" : v.prefix === "check" ? "✓" : `${v.prefix ?? "L"}${lv}`}
                </div>
              </RiseIn>
            );
          })}
        </React.Fragment>
      ))}
      {v.note && (
        <div style={{ gridColumn: `1 / span ${cols.length + 1}`, marginTop: 10 }}>
          <RiseIn delay={(at[at.length - 1] ?? 0) + 20}><Sub text={v.note} /></RiseIn>
        </div>
      )}
    </div>
  );
};

const LAYOUTS: Record<Visual["type"], React.FC<{ v: Visual; cue: Cue }>> = {
  flow: Flow, ladder: Ladder, icons: Icons, steps: Steps, versus: Versus,
  compare: Compare, stat: Stat, timeline: Timeline, assembly: Assembly, bars: Bars, doc: Doc, matrix: Matrix,
};

export const PageVisual: React.FC<{ visual: Visual; bulletAt: number[]; exampleAt: number }> = ({ visual, bulletAt, exampleAt }) => {
  const frame = useCurrentFrame();
  const cue = { bulletAt, exampleAt };
  const L = LAYOUTS[visual.type];
  // `then`: a second picture takes over at its cue (crossfade)
  const swap = visual.then ? revealAt(cue, -1)({ with: visual.then.with ?? "example" }, 0) - 10 : Infinity;
  const first = visual.then ? interpolate(frame, [swap, swap + 10], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) : 1;
  const T = visual.then ? LAYOUTS[visual.then.type] : null;
  return (
    <div style={{ position: "relative", width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: `${theme.colors.panel}cc`, border: `1.5px solid ${theme.colors.panelBorder}`, borderRadius: 24, padding: "34px 34px" }}>
      {first > 0 && <div style={{ opacity: first, width: "100%", display: "flex", justifyContent: "center" }}><L v={visual} cue={cue} /></div>}
      {T && frame >= swap && (
        <div style={{ position: "absolute", inset: 34, display: "flex", alignItems: "center", justifyContent: "center" }}>
          <T v={visual.then!} cue={cue} />
        </div>
      )}
    </div>
  );
};
