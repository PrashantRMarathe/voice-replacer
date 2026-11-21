"""yamazumi in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh yamazumi_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "yz_de"
NAME = "yamazumi_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Zero Defects": "Siro Difekts",
    "Yamazumi": "Jamasumi",
    "Heijunka": "Hejdschunka",
    "Gemba": "Gemba",
    "TAKT": "Takt",
    "ECRS": "e ze err ess",
    "SMED": "Smed",
    "ESD": "e ess de",
    "SOP": "ess o pe",
    "A": "a",
    "B": "be",
    "C": "ze",
    "D": "de",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Jeden Nachmittag fällt Meeras Set-Top-Box-Zelle zurück. Drei Werker warten, während "
    "einer in Schrauben versinkt. Niemand ist faul. Die Arbeit ist nur ungleich gestapelt. In "
    "dieser Lektion lernen Sie Yamazumi kennen, ein einfaches Diagramm, das genau zeigt, wo "
    "sich Arbeit stapelt. Und Sie sehen, wie Meera ihre Linie mit echten Daten neu abstimmt."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Messen Sie die echte Arbeit, nicht den Bestfall. Stapeln "
    "Sie sie gegen den TAKT, um zu sehen, wo sie sich häuft. Und stimmen Sie sorgfältig neu "
    "ab, nie auf Kosten von Sicherheit oder Qualität. Ihre Aufgabe für diese Woche: messen "
    "Sie eine Station Ihrer Linie, und zeichnen Sie ihren Balken gegen den TAKT. Gut gemacht, "
    "Lektion abgeschlossen. Als Nächstes lernen Sie Zero Defects kennen, die letzte Lektion "
    "des Kurses."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Yamazumi ist",
        "points": [("Ein gestapeltes Balkendiagramm der Arbeit je Station", "Es ist ein gestapeltes Balkendiagramm"),
                   ("Japanisch: „aufstapeln\"", "Das japanische Wort heißt"),
                   ("Jeder Balken: die Aufgaben eines Werkers", "Jeder Balken stapelt"),
                   ("Über der TAKT Linie = hält nicht mit", "Jeder Balken über")],
        "example": "Meeras Set-Top-Box-Zelle: vier Werker, vier gestapelte Balken, eine TAKT Linie.",
        "example_cue": "Hier ist Meeras Zelle",
        "script": "Was ist also Yamazumi? Es ist ein gestapeltes Balkendiagramm der Arbeit an jeder "
                  "Station. Das japanische Wort heißt aufstapeln. Jeder Balken stapelt die Aufgaben eines "
                  "Werkers, in Sekunden. Eine waagrechte Linie markiert die TAKT Zeit, das Tempo, das Ihr "
                  "Kunde braucht. Jeder Balken über dieser Linie hält nicht mit. Es macht aus Ihren "
                  "Zeitstudien ein Gespräch über Abstimmung. Hier ist Meeras Zelle, mit vier Werkern. Sehen "
                  "Sie das Problem schon?",
    },
    {
        "key": "p02", "num": 2, "title": "Zweck und Nutzen",
        "points": [("Ungleichgewicht, Warten, Überlast auf einen Blick", "Sie sehen Ungleichgewicht"),
                   ("Objektive Grundlage für die Besetzung", "Es gibt Ihnen eine objektive"),
                   ("Zeigt, wo Mehrfachqualifizierung hilft", "Es zeigt auch, wo"),
                   ("Ersetzt nie technische Prüfungen", "Aber Yamazumi ersetzt nie")],
        "example": "Ein Werker wartet, während ein anderer mit langem Verschrauben kämpft. Eine kleine "
                   "Aufgabe zu verlegen könnte den Fluss glätten.",
        "example_cue": "In Meeras Zelle",
        "script": "Warum der Aufwand? Weil das Diagramm Probleme sichtbar macht. Sie sehen Ungleichgewicht, "
                  "Warten und Überlast auf einen Blick. Es gibt Ihnen eine objektive Grundlage für die "
                  "Besetzung, statt Bauchgefühl. Es zeigt auch, wo Mehrfachqualifizierung hilft. In Meeras "
                  "Zelle wartet ein Werker, während ein anderer mit langem Verschrauben kämpft. Eine kleine "
                  "Aufgabe zu verlegen könnte den Fluss glätten. Aber Yamazumi ersetzt nie technische "
                  "Prüfungen. Zuerst brauchen Sie drei Kernzeiten.",
    },
    {
        "key": "p03", "num": 3, "title": "TAKT, Zykluszeit und Arbeitsinhalt",
        "points": [("TAKT: Nettozeit ÷ benötigte gute Einheiten", "Es ist Ihre netto verfügbare Zeit"),
                   ("Zykluszeit: wie oft eine Einheit geht", "Die Zykluszeit ist"),
                   ("Arbeitsinhalt: Summe der Handarbeit", "Der Arbeitsinhalt ist"),
                   ("Maschinenzeit getrennt halten", "Halten Sie Maschinenzeit getrennt")],
        "example": "420 Netto-Minuten ÷ 840 Einheiten = TAKT von 30 Sekunden. Station B braucht 35.",
        "example_cue": "Meera hat vierhundertzwanzig",
        "script": "Zuerst die TAKT Zeit. Es ist Ihre netto verfügbare Zeit, geteilt durch die guten "
                  "Einheiten, die der Kunde braucht. Die Zykluszeit ist, wie oft eine Einheit wirklich eine "
                  "Station verlässt. Der Arbeitsinhalt ist die Summe der Handarbeit an einer Einheit. "
                  "Halten Sie Maschinenzeit getrennt. Meera hat vierhundertzwanzig Netto-Minuten. Der "
                  "Bedarf ist achthundertvierzig Einheiten. Das ist ein TAKT von dreißig Sekunden. Ihre "
                  "Station B braucht fünfunddreißig. Hält sie allein mit?",
    },
    {
        "key": "p04", "num": 4, "title": "Aufbau des Diagramms",
        "points": [("Ein Balken je Werker oder Station", "Sie zeichnen einen senkrechten Balken"),
                   ("Sekunden an der Seite, TAKT Linie quer", "Die senkrechte Achse"),
                   ("Jeder Block = eine Aufgabe, in Folge", "Jeder farbige Block"),
                   ("Farben zeigen Aufgabenarten, keine Noten", "Farben zeigen Aufgabenarten")],
        "example": "Station A stapelt sich auf 22 Sekunden; Station B erreicht 35, deutlich über der Linie.",
        "example_cue": "In Meeras Diagramm",
        "script": "Bauen wir nun das Diagramm. Sie zeichnen einen senkrechten Balken je Werker oder "
                  "Station. Die senkrechte Achse zeigt Sekunden. Eine waagrechte Linie markiert den TAKT. "
                  "Jeder farbige Block ist eine Aufgabe, gestapelt in der Folge der Standardarbeit. Farben "
                  "zeigen Aufgabenarten, nie Leistungsnoten. Beschriften Sie jeden Balken mit Stichprobe "
                  "und Schicht. In Meeras Diagramm stapelt sich Station A auf zweiundzwanzig Sekunden. "
                  "Station B erreicht fünfunddreißig, deutlich über der Linie. Woher kommen diese Zahlen?",
    },
    {
        "key": "p05", "num": 5, "title": "Verlässliche Zeitstudie",
        "points": [("Start und Ende jeder Aufgabe festlegen", "Legen Sie fest, wo jede Aufgabe"),
                   ("Viele Zyklen, über Schichten", "Beobachten Sie viele Zyklen"),
                   ("Wege, Kurzstopps, Umrüstungen erfassen", "Erfassen Sie auch Wege"),
                   ("Maschinenzeit von Handzeit trennen", "Trennen Sie Maschinenzeit")],
        "example": "Das Aufspielen der Firmware läuft, während der Werker schraubt, also misst Meera jedes "
                   "Element getrennt.",
        "example_cue": "In Meeras Zelle läuft",
        "script": "Sie kommen aus echter Beobachtung am Gemba. Ihr Diagramm ist nur so gut wie seine Daten. "
                  "Legen Sie fest, wo jede Aufgabe beginnt und endet. Beobachten Sie viele Zyklen, über "
                  "Schichten, nicht nur den schnellsten. Erfassen Sie auch Wege, Kurzstopps und "
                  "Umrüstungen. Trennen Sie Maschinenzeit von der Handarbeit. In Meeras Zelle läuft das "
                  "Aufspielen der Firmware, während der Werker schraubt. Also misst sie jedes Element "
                  "getrennt. Welche Arten von Arbeit finden Sie?",
    },
    {
        "key": "p06", "num": 6, "title": "Die Arbeit einordnen",
        "points": [("Wertschöpfend: was der Kunde will", "Wertschöpfende Arbeit verändert"),
                   ("Nötig, aber ohne Wert: Prüfungen, Rückverfolgbarkeit", "Nötige Arbeit ohne Wertschöpfung"),
                   ("Verschwendung: Suchen, Gehen, Warten", "Verschwendung ist Suchen"),
                   ("ECRS, aber Qualitäts- und Sicherheitsprüfungen behalten", "Hinterfragen Sie jeden Schritt")],
        "example": "Meeras Werker geht 5 Sekunden, um Schrauben zu holen. Behälter am Verwendungsort "
                   "beseitigen diese Verschwendung.",
        "example_cue": "Meeras Werker geht",
        "script": "Sie finden drei Arten von Arbeit. Wertschöpfende Arbeit verändert das Produkt so, wie "
                  "der Kunde es will. Nötige Arbeit ohne Wertschöpfung umfasst Pflichtprüfungen und "
                  "Rückverfolgbarkeit. Verschwendung ist Suchen, Gehen und Warten. Hinterfragen Sie jeden "
                  "Schritt mit ECRS: eliminieren, kombinieren, umordnen, vereinfachen. Aber entfernen Sie "
                  "nie eine vorgeschriebene Qualitäts- oder Sicherheitsprüfung. Meeras Werker geht fünf "
                  "Sekunden, um Schrauben zu holen. Behälter am Verwendungsort beseitigen diese "
                  "Verschwendung. Nun können Sie den Ist-Zustand abbilden.",
    },
    {
        "key": "p07", "num": 7, "title": "Den Ist-Zustand aufbauen",
        "points": [("Freigegebener Bedarf → TAKT", "Beginnen Sie mit freigegebenem Bedarf"),
                   ("Ein Balken je Station, TAKT Linie gezogen", "Bauen Sie einen Balken je Station"),
                   ("Das Diagramm mit der Wirklichkeit prüfen", "Dann gehen Sie durch die Halle"),
                   ("Ein kurzer Balken ≠ freie Kapazität", "ein kurzer Balken beweist nicht")],
        "example": "TAKT 30 s: A = 22, B = 35, C = 27, D = 20. B liegt 5 Sekunden darüber, die erste "
                   "Priorität.",
        "example_cue": "Hier ist Meeras Ist-Zustand",
        "script": "Beginnen Sie mit freigegebenem Bedarf, und berechnen Sie den TAKT. Bauen Sie einen "
                  "Balken je Station, stapeln Sie jede Aufgabe, und ziehen Sie die TAKT Linie. Dann gehen "
                  "Sie durch die Halle und prüfen das Diagramm mit der Wirklichkeit. Hier ist Meeras "
                  "Ist-Zustand. Station A braucht zweiundzwanzig Sekunden, B fünfunddreißig. C braucht "
                  "siebenundzwanzig, D zwanzig. Station B liegt fünf Sekunden über dem TAKT. Das ist ihre "
                  "erste Priorität. Und ein kurzer Balken beweist nicht, dass Sie freie Kapazität haben.",
    },
    {
        "key": "p08", "num": 8, "title": "Linienabstimmung",
        "points": [("Aufgaben verlegen oder Methoden verbessern", "Abstimmen heißt"),
                   ("Keine exakt gleichen Balken", "Das Ziel sind keine"),
                   ("Layout, Folge, Können, Prüfungen achten", "Sie müssen Layout"),
                   ("ECRS vor zusätzlichen Leuten", "Versuchen Sie ECRS")],
        "example": "Eine Etikettieraufgabe von 5 Sekunden wandert von B zu D: B = 30, D = 25. Dann "
                   "pilotieren und neu messen.",
        "example_cue": "Meera findet eine Etikettieraufgabe",
        "script": "Abstimmen heißt, machbare Aufgaben zu verlegen oder Methoden zu verbessern, damit jede "
                  "Station das Tempo hält. Das Ziel sind keine exakt gleichen Balken. Sie müssen Layout, "
                  "Aufgabenfolge, Vorrichtungen, Können und Qualitätsprüfungen achten. Versuchen Sie ECRS, "
                  "bevor Sie Leute ergänzen. Meera findet eine Etikettieraufgabe von fünf Sekunden, die "
                  "nicht von der übrigen Arbeit an B abhängt. Sie verlegt sie zu Station D. B sinkt auf "
                  "dreißig, D steigt auf fünfundzwanzig. Dann pilotiert sie und misst neu.",
    },
    {
        "key": "p09", "num": 9, "title": "Personal und Effizienz",
        "points": [("Handarbeit ÷ TAKT, aufrunden", "Addieren Sie die Handarbeit"),
                   ("Abstimmungseffizienz: Arbeit gegen Kapazität", "Die Abstimmungseffizienz vergleicht"),
                   ("Eine Planungsuntergrenze, kein Versprechen", "Nehmen Sie das als Planungsuntergrenze"),
                   ("Leistung beweisen, bevor Personal sinkt", "Reduzieren Sie nie Werker")],
        "example": "104 Sekunden Arbeit bei einem TAKT von 30 Sekunden = 4 Werker; Effizienz etwa 87 %.",
        "example_cue": "Meeras Zelle hat hundertvier",
        "script": "Wie viele Leute brauchen Sie wirklich? Addieren Sie die Handarbeit, teilen Sie durch den "
                  "TAKT, und runden Sie auf. Meeras Zelle hat hundertvier Sekunden Arbeit. Bei einem TAKT "
                  "von dreißig Sekunden sind das vier Werker. Die Abstimmungseffizienz vergleicht die "
                  "zugeteilte Arbeit mit der besetzten Kapazität. Ihre liegt bei etwa siebenundachtzig "
                  "Prozent. Nehmen Sie das als Planungsuntergrenze, nicht als Versprechen. Reduzieren Sie "
                  "nie Werker, bevor gute Leistung sicher und stetig bewiesen ist.",
    },
    {
        "key": "p10", "num": 10, "title": "Engpässe und Maschinen",
        "points": [("Nicht jeder lange Balken ist ein Werker-Engpass", "Nicht jeder lange Balken"),
                   ("Gemeinsame Maschinen brauchen eine eigene Prüfung", "Maschinen können laufen"),
                   ("Hand, Automatik, Laden, Warten trennen", "Trennen Sie Handzeit"),
                   ("Verfügbarkeit, Umrüstung, Ausbeute einrechnen", "Dann rechnen Sie Verfügbarkeit")],
        "example": "Zwei Audiotester: 160 Einheiten/Stunde auf dem Papier, in Wahrheit etwa 140 gute.",
        "example_cue": "Schauen Sie auf die zwei Tester",
        "script": "Ein häufiger Fehler. Nicht jeder lange Balken ist ein Werker-Engpass. Maschinen können "
                  "laufen, während Menschen arbeiten, also brauchen gemeinsame Anlagen eine eigene "
                  "Kapazitätsprüfung. Trennen Sie Handzeit, Automatikzyklus, Laden und Warten. Dann rechnen "
                  "Sie Verfügbarkeit, Umrüstungen und Erstdurchlaufquote ein. Schauen Sie auf die zwei "
                  "Tester der Audiolinie. Auf dem Papier schaffen sie hundertsechzig Einheiten pro Stunde. "
                  "In Wahrheit sind es etwa hundertvierzig gute. Hätten Sie damit geplant?",
    },
    {
        "key": "p11", "num": 11, "title": "Linien mit gemischten Modellen",
        "points": [("Ein Diagramm kann Ärger verbergen", "Dann kann ein Diagramm"),
                   ("Balken je Modell, schlimmster Fall", "Nutzen Sie also Balken je Modell"),
                   ("Flexibles, qualifiziertes Personal", "Planen Sie flexibles, qualifiziertes"),
                   ("Heijunka und SMED glätten den Mix", "Und nutzen Sie Heijunka")],
        "example": "Im Mix 27 s im Schnitt, beim Audiomodell aber 42 s: eine lange Charge stapelt Arbeit "
                   "schnell.",
        "example_cue": "Eine Station kann",
        "script": "Was, wenn Ihre Linie mehrere Modelle baut? Dann kann ein Diagramm Ärger verbergen. Eine "
                  "Station kann im Mix siebenundzwanzig Sekunden im Schnitt brauchen. Aber beim Audiomodell "
                  "braucht sie zweiundvierzig. Fahren Sie davon eine lange Charge, und die Arbeit stapelt "
                  "sich schnell. Nutzen Sie also Balken je Modell, und prüfen Sie den schlimmsten Fall. "
                  "Planen Sie flexibles, qualifiziertes Personal. Und nutzen Sie Heijunka und SMED, um den "
                  "Mix zu glätten. Woran erkennen Sie, dass eine neue Abstimmung wirkt?",
    },
    {
        "key": "p12", "num": 12, "title": "KPI und Bestätigung",
        "points": [("Ein abgestimmtes Diagramm ist eine Hypothese", "Ein abgestimmtes Diagramm ist nur"),
                   ("Früh: Einhaltung der Standardarbeit", "Beobachten Sie Frühindikatoren"),
                   ("Spät: gute Leistung, Fehler, UPPH", "Beobachten Sie Spätindikatoren"),
                   ("Ergonomie mit den Werkern prüfen", "prüfen Sie die Ergonomie")],
        "example": "Planerfüllung zählt gute Einheiten gegen den Plan; die Erstdurchlaufquote zählt "
                   "Einheiten, die beim ersten Mal bestehen.",
        "example_cue": "Die Planerfüllung zählt",
        "script": "Ein abgestimmtes Diagramm ist nur eine Hypothese. Sie beweisen sie mit Ergebnissen. "
                  "Beobachten Sie Frühindikatoren, wie die Einhaltung der Standardarbeit. Beobachten Sie "
                  "Spätindikatoren, wie gute Leistung, Fehler und Einheiten pro Personenstunde. Halten Sie "
                  "die Definitionen einheitlich. Zwei Kennzahlen sehen ähnlich aus, bedeuten aber "
                  "Verschiedenes. Die Planerfüllung zählt gute Einheiten gegen den Plan. Die "
                  "Erstdurchlaufquote zählt Einheiten, die beim ersten Mal bestehen. Und nach jeder "
                  "Änderung prüfen Sie die Ergonomie mit den Werkern.",
    },
    {
        "key": "p13", "num": 13, "title": "Fall: Set-Top-Box-Zelle",
        "points": [("Vorher: B begrenzte die Leistung auf etwa 103/Stunde", "Vorher begrenzte Station B"),
                   ("Nachher: B auf 30 Sekunden", "Nach dem Pilot"),
                   ("Etwa 116 gute/Stunde gegen 120 theoretisch", "Die Leistung stieg"),
                   ("Erst nach zwei stabilen Wochen fertig", "Sie nannte es erst nach")],
        "example": "Unter 120 ist normal: Verfügbarkeit und Ausbeute kosten immer etwas.",
        "example_cue": "Und das ist normal",
        "script": "Sehen wir, wie Meeras Änderung ausging. Vorher begrenzte Station B die Zelle auf etwa "
                  "hundertdrei Einheiten pro Stunde. Nach dem Pilot sank Station B auf dreißig Sekunden. "
                  "Die Leistung stieg auf etwa hundertsechzehn gute Einheiten pro Stunde. Das liegt unter "
                  "den theoretischen hundertzwanzig. Und das ist normal, denn Verfügbarkeit und Ausbeute "
                  "kosten immer etwas. Sie nannte es erst nach zwei stabilen Wochen fertig. Was würden Sie "
                  "als Nächstes prüfen?",
    },
    {
        "key": "p14", "num": 14, "title": "Was tun, was lassen",
        "points": [("Echte Arbeit messen, Daten aktuell halten", "Messen Sie echte Arbeit"),
                   ("Werker, Qualität, Technik einbeziehen", "Beziehen Sie Werker"),
                   ("Sicherheit, ESD, Tests, Rückverfolgbarkeit schützen", "Schützen Sie Sicherheit, ESD"),
                   ("Keine Bestfallzeiten, kein Personalabbau", "Nutzen Sie keine")],
        "example": "Eine Barcode-Prüfung zu streichen sieht nach 6 gesparten Sekunden aus. Das ist keine "
                   "Abstimmung, sondern ein Rückverfolgbarkeitsrisiko.",
        "example_cue": "Eine Barcode-Prüfung zu streichen",
        "script": "Ein paar harte Regeln. Messen Sie echte Arbeit, und halten Sie Daten aktuell. Beziehen "
                  "Sie Werker, Qualität und Technik ein. Schützen Sie Sicherheit, ESD, Tests und "
                  "Rückverfolgbarkeit. Nutzen Sie keine Bestfall-Zykluszeiten. Und machen Sie Yamazumi nie "
                  "zum Werkzeug für Personalabbau. Eine Falle. Eine Barcode-Prüfung zu streichen spart "
                  "scheinbar sechs Sekunden. Das ist keine Abstimmung, sondern ein "
                  "Rückverfolgbarkeitsrisiko.",
    },
    {
        "key": "p15", "num": 15, "title": "Fahrplan für 90 Tage",
        "points": [("Tag 1–30: Pilotlinie, Zeitstudien, Ausgangswert", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: ECRS, neu abstimmen, qualifizieren", "In den nächsten dreißig"),
                   ("Tag 61–90: bestätigen, SOP aktualisieren, ausweiten", "In den letzten dreißig"),
                   ("Diagramme aktuell halten", "Dann halten Sie Ihre Diagramme aktuell")],
        "example": "Ein veraltetes Diagramm ist schlimmer als gar keins.",
        "example_cue": "Ein veraltetes Diagramm",
        "script": "Bereit? Hier ein Plan für neunzig Tage. In den ersten dreißig Tagen wählen Sie eine "
                  "Pilotlinie, sammeln Bedarf und Zeitstudien, und bauen Ausgangsdiagramme. In den nächsten "
                  "dreißig führen Sie ECRS-Workshops, stimmen neu ab und qualifizieren Werker. In den "
                  "letzten dreißig bestätigen Sie Ausbeute und Leistung, aktualisieren die SOP, und weiten "
                  "auf ähnliche Linien aus. Dann halten Sie Ihre Diagramme aktuell, wann immer sich Bedarf, "
                  "Mix oder Besetzung ändern. Ein veraltetes Diagramm ist schlimmer als gar keins.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson). Station bars use the
# current state from p07 (TAKT 30 s).
CURRENT = [("A", 22, None), ("B", 35, "bad"), ("C", 27, None), ("D", 20, None)]


def takt_bars(stations, note, unit, with_="example"):
    return {"type": "bars", "label": "TAKT", "value": 30, "suffix": " s", "note": note, "unit": unit,
            "with": with_, "items": [{"label": f"Station {s}", "value": v, "tone": t, "with": with_}
                                     for s, v, t in stations]}


VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Gestapelte Balken", "icon": "stack", "with": 0},
        {"label": "„Aufstapeln\"", "icon": "box", "with": 1},
        {"label": "Die Aufgaben eines Werkers", "icon": "person", "with": 2},
        {"label": "Über dem TAKT: hält nicht mit", "icon": "warning", "tone": "bad", "with": 3}],
        "then": takt_bars(CURRENT, "B hält nicht mit", "Meeras Zelle: Sekunden Arbeit je Station")},
    "p02": {"type": "icons", "items": [
        {"label": "Ungleichgewicht auf einen Blick", "icon": "search", "with": 0},
        {"label": "Besetzung auf Faktenbasis", "icon": "person", "with": 1},
        {"label": "Wo Mehrfachqualifizierung hilft", "icon": "sequence", "with": 2},
        {"label": "Technische Prüfungen bleiben nötig", "icon": "wrench", "tone": "bad", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Langes Verschrauben", "sub": "Überlast", "icon": "screw", "with": "example"},
            {"label": "Eine kleine Aufgabe verlegen", "sub": "Glatter Fluss", "icon": "sequence", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Nettozeit ÷ gute Einheiten", "icon": "clock", "with": 0},
        {"label": "Zykluszeit", "sub": "Wie oft eine Einheit geht", "icon": "sequence", "with": 1},
        {"label": "Arbeitsinhalt", "sub": "Summe der Handarbeit", "icon": "hand", "with": 2},
        {"label": "Maschinenzeit", "sub": "Getrennt", "icon": "gear", "with": 3}],
        "then": {"type": "stat", "value": 30, "suffix": " s", "icon": "clock", "label": "TAKT Zeit",
                 "unit": "420 Netto-Minuten ÷ 840 Einheiten", "with": "example"}},
    "p04": takt_bars([("A", 22, None), ("B", 35, "bad")], "B liegt über der Linie",
                     "Ein Balken je Station, TAKT Linie waagrecht", with_=0),
    "p05": {"type": "flow", "items": [
        {"label": "Start und Ende festlegen", "icon": "pin", "with": 0},
        {"label": "Viele Zyklen, jede Schicht", "icon": "clock", "with": 1},
        {"label": "Wege, Stopps, Umrüstungen", "icon": "walk", "with": 2},
        {"label": "Maschine, getrennt von Hand", "icon": "gear", "tone": "good", "with": 3}]},
    "p06": {"type": "icons", "items": [
        {"label": "Wertschöpfend", "icon": "check", "tone": "good", "with": 0},
        {"label": "Nötig: Prüfungen, Rückverfolgbarkeit", "icon": "shield", "with": 1},
        {"label": "Verschwendung: Suchen, Gehen, Warten", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "ECRS, Prüfungen behalten", "icon": "wrench", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "5 s Weg für Schrauben", "sub": "Verschwendung", "icon": "walk", "with": "example"},
            {"label": "Behälter am Verwendungsort", "sub": "Weg beseitigt", "icon": "tray", "with": "example"}]}},
    "p07": takt_bars(CURRENT, "B liegt 5 s darüber: erste Priorität", "Meeras Ist-Zustand"),
    "p08": {"type": "icons", "items": [
        {"label": "Arbeit verlegen, Methode verbessern", "icon": "sequence", "with": 0},
        {"label": "Nicht exakt gleich", "icon": "scale", "with": 1},
        {"label": "Layout, Folge, Können, Prüfungen", "icon": "clipboard", "with": 2},
        {"label": "ECRS vor zusätzlichen Leuten", "icon": "person", "with": 3}],
        "then": takt_bars([("A", 22, None), ("B", 30, "good"), ("C", 27, None), ("D", 25, None)],
                          "Etikettieren 5 s von B → D", "Nach der Änderung: pilotieren, neu messen")},
    "p09": {"type": "stat", "value": 4, "suffix": " Werker", "icon": "person", "label": "104 s Arbeit ÷ TAKT 30 s, aufgerundet",
            "unit": "Abstimmungseffizienz etwa 87 %", "with": "example"},
    "p10": {"type": "icons", "items": [
        {"label": "Langer Balken ≠ Werkerproblem", "icon": "person", "with": 0},
        {"label": "Gemeinsame Maschinen", "icon": "gear", "with": 1},
        {"label": "Hand · Automatik · Laden · Warten", "icon": "clock", "with": 2},
        {"label": "Verfügbarkeit, Umrüstung, Ausbeute", "icon": "chartDown", "with": 3}],
        "then": {"type": "compare", "before": {"label": "Auf dem Papier", "value": 160}, "after": {"label": "Echt, gut", "value": 140},
                 "unit": "Einheiten pro Stunde, zwei Audiotester", "note": "Mit der echten Zahl planen", "with": "example"}},
    "p11": {"type": "bars", "label": "TAKT", "value": 30, "suffix": " s", "note": "Der Durchschnitt verbirgt es",
            "unit": "Eine Station, Sekunden pro Einheit", "with": "example", "items": [
        {"label": "Durchschnitt im Mix", "value": 27, "with": "example"},
        {"label": "Audiomodell", "value": 42, "tone": "bad", "with": "example"}]},
    "p12": {"type": "icons", "items": [
        {"label": "Eine Hypothese zum Beweisen", "icon": "test", "with": 0},
        {"label": "Früh: Standardarbeit", "icon": "clipboard", "with": 1},
        {"label": "Spät: Leistung, Fehler, UPPH", "icon": "chartUp", "with": 2},
        {"label": "Ergonomie mit den Werkern", "icon": "person", "with": 3}]},
    "p13": {"type": "compare", "before": {"label": "Vorher", "value": 103}, "after": {"label": "Nachher", "value": 116},
            "unit": "gute Einheiten pro Stunde (Theorie: 120)", "note": "Fertig nach zwei stabilen Wochen", "with": 2},
    "p14": {"type": "icons", "items": [
        {"label": "Echte Arbeit, aktuelle Daten", "icon": "clock", "tone": "good", "with": 0},
        {"label": "Werker, Qualität, Technik", "icon": "person", "tone": "good", "with": 1},
        {"label": "Sicherheit, ESD, Tests, Rückverfolgbarkeit", "icon": "shield", "tone": "good", "with": 2},
        {"label": "Bestfall, Personalabbau", "icon": "cross", "tone": "bad", "with": 3}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Pilotlinie, Zeitstudien, Ausgangswert", "sub": "Tag 1–30", "icon": "clock", "with": 0},
        {"label": "ECRS, neu abstimmen, qualifizieren", "sub": "31–60", "icon": "sequence", "with": 1},
        {"label": "Bestätigen, SOP aktualisieren, ausweiten", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Station 4 läuft mit 33 s bei einem TAKT von 30 Sekunden; Station 1 mit 22 s. Was "
                    "versuchen Sie zuerst?",
        "options": ["Den Werker an Station 4 bitten, schneller zu arbeiten",
                    "Eine machbare Aufgabe von Station 4 zu Station 1 verlegen oder ihre Methode verbessern, "
                    "dann pilotieren und neu messen",
                    "Eine Qualitätsprüfung an Station 4 streichen",
                    "Den TAKT auf 33 Sekunden setzen"],
        "correct": 1,
        "explanation": "Abstimmen heißt, machbare Arbeit zu verlegen oder die Methode zu verbessern. Leute "
                       "antreiben, Prüfungen streichen oder den TAKT umdefinieren verdeckt das Problem, statt es "
                       "zu lösen.",
        "q_script": "Kurzer Check, ein Szenario. Station vier läuft mit dreiunddreißig Sekunden, bei einem "
                    "TAKT von dreißig Sekunden. Station eins läuft mit zweiundzwanzig. Was versuchen Sie "
                    "zuerst? Nehmen Sie sich kurz Zeit.",
        "a_script": "Suchen Sie eine machbare Aufgabe, die von Station vier zu Station eins wandern kann, "
                    "oder verbessern Sie ihre Methode. Dann pilotieren und neu messen. Leute antreiben oder "
                    "Prüfungen streichen ist keine Abstimmung.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "420 Netto-Minuten decken einen Bedarf von 840 guten Einheiten. Wie lang ist die TAKT "
                    "Zeit?",
        "options": ["20 Sekunden pro Einheit",
                    "30 Sekunden pro Einheit",
                    "2 Sekunden pro Einheit",
                    "60 Sekunden pro Einheit"],
        "correct": 1,
        "explanation": "TAKT = Nettozeit ÷ Bedarf = 420 × 60 ÷ 840 = 30 Sekunden pro Einheit.",
        "q_script": "Noch eine. Ihre Linie hat vierhundertzwanzig Netto-Minuten. Der Bedarf ist "
                    "achthundertvierzig gute Einheiten. Wie lang ist Ihre TAKT Zeit? Überlegen Sie kurz.",
        "a_script": "Dreißig Sekunden pro Einheit. Rechnen Sie Minuten in Sekunden um, dann teilen Sie durch "
                    "den Bedarf.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
