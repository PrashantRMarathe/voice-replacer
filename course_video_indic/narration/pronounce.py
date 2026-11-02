"""Voice-only respellings, one list per language, shared by every lesson.

The screen and captions keep the correct spelling; only the text sent to the voice
changes. Add a word here when the user hears it said wrong, then re-voice the clips
that contain it (tools/revoice.py). tools/say_words.py makes the listening sample.
"""
import re
import unicodedata

PRON = {
    "hi": {
        # Swara says the nukta form oddly; the user picked the plain form (31 Oct 2026)
        "ज़रूरी": "जरूरी",
        # the user picked sample 4 of each (31 Oct 2026)
        "जाना-पहचान": "जाना पेहचान",
        "पहचान": "पेहचान",
        # the one word the user wanted in English letters, so Swara says it the English way
        "विज़ुअल": "visual",
    },
}
# English terms stay in each lesson's SPOKEN (native-script forms): the user compared
# English-letter forms (S-O-P, A-three) in Swara's voice and found the old way better.

# words the voice may read in English letters (lint flags any other English left in)
LATIN_OK = {"hi": {"visual"}}


def fix(text: str, lang: str) -> str:
    for word, spoken in PRON.get(lang, {}).items():
        # NFC keeps the scripts' nukta as two code points (ज + ़) whichever way it was typed here
        word, spoken = unicodedata.normalize("NFC", word), unicodedata.normalize("NFC", spoken)
        text = re.sub(rf"(?<!\w){re.escape(word)}", spoken, text)
    return text
