import React from "react";

// Line icons for page visuals (same style as icons.tsx: 48x48 box, stroke draws
// itself in with `progress`). Referenced by name from a page's `visual` data, so
// lesson scripts can pick one without touching code.
type P = { color: string; size?: number; progress?: number };

const draw = (progress: number) => ({ strokeDasharray: 100, strokeDashoffset: 100 - 100 * progress });

const icon = (paths: string[], dots: [number, number][] = []) =>
  ({ color, size = 48, progress = 1 }: P) => (
    <svg width={size} height={size} viewBox="0 0 48 48" fill="none" strokeWidth={2.4} strokeLinecap="round" strokeLinejoin="round">
      {paths.map((d, i) => <path key={i} d={d} stroke={color} pathLength={100} style={draw(progress)} />)}
      {dots.map(([x, y], i) => <circle key={i} cx={x} cy={y} r={1.8} fill={color} opacity={progress} />)}
    </svg>
  );

export const VISUAL_ICONS: Record<string, React.FC<P>> = {
  key: icon(["M10 24 a8 8 0 1 0 16 0 a8 8 0 1 0 -16 0", "M26 24 H42 V30", "M36 24 V29"]),
  sticker: icon(["M8 10 H34 L40 16 V38 H8 Z", "M34 10 V16 H40", "M14 22 H32", "M14 29 H26"]),
  warning: icon(["M24 6 L43 39 H5 Z", "M24 18 V28"], [[24, 33]]),
  pin: icon(["M18 40 V20 a6 6 0 0 1 12 0 V40", "M10 40 H38", "M24 8 V14"]),
  barcode: icon(["M8 12 V36", "M13 12 V36", "M17 12 V36", "M23 12 V36", "M27 12 V36", "M33 12 V36", "M36 12 V36", "M40 12 V36"]),
  sensor: icon(["M6 24 C12 14 36 14 42 24 C36 34 12 34 6 24 Z", "M18 24 a6 6 0 1 0 12 0 a6 6 0 1 0 -12 0"]),
  lock: icon(["M12 22 H36 V40 H12 Z", "M16 22 V15 a8 8 0 0 1 16 0 V22", "M24 29 V33"]),
  power: icon(["M24 6 V22", "M15 12 a14 14 0 1 0 18 0"]),
  check: icon(["M10 25 L20 35 L38 14"]),
  cross: icon(["M12 12 L36 36", "M36 12 L12 36"]),
  test: icon(["M18 6 H30", "M20 6 V20 L9 38 a3 3 0 0 0 3 4 H36 a3 3 0 0 0 3 -4 L28 20 V6", "M14 30 H34"]),
  shape: icon(["M8 14 H20 a4 4 0 0 1 8 0 H40 V40 H8 Z", "M18 26 H30 V34 H18 Z"]),
  count: icon(["M8 10 H40 V38 H8 Z", "M15 18 V30", "M21 18 V30", "M27 18 V30", "M33 18 V30", "M12 27 L36 21"]),
  sequence: icon(["M8 12 H14", "M8 24 H14", "M8 36 H14", "M20 12 H40", "M20 24 H40", "M20 36 H40"]),
  person: icon(["M17 15 a7 7 0 1 0 14 0 a7 7 0 1 0 -14 0", "M10 41 C10 29 38 29 38 41"]),
  gear: icon(["M17 24 a7 7 0 1 0 14 0 a7 7 0 1 0 -14 0", "M24 7 V13 M24 35 V41 M7 24 H13 M35 24 H41 M12 12 L16 16 M36 36 L32 32 M36 12 L32 16 M12 36 L16 32"]),
  chartUp: icon(["M8 8 V40 H40", "M13 33 L21 25 L27 29 L38 15", "M31 15 H38 V22"]),
  chartDown: icon(["M8 8 V40 H40", "M13 15 L21 23 L27 19 L38 33", "M31 33 H38 V26"]),
  box: icon(["M8 16 L24 8 L40 16 V34 L24 42 L8 34 Z", "M8 16 L24 24 L40 16", "M24 24 V42"]),
  scale: icon(["M24 8 V38", "M14 38 H34", "M8 14 H40", "M8 14 L4 26 H12 Z", "M40 14 L36 26 H44 Z"]),
  tray: icon(["M6 18 H42 V36 H6 Z", "M10 22 H20 V32 H10 Z", "M24 22 H30 V32 H24 Z", "M33 22 H38 V32 H33 Z"]),
  clipboard: icon(["M12 10 H36 V42 H12 Z", "M18 6 H30 V13 H18 Z", "M17 22 L20 25 L25 19", "M28 23 H32", "M17 33 L20 36 L25 30", "M28 34 H32"]),
  chip: icon(["M14 14 H34 V34 H14 Z", "M20 20 H28 V28 H20 Z", "M19 8 V14 M24 8 V14 M29 8 V14 M19 34 V40 M24 34 V40 M29 34 V40 M8 19 H14 M8 24 H14 M8 29 H14 M34 19 H40 M34 24 H40 M34 29 H40"]),
  label: icon(["M8 14 H30 L40 24 L30 34 H8 Z"], [[16, 24]]),
  screw: icon(["M14 10 H34 L30 16 H18 Z", "M20 16 V38 L24 42 L28 38 V16", "M20 22 L28 26", "M20 29 L28 33"]),
  shield: icon(["M24 6 L40 12 V24 C40 33 33 39 24 42 C15 39 8 33 8 24 V12 Z", "M17 24 L22 29 L31 19"]),
  search: icon(["M8 20 a12 12 0 1 0 24 0 a12 12 0 1 0 -24 0", "M29 29 L41 41"]),
  hand: icon(["M16 40 V22 a3 3 0 0 1 6 0 V12 a3 3 0 0 1 6 0 V22 V14 a3 3 0 0 1 6 0 V30 a10 10 0 0 1 -10 10 Z"]),
  calendar: icon(["M8 12 H40 V40 H8 Z", "M8 20 H40", "M16 8 V14", "M32 8 V14"]),
  clock: icon(["M8 24 a16 16 0 1 0 32 0 a16 16 0 1 0 -32 0", "M24 14 V24 L31 29"]),
  walk: icon(["M26 6 a3.5 3.5 0 1 0 0.1 0", "M25 14 L21 26 L28 31 L25 42", "M21 26 L14 24", "M28 19 L36 23", "M21 26 L16 40"]),
  camera: icon(["M6 16 H32 V34 H6 Z", "M32 21 L42 16 V34 L32 29", "M12 22 H18"]),
  wave: icon(["M4 24 C10 8 16 8 20 24 C24 40 30 40 34 24 C37 14 41 14 44 20"]),
  weight: icon(["M14 18 H34 L40 40 H8 Z", "M19 18 a5 5 0 0 1 10 0"]),
  stack: icon(["M8 34 H40 V42 H8 Z", "M11 26 H37 V34 H11 Z", "M14 18 H34 V26 H14 Z", "M17 10 H31 V18 H17 Z"]),
  trash: icon(["M10 14 H38", "M18 14 V9 H30 V14", "M13 14 L15 41 H33 L35 14", "M21 20 V35", "M27 20 V35"]),
  wrench: icon(["M28 8 a9 9 0 0 0 -8 12 L8 32 a3 3 0 0 0 0 4 L12 40 a3 3 0 0 0 4 0 L28 28 a9 9 0 0 0 12 -8 L34 24 L28 20 L30 12 Z"]),
};

export const VisualIcon: React.FC<P & { name?: string }> = ({ name, ...p }) => {
  const C = (name && VISUAL_ICONS[name]) || VISUAL_ICONS.check;
  return <C {...p} />;
};
