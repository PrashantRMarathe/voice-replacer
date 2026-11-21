# Languages plan — all course languages (6 Nov 2026)

## Goal
Every lesson (26, A to Z) in every language, as **one English video + one voice track and
subtitle file per language**. The viewer picks the language in the player. Screen text stays English.

## Decisions (made with the user, 6 Nov 2026)
- **Voices:** English = the cloned course voice (F5). **Every other language = a Microsoft
  female voice** (no cloning: Chatterbox, ElevenLabs and IndicF5 were considered and dropped).
- **Spanish = Latin American** (Mexico). **Arabic = Modern Standard Arabic** (understood in every
  Arabic-speaking country), Egyptian voice.
- Speed-up to fit the English timing: up to about 14% is fine. If a clip needs more,
  **shorten the translation** instead of speeding the voice up further.

## Languages and voices

### Phase A — now (12 languages)
| # | Language | Voice | Status |
|---|---|---|---|
| 1 | English | cloned course voice (F5) | clips on the PC; track not packed yet |
| 2 | Hindi | hi-IN-SwaraNeural | ✅ 26/26 |
| 3 | Telugu | te-IN-ShrutiNeural | ✅ 26/26 |
| 4 | Tamil | ta-IN-PallaviNeural | ✅ 26/26 |
| 5 | Marathi | mr-IN-AarohiNeural | 2/26 scripts (running on the PC) |
| 6 | Bengali | bn-IN-TanishaaNeural | not started |
| 7 | Kannada | kn-IN-SapnaNeural | not started |
| 8 | Malayalam | ml-IN-SobhanaNeural | not started |
| 9 | French | fr-FR-DeniseNeural | not started |
| 10 | German | de-DE-KatjaNeural | not started |
| 11 | Spanish (Latin America) | es-MX-DaliaNeural | not started |
| 12 | Arabic (Standard) | ar-EG-SalmaNeural | not started |

### Phase B — later (14 languages, for global manufacturing)
| Language | Voice | Language | Voice |
|---|---|---|---|
| Chinese (Simplified) | zh-CN-XiaoxiaoNeural | Chinese (Traditional) | zh-TW-HsiaoChenNeural |
| Japanese | ja-JP-NanamiNeural | Turkish | tr-TR-EmelNeural |
| Korean | ko-KR-SunHiNeural | Vietnamese | vi-VN-HoaiMyNeural |
| Italian | it-IT-ElsaNeural | Thai | th-TH-PremwadeeNeural |
| Portuguese (Brazil) | pt-BR-FranciscaNeural | Polish | pl-PL-ZofiaNeural |
| Russian | ru-RU-SvetlanaNeural | Malay | ms-MY-YasminNeural |
| Indonesian | id-ID-GadisNeural | Czech | cs-CZ-VlastaNeural |

All 26 voices were checked to exist in the Microsoft voice list (6 Nov 2026).

## How one language is made (per lesson)
1. **Translate** the narration, clip by clip.
   - Indian languages: from the Hindi script (keeps the same local wording).
   - All other languages: from the English script.
   - Each clip has a length limit taken from the English clip.
   - Lean terms (Kaizen, Poka Yoke, TAKT, ...) use the pronunciation list for that language.
   - Before voicing a new language: `python tools/say_words.py all_<lang>` makes a sample of every
     lean term in a sentence; the Whisper check (below) finds bad ones, fixed in `narration/pronounce.py`.
2. **Voice** each clip with the Microsoft voice and save the timing of each word (for subtitles).
3. **Check:** flag any clip that needs more than a 14% speed-up and shorten its text. Flag
   English words left in the voice text and numbers that don't match the English.
4. **Fit and mix** onto the English video's music and effects (`tools/fit_dub.py`): -14 LUFS
   `.m4a` track plus an `.srt` subtitle file.
5. **Pack and upload** to `final/dub/` and Drive `FFIQ_indic/final/dub/`.

No video rendering is needed: the English dub videos already exist for all 26 lessons.

## What to build first (one-time)
- **`tools/dub_lang.py`** — an audio-only path that works for any language: script
  (clip → text) → Microsoft voice + word timings → hands off to `fit_dub.py`.
  No lesson pages, fonts or screen labels needed per language.
- **Language table** in one place (code, voice, 3-letter track code, right-to-left flag for Arabic).
- **Length check** per clip (translation vs English time budget).
- `fit_dub.py`: accept any language code, not only hi/te/ta/mr.

## Order of work
| Step | What | Done when |
|---|---|---|
| 0 | PC pushes its latest work to git; laptop pulls | both machines have the same `final/dub` state |
| 1 | Build `dub_lang.py` + the 6 automatic checks + a glossary per language | it reproduces an existing Hindi track; checks run on it |
| 2 | **Test:** Zero Defects in Bengali, Kannada, Malayalam, French, German, Spanish, Arabic | all 10 checks pass (the user tests nothing) |
| 3 | Finish Marathi (24 lessons) | 26/26 Marathi tracks |
| 4 | English track added on the PC | English selectable in every video |
| 5 | Bengali, Kannada, Malayalam — 26 lessons each | 26/26 each |
| 6 | French, Spanish, German, Arabic — 26 lessons each | 26/26 each |
| 7 | Final pack: every lesson with all 12 tracks + subtitles, upload to Drive | all checks pass; user OKs replacing the Drive files once (no listening) |
| 8 | Phase B languages (later), same steps 2, 5, 7 | — |

## Local feel: Option A chosen (6 Nov 2026)
- **Now (A):** voice and subtitles fully local; screen text, names (Priya, ...) and money stay
  as in the English video.
- **Later, maybe (B):** for the biggest markets, a separate video per language with translated
  screen text, local names (e.g. Sophie, Lena, Sofía, Fatima) and local money (~320 MB each).

## Delivery format
- **Phase A (12 languages):** one mp4 per lesson with all tracks (~320 MB video + ~15 MB per language).
- **Phase B (26 languages):** one mp4 would be ~700 MB, too big. Switch to one English video plus
  separate voice/subtitle files per language, loaded by the website or player.

## Respect every language and its people (user's rule, 6 Nov 2026)
The goal is not a word-for-word translation. Each version must sound like it was **written by a
good local trainer for local factory people**, so viewers feel the course was made for them.

**One style sheet per language** (`narration/style_<lang>.md`), written before lesson 1:
- **Polite form:** the respectful "you" people expect in training: vous (fr), Sie (de),
  usted (es, Latin America), آپ (hi), तुम्ही (mr), আপনি (bn), ನೀವು (kn), നിങ്ങൾ (ml),
  நீங்கள் (ta), మీరు (te). Arabic: Modern Standard Arabic, simple and clear, addressing all
  workers respectfully (avoid wording that excludes women where a neutral form exists).
- **The words factory people really use:** where a country's shop floors use the English or
  Japanese term (Kaizen, Gemba, Poka Yoke, OEE, line, KPI), keep it; where they use a local
  word, use that. Never force a dictionary word nobody says on the floor.
- **Natural speech, not book language:** short spoken sentences; the hook questions and jokes
  are rewritten as a local speaker would say them (e.g. "Sound familiar?" becomes the local
  everyday phrase, not a literal one).
- **Local formats:** number, decimal and date styles of that country (1.000,5 in de/es,
  1 000,5 in fr); currency stays as in the English lesson unless the lesson is about cost
  in general. Arabic: Western digits, matching the numbers on screen.
- **Correct writing:** proper script, accents and punctuation (French space before ? ! : ;
  Spanish ¿ ¡; Arabic ، ؟; Indian dandas where used).
- **Cultural care:** no idioms, gestures, food, religion or humour that could confuse or
  offend; nothing that singles out a nationality, caste, religion or gender. Names on screen
  (Priya, ...) stay, because the visuals show them.

**Native-reader review (in addition to the automatic checks):** after translation, a separate
reviewer pass (a fresh agent told to read as an experienced factory trainer from that country)
reads every clip and marks anything stiff, unnatural, too formal, unclear or disrespectful.
Every mark is fixed before voicing.

## Quality checks before anything is called done
**The user does not speak these languages (6 Nov 2026), so Claude owns their quality.** No step
waits for a native speaker. Every check below is automatic and must pass:

1. **Term glossary per language** (`narration/glossary_<lang>.json`), written once before lesson 1:
   the standard industry term for each lean word in that language (e.g. Kaizen stays "Kaizen" in
   every language; Zero Defects = "Zéro défaut", "Null-Fehler", "Cero Defectos", "صفر عيوب").
   Every lesson must use the glossary term; a check flags any other wording.
2. **Back-translation:** each translated clip is translated back to English separately and
   compared with the English script. Any clip whose meaning drifted is rewritten.
3. **Numbers and names:** every number, unit, %, and name (Priya, ...) matches the English.
4. **Length:** each clip fits its English time budget (speed-up ≤ 14%), otherwise shortened.
5. **Speech-recognition check (Whisper):** every voiced clip is transcribed and compared with its
   script. A missing, extra or wrongly spoken word fails the clip; the text is respelled in
   `pronounce.py` (or reworded) and re-voiced until it passes. `faster-whisper` is installed on the
   laptop (CPU: model `small` for every clip, `medium` for clips that fail). Also run on the
   `say_words.py` term sample before lesson 1, so the voice says every lean term correctly.
6. **Subtitle check:** every subtitle line shows at the right time and in the right direction
   (right-to-left for Arabic), no line too long.

**The user tests nothing (6 Nov 2026).** Claude also checks what a listener would notice:
7. **Sound:** every track measured at -14 LUFS (true peak ≤ -1.5 dB), no clipping, no silent gaps
   or overlapping clips, music under the voice at the same level as the English video.
8. **Pace:** no clip sped up past 14%; words per minute close to normal speech for that language.
9. **Timing:** each clip starts with its English clip, so the highlights still match the voice;
   the packed mp4 passes `tools/validate_video.py` and every track/subtitle opens in a player.
10. **Final listen:** Claude transcribes the final mixed track (not just the clips) and checks it
   reads as the full script, in order.

## Risks and notes
- **Two machines:** the PC and the laptop must not both pack `final/dub` at the same time.
- **Replacing Drive files:** ask the user before the first overwrite.
- **Screen text stays English.** Buyers in China, Japan or Korea may later want translated screen text.
- **Arabic:** subtitles are right-to-left; check they show correctly in the player.
- **Long languages** (French, German, Spanish, Marathi) run 15–30% longer than English, so
  plan on shortening many clips.
