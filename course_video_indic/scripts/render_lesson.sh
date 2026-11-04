#!/usr/bin/env bash
# Render Indian-language page lessons one after another (same steps as the English
# scripts/render_lesson.sh): normal version at 8 Mbps, normalised to -14 LUFS, plus .srt,
# copied to final/<language>/ and Drive FFIQ_indic/final/<language>/.
#   bash scripts/render_lesson.sh hindi A3ProblemSolvingHi GembaHi
#   bash scripts/render_lesson.sh --dub hindi A3ProblemSolvingHi    (also the voice-only Dub)
# Concurrency 1: the English chat renders at the same time.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p out/tmp
TMP="$(cygpath -w "$PWD/out/tmp" 2>/dev/null || echo "$PWD/out/tmp")"
export TMP TEMP="$TMP" TMPDIR="$TMP"

EDGE="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"   # headless Chrome download is broken here; English renders use Edge too
DUB=0
if [ "${1:-}" = "--dub" ]; then DUB=1; shift; fi
LANGDIR=$1; shift
OUT=out/$LANGDIR
FINAL=final/$LANGDIR
DRIVE="G:/My Drive/FFIQ_indic/final/$LANGDIR"
mkdir -p "$OUT" "$FINAL" "$DRIVE"

echo "== bundling"
npx remotion bundle --out-dir=out/bundle --log=error

# Edge sometimes fails to start right after a long render ("Getting compositions" ->
# [object Object]); retry so one bad start doesn't stop the queue.
render() {
  for try in 1 2 3; do
    npx remotion render out/bundle "$1" "$2" --video-bitrate=8M --concurrency=1 --log=error "--browser-executable=$EDGE" && return 0
    echo "== $1 render failed (try $try), retrying in 60s"; sleep 60
  done
  return 1
}

for comp in "$@"; do
  echo "== $comp ($(date +%H:%M))"
  render "$comp" "$OUT/${comp}_raw.mp4"
  ffmpeg -v error -y -i "$OUT/${comp}_raw.mp4" -c:v copy \
    -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k "$OUT/${comp}.mp4"
  rm "$OUT/${comp}_raw.mp4"
  if [ "$DUB" = 1 ]; then
    render "${comp}Dub" "$OUT/${comp}Dub.mp4"
  fi
  npm run --silent srt
  cp "$OUT/${comp}.mp4" "out/${comp}.srt" "$FINAL/"
  cp "$OUT/${comp}.mp4" "out/${comp}.srt" "$DRIVE/"
  echo "== $comp done ($(date +%H:%M))"
done
echo "== all done"
