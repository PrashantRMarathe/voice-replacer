#!/usr/bin/env bash
# Render page lessons one after another: normal version (8 Mbps, loudness
# normalised to -14 LUFS) and the voice-only Dub version.
#   bash scripts/render_lesson.sh MudaMuraMuri NextInspection
#   bash scripts/render_lesson.sh --dub-only MudaMuraMuri
#   bash scripts/render_lesson.sh --no-dub Yamazumi     (normal version only)
# Renders from a pre-built bundle in out/bundle: Remotion's default temp bundle
# lives in %TEMP% and was deleted mid-render when another Remotion process
# exited (two renders, or a render plus stills, at the same time).
# Its working files (audio mixing, Chrome profile) also go to out/tmp, not
# %TEMP%: something on this PC clears %TEMP% and killed renders at the last frame.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p out/tmp
TMP="$(cygpath -w "$PWD/out/tmp" 2>/dev/null || echo "$PWD/out/tmp")"
export TMP TEMP="$TMP" TMPDIR="$TMP"

DUB_ONLY=0
NO_DUB=0
if [ "${1:-}" = "--dub-only" ]; then DUB_ONLY=1; shift; fi
if [ "${1:-}" = "--no-dub" ]; then NO_DUB=1; shift; fi

echo "== bundling"
npx remotion bundle --out-dir=out/bundle --log=error

for comp in "$@"; do
  if [ "$DUB_ONLY" = 0 ]; then
    echo "== $comp"
    npx remotion render out/bundle "$comp" "out/${comp}_raw.mp4" --video-bitrate=8M --log=error
    ffmpeg -v error -y -i "out/${comp}_raw.mp4" -c:v copy \
      -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k "out/${comp}.mp4"
  fi
  [ "$NO_DUB" = 1 ] && continue
  echo "== ${comp}Dub"
  npx remotion render out/bundle "${comp}Dub" "out/${comp}Dub.mp4" --video-bitrate=8M --log=error
done
echo "== all done"
