# Job list for the two machines (docs/WORKPLAN.md). Only the PC runs this.
#
#   tools\jobs.ps1 list
#   tools\jobs.ps1 add -To laptop -Lang hindi -Comps GembaHi,HanchoHi
#   tools\jobs.ps1 take-back            # laptop's unstarted jobs -> PC (laptop is off for days)
#   tools\jobs.ps1 retry -To pc         # failed jobs -> todo again (after fixing the cause)
param(
    [Parameter(Mandatory, Position = 0)][ValidateSet('list', 'add', 'take-back', 'retry')][string]$Action,
    [ValidateSet('pc', 'laptop')][string]$To = 'pc',
    [string]$Lang,
    [string[]]$Comps,
    [string]$Drive = 'G:\My Drive'
)
$ErrorActionPreference = 'Stop'   # no native commands here, so 'Stop' is safe
$proj = Split-Path $PSScriptRoot -Parent
$root = Join-Path $Drive 'FFIQ_sync\jobs'
foreach ($m in 'pc', 'laptop') { foreach ($d in 'todo', 'doing', 'done', 'failed') { New-Item -ItemType Directory -Force "$root\$m\$d" | Out-Null } }

# composition -> lesson id, from scripts/lessons.ts
$ids = @{}
Select-String -Path "$proj\scripts\lessons.ts" -Pattern '^\s+(\w+): "(\w+)",' | ForEach-Object { $ids[$_.Matches[0].Groups[2].Value] = $_.Matches[0].Groups[1].Value }

function Find-Job($comp) { Get-ChildItem $root -Recurse -Filter "$comp.job" | Where-Object { $_.Directory.Name -ne 'done' } }

switch ($Action) {
    'list' {
        foreach ($m in 'pc', 'laptop') {
            foreach ($d in 'doing', 'todo', 'failed', 'done') {
                $f = Get-ChildItem "$root\$m\$d" -Filter *.job | ForEach-Object BaseName
                if ($f) { "{0,-7} {1,-7} {2}" -f $m, $d, ($f -join ', ') }
            }
        }
    }
    'add' {
        if (-not $Lang -or -not $Comps) { throw 'add needs -Lang and -Comps' }
        foreach ($c in $Comps) {
            if (-not $ids.ContainsKey($c)) { throw "$c is not in scripts/lessons.ts (run tools/gen_root.py first)" }
            $there = Find-Job $c
            if ($there) { "skip $c (already in $($there.Directory.Parent.Name)\$($there.Directory.Name))"; continue }
            Set-Content "$root\$To\todo\$c.job" "$Lang $($ids[$c]) $c" -Encoding ascii
            "added $c -> $To"
        }
    }
    'take-back' {
        Get-ChildItem "$root\laptop\todo" -Filter *.job | ForEach-Object { Move-Item $_.FullName "$root\pc\todo"; "moved $($_.BaseName) -> pc" }
    }
    'retry' {
        Get-ChildItem "$root\$To\failed" -Filter *.job | ForEach-Object { Move-Item $_.FullName "$root\$To\todo" -Force; "retry $($_.BaseName)" }
    }
}
