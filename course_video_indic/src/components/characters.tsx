import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "../theme";

// ---------------------------------------------------------------------------
// Custom flat-vector characters (friendly corporate-explainer style), drawn as
// SVG so they are fully controllable, consistent across all 40 lessons, and
// animatable. Parametric: gender, hair, outfit, PPE, pose, expression.
// ---------------------------------------------------------------------------

export type Pose = "pointing" | "crossed" | "resting" | "carrying" | "reaching";
export type Expr = "smile" | "neutral" | "tired" | "concerned" | "surprised";
export type PPE = {
  glasses?: boolean; // safety glasses
  mask?: boolean;    // face mask (hides mouth)
  cap?: boolean;     // factory cap
  coat?: boolean;    // white ESD coat (overrides outfit color)
};

const SKIN = "#e8b98f";
const SKIN_DARK = "#cf9a6e";

// ---- Face: eyebrows + eyes (+lashes) + soft mouth, expressive ----
const Face: React.FC<{ expr: Expr; stroke: string; mask?: boolean; female?: boolean }> = ({ expr, stroke, mask, female }) => {
  const eye = (cx: number, dir: number) =>
    expr === "surprised" ? <circle cx={cx} cy={-2} r={3.6} fill={stroke} /> :
    expr === "tired" ? <path d={`M ${cx - 5} -2 q 5 3 10 0`} fill="none" stroke={stroke} strokeWidth={2.4} strokeLinecap="round" /> :
    <g>
      <ellipse cx={cx} cy={-2} rx={3} ry={3.4} fill={stroke} />
      {/* soft catch-light */}
      <circle cx={cx + 1} cy={-3.2} r={0.9} fill="#ffffff" />
      {/* subtle lashes for a softer, feminine look */}
      {female && <line x1={cx + 3.4 * dir} y1={-4.2} x2={cx + 6 * dir} y2={-5.4} stroke={stroke} strokeWidth={1.6} strokeLinecap="round" />}
    </g>;

  const brow = (cx: number, s: number) => {
    const y = expr === "concerned" || expr === "tired" ? -12.5 : -13.5;
    const tilt = expr === "concerned" ? 3.5 * s : expr === "surprised" ? -3 : expr === "tired" ? 2.5 * s : 0.5 * s;
    return <path d={`M ${cx - 7} ${y + tilt} Q ${cx} ${y - 1.5} ${cx + 7} ${y - tilt * 0.3}`} fill="none" stroke={stroke} strokeWidth={2.2} strokeLinecap="round" />;
  };

  const mouth =
    expr === "smile" ? "M -8 10 Q 0 18 8 10" :
    expr === "concerned" ? "M -8 15 Q 0 10 8 15" :
    expr === "tired" ? "M -7 14 Q 0 12 7 14" :
    expr === "surprised" ? "M -5 12 Q 0 19 5 12 Q 0 9 -5 12" :
    "M -7 13 Q 0 15 7 13";

  // soft lips for a more elegant feminine face
  const lips = female && (expr === "smile" || expr === "neutral");

  return (
    <g>
      {brow(-11, 1)}
      {brow(11, -1)}
      {eye(-11, -1)}
      {eye(11, 1)}
      {!mask && (lips ? (
        <g>
          <path d={expr === "smile" ? "M -8 10 Q 0 17 8 10 Q 0 21 -8 10" : "M -7 12 Q 0 15 7 12 Q 0 17 -7 12"}
                fill="#d9736e" stroke="#b8524d" strokeWidth={1} />
          <path d="M -8 10 Q 0 9 8 10" fill="none" stroke="#b8524d" strokeWidth={1} opacity={0.6} />
        </g>
      ) : (
        <path d={mouth} fill="none" stroke={stroke} strokeWidth={2.6} strokeLinecap="round" />
      ))}
      {/* soft blush */}
      {!mask && <>
        <ellipse cx={-20} cy={7} rx={5} ry={3} fill="#f2a98f" opacity={0.55} />
        <ellipse cx={20} cy={7} rx={5} ry={3} fill="#f2a98f" opacity={0.55} />
      </>}
    </g>
  );
};

// ---- Arms per pose. Hand = skin dot at the end. ----
const Arms: React.FC<{ pose: Pose; sleeve: string; stroke: string }> = ({ pose, sleeve }) => {
  const sw = 20;
  const arm = (d: string) => <path d={d} fill="none" stroke={sleeve} strokeWidth={sw} strokeLinecap="round" />;
  const hand = (x: number, y: number) => <circle cx={x} cy={y} r={9} fill={SKIN} />;
  switch (pose) {
    case "pointing":
      return (<g>
        {arm("M 42 6 q 34 6 40 -34")}{hand(82, -30)}
        {arm("M -42 10 q -16 30 -8 60")}{hand(-50, 72)}
      </g>);
    case "crossed":
      return (<g>
        {arm("M -40 16 q 44 6 80 -4")}
        {arm("M 40 10 q -44 10 -80 2")}
        {hand(38, 12)}{hand(-38, 18)}
      </g>);
    case "carrying":
      return (<g>
        {arm("M -40 14 q -8 16 -2 34")}{hand(-42, 50)}
        {arm("M 40 14 q 8 16 2 34")}{hand(42, 50)}
      </g>);
    case "reaching":
      return (<g>
        {arm("M 40 12 q 38 -8 54 -36")}{hand(96, -26)}
        {arm("M -40 14 q -10 20 -2 40")}{hand(-44, 56)}
      </g>);
    default: // resting
      return (<g>
        {arm("M -42 14 q -10 30 -4 58")}{hand(-48, 72)}
        {arm("M 42 14 q 10 30 4 58")}{hand(48, 72)}
      </g>);
  }
};

export const Character: React.FC<{
  size?: number;
  gender?: "f" | "m";
  outfit?: string;
  hairColor?: string;
  expr?: Expr;
  pose?: Pose;
  ppe?: PPE;
  top?: "shirt" | "blazer" | "coat";
}> = ({
  size = 320, gender = "f", outfit = theme.colors.accent2,
  hairColor = "#3a2416", expr = "smile", pose = "resting", ppe = {}, top = "shirt",
}) => {
  const stroke = "#121824";
  const isCoat = ppe.coat || top === "coat";
  const isBlazer = top === "blazer" && !isCoat;
  const sleeve = isCoat ? "#eef2f8" : outfit;
  const baseTorso = isCoat ? "#eef2f8" : outfit;
  const rawId = React.useId();
  const gid = rawId.replace(/[:]/g, "");
  const hairFill = `url(#hair_${gid})`;
  const torso = `url(#torso_${gid})`;
  // a lighter shade of the hair for shine
  const lighten = (hex: string, amt = 40) => {
    const n = parseInt(hex.replace("#", ""), 16);
    const r = Math.min(255, ((n >> 16) & 255) + amt);
    const g = Math.min(255, ((n >> 8) & 255) + amt);
    const b = Math.min(255, (n & 255) + amt);
    return `rgb(${r},${g},${b})`;
  };

  return (
    <svg width={size} height={size * 1.22} viewBox="-120 -180 240 310">
      <defs>
        <linearGradient id={`hair_${gid}`} x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor={lighten(hairColor, 34)} />
          <stop offset="55%" stopColor={hairColor} />
          <stop offset="100%" stopColor={hairColor} />
        </linearGradient>
        <linearGradient id={`torso_${gid}`} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor={lighten(baseTorso, 18)} />
          <stop offset="100%" stopColor={baseTorso} />
        </linearGradient>
        <radialGradient id={`skin_${gid}`} cx="50%" cy="40%" r="65%">
          <stop offset="0%" stopColor="#f3c9a0" />
          <stop offset="100%" stopColor={SKIN} />
        </radialGradient>
      </defs>
      {/* legs (slim, longer) */}
      <path d="M -15 96 q -3 46 -5 78" fill="none" stroke="#2f3a52" strokeWidth={20} strokeLinecap="round" />
      <path d="M 15 96 q 3 46 5 78" fill="none" stroke="#2f3a52" strokeWidth={20} strokeLinecap="round" />
      <ellipse cx="-23" cy="120" rx="16" ry="7.5" fill={stroke} />
      <ellipse cx="23" cy="120" rx="16" ry="7.5" fill={stroke} />

      {/* torso (slimmer waist, soft shoulders) */}
      <path d="M -40 -16 q 40 -22 80 0 q 2 20 4 40 l 2 66 q -46 18 -92 0 l 2 -66 q 2 -20 2 -40 z" fill={torso} stroke={stroke} strokeWidth={3} />
      {isCoat && (
        <g>
          <path d="M 0 -20 L 0 86" stroke="#c9d3e2" strokeWidth={2.5} />
          <path d="M -14 -18 L 0 -2 L 14 -18" fill="none" stroke="#c9d3e2" strokeWidth={2.5} />
          {[16, 36, 56].map((y) => <circle key={y} cx="0" cy={y} r="2.6" fill="#c9d3e2" />)}
        </g>
      )}
      {isBlazer && (
        <g>
          {/* blazer lapels + inner blouse V + buttons */}
          <path d="M -8 -18 L -2 26 L 0 -8 L 2 26 L 8 -18" fill={outfit} stroke={stroke} strokeWidth={2.2} />
          <path d="M -7 -16 L 0 2 L 7 -16" fill="#f4f7fb" stroke={stroke} strokeWidth={1.6} />
          <circle cx="0" cy="40" r="2.4" fill={stroke} opacity={0.5} />
          <circle cx="0" cy="56" r="2.4" fill={stroke} opacity={0.5} />
        </g>
      )}

      <Arms pose={pose} sleeve={sleeve} stroke={stroke} />

      {/* neck (a touch longer, elegant) */}
      <rect x="-8" y="-42" width="16" height="30" rx="7" fill={SKIN} />
      <path d="M -8 -16 q 8 8 16 0" fill={SKIN_DARK} opacity={0.4} />

      {/* head (smaller, refined) */}
      <g transform="translate(0,-70)">
        {/* female hair: soft volume behind + a neat ponytail to one side */}
        {gender === "f" && !ppe.cap && (
          <g fill={hairFill}>
            <path d="M -32 -6 q -14 44 0 62 q -22 -4 -24 -38 q -2 -42 24 -48 z" />
            <path d="M 32 -6 q 10 30 4 50 q 18 10 22 -6 q 6 -36 -10 -54 z" />
            <ellipse cx="46" cy="40" rx="11" ry="26" transform="rotate(16 46 40)" />
            {/* ponytail tie */}
            <rect x="34" y="12" width="12" height="7" rx="3" fill={theme.colors.accent} />
          </g>
        )}
        <circle cx="0" cy="0" r="31" fill={`url(#skin_${gid})`} stroke={stroke} strokeWidth={3} />
        <circle cx="-31" cy="2" r="5" fill={SKIN_DARK} />
        <circle cx="31" cy="2" r="5" fill={SKIN_DARK} />
        {/* earrings */}
        {gender === "f" && <>
          <circle cx="-31" cy="9" r="2.6" fill="#f2c94c" />
          <circle cx="31" cy="9" r="2.6" fill="#f2c94c" />
        </>}

        {ppe.cap ? (
          <g>
            <path d="M -34 -8 q 2 -32 34 -32 q 32 0 34 32 q -17 -13 -34 -13 q -17 0 -34 13 z" fill="#2b6cb0" />
            <path d="M -38 -8 q -8 2 -10 8 q 26 -6 48 -6 z" fill="#214e82" />
          </g>
        ) : (
          <g>
            <path d={gender === "f"
              ? "M -33 -4 q -2 -40 33 -40 q 35 0 33 40 q -8 -18 -20 -22 q 1 9 -5 13 q -7 -13 -21 -11 q -14 2 -20 20 z"
              : "M -32 -6 q 0 -38 32 -37 q 32 -1 32 37 q -15 -19 -32 -19 q -17 0 -32 19 z"}
              fill={hairFill} />
            {/* hair shine highlight */}
            <path d="M -16 -34 q 16 -8 34 -2" fill="none" stroke={lighten(hairColor, 70)} strokeWidth={3} strokeLinecap="round" opacity={0.6} />
          </g>
        )}

        <Face expr={expr} stroke={stroke} mask={ppe.mask} female={gender === "f"} />

        {/* safety glasses */}
        {ppe.glasses && (
          <g>
            <rect x="-22" y="-8" width="18" height="14" rx="6" fill="#bfe9ff55" stroke="#9fd8f0" strokeWidth={2} />
            <rect x="4" y="-8" width="18" height="14" rx="6" fill="#bfe9ff55" stroke="#9fd8f0" strokeWidth={2} />
            <line x1="-4" y1="-2" x2="4" y2="-2" stroke="#9fd8f0" strokeWidth={2} />
          </g>
        )}

        {/* face mask */}
        {ppe.mask && (
          <g>
            <path d="M -18 8 q 18 12 36 0 l 0 14 q -18 10 -36 0 z" fill="#e8edf4" stroke="#c3ccd8" strokeWidth={2} />
            <line x1="-18" y1="12" x2="18" y2="12" stroke="#c3ccd8" strokeWidth={1.5} />
            <line x1="-18" y1="17" x2="18" y2="17" stroke="#c3ccd8" strokeWidth={1.5} />
          </g>
        )}
      </g>
    </svg>
  );
};

// ---- animation helpers ----
const useBob = (speed = 1, amp = 6) => {
  const frame = useCurrentFrame();
  return Math.sin(frame / (18 / speed)) * amp;
};
const useSlide = (fromX: number, delay = 0) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - delay, fps, config: { damping: 18 } });
  return { x: interpolate(s, [0, 1], [fromX, 0]), opacity: s };
};

// ---- THE GUIDE: consistent female host, light safety glasses, no mask ----
export const Guide: React.FC<{ size?: number; delay?: number; fromX?: number; expr?: Expr }> = ({
  size = 340, delay = 0, fromX = 220, expr = "smile",
}) => {
  const bob = useBob(1, 5);
  const { x, opacity } = useSlide(fromX, delay);
  return (
    <div style={{ opacity, transform: `translate(${x}px, ${bob}px)` }}>
      <Character size={size} gender="f" outfit={theme.colors.accent} hairColor="#3a2416" expr={expr} pose="pointing" top="blazer" />
    </div>
  );
};

// ---- A WORKER ACTOR: female, full PPE (ESD coat, glasses, mask, cap) ----
export const Worker: React.FC<{
  size?: number; delay?: number; fromX?: number; pose?: Pose; expr?: Expr; bobSpeed?: number; mask?: boolean;
}> = ({ size = 320, delay = 0, fromX = -200, pose = "crossed", expr = "tired", bobSpeed = 0.7, mask = true }) => {
  const bob = useBob(bobSpeed, 5);
  const { x, opacity } = useSlide(fromX, delay);
  return (
    <div style={{ opacity, transform: `translate(${x}px, ${bob}px)` }}>
      <Character size={size} gender="f" hairColor="#241a14" expr={expr} pose={pose} ppe={{ coat: true, glasses: true, mask, cap: true }} />
    </div>
  );
};

// A small speech bubble next to a character.
export const SpeechBubble: React.FC<{ text: string; delay?: number }> = ({ text, delay = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - delay, fps, config: { damping: 14 } });
  return (
    <div
      style={{
        opacity: s,
        transform: `scale(${interpolate(s, [0, 1], [0.8, 1])})`,
        transformOrigin: "bottom left",
        background: theme.colors.panel,
        border: `2px solid ${theme.colors.accent}`,
        borderRadius: 18,
        padding: "18px 26px",
        color: theme.colors.text,
        fontFamily: theme.font.body,
        fontSize: 30,
        maxWidth: 520,
        boxShadow: `0 0 26px ${theme.colors.accent}33`,
      }}
    >
      {text}
    </div>
  );
};
