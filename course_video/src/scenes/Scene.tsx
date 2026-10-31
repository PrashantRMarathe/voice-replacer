import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

// Wraps a scene with a punchy entrance (slide + scale + fade) and a soft slide-
// out, so cuts between scenes feel dynamic and premium rather than static fades.
export const Scene: React.FC<{ children: React.ReactNode; dir?: 1 | -1 }> = ({
  children,
  dir = 1,
}) => {
  const frame = useCurrentFrame();
  const { durationInFrames, fps } = useVideoConfig();

  const enter = spring({ frame, fps, config: { damping: 18, mass: 0.8 } });
  const exitStart = durationInFrames - 16;
  const exit = interpolate(frame, [exitStart, durationInFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const x = interpolate(enter, [0, 1], [70 * dir, 0]) + exit * -50 * dir;
  const scale = interpolate(enter, [0, 1], [0.94, 1]);
  const opacity = Math.min(enter, 1 - exit);

  return (
    <AbsoluteFill
      style={{
        opacity,
        transform: `translateX(${x}px) scale(${scale})`,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      {children}
    </AbsoluteFill>
  );
};
