#!/usr/bin/env bash
# Make a Hindi lesson component from the A3 one: header + data wiring copied, then the
# lesson's own TEXT/POLISH block (stdin) appended.
#   bash tools/new_component.sh <id> <Comp> <DURATION_CONST> <module> [lang] < text_and_polish.tsx   (lang: hi default, mr, te, ta)
set -euo pipefail
cd "$(dirname "$0")/.."
ID=$1; COMP=$2; DUR=$3; MOD=$4; LG=${5:-hi}
mkdir -p src/lessons/$ID
F=src/lessons/$ID/$COMP.tsx
sed -n '1,/^};$/p' src/lessons/a3_hi/A3ProblemSolvingHi.tsx \
  | sed "s#captions/a3_hi/#captions/$ID/#; s#id: \"a3_hi\"#id: \"$ID\"#; s#a3_problem_solving_hi.py#$MOD.py#; s#Hindi version of A3 Problem Solving#$LG version of $COMP#" > "$F"
{ echo; cat; cat <<TS

const PLAN = planLesson(DATA, fps);
export const $DUR = PLAN.total;

export const $COMP: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("$LG");
  setUI("$LG");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
TS
} >> "$F"
echo "wrote $F"
