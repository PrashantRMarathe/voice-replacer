"""jidoka in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh jidoka_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "jd_de"
NAME = "jidoka_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Sakichi Toyoda": "Sakitschi Tojoda",
    "Poka Yoke": "Poka Joke",
    "Jidoka": "Dschidoka",
    "Kaizen": "Kaisen",
    "Andon": "Andon",
    "PFMEA": "pe eff emm e a",
    "SOP": "ess o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Der Dosierer lief die ganze Nacht perfekt. Nur war seine Düse halb verstopft. Am Morgen "
    "hatten hundertvierzig Patientenmonitore eine zu dünne Dichtung. Kommt Ihnen das bekannt "
    "vor? In dieser Lektion lernen Sie Jidoka kennen, Automatisierung mit menschlicher Note. "
    "Sie sehen, wie ein Prozess ein Problem erkennt, selbst stoppt und Hilfe ruft, bevor sich "
    "Fehler stapeln. Wir begleiten Anjali, Prozessingenieurin an einer Linie für "
    "Patientenmonitore."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Definieren Sie zuerst das Normale, damit der Prozess weiß, "
    "wie Abweichung aussieht. Erkennen, stoppen und eindämmen Sie an der Quelle, und geben "
    "Sie nie einen Fehler weiter. Und behandeln Sie jeden Stopp als Lektion, beheben Sie die "
    "Grundursache. Ihre Aufgabe für diese Woche. Wählen Sie einen automatischen Prozess, und "
    "notieren Sie, was ihn stoppen sollte. Gut gemacht, Lektion abgeschlossen. Als Nächstes "
    "lernen Sie Kaizen kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Jidoka ist",
        "points": [("Eine Abweichung erkennen", "einen abweichenden Zustand"),
                   ("Stoppen oder eindämmen", "stoppt oder dämmt"),
                   ("Korrigieren, dann verhindern", "Dann korrigieren Menschen")],
        "example": "Anjalis Dosierer versiegelt die Frontblende jedes Patientenmonitors.",
        "example_cue": "Anjalis Aufgabe",
        "script": "Jidoka wird oft Automatisierung mit menschlicher Note genannt. Es bedeutet einen "
                  "Prozess, der einen abweichenden Zustand selbst erkennt. Er stoppt oder dämmt die Arbeit "
                  "ein, damit kein Fehler weiterwandert. Dann korrigieren Menschen und verhindern eine "
                  "Wiederholung. Anjalis Aufgabe war ein Klebstoff-Dosierer. Er versiegelt die Frontblende "
                  "jedes Patientenmonitors. Was ändert sich, wenn Sie Jidoka ergänzen?",
    },
    {
        "key": "p02", "num": 2, "title": "Ohne Jidoka und mit",
        "points": [("Fehler wandern weiter oder werden an der Quelle gefangen", "Ohne Jidoka kann ein Fehler"),
                   ("Zögern oder klare Stopp-Regeln", "Menschen zögern"),
                   ("Prüfung oder eingebaute Qualität", "die Qualität hängt")],
        "example": "Ohne es: 140 dünne Dichtungen, am nächsten Morgen beim Dichtheitstest gefunden.",
        "example_cue": "Ohne es",
        "script": "Ohne Jidoka kann ein Fehler viele Stationen durchlaufen, bevor ihn jemand sieht. "
                  "Menschen zögern zu stoppen, weil niemand es erlaubt hat. Sortieren wird Routine, und die "
                  "Qualität hängt an der Endkontrolle. Mit Jidoka wird er nahe der Quelle gefangen. Die "
                  "Stopp-Regeln sind klar, und Qualität ist eingebaut. Ohne es fand Anjali am nächsten "
                  "Morgen hundertvierzig dünne Dichtungen. Wo begann diese Idee?",
    },
    {
        "key": "p03", "num": 3, "title": "Woher es kommt",
        "points": [("Der automatische Webstuhl von Sakichi Toyoda", "Es geht zurück auf Sakichi Toyoda"),
                   ("Er stoppte, wenn ein Faden riss", "stoppte selbst"),
                   ("Eine der zwei Säulen des TPS", "zwei Säulen")],
        "example": "Just-in-Time bewegt Material gut. Jidoka sorgt dafür, dass es Fehler nicht gut bewegt.",
        "example_cue": "Hier ist die Verbindung",
        "script": "Es geht zurück auf Sakichi Toyoda und seinen automatischen Webstuhl. Der Clou war nicht "
                  "das Tempo. Der Webstuhl stoppte selbst, sobald ein Faden riss, statt schlechten Stoff zu "
                  "weben. Diese Idee wurde eine der zwei Säulen des Toyota-Produktionssystems. Hier ist die "
                  "Verbindung. Just in time bewegt Material effizient. Jidoka sorgt dafür, dass Sie Fehler "
                  "nicht effizient bewegen. Heißt das weniger Menschen?",
    },
    {
        "key": "p04", "num": 4, "title": "Menschen bleiben wichtig",
        "points": [("Maschinen beobachten, Menschen denken", "Maschinen beobachten"),
                   ("Eine Person kann mehrere Maschinen betreuen", "kann eine Person"),
                   ("Urteil, Reparatur, Verbesserung", "für Urteil")],
        "example": "Anjalis Werkerin starrte die ganze Schicht auf die Raupe. Jetzt betreut sie zwei "
                   "Stationen.",
        "example_cue": "Anjalis Werkerin",
        "script": "Nein. Jidoka ersetzt keine Menschen. Maschinen beobachten, Menschen denken. Weil die "
                  "Maschine meldet, wenn sie Hilfe braucht, kann eine Person mehrere Maschinen betreuen. "
                  "Ihre Zeit geht für Urteil, Reparatur, Standards und Verbesserung. Anjalis Werkerin "
                  "starrte die ganze Schicht auf die Klebstoffraupe. Jetzt betreut sie zwei Stationen und "
                  "löst Probleme. Wie funktioniert der Zyklus?",
    },
    {
        "key": "p05", "num": 5, "title": "Schritt 1: Erkennen",
        "points": [("Zuerst das Normale definieren", "das Normale definieren"),
                   ("Dann die Abweichung erfassen", "erfassen Sie, wenn"),
                   ("Sensoren, Prüfungen, Tests, Überwachung", "Sensoren, Kameras")],
        "example": "Normale Raupe: 2,0 bis 2,4 mm breit, ohne Lücken.",
        "example_cue": "Für Anjali",
        "script": "Der Zyklus hat vier Schritte. Erkennen, stoppen, korrigieren und verhindern. Zuerst "
                  "müssen Sie das Normale definieren. Ohne zu wissen, wie gut aussieht, erkennen Sie keine "
                  "Abweichung. Dann erfassen Sie, wenn der Prozess davon abdriftet. Sensoren, Kameras, "
                  "Tests und Werkerprüfungen können das. Für Anjali war normal eine Raupe von zwei bis zwei "
                  "Komma vier Millimetern, ohne Lücken.",
    },
    {
        "key": "p06", "num": 6, "title": "Schritte 2 bis 4: Stoppen, Korrigieren, Verhindern",
        "points": [("Je nach Risiko stoppen oder eindämmen", "Stoppen oder dämmen Sie ein"),
                   ("Korrigieren: Standard wiederherstellen", "Korrigieren heißt"),
                   ("Verhindern: Grundursache beseitigen", "Verhindern heißt")],
        "example": "Korrigieren ist nicht Verhindern. Eine gereinigte Düse kann wieder verstopfen.",
        "example_cue": "Merken Sie sich",
        "script": "Stoppen oder dämmen Sie ein, passend zum Risiko. Das kann ein Maschinenstopp sein, eine "
                  "Stationssperre, ein gesperrtes Teil oder eine blockierte Buchung. Korrigieren heißt, den "
                  "freigegebenen Standard wiederherzustellen und das betroffene Produkt zu finden. "
                  "Verhindern heißt, die Grundursache zu beseitigen und den Standard zu aktualisieren. "
                  "Merken Sie sich: Korrigieren ist nicht Verhindern. Eine gereinigte Düse kann morgen "
                  "wieder verstopfen. Was unterscheidet das von Automatisierung?",
    },
    {
        "key": "p07", "num": 7, "title": "Jidoka gegenüber reiner Automatisierung",
        "points": [("Automatisierung macht die Arbeit", "Reine Automatisierung"),
                   ("Jidoka beurteilt die Arbeit auch", "Jidoka ergänzt"),
                   ("Schnelle Maschinen machen schnelle Fehler", "eine schnelle Maschine")],
        "example": "Anjalis Dosierer: vollautomatisch, aber blind. Er dosierte die ganze Nacht weiter.",
        "example_cue": "Anjalis Dosierer",
        "script": "Reine Automatisierung macht die Arbeit. Jidoka ergänzt ein Urteil über die Arbeit. Eine "
                  "normale Maschine läuft weiter, außer etwas klemmt. Eine Maschine mit Jidoka stoppt bei "
                  "einer definierten Abweichung und ruft einen Menschen. Und hier ist die Gefahr. Eine "
                  "schnelle Maschine macht schnell Fehler. Anjalis Dosierer war vollautomatisch, aber "
                  "blind. Er dosierte die ganze Nacht dünne Raupen. Welche Prinzipien sollten Sie leiten?",
    },
    {
        "key": "p08", "num": 8, "title": "Kernprinzipien",
        "points": [("Kein Fehler wird weitergegeben", "Kein Fehler wird weitergegeben"),
                   ("Keine Abweichung wird versteckt", "Keine Abweichung wird versteckt"),
                   ("Keine Wiederholung ohne Maßnahme", "Kein wiederholtes Problem")],
        "example": "Drei Fragen: Was ist normal? Wie erkennen wir eine Abweichung? Was passiert dann?",
        "example_cue": "Stellen Sie drei Fragen",
        "script": "Merken Sie sich drei kurze Regeln. Kein Fehler wird weitergegeben. Keine Abweichung wird "
                  "versteckt. Kein wiederholtes Problem wird ohne Maßnahme hingenommen. Nutzen Sie "
                  "Maschinenerkennung und menschliches Urteil zusammen. Und starten Sie nie neu, ohne etwas "
                  "zu lernen. Jeder Stopp sollte den Prozess etwas stärker machen. Stellen Sie drei Fragen "
                  "zu jedem Prozess. Was ist normal? Wie erkennen wir eine Abweichung? Und was genau "
                  "passiert danach? Können Sie sie für Ihre Linie beantworten?",
    },
    {
        "key": "p09", "num": 9, "title": "Andon",
        "points": [("Grün: normal", "Grün bedeutet"),
                   ("Gelb: Hilfe nötig", "Gelb bedeutet"),
                   ("Rot: stoppen, eindämmen, eskalieren", "Rot bedeutet")],
        "example": "Anjalis Regel: der Teamleiter beantwortet ein Gelb innerhalb von zwei Minuten.",
        "example_cue": "An Anjalis Linie",
        "script": "Andon macht Probleme sichtbar, mit Licht, Ton oder Bildschirm. Grün bedeutet normal, "
                  "also nach Standard weiterarbeiten. Gelb bedeutet, Hilfe ist nötig, und eine "
                  "Führungskraft kommt schnell. Rot bedeutet eine kritische Abweichung. Sicher stoppen, "
                  "eindämmen und eskalieren. Dann das letzte bekannte Gutteil finden. An Anjalis Linie "
                  "beantwortet der Teamleiter jedes Gelb innerhalb von zwei Minuten. Wie schnell kommt "
                  "Hilfe an Ihre Linie?",
    },
    {
        "key": "p10", "num": 10, "title": "Eine Andon-Kultur",
        "points": [("Ein Ruf ist eine nützliche Information", "Ein echter Andon-Ruf"),
                   ("Nie einen Stopp bestrafen", "Bestrafen Sie nie"),
                   ("Rufe können zuerst steigen", "steigen die Rufe oft")],
        "example": "Andon-Rufe verdoppelten sich im ersten Monat und halbierten sich bis zum dritten.",
        "example_cue": "An Anjalis Linie",
        "script": "Andon funktioniert nur, wenn Menschen ihm vertrauen. Ein echter Andon-Ruf ist eine "
                  "nützliche Information, keine Störung. Bestrafen Sie nie einen Stopp, sonst verstecken "
                  "Menschen Probleme, um die Menge zu schützen. Und rechnen Sie mit einer Überraschung. "
                  "Werden Probleme sichtbar, steigen die Rufe oft zuerst. An Anjalis Linie verdoppelten "
                  "sich die Andon-Rufe im ersten Monat. Bis zum dritten Monat halbierten sie sich, weil "
                  "Ursachen behoben wurden. Würde Ihr Team rufen?",
    },
    {
        "key": "p11", "num": 11, "title": "Die stärksten Maßnahmen zuerst",
        "points": [("Beseitigen, oder konstruktiv verhindern", "Zuerst beseitigen"),
                   ("Sofort erkennen und stoppen", "Als Nächstes erkennen"),
                   ("Warnungen und Prüfung zuletzt", "Warnungen kommen")],
        "example": "Gutes Poka Yoke: einfach, nah an der Quelle, schwer zu umgehen, leicht zu prüfen.",
        "example_cue": "Ein gutes Poka Yoke",
        "script": "Nutzen Sie die stärkste mögliche Maßnahme. Zuerst beseitigen Sie die Fehlermöglichkeit, "
                  "oder verhindern sie konstruktiv. Als Nächstes erkennen Sie den Fehler und stoppen "
                  "sofort. Warnungen kommen danach, und spätere Prüfung nur als zusätzliche Abwehr. Ein "
                  "gutes Poka Yoke ist einfach, nah an der Quelle und schwer zu umgehen. Und es lässt sich "
                  "jede Schicht leicht prüfen. Was hat Anjali also gebaut?",
    },
    {
        "key": "p12", "num": 12, "title": "Anjalis Jidoka-Station",
        "points": [("Ein Sensor misst jede Raupe", "der jede Raupe"),
                   ("Außerhalb der Grenzen: Dosierer stoppt", "stoppt der Dosierer"),
                   ("Andon, und Sperre bis zum letzten Gutteil", "Andon ruft")],
        "example": "Erster echter Stopp: ein Monitor betroffen, nicht 140.",
        "example_cue": "Der erste echte Stopp",
        "script": "Sie ergänzte einen Kamerasensor, der jede Raupe direkt nach dem Dosieren misst. Liegt "
                  "die Breite außerhalb der Grenzen, stoppt der Dosierer, und das Teil wird gesperrt. Andon "
                  "ruft den Teamleiter. Alles seit dem letzten Gutteil wird geprüft. Der erste echte Stopp "
                  "kam zwei Wochen später. Ein Monitor war betroffen, nicht hundertvierzig. Aber warum "
                  "verstopfte die Düse?",
    },
    {
        "key": "p13", "num": 13, "title": "Grundursache nach dem Stopp",
        "points": [("Stoppen zeigt; Analyse verbessert", "Stoppen zeigt"),
                   ("Warum fragen, mit Belegen", "Warum verstopfte die Düse"),
                   ("Beheben, dann standardisieren", "Also ergänzte sie")],
        "example": "Klebstoff härtete in Pausen in der Düse aus. Kein Spülschritt im Standard.",
        "example_cue": "Klebstoff härtete",
        "script": "Stoppen zeigt ein Problem. Die Ursachenanalyse macht daraus eine Verbesserung. Warum "
                  "verstopfte die Düse? Klebstoff härtete in den Pausen darin aus. Warum? Es gab keinen "
                  "Spülschritt nach einer Pause. Warum? Der Standard deckte Pausen nie ab. Also ergänzte "
                  "sie eine automatische Spülung nach jeder Pause und eine Drucküberwachung. Auch die PFMEA "
                  "und die SOP wurden aktualisiert. Wie würden Sie Erfolg messen?",
    },
    {
        "key": "p14", "num": 14, "title": "Das Richtige messen",
        "points": [("Erstdurchlaufquote und Durchschlupf", "Beobachten Sie die Erstdurchlaufquote"),
                   ("Andon-Reaktionszeit", "Die Andon-Reaktionszeit"),
                   ("Wiederholte Abweichungen", "wiederholte Abweichungen")],
        "example": "Erstdurchlaufquote: 97,5 % → 99,0 %. Durchschlupf: null in 90 Tagen.",
        "example_cue": "Anjalis Ergebnisse",
        "script": "Messen Sie Reaktion und Wiederholung, nicht nur die Zahl der Stopps. Beobachten Sie die "
                  "Erstdurchlaufquote und den Durchschlupf zum Kunden. Verfolgen Sie die "
                  "Andon-Reaktionszeit, vom Ruf bis zur Hilfe. Und beobachten Sie wiederholte Abweichungen. "
                  "Sie sollten mit der Zeit sinken. Anjalis Ergebnisse waren klar. Die Erstdurchlaufquote "
                  "stieg um eineinhalb Punkte, auf neunundneunzig Prozent. Keine einzige Dichtung rutschte "
                  "in neunzig Tagen durch. Wer lässt das alles funktionieren?",
    },
    {
        "key": "p15", "num": 15, "title": "Rollen und Fahrplan",
        "points": [("Werker erkennen, rufen und stoppen", "Werker erkennen"),
                   ("Führungskräfte reagieren und stellen wieder her", "Führungskräfte reagieren"),
                   ("Eine Einführung in 30-60-90 Tagen", "Führen Sie es in")],
        "example": "Tage 0–30: Abweichung definieren. 31–60: erkennen und schulen. 61–90: "
                   "Hauptwiederholungen beheben.",
        "example_cue": "In den ersten dreißig Tagen",
        "script": "Jeder hat eine Rolle. Werker erkennen, rufen und stoppen. Führungskräfte reagieren "
                  "schnell und stellen den Standard wieder her. Die Instandhaltung hält Sensoren in "
                  "Betrieb, die Leitung schützt das Recht zu stoppen. Führen Sie es in neunzig Tagen ein. "
                  "In den ersten dreißig Tagen definieren Sie Abweichung und wählen einen Pilot. Dann "
                  "Erkennung und Schulung. Schließlich beheben Sie die häufigsten Wiederholungen.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Erkennen", "icon": "sensor", "with": 0},
        {"label": "Stoppen", "icon": "lock", "with": 1},
        {"label": "Korrigieren", "icon": "wrench", "with": 2},
        {"label": "Verhindern", "icon": "shield", "tone": "good", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Ohne Jidoka", "sub": "Fehler wandern, spät gefunden", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Mit Jidoka", "sub": "An der Quelle gefangen", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 140, "icon": "warning", "label": "dünne Dichtungen am Morgen",
                 "unit": "beim Dichtheitstest gefunden", "with": "example"}},
    "p03": {"type": "timeline", "items": [
        {"label": "Webstuhl stoppt bei gerissenem Faden", "sub": "Anfang der 1900er", "icon": "gear", "with": 0},
        {"label": "Säule des TPS", "sub": "TPS", "icon": "stack", "with": 2},
        {"label": "Keine Fehler weitergegeben", "sub": "Heute", "icon": "shield", "tone": "good", "with": "example"}]},
    "p04": {"type": "versus", "items": [
        {"label": "Eine Maschine beobachten", "sub": "Ganze Schicht", "icon": "search", "tone": "bad", "with": 0},
        {"label": "Zwei Stationen betreuen", "sub": "Und Probleme lösen", "icon": "person", "tone": "good", "with": "example"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Normal definieren", "icon": "clipboard", "with": 0},
        {"label": "Abdrift erfassen", "icon": "sensor", "with": 1},
        {"label": "Tests, Überwachung", "icon": "test", "with": 2}],
        "then": {"type": "stat", "value": 2.0, "decimals": 1, "suffix": "–2.4 mm", "icon": "pin", "label": "normale Raupenbreite",
                 "unit": "keine Lücken", "with": "example"}},
    "p06": {"type": "steps", "items": [
        {"label": "Stoppen oder eindämmen", "with": 0},
        {"label": "Korrigieren", "with": 1},
        {"label": "Verhindern", "with": 2}]},
    "p07": {"type": "versus", "items": [
        {"label": "Reine Automatisierung", "sub": "Dosierte die ganze Nacht", "icon": "gear", "tone": "bad", "with": 0},
        {"label": "Jidoka", "sub": "Stoppt und ruft", "icon": "sensor", "tone": "good", "with": 1}]},
    "p08": {"type": "icons", "items": [
        {"label": "Kein Fehler weitergegeben", "icon": "lock", "with": 0},
        {"label": "Keine Abweichung versteckt", "icon": "search", "with": 1},
        {"label": "Keine Wiederholung ohne Maßnahme", "icon": "key", "tone": "good", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Grün: normal", "sub": "Nach Standard weiter", "icon": "check", "tone": "good", "with": 0},
        {"label": "Gelb: Hilfe", "sub": "Führungskraft kommt schnell", "icon": "person", "with": 1},
        {"label": "Rot: Stopp", "sub": "Eindämmen, eskalieren", "icon": "warning", "tone": "bad", "with": 2}]},
    "p10": {"type": "bars", "label": "", "note": "Andon-Rufe pro Woche", "with": 2, "items": [
        {"label": "Vorher", "value": 10, "with": 2},
        {"label": "Monat 1", "value": 20, "with": "example"},
        {"label": "Monat 3", "value": 10, "tone": "good", "with": "example"}]},
    "p11": {"type": "ladder", "top": "AM STÄRKSTEN", "bottom": "AM SCHWÄCHSTEN", "items": [
        {"label": "Beseitigen oder verhindern", "icon": "shape", "with": 0},
        {"label": "Erkennen und stoppen", "icon": "sensor", "with": 1},
        {"label": "Warnen", "icon": "warning", "with": 2},
        {"label": "Später prüfen", "icon": "search", "with": 2}]},
    "p12": {"type": "flow", "items": [
        {"label": "Sensor prüft jede Raupe", "icon": "sensor", "with": 0},
        {"label": "Dosierer stoppt", "icon": "lock", "with": 1},
        {"label": "Andon, Sperre bis zum letzten Gutteil", "icon": "warning", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Vorher", "value": 140}, "after": {"label": "Mit Jidoka", "value": 1},
                 "unit": "betroffene Monitore pro Düsenproblem", "with": "example"}},
    "p13": {"type": "steps", "items": [
        {"label": "Düse verstopft", "with": 1},
        {"label": "Klebstoff in Pausen ausgehärtet", "with": "example"},
        {"label": "Kein Spülschritt", "with": "example"},
        {"label": "Autospülung + Drucküberwachung", "with": 2}]},
    "p14": {"type": "compare", "before": {"label": "Vorher", "value": 97.5}, "after": {"label": "Nachher", "value": 99.0},
            "decimals": 1, "suffix": "%", "unit": "Erstdurchlaufquote", "note": "Null Durchschlupf in 90 Tagen", "with": "example"},
    "p15": {"type": "timeline", "items": [
        {"label": "Abweichung definieren, Pilot", "sub": "Tage 0–30", "icon": "clipboard", "with": 2},
        {"label": "Erkennen, schulen", "sub": "31–60", "icon": "sensor", "with": 2},
        {"label": "Hauptwiederholungen beheben", "sub": "61–90", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Was unterscheidet Jidoka von gewöhnlicher Automatisierung?",
        "options": ["Es läuft schneller",
                    "Es erkennt eine definierte Abweichung, stoppt und ruft einen Menschen",
                    "Es braucht keine Menschen"],
        "correct": 1,
        "explanation": "Automatisierung macht die Arbeit; Jidoka beurteilt sie auch. Es stoppt bei einer "
                       "definierten Abweichung und ruft menschliche Hilfe, damit sich Fehler nicht "
                       "vervielfachen.",
        "q_script": "Kurzer Check. Was unterscheidet Jidoka von gewöhnlicher Automatisierung? Nehmen Sie sich "
                    "kurz Zeit.",
        "a_script": "Die zweite. Es erkennt eine definierte Abweichung, stoppt selbst und ruft einen "
                    "Menschen. So vervielfachen sich Fehler nicht.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Eine Werkerin sieht eine abweichende Dichtung, aber die Linie liegt hinter dem Ziel. Was "
                    "sollte sie tun?",
        "options": ["Weitermachen und es am Schichtende melden",
                    "Andon rufen und das Teil sperren, wie es die Stopp-Regeln sagen",
                    "Es still selbst beheben und weitermachen"],
        "correct": 1,
        "explanation": "Kein Fehler weitergegeben, keine Abweichung versteckt. Andon rufen und das Teil sperren "
                       "schützt den Kunden, auch wenn die Menge zurückliegt.",
        "q_script": "Noch eine, ein Szenario. Eine Werkerin sieht eine abweichende Dichtung, aber die Linie "
                    "liegt hinter dem Ziel. Was sollte sie tun? Überlegen Sie kurz.",
        "a_script": "Andon rufen und das Teil sperren, genau wie die Stopp-Regeln sagen. Kein Fehler "
                    "weitergegeben, keine Abweichung versteckt, auch wenn die Menge zurückliegt.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
