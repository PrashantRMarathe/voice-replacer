"""poka_yoke in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh poka_yoke_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "pk_de"
NAME = "poka_yoke_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Shigeo Shingo": "Schigeo Schingo",
    "Poka Yokes": "Poka Joke",
    "Poka Yoke": "Poka Joke",
    "Pareto": "Pareto",
    "QRQC": "ku err ku ze",
    "FMEA": "eff emm e a",
    "NVR": "enn fau err",
    "MES": "emm e ess",
    "SOP": "ess o pe",
    "PPM": "pe pe emm",
    "SMT": "ess emm te",
    "BOM": "be o emm",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Achtzehn Videorekorder wurden mit einer fehlenden Schraube ausgeliefert. Die Werkerin "
    "war geschickt und sorgfältig. Sie war einfach ein Mensch. Kommt Ihnen das bekannt vor? "
    "In dieser Lektion lernen Sie Poka Yoke kennen, also Fehlersicherheit. Sie sehen, wie man "
    "einen Prozess so gestaltet, dass die falsche Handlung unmöglich ist oder sofort erkannt "
    "wird. Wir begleiten Divya, Prozessingenieurin an einer NVR-Montagelinie, die das "
    "Gedächtnis aus der Qualität herausnimmt."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Fehler sind vorhersehbar, also konstruieren Sie sie heraus. "
    "Vermeiden ist besser als Erkennen, und Erkennen besser als Warnen. Und prüfen Sie jede "
    "Vorrichtung mit schlechten Mustern, damit Sie wissen, dass sie noch funktioniert. Ihre "
    "Aufgabe für diese Woche. Suchen Sie eine Prüfung an Ihrer Linie, die auf dem Gedächtnis "
    "beruht, und skizzieren Sie ein Poka Yoke dafür. Gut gemacht, Lektion abgeschlossen. Als "
    "Nächstes lernen Sie QRQC kennen, die Qualitätskontrolle mit schneller Reaktion."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Poka Yoke ist",
        "points": [("Japanisch für Fehlersicherheit", "Poka Yoke ist Japanisch"),
                   ("Verlassen Sie sich nicht auf das Gedächtnis", "Verlassen Sie sich nicht darauf"),
                   ("Falsche Handlung unmöglich oder sofort sichtbar", "Gestalten Sie den Prozess so")],
        "example": "Divya ersetzte einen Aufkleber „Ausrichtung prüfen“ durch einen codierten Stecker. Ein "
                   "Aufkleber warnt. Eine Codierung verhindert.",
        "example_cue": "An Divyas Linie klebte ein Aufkleber",
        "script": "Hier ist die Kernidee. Poka Yoke ist Japanisch für Fehlersicherheit. Verlassen Sie sich "
                  "nicht darauf, dass jemand daran denkt, das Richtige zu tun. Gestalten Sie den Prozess "
                  "so, dass die falsche Handlung nicht passieren kann oder sofort auffällt. An Divyas Linie "
                  "klebte ein Aufkleber mit dem Hinweis, die Ausrichtung des Steckers zu prüfen. Sie "
                  "ersetzte ihn durch einen codierten Stecker, der nur in einer Richtung passt. Ein "
                  "Aufkleber warnt. Eine Codierung verhindert. Woher kommt diese Idee?",
    },
    {
        "key": "p02", "num": 2, "title": "Fehler oder Defekt",
        "points": [("Aus dem Toyota-Produktionssystem", "Poka Yoke entstand"),
                   ("Fehler: die falsche Handlung", "Der Fehler ist die falsche Handlung"),
                   ("Defekt: das schlechte Produkt, das folgt", "Der Defekt ist das schlechte Produkt"),
                   ("Stoppen Sie den Fehler, bevor er ein Defekt wird", "Sie stoppen den Fehler")],
        "example": "Die Endkontrolle findet Probleme erst, wenn Arbeit und Teile schon verbraucht sind.",
        "example_cue": "Die Endkontrolle findet",
        "script": "Poka Yoke entstand im Toyota-Produktionssystem, durch den Ingenieur Shigeo Shingo. Seine "
                  "zentrale Erkenntnis war einfach. Ein Fehler und ein Defekt sind verschieden. Der Fehler "
                  "ist die falsche Handlung, zum Beispiel einen Stecker verkehrt herum stecken. Der Defekt "
                  "ist das schlechte Produkt, das daraus folgt. Sie stoppen den Fehler, bevor er zum Defekt "
                  "wird. Die Endkontrolle findet Probleme erst, wenn Arbeit und Teile schon verbraucht "
                  "sind. Warum so lange warten?",
    },
    {
        "key": "p03", "num": 3, "title": "Die Hierarchie der Maßnahmen",
        "points": [("1 Beseitigen: asymmetrische Zentrierstifte", "Am besten beseitigen"),
                   ("2 Verhindern: Barcode-Verriegelung", "Als Nächstes verhindern"),
                   ("3 Erkennen und stoppen: Sensor für fehlende Schrauben", "Dann erkennen und stoppen"),
                   ("4 Warnen: ein Alarm", "Noch schwächer"),
                   ("5 Später prüfen — am schwächsten", "Am schwächsten, später prüfen")],
        "example": "Wählen Sie Maßnahmen danach, wie zuverlässig sie Fehler stoppen — nicht danach, wie "
                   "leicht sie einzubauen sind.",
        "example_cue": "Wählen Sie Maßnahmen danach, wie zuverlässig",
        "script": "Nicht alle Maßnahmen sind gleich. Hier ist die Rangfolge der Stärke. Am besten "
                  "beseitigen Sie die Fehlermöglichkeit, mit asymmetrischen Zentrierstiften. Als Nächstes "
                  "verhindern Sie die falsche Handlung, zum Beispiel mit einer Barcode-Verriegelung. Dann "
                  "erkennen und stoppen, wie ein Sensor, der eine fehlende Schraube bemerkt. Noch schwächer "
                  "ist ein Warnalarm. Am schwächsten, später prüfen. Wählen Sie Maßnahmen danach, wie "
                  "zuverlässig sie Fehler stoppen, nicht danach, wie leicht sie einzubauen sind. Auf "
                  "welcher Stufe stehen Ihre Prüfungen heute?",
    },
    {
        "key": "p04", "num": 4, "title": "Konstruktionsregeln",
        "points": [("Ein positives Gutsignal, nicht „kein Alarm“", "Erstens, achten Sie"),
                   ("Sicher bei Strom- oder Sensorausfall", "Zweitens muss die Maßnahme"),
                   ("Überbrückung: selten, protokolliert, befristet", "Drittens machen Sie jede Überbrückung"),
                   ("Mit falschen Bedingungen testen", "Viertens behaupten Sie nie")],
        "example": "Divya zog bei einem Versuch das Sensorkabel. Die Vorrichtung blieb verriegelt.",
        "example_cue": "Divya zog bei einem Versuch",
        "script": "Befolgen Sie vier Konstruktionsregeln. Erstens, achten Sie auf ein positives Gutsignal, "
                  "nicht nur auf fehlenden Alarm. Zweitens muss die Maßnahme in einen sicheren Zustand "
                  "gehen. Fällt Strom oder ein Sensor aus, stoppt sie. Drittens machen Sie jede "
                  "Überbrückung selten, protokolliert und befristet. Viertens behaupten Sie nie, dass sie "
                  "funktioniert, ohne Test mit falschen Bedingungen. Divya zog bei einem Versuch das "
                  "Sensorkabel. Die Vorrichtung blieb verriegelt. Welche Arten von Poka Yoke gibt es?",
    },
    {
        "key": "p05", "num": 5, "title": "Drei Methoden",
        "points": [("Kontakt: Form, Größe, Position", "Die Kontaktmethode"),
                   ("Festwert: die richtige Anzahl", "Die Festwertmethode"),
                   ("Bewegungsschritt: die richtige Reihenfolge", "Die Bewegungsschrittmethode")],
        "example": "Ausrichtungsproblem → Kontakt. Fehlendes Teil → Festwert. Scannen, programmieren, "
                   "testen, etikettieren in Reihenfolge → Bewegungsschritt.",
        "example_cue": "Ein Ausrichtungsproblem",
        "script": "Es gibt drei klassische Methoden. Die Kontaktmethode unterscheidet Richtig und Falsch "
                  "über Form, Größe oder Position. Ein asymmetrisches Nest ist ein Beispiel. Die "
                  "Festwertmethode prüft die Anzahl, wie ein Zähler für alle sechs Schrauben. Die "
                  "Bewegungsschrittmethode prüft die Reihenfolge. Scannen, programmieren, testen, dann "
                  "etikettieren. Jede kann verhindern oder erkennen. Ein Ausrichtungsproblem? Kontakt. Ein "
                  "fehlendes Teil? Festwert.",
    },
    {
        "key": "p06", "num": 6, "title": "Menschliche Fehler sind vorhersehbar",
        "points": [("Menschliche Fehler sind vorhersehbar", "Menschliche Fehler sind vorhersehbar"),
                   ("Auslassen, falsches Teil, vertauscht, falsche Reihenfolge", "Menschen lassen Schritte aus"),
                   ("Fragen Sie, was es möglich machte, nicht wer", "Fragen Sie also, was")],
        "example": "Falsche Firmware → ähnliche Rezeptnamen → Modell von Hand gewählt → MES-Scan nicht mit "
                   "dem Programmiergerät verbunden.",
        "example_cue": "Divya verfolgte falsche Firmware",
        "script": "Menschliche Fehler sind vorhersehbar, also behandeln Sie sie als Systemrisiken. Menschen "
                  "lassen Schritte aus, nehmen das falsche Teil, vertauschen Dinge oder machen Schritte in "
                  "falscher Reihenfolge. Sie geben die falsche Einstellung ein oder verwechseln Etiketten. "
                  "Fragen Sie also, was den Fehler möglich machte, nicht wer ihn gemacht hat. Divya "
                  "verfolgte falsche Firmware bis zu Rezepten mit ähnlichen Namen zurück. Das Modell wurde "
                  "von Hand gewählt. Der MES-Scan war nicht mit dem Programmiergerät verbunden. Sehen Sie "
                  "die Lösung schon?",
    },
    {
        "key": "p07", "num": 7, "title": "Eine Konstruktionsmethode in 8 Schritten",
        "points": [("Definieren, beobachten, messen, Ursache finden", "Definieren Sie den Defekt"),
                   ("Die einfachste robuste Idee wählen", "Wählen Sie die einfachste"),
                   ("Prototyp bauen und mit schlechten Teilen prüfen", "Bauen Sie einen Prototyp"),
                   ("SOP aktualisieren, schulen, überwachen", "Dann aktualisieren Sie die SOP")],
        "example": "Legen Sie den Erfolg vor dem Einbau fest: falsche Teile abgewiesen, gute Teile "
                   "durchgelassen, Takt gehalten.",
        "example_cue": "Bevor Sie irgendetwas einbauen",
        "script": "Arbeiten Sie im bereichsübergreifenden Team, in acht Schritten. Definieren Sie den "
                  "Defekt. Beobachten Sie den realen Arbeitsgang, und finden Sie, wo der Fehler entsteht. "
                  "Messen Sie die Ausgangslage, und finden Sie die Ursache. Wählen Sie die einfachste "
                  "robuste Idee. Bauen Sie einen Prototyp, und prüfen Sie ihn mit guten und schlechten "
                  "Teilen. Dann aktualisieren Sie die SOP, schulen und überwachen. Bevor Sie irgendetwas "
                  "einbauen, legen Sie den Erfolg fest. Falsche Teile abgewiesen, gute durchgelassen, und "
                  "das Tempo hält.",
    },
    {
        "key": "p08", "num": 8, "title": "Anwendungen in der Montage",
        "points": [("Drehmomentsignal mit dem Auftrag verknüpft", "Sie verknüpfte das Drehmomentsignal"),
                   ("Vorrichtung gibt nur frei, wenn jede Schraube gut ist", "Die Vorrichtung gibt nur frei"),
                   ("Codierte Stecker, Dichtungssensor", "Sie ergänzte auch codierte")],
        "example": "Fehlende Schrauben: 18 von 10.000 → 1 von 10.000, etwa 94 % weniger.",
        "example_cue": "Fehlende Schrauben sanken",
        "script": "Gehen wir jetzt an Divyas Montagelinie. Fehlende Schrauben waren das große Problem. Sie "
                  "verknüpfte das Drehmomentsignal des Schraubers mit dem Fertigungsauftrag. Die "
                  "Vorrichtung gibt nur frei, wenn jede Schraube ein gutes Ergebnis hat. Eine Magnetschale "
                  "konnte das nicht beweisen. Fehlende Schrauben sanken von achtzehn pro zehntausend auf "
                  "eine. Das sind etwa vierundneunzig Prozent weniger. Sie ergänzte auch codierte Stecker "
                  "und einen Dichtungssensor vor dem Schließen. Und die Platinen im Inneren?",
    },
    {
        "key": "p09", "num": 9, "title": "Anwendungen in SMT und Test",
        "points": [("Jede Feeder-Rolle gegen die BOM gescannt", "Scannen Sie also jede Feeder-Rolle"),
                   ("Programmversion vor dem Start geprüft", "Prüfen Sie die Programmversion"),
                   ("Seriennummer an Modell, Firmware und Gutergebnis gebunden", "Binden Sie im Test jede"),
                   ("Ein Netzwerkausfall darf nie „bestanden“ ergeben", "Und stellen Sie sicher, dass ein Netzwerkausfall")],
        "example": "Divyas Tester kann ohne Gutergebnis für diese Seriennummer kein Etikett drucken.",
        "example_cue": "Divyas Tester kann kein Etikett drucken",
        "script": "Auf der Platinenlinie können falsche Einstellungen sehr schnell Tausende Defekte "
                  "erzeugen. Scannen Sie also jede Feeder-Rolle gegen die Stückliste. Prüfen Sie die "
                  "Programmversion, bevor die Maschine startet. Binden Sie im Test jede Seriennummer an ihr "
                  "Modell, ihre Firmware und ihr Gutergebnis. Divyas Tester kann kein Etikett drucken ohne "
                  "dieses Ergebnis. Und stellen Sie sicher, dass ein Netzwerkausfall nie ein falsches "
                  "Bestanden erzeugen kann. Haben Sie Ihren so getestet?",
    },
    {
        "key": "p10", "num": 10, "title": "Verpackung und Versand",
        "points": [("Seriennummer scannen + mit dem Kartonetikett abgleichen", "Scannen Sie also die Seriennummer"),
                   ("Zubehör vor dem Verschließen gezählt", "zählen Sie das Zubehör"),
                   ("Gewichtskontrollen haben blinde Flecken", "Gewichtskontrollen helfen"),
                   ("Barcodes lassen sich austricksen", "ein Barcode ist nicht automatisch")],
        "example": "Ein falsches Netzteil wog so viel wie das richtige — eine geformte Kit-Schale hat es "
                   "erkannt.",
        "example_cue": "Divya fand ein falsches Netzteil",
        "script": "Ein perfektes Produkt kann beim Verpacken trotzdem zur Reklamation werden. Scannen Sie "
                  "also die Seriennummer, gleichen Sie das Kartonetikett ab, und zählen Sie das Zubehör, "
                  "bevor der Karton schließt. Gewichtskontrollen helfen, aber sie haben blinde Flecken. "
                  "Divya fand ein falsches Netzteil, das genauso viel wog wie das richtige. Eine geformte "
                  "Kit-Schale hat es stattdessen erkannt. Und denken Sie daran, ein Barcode ist nicht "
                  "automatisch fehlersicher. Doppelte Etiketten und manuelle Übersteuerungen können ihn "
                  "austricksen. Muss also jede Lösung teuer sein?",
    },
    {
        "key": "p11", "num": 11, "title": "Kostengünstig und sicher",
        "points": [("Einfach: Stifte, Führungen, Schalter, Schalen", "Stifte, Führungen, Endschalter"),
                   ("Nie eine Quetschstelle schaffen", "Eine Vorrichtung darf nie"),
                   ("Qualitätssensoren sind keine Sicherheitssysteme", "ein normaler Qualitätssensor"),
                   ("Reinigung und Kalibrierung einplanen", "Planen Sie auch ihre Reinigung")],
        "example": "Divyas beste Vorrichtung kostete ₹1.200: zwei Stifte, die verhindern, dass die Rückwand "
                   "verkehrt herum montiert wird.",
        "example_cue": "Divyas beste Vorrichtung kostete",
        "script": "Überhaupt nicht. Viele der besten Poka Yokes sind einfach. Stifte, Führungen, "
                  "Endschalter, Zählschalen und Gut-Schlecht-Lehren. Divyas beste Vorrichtung kostete "
                  "zwölfhundert Rupien. Zwei Stifte, die verhindern, dass die Rückwand verkehrt herum "
                  "montiert wird. Aber Sicherheit geht vor. Eine Vorrichtung darf nie eine Quetschstelle "
                  "schaffen. Und ein normaler Qualitätssensor ist kein Sicherheitssystem. Planen Sie auch "
                  "ihre Reinigung und Kalibrierung ein. Wie sorgen Sie also dafür, dass es hält?",
    },
    {
        "key": "p12", "num": 12, "title": "FMEA, Kontrollplan und Audits",
        "points": [("FMEA: mit der Fehlerart verknüpfen", "In der FMEA"),
                   ("Kontrollplan: Methode und Reaktion", "Im Kontrollplan"),
                   ("Standardarbeit: Gutsignal, wer zurücksetzt", "In der Standardarbeit"),
                   ("Mit einem bekannten Schlechtteil auditieren", "Geben Sie ihr ein bekanntes Schlechtteil")],
        "example": "Divya gibt jeder Vorrichtung in jeder Schicht ein bekanntes Schlechtteil.",
        "example_cue": "Divya macht das in jeder Schicht",
        "script": "Bauen Sie jede Vorrichtung in Ihr Qualitätssystem ein. In der FMEA verknüpfen Sie sie "
                  "mit der Fehlerart, die sie beherrscht. Im Kontrollplan schreiben Sie die Methode und die "
                  "Reaktion auf. In der Standardarbeit zeigen Sie, wie ein Gutsignal aussieht und wer die "
                  "Vorrichtung zurücksetzen darf. Dann auditieren Sie sie. Prüfen Sie nicht nur, ob die "
                  "Vorrichtung existiert. Geben Sie ihr ein bekanntes Schlechtteil, und bestätigen Sie, "
                  "dass sie es abweist. Divya macht das in jeder Schicht. Wie messen Sie den Nutzen?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI und Einsparungen",
        "points": [("Fehler-PPM und Durchschlupf sinken", "Die Fehler-PPM"),
                   ("Erstdurchlaufquote steigt", "Die Erstdurchlaufquote sollte steigen"),
                   ("Fehlabweisungen beobachten", "Und beobachten Sie Fehlabweisungen")],
        "example": "60.000 Einheiten/Monat, Fehler von 0,8 % auf 0,2 % gesenkt ≈ ₹65.000 Einsparung pro "
                   "Monat, abzüglich Betriebskosten.",
        "example_cue": "Divyas Linie fertigt",
        "script": "Messen Sie das Ergebnis und den Zustand Ihrer Vorrichtung. Die Fehler-PPM und der "
                  "Durchschlupf zum Kunden sollten sinken. Die Erstdurchlaufquote sollte steigen. Und "
                  "beobachten Sie Fehlabweisungen. Ein Sensor, der ständig gute Einheiten abweist, "
                  "verleitet Menschen dazu, ihn zu überbrücken. Divyas Linie fertigt sechzigtausend "
                  "Einheiten im Monat. Die Fehler von fast einem Prozent auf ein Viertel davon zu senken, "
                  "spart etwa fünfundsechzigtausend Rupien im Monat. Ziehen Sie dann Ihre Betriebskosten "
                  "ab.",
    },
    {
        "key": "p14", "num": 14, "title": "90-Tage-Fahrplan",
        "points": [("Wochen 1–2: wichtigste Fehlerarten + Ausgangslage", "In den ersten zwei Wochen"),
                   ("Wochen 3–4: Konstruktionsoptionen, Logik festlegen", "In den nächsten zwei Wochen"),
                   ("Monat 2: Pilot an einer Station", "Im zweiten Monat"),
                   ("Monat 3: dokumentieren, schulen, übertragen", "Im letzten Monat")],
        "example": "Testen Sie im Pilot jede bekannte falsche Bedingung.",
        "example_cue": "testen Sie jede falsche Bedingung",
        "script": "Hier ist ein einfacher Neunzig-Tage-Plan. In den ersten zwei Wochen wählen Sie Ihre "
                  "wichtigsten Fehlerarten aus Pareto und FMEA, und legen eine Ausgangslage fest. In den "
                  "nächsten zwei Wochen entwerfen Sie Optionen und legen die Logik fest. Im zweiten Monat "
                  "machen Sie einen Pilot an einer Station, und testen Sie jede falsche Bedingung, die Sie "
                  "kennen. Im letzten Monat aktualisieren Sie die Dokumente, schulen die Menschen und "
                  "übertragen es dann auf andere Linien. Wer ist für welchen Teil verantwortlich?",
    },
    {
        "key": "p15", "num": 15, "title": "Freigabe-Checkliste",
        "points": [("Fehlerart klar, mit Ausgangslage", "Ist die Fehlerart klar"),
                   ("Sicherheit und Ergonomie geprüft", "Wurden Sicherheit und Ergonomie"),
                   ("Schlechtmuster an jedem Modell getestet", "Wurde sie an jedem Modell"),
                   ("Stromausfall, Offline, Überbrückung abgedeckt", "Kommt sie mit Stromausfall")],
        "example": "Die Produktion ist für die Station verantwortlich. Die Technik konstruiert sie. Die "
                   "Qualität prüft sie.",
        "example_cue": "Die Produktion ist für die Station verantwortlich",
        "script": "Die Produktion ist für die Station verantwortlich. Die Technik konstruiert sie, und die "
                  "Qualität prüft sie auf Herz und Nieren. Bevor Sie eine Vorrichtung freigeben, gehen Sie "
                  "eine letzte Checkliste durch. Ist die Fehlerart klar, mit einer Ausgangslage? Wurden "
                  "Sicherheit und Ergonomie geprüft? Wurde sie an jedem Modell mit Schlechtmustern "
                  "getestet? Kommt sie mit Stromausfall, Offline-Betrieb und Überbrückung zurecht? Das "
                  "beste Poka Yoke macht die richtige Handlung natürlich und die falsche unmöglich.",
    },
]

# The picture beside each page's boxes (same layouts and icons as English, German
# labels). Items appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "versus", "items": [
        {"label": "Ein Aufkleber warnt", "sub": "„Ausrichtung prüfen“", "icon": "sticker", "with": "example"},
        {"label": "Eine Codierung verhindert", "sub": "Passt nur in einer Richtung", "icon": "key", "with": "example"}]},
    "p02": {"type": "flow", "stop": {"after": 0, "label": "HIER STOPP", "with": 3}, "items": [
        {"label": "Fehler", "sub": "Die falsche Handlung", "icon": "hand", "tone": "bad", "with": 1},
        {"label": "Defekt", "sub": "Das schlechte Produkt", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Am Linienende gefunden", "sub": "Arbeit und Teile schon verbraucht", "icon": "search", "tone": "bad", "with": "example"}]},
    "p03": {"type": "ladder", "items": [
        {"label": "Beseitigen", "icon": "pin"}, {"label": "Verhindern", "icon": "barcode"},
        {"label": "Erkennen und stoppen", "icon": "sensor"}, {"label": "Warnen", "icon": "warning"},
        {"label": "Später prüfen", "icon": "search"}]},
    "p04": {"type": "icons", "items": [
        {"label": "Positives Gutsignal", "icon": "check"}, {"label": "Sicherer Zustand", "icon": "power"},
        {"label": "Überbrückung protokolliert", "icon": "lock"}, {"label": "Falsche Fälle testen", "icon": "test"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Kontakt", "sub": "Form, Größe, Position", "icon": "shape"},
        {"label": "Festwert", "sub": "Die richtige Anzahl", "icon": "count"},
        {"label": "Bewegungsschritt", "sub": "Die richtige Reihenfolge", "icon": "sequence"}]},
    "p06": {"type": "flow", "items": [
        {"label": "Ähnliche Rezeptnamen", "icon": "sticker", "tone": "bad", "with": 2},
        {"label": "Modell von Hand gewählt", "icon": "hand", "tone": "bad", "with": 2},
        {"label": "Falsche Firmware", "icon": "chip", "tone": "bad", "with": 2},
        {"label": "Lösung: den MES-Scan verknüpfen", "sub": "mit dem Programmiergerät", "icon": "barcode", "tone": "good", "with": "example"}]},
    "p07": {"type": "steps", "items": [
        {"label": "Definieren", "with": 0}, {"label": "Beobachten", "with": 0},
        {"label": "Messen", "with": 0}, {"label": "Ursache finden", "with": 0},
        {"label": "Idee wählen", "with": 1}, {"label": "Prototyp", "with": 2},
        {"label": "Prüfen", "with": 2}, {"label": "Standardisieren", "with": 3}]},
    "p08": {"type": "assembly", "label": "Divyas NVR-Linie: die Vorrichtung zählt jede Schraube",
            "then": {"type": "compare", "before": {"label": "Vorher", "value": 18}, "after": {"label": "Nachher", "value": 1},
                     "unit": "fehlende Schrauben pro 10.000 Einheiten", "note": "etwa 94 % weniger"}},
    "p09": {"type": "flow", "stop": {"after": 2, "label": "KEIN GUTERGEBNIS, KEIN ETIKETT", "with": "example"}, "items": [
        {"label": "Rolle gegen BOM gescannt", "icon": "barcode", "with": 0},
        {"label": "Programmversion geprüft", "icon": "chip", "with": 1},
        {"label": "Gutergebnis pro Seriennummer", "icon": "test", "with": 2},
        {"label": "Etikett wird gedruckt", "icon": "label", "tone": "good", "with": "example"}]},
    "p10": {"type": "versus", "items": [
        {"label": "Gewichtskontrolle", "sub": "Falsches Netzteil, gleiches Gewicht", "icon": "scale", "with": "example"},
        {"label": "Geformte Kit-Schale", "sub": "Falsches Netzteil passt nicht", "icon": "tray", "with": "example"}]},
    "p11": {"type": "stat", "value": 1200, "prefix": "₹", "icon": "pin", "label": "Zwei Zentrierstifte",
            "unit": "Keine verkehrt montierten Rückwände mehr"},
    "p12": {"type": "flow", "items": [
        {"label": "FMEA", "sub": "Die Fehlerart", "icon": "clipboard"},
        {"label": "Kontrollplan", "sub": "Methode und Reaktion", "icon": "shield"},
        {"label": "Standardarbeit", "sub": "Gutsignal, wer zurücksetzt", "icon": "person"},
        {"label": "Audit", "sub": "Ein bekanntes Schlechtteil", "icon": "test", "tone": "good"}]},
    "p13": {"type": "compare", "before": {"label": "Vorher", "value": 0.8}, "after": {"label": "Nachher", "value": 0.2},
            "suffix": "%", "decimals": 1, "unit": "Fehlerquote, 60.000 Einheiten im Monat", "note": "≈ ₹65.000 Einsparung pro Monat"},
    "p14": {"type": "timeline", "items": [
        {"label": "Fehlerarten + Ausgangslage", "sub": "W1–2", "span": 2, "icon": "search"},
        {"label": "Konstruktionsoptionen, Logik festlegen", "sub": "W3–4", "span": 2, "icon": "gear"},
        {"label": "Pilot an einer Station", "sub": "Monat 2", "span": 4, "icon": "test"},
        {"label": "Dokumentieren, schulen, übertragen", "sub": "Monat 3", "span": 4, "icon": "clipboard"}]},
    "p15": {"type": "icons", "items": [
        {"label": "Produktion", "sub": "Verantwortlich für die Station", "icon": "person", "with": "example"},
        {"label": "Technik", "sub": "Konstruiert sie", "icon": "gear", "with": "example"},
        {"label": "Qualität", "sub": "Prüft sie", "icon": "shield", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Eine Vorrichtung gibt erst frei, wenn sie alle sechs Schrauben gezählt hat. Welche Poka "
                    "Yoke Methode ist das?",
        "options": ["Kontaktmethode", "Festwertmethode", "Bewegungsschrittmethode"],
        "correct": 1,
        "explanation": "Sie bestätigt die richtige Anzahl, also ist es die Festwertmethode. Kontakt prüft Form "
                       "oder Position; Bewegungsschritt prüft die Reihenfolge.",
        "q_script": "Kurzer Check. Eine Vorrichtung gibt erst nach allen sechs Schrauben frei. Welche Poka "
                    "Yoke Methode ist das? Nehmen Sie sich kurz Zeit.",
        "a_script": "Es ist die Festwertmethode. Sie bestätigt die richtige Anzahl. Kontakt prüft die Form, "
                    "und Bewegungsschritt prüft die Reihenfolge.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Ein neuer Dichtungssensor weist so viele gute Einheiten ab, dass die Werker anfangen, "
                    "ihn zu überbrücken. Was sollte das Team ZUERST tun?",
        "options": ["Den Sensor entfernen", "Die Werker abmahnen",
                    "Die Überbrückung sperren und die Fehlabweisungen mit geprüften Mustern beheben",
                    "Ein Erinnerungsschild anbringen"],
        "correct": 2,
        "explanation": "Fehlabweisungen verleiten zum Überbrücken. Sperren Sie die Überbrückung, verbessern Sie "
                       "dann Position, Beleuchtung oder Schwellen mit bekannten Gut- und Schlechtmustern, und "
                       "verfolgen Sie die Fehlabweisungsquote.",
        "q_script": "Noch eine, und diesmal ist es ein Szenario. Ein neuer Dichtungssensor weist so viele "
                    "gute Einheiten ab, dass die Werker anfangen, ihn zu überbrücken. Was sollte das Team "
                    "zuerst tun? Überlegen Sie kurz.",
        "a_script": "Sperren Sie die Überbrückung, dann beheben Sie die Fehlabweisungen. Verbessern Sie die "
                    "Sensoreinstellung mit bekannten Gut- und Schlechtmustern. Fehlabweisungen verleiten "
                    "Menschen dazu, eine Vorrichtung zu überbrücken.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
