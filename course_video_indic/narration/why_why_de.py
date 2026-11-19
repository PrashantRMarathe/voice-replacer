"""why_why in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh why_why_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ww_de"
NAME = "why_why_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "X-Matrix": "Ix-Matrix",
    "Why-Why": "Wai Wai",
    "Pareto": "Pareto",
    "Gemba": "Gemba",
    "5W2H": "fünf we zwei ha",
    "FMEA": "eff emm e a",
    "HDMI": "ha de emm i",
    "SOP": "ess o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Einundzwanzig Handys fielen im Endtest beim Laden durch. Die erste Antwort kam schnell. "
    "Bedienfehler. Zwei Tage später passierte es wieder. Kommt Ihnen das bekannt vor? In "
    "dieser Lektion lernen Sie die Why-Why-Analyse kennen, oft fünf Warum genannt. Sie sehen, "
    "wie Sie an der bequemen Antwort vorbei zu einer Ursache graben, die Sie beweisen und "
    "steuern können. Wir begleiten Neha, Qualitätsingenieurin an einer Handylinie."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Beginnen Sie mit einem scharfen Problem, und schützen Sie "
    "zuerst Ihren Kunden. Stützen Sie jedes Warum mit Belegen, und testen Sie es, bevor Sie "
    "es Grundursache nennen. Und beheben Sie beides, wie es entstand und warum es "
    "durchrutschte. Ihre Aufgabe für diese Woche. Nehmen Sie einen Wiederholfehler, und "
    "schreiben Sie seine 5W2H-Beschreibung. Gut gemacht, Lektion abgeschlossen. Als Nächstes "
    "lernen Sie die X-Matrix kennen, die Strategie mit Handeln verbindet."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Why-Why ist",
        "points": [("Immer wieder warum fragen, mit Fakten", "Die Why-Why-Analyse heißt"),
                   ("Fünf ist keine Regel", "aber fünf ist keine Regel"),
                   ("Bei einer beweisbaren, steuerbaren Ursache aufhören", "Sie hören auf")],
        "example": "Ladefehler ist das Symptom: Steckersitz, Platinenschaden, Vorrichtungskontakt oder "
                   "Testereinstellung könnten es verursachen.",
        "example_cue": "An Nehas Linie",
        "script": "Hier ist die Kernidee. Die Why-Why-Analyse heißt, immer wieder zu fragen, warum ein "
                  "Problem geschah, mit Fakten hinter jeder Antwort. Man nennt sie oft fünf Warum, aber "
                  "fünf ist keine Regel. Sie hören auf, wenn Sie eine Ursache erreichen, die Sie beweisen "
                  "und steuern können. An Nehas Linie ist der Ladefehler das Symptom. Es könnte "
                  "Steckersitz, Platinenschaden, Vorrichtungskontakt oder Testereinstellung sein. Nichts "
                  "davon ist die Grundursache, bevor es getestet ist. Wie passt das zu anderen Werkzeugen?",
    },
    {
        "key": "p02", "num": 2, "title": "Why-Why und Ursachenanalyse",
        "points": [("Ein Werkzeug der Ursachenanalyse", "Why-Why ist ein Werkzeug"),
                   ("An den echten Ort, das echte Produkt sehen", "Gehen Sie an den echten Ort"),
                   ("Welcher Beleg stützt dieses Warum?", "fragen Sie, welcher Beleg"),
                   ("Menschliches Handeln ist ein Hinweis, nicht die Antwort", "Und sehen Sie menschliches Handeln")],
        "example": "Fehlende Schrauben an einer Audiolinie: „Werker vergaß\" reichte nicht. Das Team prüfte "
                   "Zuführung und Reihenfolge.",
        "example_cue": "Als an einer Audiolinie",
        "script": "Why-Why ist ein Werkzeug der Ursachenanalyse. Fischgräten, Pareto-Diagramme und Versuche "
                  "stehen daneben. Es wirkt am besten bei einer klaren Ursache-Wirkungs-Kette. Gehen Sie an "
                  "den echten Ort, und schauen Sie auf das echte Produkt. Bei jedem Schritt fragen Sie, "
                  "welcher Beleg dieses Warum stützt. Und sehen Sie menschliches Handeln als Hinweis, nicht "
                  "als letzte Antwort. Als an einer Audiolinie Schrauben fehlten, reichte Werker vergaß "
                  "nicht. Das Team prüfte Zuführung und Reihenfolge. Wo beginnen Sie?",
    },
    {
        "key": "p03", "num": 3, "title": "Schritt 1: mit 5W2H definieren",
        "points": [("Eine scharfe Problembeschreibung", "Beginnen Sie mit einer scharfen"),
                   ("5W2H: was, wo, wann, wie gefunden, wie viele", "Nutzen Sie 5W2H"),
                   ("Den letzten bekannten guten Zustand aufnehmen", "Nehmen Sie den letzten bekannten guten")],
        "example": "Linie 2: 21 von 700 Handys (3 %) fielen nach dem Vorrichtungswechsel um 11 Uhr beim "
                   "Laden durch; die Schicht davor lag unter 0,5 %.",
        "example_cue": "An Linie zwei fielen",
        "script": "Beginnen Sie mit einer scharfen Problembeschreibung. Ein vages Problem bekommt vage "
                  "Antworten. Nutzen Sie 5W2H. Was fiel aus, wo, wann, wie wurde es gefunden, und wie "
                  "viele. Nehmen Sie den letzten bekannten guten Zustand auf. Hier ist Nehas Beschreibung. "
                  "An Linie zwei fielen einundzwanzig von siebenhundert Handys beim Laden durch. Das sind "
                  "drei Prozent, direkt nach einem Vorrichtungswechsel um elf Uhr. Die Schicht davor lag "
                  "unter einem halben Prozent. Und die schon gebauten Handys?",
    },
    {
        "key": "p04", "num": 4, "title": "Schritt 2: zuerst eingrenzen",
        "points": [("Zuerst den Kunden schützen", "schützen Sie Ihren Kunden"),
                   ("Den letzten bekannten guten Punkt finden", "Finden Sie den letzten bekannten guten"),
                   ("Bestand physisch und im System sperren", "Sperren Sie diesen Bestand"),
                   ("Jede Einheit abgleichen", "Dann gleichen Sie jede Einheit ab")],
        "example": "100 % sortieren schützt den Kunden, beweist aber nicht, dass die Ursache weg ist.",
        "example_cue": "Hundert Prozent zu sortieren",
        "script": "Bevor Sie analysieren, schützen Sie Ihren Kunden. Eingrenzung begrenzt das Risiko, "
                  "während die Untersuchung läuft. Finden Sie den letzten bekannten guten Punkt, und jede "
                  "Seriennummer oder jedes Los seitdem. Sperren Sie diesen Bestand physisch, und auch im "
                  "System. Dann gleichen Sie jede Einheit ab. Geprüft, durchgefallen, nachgearbeitet, "
                  "freigegeben oder offen. Neha sperrte jedes Handy seit dem Vorrichtungswechsel. Aber "
                  "Vorsicht. Hundert Prozent zu sortieren schützt den Kunden. Es beweist nicht, dass die "
                  "Ursache weg ist.",
    },
    {
        "key": "p05", "num": 5, "title": "Schritt 3: Fakten am Gemba",
        "points": [("Defekte mit bekannt guten Einheiten vergleichen", "vergleichen Sie defekte Einheiten"),
                   ("Einstellungen, Vorrichtungen, Versionen, Lose prüfen", "Prüfen Sie Einstellungen"),
                   ("Belege sichern, bevor jemand nachstellt", "Sichern Sie die Belege"),
                   ("Gesehen · Quelle · könnte heißen", "Führen Sie drei Spalten")],
        "example": "Neha fotografierte und beschriftete jedes defekte Handy nach Seriennummer, dann holte "
                   "sie Tester- und Wartungsprotokolle.",
        "example_cue": "Neha fotografierte",
        "script": "Ihre Analyse ist nur so gut wie Ihre Belege. Gehen Sie zum Gemba, und vergleichen Sie "
                  "defekte Einheiten mit bekannt guten. Prüfen Sie Einstellungen, Vorrichtungen, "
                  "Kalibrierung, Softwareversionen und Lieferantenlose. Sichern Sie die Belege, bevor "
                  "jemand etwas nachstellt. Neha fotografierte und beschriftete jedes defekte Handy nach "
                  "Seriennummer. Dann holte sie die Testerprotokolle und die Wartungsberichte. Führen Sie "
                  "drei Spalten. Was Sie sahen, woher es kam, und was es heißen könnte. Nun können Sie "
                  "warum fragen.",
    },
    {
        "key": "p06", "num": 6, "title": "Schritt 4: die Kette bauen",
        "points": [("Beim beobachteten Ereignis beginnen", "Schreiben Sie das beobachtete Ereignis"),
                   ("Jeder Pfeil ist eine prüfbare Behauptung", "Jeder Pfeil ist eine Behauptung"),
                   ("Fakten, nicht „Nachlässigkeit\"", "Nutzen Sie konkrete Fakten"),
                   ("Verzweigen, wenn Ursachen zusammenwirken", "Verzweigen Sie die Kette")],
        "example": "Falsches Kartonetikett → alter Druckauftrag → Software ließ es zu → Drucker nicht mit "
                   "dem gescannten Produkt verknüpft.",
        "example_cue": "Ein falsches Kartonetikett",
        "script": "Schreiben Sie das beobachtete Ereignis oben hin. Fragen Sie, warum es geschah. Dann "
                  "fragen Sie, warum dieser Zustand bestand. Jeder Pfeil ist eine Behauptung, die Sie "
                  "prüfen können müssen. Fragen Sie, warum der Fehler geschah, nie, wer schuld ist. Nutzen "
                  "Sie konkrete Fakten, keine Etiketten wie Nachlässigkeit. Ein Beispiel aus der "
                  "Verpackung. Ein falsches Kartonetikett führte zu einem alten Druckauftrag zurück. Die "
                  "Software ließ es zu, weil der Drucker nicht mit dem gescannten Produkt verknüpft war. "
                  "Verzweigen Sie die Kette, wenn mehrere Ursachen beitrugen.",
    },
    {
        "key": "p07", "num": 7, "title": "Entstehung, Durchschlupf und System",
        "points": [("Entstehung: wie der Fehler gemacht wurde", "Die Entstehungsursache"),
                   ("Durchschlupf: warum ihn niemand fing", "Die Durchschlupfursache"),
                   ("System: warum Kontrollen das Risiko verfehlten", "Und die Systemursache"),
                   ("Jede braucht ihre eigene Lösung", "Jede braucht")],
        "example": "Vorrichtung erlaubt halben Akkusitz (Entstehung); Endtest übersah Wackelkontakt "
                   "(Durchschlupf).",
        "example_cue": "An Nehas Linie",
        "script": "Eine vollständige Analyse hat meist mehr als eine Kette. Die Entstehungsursache erklärt, "
                  "wie der Fehler gemacht wurde. Die Durchschlupfursache erklärt, warum ihn niemand fing. "
                  "Und die Systemursache erklärt, warum Ihre Kontrollen das Risiko überhaupt verfehlten. An "
                  "Nehas Linie konnte eine Vorrichtung einen halben Akkusitz zulassen. Das ist Entstehung. "
                  "Der Endtest prüfte keinen Wackelkontakt. Das ist Durchschlupf. Jede braucht ihre eigene "
                  "Lösung. Aber was, wenn es viele mögliche Ursachen gibt?",
    },
    {
        "key": "p08", "num": 8, "title": "Fischgräte und Pareto",
        "points": [("Fischgräte: 6 Ursachengruppen", "Ein Fischgrätendiagramm ordnet"),
                   ("Pareto: nach Häufigkeit ordnen", "Ein Pareto-Diagramm ordnet"),
                   ("Seltene Sicherheitsrisiken zählen trotzdem", "Aber ein seltenes Sicherheitsrisiko"),
                   ("Eine Fischgräte sind Vermutungen, kein Beweis", "eine Fischgräte ist eine Liste")],
        "example": "Nehas zwei größte Fehlerarten machten 65 % aus. Dort setzte sie zuerst an.",
        "example_cue": "Nehas zwei größte",
        "script": "Wenn viele Ursachen möglich sind, beginnen Sie breit. Ein Fischgrätendiagramm ordnet "
                  "Ideen nach Mensch, Maschine, Methode, Material, Messung und Umwelt. Ein Pareto-Diagramm "
                  "ordnet Fehler nach Häufigkeit. Nehas zwei größte Fehlerarten machten fünfundsechzig "
                  "Prozent aus. Dort setzte sie zuerst an. Aber ein seltenes Sicherheitsrisiko zählt "
                  "trotzdem, auch bei kleiner Zahl. Und denken Sie daran, eine Fischgräte ist eine Liste "
                  "von Vermutungen, kein Beweis. Wie beweisen Sie eine Ursache?",
    },
    {
        "key": "p09", "num": 9, "title": "Die Ursache beweisen",
        "points": [("Vorhersagen, was sich ändern sollte", "Vor dem Versuch"),
                   ("Andere Faktoren festhalten", "Halten Sie andere Faktoren fest"),
                   ("Gut und schlecht testen, über Schichten", "Testen Sie gute und schlechte")],
        "example": "Gute gegen verschlissene Vorrichtungsstifte, mit gleichen Teilen: die Fehler folgten den "
                   "verschlissenen Stiften.",
        "example_cue": "Neha vermutete",
        "script": "Eine logische Kette reicht nicht. Sie müssen sie testen. Vor dem Versuch schreiben Sie "
                  "auf, was sich ändern sollte, wenn Ihre Ursache stimmt. Halten Sie andere Faktoren fest, "
                  "wie Materiallos und Programmversion. Testen Sie gute und schlechte Bedingungen, über "
                  "Schichten. Neha vermutete einen verschlissenen Vorrichtungsstift. Sie testete gute und "
                  "verschlissene Stifte, mit gleichen Teilen. Die Fehler folgten den verschlissenen "
                  "Stiften. Was hätte sie widerlegt? Fehler, die bei den guten Stiften blieben.",
    },
    {
        "key": "p10", "num": 10, "title": "Korrekturmaßnahme und Poka Yoke",
        "points": [("Die Ursache beheben, nicht das Symptom", "Nun beheben Sie die Ursache"),
                   ("Technische Vorbeugung schlägt Erinnerungen", "Technische Vorbeugung"),
                   ("Entstehung beheben + unabhängige Durchschlupfprüfung", "Beheben Sie die Entstehung"),
                   ("FMEA, SOP, Schulung aktualisieren", "Dann aktualisieren Sie die FMEA")],
        "example": "Falsche Audioetiketten: der Drucker braucht jetzt zuerst einen passenden "
                   "Seriennummer-Scan. Nachschulung baut auf Gedächtnis.",
        "example_cue": "Bei falschen Etiketten",
        "script": "Nun beheben Sie die Ursache, nicht nur das Symptom. Technische Vorbeugung schlägt "
                  "Erinnerungen. Denken Sie an codierte Vorrichtungen, Barcode-Verriegelungen und "
                  "Anwesenheitssensoren. Beheben Sie die Entstehung, und ergänzen Sie eine unabhängige "
                  "Prüfung gegen den Durchschlupf. Dann aktualisieren Sie die FMEA, die SOP und die "
                  "Schulung. Bei falschen Etiketten an Audiogeräten braucht der Drucker jetzt zuerst einen "
                  "passenden Seriennummer-Scan. Warum ist Nachschulung meist schwach? Weil sie auf "
                  "Gedächtnis baut. Wirkte Ihre Lösung?",
    },
    {
        "key": "p11", "num": 11, "title": "Bestätigen und abschließen",
        "points": [("Erledigt ≠ bewiesen", "Eine Maßnahme zu erledigen"),
                   ("Herausfordern: gute, schlechte, Grenzmuster", "Fordern Sie die neue Kontrolle heraus"),
                   ("Wiederholung und Ausbeute beobachten", "Beobachten Sie Wiederholung"),
                   ("Kein neuer Stillstand, keine Fehlablehnungen", "Prüfen Sie, dass Sie")],
        "example": "Nehas Abschlussregel: null Wiederholungen in 10 Produktionstagen, Prüftests bestanden, "
                   "jede verdächtige Einheit erfasst.",
        "example_cue": "Neha legte eine Abschlussregel",
        "script": "Eine Maßnahme zu erledigen ist nicht dasselbe wie zu beweisen, dass sie wirkt. Fordern "
                  "Sie die neue Kontrolle heraus, mit bekannt guten, bekannt schlechten und Grenzmustern. "
                  "Beobachten Sie Wiederholung und Erstdurchlaufquote über Schichten, Modelle und Wechsel. "
                  "Prüfen Sie, dass Sie keinen neuen Stillstand und keine Fehlablehnungen geschaffen haben. "
                  "Neha legte eine Abschlussregel mit ihrem Werk fest. Null Wiederholungen in zehn "
                  "Produktionstagen, Prüftests bestanden, jede verdächtige Einheit erfasst. Dann zeichnet "
                  "die Qualität ab.",
    },
    {
        "key": "p12", "num": 12, "title": "KPI für Why-Why",
        "points": [("Tempo und Ergebnisse messen", "Messen Sie Tempo"),
                   ("Frühindikatoren: schnelle Eingrenzung, bestätigte Maßnahmen", "Frühindikatoren sind"),
                   ("Spätindikatoren: Fehlerrate, Wiederholung", "Spätindikatoren sind"),
                   ("Definitionen stabil halten", "Halten Sie die Definitionen stabil")],
        "example": "50 → 15 Fehler = 70 % weniger. ₹1,2 lakh Kosten, ₹30.000 Einsparung im Monat = "
                   "Amortisation in 4 Monaten.",
        "example_cue": "Nehas Fehler sanken",
        "script": "Messen Sie Tempo und Ergebnisse. Frühindikatoren sind schnelle Eingrenzung und "
                  "bestätigte Maßnahmen. Spätindikatoren sind Fehlerrate und Wiederholung. Halten Sie die "
                  "Definitionen stabil, damit niemand eine Zahl durch Umdefinieren verbessert. Nehas Fehler "
                  "sanken von fünfzig auf fünfzehn, bei gleicher Menge. Das sind siebzig Prozent weniger. "
                  "Ihre Lösung kostete hundertzwanzigtausend Rupien, und spart dreißigtausend im Monat. Sie "
                  "amortisiert sich also in vier Monaten. Was davon verfolgt Ihr Team heute?",
    },
    {
        "key": "p13", "num": 13, "title": "Fallstudie: Ladefehler",
        "points": [("Handy oder Tester? Das zuerst testen", "Lag der Fehler im Handy"),
                   ("Am zweiten Tester neu getestet: weiter durchgefallen", "Sie testete die defekten Handys"),
                   ("Verschlissener Stift an der Montagevorrichtung", "Der Akkustecker saß"),
                   ("Lösung: neue Stifte, Standzeitgrenzen, Rüstprüfung", "Ihre Lösung waren")],
        "example": "Die defekten Handys fielen auch am zweiten Tester durch: die Handys waren wirklich "
                   "fehlerhaft.",
        "example_cue": "Sie fielen auch dort durch",
        "script": "So fügte sich Nehas Fall zusammen. Lag der Fehler im Handy, oder im Tester? Sie testete "
                  "die defekten Handys an einem zweiten Tester. Sie fielen auch dort durch, also waren die "
                  "Handys wirklich fehlerhaft. Die Kette lief so. Der Akkustecker saß nur halb, weil ein "
                  "verschlissener Federstift an der neuen Montagevorrichtung ihn nicht ganz eindrückte. Er "
                  "war verschlissen, weil es kein Wechselintervall gab. Ihre Lösung waren neue Stifte, "
                  "Standzeitgrenzen und eine Rüstprüfung. Hätten Sie zuerst den Tester geprüft?",
    },
    {
        "key": "p14", "num": 14, "title": "Set-Top-Box und Audio",
        "points": [("Andere Produkte, andere Belege", "Andere Produkte brauchen"),
                   ("Set-Top-Box: HDMI-Lötung, Firmware, Tester", "Bei einer Set-Top-Box"),
                   ("Audio: Kit, Packfolge, Scans verfolgen", "Bei einem Audiogerät"),
                   ("Bewiesene Lösungen auf ähnliche Linien übertragen", "Ist eine Lösung bewiesen")],
        "example": "Fehlende Fernbedienung: das Kit ließ sie aus, dann schloss der Karton ohne Scan der "
                   "Fernbedienung.",
        "example_cue": "Das Kit ließ die Fernbedienung aus",
        "script": "Andere Produkte brauchen andere Belege. Bei einer Set-Top-Box ohne Bild prüfen Sie "
                  "HDMI-Lötung, Firmware und Testereinstellungen. Und Sie fragen, warum die Bildprüfung am "
                  "Linienende es übersah. Bei einem Audiogerät ohne Fernbedienung verfolgen Sie Kit, "
                  "Packfolge und Scans. Das Kit ließ die Fernbedienung aus. Dann schloss der Karton ohne "
                  "Scan der Fernbedienung. Ist eine Lösung bewiesen, übertragen Sie sie auch auf ähnliche "
                  "Linien. Bereit für den Einführungsplan?",
    },
    {
        "key": "p15", "num": 15, "title": "Einführung in 90 Tagen",
        "points": [("Pilotlinie + ein paar Moderatoren", "Beginnen Sie mit einer Pilotlinie"),
                   ("Tag 1–30: Auslöser, Rollen, Vorlagen", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: untersuchen, Hypothesen testen", "In den nächsten dreißig"),
                   ("Tag 61–90: herausfordern, aktualisieren, verbreiten", "In den letzten dreißig")],
        "example": "Auf echte Muster und bestätigte Glieder auditieren, nicht auf saubere Formulare.",
        "example_cue": "Auditieren Sie auf echte Muster",
        "script": "Machen Sie Why-Why zum Teil der täglichen Führung. Beginnen Sie mit einer Pilotlinie mit "
                  "hohem Risiko, und schulen Sie ein paar Moderatoren. In den ersten dreißig Tagen legen "
                  "Sie Auslöser, Rollen und Vorlagen fest. In den nächsten dreißig führen Sie echte "
                  "Untersuchungen und testen Ihre Hypothesen. In den letzten dreißig prüfen Sie die "
                  "Lösungen, aktualisieren Kontrollen und verbreiten die Lehren. Auditieren Sie auf echte "
                  "Muster und bestätigte Glieder, nicht auf saubere Formulare. Fragen Sie warum, bis Sie "
                  "die Ursache beweisen. Dann machen Sie eine Wiederholung unmöglich.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Warum?", "sub": "Durch einen Fakt gestützt", "icon": "search", "with": 0},
        {"label": "Wieder warum?", "sub": "Fünf ist keine Regel", "icon": "count", "with": 1},
        {"label": "Eine beweisbare, steuerbare Ursache", "icon": "key", "tone": "good", "with": 2}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Steckersitz", "icon": "pin", "with": "example"},
            {"label": "Platinenschaden", "icon": "chip", "with": "example"},
            {"label": "Vorrichtungskontakt", "icon": "wrench", "with": "example"},
            {"label": "Testereinstellung", "icon": "test", "with": "example"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Why-Why", "sub": "Ein Werkzeug von vielen", "icon": "search", "tone": "good", "with": 0},
        {"label": "Echter Ort, echtes Produkt", "icon": "walk", "with": 1},
        {"label": "Belege für jedes Warum", "icon": "clipboard", "with": 2},
        {"label": "Menschen sind ein Hinweis", "icon": "person", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Werker vergaß", "sub": "Reicht nicht", "icon": "person", "with": "example"},
            {"label": "Zuführung und Reihenfolge prüfen", "sub": "Fakten", "icon": "search", "with": "example"}]}},
    "p03": {"type": "doc", "items": [
        {"label": "Problembeschreibung · Linie 2", "icon": "label", "with": 0},
        {"label": "Was: Ladefehler im Endtest", "icon": "power", "with": 1},
        {"label": "Wann: nach dem Vorrichtungswechsel um 11 Uhr", "icon": "clock", "with": 1},
        {"label": "Wie viele: 21 von 700 Handys (3 %)", "icon": "count", "with": 1},
        {"label": "Letzter guter Zustand: unter 0,5 %", "icon": "check", "with": 2}]},
    "p04": {"type": "flow", "items": [
        {"label": "Den Kunden schützen", "icon": "shield", "with": 0},
        {"label": "Letzten guten Punkt finden", "icon": "search", "with": 1},
        {"label": "Bestand sperren: Halle und System", "icon": "lock", "with": 2},
        {"label": "Jede Einheit abgleichen", "icon": "count", "tone": "good", "with": 3}]},
    "p05": {"type": "icons", "items": [
        {"label": "Defekt gegen bekannt gut", "icon": "scale", "with": 0},
        {"label": "Einstellungen, Versionen, Lose", "icon": "gear", "with": 1},
        {"label": "Belege sichern", "icon": "camera", "with": 2},
        {"label": "Gesehen · Quelle · Bedeutung", "icon": "clipboard", "with": 3}]},
    "p06": {"type": "icons", "items": [
        {"label": "Beim Ereignis beginnen", "icon": "search", "with": 0},
        {"label": "Jeder Pfeil: eine prüfbare Behauptung", "icon": "check", "with": 1},
        {"label": "Fakten, keine Etiketten", "icon": "cross", "tone": "bad", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Falsches Kartonetikett", "icon": "label", "tone": "bad", "with": "example"},
            {"label": "Alter Druckauftrag", "icon": "sequence", "with": "example"},
            {"label": "Software ließ es zu", "icon": "chip", "with": "example"},
            {"label": "Drucker nicht mit dem Scan verknüpft", "icon": "barcode", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Entstehung", "sub": "Wie er gemacht wurde", "icon": "wrench", "with": 0},
        {"label": "Durchschlupf", "sub": "Warum ihn niemand fing", "icon": "search", "with": 1},
        {"label": "System", "sub": "Warum Kontrollen ihn verfehlten", "icon": "gear", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Vorrichtung erlaubt halben Sitz", "sub": "Entstehung", "icon": "pin", "tone": "bad", "with": "example"},
            {"label": "Endtest übersieht Wackelkontakt", "sub": "Durchschlupf", "icon": "test", "tone": "bad", "with": "example"},
            {"label": "Eine Lösung für jede", "icon": "check", "tone": "good", "with": 3}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Fischgräte: 6 Gruppen", "icon": "gear", "with": 0},
        {"label": "Pareto: nach Anzahl ordnen", "icon": "chartUp", "with": 1},
        {"label": "Seltene Sicherheitsrisiken", "icon": "warning", "tone": "bad", "with": 2},
        {"label": "Vermutungen, kein Beweis", "icon": "search", "with": 3}],
        "then": {"type": "bars", "label": "", "note": "Die zwei größten = 65 % der Fehler", "with": "example", "items": [
            {"label": "Art 1", "value": 40, "tone": "bad", "with": "example"},
            {"label": "Art 2", "value": 25, "tone": "bad", "with": "example"},
            {"label": "Art 3", "value": 15, "with": "example"},
            {"label": "Art 4", "value": 12, "with": "example"},
            {"label": "Sonstige", "value": 8, "with": "example"}]}},
    "p09": {"type": "steps", "items": [
        {"label": "Die Änderung vorhersagen", "with": 0}, {"label": "Andere Faktoren festhalten", "with": 1},
        {"label": "Gut und schlecht testen", "with": 2}, {"label": "Über Schichten", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Verschlissene Stifte", "sub": "Fehler folgten", "icon": "pin", "with": "example"},
            {"label": "Gute Stifte", "sub": "Gleiche Teile bestanden", "icon": "check", "with": "example"}]}},
    "p10": {"type": "ladder", "top": "AM STÄRKSTEN", "bottom": "AM SCHWÄCHSTEN", "items": [
        {"label": "Codierte Vorrichtung, Verriegelung", "icon": "key", "with": 1},
        {"label": "Anwesenheitssensor", "icon": "sensor", "with": 1},
        {"label": "Unabhängige Durchschlupfprüfung", "icon": "search", "with": 2},
        {"label": "Nachschulung, Erinnerungen", "icon": "warning", "tone": "bad", "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Bekannt gut", "icon": "check", "tone": "good", "with": 1},
        {"label": "Bekannt schlecht", "icon": "cross", "tone": "bad", "with": 1},
        {"label": "Grenzmuster", "icon": "scale", "with": 1},
        {"label": "Wiederholung und Ausbeute", "icon": "chartUp", "with": 2}],
        "then": {"type": "doc", "with": "example", "items": [
            {"label": "Abschlussregel · Linie 2", "icon": "label", "with": "example"},
            {"label": "Null Wiederholungen in 10 Produktionstagen", "icon": "calendar", "with": "example"},
            {"label": "Prüftests bestanden", "icon": "test", "with": "example"},
            {"label": "Jede verdächtige Einheit erfasst", "icon": "count", "with": "example"},
            {"label": "Die Qualität zeichnet ab", "icon": "person", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Tempo und Ergebnisse", "icon": "clock", "with": 0},
        {"label": "Früh: schnelle Eingrenzung", "icon": "shield", "with": 1},
        {"label": "Spät: Fehler, Wiederholungen", "icon": "chartDown", "with": 2},
        {"label": "Stabile Definitionen", "icon": "scale", "with": 3}],
        "then": {"type": "compare", "before": {"label": "Vorher", "value": 50}, "after": {"label": "Nachher", "value": 15},
                 "unit": "Ladefehler, gleiche Menge", "note": "70 % weniger · Amortisation in 4 Monaten", "with": "example"}},
    "p13": {"type": "flow", "items": [
        {"label": "Handy oder Tester?", "icon": "search", "with": 0},
        {"label": "Zweiter Tester: weiter durchgefallen", "icon": "test", "with": 1},
        {"label": "Verschlissener Stift der Montagevorrichtung, kein Wechselintervall", "icon": "pin", "tone": "bad", "with": 2},
        {"label": "Neue Stifte, Standzeitgrenzen, Rüstprüfung", "icon": "check", "tone": "good", "with": 3}]},
    "p14": {"type": "icons", "items": [
        {"label": "Set-Top-Box", "sub": "HDMI, Firmware, Tester", "icon": "chip", "with": 1},
        {"label": "Audiogerät", "sub": "Kit, Folge, Scans", "icon": "wave", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Kit ließ die Fernbedienung aus", "icon": "tray", "tone": "bad", "with": "example"},
            {"label": "Karton geschlossen, kein Scan der Fernbedienung", "icon": "box", "tone": "bad", "with": "example"},
            {"label": "Die bewiesene Lösung verbreiten", "icon": "sequence", "tone": "good", "with": 3}]}},
    "p15": {"type": "timeline", "items": [
        {"label": "Auslöser, Rollen, Vorlagen", "sub": "Tag 1–30", "icon": "clipboard", "with": 1},
        {"label": "Untersuchen, Hypothesen testen", "sub": "31–60", "icon": "search", "with": 2},
        {"label": "Herausfordern, aktualisieren, verbreiten", "sub": "61–90", "icon": "chartUp", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Der Endtest erkannte einen halb sitzenden Akkustecker nicht. Welche Art Ursache ist das?",
        "options": ["Entstehungsursache", "Durchschlupfursache", "Systemursache"],
        "correct": 1,
        "explanation": "Der Fehler entstand früher (Entstehung). Die Durchschlupfursache erklärt, warum die "
                       "Prüfbarriere, hier der Endtest, ihn nicht fing.",
        "q_script": "Kurzer Check. Der Endtest erkannte einen halb sitzenden Akkustecker nicht. Welche Art "
                    "Ursache ist das? Nehmen Sie sich kurz Zeit.",
        "a_script": "Eine Durchschlupfursache. Der Fehler entstand früher. Der Durchschlupf erklärt, warum "
                    "unsere Prüfungen ihn nicht fingen.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "30 Kartons bekamen falsche Etiketten, und jemand sagt „Bedienfehler\". Was sollte das "
                    "Team ZUERST tun?",
        "options": ["Den Werker nachschulen und abschließen", "Verdächtige Kartons eingrenzen, dann fragen, warum der Prozess es zuließ",
                    "Ein Erinnerungsschild an der Verpackung anbringen"],
        "correct": 1,
        "explanation": "Zuerst eingrenzen, dann klären, warum der Prozess überhaupt ein falsches Etikett zuließ. "
                       "Nachschulung oder ein Schild bauen auf Gedächtnis, und stoppen Wiederholungen selten.",
        "q_script": "Noch eine, ein Szenario. Dreißig Kartons bekamen falsche Etiketten, und jemand sagt "
                    "Bedienfehler. Was sollte das Team zuerst tun? Überlegen Sie kurz.",
        "a_script": "Grenzen Sie zuerst die verdächtigen Kartons ein. Dann fragen Sie, warum der Prozess "
                    "überhaupt ein falsches Etikett zuließ. Nachschulung oder ein Schild bauen auf "
                    "Gedächtnis, und stoppen Wiederholungen selten.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
