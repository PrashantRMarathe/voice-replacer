"""hancho in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh hancho_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "hc_de"
NAME = "hancho_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Ishikawa": "Ischikawa",
    "Hancho": "Hantscho",
    "Gemba": "Gemba",
    "TAKT": "Takt",
    "SOP": "ess o pe",
    "LED": "ell e de",
    "TV": "te fau",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Letzten Monat fehlten der Linie zwanzig TV pro Stunde, eine ganze Schicht lang. Niemand "
    "merkte es bis zum Bericht am nächsten Morgen. Da war der Verlust schon Geschichte. Kommt "
    "Ihnen das bekannt vor? In dieser Lektion lernen Sie Hancho kennen, Führung direkt in der "
    "Fertigung. Sie sehen, wie eine Teamleiterin eine Lücke in der ersten Stunde erkennt und "
    "vor Schichtende behebt. Wir begleiten Sunita, neue Hancho an einer LED-TV-Linie."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Führen Sie vom Gemba aus, und vergleichen Sie den Standard "
    "mit dem, was wirklich passiert. Machen Sie jede Lücke sichtbar, jede Stunde, und "
    "reagieren Sie in derselben Schicht. Und entwickeln Sie Ihre Leute, damit die Linie nicht "
    "von Ihnen abhängt. Ihre Aufgabe für diese Woche. Schreiben Sie Ihre eigene "
    "Führungs-Standardarbeit für eine Schicht. Gut gemacht, Lektion abgeschlossen. Als "
    "Nächstes lernen Sie das Ishikawa-Diagramm kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was ein Hancho ist",
        "points": [("Japanisch für Teamleiter", "ist Japanisch für"),
                   ("Ein Führungssystem, kein Werkzeug", "Es ist kein Werkzeug"),
                   ("Führt dort, wo Wert entsteht", "die genau dort führt")],
        "example": "Sunita: zwölf Werker, eine LED-TV-Linie, die Ergebnisse jeder Schicht.",
        "example_cue": "Sunita führt zwölf Werker an einer LED-Bildschirmlinie",
        "script": "Hancho ist Japanisch für Teamleiter, oder Führungskraft der ersten Ebene. Es ist kein "
                  "Werkzeug zum Ausfüllen. Es ist ein Führungssystem, aufgebaut um eine Person, die genau "
                  "dort führt, wo Wert entsteht. Nah an den Werkern, am Prozess und an den Problemen. "
                  "Sunita führt zwölf Werker an einer LED-Bildschirmlinie. Sie verantwortet die Ergebnisse "
                  "jeder Schicht, und jeden TV. Wie denkt also ein Hancho?",
    },
    {
        "key": "p02", "num": 2, "title": "Die Hancho-Denkweise",
        "points": [("Was ist der Standard? Was ist Ist?", "Was ist der Standard"),
                   ("Wo ist die Lücke, und warum?", "Wo ist die Lücke"),
                   ("Jetzt handeln, dann Wiederholung verhindern", "Was tun wir sofort")],
        "example": "Sunita hat diese Fragen auf einer Karte in der Tasche.",
        "example_cue": "Sunita hat diese Fragen",
        "script": "Ein Hancho stellt jedes Mal dieselben Fragen. Was ist der Standard? Was passiert "
                  "wirklich? Wo ist die Lücke, und was hat sie verursacht? Was tun wir sofort, und was muss "
                  "sich ändern, damit es nie wieder passiert? Keine davon enthält Schuld. Nur Standard, "
                  "Ist, Lücke und Handeln. Sunita hat diese Fragen auf einer kleinen Karte in der Tasche. "
                  "Warum braucht eine Linie diese Rolle?",
    },
    {
        "key": "p03", "num": 3, "title": "Warum Linien einen Hancho brauchen",
        "points": [("Kleine Lücken wachsen, wenn Führung fern ist", "Wenn Führung fern vom Prozess"),
                   ("Schnellere Reaktion, klare Verantwortung", "Ein Hancho bedeutet"),
                   ("Täglicher Kaizen, nicht nur Projekte", "Und Verbesserung passiert")],
        "example": "Letzten Monat: eine Lücke von 20 TV pro Stunde, am nächsten Morgen gefunden.",
        "example_cue": "Denken Sie an die Lücke",
        "script": "Wenn Führung fern vom Prozess ist, wachsen kleine Lücken. Eine lockere Vorrichtung wird "
                  "zum Stillstand. Ein paar Fehler werden zur Reklamation. Ein Hancho bedeutet schnellere "
                  "Reaktion und klare Verantwortung in jeder Schicht. Standards werden eingehalten, weil "
                  "jemand prüft. Und Verbesserung passiert jeden Tag, nicht nur in Sonderprojekten. Denken "
                  "Sie an die Lücke vom letzten Monat, am nächsten Morgen gefunden. Wofür genau ist ein "
                  "Hancho verantwortlich?",
    },
    {
        "key": "p04", "num": 4, "title": "Wofür ein Hancho verantwortlich ist",
        "points": [("Sicherheit und Qualität", "Sicherheit kommt zuerst"),
                   ("Lieferung und Kosten", "Lieferung bedeutet"),
                   ("Menschen und Prozess", "Und Menschen")],
        "example": "Sunitas Regel: selbst lösen, Unterstützung rufen oder eskalieren. Wissen, was.",
        "example_cue": "Sunita lernte",
        "script": "Ein Hancho verantwortet sechs Bereiche. Sicherheit kommt zuerst, dann Qualität, indem "
                  "der Standard geschützt und Fehler eingedämmt werden. Lieferung bedeutet, Plan gegen Ist "
                  "jede Stunde zu verfolgen. Kosten bedeutet, Ausschuss, Nacharbeit und Stillstand zu "
                  "senken. Und Menschen und Prozess, durch Schulung, Standardarbeit und eine bereite Linie. "
                  "Sunita lernte noch etwas. Wissen, wann sie es selbst löst, wann sie Unterstützung ruft "
                  "und wann sie eskaliert. Wie beginnt ihr Tag?",
    },
    {
        "key": "p05", "num": 5, "title": "Vor Schichtbeginn",
        "points": [("Bereitschaftsprüfung vor der Schicht", "Zuerst die Bereitschaft"),
                   ("Ein kurzes Team-Briefing", "Dann ein kurzes Briefing"),
                   ("Anlauf- und Erstteilprüfungen", "Dann die Anlaufprüfungen")],
        "example": "Heutiges Briefing: Modellwechsel auf den 43-Zoll-TV um 10 Uhr.",
        "example_cue": "Das heutige Briefing",
        "script": "Sunitas Tag beginnt vor der Linie. Zuerst die Bereitschaft. Sind Menschen, Material, "
                  "Maschinen, Werkzeuge und Dokumente bereit? Dann ein kurzes Briefing. Das Ziel, "
                  "Qualitätswarnungen, Sicherheitspunkte und was die letzte Schicht gelernt hat. Dann die "
                  "Anlaufprüfungen, mit dem Erstteil. Das heutige Briefing hatte einen großen Punkt. Einen "
                  "Modellwechsel auf den dreiundvierzig-Zoll-TV um zehn Uhr. Was passiert, wenn die Linie "
                  "läuft?",
    },
    {
        "key": "p06", "num": 6, "title": "Während und nach der Schicht",
        "points": [("Stündlich Plan gegen Ist", "Jede Stunde"),
                   ("Auf jede Abweichung reagieren", "Sie reagiert"),
                   ("Am Prozess coachen", "Sie coacht"),
                   ("Eine sachliche Übergabe", "Am Ende")],
        "example": "Übergabenotiz: offene Punkte, WIP, Qualitätsstand, Maßnahmen und Verantwortliche.",
        "example_cue": "Ihre Übergabe",
        "script": "Jede Stunde vergleicht sie Plan mit Ist. Menge, Erstdurchlaufquote, Stillstand und "
                  "Umlauf. Sie reagiert auf jede Abweichung und erfasst sie. Sie coacht Werker am Prozess, "
                  "nicht im Besprechungsraum. Am Ende übergibt sie an die nächste Schicht mit Fakten, nicht "
                  "mit Erinnerungen. Ihre Übergabe deckt offene Punkte, Qualitätsstand, Maßnahmen und "
                  "Verantwortliche ab. Wo verbringt sie die meiste Zeit?",
    },
    {
        "key": "p07", "num": 7, "title": "Führen am Gemba",
        "points": [("Den echten Prozess und das echte Produkt beobachten", "Sie beobachtet"),
                   ("Mit dem Werker sprechen", "Sie spricht"),
                   ("Fragen stellen, nicht nur Antworten geben", "Sie stellt Fragen")],
        "example": "„Was sollte passieren? Was passiert wirklich? Was hat sich geändert?“",
        "example_cue": "Ihre drei Lieblingsfragen",
        "script": "Am Gemba, nicht am Schreibtisch. Sie beobachtet den echten Prozess und das echte "
                  "Produkt. Sie spricht mit dem Werker, der die Arbeit macht. Sie vergleicht die echte "
                  "Methode mit dem Standard. Und sie stellt Fragen, die zum Denken bringen, statt jede "
                  "Antwort zu liefern. Ihre drei Lieblingsfragen sind einfach. Was sollte passieren? Was "
                  "passiert wirklich? Und was hat sich geändert? Welche würden Sie zuerst stellen?",
    },
    {
        "key": "p08", "num": 8, "title": "Führungs-Standardarbeit",
        "points": [("Prüfungen nach Häufigkeit", "listet ihre Prüfungen auf"),
                   ("Reihenfolge, Zykluszeit, Qualitätspunkte", "Sie prüft"),
                   ("Die aktuelle SOP an jeder Station", "Und die aktuelle SOP")],
        "example": "Sunitas Liste: Schichtbeginn, jede Stunde, jeder Modellwechsel, Schichtende.",
        "example_cue": "Ihre Liste läuft",
        "script": "Auch ein Hancho braucht Standardarbeit. Die Führungs-Standardarbeit listet ihre "
                  "Prüfungen auf, nach Häufigkeit. Sie prüft die Arbeitsfolge, die Zykluszeit gegen den "
                  "TAKT und die Qualitätspunkte. Sie prüft, ob Werkzeuge und Vorrichtungen stimmen. Und die "
                  "aktuelle SOP muss an jeder Station sein und verstanden werden. Ihre Liste läuft zu "
                  "Schichtbeginn, jede Stunde, bei jedem Modellwechsel und am Ende. Was stünde auf Ihrer?",
    },
    {
        "key": "p09", "num": 9, "title": "Visuelles Management",
        "points": [("Plan gegen Ist, jede Stunde", "Plan gegen Ist"),
                   ("Qualität, Stillstand, offene Maßnahmen", "Erstdurchlaufquote"),
                   ("Sehen, reagieren, erfassen, nachverfolgen", "Jede rote Zahl")],
        "example": "10 bis 11 Uhr: Plan 120 TV, Ist 98. Rot.",
        "example_cue": "Um elf Uhr",
        "script": "Machen Sie die Linie auf einen Blick lesbar. Plan gegen Ist, jede Stunde. "
                  "Erstdurchlaufquote, Hauptfehler, Stillstandsgründe und offene Maßnahmen mit "
                  "Verantwortlichen. Aber eine Tafel ist keine Dekoration. Jede rote Zahl muss eine "
                  "Reaktion auslösen. Sehen, reagieren, erfassen und nachverfolgen. Um elf Uhr wurde "
                  "Sunitas Tafel rot. Plan, hundertzwanzig TV. Ist, achtundneunzig. Was sollte sie zuerst "
                  "tun?",
    },
    {
        "key": "p10", "num": 10, "title": "Reaktion auf Abweichungen",
        "points": [("Erkennen, eindämmen, rufen", "Erkennen Sie die Lücke"),
                   ("Korrigieren und bestätigen", "Korrigieren Sie den Prozess"),
                   ("Verhindern und teilen", "Dann verhindern Sie es")],
        "example": "Stufe 1: das Team behebt es. Stufe 2: Unterstützung rufen. Stufe 3: an die Leitung "
                   "eskalieren.",
        "example_cue": "Es gibt drei Stufen",
        "script": "Folgen Sie einer klaren Reaktion. Erkennen Sie die Lücke, dämmen Sie sie für den Kunden "
                  "ein, und rufen Sie Unterstützung. Korrigieren Sie den Prozess, und bestätigen Sie die "
                  "Menge. Dann verhindern Sie es, und teilen Sie das Gelernte. Es gibt drei Stufen. Stufe "
                  "eins, das Team behebt es. Stufe zwei, Qualität, Technik oder Instandhaltung rufen. Stufe "
                  "drei, Sicherheits- oder Kundenrisiko, sofort eskalieren. Welche Stufe hatte Sunita?",
    },
    {
        "key": "p11", "num": 11, "title": "Sunitas rote Stunde",
        "points": [("Menge: 98 statt 120 pro Stunde", "Die Menge war auf"),
                   ("Erstdurchlaufquote: 98,5 % auf 95,8 %", "Die Erstdurchlaufquote"),
                   ("Arbeit staut sich vor dem Test", "Und Arbeit staute sich")],
        "example": "Es begann direkt nach dem Modellwechsel um 10 Uhr.",
        "example_cue": "Alles begann",
        "script": "Das sah sie. Die Menge war auf achtundneunzig TV pro Stunde gefallen, bei einem Plan von "
                  "hundertzwanzig. Die Erstdurchlaufquote war um fast drei Punkte gesunken. Und Arbeit "
                  "staute sich vor der Teststation. Drei Zahlen, alle in die falsche Richtung. Alles begann "
                  "direkt nach dem Modellwechsel um zehn Uhr. Würden Sie zuerst zur Teststation gehen?",
    },
    {
        "key": "p12", "num": 12, "title": "Eindämmen, dann hingehen und schauen",
        "points": [("Verdächtige TV sperren", "sperrte sie"),
                   ("Die Engpassstation finden", "fand den Engpass"),
                   ("Methode mit Standard vergleichen", "verglich die Methode")],
        "example": "Station 6: beim neuen Modell lief das Panelkabel anders, und die Werker bogen es von "
                   "Hand.",
        "example_cue": "An Station sechs",
        "script": "Noch nicht. Zuerst sperrte sie jeden verdächtigen TV seit zehn Uhr. Kunde geschützt. "
                  "Dann ging sie die Linie ab und fand den Engpass vor dem Test. Sie verglich die Methode "
                  "mit dem Standard, an jeder Station. An Station sechs lief das Panelkabel des neuen "
                  "Modells anders. Die Vorrichtung führte noch den alten Weg. Also bogen die Werker das "
                  "Kabel von Hand, und manches saß nicht richtig. War das Stufe eins?",
    },
    {
        "key": "p13", "num": 13, "title": "Rufen, korrigieren, bestätigen",
        "points": [("Stufe 2: die Technik rufen", "Sie rief die Technik"),
                   ("Vorrichtung korrigieren, SOP aktualisieren", "passte die Kabelführung"),
                   ("Über mehrere Zyklen bestätigen", "bestätigte es")],
        "example": "Um 1 Uhr nachmittags: 120 TV pro Stunde, Erstdurchlaufquote 98,6 %.",
        "example_cue": "Um ein Uhr",
        "script": "Es war Stufe zwei. Sie rief die Technik, mit Fakten, Fotos und den defekten Einheiten. "
                  "Die Technik passte die Kabelführung für das neue Modell an, und die SOP wurde "
                  "aktualisiert. Sunita bestätigte es über mehrere Zyklen, nicht nur mit einem guten TV. Um "
                  "ein Uhr lief die Linie wieder mit hundertzwanzig pro Stunde. Die Erstdurchlaufquote lag "
                  "bei achtundneunzig Komma sechs. Wer sorgte dafür, dass jede Schicht es wusste?",
    },
    {
        "key": "p14", "num": 14, "title": "Menschen entwickeln",
        "points": [("Erklären, zeigen, üben, prüfen", "Erklären, vorführen"),
                   ("Kritische Fähigkeiten zertifizieren", "Zertifizieren Sie kritische Fähigkeiten"),
                   ("Für Vertretung querschulen", "Schulen Sie quer")],
        "example": "Sunita schulte zwei Werker auf die neue Kabelführung vor der Nachtschicht.",
        "example_cue": "Sunita schulte",
        "script": "Ein Hancho baut Fähigkeiten auf, keine Abhängigkeit. Nutzen Sie einen einfachen "
                  "Schulungsrhythmus. Erklären, vorführen, üben lassen, dann prüfen. Zertifizieren Sie "
                  "kritische Fähigkeiten, bevor jemand allein arbeitet. Schulen Sie quer, damit ein Ausfall "
                  "die Linie nicht stoppt. Und coachen Sie Problemlösen, nicht nur die Arbeit. Sunita "
                  "schulte zwei Werker auf die neue Kabelführung, bevor die Nachtschicht begann. Könnte "
                  "Ihre Linie ohne Sie laufen?",
    },
    {
        "key": "p15", "num": 15, "title": "Messen, dann starten",
        "points": [("KPI stündlich, täglich, wöchentlich", "Prüfen Sie Menge"),
                   ("Auditieren zum Coachen, nicht zum Beschuldigen", "Auditieren Sie zum Coachen"),
                   ("Ein 30-Tage-Plan", "Hier ist ein Dreißig-Tage-Plan")],
        "example": "Woche 1 Rollen · Woche 2 Stundentafel · Woche 3 Fähigkeiten · Woche 4 Audit und Prüfung.",
        "example_cue": "Hier ist ein Dreißig-Tage-Plan",
        "script": "Messen Sie Ergebnisse und Disziplin. Prüfen Sie Menge und Stillstand stündlich, Qualität "
                  "täglich, und Fähigkeiten und Kaizen wöchentlich. Eine grüne Zahl ohne Disziplin hält "
                  "nicht. Auditieren Sie zum Coachen, nicht um Menschen zu erwischen. Hier ist ein "
                  "Dreißig-Tage-Plan. Woche eins, Rollen und Führungs-Standardarbeit festlegen. Woche zwei, "
                  "die Stundentafel starten. Woche drei, Fähigkeiten und Coaching. Woche vier, Audit und "
                  "Prüfung. Mit welcher Woche starten Sie?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Teamleiter", "sub": "班長", "icon": "person", "with": 0},
        {"label": "Ein System", "icon": "gear", "with": 1},
        {"label": "Am Gemba", "icon": "walk", "tone": "good", "with": 2}]},
    "p02": {"type": "steps", "items": [
        {"label": "Standard?", "with": 0}, {"label": "Ist?", "with": 0},
        {"label": "Lücke und Ursache?", "with": 1}, {"label": "Handeln und verhindern", "with": 2}]},
    "p03": {"type": "versus", "items": [
        {"label": "Führung fern", "sub": "Lücke am nächsten Morgen gefunden", "icon": "clock", "tone": "bad", "with": 0},
        {"label": "Hancho an der Linie", "sub": "Lücke in dieser Stunde gefunden", "icon": "person", "tone": "good", "with": 1}]},
    "p04": {"type": "icons", "items": [
        {"label": "Sicherheit", "icon": "shield", "with": 0},
        {"label": "Qualität", "icon": "check", "with": 0},
        {"label": "Lieferung", "icon": "calendar", "with": 1},
        {"label": "Kosten", "icon": "scale", "with": 1},
        {"label": "Menschen", "icon": "person", "with": 2},
        {"label": "Prozess", "icon": "clipboard", "with": 2}]},
    "p05": {"type": "flow", "items": [
        {"label": "Bereitschaft", "sub": "Menschen, Material, Werkzeuge", "icon": "clipboard", "with": 0},
        {"label": "Briefing", "sub": "Ziel, Warnungen, Erkenntnisse", "icon": "person", "with": 1},
        {"label": "Anlaufprüfungen", "sub": "Erstteil", "icon": "check", "tone": "good", "with": 2}]},
    "p06": {"type": "timeline", "items": [
        {"label": "Plan gegen Ist", "sub": "Stündlich", "icon": "clock", "with": 0},
        {"label": "Reagieren, coachen", "sub": "Ganze Schicht", "icon": "hand", "with": 1},
        {"label": "Übergabe", "sub": "Schichtende", "icon": "clipboard", "tone": "good", "with": 3}]},
    "p07": {"type": "icons", "items": [
        {"label": "Beobachten", "icon": "search", "with": 0},
        {"label": "Sprechen", "icon": "person", "with": 1},
        {"label": "Fragen, nicht anweisen", "icon": "key", "tone": "good", "with": 2}]},
    "p08": {"type": "doc", "items": [
        {"label": "Schichtbeginn: Bereitschaft", "icon": "calendar", "with": "example"},
        {"label": "Stündlich: Plan gegen Ist", "icon": "clock", "with": "example"},
        {"label": "Modellwechsel: Erstteil", "icon": "check", "with": "example"},
        {"label": "Schichtende: Übergabe", "icon": "clipboard", "with": "example"}]},
    "p09": {"type": "bars", "label": "", "note": "10–11 Uhr: Plan gegen Ist", "with": "example", "items": [
        {"label": "Plan", "value": 120, "tone": "good", "with": "example"},
        {"label": "Ist", "value": 98, "tone": "bad", "with": "example"}]},
    "p10": {"type": "ladder", "top": "STUFE 3", "bottom": "STUFE 1", "items": [
        {"label": "Sicherheits- oder Kundenrisiko: sofort eskalieren", "icon": "warning", "tone": "bad", "with": "example"},
        {"label": "Unterstützungsbereiche rufen", "icon": "person", "with": "example"},
        {"label": "Das Team stellt den Standard wieder her", "icon": "hand", "tone": "good", "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "98 statt 120 pro Stunde", "icon": "chartDown", "tone": "bad", "with": 0},
        {"label": "FPY 98.5% → 95.8%", "icon": "test", "tone": "bad", "with": 1},
        {"label": "WIP vor dem Test", "icon": "stack", "tone": "bad", "with": 2}]},
    "p12": {"type": "flow", "items": [
        {"label": "Verdächtige TV sperren", "icon": "lock", "with": 0},
        {"label": "Den Engpass finden", "icon": "search", "with": 1},
        {"label": "Station 6: Kabelweg geändert", "icon": "wrench", "tone": "bad", "with": "example"}]},
    "p13": {"type": "compare", "before": {"label": "11 Uhr", "value": 98}, "after": {"label": "1 Uhr nachmittags", "value": 120},
            "unit": "TV pro Stunde", "note": "Erstdurchlaufquote wieder bei 98,6 %", "with": "example"},
    "p14": {"type": "steps", "items": [
        {"label": "Erklären", "with": 0}, {"label": "Vorführen", "with": 0},
        {"label": "Üben", "with": 0}, {"label": "Prüfen", "with": 1}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Rollen, Führungs-Standardarbeit", "sub": "Woche 1", "icon": "clipboard", "with": 2},
        {"label": "Stundentafel", "sub": "Woche 2", "icon": "chartUp", "with": 2},
        {"label": "Fähigkeiten, Coaching", "sub": "Woche 3", "icon": "person", "with": 2},
        {"label": "Audit, Prüfung", "sub": "Woche 4", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Die Aufgabe eines Hancho ist vor allem…",
        "options": ["Am Tagesende den Schichtbericht ausfüllen",
                    "Am Gemba führen: den Standard halten, auf Lücken reagieren, Menschen entwickeln",
                    "Selbst die schwerste Station übernehmen, jede Schicht"],
        "correct": 1,
        "explanation": "Ein Hancho führt dort, wo Wert entsteht: er schützt den Standard, reagiert schnell auf "
                       "Abweichungen und baut die Fähigkeiten des Teams auf. Berichte und Stationsvertretung "
                       "sind nicht der Kern der Rolle.",
        "q_script": "Kurzer Check. Was ist die Hauptaufgabe eines Hancho? Nehmen Sie sich kurz Zeit.",
        "a_script": "Die zweite. Am Gemba führen. Den Standard halten, auf Lücken reagieren und Ihre Leute "
                    "entwickeln.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Die Stundentafel wird rot, und verdächtige Einheiten könnten ein Sicherheitsrisiko "
                    "haben. Welche Reaktionsstufe?",
        "options": ["Stufe 1: das Team behebt es still",
                    "Stufe 2: die Instandhaltung rufen, wenn sie Zeit hat",
                    "Stufe 3: eindämmen und sofort an die Leitung eskalieren"],
        "correct": 2,
        "explanation": "Sicherheits- oder Kundenrisiko ist Stufe 3: Einheiten eindämmen und sofort eskalieren. "
                       "Warten Sie nicht, ob das Team es schafft.",
        "q_script": "Noch eine, diesmal ein Szenario. Die Stundentafel wird rot, und verdächtige Einheiten "
                    "könnten ein Sicherheitsrisiko haben. Welche Reaktionsstufe ist es? Überlegen Sie kurz.",
        "a_script": "Stufe drei. Dämmen Sie die Einheiten ein, und eskalieren Sie sofort an die Leitung. "
                    "Sicherheitsrisiken warten nie.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
