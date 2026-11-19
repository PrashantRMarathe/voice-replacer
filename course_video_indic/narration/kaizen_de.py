"""kaizen in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh kaizen_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "kz_de"
NAME = "kaizen_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Low Cost Automation": "Lou Kost Otomeeschen",
    "Kaizen": "Kaisen",
    "Gemba": "Gemba",
    "Check": "tscheck",
    "Plan": "plän",
    "PDCA": "pe de ze a",
    "SDCA": "ess de ze a",
    "ECRS": "e ze err ess",
    "TAKT": "Takt",
    "SOP": "ess o pe",
    "Act": "äkt",
    "Do": "duh",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Jeder Monitor an Sureshs Linie wurde zweimal gewendet. Mit dem Bildschirm nach unten, "
    "dann wieder nach oben. Niemand fragte, warum. Man hatte es immer so gemacht. Kommt Ihnen "
    "das bekannt vor? In dieser Lektion lernen Sie Kaizen kennen, kontinuierliche "
    "Verbesserung. Sie sehen, wie kleine, getestete Änderungen von den Menschen an der Arbeit "
    "zu großen Ergebnissen werden. Wir begleiten Suresh, Linienleiter in der Monitormontage."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Kaizen ist eine tägliche Gewohnheit, kein einmaliges "
    "Ereignis. Testen Sie klein, messen Sie ehrlich, und prüfen Sie, dass nichts schlechter "
    "wurde. Und standardisieren Sie jeden Gewinn, als Startpunkt für den nächsten. Ihre "
    "Aufgabe für diese Woche. Fragen Sie einen Werker, was seine Arbeit schwer macht, und "
    "testen Sie eine kleine Lösung. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen "
    "Sie Low Cost Automation kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Kaizen bedeutet",
        "points": [("Veränderung zum Besseren", "Veränderung zum Besseren"),
                   ("Viele kleine, disziplinierte Änderungen", "viele kleine Änderungen"),
                   ("Von denen gemacht, die der Arbeit am nächsten sind", "Sie kommen von den Menschen")],
        "example": "Sureshs Linie: zweimal wenden, jeder Monitor, jede Einheit, jede Schicht.",
        "example_cue": "An Sureshs Linie",
        "script": "Kaizen ist ein japanisches Wort für Veränderung zum Besseren. In einer Fabrik bedeutet "
                  "es kontinuierliche Verbesserung durch viele kleine Änderungen. Sie kommen von den "
                  "Menschen, die der Arbeit am nächsten sind, jeden Tag. Nicht ein großes Projekt pro Jahr. "
                  "An Sureshs Linie wurde jeder Monitor in jeder Schicht zweimal gewendet. Das sind "
                  "Tausende schwere Hebungen pro Woche. Was macht eine Verbesserung also zum Kaizen?",
    },
    {
        "key": "p02", "num": 2, "title": "Was es zum Kaizen macht",
        "points": [("Kontinuierlich und von Menschen getragen", "Es ist kontinuierlich"),
                   ("Beginnt am Gemba", "Es beginnt am Gemba"),
                   ("Zuerst günstig, mit Daten belegt", "Es probiert zuerst"),
                   ("Endet in einem neuen Standard", "Und es endet")],
        "example": "Jeder verbesserte Standard ist die Basis für das nächste Kaizen.",
        "example_cue": "Dann beginnt der Zyklus",
        "script": "Ein paar Dinge zeichnen es aus. Es ist kontinuierlich und wird von Menschen getragen, "
                  "nicht nur von Ingenieuren. Es beginnt am Gemba, mit dem, was Sie wirklich sehen. Es "
                  "probiert zuerst günstige Ideen und prüft die Ergebnisse mit Daten. Und es endet in einem "
                  "neuen Standard, der besten Methode, die Sie heute kennen. Dann beginnt der Zyklus von "
                  "dieser neuen Basis aus neu. Welche Haltung braucht das?",
    },
    {
        "key": "p03", "num": 3, "title": "Die Kaizen-Haltung",
        "points": [("Jeder Prozess kann besser werden", "Jeder Prozess kann"),
                   ("Probleme sind zum Lernen da, nicht zum Beschuldigen", "Probleme sind"),
                   ("Kreativität vor Kapital", "Kreativität vor Kapital")],
        "example": "„Wir haben ihn immer gewendet“ ist genau der Satz, den Kaizen hinterfragt.",
        "example_cue": "Wir haben es immer",
        "script": "Es beginnt mit einer Überzeugung. Jeder Prozess kann besser werden, auch ein guter. "
                  "Probleme sind Chancen zum Lernen, keine Gründe für Schuld. Gehen Sie hin und schauen "
                  "Sie, bevor Sie entscheiden. Und nutzen Sie Kreativität vor Kapital. Eine "
                  "Klebebandmarkierung schlägt oft eine neue Maschine. Wir haben es immer so gemacht, ist "
                  "genau der Satz, den Kaizen hinterfragt. Wann haben Sie ihn zuletzt an Ihrer Linie "
                  "gehört?",
    },
    {
        "key": "p04", "num": 4, "title": "Arten von Kaizen",
        "points": [("Tages-Kaizen: Minuten bis Tage", "Das Tages-Kaizen"),
                   ("Punkt-Kaizen: ein bestimmter Verlust", "Das Punkt-Kaizen"),
                   ("Kaizen-Event: drei bis fünf Tage", "Ein Kaizen-Event"),
                   ("System-Kaizen: Fluss von Anfang bis Ende", "Das System-Kaizen")],
        "example": "Das doppelte Wenden: ein Punkt-Kaizen, getragen von Sureshs eigenem Team.",
        "example_cue": "Das doppelte Wenden",
        "script": "Kaizen gibt es in verschiedenen Größen. Das Tages-Kaizen ist klein und lokal, wie ein "
                  "Werkzeug näher zu legen. Das Punkt-Kaizen zielt auf einen bestimmten Verlust, in Stunden "
                  "oder Tagen. Ein Kaizen-Event bringt ein bereichsübergreifendes Team für drei bis fünf "
                  "Tage zusammen. Das System-Kaizen verbessert den Fluss über Abteilungen, über Wochen. Das "
                  "doppelte Wenden war ein Punkt-Kaizen, getragen von Sureshs eigenem Team. Welche Größe "
                  "passt zu Ihrem größten Schmerz?",
    },
    {
        "key": "p05", "num": 5, "title": "Kaizen läuft mit PDCA",
        "points": [("Plan: beobachten, definieren, Ursache finden", "Plan heißt"),
                   ("Do: ein kleiner, sicherer Versuch", "Do heißt"),
                   ("Check: mit der Ausgangslage vergleichen", "Check heißt"),
                   ("Act: standardisieren, oder lernen und wiederholen", "Act heißt")],
        "example": "SDCA hält den Standard. PDCA verbessert ihn.",
        "example_cue": "Sein Zwilling",
        "script": "Jedes Kaizen folgt dem PDCA. Plan heißt beobachten, die Lücke definieren und die Ursache "
                  "finden. Do heißt ein kleiner, sicherer Versuch. Check heißt, das Ergebnis mit "
                  "Ausgangslage und Ziel zu vergleichen. Act heißt standardisieren, oder lernen und neu "
                  "versuchen. Sein Zwilling ist das SDCA, das den Standard stabil hält. Starke Teams "
                  "wechseln zwischen beiden. Ohne PDCA ist eine Idee nur eine ungetestete Änderung. Wo "
                  "fangen Sie an?",
    },
    {
        "key": "p06", "num": 6, "title": "Am Gemba sehen",
        "points": [("Die Arbeit sehen, wie sie wirklich ist", "Beobachten Sie die Arbeit"),
                   ("Laufen, Greifen, Wenden zählen", "Zählen Sie Laufen"),
                   ("Fragen, was die Arbeit schwer macht", "Fragen Sie die Werker")],
        "example": "Nach unten wenden für den Fuß, nach oben für den Test. Zwei Hebungen eines "
                   "6-kg-Monitors.",
        "example_cue": "Sureshs Team sah es",
        "script": "Am Gemba, natürlich. Beobachten Sie die Arbeit, wie sie wirklich ist, nicht wie die SOP "
                  "sie beschreibt. Zählen Sie Laufen, Greifen, Suchen und Heben. Fragen Sie die Werker, was "
                  "ihre Arbeit schwer macht. Sureshs Team sah es sofort. Jeder Monitor ging mit dem "
                  "Bildschirm nach unten für den Fuß, dann wieder nach oben für den Test. Zwei Hebungen "
                  "eines sechs Kilo schweren Monitors, jedes Mal. Was würden Sie notieren?",
    },
    {
        "key": "p07", "num": 7, "title": "Das Problem definieren",
        "points": [("Symptom, dann die Fakten", "Beginnen Sie mit dem Symptom"),
                   ("Den Verlust messen", "Messen Sie den Verlust"),
                   ("Ein Ziel mit Termin", "Setzen Sie ein Ziel")],
        "example": "Zyklus 38 s gegenüber TAKT 35 s. 2 Wendungen pro Einheit. 15 verkratzte Panels pro "
                   "1.000.",
        "example_cue": "Sureshs Fakten",
        "script": "Beginnen Sie mit dem Symptom. Die Linie verfehlte ihr Stundenziel. Dann holen Sie die "
                  "Fakten. Messen Sie den Verlust, und trennen Sie Fakten von Meinungen. Sureshs Fakten "
                  "waren klar. Die Zykluszeit lag bei achtunddreißig Sekunden, gegenüber einem TAKT von "
                  "fünfunddreißig. Jedes Wenden riskierte einen Kratzer, und fünfzehn von tausend Panels "
                  "waren verkratzt. Setzen Sie ein Ziel mit Termin, ohne die Lösung. Was wäre Ihr Ziel?",
    },
    {
        "key": "p08", "num": 8, "title": "Ideen finden",
        "points": [("Zuerst die Werker fragen", "Fragen Sie zuerst die Werker"),
                   ("ECRS nutzen", "Nutzen Sie ECRS"),
                   ("Andere Linien anschauen", "Schauen Sie auf andere Linien")],
        "example": "Leela, eine Werkerin: „Warum den Fuß nicht montieren, solange der Monitor noch in der "
                   "Schale liegt?“",
        "example_cue": "Leela, eine Werkerin",
        "script": "Finden Sie jetzt Ideen, und zwar viele. Fragen Sie zuerst die Werker. Was macht diese "
                  "Arbeit schwer? Was würde einen Schritt streichen? Nutzen Sie ECRS, eliminieren, "
                  "kombinieren, umordnen und vereinfachen. Schauen Sie auf andere Linien und andere "
                  "Branchen. Leela, eine Werkerin der Nachtschicht, hatte die beste Idee. Warum den Fuß "
                  "nicht montieren, solange der Monitor noch mit dem Bildschirm nach unten in der Schale "
                  "liegt? Warum hatte sie vorher niemand gefragt?",
    },
    {
        "key": "p09", "num": 9, "title": "Die Idee wählen",
        "points": [("Sicherheit und Qualität sind K.-o.-Kriterien", "Sicherheit und Qualität"),
                   ("Wirkung, Aufwand, Kosten, Tempo bewerten", "Dann bewerten Sie"),
                   ("Sie muss eine bestätigte Ursache treffen", "Und die Idee muss")],
        "example": "Leelas Idee: hoch bei Wirkung, Aufwand und Kosten. Sie gewann.",
        "example_cue": "Leelas Idee",
        "script": "Wählen Sie mit einer einfachen Bewertungsmatrix. Sicherheit und Qualität sind "
                  "K.-o.-Kriterien. Dann bewerten Sie Wirkung, Aufwand, Kosten und Tempo. Und die Idee muss "
                  "eine bestätigte Ursache treffen, einfach genug für alle. Leelas Idee bekam hohe Werte "
                  "bei Wirkung, Aufwand und Kosten. Sie gewann klar. Wie testen Sie sie?",
    },
    {
        "key": "p10", "num": 10, "title": "Klein testen",
        "points": [("Eine Hypothese und ein Umfang", "Schreiben Sie eine Hypothese"),
                   ("Gleiche Messgrößen wie die Ausgangslage", "Messen Sie genauso"),
                   ("Menschen beobachten, nicht nur Zahlen", "Beobachten Sie die Werker")],
        "example": "Eine Station, eine Schicht: neue Schrittfolge und ein Schaumpolster in der Schale. "
                   "Kosten: fast nichts.",
        "example_cue": "Sureshs Versuch",
        "script": "Zuerst klein und sicher. Schreiben Sie eine Hypothese. Montieren wir den Fuß in der "
                  "Schale, fallen beide Wendungen weg. Legen Sie den Umfang fest, eine Station und eine "
                  "Schicht. Messen Sie genauso wie die Ausgangslage. Beobachten Sie die Werker, nicht nur "
                  "die Zahlen. Sureshs Versuch lief an einer Station, eine Schicht lang. Er nutzte eine "
                  "neue Schrittfolge und ein Schaumpolster in der Schale. Es kostete fast nichts. Was "
                  "passierte?",
    },
    {
        "key": "p11", "num": 11, "title": "Die Ergebnisse prüfen",
        "points": [("Zykluszeit: von 38 s auf 33 s", "Die Zykluszeit sank"),
                   ("Wendungen pro Einheit: von 2 auf 0", "Beide Wendungen"),
                   ("Kratzer: von 15 auf 3 pro 1.000", "Kratzer sanken"),
                   ("Nichts anderes wurde schlechter", "nichts anderes schlechter wurde")],
        "example": "Ausgewogenheitsregel: das Ziel wird besser, und Sicherheit, Qualität und Lieferung "
                   "leiden nicht.",
        "example_cue": "Das ist die Ausgewogenheitsregel",
        "script": "Die Zykluszeit sank auf dreiunddreißig Sekunden, jetzt unter dem TAKT. Beide Wendungen "
                  "fielen weg. Kratzer sanken von fünfzehn auf drei pro tausend. Und das Team prüfte, dass "
                  "nichts anderes schlechter wurde. Testergebnisse, Sicherheit und die nächste Station "
                  "hielten. Die Werker sagten, ihr Rücken spürte den Unterschied schon mittags. Das ist die "
                  "Ausgewogenheitsregel. Eine Zahl zu verbessern und eine andere zu verschlechtern, ist "
                  "kein Kaizen. Aber woher wissen Sie, dass es hält?",
    },
    {
        "key": "p12", "num": 12, "title": "Ehrlich messen",
        "points": [("Gleiche Definitionen, vorher und nachher", "Nutzen Sie dieselben Definitionen"),
                   ("Gute Menge zählen, nicht Brutto", "Zählen Sie gute Menge"),
                   ("Nach 30, 60, 90 Tagen erneut prüfen", "prüfen Sie erneut")],
        "example": "Tag 30: weiter 33 s. Tag 90: weiter 33 s, und 3 Kratzer pro 1.000.",
        "example_cue": "Suresh prüfte",
        "script": "Messen Sie ehrlich. Nutzen Sie dieselben Definitionen vorher und nachher. Zählen Sie "
                  "gute Menge, nicht Bruttomenge. Zeigen Sie die echte Veränderung, nicht nur einen "
                  "Prozentsatz. Und prüfen Sie, dass nichts anderes es bewirkt hat, wie ein leichterer "
                  "Modellmix. Dann prüfen Sie erneut nach dreißig, sechzig und neunzig Tagen. Suresh prüfte "
                  "an Tag dreißig, und wieder an Tag neunzig. Weiter dreiunddreißig Sekunden. Was sichert "
                  "es ab?",
    },
    {
        "key": "p13", "num": 13, "title": "Den Gewinn standardisieren",
        "points": [("SOP und Standardarbeit aktualisieren", "Aktualisieren Sie die SOP"),
                   ("Alle schulen, den alten Weg entfernen", "Schulen Sie jeden Werker"),
                   ("Verantwortlichen benennen und auditieren", "Benennen Sie einen Verantwortlichen")],
        "example": "Die alten Wendeanweisungen wurden noch in derselben Woche von jeder Station entfernt.",
        "example_cue": "Suresh entfernte",
        "script": "Ein Kaizen ist erst fertig, wenn es Standard ist. Aktualisieren Sie die SOP und die "
                  "Standardarbeit. Schulen Sie jeden Werker, und entfernen Sie die alte Methode. Benennen "
                  "Sie einen Verantwortlichen, und auditieren Sie. Suresh entfernte die alten "
                  "Wendeanweisungen noch in derselben Woche. Und an der neuen Basis beginnt das nächste "
                  "Kaizen. Wie halten Sie Ideen am Laufen?",
    },
    {
        "key": "p14", "num": 14, "title": "Eine Gewohnheit daraus machen",
        "points": [("Eine sichtbare Ideentafel", "Eine sichtbare Ideentafel"),
                   ("Schnelle Antworten auf jede Idee", "Antworten Sie auf jede Idee"),
                   ("Die Menschen anerkennen", "Erkennen Sie")],
        "example": "Sureshs Team: 40 Ideen in 3 Monaten, 27 getestet, 19 standardisiert.",
        "example_cue": "In drei Monaten",
        "script": "Machen Sie Kaizen zur täglichen Gewohnheit. Eine sichtbare Ideentafel zeigt, dass Ideen "
                  "zählen. Antworten Sie auf jede Idee innerhalb einer Woche, auch wenn die Antwort nein "
                  "ist. Erkennen Sie die Menschen an, nicht nur die Einsparungen. Und prüfen Sie jede Woche "
                  "die laufenden Ideen. In drei Monaten sammelte Sureshs Team vierzig Ideen. Es testete "
                  "siebenundzwanzig und standardisierte neunzehn. Was würde an Ihrer Linie passieren?",
    },
    {
        "key": "p15", "num": 15, "title": "Morgen starten",
        "points": [("Einen wiederkehrenden Schmerz wählen", "Wählen Sie einen wiederkehrenden Schmerz"),
                   ("Zehn Zyklen beobachten, mit dem Team reden", "Beobachten Sie zehn Zyklen"),
                   ("Die kleinste sichere Lösung testen", "testen Sie die kleinste sichere Lösung")],
        "example": "Kaizen = kleine Verbesserungen × disziplinierte Wiederholung × Eigenverantwortung.",
        "example_cue": "Kleine Verbesserungen",
        "script": "So starten Sie morgen. Wählen Sie einen wiederkehrenden Schmerz an Ihrer Linie. "
                  "Beobachten Sie zehn Zyklen, und messen Sie den Verlust. Sprechen Sie mit den Menschen an "
                  "der Arbeit, und setzen Sie ein messbares Ziel. Dann testen Sie die kleinste sichere "
                  "Lösung. Wirkt sie, standardisieren Sie sie. Kleine Verbesserungen, diszipliniert "
                  "wiederholt, von Menschen, die sie tragen. So werden gewöhnliche Linien großartig. Wen "
                  "fragen Sie zuerst?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Veränderung zum Besseren", "icon": "chartUp", "with": 0},
        {"label": "Kleine Schritte", "icon": "sequence", "with": 1},
        {"label": "Vom Team", "icon": "person", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 2, "icon": "weight", "label": "Wendungen pro Monitor",
                 "unit": "jede Einheit, jede Schicht", "with": "example"}},
    "p02": {"type": "icons", "items": [
        {"label": "Kontinuierlich", "icon": "sequence", "with": 0},
        {"label": "Am Gemba", "icon": "walk", "with": 1},
        {"label": "Günstig, Daten", "icon": "scale", "with": 2},
        {"label": "Neuer Standard", "icon": "clipboard", "tone": "good", "with": 3}]},
    "p03": {"type": "versus", "items": [
        {"label": "„Haben wir immer so gemacht“", "sub": "Verlust hinnehmen", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "„Jeder Prozess kann besser werden“", "sub": "Kaizen", "icon": "check", "tone": "good", "with": 0}]},
    "p04": {"type": "ladder", "top": "AM GRÖSSTEN", "bottom": "AM KLEINSTEN", "items": [
        {"label": "System-Kaizen", "sub": "Wochen", "icon": "stack", "with": 3},
        {"label": "Kaizen-Event", "sub": "3–5 Tage", "icon": "calendar", "with": 2},
        {"label": "Punkt-Kaizen", "sub": "Stunden bis Tage", "icon": "pin", "with": 1},
        {"label": "Tages-Kaizen", "sub": "Minuten", "icon": "hand", "with": 0}]},
    "p05": {"type": "flow", "items": [
        {"label": "Plan", "icon": "clipboard", "with": 0},
        {"label": "Do", "icon": "wrench", "with": 1},
        {"label": "Check", "icon": "search", "with": 2},
        {"label": "Act", "icon": "check", "tone": "good", "with": 3}]},
    "p06": {"type": "flow", "items": [
        {"label": "Bildschirm unten: Fuß montieren", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Bildschirm oben: testen", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Zwei Hebungen à 6 kg", "icon": "warning", "tone": "bad", "with": "example"}]},
    "p07": {"type": "bars", "label": "TAKT", "value": 35, "suffix": " s", "with": "example", "items": [
        {"label": "Zykluszeit", "value": 38, "tone": "bad", "with": "example"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Werker fragen", "icon": "person", "with": 0},
        {"label": "ECRS", "icon": "key", "with": 1},
        {"label": "Andere Linien", "icon": "search", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Zweimal wenden", "sub": "Heute", "icon": "weight", "tone": "bad", "with": "example"},
            {"label": "Fuß in der Schale montieren", "sub": "Leelas Idee", "icon": "check", "tone": "good", "with": "example"}]}},
    "p09": {"type": "icons", "with": "example", "items": [
        {"label": "Roboterarm", "sub": "Bewertung 2,4", "icon": "gear", "with": "example"},
        {"label": "Hebehilfe", "sub": "Bewertung 3,6", "icon": "weight", "with": "example"},
        {"label": "Leelas Idee", "sub": "Bewertung 4,7 von 5", "icon": "check", "tone": "good", "with": "example"}]},
    "p10": {"type": "doc", "items": [
        {"label": "Hypothese: beide Wendungen fallen weg", "icon": "key", "with": 0},
        {"label": "Umfang: eine Station, eine Schicht", "icon": "pin", "with": 0},
        {"label": "Gleiche Messgrößen wie die Ausgangslage", "icon": "scale", "with": 1},
        {"label": "Schaumpolster + neue Schrittfolge", "icon": "shape", "with": "example"}]},
    "p11": {"type": "compare", "before": {"label": "Vorher", "value": 15}, "after": {"label": "Versuch", "value": 3},
            "unit": "verkratzte Panels pro 1.000 Monitore", "note": "Zyklus 38 s → 33 s · Wendungen 2 → 0", "with": 2},
    "p12": {"type": "timeline", "items": [
        {"label": "Ausgangslage", "sub": "Vorher", "icon": "clipboard", "with": 0},
        {"label": "Weiter 33 s", "sub": "Tag 30", "icon": "check", "with": "example"},
        {"label": "Weiter 33 s", "sub": "Tag 90", "icon": "check", "tone": "good", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "SOP aktualisieren", "icon": "clipboard", "with": 0},
        {"label": "Schulen, alten Weg entfernen", "icon": "person", "with": 1},
        {"label": "Verantwortlicher und Audit", "icon": "search", "tone": "good", "with": 2}]},
    "p14": {"type": "bars", "label": "", "note": "Sureshs Team, die ersten drei Monate", "with": "example", "items": [
        {"label": "Ideen", "value": 40, "with": "example"},
        {"label": "Getestet", "value": 27, "with": "example"},
        {"label": "Standardisiert", "value": 19, "tone": "good", "with": "example"}]},
    "p15": {"type": "steps", "items": [
        {"label": "Ein wiederkehrender Schmerz", "with": 0},
        {"label": "Zehn Zyklen, mit dem Team reden", "with": 1},
        {"label": "Kleinste sichere Lösung", "with": 2},
        {"label": "Standardisieren", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Welche ist die beste Kaizen-Problembeschreibung?",
        "options": ["„Wir brauchen einen Roboterarm an der Monitorlinie“",
                    "„Zykluszeit 38 s gegenüber TAKT 35 s, mit 2 Wendungen pro Einheit; in 4 Wochen 35 s "
                    "erreichen“",
                    "„Die Werker sind zu langsam“"],
        "correct": 1,
        "explanation": "Eine gute Beschreibung hat die gemessene Lücke, den beobachteten Verlust und ein Ziel "
                       "mit Termin, ohne Lösung und ohne Schuld.",
        "q_script": "Kurzer Check. Welche ist die beste Kaizen-Problembeschreibung? Nehmen Sie sich kurz "
                    "Zeit.",
        "a_script": "Die zweite. Sie hat die gemessene Lücke, den beobachteten Verlust und ein Ziel mit "
                    "Termin. Die anderen sind eine Lösung und eine Schuldzuweisung.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Ein Versuch senkt die Zykluszeit um 4 Sekunden, aber Werker melden Schulterschmerzen. "
                    "Was nun?",
        "options": ["Standardisieren: das Ziel wurde besser",
                    "Noch nicht als Erfolg werten: Methode anpassen und neu testen",
                    "Werker stündlich rotieren lassen und beibehalten"],
        "correct": 1,
        "explanation": "Die Ausgewogenheitsregel: ein Kaizen ist nur erfolgreich, wenn Sicherheit, Qualität und "
                       "Menschen nicht leiden. Schmerzen bedeuten, dass die Methode sich ändern muss, bevor sie "
                       "Standard wird.",
        "q_script": "Noch eine, ein Szenario. Ein Versuch senkt die Zykluszeit um vier Sekunden. Aber Werker "
                    "melden Schulterschmerzen. Was sollte das Team tun? Überlegen Sie kurz.",
        "a_script": "Noch ist es kein Erfolg. Passen Sie die Methode an und testen Sie neu. Ein Kaizen zählt "
                    "nur, wenn Sicherheit und Menschen nicht für den Gewinn bezahlen.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
