"""fmea in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh fmea_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "fm_de"
NAME = "fmea_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Gemba": "Gemba",
    "FMEA": "eff emm e a",
    "RPN": "err pe enn",
    "SOP": "ess o pe",
    "5G": "fünf ge",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Sechs Außen-Funkeinheiten kamen aus dem Feld zurück, voller Wasser. Bei zwei fehlte die "
    "Dichtung. Bei vier war sie verdreht. Alle hatten die Endkontrolle bestanden. Kommt Ihnen "
    "das bekannt vor? In dieser Lektion lernen Sie die FMEA kennen, die Fehlermöglichkeits- "
    "und Einflussanalyse. Sie sehen, wie man Risiken findet, bevor sie den Kunden erreichen, "
    "und die größten zuerst angeht. Wir begleiten Asha, Qualitätsingenieurin in einem "
    "Telekommunikationswerk."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Bauen Sie eine klare Kette, von der Folge über die "
    "Fehlerart zu einer Ursache, die Sie beherrschen. Bewerten Sie mit Belegen, und lassen "
    "Sie nie die Zahl das Urteil ersetzen. Und bevorzugen Sie Vermeidung, dann beweisen Sie "
    "die Wirkung, bevor Sie neu bewerten. Ihre Aufgabe für diese Woche. Wählen Sie einen "
    "kritischen Schritt, und schreiben Sie mit Ihrem Team seine Fehlerkette auf. Gut gemacht, "
    "Lektion abgeschlossen. Als Nächstes lernen Sie Gemba kennen, den echten Ort."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was die FMEA ist",
        "points": [("Wie könnte es versagen, und warum?", "Sie fragt, wie"),
                   ("Was wäre die Folge?", "was die Folge"),
                   ("Handeln, bevor es den Kunden erreicht", "Dann handeln Sie")],
        "example": "Ashas Ziel: die Gehäusedichtung einer 5G-Kleinzelle für außen.",
        "example_cue": "Ashas Ziel",
        "script": "Die FMEA ist eine Teammethode, um vor dem Versagen zu denken. Sie fragt, wie ein Produkt "
                  "oder Prozess versagen könnte, und warum. Sie fragt, was die Folge wäre und welche "
                  "Maßnahmen Sie heute haben. Dann handeln Sie, bevor der Fehler Ihren Kunden erreicht. Das "
                  "ist eingebaute Qualität, keine Prüfung. Ashas Ziel war die Gehäusedichtung einer "
                  "5G-Kleinzelle für außen. Welche Begriffe brauchen Sie?",
    },
    {
        "key": "p02", "num": 2, "title": "Die Schlüsselbegriffe",
        "points": [("Fehlerart: wie es versagt", "Eine Fehlerart"),
                   ("Folge: was der Kunde erleidet", "Die Folge"),
                   ("Ursache: warum es passieren könnte", "Die Ursache"),
                   ("Maßnahme und Aktion", "Eine Maßnahme")],
        "example": "Fehlerart: Dichtung verdreht. Folge: Wasser im Gerät. Ursache: keine Sitzprüfung.",
        "example_cue": "Für Asha",
        "script": "Lernen Sie fünf Begriffe. Eine Fehlerart ist, wie die Anforderung verfehlt wird. Die "
                  "Folge ist, was dem nächsten Prozess oder dem Kunden passiert. Die Ursache ist, warum es "
                  "passieren könnte. Eine Maßnahme verhindert die Ursache oder erkennt den Fehler. Und eine "
                  "Aktion senkt das Risiko. Für Asha war die Fehlerart eine verdrehte Dichtung. Die Folge "
                  "war Wasser im Gerät. Erraten Sie die Ursache?",
    },
    {
        "key": "p03", "num": 3, "title": "Arten der FMEA",
        "points": [("System- und Konstruktions-FMEA", "System und Konstruktion"),
                   ("Prozess-FMEA: die Fertigungsschritte", "Eine Prozess-FMEA"),
                   ("Klare Start- und Endgrenzen", "Legen Sie klare Grenzen fest")],
        "example": "Ashas Umfang: von der Entnahme der Dichtung bis zum dichten, geprüften Gehäuse.",
        "example_cue": "Ashas Umfang",
        "script": "Es gibt mehrere Arten. System und Konstruktion, also die System-FMEA und die "
                  "Konstruktions-FMEA, betrachten das Produkt und das Zusammenspiel seiner Teile. Die "
                  "Maschinen-Analyse betrachtet Anlagen. Eine Prozess-FMEA betrachtet Ihre "
                  "Fertigungsschritte, und die nutzen die meisten Lean-Teams. Legen Sie klare Grenzen fest, "
                  "damit es überschaubar bleibt. Ashas Umfang reichte von der Entnahme der Dichtung bis zum "
                  "dichten, geprüften Gehäuse. Wann sollten Sie eine erstellen?",
    },
    {
        "key": "p04", "num": 4, "title": "Wann starten oder aktualisieren",
        "points": [("Neues Produkt oder neuer Prozess", "ein neues Produkt"),
                   ("Jede Änderung: Material, Werkzeug, Layout", "jeder Änderung"),
                   ("Nach einer Reklamation oder einem Durchschlupf", "nach einer Reklamation")],
        "example": "Asha aktualisierte ihre am Tag, als die sechs nassen Geräte zurückkamen.",
        "example_cue": "Asha aktualisierte ihre",
        "script": "Starten Sie eine für ein neues Produkt oder einen neuen Prozess. Aktualisieren Sie sie "
                  "nach jeder Änderung. Material, Anlage, Software, Werkzeug, Layout oder Methode. Und "
                  "aktualisieren Sie sie nach einer Reklamation, oder wenn Sie erfahren, dass eine Maßnahme "
                  "nicht wirkt. Eine FMEA, die zwei Jahre alt ist, beschreibt ein Werk, das es nicht mehr "
                  "gibt. Asha aktualisierte ihre am Tag, als die nassen Geräte zurückkamen. Wer erstellt "
                  "sie?",
    },
    {
        "key": "p05", "num": 5, "title": "Das Team und die Eingaben",
        "points": [("Ein bereichsübergreifendes Team", "Holen Sie die Produktion"),
                   ("Erfahrene Werker", "Nehmen Sie erfahrene Werker"),
                   ("Ablaufplan, Daten, Arbeitsanweisungen", "Bringen Sie auch die Eingaben"),
                   ("Vor dem Bewerten an den Gemba gehen", "gehen Sie an den Gemba")],
        "example": "Am Gemba sah Asha zwei Dichtungsgrößen in einer Kiste.",
        "example_cue": "Am Gemba",
        "script": "Holen Sie die Produktion, Technik, Qualität, Instandhaltung und den Test dazu. Nehmen "
                  "Sie erfahrene Werker, die die echte Arbeit kennen. Bringen Sie auch die Eingaben mit. "
                  "Einen Prozessablauf, Fehlerdaten, Arbeitsanweisungen und Erfahrungen. Dann gehen Sie an "
                  "den Gemba, bevor Sie irgendetwas bewerten. Vergleichen Sie die geschriebene Methode mit "
                  "dem, was wirklich passiert. Am Gemba sah Asha zwei Dichtungsgrößen in einer Kiste. Was "
                  "würden Sie notieren?",
    },
    {
        "key": "p06", "num": 6, "title": "Die sieben Schritte",
        "points": [("Planen, Struktur, Funktion", "Planen Sie den Umfang"),
                   ("Fehleranalyse", "analysieren Sie die Fehler"),
                   ("Risikoanalyse", "bewerten Sie das Risiko"),
                   ("Optimieren und dokumentieren", "handeln Sie")],
        "example": "Ashas Team: eine Anforderung und eine Fehlerkette auf einmal.",
        "example_cue": "Ashas Team",
        "script": "Die Methode hat sieben Schritte. Planen Sie den Umfang, bilden Sie die Struktur ab, und "
                  "schreiben Sie, was jeder Schritt leisten muss. Dann analysieren Sie die Fehler und "
                  "bewerten Sie das Risiko. Schließlich handeln Sie und dokumentieren, was sich geändert "
                  "hat. Eine einfache Regel hält Meetings vernünftig. Ashas Team arbeitete an einer "
                  "Anforderung und einer Fehlerkette auf einmal. Wie sieht eine gute Anforderung aus?",
    },
    {
        "key": "p07", "num": 7, "title": "Klare Funktionen schreiben",
        "points": [("Ein Verb plus eine Anforderung", "als Verb, plus"),
                   ("Messbar, nicht vage", "messbar")],
        "example": "Schwach: „Dichtung einsetzen.“ Stark: „Die richtige Dichtung ganz in die Nut legen, ohne "
                   "Verdrehung oder Schaden.“",
        "example_cue": "Vergleichen Sie diese",
        "script": "Schreiben Sie jede Funktion als Verb, plus eine Anforderung, die Sie prüfen können. "
                  "Machen Sie sie messbar, nicht vage. Richtig montieren sagt niemandem etwas. Vergleichen "
                  "Sie diese. Dichtung einsetzen. Oder, die richtige Dichtung ganz in die Nut legen, ohne "
                  "Verdrehung oder Schaden. Die zweite sagt Ihnen genau, wie sie versagen kann. Fehlt, "
                  "falsche Größe, nicht im Sitz, oder verdreht. Können Sie einen Ihrer Schritte so "
                  "umschreiben?",
    },
    {
        "key": "p08", "num": 8, "title": "Die Fehlerkette",
        "points": [("Folge: Wassereintritt, Ausfall im Feld", "Die Folge ist"),
                   ("Fehlerart: Dichtung fehlt oder verdreht", "Die Fehlerart ist"),
                   ("Ursache: etwas, das Sie beherrschen", "Die Ursache muss")],
        "example": "Ursache: zwei Dichtungsgrößen in einer Kiste, und keine Sitzprüfung.",
        "example_cue": "Ashas Ursachen waren",
        "script": "Verknüpfen Sie jetzt die Kette. Die Folge ist Wassereintritt und ein ausgefallenes Gerät "
                  "am Mast. Die Fehlerart ist eine fehlende oder verdrehte Dichtung. Die Ursache muss etwas "
                  "sein, das Sie wirklich beherrschen. Schreiben Sie nie Nachlässigkeit oder menschlicher "
                  "Fehler. Ashas Ursachen waren konkret. Zwei Dichtungsgrößen teilten sich eine Kiste. Und "
                  "nichts prüfte, ob die Dichtung im Sitz war. Jetzt können Sie eine Lösung entwerfen. Aber "
                  "welches Risiko kommt zuerst?",
    },
    {
        "key": "p09", "num": 9, "title": "Bedeutung, Auftreten, Entdeckung",
        "points": [("Bedeutung: wie schlimm die Folge ist", "Die Bedeutung bewertet"),
                   ("Auftreten: wie oft die Ursache vorkommt", "Das Auftreten bewertet"),
                   ("Entdeckung: wie wahrscheinlich wir es finden", "Die Entdeckung bewertet"),
                   ("Jede Bewertung braucht Belege", "Belegen Sie jede Bewertung")],
        "example": "Dichtungsrisiko: Bedeutung 8, Auftreten 5, Entdeckung 6.",
        "example_cue": "Ashas Team bewertete",
        "script": "Sie bewerten drei Dinge, meist von eins bis zehn. Die Bedeutung bewertet, wie schlimm "
                  "die Folge ist. Das Auftreten bewertet, wie oft die Ursache vorkommt, mit der heutigen "
                  "Vermeidung. Die Entdeckung bewertet, wie wahrscheinlich Sie es finden, bevor es "
                  "entkommt. Hier heißt zehn, dass Sie es wohl nicht finden. Belegen Sie jede Bewertung mit "
                  "Daten, nicht mit Gefühlen. Ashas Team bewertete die Dichtung mit acht, fünf und sechs. "
                  "Was ergibt das?",
    },
    {
        "key": "p10", "num": 10, "title": "Risikoprioritätszahl",
        "points": [("RPN = Bedeutung × Auftreten × Entdeckung", "Die Risikoprioritätszahl"),
                   ("8 × 5 × 6 = 240", "Das sind zweihundertvierzig"),
                   ("Ein Hinweis, kein Urteil", "Aber behandeln Sie sie")],
        "example": "RPN der Dichtung: 240, die höchste auf Ashas Bogen.",
        "example_cue": "Es war die höchste Zahl",
        "script": "Die Risikoprioritätszahl multipliziert die drei Bewertungen. Für die Dichtung acht mal "
                  "fünf mal sechs. Das sind zweihundertvierzig. Es war die höchste Zahl auf Ashas Bogen. "
                  "Aber behandeln Sie sie als Hinweis, nicht als Urteil. Verschiedene Bewertungen können "
                  "dieselbe RPN ergeben. Und Teams sind versucht, Bewertungen zu schieben, um unter einer "
                  "Grenze zu bleiben. Worauf sollten Sie also auch schauen?",
    },
    {
        "key": "p11", "num": 11, "title": "Die Bedeutung zuerst",
        "points": [("Hohe Bedeutung braucht trotzdem Handeln", "eine hohe Bedeutung"),
                   ("Handlungspriorität hoch, mittel, niedrig", "Viele Teams nutzen heute"),
                   ("Fragen Sie: Ist die Vermeidung oder die Entdeckung schwach?", "Und fragen Sie immer")],
        "example": "Ein Sicherheitsrisiko mit RPN 90 kann wichtiger sein als ein optisches mit 200.",
        "example_cue": "Ein Sicherheitsrisiko",
        "script": "Schauen Sie zuerst auf die Bedeutung. Eine hohe Bedeutung braucht Handeln, auch wenn "
                  "ihre RPN mäßig wirkt. Viele Teams nutzen heute die Handlungspriorität, bewertet mit "
                  "hoch, mittel oder niedrig. Hoch heißt handeln, oder formal begründen, warum nicht. Und "
                  "fragen Sie immer, welche Maßnahme schwach ist, die Vermeidung oder die Entdeckung. Ein "
                  "Sicherheitsrisiko mit neunzig kann wichtiger sein als ein optisches mit zweihundert. "
                  "Stimmen Sie zu?",
    },
    {
        "key": "p12", "num": 12, "title": "Vermeidung oder Entdeckung",
        "points": [("Vermeidung: die Ursache verhindern", "Vermeidungsmaßnahmen"),
                   ("Entdeckung: vor der Freigabe finden", "Entdeckungsmaßnahmen"),
                   ("Automatisch schlägt menschliches Urteil", "automatisch schlägt")],
        "example": "Ashas einzige Maßnahme: eine visuelle Endkontrolle. Entdeckung, und schwach.",
        "example_cue": "Ashas einzige Maßnahme",
        "script": "Wissen Sie, welche Art Maßnahme Sie haben. Vermeidungsmaßnahmen verhindern die Ursache, "
                  "wie ein codiertes Teil oder eine Rezeptsperre. Entdeckungsmaßnahmen finden den Fehler "
                  "vor der Freigabe, wie ein Sensor oder ein Test. Fragen Sie, ob jede jedes Teil prüft und "
                  "ob man sie umgehen kann. Und automatisch schlägt menschliches Urteil, fast immer. Ashas "
                  "einzige Maßnahme war eine visuelle Endkontrolle. Entdeckung, und schwach. Was würden Sie "
                  "ergänzen?",
    },
    {
        "key": "p13", "num": 13, "title": "Starke Aktionen wählen",
        "points": [("Die Ursache beseitigen", "Zuerst beseitigen"),
                   ("Verhindern: Sperre, Codierung, Verriegelung", "Als Nächstes verhindern"),
                   ("Entdeckung verbessern", "Dann verbessern Sie die Entdeckung"),
                   ("Schulung und Checklisten zuletzt", "Schulung und Checklisten")],
        "example": "Ashas Aktionen: eine Dichtung pro codierter Schale, eine Nutvorrichtung, ein "
                   "Anwesenheitssensor und ein Dichtheitstest.",
        "example_cue": "Asha wählte",
        "script": "Manche Aktionen sind stärker als andere. Zuerst beseitigen Sie die Ursache konstruktiv, "
                  "wenn möglich. Als Nächstes verhindern Sie sie, mit einer Sperre, Codierung oder "
                  "Verriegelung. Dann senken Sie die Streuung. Dann verbessern Sie die Entdeckung mit einer "
                  "automatischen Prüfung. Schulung und Checklisten kommen zuletzt, wenn nichts Stärkeres "
                  "geht. Asha wählte eine codierte Schale mit nur einer Dichtungsgröße, eine "
                  "Nutvorrichtung, einen Anwesenheitssensor und einen Dichtheitstest. Hat es gewirkt?",
    },
    {
        "key": "p14", "num": 14, "title": "Prüfen, dann neu bewerten",
        "points": [("Unter echten Bedingungen beweisen", "Beweisen Sie zuerst"),
                   ("Bedeutung bleibt 8: gleiche Folge", "Die Bedeutung blieb"),
                   ("Auftreten 5 → 2, Entdeckung 6 → 2", "Das Auftreten sank"),
                   ("RPN 240 → 32", "Die RPN sank")],
        "example": "Erst der Beweis: der Sensor fand jedes Schlechtmuster in einem Versuch mit 500 "
                   "Einheiten.",
        "example_cue": "Ashas Beweis",
        "script": "Bewerten Sie nie neu, nur weil Sie einen Sensor gekauft haben. Beweisen Sie zuerst die "
                  "Wirkung unter echten Bedingungen. Ashas Beweis kam aus einem Versuch mit fünfhundert "
                  "Einheiten. Der Sensor fand jedes Schlechtmuster. Die Bedeutung blieb bei acht, denn "
                  "Wasser im Gerät ist genauso schlimm. Das Auftreten sank auf zwei, die Entdeckung auf "
                  "zwei. Die RPN sank von zweihundertvierzig auf zweiunddreißig. Ist die Arbeit jetzt "
                  "fertig?",
    },
    {
        "key": "p15", "num": 15, "title": "Lebendig halten",
        "points": [("Kontrollplan, SOP, Schulung aktualisieren", "Aktualisieren Sie den Kontrollplan, die SOP"),
                   ("Hohe Risiken jede Woche prüfen", "Prüfen Sie offene hohe Risiken"),
                   ("Erkenntnisse auf ähnliche Produkte übertragen", "Übertragen Sie, was Sie gelernt haben")],
        "example": "Ashas Team übertrug die codierte Schale auf zwei weitere Außengeräte.",
        "example_cue": "Ashas Team übertrug",
        "script": "Nicht ganz. Eine FMEA ist ein lebendes Dokument, kein Formular zum Abheften. "
                  "Aktualisieren Sie den Kontrollplan, die SOP, die Schulung und die Audits. Prüfen Sie "
                  "offene hohe Risiken jede Woche, und den ganzen Bogen nach jeder Reklamation. Übertragen "
                  "Sie, was Sie gelernt haben, auf ähnliche Produkte. Ashas Team übertrug die codierte "
                  "Schale auf zwei weitere Außengeräte. Und seitdem kam kein nasses Gerät mehr zurück. Wo "
                  "starten Sie Ihre?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Wie könnte es versagen?", "icon": "search", "with": 0},
        {"label": "Was ist die Folge?", "icon": "warning", "with": 1},
        {"label": "Zuerst handeln", "icon": "shield", "tone": "good", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Fehlerart", "sub": "Wie es versagt", "icon": "cross", "with": 0},
        {"label": "Folge", "sub": "Was es verursacht", "icon": "warning", "with": 1},
        {"label": "Ursache", "sub": "Warum es passiert", "icon": "search", "with": 2},
        {"label": "Maßnahme, Aktion", "sub": "Was es stoppt", "icon": "shield", "tone": "good", "with": 3}]},
    "p03": {"type": "icons", "items": [
        {"label": "System", "icon": "stack", "with": 0},
        {"label": "Konstruktion", "icon": "shape", "with": 0},
        {"label": "Prozess", "icon": "sequence", "tone": "good", "with": 1},
        {"label": "Grenzen", "icon": "pin", "with": 2}]},
    "p04": {"type": "icons", "items": [
        {"label": "Neues Produkt oder neuer Prozess", "icon": "box", "with": 0},
        {"label": "Jede Änderung", "icon": "gear", "with": 1},
        {"label": "Reklamation oder Durchschlupf", "icon": "warning", "tone": "bad", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Bereichsübergreifend", "icon": "person", "with": 0},
        {"label": "Werker", "icon": "hand", "with": 1},
        {"label": "Daten und Ablauf", "icon": "clipboard", "with": 2},
        {"label": "Zuerst der Gemba", "icon": "walk", "tone": "good", "with": 3}]},
    "p06": {"type": "steps", "items": [
        {"label": "Planen", "with": 0}, {"label": "Struktur", "with": 0},
        {"label": "Funktion", "with": 0}, {"label": "Fehler", "with": 1},
        {"label": "Risiko", "with": 2}, {"label": "Optimieren", "with": 3},
        {"label": "Dokumentieren", "with": 3}]},
    "p07": {"type": "versus", "items": [
        {"label": "„Dichtung einsetzen“", "sub": "Vage", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "„Richtige Dichtung, ganz im Sitz, unverdreht“", "sub": "Messbar", "icon": "check", "tone": "good", "with": "example"}]},
    "p08": {"type": "flow", "items": [
        {"label": "Folge", "sub": "Wassereintritt", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Fehlerart", "sub": "Fehlt oder verdreht", "icon": "cross", "tone": "bad", "with": 1},
        {"label": "Ursache", "sub": "Gemischte Kiste, keine Sitzprüfung", "icon": "search", "with": "example"}]},
    "p09": {"type": "bars", "label": "", "note": "Bedeutung · Auftreten · Entdeckung, 1 bis 10", "with": "example", "items": [
        {"label": "Bed.", "value": 8, "tone": "bad", "with": "example"},
        {"label": "Auftr.", "value": 5, "with": "example"},
        {"label": "Entd.", "value": 6, "with": "example"}]},
    "p10": {"type": "stat", "value": 240, "icon": "warning", "label": "RPN der Dichtung",
            "unit": "8 × 5 × 6", "with": 1},
    "p11": {"type": "ladder", "top": "HOCH", "bottom": "NIEDRIG", "items": [
        {"label": "Handeln, oder begründen, warum nicht", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Prüfen und verbessern", "icon": "search", "with": 1},
        {"label": "Halten und überwachen", "icon": "check", "tone": "good", "with": 1}]},
    "p12": {"type": "versus", "items": [
        {"label": "Entdeckung", "sub": "Visuelle Endkontrolle", "icon": "search", "with": 1},
        {"label": "Vermeidung", "sub": "Die Ursache verhindern", "icon": "key", "tone": "good", "with": 0}]},
    "p13": {"type": "ladder", "top": "AM STÄRKSTEN", "bottom": "AM SCHWÄCHSTEN", "items": [
        {"label": "Konstruktiv beseitigen", "icon": "shape", "with": 0},
        {"label": "Verhindern: Codierung, Sperre", "icon": "key", "with": 1},
        {"label": "Automatisch entdecken", "icon": "sensor", "with": 2},
        {"label": "Schulen, Checkliste", "icon": "clipboard", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Vorher", "value": 240}, "after": {"label": "Nachher", "value": 32},
            "unit": "RPN der Dichtung", "note": "Auftreten 5 → 2 · Entdeckung 6 → 2", "with": 3},
    "p15": {"type": "flow", "items": [
        {"label": "Kontrollplan, SOP", "icon": "clipboard", "with": 0},
        {"label": "Wöchentliche Risikoprüfung", "icon": "calendar", "with": 1},
        {"label": "Auf ähnliche Geräte übertragen", "icon": "sequence", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Welche ist eine nützliche FMEA-Ursache?",
        "options": ["Nachlässigkeit des Werkers",
                    "Zwei Dichtungsgrößen teilen sich eine Kiste an der Station",
                    "Wasser dringt in das Gerät ein"],
        "correct": 1,
        "explanation": "Eine nützliche Ursache ist ein konkreter Zustand, den Sie beherrschen. Nachlässigkeit "
                       "ist eine Schuldzuweisung, und Wasser im Gerät ist die Folge.",
        "q_script": "Kurzer Check. Welche davon ist eine nützliche Ursache für eine FMEA? Nehmen Sie sich "
                    "kurz Zeit.",
        "a_script": "Die zweite. Sie ist ein konkreter Zustand, den Sie beherrschen. Nachlässigkeit ist nur "
                    "Schuld, und Wasser im Gerät ist die Folge.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Nach einem Sensor und einem Dichtheitstest will das Team die Bedeutung von 8 auf 4 "
                    "senken. Ist das richtig?",
        "options": ["Ja: das Risiko ist jetzt geringer",
                    "Nein: die Bedeutung ändert sich nur, wenn sich die Folge ändert",
                    "Ja, wenn die RPN unter 100 bleibt"],
        "correct": 1,
        "explanation": "Die Bedeutung bewertet die Folge. Wasser in einem Gerät ist genauso schlimm wie vorher. "
                       "Die neuen Maßnahmen senken Auftreten und Entdeckung, nicht die Bedeutung.",
        "q_script": "Noch eine, diesmal ein Szenario. Nach einem Sensor und einem Dichtheitstest will das "
                    "Team die Bedeutung von acht auf vier senken. Ist das richtig? Überlegen Sie kurz.",
        "a_script": "Nein. Die Bedeutung bewertet die Folge, und Wasser im Gerät ist genauso schlimm wie "
                    "vorher. Die neuen Maßnahmen senken stattdessen Auftreten und Entdeckung.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
