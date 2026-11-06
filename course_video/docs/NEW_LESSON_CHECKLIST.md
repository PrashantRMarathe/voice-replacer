# ✅ New Lesson Checklist

Quick checklist for one new page lesson. Full detail in `PLAYBOOK.md` §4.

- [ ] `narration/<name>.py`: copy `zero_defects.py`; set `ID`/`NAME`; write
      intro/outro, `PAGES` (title, 2–4 `points` as (text, cue), example +
      `example_cue`, spoken script): every box is spoken (PLAYBOOK §4c)
- [ ] 2 `QUIZZES` (`after` = page key): one mid-lesson, one on the last page,
      each with `q_script` + `a_script`
- [ ] `python narration/<name>.py`: bootstrap voice + timings/content/quizzes/words
- [ ] `src/lessons/<id>/<Name>.tsx`: copy `ZeroDefects.tsx`; set paths, id, titles
- [ ] Register `<Name>` + `<Name>Dub` (`captions: false`) in `src/Root.tsx`
- [ ] Add `<id>: "<Name>"` to `scripts/lessons.ts`
- [ ] Scripts follow the style guide (PLAYBOOK §4b): hook intro, one story thread,
      short sentences, talk to the learner; script lint shows `OK`
- [ ] Content review (PLAYBOOK §4b rules 13–17): numbers agree across pages and
      with the screen, the story obeys the lesson's own rules, technical claims
      checked, no reference to a later lesson, outro names the next letter, no
      case or numbers copied from another lesson
- [ ] `npm run check` passes
- [ ] Preview still: `npx remotion still <Name> out/x.png --frame=N`
- [ ] Unclear pronunciations looked up (or asked) and put in `say()`
- [ ] Copy `out/<NAME>.json` to `G:/My Drive/FFIQ_voice/input/` (content stays off GitHub)
- [ ] Ask the user to **Run all** in `colab_clone_drive.ipynb` (docs/AUTOMATION.md)
- [ ] Watcher running (`python narration/watch_drive.py`): it gates (F5, voice A,
      brightness, pace), imports, checks, renders → `FFIQ_voice/final/<Name>.mp4`
- [ ] `status.txt` shows ✅ DONE (⚠️ HELD → read `_HELD.json`, see docs/VOICE.md)
- [ ] Watch a page start + a two-line sentence: captions change with the voice
- [ ] `<Name>Dub` rendered too, if the user needs a no-caption master
- [ ] Audio: normal version has the polish layer (music bed + soft sounds, −14 LUFS);
      `...Dub` is voice-only. Brand mark, calm background, tasteful characters

## Fixing a finished lesson (only some sentences change)
1. Edit `narration/<name>.py`; `python narration/lint_scripts.py <name>` shows `OK`.
2. Write a clone file with **only the changed clips** (`{key: say(text)}`) as
   `input/<NAME>.json`; the user clicks Run all. Unchanged clips keep their mp3.
3. `python narration/import_clones.py <NAME> <clones_dir>` (partial batch is fine),
   `npm run check`, then `bash scripts/render_lesson.sh --no-dub <Comp>` and copy
   the `.mp4` + `.srt` to `final/`. On-screen-only edits need no clone: run
   `import_clones.py <NAME> --realign` and re-render.

---

## Starter prompt for a new chat
Paste this into a fresh session to continue the course:

> I'm continuing the "Factory Flow IQ" Lean Manufacturing animated course in the
> `course_video/` Remotion project. Read `course_video/CLAUDE.md` and
> `course_video/docs/PLAYBOOK.md` first, then follow them exactly.
> Make a new lesson: **<LESSON NAME>** (content below), as a page lesson like
> Zero Defects: same style, characters, FFIQ brand, one-line sentence captions,
> **the polish layer on the normal version (Dub stays voice-only)**, and **2 narrated quizzes**. Build the
> normal and `...Dub` compositions, run `npm run check`, render a preview still
> for me, then queue the clone script in my Drive input folder
> (`docs/AUTOMATION.md`) so I only click Run all in Colab; the voice must follow
> `docs/VOICE.md`. Keep my content off GitHub. Don't install react-peeps. Keep
> characters tasteful.
