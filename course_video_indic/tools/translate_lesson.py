"""Make a Tamil/Telugu lesson from its Hindi one, so pages, visuals, icons and numbers stay identical.
Only the Hindi text is replaced; everything else is copied.

  python tools/translate_lesson.py dump  kaizen_hi            numbered Hindi strings -> stdout
  python tools/translate_lesson.py build kaizen_hi ta file    file has "<n>|<translation>" lines

build stops without writing if a line is missing or a string's digits or English terms differ
from the Hindi. It writes narration/<lesson>_<lang>.py and the component, and registers the
lesson in tools/gen_root.py (run that next, then lint, then tools/build_hindi.sh to voice it).
"""
import ast
import importlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "narration"))
sys.path.insert(0, str(ROOT / "tools"))
from lesson_terms import TERMS  # noqa: E402

LANGS = {"ta": ("Tamil", "ta-IN-PallaviNeural"), "te": ("Telugu", "te-IN-ShrutiNeural")}
DEVA = re.compile("[ऀ-ॿ]")
TS_STR = re.compile(r'"((?:[^"\\\n]|\\.)*)"')
DIGITS = re.compile(r"\d+(?:[.,]\d+)*")
LATIN = re.compile(r"\d*[A-Za-z][A-Za-z0-9]*")
FSTRING_WORDS = {"स्टेशन": {"ta": "ஸ்டேஷன்", "te": "స్టేషన్"}}  # Hindi inside f"..." strings (Yamazumi)


def line_starts(src):
    starts, n = [0], 0
    for line in src.split("\n"):
        n += len(line.encode("utf-8")) + 1
        starts.append(n)
    return starts


def py_strings(src):
    """(start, end, value) in bytes for every Hindi string in the module, in source order."""
    tree, starts, out = ast.parse(src), line_starts(src), []
    doc = ast.get_docstring(tree, clean=False)
    spoken = next(n for n in tree.body if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "SPOKEN")
    skip = {id(n) for n in ast.walk(spoken)}
    for node in ast.walk(tree):
        if isinstance(node, ast.JoinedStr):  # words inside f-strings come from FSTRING_WORDS
            skip |= {id(n) for n in ast.walk(node)}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and DEVA.search(node.value):
            if id(node) not in skip and node.value != doc:
                out.append((starts[node.lineno - 1] + node.col_offset,
                            starts[node.end_lineno - 1] + node.end_col_offset, node.value))
    return sorted(out)


def sources(mod_name):
    src = (ROOT / "narration" / f"{mod_name}.py").read_text(encoding="utf-8")
    lid = re.search(r'^ID = "(\w+)_hi"', src, re.M).group(1)
    tsx = next((ROOT / "src/lessons" / f"{lid}_hi").glob("*Hi.tsx"))
    return src, lid, tsx


def hindi_strings(mod_name):
    src, _, tsx = sources(mod_name)
    ts = [m.group(1) for m in TS_STR.finditer(tsx.read_text(encoding="utf-8")) if DEVA.search(m.group(1))]
    return [v for _, _, v in py_strings(src)] + ts


def wrap(text, indent):
    """A long string becomes implicit concatenation over several lines, like the Hindi modules."""
    if len(text) <= 88:
        return json.dumps(text, ensure_ascii=False)
    parts, cur = [], ""
    for w in text.split(" "):
        if cur and len(cur) + len(w) > 88:
            parts.append(cur)
            cur = ""
        cur += w + " "
    parts.append(cur[:-1])
    return ("\n" + " " * indent).join(json.dumps(p, ensure_ascii=False) for p in parts)


def check(hi, tr, n):
    errs = []
    if Counter(DIGITS.findall(hi)) != Counter(DIGITS.findall(tr)):
        errs.append(f"{n}: digits differ: {DIGITS.findall(hi)} vs {DIGITS.findall(tr)}")
    if Counter(LATIN.findall(hi)) != Counter(LATIN.findall(tr)):
        errs.append(f"{n}: English differs: {LATIN.findall(hi)} vs {LATIN.findall(tr)}")
    if DEVA.search(tr):
        errs.append(f"{n}: Hindi left in the translation")
    return errs


def build(mod_name, lang, file):
    src, lid, tsx = sources(mod_name)
    name, voice = LANGS[lang]
    hi = hindi_strings(mod_name)
    lines = {}
    for line in Path(file).read_text(encoding="utf-8-sig").splitlines():
        if line.strip():
            k, _, v = line.partition("|")
            lines[int(k)] = v.rstrip()  # a leading space is meaningful (a suffix after a number)
    errs = [f"line {i} missing" for i in range(1, len(hi) + 1) if i not in lines]
    errs += [f"extra line {k}" for k in lines if not 1 <= k <= len(hi)]
    if not errs:
        for i, h in enumerate(hi, 1):
            errs += check(h, lines[i], i)
    if errs:
        sys.exit("NOT written:\n  " + "\n  ".join(errs))

    # module: replace each Hindi string in place, last first so the offsets stay valid
    b = src.encode("utf-8")
    strs = py_strings(src)
    for i, (s, e, _) in reversed(list(enumerate(strs, 1))):
        col = s - b.rfind(b"\n", 0, s) - 1
        b = b[:s] + wrap(lines[i], col).encode("utf-8") + b[e:]
    out = b.decode("utf-8")
    mod = importlib.import_module(mod_name)
    new_mod = f"{mod_name[:-3]}_{lang}"
    for en, hindi in mod.SPOKEN.items():
        if en not in TERMS[lang]:
            sys.exit(f"NOT written: add {en!r} to tools/lesson_terms.py")
        out = re.sub(rf'("{re.escape(en)}":\s*)"{re.escape(hindi)}"',
                     lambda m: m.group(1) + json.dumps(TERMS[lang][en], ensure_ascii=False), out)
    header = (f'"""{mod_name[:-3]} in {name}, made from the Hindi lesson with tools/translate_lesson.py:\n'
              f'same pages, visuals and numbers. Voice: Microsoft {name} neural female voice ({voice}).\n\n'
              f'  bash tools/build_hindi.sh {new_mod} --force     voice + level + sync\n"""')
    out = re.sub(r'\A""".*?"""', lambda _: header, out, count=1, flags=re.S)
    out = out.replace(f'ID = "{lid}_hi"', f'ID = "{lid}_{lang}"').replace(f'NAME = "{mod_name}"', f'NAME = "{new_mod}"')
    out = out.replace('LANG = "hi"', f'LANG = "{lang}"')
    for hindi, forms in FSTRING_WORDS.items():
        out = out.replace(hindi, forms[lang])
    out = re.sub(r"^VOICE = .*$", f'VOICE = "{voice}"   # female (user, 2 Nov 2026)', out, flags=re.M)
    out = out.replace(r'rf"\b{re.escape(en)}\b"', 'rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])"')
    out = out.replace("Devanagari", f"{name} script").replace("Hindi", name).replace(f"from the {name} lesson", "from the Hindi lesson")
    m = DEVA.search(out)
    if m:
        sys.exit("NOT written: Hindi left in the module near: " + out[max(0, m.start() - 60):m.start() + 60])

    # component: same order as the dump, after the module's strings
    t = tsx.read_text(encoding="utf-8")
    counter = iter(range(len(strs) + 1, len(hi) + 1))
    t = TS_STR.sub(lambda m: json.dumps(lines[next(counter)], ensure_ascii=False) if DEVA.search(m.group(1)) else m.group(0), t)
    comp = tsx.stem[:-2] + lang.capitalize()
    t = t.replace(tsx.stem, comp).replace(f"{lid}_hi", f"{lid}_{lang}").replace(mod_name, new_mod)
    t = t.replace('"hi"', f'"{lang}"').replace("_HI_DURATION", f"_{lang.upper()}_DURATION").replace("Hindi", name)
    t = re.sub(r"^// \w+ version of", f"// {name} version of", t, flags=re.M)
    if DEVA.search(t):
        sys.exit("NOT written: Hindi left in the component")
    dur = re.search(r"export const (\w+_DURATION)", t).group(1)

    (ROOT / "narration" / f"{new_mod}.py").write_text(out, encoding="utf-8")
    folder = ROOT / "src/lessons" / f"{lid}_{lang}"
    folder.mkdir(exist_ok=True)
    (folder / f"{comp}.tsx").write_text(t, encoding="utf-8")
    g = ROOT / "tools/gen_root.py"
    s = g.read_text(encoding="utf-8")
    entry = f'    ("{lid}_{lang}", "{comp}", "{dur}"),\n'
    if entry not in s:
        g.write_text(s.replace("]\n# A lesson joins Root", entry + "]\n# A lesson joins Root", 1), encoding="utf-8")
    print(f"wrote {new_mod}.py and {comp}.tsx")


if __name__ == "__main__":
    if sys.argv[1] == "dump":
        for i, h in enumerate(hindi_strings(sys.argv[2]), 1):
            print(f"{i}|{h}")
    else:
        build(sys.argv[2], sys.argv[3], sys.argv[4])
