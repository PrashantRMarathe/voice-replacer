# Render worker for the two-machine setup (docs/WORKPLAN.md). Runs this machine's job list
# from Drive, checks every video with tools/validate_video.py, and only then copies it to final.
#
#   powershell -ExecutionPolicy Bypass -File tools\worker.ps1 -Machine laptop
#   powershell -ExecutionPolicy Bypass -File tools\worker.ps1 -Machine pc -Concurrency 1
#
# Laptop: first pulls git and the audio from Drive, and stops if the PC has not published
# this exact commit (tools\pc_publish.ps1). A job left in doing\ (laptop switched off) is
# simply rendered again on the next start.
param(
    [Parameter(Mandatory)][ValidateSet('pc', 'laptop')][string]$Machine,
    [int]$Concurrency = 2,
    [string]$Drive = 'G:\My Drive'
)
$ErrorActionPreference = 'Continue'   # 'Stop' turns npx/ffmpeg stderr into errors in PowerShell 5.1
$env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' + [Environment]::GetEnvironmentVariable('Path', 'User')
$proj = Split-Path $PSScriptRoot -Parent
Set-Location $proj
$sync = Join-Path $Drive 'FFIQ_sync'
$jobs = Join-Path $sync "jobs\$Machine"
$edge = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
$port = if ($Machine -eq 'pc') { 3927 } else { 3947 }
$py = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $py) { $py = "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" }
foreach ($d in 'todo', 'doing', 'done', 'failed') { New-Item -ItemType Directory -Force (Join-Path $jobs $d) | Out-Null }
New-Item -ItemType Directory -Force (Join-Path $sync 'checks'), out | Out-Null

function Say($m) { "{0}  {1}" -f (Get-Date -Format 'dd-MM HH:mm'), $m }

if ($Machine -eq 'laptop') {
    Say 'git pull'
    git pull --ff-only
    if ($LASTEXITCODE) { throw 'git pull failed: do not edit files on the laptop' }
    $ready = Join-Path $sync 'READY.txt'
    if (-not (Test-Path $ready)) { throw 'PC has not published yet (no FFIQ_sync\READY.txt)' }
    $want = (Select-String -Path $ready -Pattern '^commit=(\w+)').Matches[0].Groups[1].Value
    $have = (git rev-parse HEAD).Trim()
    if ($want -ne $have) { throw "PC published commit $want but this laptop is on $have. Wait for Drive / git, then run again." }
    $wantFiles = [int](Select-String -Path $ready -Pattern '^files=(\d+)').Matches[0].Groups[1].Value
    $wantBytes = [long](Select-String -Path $ready -Pattern '^bytes=(\d+)').Matches[0].Groups[1].Value
    $onDrive = Get-ChildItem (Join-Path $sync 'audio') -Recurse -File
    $driveBytes = ($onDrive | Measure-Object Length -Sum).Sum
    if ($onDrive.Count -ne $wantFiles -or $driveBytes -ne $wantBytes) {
        throw "Drive still downloading the audio ($($onDrive.Count) of $wantFiles files). Wait a few minutes, then run again."
    }
    Say 'copying audio from Drive'
    robocopy (Join-Path $sync 'audio') public\audio /MIR /NJH /NJS /NP /NFL /NDL /R:3 /W:10 | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "audio copy failed (robocopy $LASTEXITCODE)" }
}

# keep the machine awake while rendering (ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
Add-Type -Namespace W -Name P -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint f);'
[W.P]::SetThreadExecutionState([uint32]2147483649) | Out-Null

$bundled = $false
try {
    while ($true) {
        # jobs interrupted last time first, then new ones (oldest first)
        $job = Get-ChildItem (Join-Path $jobs 'doing') -Filter *.job | Select-Object -First 1
        if (-not $job) {
            $next = Get-ChildItem (Join-Path $jobs 'todo') -Filter *.job | Sort-Object LastWriteTime | Select-Object -First 1
            if (-not $next) { break }
            Move-Item $next.FullName (Join-Path $jobs 'doing')
            $job = Get-Item (Join-Path $jobs "doing\$($next.Name)")
        }
        $lang, $id, $comp = (Get-Content $job.FullName -TotalCount 1).Trim() -split '\s+'
        $log = Join-Path $jobs "doing\$comp.log"
        $t0 = Get-Date
        Say "START $comp ($lang)" | Tee-Object -FilePath $log
        if (-not $bundled) {
            npx remotion bundle --out-dir=out/bundle_$Machine --log=error 2>&1 | Tee-Object -FilePath $log -Append
            $bundled = $true
        }
        New-Item -ItemType Directory -Force "out\$lang" | Out-Null
        $raw, $mp4, $srt = "out\$lang\${comp}_raw.mp4", "out\$lang\$comp.mp4", "out\$lang\$comp.srt"
        Remove-Item $raw, $mp4 -ErrorAction SilentlyContinue
        npx remotion render out/bundle_$Machine $comp $raw --video-bitrate=8M --concurrency=$Concurrency --port=$port --log=error "--browser-executable=$edge" 2>&1 | Tee-Object -FilePath $log -Append
        $ok = Test-Path $raw
        if ($ok) {
            ffmpeg -v error -y -i $raw -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k $mp4 2>&1 | Tee-Object -FilePath $log -Append
            node --disable-warning=MODULE_TYPELESS_PACKAGE_JSON scripts/srt.ts $id 2>&1 | Tee-Object -FilePath $log -Append
            Copy-Item "out\$comp.srt" $srt -Force
            & $py tools/validate_video.py $id $mp4 $srt 2>&1 | Tee-Object -FilePath $log -Append
            $ok = ($LASTEXITCODE -eq 0)
            Copy-Item "out\check\${comp}_sheet.jpg" (Join-Path $sync 'checks') -Force -ErrorAction SilentlyContinue
        }
        if ($ok) {
            foreach ($dest in "final\$lang", (Join-Path $Drive "FFIQ_indic\final\$lang")) {
                New-Item -ItemType Directory -Force $dest | Out-Null
                Copy-Item $mp4, $srt $dest -Force
            }
            Remove-Item $raw -ErrorAction SilentlyContinue
            $to = 'done'
        } else { $to = 'failed' }
        Say ("{0} {1}  ({2:N0} min)" -f $to.ToUpper(), $comp, ((Get-Date) - $t0).TotalMinutes) | Tee-Object -FilePath $log -Append
        Move-Item $job.FullName, $log (Join-Path $jobs $to) -Force
    }
    Say "no jobs left for $Machine"
} finally {
    [W.P]::SetThreadExecutionState([uint32]2147483648) | Out-Null
}
