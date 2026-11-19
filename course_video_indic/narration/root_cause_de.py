"""root_cause in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh root_cause_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "rc_de"
NAME = "root_cause_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Root Cause Analysis": "Ruht Kohs Änälisis",
    "Skill Training Matrix": "Skill Treening Matrix",
    "Poka Yoke": "Poka Joke",
    "Ishikawa": "Ischikawa",
    "Pareto": "Pareto",
    "5W2H": "fünf we zwei ha",
    "QRQC": "ku err ku ze",
    "FMEA": "eff emm e a",
    "RCA": "err ze a",
    "DOE": "de o e",
    "MES": "emm e ess",
    "SOP": "ess o pe",
    "SKU": "ess ka u",
    "AOI": "a o i",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Sechsunddreißig Kameras fielen an einem Vormittag im Fokustest durch. Innerhalb einer "
    "Stunde hatten drei Leute drei Antworten. Die Vorrichtung. Die Linse. Der Tester. Wer "
    "hatte recht? In dieser Lektion lernen Sie die Root Cause Analysis kennen. Sie sehen, wie "
    "Sie vom Symptom zu einer beweisbaren Ursache kommen und sie dauerhaft stoppen. Wir "
    "begleiten Lakshmi, Qualitätsingenieurin in einem Kamerawerk."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Definieren Sie das Problem scharf, und schützen Sie zuerst "
    "Ihren Kunden. Behandeln Sie jede Ursache als Hypothese, bis ein Test sie beweist. Und "
    "beheben Sie beides, warum es entstand und warum es durchrutschte. Ihre Aufgabe für diese "
    "Woche. Nehmen Sie ein abgeschlossenes Problem, und prüfen Sie, ob seine Grundursache je "
    "getestet wurde. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie die Skill "
    "Training Matrix kennen."
)

# One story thread: Lakshmi's network-camera plant. Line 3: 36 of 1,200 units fail
# focus after the 10:00 changeover (3.0% vs 0.5% baseline); Line 2 has no failures.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was RCA ist",
        "points": [("Symptom: was Sie beobachten", "Das Symptom ist"),
                   ("Mechanismus: wie es geschah", "Der Mechanismus ist"),
                   ("Grundursache: steuerbar, mit Belegen", "Die Grundursache ist")],
        "example": "Unscharfes Bild = das Symptom. Ein falscher Abstandshalter könnte die Ursache sein, "
                   "unbestätigt, bis er getestet ist.",
        "example_cue": "An Lakshmis Linie",
        "script": "Hier ist die Kernidee. Root Cause Analysis ist eine belegbasierte Untersuchung, warum "
                  "etwas schiefging. Sie trennt drei Dinge. Das Symptom ist, was Sie beobachten. Der "
                  "Mechanismus ist, wie es geschah. Die Grundursache ist eine Bedingung, die Sie steuern "
                  "können, gestützt durch Belege. An Lakshmis Linie ist ein unscharfes Bild das Symptom. "
                  "Ein falscher Abstandshalter könnte die Ursache sein. Aber nichts ist bestätigt, bis es "
                  "getestet ist. Wo passt das hin?",
    },
    {
        "key": "p02", "num": 2, "title": "RCA im Qualitätssystem",
        "points": [("Eine Abweichung erkennen", "Zuerst erkennen Sie"),
                   ("Eingrenzen, um den Kunden zu schützen", "Dann grenzen Sie sie ein"),
                   ("Mit echten Daten untersuchen", "Dann untersuchen Sie"),
                   ("Korrigieren, dann über Zeit bestätigen", "Sie beheben die bestätigten")],
        "example": "Ein erfolgreiches Sortieren schützt den Kunden, beweist aber nicht, dass die Ursache weg "
                   "ist.",
        "example_cue": "Ein erfolgreiches Sortieren schützt",
        "script": "RCA ist ein Glied in einem geschlossenen Kreis. Zuerst erkennen Sie eine Abweichung. "
                  "Dann grenzen Sie sie ein, um Ihren Kunden zu schützen. Dann untersuchen Sie mit echten "
                  "Daten. Sie beheben die bestätigten Ursachen, und bestätigen das Ergebnis über die Zeit. "
                  "Es steht neben QRQC, der FMEA, Kontrollplänen und Poka Yoke. Und ein Kernpunkt. Ein "
                  "erfolgreiches Sortieren schützt den Kunden. Aber beweist es, dass die Ursache weg ist? "
                  "Überhaupt nicht.",
    },
    {
        "key": "p03", "num": 3, "title": "Definieren: 5W2H und Is / Is Not",
        "points": [("Scharfes, messbares Problem", "beginnt mit einem scharfen"),
                   ("5W2H erfasst die Fakten", "Nutzen Sie 5W2H"),
                   ("Is / Is Not: wo es auftritt, und wo nicht", "genannt Ist, Ist nicht")],
        "example": "Linie 3: 36 von 1.200 Kameras fielen nach dem Wechsel um 10:00 im Fokus durch. Linie 2, "
                   "andere Vorrichtung: keine.",
        "example_cue": "Lakshmis Beschreibung war klar",
        "script": "Jede gute RCA beginnt mit einem scharfen, messbaren Problem. Nutzen Sie 5W2H, um die "
                  "Fakten zu erfassen. Dann ergänzen Sie einen starken Vergleich, genannt Ist, Ist nicht. "
                  "Wo tritt das Problem auf, und wo nicht? Lakshmis Beschreibung war klar. An Linie drei "
                  "fielen sechsunddreißig von zwölfhundert Kameras im Fokus durch. Es begann nach dem "
                  "Wechsel um zehn Uhr. Linie zwei, mit einer anderen Vorrichtung, hatte keine. Was sagt "
                  "Ihnen dieser Vergleich?",
    },
    {
        "key": "p04", "num": 4, "title": "Belege und Rückverfolgbarkeit",
        "points": [("Belege sammeln, bevor Einstellungen sich ändern", "sammeln Sie die Belege"),
                   ("Defekte und gute Muster aufheben", "Heben Sie defekte Teile"),
                   ("MES-Daten, Testprotokolle, Alarme holen", "Holen Sie die MES-Daten"),
                   ("Jede kürzliche Änderung erfassen", "Erfassen Sie jede kürzliche Änderung"),
                   ("Kalibrierung der Messmittel prüfen", "Und bestätigen Sie, dass Ihre Messmittel")],
        "example": "Lakshmi verpackte zehn defekte und zehn gute Kameras, bevor jemand die Vorrichtung "
                   "anfasste.",
        "example_cue": "Lakshmi verpackte zehn",
        "script": "Es zeigt auf den Wechsel. Aber zuerst sammeln Sie die Belege, bevor jemand eine "
                  "Einstellung ändert. Heben Sie defekte Teile und bekannt gute Muster auf. Holen Sie die "
                  "MES-Daten, Testprotokolle und Maschinenalarme. Erfassen Sie jede kürzliche Änderung, bei "
                  "Werkzeug, Firmware, Rezept und Materiallos. Und bestätigen Sie, dass Ihre Messmittel "
                  "kalibriert sind, bevor Sie kleinen Unterschieden trauen. Lakshmi verpackte zehn defekte "
                  "und zehn gute Kameras. Könnte ein anderer Ingenieur Ihre Befunde wiederholen?",
    },
    {
        "key": "p05", "num": 5, "title": "Pareto: den Kampf wählen",
        "points": [("Nach Anzahl, Kosten oder Risiko ordnen", "Ordnen Sie Ihre Fehlerarten"),
                   ("Sortieren und kumulierte % addieren", "Sortieren Sie sie"),
                   ("Den größten nach Schicht, Station, Lieferant aufteilen", "Dann teilen Sie den größten"),
                   ("Schwere Risiken haben Vorrang", "Ein schweres")],
        "example": "Falsche PCB 40 · fehlende Schraube 25 · Fokus 20 · Etikett 10 · Sonstige 5 → die drei "
                   "größten = 85 %.",
        "example_cue": "An Lakshmis Linie machten drei",
        "script": "Bei vielen Problemen hilft Pareto bei der Wahl. Ordnen Sie Ihre Fehlerarten nach Anzahl, "
                  "Kosten oder Risiko. Sortieren Sie sie, und addieren Sie den kumulierten Prozentsatz. Oft "
                  "machen wenige Ursachen den Großteil des Verlusts aus. An Lakshmis Linie machten drei "
                  "Fehlerarten fünfundachtzig Prozent aus. Dann teilen Sie den größten nach Schicht, "
                  "Station oder Lieferant auf. Aber Vorsicht. Ein schweres Sicherheits- oder Kundenrisiko "
                  "hat Vorrang, egal welcher Rang. Wie graben Sie tiefer?",
    },
    {
        "key": "p06", "num": 6, "title": "5 Why: die Kette testen",
        "points": [("Fünf ist keine Regel", "Fünf ist keine Regel"),
                   ("Belege für jedes Glied", "Jedes Glied braucht Belege"),
                   ("Verzweigen, wenn es mehr als eine Ursache gibt", "Verzweigen Sie"),
                   ("Nie bei „Bedienfehler\" aufhören", "hören Sie nie bei Bedienfehler auf")],
        "example": "Fehlende Schraube → Zyklus endete ohne Bestätigung → Drehmomentsignal nicht mit MES "
                   "verknüpft.",
        "example_cue": "Nehmen Sie eine fehlende Schraube",
        "script": "Nutzen Sie fünf Warum als Kette prüfbarer Behauptungen. Fünf ist keine Regel. Jedes "
                  "Glied braucht Belege. Verzweigen Sie bei mehreren Ursachen. Und hören Sie nie bei "
                  "Bedienfehler auf. Fragen Sie, was die Arbeitsgestaltung zuließ. Nehmen Sie eine fehlende "
                  "Schraube. Die Station beendete den Zyklus ohne Bestätigung. Warum? Das Drehmomentsignal "
                  "war nicht mit MES verknüpft. Haben Sie die Protokolle geprüft?",
    },
    {
        "key": "p07", "num": 7, "title": "Fischgräte und die 6M",
        "points": [("Fischgräte = Ishikawa-Diagramm", "Die Fischgräte, oder das Ishikawa-Diagramm"),
                   ("Mensch · Maschine · Methode", "Mensch, Maschine, Methode"),
                   ("Material · Messung · Umwelt", "Material, Messung und Umwelt"),
                   ("Sie beweist nicht, welche Ursache stimmt", "Eine Fischgräte beweist nicht")],
        "example": "Lakshmis Fischgräte: Vorrichtungsverschleiß, falsches Rezept, Linsentoleranz, "
                   "Testerwiederholbarkeit, Handhabung, Hitze.",
        "example_cue": "Lakshmis Team füllte sie aus",
        "script": "Die Fischgräte, oder das Ishikawa-Diagramm, ordnet Ihre Ideen. Sie hat sechs Äste. "
                  "Mensch, Maschine, Methode, Material, Messung und Umwelt. Lakshmis Team füllte sie aus. "
                  "Vorrichtungsverschleiß, ein falsches Rezept, Linsentoleranz, Wiederholbarkeit des "
                  "Testers, Handhabung und Hitze. Eine gute Liste Verdächtiger. Aber der Kernpunkt. Eine "
                  "Fischgräte beweist nicht, welche Ursache stimmt. Für jeden Ast schreiben Sie den Test, "
                  "der sie bestätigt oder verwirft. Was hat sich geändert?",
    },
    {
        "key": "p08", "num": 8, "title": "Änderungsanalyse und Fehlerbäume",
        "points": [("Änderungsanalyse: fehlerhaft gegen zuletzt stabil", "Das ist die Änderungsanalyse"),
                   ("Fehlerbaum: rückwärts mit AND / OR", "nutzen Sie einen Fehlerbaum"),
                   ("Gleichzeitig ≠ Ursache", "Nur weil zwei Dinge")],
        "example": "Kein Bild rutscht nur durch, wenn die Firmware falsch ist AND die Verriegelung fehlt.",
        "example_cue": "Ein Videorekorder ohne Bild",
        "script": "Das ist die Änderungsanalyse. Sie vergleichen den fehlerhaften Zustand mit dem letzten "
                  "stabilen, und listen jede Änderung dazwischen. Bei komplexen Problemen nutzen Sie einen "
                  "Fehlerbaum. Er arbeitet rückwärts vom Fehler, mit Und- und Oder-Logik. Ein Videorekorder "
                  "ohne Bild rutscht nur durch, wenn die Firmware falsch ist und die Verriegelung fehlt. "
                  "Aber Vorsicht. Nur weil zwei Dinge gleichzeitig geschahen, verursachte das eine nicht "
                  "das andere. Wie beweisen Sie es?",
    },
    {
        "key": "p09", "num": 9, "title": "Die Hypothese testen",
        "points": [("Eine Vorhersage aufschreiben", "Schreiben Sie eine Vorhersage"),
                   ("Ein Faktor auf einmal, oder ein DOE", "Ändern Sie einen Faktor"),
                   ("Genug Muster, wiederholt", "Nutzen Sie genug Muster"),
                   ("Zuerst das Messmittel prüfen", "sie prüfte zuerst das Messmittel")],
        "example": "Freigegebene gegen verdächtige Abstandshalter, mit gleicher Kamera, gleichem Rezept, "
                   "gleichem Raum.",
        "example_cue": "Lakshmi verglich freigegebene",
        "script": "Schreiben Sie eine Vorhersage. Ist der Abstandshalter falsch, sollten Fokusfehler "
                  "steigen. Dann testen Sie es. Ändern Sie einen Faktor auf einmal, oder nutzen Sie ein "
                  "geplantes Experiment, ein DOE, wenn Faktoren zusammenwirken. Nutzen Sie genug Muster, "
                  "und wiederholen Sie den Versuch. Lakshmi verglich freigegebene und verdächtige "
                  "Abstandshalter, mit gleicher Kamera, gleichem Rezept, gleichem Raum. Und sie prüfte "
                  "zuerst das Messmittel. Streut die Messung stark, verbirgt sich sogar ein echter "
                  "Unterschied. Bereit für die Lösung?",
    },
    {
        "key": "p10", "num": 10, "title": "Eingrenzen, korrigieren, vorbeugen",
        "points": [("Eingrenzen: den Kunden jetzt schützen", "Die Eingrenzung schützt"),
                   ("Korrigieren: die bestätigte Ursache beseitigen", "Die Korrekturmaßnahme beseitigt"),
                   ("Vorbeugen: auf ähnliche Linien übertragen", "Und die Vorbeugemaßnahme"),
                   ("Auch die Durchschlupfursache beheben", "Beheben Sie auch die Durchschlupfursache")],
        "example": "Falsche Platine: gesperrten Bestand scannen → MES-Abgleich ergänzen → auf andere "
                   "Varianten übertragen.",
        "example_cue": "Bei einer falschen Platine",
        "script": "Halten Sie drei Maßnahmen getrennt. Die Eingrenzung schützt Ihren Kunden jetzt. Die "
                  "Korrekturmaßnahme beseitigt die bestätigte Ursache. Und die Vorbeugemaßnahme überträgt "
                  "die Lehre auf ähnliche Linien. Beheben Sie auch die Durchschlupfursache, mit einer "
                  "Verriegelung oder Anwesenheitsprüfung. Bei einer falschen Platine scannen Sie den "
                  "gesperrten Bestand. Dann ergänzen Sie einen MES-Abgleich, und übertragen ihn auf andere "
                  "Varianten. Eine Regel. Geben Sie gesperrten Bestand nie frei, nur weil die Lösung "
                  "bestellt ist. Wie machen Sie es dauerhaft?",
    },
    {
        "key": "p11", "num": 11, "title": "Verknüpfung mit FMEA und Poka Yoke",
        "points": [("Jede Ursache mit einer Fehlerart verknüpfen", "Verknüpfen Sie jede bestätigte Ursache"),
                   ("Den Kontrollplan aktualisieren", "Aktualisieren Sie den Kontrollplan"),
                   ("Poka Yoke validieren: gut, schlecht, grenzwertig", "Validieren Sie jedes Poka Yoke"),
                   ("SOP, Schulung, Audits aktualisieren", "Dann aktualisieren Sie die SOP")],
        "example": "Fragen Sie: Verhindert die neue Kontrolle den Fehler, erkennt sie ihn, oder macht sie "
                   "ihn nur sichtbar?",
        "example_cue": "Verhindert die neue Kontrolle",
        "script": "Führen Sie das Gelernte ins System zurück. Verknüpfen Sie jede bestätigte Ursache mit "
                  "einer Fehlerart in Ihrer FMEA, und bewerten Sie das Risiko neu. Aktualisieren Sie den "
                  "Kontrollplan, mit Methode, Reaktion und Verantwortlichem. Validieren Sie jedes Poka Yoke "
                  "mit bekannt guten, bekannt schlechten und grenzwertigen Teilen. Dann aktualisieren Sie "
                  "die SOP, Schulung und Auditfragen. Stellen Sie sich eine Frage. Verhindert die neue "
                  "Kontrolle den Fehler, erkennt sie ihn, oder macht sie ihn nur sichtbar?",
    },
    {
        "key": "p12", "num": 12, "title": "RCA-Kennzahlen",
        "points": [("Geschlossene Formulare sind kein Erfolg", "Melden Sie keinen Erfolg"),
                   ("Fehlerrate ≠ Erstdurchlaufquote", "Verfolgen Sie die Fehlerrate"),
                   ("Wiederholungen nach Abschluss verfolgen", "Verfolgen Sie, wie oft"),
                   ("Kosten und Amortisation", "Was kostet sie")],
        "example": "60 → 12 Fehler pro 20.000: 80 % weniger. ₹90.000 Kontrolle spart ₹15.000/Monat = "
                   "Amortisation in 6 Monaten.",
        "example_cue": "Eine Kontrolle, die Fehler",
        "script": "Messen Sie die Qualität Ihrer Untersuchungen und ihre Wirkung aufs Geschäft. Melden Sie "
                  "keinen Erfolg, nur weil ein Formular geschlossen ist. Verfolgen Sie die Fehlerrate und "
                  "die Erstdurchlaufquote, aber verwechseln Sie sie nie. Verfolgen Sie, wie oft Probleme "
                  "nach Abschluss wiederkehren. Eine Kontrolle, die Fehler um achtzig Prozent senkt, klingt "
                  "toll. Was kostet sie, und wie schnell amortisiert sie sich? Lakshmis in sechs Monaten. "
                  "Nun ihr ganzer Fall.",
    },
    {
        "key": "p13", "num": 13, "title": "Fallstudie: Fokusfehler",
        "points": [("Jede Kamera seit dem letzten guten Erstteil gesperrt", "Lakshmi sperrte jede Kamera"),
                   ("Vier Verdächtige: Abstandshalter, Rezept, Sitz, Tester", "Ihr Team listete vier"),
                   ("Gemessen, Protokolle verglichen, Kreuztausch-Test", "Sie maßen die Abstandshalter"),
                   ("Codierter Abstandshalter + Vorrichtungs-Scan mit Rezept verknüpft", "Die Lösung war ein codierter")],
        "example": "Tausch der Abstandshalter verschob die Fehler. Tausch der Tester nicht. Das war der "
                   "Beweis.",
        "example_cue": "Der Tausch der Abstandshalter",
        "script": "Lakshmi sperrte jede Kamera seit dem letzten freigegebenen Erstteil. Ihr Team listete "
                  "vier Verdächtige. Dicke des Abstandshalters, falsches Rezept, Sitz der Linse und Drift "
                  "des Testers. Sie maßen die Abstandshalter, verglichen die Protokolle, und machten einen "
                  "Kreuztausch-Test. Der Tausch der Abstandshalter verschob die Fehler. Der Tausch der "
                  "Tester nicht. Nun hatten sie Beweise. Die Lösung war ein codierter Abstandshalter, und "
                  "ein Vorrichtungs-Scan mit Rezeptabgleich. Welche Belege hätten Sie gebraucht?",
    },
    {
        "key": "p14", "num": 14, "title": "Zwei weitere Fälle: SMT und Etikett",
        "points": [("Platinenlinie: falsches Bauteil bestückt", "An der Platinenlinie"),
                   ("Lösung: Feeder-Verriegelung gegen die BOM", "Die Lösung war eine Feeder-Verriegelung"),
                   ("Verpackung: Kartonetikett ≠ Gerät", "In der Verpackung"),
                   ("Lösung: Karton schließt erst, wenn alles passt", "Diese Lösung verhinderte")],
        "example": "Beide Lösungen wurden vor dem Abschluss herausgefordert.",
        "example_cue": "Beide Lösungen wurden",
        "script": "Zwei kürzere Fälle zeigen dasselbe Muster. An der Platinenlinie wurde ein falsches "
                  "Bauteil bestückt. Das Team verglich Stückliste, Feeder-Einrichtung, Rollen-Barcode und "
                  "AOI-Bilder. Die Lösung war eine Feeder-Verriegelung gegen die Stückliste. In der "
                  "Verpackung passte ein Kartonetikett nicht zum Gerät. Diese Lösung verhinderte, dass der "
                  "Karton schloss, bevor Seriennummer, SKU und Etikett übereinstimmten. Beide Lösungen "
                  "wurden herausgefordert. Könnten Sie beweisen, dass jede verdächtige Einheit gefunden "
                  "wurde?",
    },
    {
        "key": "p15", "num": 15, "title": "Einführung in 90 Tagen",
        "points": [("Tag 1–30: Auslöser, Rollen, Formulare, Piloten", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: schulen, untersuchen", "In den nächsten dreißig"),
                   ("Tag 61–90: auditieren, FMEA aktualisieren, ausweiten", "In den letzten dreißig"),
                   ("Abschluss: abgeglichen, bestätigt, getestet", "Bevor Sie ein Problem schließen")],
        "example": "Machen Sie RCA zur Routine, nicht zu einem einmaligen Workshop.",
        "example_cue": "Machen Sie RCA zur Routine",
        "script": "Machen Sie RCA zur Routine, nicht zu einem einmaligen Workshop. In den ersten dreißig "
                  "Tagen legen Sie Auslöser, Rollen, Formulare und Pilotbereiche fest. In den nächsten "
                  "dreißig schulen Sie Teams und führen echte Untersuchungen. In den letzten dreißig "
                  "auditieren Sie die Ergebnisse, aktualisieren FMEA und Kontrollpläne, und weiten aus. "
                  "Bevor Sie ein Problem schließen, prüfen Sie es. Ist die Eingrenzung abgeglichen? Sind "
                  "die Ursachen bestätigt und die Maßnahmen getestet? Beweisen Sie die Ursache, dann beugen "
                  "Sie vor.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Symptom", "sub": "Ein unscharfes Bild", "icon": "camera", "tone": "bad"},
        {"label": "Mechanismus", "sub": "Wie es geschah", "icon": "gear"},
        {"label": "Grundursache", "sub": "Ein falscher Abstandshalter? Erst testen", "icon": "search"}]},
    "p02": {"type": "flow", "items": [
        {"label": "Erkennen", "icon": "sensor"}, {"label": "Eingrenzen", "icon": "lock"},
        {"label": "Mit Daten untersuchen", "icon": "search"},
        {"label": "Korrigieren, über Zeit bestätigen", "icon": "check", "tone": "good"}]},
    "p03": {"type": "compare", "before": {"label": "Linie 3", "value": 36}, "after": {"label": "Linie 2", "value": 0},
            "unit": "Fokusfehler nach dem Wechsel (Linie 2 hat eine andere Vorrichtung)",
            "note": "Is / Is Not zeigt auf die Vorrichtung", "with": "example"},
    "p04": {"type": "icons", "items": [
        {"label": "Zuerst Belege", "icon": "search"}, {"label": "Defekte + gute Muster", "icon": "box"},
        {"label": "Protokolle und Alarme", "icon": "clipboard"}, {"label": "Kürzliche Änderungen", "icon": "sequence"},
        {"label": "Kalibrierung", "icon": "scale"}]},
    "p05": {"type": "bars", "label": "", "note": "Die drei größten = 85 % der Fehler", "items": [
        {"label": "Falsche PCB", "value": 40, "tone": "bad", "with": "example"},
        {"label": "Fehlende Schraube", "value": 25, "tone": "bad", "with": "example"},
        {"label": "Fokus", "value": 20, "tone": "bad", "with": "example"},
        {"label": "Etikett", "value": 10, "with": "example"},
        {"label": "Sonstige", "value": 5, "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Fünf ist keine Regel", "icon": "count"}, {"label": "Belege pro Glied", "icon": "search"},
        {"label": "Bei Bedarf verzweigen", "icon": "sequence"}, {"label": "Nie „Bedienfehler\"", "icon": "cross", "tone": "bad"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Eine fehlende Schraube", "icon": "screw", "tone": "bad", "with": "example"},
            {"label": "Warum? Der Zyklus endete trotzdem", "icon": "sequence", "with": "example"},
            {"label": "Warum? Drehmoment nicht mit MES verknüpft", "icon": "chip", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Mensch", "sub": "Handhabung", "icon": "person", "with": 1},
        {"label": "Maschine", "sub": "Vorrichtungsverschleiß", "icon": "gear", "with": 1},
        {"label": "Methode", "sub": "Falsches Rezept", "icon": "clipboard", "with": 1},
        {"label": "Material", "sub": "Linsentoleranz", "icon": "box", "with": 2},
        {"label": "Messung", "sub": "Testerwiederholbarkeit", "icon": "scale", "with": 2},
        {"label": "Umwelt", "sub": "Hitze", "icon": "wave", "with": 2}]},
    "p08": {"type": "icons", "items": [
        {"label": "Änderungsanalyse", "sub": "Fehlerhaft gegen zuletzt stabil", "icon": "sequence", "with": 0},
        {"label": "Fehlerbaum", "sub": "AND / OR, rückwärts", "icon": "gear", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Firmware ist falsch", "icon": "chip", "tone": "bad", "with": "example"},
            {"label": "AND die Verriegelung fehlt", "icon": "lock", "tone": "bad", "with": "example"},
            {"label": "Eine Einheit ohne Bild rutscht durch", "icon": "box", "tone": "bad", "with": "example"}]}},
    "p09": {"type": "icons", "items": [
        {"label": "Vorhersage aufschreiben", "icon": "clipboard"}, {"label": "Ein Faktor, oder ein DOE", "icon": "gear"},
        {"label": "Genug Muster", "icon": "stack"}, {"label": "Messmittel prüfen", "icon": "scale"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Verdächtiger Abstandshalter", "sub": "Gleiche Kamera, Rezept, Raum", "icon": "shape"},
            {"label": "Freigegebener Abstandshalter", "sub": "Gleiche Kamera, Rezept, Raum", "icon": "shape"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "Eingrenzen", "sub": "Gesperrten Bestand scannen", "icon": "lock"},
        {"label": "Korrigieren", "sub": "MES-Abgleich ergänzen", "icon": "barcode"},
        {"label": "Vorbeugen", "sub": "Auf andere Varianten übertragen", "icon": "sequence", "tone": "good"}]},
    "p11": {"type": "icons", "items": [
        {"label": "FMEA", "icon": "clipboard"}, {"label": "Kontrollplan", "icon": "shield"},
        {"label": "Poka Yoke validieren", "icon": "test"}, {"label": "SOP, Schulung, Audits", "icon": "person"}],
        "then": {"type": "ladder", "top": "AM BESTEN", "bottom": "AM SCHWÄCHSTEN", "with": "example", "items": [
            {"label": "Verhindert den Fehler", "icon": "key", "with": "example"},
            {"label": "Erkennt ihn", "icon": "sensor", "with": "example"},
            {"label": "Macht ihn nur sichtbar", "icon": "search", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Geschlossenes Formular ≠ Erfolg", "icon": "cross", "tone": "bad"},
        {"label": "Fehlerrate gegen FPY", "icon": "chartUp"},
        {"label": "Wiederholungen nach Abschluss", "icon": "sequence"}, {"label": "Kosten und Amortisation", "icon": "calendar"}],
        "then": {"type": "compare", "before": {"label": "Vorher", "value": 60}, "after": {"label": "Nachher", "value": 12},
                 "unit": "Fehler pro 20.000 Kameras", "note": "80 % weniger, Amortisation in 6 Monaten", "with": "example"}},
    "p13": {"type": "flow", "items": [
        {"label": "Sperren seit dem letzten guten Erstteil", "icon": "lock"},
        {"label": "Vier Verdächtige gelistet", "icon": "search"},
        {"label": "Kreuztausch-Test", "sub": "Abstandshalter verschoben es, Tester nicht", "icon": "test"},
        {"label": "Codierter Abstandshalter + Vorrichtungs-Scan", "icon": "key", "tone": "good"}]},
    "p14": {"type": "icons", "items": [
        {"label": "Falsches Bauteil", "sub": "Platinenlinie", "icon": "chip", "tone": "bad"},
        {"label": "Feeder-Verriegelung", "sub": "Gegen die BOM geprüft", "icon": "lock", "tone": "good"},
        {"label": "Etikett ≠ Gerät", "sub": "Verpackung", "icon": "label", "tone": "bad"},
        {"label": "Karton schließt nicht", "sub": "Bis alle drei passen", "icon": "box", "tone": "good"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Auslöser, Rollen, Formulare, Piloten", "sub": "Tag 1–30", "icon": "clipboard", "with": 0},
        {"label": "Schulen, echte Untersuchungen führen", "sub": "31–60", "icon": "person", "with": 1},
        {"label": "Auditieren, FMEA aktualisieren, ausweiten", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Das Fischgrätendiagramm eines Teams listet sechs mögliche Ursachen. Was beweist es?",
        "options": ["Der größte Ast ist die Grundursache", "Noch nichts: jede Ursache muss getestet werden",
                    "Alle sechs Ursachen stimmen"],
        "correct": 1,
        "explanation": "Eine Fischgräte ordnet Hypothesen. Sie beweist nichts, bis jede Kandidatin durch einen "
                       "Test bestätigt oder verworfen ist.",
        "q_script": "Kurzer Check. Das Fischgrätendiagramm eines Teams listet sechs mögliche Ursachen. Was "
                    "beweist es? Nehmen Sie sich kurz Zeit.",
        "a_script": "Noch nichts. Eine Fischgräte ist eine Liste von Hypothesen. Jede muss getestet werden, "
                    "bevor Sie sie Ursache nennen.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Ein Fehler mit falscher PCB wird gefunden. Die neue MES-Verriegelung ist bestellt, aber "
                    "nicht eingebaut. Darf der gesperrte WIP freigegeben werden?",
        "options": ["Ja, die Lösung ist unterwegs", "Nein, erst nach Prüfung und autorisierter Entscheidung freigeben",
                    "Ja, wenn der Werker neu geschult ist", "Ja, wenn die nächste Schicht informiert ist"],
        "correct": 1,
        "explanation": "Eine bestellte Lösung schützt den Kunden nicht. Gesperrter Bestand wird erst nach "
                       "Prüfung und Entscheidung im Qualitätsprozess freigegeben.",
        "q_script": "Noch eine, ein Szenario. Ein Fehler mit falscher Platine wird gefunden. Die neue "
                    "Verriegelung ist bestellt, aber nicht eingebaut. Darf der gesperrte Bestand freigegeben "
                    "werden? Überlegen Sie kurz.",
        "a_script": "Nein. Geben Sie ihn erst nach Prüfung und einer autorisierten Entscheidung frei. Eine "
                    "bestellte Lösung schützt Ihren Kunden nicht.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
