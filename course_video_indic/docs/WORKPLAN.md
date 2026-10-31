# Work plan: 11 languages, 2 machines, every video made once

English is the source and is **locked** (no script changes while languages are made).
Target languages: Hindi, Marathi, Telugu, Tamil, Kannada, Bengali, Malayalam,
Spanish (Latin America), French, German, Arabic (Modern Standard).
Rule from the user: **each video is made once.** All checking happens before rendering,
and every rendered video is checked again before it reaches `final/`. Slower is fine.

## Voices (female only)
| Language | Voice | | Language | Voice |
|---|---|---|---|---|
| Hindi | hi-IN-SwaraNeural | | Malayalam | ml-IN-SobhanaNeural |
| Marathi | mr-IN-AarohiNeural | | Spanish | es-MX-DaliaNeural |
| Telugu | te-IN-ShrutiNeural | | French | fr-FR-DeniseNeural |
| Tamil | ta-IN-PallaviNeural | | German | de-DE-KatjaNeural |
| Kannada | kn-IN-SapnaNeural | | Arabic | ar-SA-ZariyahNeural |
| Bengali | bn-IN-TanishaaNeural | | | |

## Order
1. Hindi (13 of 26 scripts exist) · 2. Marathi · 3–7. Telugu, Tamil, Kannada, Bengali,
Malayalam · 8–10. Spanish, French, German (Latin-script lint mode needed once) ·
11. Arabic last (right-to-left layout: mirrored pages, RTL captions, Arabic font).

## Four gates per language
1. **Script check** (before any voice): every page/quiz/outro translated, every number
   identical to English, no English left in the voice text, text fits the boxes
   (`npm run check`), and an English back-translation read against the source.
2. **Voice check** (before any render): female voice, every clip's pace, loudness and
   ending (no cut-off), captions synced to real pauses.
3. **Pilot**: render ONE lesson; the user (or a native speaker for es/fr/de/ar) watches it.
   Nothing else in that language is rendered until the user says OK.
4. **Video check** (every video): `tools/validate_video.py` checks length vs the planned
   timeline, −14 LUFS, true peak, silent gaps, captions; it saves one frame per page as a
   contact sheet (`out/check/<Comp>_sheet.jpg`, copied to Drive `FFIQ_sync/checks/`),
   which is looked at before the video is accepted. Only PASS videos go to `final/`.

## Two machines
**The PC is the boss. The laptop only renders.**

| | PC | Laptop |
|---|---|---|
| Edit scripts, translate, voices | yes | **never** |
| git commit / push | yes | **never** (only `git pull`) |
| Render | its job list | its job list, when it is on |

What moves where:
- **Code and scripts: git** (small text files only; audio and videos are never committed).
- **Audio: Drive** `G:\My Drive\FFIQ_sync\audio\` (copied by `tools\pc_publish.ps1`).
- **Jobs: Drive** `FFIQ_sync\jobs\<pc|laptop>\{todo,doing,done,failed}\<Comp>.job`.
- **Finished videos**: `final/<language>/` and Drive `FFIQ_indic\final\<language>\`.

Each machine only ever takes jobs from its own folder, so the same video is never
rendered twice. If the laptop is switched off mid-video, that job stays in `doing\`
and is rendered again from the start next time (no half videos reach `final`).

### PC routine (after a language passes gates 1–3)
```powershell
git add <text files> ; git commit ; git push        # scripts + caption/timing data
powershell -ExecutionPolicy Bypass -File tools\pc_publish.ps1    # audio -> Drive, writes READY.txt
tools\jobs.ps1 add -To laptop -Lang hindi -Comps GembaHi,HanchoHi
tools\jobs.ps1 add -To pc     -Lang hindi -Comps OnePointLessonHi
powershell -ExecutionPolicy Bypass -File tools\worker.ps1 -Machine pc -Concurrency 1
tools\jobs.ps1 list
```
`take-back` moves the laptop's unstarted jobs to the PC (laptop off for days);
`retry -To pc` puts failed jobs back after the cause is fixed.

### Laptop routine (whenever it is on)
```powershell
powershell -ExecutionPolicy Bypass -File tools\worker.ps1 -Machine laptop
```
It pulls git, checks the PC published that exact commit and that Drive has all the audio,
copies the audio, then renders its jobs one at a time and checks each one.

### Limits
- PC 16 GB: at most 2 renders at once (1 if the other chats render too).
- Laptop: 1 render at a time (`-Concurrency 2` inside that render is fine with 16 GB).
- Lid closed = sleep; keep the laptop open and on power.

## Laptop one-time setup
1. Google Drive for desktop, same account; make `FFIQ_sync` and `FFIQ_indic\final`
   available offline.
2. Git, Node 26, Python 3.11 (`pip install` nothing extra), ffmpeg full build on PATH.
3. `git clone --depth 1 --branch add-course-video https://github.com/PrashantRMarathe/voice-replacer.git`
   (`--depth 1` skips the old audio in history: a small download instead of ~1.3 GB).
4. `cd course_video_indic` then `npm ci` (if antivirus blocks esbuild, allow-list the folder).
5. Test: PC adds one job for the laptop; the laptop runs the worker; compare its contact
   sheet with the PC's for the same lesson.

## Time (estimate)
About 4–5 days per language (translate + gates + 26 renders), ~25–30 renders a day
with both machines. All 11 languages: roughly 5–7 weeks; the main risk is waiting for
pilot reviews.
