"""elimination_of_waste in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh elimination_of_waste_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ew_de"
NAME = "elimination_of_waste_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Elimination of Waste": "Elimineeschen of Weest",
    "TIMWOODS": "Tim Wuds",
    "Pareto": "Pareto",
    "Gemba": "Gemba",
    "Muda": "Muda",
    "ECRS": "e ze err ess",
    "FMEA": "eff emm e a",
    "SOP": "ess o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Jeden Monat gingen fünfzehnhundert Soundbars in die Nacharbeit. Jede Reparatur kostete "
    "zweiundvierzig Rupien. Niemand hatte es je zusammengerechnet. Kommt Ihnen das bekannt "
    "vor? In dieser Lektion lernen Sie Elimination of Waste kennen. Sie sehen, wie man Arbeit "
    "erkennt, die Ihr Kunde nicht bezahlen würde, ihre Ursache beseitigt und den Gewinn "
    "beweist. Wir begleiten Deepak, Produktionsleiter an einer Soundbar-Linie."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Verschwendung ist alles, was Ihr Kunde nicht bezahlen "
    "würde, aber nie Ihre Sicherheits- oder Qualitätsprüfungen. Finden Sie sie mit Fakten am "
    "Gemba, nicht mit Meinungen. Und beseitigen Sie die Ursache, dann beweisen und halten Sie "
    "den Gewinn. Ihre Aufgabe für diese Woche. Gehen Sie dreißig Minuten Ihre Linie ab, und "
    "notieren Sie drei Verschwendungen als Fakten. Gut gemacht, Lektion abgeschlossen. Als "
    "Nächstes lernen Sie die FMEA kennen, die Fehlermöglichkeits- und Einflussanalyse."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Verschwendung wirklich ist",
        "points": [("Verbraucht Ressourcen, schafft keinen Kundenwert", "Verschwendung ist jede Tätigkeit"),
                   ("Keine einmalige Kostensenkung", "Sie zu beseitigen ist keine"),
                   ("Ursache beseitigen, Rückkehr verhindern", "beseitigen ihre Grundursache")],
        "example": "Deepaks Linie: 1.500 Soundbars werden jeden Monat nachgearbeitet.",
        "example_cue": "An Deepaks Linie",
        "script": "Beginnen wir mit einer Definition. Verschwendung ist jede Tätigkeit, die Zeit, Platz, "
                  "Material oder Mühe kostet, aber keinen Wert für Ihren Kunden schafft. Sie zu beseitigen "
                  "ist keine einmalige Sparaktion. Sie finden die Verschwendung, beseitigen ihre "
                  "Grundursache und verhindern, dass sie zurückkommt. An Deepaks Linie wurden jeden Monat "
                  "fünfzehnhundert Soundbars nachgearbeitet. Wie entscheiden Sie also, was Wert ist und was "
                  "Verschwendung?",
    },
    {
        "key": "p02", "num": 2, "title": "Der Wertetest",
        "points": [("Er verändert das Produkt", "Sie verändert das Produkt"),
                   ("Der Kunde würde dafür zahlen", "Der Kunde würde"),
                   ("Gleich beim ersten Mal richtig", "Sie wird richtig gemacht"),
                   ("Sonst: notwendig, oder reine Verschwendung", "Alles andere")],
        "example": "Den Lautsprecher einbauen: Wert. Ihn nach einem Klappern neu einbauen: reine "
                   "Verschwendung.",
        "example_cue": "Den Lautsprecher einbauen",
        "script": "Nutzen Sie einen einfachen Wertetest. Eine Tätigkeit schafft nur Wert, wenn drei Dinge "
                  "stimmen. Sie verändert das Produkt. Der Kunde würde für diese Veränderung zahlen. Und "
                  "sie wird richtig gemacht, beim ersten Mal. Alles andere ist entweder notwendig, wie eine "
                  "gesetzliche Prüfung, oder reine Verschwendung. Den Lautsprecher einbauen ist Wert. Ihn "
                  "nach einem Klappern neu einbauen ist reine Verschwendung. Wie viel Ihres Tages besteht "
                  "diesen Test?",
    },
    {
        "key": "p03", "num": 3, "title": "Warum es wichtig ist",
        "points": [("Schnellerer Fluss, kürzere Durchlaufzeit", "Die Arbeit fließt schneller"),
                   ("Weniger Fehler und Nacharbeit", "Weniger Fehler"),
                   ("Kapazität frei, ohne neue Ausgaben", "Sie setzen Menschen"),
                   ("Ideen von denen, die die Arbeit machen", "Ihre Leute können")],
        "example": "Deepaks Ziel: Kapazität für ein neues Modell freimachen, ohne zusätzliche Schicht.",
        "example_cue": "Deepak brauchte",
        "script": "Warum der Aufwand? Weil Verschwendung Ihre Kapazität versteckt. Beseitigen Sie sie, und "
                  "die Arbeit fließt schneller, die Durchlaufzeit sinkt. Weniger Fehler bedeutet weniger "
                  "Nacharbeit und weniger Rücksendungen. Sie setzen Menschen, Maschinen, Platz und Geld "
                  "frei, ohne neue Investitionen. Und Ihre Leute können ihre Ideen einbringen. Deepak "
                  "brauchte Platz für ein neues Soundbar-Modell, ohne zusätzliche Schicht. Woher käme Ihre "
                  "freie Kapazität?",
    },
    {
        "key": "p04", "num": 4, "title": "Drei Leitplanken",
        "points": [("Sicherheits- und Qualitätsprüfungen sind keine Verschwendung", "Nennen Sie nie eine"),
                   ("Verschwendung nicht auf andere abwälzen", "Wälzen Sie Verschwendung nicht"),
                   ("Menschen sind nie die Verschwendung", "Menschen sind nie")],
        "example": "Der Audio-Endtest bleibt. Er schützt den Kunden.",
        "example_cue": "An Deepaks Linie",
        "script": "Bevor Sie kürzen, drei Leitplanken. Nennen Sie nie eine Sicherheits- oder "
                  "Qualitätsprüfung Verschwendung, außer eine Risikobewertung genehmigt es. Wälzen Sie "
                  "Verschwendung nicht auf eine andere Schicht, einen Lieferanten oder Ihren Kunden ab. "
                  "Verschieben ist nicht beseitigen. Und Menschen sind nie die Verschwendung. Ungenutzte "
                  "Fähigkeiten schon. An Deepaks Linie bleibt der Audio-Endtest. Er schützt jeden Kunden. "
                  "Nach welchen Verschwendungen suchen Sie also?",
    },
    {
        "key": "p05", "num": 5, "title": "Die acht Verschwendungsarten",
        "points": [("Transport, Bestände, Bewegung, Warten", "Transport, Bestände"),
                   ("Überproduktion, Überbearbeitung", "Überproduktion"),
                   ("Fehler, ungenutzte Fähigkeiten", "Fehler und ungenutzte Fähigkeiten")],
        "example": "Merken Sie sie sich als TIMWOODS.",
        "example_cue": "Merken Sie sie sich als TIMWOODS",
        "script": "Lean teilt Verschwendung in acht Arten ein. Sie sehen sie in der Muda-Lektion wieder. "
                  "Transport, Bestände, Bewegung und Warten. Dann Überproduktion und Überbearbeitung, also "
                  "mehr tun, als der Kunde braucht. Schließlich Fehler und ungenutzte Fähigkeiten. Merken "
                  "Sie sie sich als TIMWOODS. Jede steckt irgendwo an jeder Linie, auch an Ihrer. Die Kunst "
                  "ist nicht, sie zu benennen. Sondern sie an Ihrer eigenen Linie zu sehen. Wie suchen Sie "
                  "also?",
    },
    {
        "key": "p06", "num": 6, "title": "Der Verschwendungsrundgang",
        "points": [("Gehen Sie bei normaler Arbeit an den Gemba", "Gehen Sie an den Gemba"),
                   ("Fakten notieren, nie Schuld zuweisen", "Notieren Sie Fakten"),
                   ("Wo, was, wie lange, wie oft", "Notieren Sie, wo es passierte")],
        "example": "Fakt: „Vier Werker warteten 12 Minuten auf fehlende Gitter.“ Meinung: „Das Lager ist "
                   "immer zu spät.“",
        "example_cue": "Vergleichen Sie diese zwei",
        "script": "Machen Sie einen Verschwendungsrundgang. Gehen Sie an den Gemba, während der normalen "
                  "Produktion, nicht bei einem Besuch. Notieren Sie Fakten, und geben Sie nie einer Person "
                  "die Schuld. Notieren Sie, wo es passierte, welches Produkt, wie lange und wie oft. "
                  "Beobachten Sie Menschen, Teile und Papiere. Vergleichen Sie diese zwei. Vier Werker "
                  "warteten zwölf Minuten auf fehlende Gitter. Oder, das Lager ist immer zu spät. Nur das "
                  "Erste sagt Ihnen, wo Sie suchen müssen und wie groß es ist. Was können Sie wirklich "
                  "beheben?",
    },
    {
        "key": "p07", "num": 7, "title": "Was Deepak fand",
        "points": [("Warten auf verspätete Kits", "Werker warteten"),
                   ("Greifen und Laufen nach Werkzeug", "griffen und liefen"),
                   ("Ein doppelter Barcodescan", "denselben Barcode"),
                   ("Nacharbeit: brummende Soundbars", "das Größte")],
        "example": "Die Nacharbeit war das Größte: 1.500 brummende Soundbars im Monat.",
        "example_cue": "das Größte",
        "script": "In einer Stunde füllte Deepaks Team eine Seite. Werker warteten auf verspätete Kits. Sie "
                  "griffen und liefen in jedem Zyklus nach Schraubendrehern. Die Verpackung scannte "
                  "denselben Barcode zweimal, in zwei Systemen. Aber das Größte war die Nacharbeit. "
                  "Fünfzehnhundert Soundbars im Monat fielen beim Brummtest durch und gingen zurück an den "
                  "Reparaturplatz. Wie messen Sie, wie viel Zeit wirklich Wert ist?",
    },
    {
        "key": "p08", "num": 8, "title": "Den Fluss messen",
        "points": [("Flusseffizienz = Wertzeit ÷ Durchlaufzeit", "Die Flusseffizienz ist"),
                   ("18 min Wert in 240 min", "achtzehn Minuten"),
                   ("Nur 7,5 % der Zeit schaffen Wert", "siebeneinhalb")],
        "example": "Eine Soundbar verbringt 4 Stunden im Werk. Nur 18 Minuten verändern sie.",
        "example_cue": "Eine Soundbar verbringt",
        "script": "Geben Sie ihm eine Zahl. Die Flusseffizienz ist die wertschöpfende Zeit, geteilt durch "
                  "die gesamte Durchlaufzeit. Eine Soundbar verbringt vier Stunden in Deepaks Werk. Nur "
                  "achtzehn Minuten davon verändern sie wirklich. Das ist eine Flusseffizienz von "
                  "siebeneinhalb Prozent. Alles andere ist Warten, Bewegen, Prüfen oder Reparieren. Keine "
                  "Panik. Am Anfang ist das normal. Aber welche Verschwendung greifen Sie zuerst an?",
    },
    {
        "key": "p09", "num": 9, "title": "Die Grundursache finden",
        "points": [("Pareto: den größten Verlust wählen", "Nutzen Sie ein Pareto"),
                   ("Fragen Sie warum, mit Belegen", "Dann fragen Sie warum"),
                   ("Die Ursache beheben, nicht das Symptom", "Beheben Sie die Ursache")],
        "example": "Grundursache: keine feste Führung für das Lautsprecherkabel, also berührte es die "
                   "Membran.",
        "example_cue": "Das Kabel hatte",
        "script": "Nutzen Sie ein Pareto, und wählen Sie zuerst den größten Verlust. Für Deepak war das die "
                  "Nacharbeit. Dann fragen Sie warum, mit Belegen. Warum brummten die Soundbars? Ein "
                  "Lautsprecherkabel berührte die Membran. Warum? Das Kabel hatte keine feste Führung. Das "
                  "ist eine Prozessursache, keine nachlässige Person. Beheben Sie die Ursache, nicht das "
                  "Symptom. Welche Maßnahme wählen Sie?",
    },
    {
        "key": "p10", "num": 10, "title": "Maßnahmen: ECRS",
        "points": [("Das Unnötige eliminieren", "Eliminieren Sie, was"),
                   ("Aufgaben oder Prüfungen kombinieren", "Kombinieren Sie Aufgaben"),
                   ("Reihenfolge oder Layout umordnen", "Ordnen Sie Reihenfolge"),
                   ("Das Verbleibende vereinfachen", "Vereinfachen Sie")],
        "example": "Ein Kabelclip, Kit-Wagen an der Linie, ein Scan statt zwei.",
        "example_cue": "Deepaks Team wählte",
        "script": "Denken Sie an ECRS. Eliminieren Sie, was nicht gebraucht wird. Kombinieren Sie Aufgaben, "
                  "die zusammengehören. Ordnen Sie Reihenfolge oder Layout um. Vereinfachen Sie, was "
                  "bleibt. Deepaks Team wählte drei Änderungen. Einen kleinen Clip, der das "
                  "Lautsprecherkabel führt. Kit-Wagen, die stündlich an die Linie kommen. Und ein Scan an "
                  "der Verpackung statt zwei. Welcher ECRS-Buchstabe passt wozu?",
    },
    {
        "key": "p11", "num": 11, "title": "Die Kosten von Fehlern",
        "points": [("Intern: Ausschuss, Nacharbeit, Nachtest", "Interne Fehler bedeuten"),
                   ("Extern: Rücksendungen, Garantie, Fracht", "Externe Fehler bedeuten"),
                   ("Jede Reparatur versteckt mehr Verschwendung", "jede Reparatur")],
        "example": "Nacharbeit: ₹42 pro Soundbar, 1.500 im Monat.",
        "example_cue": "Jede Nacharbeit",
        "script": "Fehler sind die teuerste Verschwendung. Interne Fehler bedeuten Ausschuss, Nacharbeit, "
                  "Nachtest und stehende Linien. Externe Fehler bedeuten Rücksendungen, Garantiefälle und "
                  "Eilfracht. Und jede Reparatur versteckt mehr Verschwendung, wie Handling, Warten und "
                  "Papierkram. Eine brummende Soundbar wurde geöffnet, neu verkabelt, neu getestet und "
                  "erneut erfasst. Jede Nacharbeit an Deepaks Linie kostete zweiundvierzig Rupien. Bei "
                  "fünfzehnhundert im Monat summierte sich das schnell. Hat der Clip also funktioniert?",
    },
    {
        "key": "p12", "num": 12, "title": "Die Ergebnisse",
        "points": [("Nacharbeit: von 1.500 auf 300 im Monat", "Die Nacharbeit sank"),
                   ("Erstdurchlaufquote bis 99 %", "Die Erstdurchlaufquote"),
                   ("Greifen nach Werkzeug: von 22 s auf 13 s", "das Greifen nach Werkzeug")],
        "example": "Gleiche Menschen, gleiche Schicht. Platz für das neue Modell.",
        "example_cue": "Gleiche Menschen",
        "script": "Ja, nach einem Versuch über vier Wochen. Die Nacharbeit sank von fünfzehnhundert auf "
                  "dreihundert Soundbars im Monat. Die Erstdurchlaufquote stieg auf neunundneunzig Prozent. "
                  "Mit Kit-Wagen und Werkzeug griffbereit sank das Greifen nach Werkzeug von zweiundzwanzig "
                  "auf dreizehn Sekunden pro Zyklus. Gleiche Menschen, gleiche Schicht, und jetzt ist Platz "
                  "für das neue Modell. Aber was war es in Geld wert?",
    },
    {
        "key": "p13", "num": 13, "title": "Das Geld beweisen",
        "points": [("Einsparung = vermiedene Kosten − Kosten der Lösung", "Einsparungen sind"),
                   ("Harte Einsparungen von Kapazität trennen", "Trennen Sie harte Einsparungen"),
                   ("Das Controlling bestätigt die Zahlen", "Das Controlling sollte")],
        "example": "1.200 Nacharbeiten weniger × ₹42 × 12 Monate ≈ ₹6 lakh. Minus ₹1,2 lakh für die Lösung: "
                   "≈ ₹4,8 lakh netto.",
        "example_cue": "Zwölfhundert Nacharbeiten weniger",
        "script": "Einsparungen sind die Kosten, die Sie vermeiden, minus die Kosten der Lösung. "
                  "Zwölfhundert Nacharbeiten weniger im Monat, zu zweiundvierzig Rupien, über ein Jahr. Das "
                  "sind etwa sechshunderttausend Rupien. Clips, Wagen und Systemänderung kosteten etwa "
                  "hundertzwanzigtausend. Der Nettonutzen im ersten Jahr liegt also bei etwa "
                  "vierhundertachtzigtausend Rupien. Trennen Sie harte Einsparungen von freier Kapazität. "
                  "Und das Controlling sollte die Zahlen bestätigen. Wie sorgen Sie dafür, dass es hält?",
    },
    {
        "key": "p14", "num": 14, "title": "Damit es hält",
        "points": [("SOP, Layout, Schulung aktualisieren", "Aktualisieren Sie die SOP"),
                   ("Tagestafel: Ziel, Ist, Lücke, Maßnahme", "Eine Tagestafel"),
                   ("Audit nach 7, 30 und 90 Tagen", "Auditieren Sie nach sieben")],
        "example": "Deepaks Audit an Tag 30: eine Schicht nutzte den Clip nicht mehr. Am selben Tag behoben.",
        "example_cue": "An Tag dreißig",
        "script": "Machen Sie den neuen Weg zum normalen Weg. Aktualisieren Sie die SOP, das Layout und die "
                  "Schulung. Eine Tagestafel zeigt Ziel, Ist, Lücke und Maßnahme, mit einem "
                  "Verantwortlichen. Auditieren Sie nach sieben, dreißig und neunzig Tagen, denn "
                  "Abweichungen sind leise. An Tag dreißig nutzte eine Schicht den Clip nicht mehr. Deepaks "
                  "Team fand es und behob es am selben Tag. Hätte Ihr Audit das erkannt?",
    },
    {
        "key": "p15", "num": 15, "title": "Ihr 30-Tage-Plan",
        "points": [("Tage 1–7: Produkt wählen, abgehen, abbilden", "In der ersten Woche"),
                   ("Tage 8–18: Pareto, Grundursache, Pilot", "In den nächsten elf Tagen"),
                   ("Tage 19–30: messen, standardisieren, auditieren", "In den letzten zwölf Tagen")],
        "example": "Dann teilen Sie es: andere Linien übernehmen, was wirkte, nachdem sie geprüft haben, ob "
                   "es passt.",
        "example_cue": "Dann teilen Sie es",
        "script": "Hier ist ein Dreißig-Tage-Plan, den Sie jetzt starten können. In der ersten Woche wählen "
                  "Sie eine Produktfamilie, gehen den Gemba ab und bilden den Fluss ab. In den nächsten elf "
                  "Tagen nutzen Sie ein Pareto, finden die Grundursache und machen einen kleinen Pilot. In "
                  "den letzten zwölf Tagen messen Sie das Ergebnis, aktualisieren den Standard und "
                  "auditieren ihn. Dann teilen Sie es, damit andere Linien übernehmen, was wirkte. Welches "
                  "Produkt gehen Sie zuerst ab?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Kein Kundenwert", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Keine einmaligen Kürzungen", "icon": "calendar", "with": 1},
        {"label": "Ursache beseitigen", "icon": "key", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 1500, "icon": "wave", "label": "Soundbars jeden Monat nachgearbeitet",
                 "unit": "Deepaks Linie", "with": "example"}},
    "p02": {"type": "steps", "items": [
        {"label": "Verändert das Produkt", "with": 0},
        {"label": "Kunde würde zahlen", "with": 1},
        {"label": "Beim ersten Mal richtig", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Nach Klappern neu einbauen", "sub": "Reine Verschwendung", "icon": "wrench", "tone": "bad", "with": "example"},
            {"label": "Lautsprecher einbauen", "sub": "Wert", "icon": "wave", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Schnellerer Fluss", "icon": "chartDown", "with": 0},
        {"label": "Weniger Fehler", "icon": "check", "with": 1},
        {"label": "Freie Kapazität", "icon": "box", "with": 2},
        {"label": "Ideen der Menschen", "icon": "person", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Sicherheits- und Qualitätsprüfungen behalten", "icon": "shield", "tone": "good", "with": 0},
        {"label": "Verschwendung nicht abwälzen", "icon": "sequence", "with": 1},
        {"label": "Menschen sind keine Verschwendung", "icon": "person", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Transport", "icon": "sequence", "with": 0},
        {"label": "Bestände", "icon": "stack", "with": 0},
        {"label": "Bewegung", "icon": "walk", "with": 0},
        {"label": "Warten", "icon": "clock", "with": 0},
        {"label": "Überproduktion", "icon": "box", "with": 1},
        {"label": "Überbearbeitung", "icon": "gear", "with": 1},
        {"label": "Fehler", "icon": "cross", "with": 2},
        {"label": "Ungenutzte Fähigkeiten", "icon": "person", "with": 2}]},
    "p06": {"type": "flow", "items": [
        {"label": "Normale Produktion", "icon": "walk", "with": 0},
        {"label": "Fakten, keine Schuld", "icon": "clipboard", "with": 1},
        {"label": "Wo · wie lange · wie oft", "icon": "clock", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "„Das Lager ist immer zu spät“", "sub": "Meinung", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "„4 warteten 12 Min. auf Gitter“", "sub": "Fakt", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Verspätete Kits", "icon": "clock", "tone": "bad", "with": 0},
        {"label": "Greifen nach Werkzeug", "icon": "walk", "tone": "bad", "with": 1},
        {"label": "Doppelter Scan", "icon": "barcode", "tone": "bad", "with": 2},
        {"label": "Brummende Soundbars", "icon": "wave", "tone": "bad", "with": 3}]},
    "p08": {"type": "compare", "before": {"label": "Durchlaufzeit", "value": 240}, "after": {"label": "Wertschöpfend", "value": 18},
            "unit": "Minuten pro Soundbar", "note": "Flusseffizienz 7,5 %", "with": 1},
    "p09": {"type": "steps", "items": [
        {"label": "Soundbars brummen", "with": 1},
        {"label": "Kabel berührt die Membran", "with": 1},
        {"label": "Keine feste Kabelführung", "with": "example"}]},
    "p10": {"type": "steps", "items": [
        {"label": "Eliminieren", "with": 0}, {"label": "Kombinieren", "with": 1},
        {"label": "Umordnen", "with": 2}, {"label": "Vereinfachen", "with": 3}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Kabelclip", "icon": "shape", "tone": "good", "with": "example"},
            {"label": "Stündliche Kit-Wagen", "icon": "box", "with": "example"},
            {"label": "Ein Scan, nicht zwei", "icon": "barcode", "with": "example"}]}},
    "p11": {"type": "icons", "items": [
        {"label": "Intern", "sub": "Ausschuss, Nacharbeit, Nachtest", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Extern", "sub": "Rücksendungen, Garantie", "icon": "box", "tone": "bad", "with": 1},
        {"label": "Versteckt", "sub": "Handling, Warten, Papierkram", "icon": "clock", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 42, "prefix": "₹", "icon": "wrench", "label": "pro Nacharbeit",
                 "unit": "1.500 Nacharbeiten im Monat", "with": "example"}},
    "p12": {"type": "compare", "before": {"label": "Vorher", "value": 1500}, "after": {"label": "Nachher", "value": 300},
            "unit": "Soundbars im Monat nachgearbeitet", "note": "FPY 99 % · Werkzeuggriff 22 s → 13 s", "with": 0},
    "p13": {"type": "stat", "value": 4.8, "decimals": 1, "prefix": "₹", "suffix": " lakh", "icon": "chartUp",
            "label": "Nettonutzen, erstes Jahr", "unit": "₹6 lakh vermieden − ₹1,2 lakh für die Lösung", "with": "example"},
    "p14": {"type": "timeline", "items": [
        {"label": "Standard aktualisiert", "sub": "Tag 0", "icon": "clipboard", "with": 0},
        {"label": "Audit", "sub": "Tag 7", "icon": "search", "with": 2},
        {"label": "Abweichung erkannt", "sub": "Tag 30", "icon": "warning", "with": "example"},
        {"label": "Audit", "sub": "Tag 90", "icon": "check", "tone": "good", "with": 2}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Abgehen und abbilden", "sub": "Tage 1–7", "icon": "walk", "with": 0},
        {"label": "Ursache und Pilot", "sub": "Tage 8–18", "icon": "search", "with": 1},
        {"label": "Beweisen und halten", "sub": "Tage 19–30", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Ein Produkt verbringt 300 Minuten im Werk, aber nur 30 Minuten verändern es. Wie hoch "
                    "ist die Flusseffizienz?",
        "options": ["10%", "30%", "90%"],
        "correct": 0,
        "explanation": "Flusseffizienz = wertschöpfende Zeit ÷ gesamte Durchlaufzeit = 30 ÷ 300 = 10 %. Die "
                       "anderen 90 % sind Warten, Bewegen, Prüfen oder Reparieren.",
        "q_script": "Kurzer Check. Ein Produkt verbringt dreihundert Minuten im Werk. Nur dreißig Minuten "
                    "verändern es wirklich. Wie hoch ist die Flusseffizienz? Nehmen Sie sich kurz Zeit.",
        "a_script": "Zehn Prozent. Teilen Sie die wertschöpfende Zeit durch die gesamte Durchlaufzeit. Der "
                    "Rest ist Warten, Bewegen, Prüfen oder Reparieren.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Um die Zykluszeit zu senken, schlägt ein Team vor, den Audio-Endtest zu streichen. Was "
                    "sollte passieren?",
        "options": ["Streichen: Tests verändern das Produkt nicht",
                    "Behalten, außer eine Risikobewertung genehmigt es, und die Fehler senken, die er findet",
                    "Den Test zum Kunden verlegen"],
        "correct": 1,
        "explanation": "Vorgeschriebene Qualitätsprüfungen sind keine Verschwendung, die man einfach streicht. "
                       "Behalten Sie den Test, außer eine Risikobewertung genehmigt eine Änderung, und gehen Sie "
                       "die Fehler dahinter an. Ihn zum Kunden zu verlegen, verschiebt nur die Verschwendung.",
        "q_script": "Noch eine, diesmal ein Szenario. Um die Zykluszeit zu senken, will ein Team den "
                    "Audio-Endtest streichen. Was sollte passieren? Überlegen Sie kurz.",
        "a_script": "Behalten Sie den Test, außer eine Risikobewertung genehmigt eine Änderung. Dann gehen "
                    "Sie die Fehler an, die er findet. Ihn zum Kunden zu verlegen, verschiebt nur die "
                    "Verschwendung.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
