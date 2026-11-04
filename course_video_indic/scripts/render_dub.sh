#!/usr/bin/env bash
# Dub videos: render each English lesson once (music + effects, no voice), then lay every
# language over it as its own audio track + subtitles (tools/fit_dub.py all).
#   bash scripts/render_dub.sh "hi te" A3ProblemSolving Gemba ...     (no names = all in src/dub/lessons.json)
# Run python tools/make_dub.py first after the English lessons change.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p out/tmp out/dub
TMP="$(cygpath -w "$PWD/out/tmp" 2>/dev/null || echo "$PWD/out/tmp")"
export TMP TEMP="$TMP" TMPDIR="$TMP" PYTHONIOENCODING=utf-8
PY=../.venv/Scripts/python.exe
EDGE="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
LANGS=$1; shift
if [ $# -eq 0 ]; then set -- $($PY -c "import json;print(' '.join(json.load(open('src/dub/lessons.json')).values()))"); fi

echo "== bundling"
npx remotion bundle src/dub/index.tsx --out-dir=out/bundle_dub --log=error

for comp in "$@"; do
  id=$($PY -c "import json,sys;print({v:k for k,v in json.load(open('src/dub/lessons.json')).items()}[sys.argv[1]])" "$comp")
  echo "== $comp ($(date +%H:%M))"
  if [ ! -f "out/dub/${comp}_video.mp4" ]; then
    # Edge sometimes fails to start right after a long render: retry
    for try in 1 2 3; do
      npx remotion render out/bundle_dub "${comp}DubVideo" "out/dub/${comp}_video.mp4" --video-bitrate=8M \
        --concurrency=1 --port=3937 --log=error "--browser-executable=$EDGE" && break
      rm -f "out/dub/${comp}_video.mp4"
      [ $try = 3 ] && { echo "== $comp FAILED"; continue 2; }
      echo "== $comp render failed (try $try), retrying in 60s"; sleep 60
    done
  fi
  $PY tools/fit_dub.py all "$id" $LANGS | grep -v " speed "
  echo "== $comp done ($(date +%H:%M))"
done
echo "== all done"
