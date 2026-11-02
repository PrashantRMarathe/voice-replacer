#!/usr/bin/env bash
# Voice lessons with a watchdog (edge-tts can hang with no timeout), then level + caption-sync.
# Only missing clips are voiced, so it can simply be run again after a stop.
#   bash tools/voice_lessons.sh kaizen_ta burn_down_chart_ta
set -uo pipefail
cd "$(dirname "$0")/.."
export PYTHONIOENCODING=utf-8
PY=../.venv/Scripts/python.exe
for MOD in "$@"; do
  ID=$($PY -c "import sys; sys.path.insert(0,'narration'); import $MOD as m; print(m.ID)")
  ok=0
  for try in 1 2 3 4 5 6 7 8 9 10; do
    timeout 240 $PY narration/$MOD.py > /dev/null; rc=$?
    [ $rc -eq 0 ] && ok=1 && break
    echo "!! $MOD attempt $try rc=$rc"
    # a killed attempt can leave a half-written clip: the newest one is voiced again
    if [ $rc -eq 124 ]; then rm -f "$(ls -t public/audio/$ID/*.mp3 2>/dev/null | head -1)"; fi
  done
  [ $ok -eq 1 ] || { echo "FAILED $MOD"; continue; }
  WAV=out/ms_$ID; mkdir -p "$WAV"
  for f in public/audio/$ID/*.mp3; do ffmpeg -loglevel error -y -i "$f" -ar 24000 -ac 1 "$WAV/$(basename "$f" .mp3).wav"; done
  $PY narration/import_clones.py "$MOD" "$WAV" 2>&1 | tail -1
  echo "== $MOD done, $(ls public/audio/$ID/*.mp3 | wc -l) clips"
done
