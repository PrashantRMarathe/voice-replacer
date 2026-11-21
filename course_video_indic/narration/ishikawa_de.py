"""ishikawa in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh ishikawa_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ik_de"
NAME = "ishikawa_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Kaoru Ishikawa": "Kaoru Ischikawa",
    "Ishikawa": "Ischikawa",
    "Pareto": "Pareto",
    "Jidoka": "Dschidoka",
    "Gemba": "Gemba",
    "PFMEA": "pe eff emm e a",
    "SOP": "ess o pe",
    "ESD": "e ess de",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Port-Testfehler an der Switch-Linie stiegen in einer Woche auf das Sechsfache. Das erste "
    "Meeting dauerte zwei Stunden. Es endete mit einer Entscheidung. Einen neuen Tester "
    "kaufen. Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie das Ishikawa-Diagramm "
    "kennen, auch Fischgräte genannt. Sie sehen, wie man breit nach Ursachen sucht und die "
    "echten beweist, bevor man eine Rupie ausgibt. Wir begleiten Nikhil, Qualitätsingenieur "
    "an einer Linie für Netzwerk-Switches."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Setzen Sie eine scharfe, messbare Wirkung in den Kopf. "
    "Suchen Sie breit über die sechs M, ohne Schuld. Und behandeln Sie jede Gräte als "
    "Vermutung, bis Belege sie beweisen. Ihre Aufgabe für diese Woche. Zeichnen Sie eine "
    "Fischgräte für ein wiederkehrendes Problem, und wählen Sie drei Ursachen zum Testen. Gut "
    "gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie Jidoka kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was eine Fischgräte ist",
        "points": [("Ein Problem im Kopf", "Ein Problem sitzt"),
                   ("Mögliche Ursachen auf den Gräten", "Alle möglichen Ursachen"),
                   ("Ein Denkwerkzeug fürs Team", "Es ist ein Teamwerkzeug")],
        "example": "Nikhils Problem: Netzwerk-Switches fallen beim Port-Link-Test durch.",
        "example_cue": "Nikhils Problem",
        "script": "Ein Ishikawa-Diagramm sieht aus wie das Skelett eines Fisches. Ein Problem sitzt im "
                  "Kopf. Alle möglichen Ursachen zweigen von den Gräten ab, sortiert in Familien. Es ist "
                  "ein Teamwerkzeug, damit alle die ganze Suche auf einer Seite sehen. Es verhindert den "
                  "Sprung zur ersten Idee. Nikhils Problem waren Switches, die beim Port-Link-Test "
                  "durchfielen. Woher kommt dieses Werkzeug?",
    },
    {
        "key": "p02", "num": 2, "title": "Herkunft und Grenzen",
        "points": [("Kaoru Ishikawa, Qualitätspionier", "Kaoru Ishikawa"),
                   ("Eines der sieben Qualitätswerkzeuge", "sieben Qualitätswerkzeuge"),
                   ("Zeigt mögliche Ursachen, beweist nichts", "es beweist")],
        "example": "Einen Tester zu kaufen war eine Vermutung. Die Fischgräte macht daraus eine Vermutung "
                   "unter vielen.",
        "example_cue": "Einen neuen Tester zu kaufen",
        "script": "Bekannt gemacht hat es Kaoru Ishikawa, ein japanischer Qualitätsexperte. Es ist eines "
                  "der sieben Qualitätswerkzeuge. Aber das Wichtigste: Es zeigt mögliche Ursachen, es "
                  "beweist keine davon. Beweise kommen später, aus Beobachtung, Messung und Versuchen. "
                  "Einen neuen Tester zu kaufen war nur eine Vermutung. Die Fischgräte macht daraus eine "
                  "Vermutung unter vielen. Wie sieht der Fisch also aus?",
    },
    {
        "key": "p03", "num": 3, "title": "Aufbau des Fisches",
        "points": [("Kopf: die Wirkung", "Der Kopf ist"),
                   ("Wirbelsäule und Hauptgräten: Ursachenfamilien", "Die Wirbelsäule verbindet"),
                   ("Nebengräten: konkrete Ursachen", "Nebengräten tragen")],
        "example": "Eine Ursache gilt als „vermutet“, bis sie bewiesen ist.",
        "example_cue": "Nikhils Regel",
        "script": "Lesen Sie von links nach rechts. Der Kopf ist die Wirkung, das Problem, das Sie lösen "
                  "wollen. Die Wirbelsäule verbindet alles damit. Die Hauptgräten sind Ursachenfamilien, "
                  "wie Maschine oder Methode. Nebengräten tragen konkrete mögliche Ursachen, kleinere "
                  "Gräten gehen tiefer. Nikhils Regel war einfach. Jede Ursache ist vermutet, bis sie "
                  "bewiesen ist. Was kommt in den Kopf?",
    },
    {
        "key": "p04", "num": 4, "title": "Eine scharfe Wirkung",
        "points": [("Was, wo, wann, wie viel", "Sagen Sie, was versagt"),
                   ("Eine Ausgangslage und ein Nenner", "Ergänzen Sie eine Ausgangslage"),
                   ("Ein Fehlerbild auf einmal", "Bleiben Sie bei einem")],
        "example": "„Port-Link-Fehler an Switch-Linie 3 stiegen diese Woche von 5 auf 32 pro 1.000.“",
        "example_cue": "Nikhil schrieb",
        "script": "Ein vager Kopf ergibt einen vagen Fisch. Die Qualität ist schlecht, hilft niemandem. "
                  "Sagen Sie, was versagt, wo, wann und wie viel. Ergänzen Sie eine Ausgangslage und einen "
                  "klaren Nenner. Bleiben Sie bei einem Fehlerbild auf einmal. Nikhil schrieb einen Satz. "
                  "Port-Link-Fehler an Switch-Linie drei stiegen diese Woche von fünf auf zweiunddreißig "
                  "pro tausend. Sehen Sie, wie viel schärfer das ist?",
    },
    {
        "key": "p05", "num": 5, "title": "Die 6M: Mensch, Maschine, Methode",
        "points": [("Mensch: Können, Belastung, Übergabe", "Mensch umfasst"),
                   ("Maschine: Verschleiß, Einstellungen, Wartung", "Maschine umfasst"),
                   ("Methode: Ablauf, SOP, Umrüsten", "Methode umfasst")],
        "example": "Nutzen Sie die Familien als Denkanstöße, nicht als starre Kästen.",
        "example_cue": "Nutzen Sie sie als Denkanstöße",
        "script": "Die meisten Teams nutzen sechs Familien, die sechs M. Mensch umfasst Können, Schulung, "
                  "Belastung und Übergaben. Maschine umfasst Vorrichtungsverschleiß, Einstellungen, Wartung "
                  "und Software. Methode umfasst den Ablauf, die SOP, Umrüsten und Einstellprüfungen. "
                  "Fragen Sie Ihr Team für jede Familie: Könnte das unsere Wirkung erklären? Nutzen Sie sie "
                  "als Denkanstöße, nicht als starre Kästen. Eine Ursache kann zwei Familien berühren. Und "
                  "die anderen drei M?",
    },
    {
        "key": "p06", "num": 6, "title": "Material, Messung, Mitwelt",
        "points": [("Material: Lieferant, Charge, Handling", "Material umfasst"),
                   ("Messung: Lehren, Testgrenzen, Fehlabweisungen", "Messung umfasst"),
                   ("Mitwelt: ESD, Feuchte, Staub, Wärme", "Mitwelt umfasst")],
        "example": "Messung vergessen Teams am häufigsten. Sagt der Tester selbst die Wahrheit?",
        "example_cue": "Messung vergessen Teams",
        "script": "Material umfasst Lieferantenschwankungen, die falsche Charge und Schäden beim Handling. "
                  "Messung umfasst Lehren, Testgrenzen, Kalibrierung und Fehlabweisungen. Mitwelt umfasst "
                  "ESD, Feuchte, Staub, Licht und Wärme. Messung vergessen Teams am häufigsten. Sagt Ihnen "
                  "der Tester selbst die Wahrheit? Behalten Sie die Frage im Kopf. Eine verschlissene "
                  "Testvorrichtung kann den ganzen Tag gute Teile abweisen. Was sammeln Sie, bevor Sie "
                  "zeichnen?",
    },
    {
        "key": "p07", "num": 7, "title": "Zuerst Belege sammeln",
        "points": [("Ein Pareto der Fehlerarten", "einem Pareto"),
                   ("Nach Schicht, Charge, Station, Tester aufteilen", "Teilen Sie die Daten"),
                   ("Gute mit schlechten Einheiten vergleichen", "Vergleichen Sie gute Einheiten")],
        "example": "Die Fehler häuften sich an zwei der vier Teststationen.",
        "example_cue": "Nikhils erste Aufteilung",
        "script": "Bringen Sie Daten in den Raum. Beginnen Sie mit einem Pareto der Fehlerarten, um am "
                  "größten zu arbeiten. Teilen Sie die Daten nach Schicht, Charge, Station und Tester. "
                  "Vergleichen Sie gute Einheiten mit schlechten, nebeneinander. Nikhils erste Aufteilung "
                  "war eine Überraschung. Die meisten Fehler kamen von nur zwei der vier Teststationen. Was "
                  "würden Sie allein daraus vermuten?",
    },
    {
        "key": "p08", "num": 8, "title": "Erstellen: acht Schritte",
        "points": [("Wirkung definieren, Team holen", "Definieren Sie die Wirkung"),
                   ("Gräten zeichnen, sammeln, ohne Schuld", "Zeichnen Sie Kopf"),
                   ("Warum fragen, zusammenfassen, priorisieren", "Fragen Sie, warum das"),
                   ("Verantwortliche zum Testen der Ursachen", "Benennen Sie einen Verantwortlichen")],
        "example": "Nikhils Team: Produktion, Qualität, Test, Instandhaltung und Lager.",
        "example_cue": "Nikhils Team",
        "script": "Erstellen Sie es in acht Schritten. Definieren Sie die Wirkung, mit einem "
                  "bereichsübergreifenden Team. Zeichnen Sie Kopf, Wirbelsäule und Familien. Sammeln Sie "
                  "Ursachen ohne Schuld. Fragen Sie, warum das passieren könnte. Fassen Sie Doppeltes "
                  "zusammen, und priorisieren Sie mit Daten. Benennen Sie einen Verantwortlichen für jeden "
                  "Test. Nikhils Team mischte Produktion, Qualität, Test, Instandhaltung und Lager. Warum "
                  "das Lager?",
    },
    {
        "key": "p09", "num": 9, "title": "Nikhils Fischgräte",
        "points": [("Maschine: Einpresshöhe driftet", "Maschine hatte"),
                   ("Messung: verschlissene Testkabel", "Messung hatte"),
                   ("Material, Methode, Mensch, Mitwelt", "Andere Gräten")],
        "example": "Dreiundzwanzig mögliche Ursachen in vierzig Minuten.",
        "example_cue": "In vierzig Minuten",
        "script": "Weil Materialprobleme oft im Lager beginnen. Das fand das Team. Maschine hatte ein "
                  "Einpresswerkzeug, dessen Höhenanschlag driften konnte. Messung hatte Loopback-Testkabel, "
                  "tausendfach gesteckt. Andere Gräten trugen eine neue Port-Charge, eine fehlende "
                  "Steckprüfung, eine Leiharbeitsgruppe und ESD-Aufzeichnungen. In vierzig Minuten hatten "
                  "sie dreiundzwanzig mögliche Ursachen. Welche testen Sie zuerst?",
    },
    {
        "key": "p10", "num": 10, "title": "Fischgräte, dann fünf Warum",
        "points": [("Die Fischgräte geht in die Breite", "Die Fischgräte geht in die Breite"),
                   ("Fünf Warum gehen in die Tiefe", "Fünf Warum gehen in die Tiefe"),
                   ("Nie bei Werkerfehler aufhören", "hören Sie nie")],
        "example": "Warum verschlissene Kabel? Kein Wechselgrenzwert. Warum? Die Kabel standen in keinem "
                   "Wartungsplan.",
        "example_cue": "Nehmen Sie die Testkabel",
        "script": "Nutzen Sie zwei Werkzeuge zusammen. Die Fischgräte geht in die Breite. Fünf Warum gehen "
                  "in die Tiefe. Nehmen Sie die Testkabel. Warum waren sie verschlissen? Niemand tauschte "
                  "sie. Warum? Sie standen in keinem Wartungsplan. Und hören Sie nie bei Werkerfehler auf. "
                  "Aber eine überzeugende Kette ist noch kein Beweis. Wie beweisen Sie eine Ursache?",
    },
    {
        "key": "p11", "num": 11, "title": "Beweisen: die Belegleiter",
        "points": [("Am Gemba beobachten", "Beobachten Sie den Zustand am Gemba"),
                   ("Zurückverfolgen und messen", "Verfolgen Sie Fehler"),
                   ("Experimentieren, dann wiederholen", "Machen Sie ein kontrolliertes")],
        "example": "Abstimmungen zählen nicht. Ein einzelner guter Versuch ist auch kein Beweis.",
        "example_cue": "Abstimmungen zählen nicht",
        "script": "Steigen Sie eine Belegleiter hinauf. Beobachten Sie den Zustand am Gemba. Verfolgen Sie "
                  "Fehler zu Chargen, Schichten und Stationen zurück. Messen Sie mit kalibrierten Geräten. "
                  "Machen Sie ein kontrolliertes Experiment, ein Faktor nach dem anderen, und wiederholen "
                  "Sie es. Abstimmungen zählen nicht als Beleg. Was hat Nikhil also bewiesen?",
    },
    {
        "key": "p12", "num": 12, "title": "Zwei Ursachen, beide echt",
        "points": [("Verschlissene Kabel: Scheinfehler", "Neue Kabel beseitigten"),
                   ("Höhendrift: echte Fehler", "der Einpressanschlag"),
                   ("Ursachen können gleichzeitig wirken", "Zwei Ursachen")],
        "example": "Nachtest mit neuen Kabeln: 6 von 10 „fehlerhaften“ Switches bestanden. Die anderen 4 "
                   "hatten zu flache Ports.",
        "example_cue": "Er testete zehn",
        "script": "Er testete zehn fehlerhafte Switches erneut, mit neuen Kabeln. Sechs bestanden. Neue "
                  "Kabel beseitigten die Scheinfehler sofort. Die anderen vier waren wirklich defekt. Ihre "
                  "Ports saßen zu flach, weil der Einpressanschlag gedriftet war. Zwei Ursachen, beide "
                  "echt, zur selben Zeit. Das passiert öfter, als man denkt. Nur eine zu beheben ließe das "
                  "halbe Problem stehen. Ein neuer Tester hätte keine behoben. Welche Aktionen würden Sie "
                  "wählen?",
    },
    {
        "key": "p13", "num": 13, "title": "Starke Korrekturmaßnahmen",
        "points": [("Konstruktiv beseitigen, bevor Sie nachschulen", "Beseitigen Sie die Ursache konstruktiv"),
                   ("Sperren, Verriegelungen, Zähler", "Nutzen Sie Sperren"),
                   ("SOP, PFMEA, Kontrollplan aktualisieren", "aktualisieren Sie die SOP")],
        "example": "Steckzähler am Kabel mit Wechselgrenzwert. Höhenprüfung und Sperre zu jedem "
                   "Schichtbeginn.",
        "example_cue": "Nikhils Team ergänzte",
        "script": "Beseitigen Sie die Ursache konstruktiv, bevor Sie auf Erinnerungen oder Nachschulung "
                  "setzen. Nutzen Sie Sperren, Verriegelungen, Zähler und Vorrichtungen. Dann aktualisieren "
                  "Sie die SOP, die PFMEA, den Kontrollplan und die Schulung, zusammen. Nikhils Team "
                  "ergänzte einen Steckzähler an jedem Testkabel, mit Wechselgrenzwert. Und die "
                  "Einpresshöhe wurde zu jedem Schichtbeginn geprüft und gesperrt. Woher wüssten Sie, dass "
                  "es gewirkt hat?",
    },
    {
        "key": "p14", "num": 14, "title": "Wirkung beweisen",
        "points": [("Ziel vor dem Start festlegen", "Legen Sie Ihr Ziel"),
                   ("Ein festes Zeitfenster und eine Stichprobe", "ein festes Zeitfenster"),
                   ("32 → 4 pro 1.000, gehalten über 30 Tage", "Die Fehler sanken")],
        "example": "Null Scheinfehler durch verschlissene Kabel, über 30 Produktionstage.",
        "example_cue": "Und kein einziger",
        "script": "Legen Sie Ihr Ziel vor der Änderung fest, nicht nach den Ergebnissen. Bestimmen Sie ein "
                  "festes Zeitfenster und eine Stichprobe. Nikhil wählte dreißig Produktionstage. Er prüfte "
                  "den Zähler auch mit einem verschlissenen Kabel, um zu beweisen, dass er sperrt. Die "
                  "Fehler sanken von zweiunddreißig pro tausend auf vier und blieben dort. Und kein "
                  "einziger Scheinfehler kam von einem verschlissenen Kabel. Das Tester-Budget ging zurück "
                  "in die Schublade. Welche Fehler sollten Sie vermeiden?",
    },
    {
        "key": "p15", "num": 15, "title": "Fehler und gute Praxis",
        "points": [("Vage Wirkungen und gemischte Fehler", "Eine vage Wirkung"),
                   ("Fehlende Bereiche im Raum", "Instandhaltung, Test oder Lager"),
                   ("Keine Prüfung nach der Sitzung", "Nach dem Sammeln aufhören")],
        "example": "Lassen Sie verworfene Ursachen im Diagramm, mit dem Beleg, der sie ausschloss.",
        "example_cue": "Lassen Sie verworfene Ursachen",
        "script": "Achten Sie auf ein paar Fehler. Eine vage Wirkung, oder mehrere Fehler gemischt. "
                  "Instandhaltung, Test oder Lager außen vor lassen. Werker-Nachlässigkeit schreiben, statt "
                  "auf das System zu schauen. Nach dem Sammeln aufhören, ohne Tests und ohne "
                  "Verantwortliche. Lassen Sie verworfene Ursachen im Diagramm, mit dem Beleg, der sie "
                  "ausschloss. Ihr nächstes Team wird es Ihnen danken. Welchen Fehler haben Sie schon "
                  "gesehen?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Mögliche Ursachen", "icon": "search", "with": 1},
        {"label": "Ursachenfamilien", "icon": "stack", "with": 1},
        {"label": "Das Problem", "sub": "Im Kopf", "icon": "warning", "tone": "bad", "with": 0}]},
    "p02": {"type": "versus", "items": [
        {"label": "Beweis", "sub": "Nicht aus der Fischgräte", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Mögliche Ursachen", "sub": "Was sie zeigt", "icon": "search", "tone": "good", "with": 2}]},
    "p03": {"type": "icons", "items": [
        {"label": "Kopf", "sub": "Die Wirkung", "icon": "warning", "with": 0},
        {"label": "Hauptgräten", "sub": "Ursachenfamilien", "icon": "stack", "with": 1},
        {"label": "Nebengräten", "sub": "Konkrete Ursachen", "icon": "search", "with": 2}]},
    "p04": {"type": "versus", "items": [
        {"label": "„Die Qualität ist schlecht“", "sub": "Vage", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "5 → 32 pro 1.000", "sub": "Linie 3, Port-Link, diese Woche", "icon": "check", "tone": "good", "with": "example"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Mensch", "icon": "person", "with": 0},
        {"label": "Maschine", "icon": "gear", "with": 1},
        {"label": "Methode", "icon": "clipboard", "with": 2}]},
    "p06": {"type": "icons", "items": [
        {"label": "Material", "icon": "box", "with": 0},
        {"label": "Messung", "icon": "scale", "tone": "bad", "with": 1},
        {"label": "Mitwelt", "icon": "wave", "with": 2}]},
    "p07": {"type": "bars", "label": "", "note": "Port-Link-Fehler nach Teststation", "with": "example", "items": [
        {"label": "T1", "value": 14, "tone": "bad", "with": "example"},
        {"label": "T2", "value": 3, "with": "example"},
        {"label": "T3", "value": 12, "tone": "bad", "with": "example"},
        {"label": "T4", "value": 3, "with": "example"}]},
    "p08": {"type": "steps", "items": [
        {"label": "Definieren, Team", "with": 0}, {"label": "Zeichnen, sammeln", "with": 1},
        {"label": "Warum? Zusammenfassen, ordnen", "with": 2}, {"label": "Verantwortliche testen", "with": 3}]},
    "p09": {"type": "icons", "items": [
        {"label": "Maschine", "sub": "Einpresshöhe driftet", "icon": "gear", "with": 0},
        {"label": "Messung", "sub": "Verschlissene Testkabel", "icon": "scale", "with": 1},
        {"label": "Material", "sub": "Neue Port-Charge", "icon": "box", "with": 2},
        {"label": "Methode", "sub": "Keine Steckprüfung", "icon": "clipboard", "with": 2},
        {"label": "Mensch", "sub": "Leiharbeitsgruppe", "icon": "person", "with": 2},
        {"label": "Mitwelt", "sub": "ESD-Aufzeichnungen", "icon": "wave", "with": 2}],
        "then": {"type": "stat", "value": 23, "icon": "search", "label": "mögliche Ursachen in 40 Minuten",
                 "unit": "jede noch eine Vermutung", "with": "example"}},
    "p10": {"type": "steps", "items": [
        {"label": "Kabel verschlissen", "with": "example"},
        {"label": "Nie getauscht", "with": "example"},
        {"label": "Nicht im Wartungsplan", "with": "example"}]},
    "p11": {"type": "ladder", "top": "AM STÄRKSTEN", "bottom": "AM SCHWÄCHSTEN", "items": [
        {"label": "Wiederholen", "icon": "check", "with": 2},
        {"label": "Experimentieren", "icon": "test", "with": 2},
        {"label": "Verfolgen und messen", "icon": "scale", "with": 1},
        {"label": "Beobachten", "icon": "search", "with": 0}]},
    "p12": {"type": "bars", "label": "", "note": "10 fehlerhafte Switches mit neuen Kabeln nachgetestet: 6 bestanden, 4 hatten zu flache "
                                                 "Ports", "with": "example", "items": [
        {"label": "Scheinfehler", "value": 6, "with": "example"},
        {"label": "Echte Fehler", "value": 4, "tone": "bad", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Steckzähler am Kabel", "icon": "count", "with": "example"},
        {"label": "Höhensperre beim Einpressen", "icon": "lock", "with": "example"},
        {"label": "SOP, PFMEA, Kontrollplan", "icon": "clipboard", "tone": "good", "with": 2}]},
    "p14": {"type": "compare", "before": {"label": "Vorher", "value": 32}, "after": {"label": "Nachher", "value": 4},
            "unit": "Port-Link-Fehler pro 1.000 Switches", "note": "Über 30 Produktionstage gehalten", "with": 2},
    "p15": {"type": "icons", "items": [
        {"label": "Vage Wirkung", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Fehlende Bereiche", "icon": "person", "tone": "bad", "with": 1},
        {"label": "Keine Prüfung", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Verworfene Ursachen behalten", "icon": "clipboard", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Welche Wirkung gehört am besten in den Kopf einer Fischgräte?",
        "options": ["„Qualitätsprobleme an der Switch-Linie“",
                    "„Port-Link-Fehler an Linie 3 stiegen diese Woche von 5 auf 32 pro 1.000“",
                    "„Der Tester ist schlecht“"],
        "correct": 1,
        "explanation": "Ein guter Kopf nennt einen Fehler, den Ort, den Zeitraum und das Ausmaß, mit "
                       "Ausgangslage. „Der Tester ist schlecht“ ist schon eine Ursache.",
        "q_script": "Kurzer Check. Welche Wirkung gehört am besten in den Kopf einer Fischgräte? Nehmen Sie "
                    "sich kurz Zeit.",
        "a_script": "Die zweite. Sie nennt einen Fehler, den Ort, den Zeitraum und das Ausmaß. Die letzte ist "
                    "schon eine Ursache.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Nach dem Sammeln stimmt das Team für „Werker-Nachlässigkeit“ als Hauptursache. Was nun?",
        "options": ["Die Werker nachschulen: das Team ist sich einig",
                    "Fragen, was den Fehler möglich machte, und Ursachen mit Belegen testen",
                    "Ein Warnschild an der Station anbringen"],
        "correct": 1,
        "explanation": "Eine Abstimmung ist kein Beleg, und Nachlässigkeit ist keine beherrschbare Ursache. "
                       "Fragen Sie, welcher Prozesszustand den Fehler möglich machte, und beweisen Sie ihn.",
        "q_script": "Noch eine, ein Szenario. Nach dem Sammeln stimmt das Team für Werker-Nachlässigkeit als "
                    "Hauptursache. Was sollte als Nächstes passieren? Überlegen Sie kurz.",
        "a_script": "Fragen Sie, was den Fehler möglich machte, und testen Sie jede Ursache mit Belegen. Eine "
                    "Abstimmung ist kein Beweis, und Nachlässigkeit ist keine Ursache, die Sie beherrschen.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
