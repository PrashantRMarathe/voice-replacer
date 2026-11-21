#!/usr/bin/env bash
# Voice one Indian-language lesson with edge-tts, then level + caption-sync it.
#   bash tools/build_hindi.sh <module> [--force]     e.g. a3_problem_solving_hi
set -euo pipefail
cd "$(dirname "$0")/.."
PY=../.venv/Scripts/python.exe
MOD=$1; shift || true
ID=$($PY -c "import sys; sys.path.insert(0,'narration'); import $MOD as m; print(m.ID)")
$PY narration/$MOD.py "$@"
WAV=out/ms_$ID
mkdir -p "$WAV"
for f in public/audio/$ID/*.mp3; do
  k=$(basename "$f" .mp3)
  ffmpeg -loglevel error -y -i "$f" -ar 24000 -ac 1 "$WAV/$k.wav"
done
$PY narration/import_clones.py "$MOD" "$WAV"
