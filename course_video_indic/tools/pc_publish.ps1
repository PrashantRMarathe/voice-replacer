# PC only: hand the current work to the laptop (docs/WORKPLAN.md).
# Code goes through git (small text files); audio goes through Drive (never git).
#
#   powershell -ExecutionPolicy Bypass -File tools\pc_publish.ps1
param([string]$Drive = 'G:\My Drive')
$ErrorActionPreference = 'Continue'   # 'Stop' turns git's normal stderr into errors in PowerShell 5.1
$proj = Split-Path $PSScriptRoot -Parent
Set-Location $proj
$sync = Join-Path $Drive 'FFIQ_sync'

$dirty = git status --porcelain -- narration src scripts tools package.json
if ($dirty) { $dirty; throw 'commit these changes first, so the laptop renders the same text' }
git fetch --quiet
if ((git rev-list --count '@{u}..HEAD') -ne '0') { throw 'push first (git push), the laptop pulls from GitHub' }

"copying audio to Drive (only changed files)"
robocopy public\audio (Join-Path $sync 'audio') /MIR /NJH /NJS /NP /NFL /NDL /R:3 /W:10 | Out-Null
if ($LASTEXITCODE -ge 8) { throw "audio copy failed (robocopy $LASTEXITCODE)" }

$commit = (git rev-parse HEAD).Trim()
$files = Get-ChildItem public\audio -Recurse -File
$bytes = ($files | Measure-Object Length -Sum).Sum
# files/bytes let the laptop wait until Drive has really downloaded all the audio
Set-Content (Join-Path $sync 'READY.txt') "commit=$commit`nfiles=$($files.Count)`nbytes=$bytes`ntime=$(Get-Date -Format 'yyyy-MM-dd HH:mm')" -Encoding ascii
"published $commit. The laptop can run tools\worker.ps1 -Machine laptop once Drive has uploaded."
