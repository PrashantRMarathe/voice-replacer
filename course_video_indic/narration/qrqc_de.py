"""qrqc in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh qrqc_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "qr_de"
NAME = "qrqc_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Root Cause Analysis": "Ruht Kohs Änälisis",
    "QRQC": "ku err ku ze",
    "FMEA": "eff emm e a",
    "5W2H": "fünf we zwei ha",
    "MES": "emm e ess",
    "SKU": "ess ka u",
    "SOP": "ess o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Zehn Uhr. Kameras fallen im Fokustest durch. Jemand setzt den Tester zurück, und die "
    "Linie läuft weiter. Bis Mittag ist eine ganze Schicht verdächtiger Kameras auf dem Weg "
    "ins Lager. Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie QRQC kennen, Quick "
    "Response Quality Control. Sie sehen, wie Sie in Minuten reagieren, Ihren Kunden schützen "
    "und trotzdem die echte Ursache finden. Wir begleiten Farhan, Qualitätsleiter in einem "
    "Kamerawerk."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Reagieren Sie schnell, aber mit Belegen. Grenzen Sie zuerst "
    "ein, und gleichen Sie jede verdächtige Einheit ab. Und schließen Sie ein Problem erst, "
    "wenn die Lösung in echter Produktion bewiesen ist. Ihre Aufgabe für diese Woche. "
    "Schreiben Sie die ersten dreißig Minuten Ihres Reaktionsplans für einen kritischen "
    "Fehler auf. Gut gemacht, Lektion abgeschlossen. Als Nächstes vertiefen Sie die Root "
    "Cause Analysis."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was QRQC ist",
        "points": [("Erkennen und sichtbar machen", "Sie erkennen es"),
                   ("Eingrenzen, um den Kunden zu schützen", "Sie grenzen es ein"),
                   ("Ursache mit Fakten finden, Lösung beweisen", "Dann finden Sie die Ursache"),
                   ("Tempo ersetzt nie Belege", "Tempo zählt")],
        "example": "Linie 4: QRQC beginnt mit dem Sperren des Auftrags, nicht mit dem Zurücksetzen des "
                   "Testers.",
        "example_cue": "An Farhans Linie vier",
        "script": "Hier ist die Kernidee. QRQC steht für Quick Response Quality Control. Es ist ein "
                  "disziplinierter Weg, auf ein Problem zu reagieren. Sie erkennen es und machen es "
                  "sichtbar. Sie grenzen es ein, um Ihren Kunden zu schützen. Dann finden Sie die Ursache "
                  "mit Fakten, und beweisen, dass die Lösung wirkt. Tempo zählt, aber es ersetzt nie "
                  "Belege. An Farhans Linie vier beginnt QRQC mit dem Sperren des Auftrags. Nicht mit dem "
                  "Zurücksetzen des Testers. Was steckt dahinter?",
    },
    {
        "key": "p02", "num": 2, "title": "Grundprinzipien",
        "points": [("Echter Ort, echte Teile", "Gehen Sie an den echten Ort"),
                   ("Geprüfte Fakten, nie Schuld", "Nutzen Sie geprüfte Fakten"),
                   ("Sofort reagieren bei Kunden- oder Sicherheitsrisiko", "Reagieren Sie sofort"),
                   ("Eingrenzung ≠ dauerhafte Lösung", "Und trennen Sie die vorläufige Eingrenzung")],
        "example": "Farhans Besprechung beginnt mit der defekten Kamera auf dem Tisch, neben ihren Daten.",
        "example_cue": "Farhans Besprechung beginnt",
        "script": "QRQC entstand in der Qualität von Autozulieferern. Es ruht auf ein paar Prinzipien. "
                  "Gehen Sie an den echten Ort, und schauen Sie auf die echten Teile. Nutzen Sie geprüfte "
                  "Fakten, nie Meinungen oder Schuld. Reagieren Sie sofort auf jedes Kunden- oder "
                  "Sicherheitsrisiko. Und trennen Sie die vorläufige Eingrenzung von der dauerhaften "
                  "Lösung. Farhans Besprechung beginnt mit der defekten Kamera auf dem Tisch, neben ihren "
                  "Daten. Was käme auf Ihren Tisch?",
    },
    {
        "key": "p03", "num": 3, "title": "Drei Eskalationsstufen",
        "points": [("Stufe 1: Linie oder Schicht reagiert", "Auf Stufe eins"),
                   ("Stufe 2: bereichsübergreifendes Team", "Auf Stufe zwei"),
                   ("Stufe 3: Werksleitung, Kunde", "Auf Stufe drei"),
                   ("Sofort eskalieren: Sicherheit, wiederholter Durchschlupf", "Eskalieren Sie sofort")],
        "example": "Ihr Werk legt die Eskalationszeiten nach Risiko fest.",
        "example_cue": "Ihr Werk legt die Zeiten",
        "script": "Ein gutes QRQC-System hat drei Stufen. Auf Stufe eins erkennt die Linie oder Schicht das "
                  "Problem, stoppt oder sortiert aus, und hält die Belege fest. Auf Stufe zwei untersucht "
                  "ein bereichsübergreifendes Team und handelt. Auf Stufe drei stellt die Werksleitung "
                  "Mittel bereit, oder spricht mit dem Kunden. Eskalieren Sie sofort bei Sicherheit oder "
                  "wiederholtem Durchschlupf. Ihr Werk legt die Zeiten nach Risiko fest. Was passiert in "
                  "den ersten Minuten?",
    },
    {
        "key": "p04", "num": 4, "title": "Die ersten 30 Minuten",
        "points": [("0–5 Min.: erkennen, Station und Los finden, sperren", "In den ersten fünf Minuten"),
                   ("Dann: Leitung und Qualität informieren, Muster aufheben", "Dann informieren Sie"),
                   ("Dann: den letzten bekannten guten Punkt finden", "Dann finden Sie den letzten"),
                   ("Bis 30 Min.: sperren, erfassen, zuweisen", "Bis dreißig Minuten")],
        "example": "Starten Sie einen kritischen Prozess nie auf ein mündliches Okay neu.",
        "example_cue": "starten Sie einen kritischen Prozess",
        "script": "Die erste halbe Stunde gibt den Ton an. In den ersten fünf Minuten erkennen Sie es, "
                  "finden Station und Los, und stoppen oder sperren den Fluss. Dann informieren Sie die "
                  "Schichtleitung und die Qualität, und heben defekte und gute Muster auf. Dann finden Sie "
                  "den letzten bekannten guten Punkt. Bis dreißig Minuten sperren Sie den verdächtigen "
                  "Bestand, und erfassen Mengen und Verantwortliche. Und starten Sie einen kritischen "
                  "Prozess nie auf ein mündliches Okay neu. Wen rufen Sie zuerst an?",
    },
    {
        "key": "p05", "num": 5, "title": "5W2H: das Problem definieren",
        "points": [("Was, wo, wann, wer", "Was fiel aus, wo"),
                   ("Wie erkannt, wie viele", "wie es erkannt wurde"),
                   ("Bestätigter Ausschuss oder verdächtige Menge", "Trennen Sie bestätigten Ausschuss")],
        "example": "Linie 4: 24 von 800 Kameras fielen zwischen 10 Uhr und Mittag im Fokus durch, direkt "
                   "nach einem Wechsel der Linsenvorrichtung.",
        "example_cue": "An Linie vier fielen",
        "script": "Eine scharfe Problembeschreibung verhindert, dass Sie das Falsche jagen. Nutzen Sie "
                  "5W2H. Was fiel aus, wo, wann, wer sah es, wie es erkannt wurde, und wie viele. Trennen "
                  "Sie bestätigten Ausschuss von der verdächtigen Menge. Hier ist Farhans Beschreibung. An "
                  "Linie vier fielen an dem Morgen vierundzwanzig von achthundert Kameras im Fokus durch. "
                  "Es begann direkt nach einem Wechsel der Linsenvorrichtung. Das zeigt schon eine "
                  "Richtung. Aber zuerst: was ist mit den verdächtigen Einheiten?",
    },
    {
        "key": "p06", "num": 6, "title": "Eingrenzung und Abgleich",
        "points": [("Den verdächtigen Umfang finden", "Finden Sie den verdächtigen Umfang"),
                   ("Sperren: physisch und im System", "Sperren Sie diesen Bestand"),
                   ("Nach Risiko prüfen", "Prüfen Sie ihn nach Risiko"),
                   ("Jede Einheit abgleichen", "Dann gleichen Sie jede Einheit ab")],
        "example": "2.000 verdächtige Kameras: gut geprüft + durchgefallen + wartend müssen genau aufgehen. "
                   "Keine Einheit darf verschwinden.",
        "example_cue": "Farhan hatte zweitausend",
        "script": "Eingrenzung ist eine Barriere, keine Heilung. Finden Sie den verdächtigen Umfang nach "
                  "Seriennummer, Auftrag und Schicht. Sperren Sie diesen Bestand, physisch und im System. "
                  "Prüfen Sie ihn nach Risiko. Dann gleichen Sie jede Einheit ab. Farhan hatte zweitausend "
                  "verdächtige Kameras. Die meisten waren gut, einige fielen durch, der Rest wartete noch. "
                  "Die Zahlen müssen genau aufgehen. Keine Einheit darf einfach verschwinden. Wo verfolgt "
                  "das Team all das?",
    },
    {
        "key": "p07", "num": 7, "title": "Die QRQC-Tafel und Besprechung",
        "points": [("Risiko, Eingrenzung, Ursache, Maßnahme, Verantwortlicher, Termin", "Jedes Problem zeigt"),
                   ("Rot offen · Gelb in Prüfung · Grün bewiesen", "Nutzen Sie Rot für offen"),
                   ("Echte Muster und Trenddiagramme mitbringen", "Bringen Sie echte Muster"),
                   ("Nichts „erledigt\" ohne Beweis", "achten Sie auf Besprechungstheater")],
        "example": "Farhans 15-Minuten-Besprechung: neue Probleme, dann Eingrenzung, dann Maßnahmen und "
                   "Eskalationen.",
        "example_cue": "Farhan hält jede Schicht",
        "script": "Die QRQC-Tafel ist Ihre Leitstelle. Jedes Problem zeigt Risiko, Eingrenzung, Ursache, "
                  "Maßnahme, Verantwortlichen und Termin. Nutzen Sie Rot für offen, Gelb für in Prüfung, "
                  "und Grün nur für bewiesenen Abschluss. Farhan hält jede Schicht eine fünfzehnminütige "
                  "Besprechung an der Tafel. Zuerst neue Probleme, dann Eingrenzung, dann Maßnahmen und "
                  "Eskalationen. Bringen Sie echte Muster und Trenddiagramme mit. Und achten Sie auf "
                  "Besprechungstheater. Ist etwas ohne Beweis erledigt?",
    },
    {
        "key": "p08", "num": 8, "title": "Grundursache mit Belegen",
        "points": [("Fünf Warum = eine Hypothese, kein Beweis", "Eine Kette aus fünf Warum"),
                   ("Den Fehler sicher nachstellen", "Stellen Sie den Fehler"),
                   ("Ursachen über die 6M sammeln", "Sammeln Sie Ursachen über"),
                   ("Entstanden · durchgerutscht · vom System zugelassen", "Suchen Sie drei Ursachen")],
        "example": "Ein Fischgrätendiagramm allein reicht nicht: jede konkurrierende Idee muss getestet "
                   "werden.",
        "example_cue": "Dann testen Sie die konkurrierenden Ideen",
        "script": "Nun finden Sie die Grundursache, mit Belegen. Eine Kette aus fünf Warum ist eine "
                  "Hypothese, kein Beweis. Stellen Sie den Fehler sicher nach, wenn möglich. Sammeln Sie "
                  "Ursachen über Mensch, Maschine, Methode, Material, Messung und Umwelt. Dann testen Sie "
                  "die konkurrierenden Ideen. Suchen Sie drei Ursachen. Warum es entstand, warum es "
                  "durchrutschte, und was im System beides zuließ. Sehen Sie, warum ein Fischgrätendiagramm "
                  "allein nicht reicht?",
    },
    {
        "key": "p09", "num": 9, "title": "Korrekturmaßnahme und Änderungslenkung",
        "points": [("Beheben, wie es entstand und wie es durchrutschte", "Gehen Sie beides an"),
                   ("Technische Sperren statt Erinnerungen", "Bevorzugen Sie technische Sperren"),
                   ("Zykluszeit, Sicherheit, Fehlablehnungen prüfen", "Prüfen Sie die Wirkung"),
                   ("FMEA, SOP, Schulung aktualisieren", "Dann aktualisieren Sie die FMEA")],
        "example": "Ein mündliches „Vorrichtung prüfen\" wurde ein Scan: jede Vorrichtung mit ihrem "
                   "freigegebenen Rezept verknüpft.",
        "example_cue": "An Farhans Linie",
        "script": "Nun beheben Sie jede bestätigte Ursache. Gehen Sie beides an, wie es entstand, und wie "
                  "es durchrutschte. Bevorzugen Sie technische Sperren, wie codierte Vorrichtungen und "
                  "Scan-Verriegelungen, statt Erinnerungen. Prüfen Sie die Wirkung auf Zykluszeit, "
                  "Sicherheit und Fehlablehnungen. Dann aktualisieren Sie die FMEA, die SOP und die "
                  "Schulung. An Farhans Linie wurde eine mündliche Anweisung, die Vorrichtung zu prüfen, "
                  "ein Scan. Jede Vorrichtung ist jetzt mit ihrem Rezept verknüpft. Wann schließen Sie ab?",
    },
    {
        "key": "p10", "num": 10, "title": "Abschlusskriterien",
        "points": [("Eingebaut ≠ bewiesen", "Eine Lösung einbauen"),
                   ("Herausfordern: gute, schlechte, grenzwertige Teile", "fordern Sie sie heraus"),
                   ("Über Schichten, Modelle, Wechsel", "Prüfen Sie sie über Schichten"),
                   ("Jede verdächtige Einheit entschieden, dann Freigabe", "Sorgen Sie dafür, dass jede")],
        "example": "Farhans Regel: zehn Produktionstage ohne Wiederholung, bevor die Tafel grün wird.",
        "example_cue": "Farhan wartet zehn",
        "script": "Hier ist die Falle. Eine Lösung einbauen ist nicht dasselbe wie sie beweisen. Zum "
                  "Abschluss fordern Sie sie heraus, mit bekannt guten, bekannt schlechten und "
                  "grenzwertigen Teilen. Prüfen Sie sie über Schichten, Modelle und Wechsel. Verfolgen Sie "
                  "Wiederholung und Ausbeute über eine feste Zeit. Sorgen Sie dafür, dass jede verdächtige "
                  "Einheit entschieden ist. Dann geben Qualität und Verantwortlicher frei. Farhan wartet "
                  "zehn Produktionstage ohne Wiederholung. Erst dann wird die Tafel grün. Wie messen Sie "
                  "das alles?",
    },
    {
        "key": "p11", "num": 11, "title": "QRQC-KPI",
        "points": [("Reaktionszeit: Erkennung → Eingrenzung", "Die Reaktionszeit läuft"),
                   ("Eingrenzungsabdeckung %", "Die Eingrenzungsabdeckung ist"),
                   ("Erstdurchlaufquote und Fehlerrate", "Verfolgen Sie die Erstdurchlaufquote"),
                   ("Pünktlicher Abschluss der Maßnahmen", "messen Sie den pünktlichen Abschluss")],
        "example": "95 % der verdächtigen Einheiten gefunden = nicht fertig: 5 % sind noch draußen.",
        "example_cue": "Wenn Sie fünfundneunzig",
        "script": "Nutzen Sie ausgewogene Kennzahlen. Die Reaktionszeit läuft von der Erkennung bis zur "
                  "ersten wirksamen Eingrenzung. Die Eingrenzungsabdeckung ist der Anteil der verdächtigen "
                  "Einheiten, die Sie erfasst haben. Verfolgen Sie die Erstdurchlaufquote und die "
                  "Fehlerrate. Und messen Sie den pünktlichen Abschluss der Maßnahmen. Eine feine Sache. "
                  "Wenn Sie fünfundneunzig Prozent der verdächtigen Einheiten gefunden haben, sind Sie "
                  "nicht fertig. Fünf Prozent sind noch draußen. Bereit für Farhans Fall?",
    },
    {
        "key": "p12", "num": 12, "title": "Fallstudie: Fokusfehler",
        "points": [("24 von 800 fallen im Fokus durch, normal < 0,5 %", "Nach dem Wechsel"),
                   ("Auftrag + Ausstoß seit dem letzten guten Einrichten sperren", "Farhan sperrte den Auftrag"),
                   ("Vorrichtung, Rezept, Fokustrend vergleichen", "Das Team verglich"),
                   ("Die Rezept-Hypothese testen", "Ihre Hypothese war")],
        "example": "Das falsche Fokusrezept stellte den Fehler an kontrollierten Mustern nach. Erst dann "
                   "galt es als Ursache.",
        "example_cue": "Also testeten sie es",
        "script": "Hier die ganze Geschichte. Nach dem Wechsel fielen vierundzwanzig von achthundert "
                  "Kameras im Fokus durch. Normal waren unter ein halbes Prozent. Farhan sperrte den "
                  "Auftrag, und alles seit dem letzten guten Einrichten. Das Team verglich "
                  "Vorrichtungsdaten, Rezeptversionen und Fokustrends. Ihre Hypothese war das falsche "
                  "Fokusrezept. Also testeten sie es an kontrollierten Mustern, und der Fehler trat wieder "
                  "auf. Erst dann nannten sie es die Ursache. Hätte Ihr Team gewartet?",
    },
    {
        "key": "p13", "num": 13, "title": "Fallstudie: falsches Etikett",
        "points": [("Kartonetikett ≠ Gerät darin", "Ein Karton für Videorekorder"),
                   ("Palette sperren, jede Seriennummer abgleichen", "Das Team sperrte die Palette"),
                   ("Scans und Druckaufträge zurückverfolgen", "Dann verfolgten sie"),
                   ("Abgleich Seriennummer–SKU erzwingen, Umgehungen protokollieren", "Also erzwang die Lösung")],
        "example": "Grundursache: der MES-Abgleich war bei einer Druckerstörung abgeschaltet worden, und "
                   "niemand protokollierte es.",
        "example_cue": "Der MES-Abgleich war",
        "script": "Ein zweiter Fall, aus der Verpackung. Ein Karton für Videorekorder zeigte die falsche "
                  "SKU. Das Produkt darin funktionierte einwandfrei. Aber der Kunde bekäme trotzdem den "
                  "falschen Artikel. Das Team sperrte die Palette, und glich jede Seriennummer mit ihrem "
                  "Etikett ab. Dann verfolgten sie Scans und Druckaufträge zurück. Der MES-Abgleich war bei "
                  "einer Druckerstörung abgeschaltet worden. Niemand protokollierte es. Also erzwang die "
                  "Lösung einen Abgleich von Seriennummer und SKU vor dem Druck, und protokollierte jede "
                  "Umgehung. Hätten Sie dort gesucht?",
    },
    {
        "key": "p14", "num": 14, "title": "Einführung in 90 Tagen",
        "points": [("Zuerst einen Pilotbereich mit hohem Risiko", "Beginnen Sie mit einem Pilotbereich"),
                   ("Tag 1–30: Auslöser, Stufen, Tafel", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: Leiter schulen, Besprechungen führen", "In den nächsten dreißig"),
                   ("Tag 61–90: auditieren, mit FMEA verknüpfen, ausweiten", "In den letzten dreißig")],
        "example": "Führen Sie QRQC wie ein Betriebssystem ein, nicht als einzelnes Formular.",
        "example_cue": "führen Sie QRQC wie ein Betriebssystem",
        "script": "Nun führen Sie QRQC wie ein Betriebssystem ein, nicht als einzelnes Formular. Beginnen "
                  "Sie mit einem Pilotbereich mit hohem Risiko, und machen Sie die Methode dort stabil. In "
                  "den ersten dreißig Tagen legen Sie Auslöser, Stufen und die Tafel fest. In den nächsten "
                  "dreißig schulen Sie Ihre Linienleiter und führen die Besprechungen. In den letzten "
                  "dreißig auditieren Sie die Maßnahmen, verknüpfen sie mit der FMEA, und weiten auf andere "
                  "Linien aus. Wer verantwortet was?",
    },
    {
        "key": "p15", "num": 15, "title": "Der Problembericht und die Rollen",
        "points": [("Werksleiter fördert", "Der Werksleiter fördert"),
                   ("Qualität verantwortet die Methode", "Die Qualität verantwortet"),
                   ("Produktion verantwortet die Reaktion", "Die Produktion verantwortet"),
                   ("Technik verantwortet die technischen Lösungen", "Und die Technik verantwortet"),
                   ("Ein Bericht für jedes Problem", "Führen Sie einen Bericht")],
        "example": "Der Test: Könnte jemand das ganze Ereignis nur aus Ihrem Bericht nachbauen?",
        "example_cue": "Könnte jemand das ganze",
        "script": "Der Werksleiter fördert es. Die Qualität verantwortet die Methode. Die Produktion "
                  "verantwortet die sofortige Reaktion. Und die Technik verantwortet die technischen "
                  "Lösungen. Führen Sie einen Bericht für jedes Problem. Er enthält Problem, Fotos und das "
                  "Verdachtsfenster. Dazu Eingrenzung und Abgleich, Ursachen, Maßnahmen und Beweis. Hier "
                  "ist der Test. Könnte jemand das ganze Ereignis nur aus Ihrem Bericht nachbauen? "
                  "Reagieren Sie schnell, aber schließen Sie immer mit Belegen.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Erkennen, sichtbar machen", "icon": "sensor", "with": 0},
        {"label": "Eingrenzen: den Kunden schützen", "icon": "lock", "with": 1},
        {"label": "Ursache mit Fakten, Lösung beweisen", "icon": "search", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Tester zurücksetzen", "sub": "und weiterlaufen", "icon": "power"},
            {"label": "Den Auftrag sperren", "sub": "Hier beginnt QRQC", "icon": "lock"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Echter Ort, echte Teile", "icon": "walk"}, {"label": "Fakten, nie Schuld", "icon": "search"},
        {"label": "Sofort reagieren", "icon": "warning"}, {"label": "Eingrenzung ist nicht die Lösung", "icon": "lock"}]},
    "p03": {"type": "flow", "items": [
        {"label": "Stufe 1: Linie oder Schicht", "sub": "Stoppen, aussortieren, festhalten", "icon": "person", "with": 0},
        {"label": "Stufe 2: bereichsübergreifendes Team", "sub": "Untersuchen und handeln", "icon": "gear", "with": 1},
        {"label": "Stufe 3: Werksleitung", "sub": "Mittel, der Kunde", "icon": "shield", "with": 2}]},
    "p04": {"type": "timeline", "items": [
        {"label": "Erkennen, Station und Los finden, sperren", "sub": "0–5", "span": 5, "icon": "sensor"},
        {"label": "Leitung und Qualität informieren, Muster aufheben", "sub": "Dann", "span": 8, "icon": "person"},
        {"label": "Letzten bekannten guten Punkt finden", "sub": "Danach", "span": 7, "icon": "search"},
        {"label": "Sperren, erfassen, zuweisen", "sub": "Bis 30", "span": 10, "icon": "lock"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Was, wo, wann, wer", "icon": "search", "with": 0},
        {"label": "Wie erkannt, wie viele", "icon": "count", "with": 1},
        {"label": "Ausschuss oder Verdacht", "icon": "stack", "with": 2}],
        "then": {"type": "stat", "value": 24, "suffix": " / 800", "icon": "camera", "label": "Kameras im Fokus durchgefallen",
                 "unit": "10 Uhr bis Mittag, direkt nach einem Wechsel der Linsenvorrichtung", "with": "example"}},
    "p06": {"type": "icons", "items": [
        {"label": "Umfang finden", "icon": "search"}, {"label": "Sperren", "icon": "lock"},
        {"label": "Nach Risiko prüfen", "icon": "test"}, {"label": "Abgleichen", "icon": "count"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "2.000 verdächtige Kameras", "icon": "stack", "with": "example"},
            {"label": "Gut + durchgefallen + wartend", "icon": "count", "with": "example"},
            {"label": "= 2.000: keine fehlt", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Offen", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "In Prüfung", "icon": "clock", "with": 1},
        {"label": "Bewiesen", "sub": "Erst dann: grün", "icon": "check", "tone": "good", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Neue Probleme", "icon": "warning", "with": "example"},
            {"label": "Eingrenzung", "icon": "lock", "with": "example"},
            {"label": "Maßnahmen, Eskalationen", "icon": "sequence", "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Mensch", "icon": "person", "with": 2}, {"label": "Maschine", "icon": "gear", "with": 2},
        {"label": "Methode", "icon": "clipboard", "with": 2}, {"label": "Material", "icon": "box", "with": 2},
        {"label": "Messung", "icon": "scale", "with": 2}, {"label": "Umwelt", "icon": "wave", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Entstanden + durchgerutscht", "icon": "search"}, {"label": "Technische Sperren", "icon": "key"},
        {"label": "Zykluszeit, Sicherheit", "icon": "clock"}, {"label": "FMEA, SOP, Schulung", "icon": "clipboard"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "„Vorrichtung prüfen\"", "sub": "Eine mündliche Erinnerung", "icon": "person"},
            {"label": "Vorrichtungs-Scan", "sub": "Mit ihrem freigegebenen Rezept verknüpft", "icon": "barcode"}]}},
    "p10": {"type": "icons", "items": [
        {"label": "Eingebaut ist nicht bewiesen", "icon": "cross", "tone": "bad"}, {"label": "Herausfordern", "icon": "test"},
        {"label": "Über Schichten, Modelle", "icon": "sequence"}, {"label": "Jede Einheit entschieden", "icon": "check"}],
        "then": {"type": "stat", "value": 10, "suffix": " Tage", "icon": "calendar", "label": "Produktion ohne Wiederholung",
                 "unit": "bevor die Tafel grün wird", "with": "example"}},
    "p11": {"type": "icons", "items": [
        {"label": "Reaktionszeit", "icon": "clock"}, {"label": "Eingrenzungsabdeckung", "icon": "count"},
        {"label": "Ausbeute, Fehlerrate", "icon": "chartUp"}, {"label": "Pünktlicher Abschluss", "icon": "calendar"}],
        "then": {"type": "stat", "value": 5, "suffix": "%", "icon": "warning", "label": "der verdächtigen Einheiten noch draußen",
                 "unit": "95 % gefunden ist nicht fertig", "with": "example"}},
    "p12": {"type": "flow", "items": [
        {"label": "24 von 800 fallen im Fokus durch", "sub": "Normal: unter 0,5 %", "icon": "camera", "tone": "bad", "with": 0},
        {"label": "Sperren seit dem letzten guten Einrichten", "icon": "lock", "with": 1},
        {"label": "Vorrichtung, Rezept, Trend vergleichen", "icon": "search", "with": 2},
        {"label": "Falsches Rezept stellte es nach", "sub": "Erst dann: die Ursache", "icon": "test", "tone": "good", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Kartonetikett ≠ Gerät", "icon": "label", "tone": "bad", "with": 0},
        {"label": "Palette sperren, Seriennummern abgleichen", "icon": "lock", "with": 1},
        {"label": "MES-Abgleich abgeschaltet", "sub": "Bei einer Druckerstörung, nicht protokolliert", "icon": "warning", "tone": "bad", "with": "example"},
        {"label": "Abgleich Seriennummer–SKU erzwungen", "sub": "Jede Umgehung protokolliert", "icon": "barcode", "tone": "good", "with": 3}]},
    "p14": {"type": "timeline", "items": [
        {"label": "Auslöser, Stufen, Tafel", "sub": "Tag 1–30", "icon": "clipboard", "with": 1},
        {"label": "Leiter schulen, Besprechungen führen", "sub": "31–60", "icon": "person", "with": 2},
        {"label": "Auditieren, mit FMEA verknüpfen, ausweiten", "sub": "61–90", "icon": "chartUp", "with": 3}]},
    "p15": {"type": "icons", "items": [
        {"label": "Werksleiter", "sub": "Fördert", "icon": "person"}, {"label": "Qualität", "sub": "Die Methode", "icon": "shield"},
        {"label": "Produktion", "sub": "Die Reaktion", "icon": "wrench"}, {"label": "Technik", "sub": "Die Lösungen", "icon": "gear"},
        {"label": "Ein Bericht", "sub": "Jedes Problem", "icon": "clipboard"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "1.900 von 2.000 verdächtigen Einheiten wurden gefunden und geprüft. Ist die Eingrenzung "
                    "vollständig?",
        "options": ["Ja, 95 % reichen", "Nein, 100 verdächtige Einheiten fehlen noch",
                    "Ja, wenn die Lösung eingebaut ist"],
        "correct": 1,
        "explanation": "Eine Eingrenzungsabdeckung von 95 % heißt, 5 % der verdächtigen Menge sind noch draußen. "
                       "Die Eingrenzung ist erst vollständig, wenn jede Einheit erfasst ist.",
        "q_script": "Kurzer Check. Neunzehnhundert von zweitausend verdächtigen Einheiten wurden gefunden und "
                    "geprüft. Ist die Eingrenzung vollständig? Nehmen Sie sich kurz Zeit.",
        "a_script": "Nein. Hundert verdächtige Einheiten fehlen noch. Die Eingrenzung ist erst vollständig, "
                    "wenn jede Einheit gefunden ist.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Fokusfehler steigen im Test direkt nach einem Vorrichtungswechsel. Der Tester wird "
                    "zurückgesetzt und besteht. Was sollte ZUERST passieren?",
        "options": ["Weiterlaufen, der Tester hat bestanden", "Einheiten seit dem letzten guten Einrichten sperren und die Belege festhalten",
                    "Die Vorrichtung zurückwechseln und nichts sagen", "Auf die Besprechung am Tagesende warten"],
        "correct": 1,
        "explanation": "Zuerst den Kunden schützen: alles seit dem letzten bestätigten Einrichten sperren, "
                       "Muster und Daten aufheben, dann untersuchen. Den Tester zurückzusetzen verbirgt die "
                       "Abweichung.",
        "q_script": "Noch eine, ein Szenario. Fokusfehler steigen direkt nach einem Vorrichtungswechsel. "
                    "Jemand setzt den Tester zurück, und er besteht. Was sollte zuerst passieren? Überlegen "
                    "Sie kurz.",
        "a_script": "Sperren Sie jede Einheit seit dem letzten guten Einrichten, und halten Sie die Belege "
                    "fest. Dann untersuchen Sie. Den Tester zurückzusetzen verbirgt das Problem nur.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
