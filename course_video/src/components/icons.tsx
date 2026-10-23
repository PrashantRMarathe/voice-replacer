import React from "react";

// Clean animated line-icons (stroke draws itself in). Far more professional
// than emoji. Each takes a `color` and `progress` 0..1 for the draw-on effect.
type IconProps = { color: string; size?: number; progress?: number };

const base = (progress: number) => ({
  strokeDasharray: 100,
  strokeDashoffset: 100 - 100 * progress,
  transition: "none" as const,
});

const wrap = (size: number, children: React.ReactNode) => (
  <svg width={size} height={size} viewBox="0 0 48 48" fill="none" strokeWidth={2.4} strokeLinecap="round" strokeLinejoin="round">
    {children}
  </svg>
);

export const IconDefect = ({ color, size = 48, progress = 1 }: IconProps) =>
  wrap(size, <>
    <path d="M24 6 L42 38 H6 Z" stroke={color} pathLength={100} style={base(progress)} />
    <line x1="24" y1="18" x2="24" y2="28" stroke={color} pathLength={100} style={base(progress)} />
    <circle cx="24" cy="33" r="1.5" fill={color} />
  </>);

export const IconOverproduction = ({ color, size = 48, progress = 1 }: IconProps) =>
  wrap(size, <>
    <rect x="8" y="26" width="10" height="14" stroke={color} pathLength={100} style={base(progress)} />
    <rect x="19" y="18" width="10" height="22" stroke={color} pathLength={100} style={base(progress)} />
    <rect x="30" y="10" width="10" height="30" stroke={color} pathLength={100} style={base(progress)} />
  </>);

export const IconWaiting = ({ color, size = 48, progress = 1 }: IconProps) =>
  wrap(size, <>
    <circle cx="24" cy="24" r="16" stroke={color} pathLength={100} style={base(progress)} />
    <path d="M24 14 V24 L31 29" stroke={color} pathLength={100} style={base(progress)} />
  </>);

export const IconTalent = ({ color, size = 48, progress = 1 }: IconProps) =>
  wrap(size, <>
    <circle cx="24" cy="16" r="7" stroke={color} pathLength={100} style={base(progress)} />
    <path d="M12 40 C12 30 36 30 36 40" stroke={color} pathLength={100} style={base(progress)} />
  </>);

export const IconTransport = ({ color, size = 48, progress = 1 }: IconProps) =>
  wrap(size, <>
    <rect x="6" y="18" width="20" height="14" stroke={color} pathLength={100} style={base(progress)} />
    <path d="M26 22 H36 L42 28 V32 H26 Z" stroke={color} pathLength={100} style={base(progress)} />
    <circle cx="14" cy="34" r="3.5" stroke={color} />
    <circle cx="34" cy="34" r="3.5" stroke={color} />
  </>);

export const IconInventory = ({ color, size = 48, progress = 1 }: IconProps) =>
  wrap(size, <>
    <path d="M8 16 L24 8 L40 16 V34 L24 42 L8 34 Z" stroke={color} pathLength={100} style={base(progress)} />
    <path d="M8 16 L24 24 L40 16" stroke={color} pathLength={100} style={base(progress)} />
    <line x1="24" y1="24" x2="24" y2="42" stroke={color} pathLength={100} style={base(progress)} />
  </>);

export const IconMotion = ({ color, size = 48, progress = 1 }: IconProps) =>
  wrap(size, <>
    <circle cx="26" cy="10" r="4" stroke={color} />
    <path d="M26 15 L22 26 L30 30 L26 40 M22 26 L14 24 M30 22 L38 26" stroke={color} pathLength={100} style={base(progress)} />
  </>);

export const IconProcessing = ({ color, size = 48, progress = 1 }: IconProps) =>
  wrap(size, <>
    <circle cx="24" cy="24" r="7" stroke={color} pathLength={100} style={base(progress)} />
    <path d="M24 8 V13 M24 35 V40 M8 24 H13 M35 24 H40 M13 13 L16 16 M35 35 L32 32 M35 13 L32 16 M13 35 L16 32" stroke={color} pathLength={100} style={base(progress)} />
  </>);

export const WASTE_ICONS = [
  IconDefect, IconOverproduction, IconWaiting, IconTalent,
  IconTransport, IconInventory, IconMotion, IconProcessing,
];
