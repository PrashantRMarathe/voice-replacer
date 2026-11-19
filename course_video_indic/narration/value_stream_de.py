"""value_stream in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh value_stream_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "vs_de"
NAME = "value_stream_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Value Stream Mapping": "Wäliu Strihm Mäpping",
    "Why-Why": "Wai Wai",
    "Pareto": "Pareto",
    "Kanban": "Kanban",
    "Kaizen": "Kaisen",
    "Gemba": "Gemba",
    "TAKT": "Takt",
    "WIP": "we i pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Eine Set-Top-Box braucht fünfzehn Minuten für Bau und Test. Und doch braucht sie fast "
    "vier Tage bis zum Kunden. Wo bleibt all die Zeit? In dieser Lektion lernen Sie Value "
    "Stream Mapping kennen. Sie sehen, wie Sie den echten Fluss von Material und Information "
    "zeichnen. Dann finden Sie das Warten, und gestalten einen besseren Soll-Zustand. Wir "
    "begleiten Rahul, Verbesserungsingenieur, beim Abbilden der Set-Top-Box-Linie seines "
    "Werks."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Bilden Sie den echten Fluss ab, von Material und "
    "Information. Der Großteil Ihrer Durchlaufzeit steckt im Warten, nicht in der Arbeit. Und "
    "gestalten Sie einen Soll-Zustand, den Sie beweisen können, bevor Sie Bestand senken. "
    "Ihre Aufgabe für diese Woche. Gehen Sie eine Produktfamilie rückwärts vom Versand ab, "
    "und zählen Sie jeden Stapel. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie "
    "die Why-Why-Analyse kennen, um echte Ursachen zu finden."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was eine VSM zeigt",
        "points": [("Eine Produktfamilie, vom Auftrag bis zur Lieferung", "zeigt den ganzen Weg"),
                   ("Material und die Information, die es steuert", "Sie umfasst das Material"),
                   ("Wertschöpfende Arbeit, Warten, Bestand", "Sie zeigt wertschöpfende Arbeit"),
                   ("Ein gemeinsames Bild der Wirklichkeit", "Sie ist ein gemeinsames Bild")],
        "example": "Rahul folgt einer Set-Top-Box von den eingehenden Platinen bis zum Versand, mit "
                   "Planungssignalen und Lagerfreigabe.",
        "example_cue": "Rahul folgt einer Set-Top-Box",
        "script": "Hier ist die Kernidee. Eine Wertstromkarte zeigt den ganzen Weg einer Produktfamilie, "
                  "vom Kundenauftrag bis zur Lieferung. Sie umfasst das Material, und die Information, die "
                  "es steuert. Sie zeigt wertschöpfende Arbeit, Warten, Bestandsstapel und langsame "
                  "Signale. Sie ist ein gemeinsames Bild der Wirklichkeit, kein schmückendes Flussdiagramm. "
                  "Rahul folgt einer Set-Top-Box von den eingehenden Platinen bis zum Versand. Er nimmt "
                  "Planungssignale und Lagerfreigabe auf, nicht nur die Linie. Was zählt für Sie als Wert?",
    },
    {
        "key": "p02", "num": 2, "title": "Wert, Fluss und Verschwendung",
        "points": [("Wert: wofür der Kunde zahlen würde", "Wert ist, wofür Ihr Kunde"),
                   ("Heute nötig, aber ohne Wert", "Manche Arbeit schafft keinen Wert"),
                   ("Reine Verschwendung: Warten, Transport, Nacharbeit", "Dann gibt es reine Verschwendung")],
        "example": "Rahuls Box: 15 Minuten Bau und Test gegen 2 Tage Warten auf die Materialfreigabe.",
        "example_cue": "Rahuls Box verbringt",
        "script": "Wert ist, wofür Ihr Kunde gern zahlen würde. Er ändert Form, Passung oder Funktion des "
                  "Produkts, beim ersten Mal richtig. Manche Arbeit schafft keinen Wert, ist aber heute "
                  "noch nötig, wie eine Pflichtprüfung. Dann gibt es reine Verschwendung, wie Warten, "
                  "Transport und Nacharbeit. Rahuls Box verbringt fünfzehn Minuten mit Bau und Test. Sie "
                  "verbringt zwei Tage mit Warten auf die Materialfreigabe. Was greifen Sie zuerst an? "
                  "Sekunden der Montage, oder Tage des Wartens?",
    },
    {
        "key": "p03", "num": 3, "title": "Produktfamilien und Umfang",
        "points": [("Nicht alles auf einmal abbilden", "Bilden Sie nicht alles"),
                   ("Familie: gleiche Schritte und Anlagen", "Eine Produktfamilie ist"),
                   ("Raster Produkte × Prozesse", "Bauen Sie ein einfaches Raster"),
                   ("Produkte mit gleichem Weg gruppieren", "Dann gruppieren Sie die Produkte")],
        "example": "Handys und Audiogeräte teilen die Verpackung, aber der Test ist ganz anders, also "
                   "getrennte Karten.",
        "example_cue": "Rahul bemerkte, dass Handys",
        "script": "Bilden Sie nicht alles auf einmal ab. Eine Produktfamilie ist eine Gruppe von Teilen, "
                  "die meist dieselben Schritte und Anlagen durchlaufen. Wer fremde Produkte mischt, "
                  "verbirgt Schwankungen, und die Durchschnitte lügen. Bauen Sie ein einfaches Raster, "
                  "Produkte an der Seite, Prozesse oben. Dann gruppieren Sie die Produkte mit gleichem Weg. "
                  "Rahul bemerkte, dass Handys und Audiogeräte die Verpackung teilen, aber ganz anders "
                  "getestet werden. Also bekommen sie getrennte Karten. Welche Familie bilden Sie zuerst "
                  "ab?",
    },
    {
        "key": "p04", "num": 4, "title": "Symbole und Regeln",
        "points": [("Fabriksymbole: Kunde und Lieferant", "Fabriksymbole zeigen"),
                   ("Prozesskästen + Datenkästen", "Prozesskästen zeigen"),
                   ("Dreiecke: wartender Bestand", "Dreiecke zeigen"),
                   ("Material- und Informationspfeile", "Durchgezogene Pfeile tragen")],
        "example": "Kaizen-Blitze markieren Ideen; eine Zeitleiste trennt Bearbeitung und Warten. Immer eine "
                   "Legende ergänzen.",
        "example_cue": "Kaizen-Blitze markieren",
        "script": "Wertstromkarten nutzen eine einfache Bildsprache. Fabriksymbole zeigen Ihren Kunden und "
                  "Lieferanten. Prozesskästen zeigen Arbeitsgänge, mit Datenkästen darunter für Zykluszeit, "
                  "Rüstzeit, Verfügbarkeit und Ausbeute. Dreiecke zeigen wartenden Bestand. Durchgezogene "
                  "Pfeile tragen Material, dünnere Pfeile Information. Kaizen-Blitze markieren "
                  "Verbesserungsideen. Eine Zeitleiste unten trennt Bearbeitung und Warten. Symbole "
                  "variieren je Firma, also ergänzen Sie immer eine Legende. Bereit für echte Daten?",
    },
    {
        "key": "p05", "num": 5, "title": "Gemba-Rundgang und Daten",
        "points": [("Am Gemba beginnen", "Das Abbilden beginnt am Gemba"),
                   ("Vom Versand zurück zum Lieferanten gehen", "Gehen Sie vom Versand"),
                   ("Echte Zyklen selbst messen", "Messen Sie echte Zyklen"),
                   ("WIP an jedem Puffer zählen", "Zählen Sie das WIP")],
        "example": "Rahuls System zeigte eine Zahl für das WIP am Test, seine Zählung eine andere. Er glich "
                   "sie vor jeder Rechnung ab.",
        "example_cue": "Rahuls System zeigte",
        "script": "Das Abbilden beginnt am Gemba, wo die Arbeit wirklich passiert. Gehen Sie vom Versand "
                  "zurück zum Lieferanten. Sie sehen die echten Warteschlangen, und ob Material gezogen "
                  "oder geschoben wird. Messen Sie echte Zyklen selbst, mehrmals, statt Standardzeiten zu "
                  "trauen. Zählen Sie das WIP an jedem Puffer. Rahuls System zeigte eine Zahl für das WIP "
                  "am Test. Seine Zählung zeigte eine andere. Er glich sie ab, bevor er rechnete. Wie "
                  "schnell muss es für Ihren Kunden gehen?",
    },
    {
        "key": "p06", "num": 6, "title": "Kundenbedarf und TAKT",
        "points": [("TAKT: das Tempo, das Ihr Kunde braucht", "TAKT gibt das Tempo vor"),
                   ("Nettozeit ÷ gute Einheiten, gleicher Zeitraum", "Teilen Sie Ihre netto verfügbare"),
                   ("Jede Station damit vergleichen", "Vergleichen Sie nun jede Station")],
        "example": "1.200 gute Boxen in einer Schicht → TAKT 21 Sekunden, etwa 170 pro Stunde. Eine Station "
                   "mit 24 Sekunden schafft das nicht allein.",
        "example_cue": "Rahuls Linie läuft",
        "script": "TAKT gibt das Tempo vor, das Ihr Kunde braucht. Teilen Sie Ihre netto verfügbare Zeit "
                  "durch die geforderten guten Einheiten, im gleichen Zeitraum. Nettozeit lässt geplante "
                  "Pausen und Stopps weg. Rahuls Linie läuft eine Schicht und braucht zwölfhundert gute "
                  "Boxen am Tag. Das ergibt einen TAKT von einundzwanzig Sekunden, etwa hundertsiebzig pro "
                  "Stunde. Vergleichen Sie nun jede Station damit. Eine Station braucht vierundzwanzig "
                  "Sekunden. Was heißt das? Sie hält nicht mit, außer eine zweite läuft parallel.",
    },
    {
        "key": "p07", "num": 7, "title": "Die Ist-Zustand-Karte",
        "points": [("Bedarf rechts, dann nach vorn arbeiten", "Setzen Sie den Kundenbedarf"),
                   ("Daten unter jeden Kasten", "Ergänzen Sie die Daten"),
                   ("Den Informationsfluss zeichnen", "Dann zeichnen Sie den Informationsfluss"),
                   ("Mit Ihren Werkern prüfen", "Fragen Sie zum Schluss Ihre Werker")],
        "example": "Die Planung gab wöchentliche Chargen frei; der Test schaffte nur eine Tagesrate. "
                   "Dazwischen stapelten sich Boxen.",
        "example_cue": "Rahuls Karte zeigte",
        "script": "Nun zeichnen Sie den Ist-Zustand. Setzen Sie den Kundenbedarf rechts, dann arbeiten Sie "
                  "sich durch jeden Prozess und Puffer nach vorn. Ergänzen Sie die Daten unter jedem "
                  "Kasten. Dann zeichnen Sie den Informationsfluss. Prognosen, Tagespläne, Aufträge und "
                  "Kanban-Signale. Rahuls Karte zeigte einen Widerspruch. Die Planung gab wöchentliche "
                  "Chargen an die Montage, aber der Test schaffte nur eine Tagesrate. Also stapelten sich "
                  "halbfertige Boxen dazwischen. Fragen Sie zum Schluss Ihre Werker. Passen die Pfeile zu "
                  "einem normalen Tag?",
    },
    {
        "key": "p08", "num": 8, "title": "Durchlaufzeit und Bestand",
        "points": [("Zeitleiste: Arbeit gegen Warten", "Die Zeitleiste trennt"),
                   ("Warten = Puffer ÷ Tagesbedarf", "Um das Warten zu schätzen"),
                   ("Wertschöpfungsanteil: ein Signal, kein Beweis", "Dieser winzige Anteil")],
        "example": "Drei Puffer bei 1.200 am Tag = 3,5 Tage Warten gegen 15 Minuten Bearbeitung.",
        "example_cue": "Rahul hat drei Puffer",
        "script": "Die Zeitleiste trennt Arbeitszeit von Wartezeit. Um das Warten zu schätzen, teilen Sie "
                  "den Bestand jedes Puffers durch den Tagesbedarf. Rahul hat drei Puffer, und einen Bedarf "
                  "von zwölfhundert am Tag. Zusammen halten sie dreieinhalb Tage Warten. Die echte "
                  "Bearbeitung ergibt nur fünfzehn Minuten. Sehen Sie die Lücke? Dieser winzige Anteil ist "
                  "der Wertschöpfungsanteil. Nehmen Sie ihn als Signal, nicht als Beweis, dass alles Warten "
                  "verschwinden kann. Warum liegt der Bestand dort?",
    },
    {
        "key": "p09", "num": 9, "title": "Engpässe und Ursachen",
        "points": [("Eine Karte zeigt wo, nicht warum", "Eine Karte sagt Ihnen"),
                   ("Lange Schlangen, Eilaufträge, Nacharbeitsschleifen", "Suchen Sie lange Schlangen"),
                   ("Tiefer graben: Pareto, fünf Warum, Fischgräte", "Dann graben Sie tiefer")],
        "example": "2.000 Boxen warten am Test: zu wenig Tester, Stillstand, Firmware oder Chargenfreigaben? "
                   "Vor dem Kauf prüfen.",
        "example_cue": "Rahul fand zweitausend",
        "script": "Eine Karte sagt Ihnen, wo Sie suchen, nicht warum es passiert. Suchen Sie lange "
                  "Schlangen, häufige Eilaufträge und Nacharbeitsschleifen. Dann graben Sie tiefer, mit "
                  "Pareto, fünf Warum oder einer Fischgräte. Rahul fand zweitausend Boxen, die am Test "
                  "warteten. Zu wenig Tester? Stillstand? Instabile Firmware? Oder große Chargenfreigaben? "
                  "Jedes braucht eine andere Lösung. Also prüfte er die Daten, bevor jemand einen Tester "
                  "kaufte. Was prüfen Sie zuerst?",
    },
    {
        "key": "p10", "num": 10, "title": "Soll-Zustand: Fluss und Pull",
        "points": [("Fließfertigung im oder unter dem TAKT", "Nutzen Sie Fließfertigung"),
                   ("Begrenzte First-in-first-out-Bahnen", "nutzen Sie eine First-in-first-out-Bahn"),
                   ("Supermarkt mit Pull-Signalen", "nutzen Sie einen Supermarkt"),
                   ("Ein Schrittmacherprozess", "Dann wählen Sie einen Schrittmacher")],
        "example": "Rahuls Entwurf: Montage und Verpackung teilen eine begrenzte Bahn; Platinen werden aus "
                   "einem Supermarkt gezogen.",
        "example_cue": "In Rahuls Entwurf",
        "script": "Nun gestalten Sie den Soll-Zustand. Er muss besser sein, und auch realistisch. Nutzen "
                  "Sie Fließfertigung, wo Schritte im oder unter dem TAKT laufen. Wo nicht, nutzen Sie eine "
                  "First-in-first-out-Bahn mit fester Grenze. Wo Fluss gar nicht verbindet, nutzen Sie "
                  "einen Supermarkt mit Pull-Signalen. Dann wählen Sie einen Schrittmacher, den einen "
                  "Prozess, den Sie einplanen. In Rahuls Entwurf teilen Montage und Verpackung eine "
                  "begrenzte Bahn. Platinen werden aus einem Supermarkt gezogen. Wo könnte Ihre Linie "
                  "fließen?",
    },
    {
        "key": "p11", "num": 11, "title": "Pitch, Kanban und Nachschub",
        "points": [("Pitch = TAKT × Packmenge", "Der Pitch ist der Rhythmus"),
                   ("Kanban-Größe: Wiederbeschaffungszeit und Bedarf", "Kanban-Größen hängen"),
                   ("Nachschub beweisen, bevor Bestand sinkt", "Beweisen Sie, dass der Nachschub")],
        "example": "Packungen zu 20 → ein Pitch von 7 Minuten. Ein Kit reicht 6 Minuten, Nachschub dauert "
                   "12: mehr Kits, oder schnellerer Nachschub.",
        "example_cue": "Rahuls Packungen fassen",
        "script": "Glätten macht Pull-Signale berechenbar. Der Pitch ist der Rhythmus, um eine "
                  "Standardpackung zu bewegen. Er ist TAKT mal Packmenge. Rahuls Packungen fassen zwanzig "
                  "Boxen, also ist sein Pitch sieben Minuten. Kanban-Größen hängen von "
                  "Wiederbeschaffungszeit und Bedarf ab. Ein Kit reicht sechs Minuten, aber Nachschub "
                  "dauert zwölf. Er braucht also mehr Kits, oder schnelleren Nachschub. Die Regel für Sie. "
                  "Beweisen Sie, dass der Nachschub wirkt, bevor Sie Bestand senken. Bereit für den ganzen "
                  "Fall?",
    },
    {
        "key": "p12", "num": 12, "title": "Durchgerechnete Fallstudie",
        "points": [("1.200 Boxen am Tag; 4.200 wartend", "Der Bedarf ist zwölfhundert"),
                   ("3,5 Tage Wartezeit", "Das sind dreieinhalb Tage"),
                   ("Soll-Zustand: Puffer halbiert", "Sein Soll-Zustand halbiert"),
                   ("Zuerst Kapazität, Material, Qualität bestätigen", "Halten Testkapazität")],
        "example": "Die Wartezeit sinkt unter zwei Tage, 50 % weniger. Aber er schaltet noch nicht um.",
        "example_cue": "Die Wartezeit sinkt",
        "script": "Hier Rahuls Fall, mit Übungszahlen. Der Bedarf ist zwölfhundert Boxen am Tag. Heute "
                  "warten zweiundvierzighundert Einheiten in drei Puffern. Das sind dreieinhalb Tage "
                  "Wartezeit. Sein Soll-Zustand halbiert jeden Puffer, auf einundzwanzighundert Einheiten. "
                  "Die Wartezeit sinkt unter zwei Tage. Das sind fünfzig Prozent weniger. Aber er schaltet "
                  "noch nicht um. Halten Testkapazität, Materiallieferung und Qualitätskontrollen mit "
                  "weniger Puffer stand? Wie würden Sie das prüfen?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI und echter Nutzen",
        "points": [("Den ganzen Fluss messen", "Messen Sie den ganzen Fluss"),
                   ("Durchlaufzeit, WIP, Liefertreue, FPY", "Verfolgen Sie Durchlaufzeit, WIP"),
                   ("Ausgangswert, dann wochenlang bestätigen", "Legen Sie einen Ausgangswert fest"),
                   ("Auf Bestand achten, der nur verschoben wurde", "Achten Sie auf Bestand")],
        "example": "Weniger WIP setzt etwa ₹31 lakh Bestand frei: einmal freigesetztes Geld, kein jährlicher "
                   "Gewinn.",
        "example_cue": "Rahuls geringeres WIP",
        "script": "Messen Sie den ganzen Fluss, nicht nur das Stationstempo. Verfolgen Sie Durchlaufzeit, "
                  "WIP, Liefertreue und Erstdurchlaufquote. Legen Sie einen Ausgangswert fest, dann "
                  "bestätigen Sie über mehrere typische Wochen. Achten Sie auf Bestand, der nur woandershin "
                  "wanderte. Eine Geldfalle. Rahuls geringeres WIP setzt etwa drei Komma eins Millionen "
                  "Rupien an Bestand frei. Das ist einmal freigesetztes Geld. Es ist kein jährlicher Gewinn "
                  "in dieser Höhe. Würde Ihre Finanzabteilung den Unterschied sehen? Berichten Sie ehrlich.",
    },
    {
        "key": "p14", "num": 14, "title": "Steuerung und 90 Tage",
        "points": [("Jede Funktion hat eine Rolle", "Wertstromverbesserung braucht"),
                   ("Tag 1–30: Familie wählen, Ist abbilden", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: Soll gestalten, Pull pilotieren", "In den nächsten dreißig"),
                   ("Tag 61–90: stabilisieren, auditieren, ausweiten", "In den letzten dreißig")],
        "example": "Rahul behob den Test-Engpass, bevor er dessen Puffer senkte. Sonst läuft die Linie leer.",
        "example_cue": "Rahul behob den Test-Engpass",
        "script": "Wertstromverbesserung braucht jede Funktion. Die Planung verantwortet die Planlogik. Die "
                  "Produktion den Fluss, die Qualität die Kontrollen, die Materialwirtschaft den Nachschub. "
                  "Das Management räumt Hindernisse weg. In den ersten dreißig Tagen wählen Sie die Familie "
                  "und bilden den Ist-Zustand ab. In den nächsten dreißig gestalten Sie den Soll-Zustand "
                  "und pilotieren Pull. In den letzten dreißig stabilisieren, auditieren und weiten Sie "
                  "aus. Rahul behob den Test-Engpass, bevor er dessen Puffer senkte. Sonst läuft die Linie "
                  "leer. Ihr erster Pilot?",
    },
    {
        "key": "p15", "num": 15, "title": "Was tun, was lassen, Vorlage",
        "points": [("Bei Änderung von Bedarf oder Weg anpassen", "Passen Sie sie an"),
                   ("Echten Fluss abbilden, Werker einbeziehen", "Bilden Sie also den echten Fluss"),
                   ("Zykluszeit ≠ Durchlaufzeit", "verwechseln Sie nicht Zykluszeit"),
                   ("Kapazität prüfen, bevor Puffer wegfallen", "entfernen Sie keine Puffer")],
        "example": "Eine Karte nur mit Prozesskästen ist keine Wertstromkarte. Sie ist nur ein "
                   "Flussdiagramm.",
        "example_cue": "Eine Karte nur mit Prozesskästen",
        "script": "Eine gute Karte ist ein lebendes Entscheidungswerkzeug. Passen Sie sie an, wenn Bedarf, "
                  "Weg oder große Engpässe sich ändern. Bilden Sie also den echten Fluss ab, mit "
                  "einheitlichen Einheiten, und beziehen Sie Ihre Werker ein. Zeigen Sie Nacharbeitswege "
                  "und Planungssignale. Aber verwechseln Sie nicht Zykluszeit mit Durchlaufzeit. Nennen Sie "
                  "einmal freigesetztes Geld keine jährliche Einsparung. Und entfernen Sie keine Puffer, "
                  "bevor Sie Kapazität und Nachschub geprüft haben. Eine Karte nur mit Prozesskästen ist "
                  "keine Wertstromkarte. Sie ist nur ein Flussdiagramm.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Eine Produktfamilie", "icon": "box"}, {"label": "Material + Information", "icon": "sequence"},
        {"label": "Arbeit gegen Warten", "icon": "clock"}, {"label": "Ein gemeinsames Bild", "icon": "person"}]},
    "p02": {"type": "versus", "items": [
        {"label": "2 Tage Warten", "sub": "auf die Materialfreigabe", "icon": "clock", "with": "example"},
        {"label": "15 Minuten echte Arbeit", "sub": "gebaut und getestet", "icon": "wrench", "with": "example"}]},
    "p03": {"type": "matrix", "prefix": "check", "cols": ["Montage", "Handytest", "Audiotest", "Verpackung"],
            "note": "Gleiche Verpackung, anderer Test: getrennte Karten", "items": [
        {"label": "Handys", "cells": [3, 3, None, 3], "with": 2},
        {"label": "Audio", "cells": [3, None, 3, 3], "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Kunde, Lieferant", "icon": "box"}, {"label": "Prozess- + Datenkästen", "icon": "clipboard"},
        {"label": "Dreiecke: Bestand", "icon": "stack"}, {"label": "Material gegen Information", "icon": "sequence"}]},
    "p05": {"type": "flow", "items": [
        {"label": "Zum Gemba gehen", "icon": "walk"},
        {"label": "Vom Versand zurück", "icon": "sequence"},
        {"label": "Echte Zyklen messen", "icon": "clock"},
        {"label": "Jeden Puffer zählen", "sub": "Mit dem System abgleichen", "icon": "count", "tone": "good"}]},
    "p06": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Das Tempo des Kunden", "icon": "clock", "with": 0},
        {"label": "Nettozeit ÷ gute Einheiten", "icon": "count", "with": 1},
        {"label": "Jede Station vergleichen", "icon": "scale", "with": 2}],
        "then": {"type": "bars", "label": "TAKT", "value": 21, "suffix": " s", "note": "schafft es nicht allein",
                 "unit": "1.200 gute Boxen pro Schicht ≈ 170 pro Stunde", "with": "example", "items": [
            {"label": "Eine Station", "value": 24, "tone": "bad", "with": "example"}]}},
    "p07": {"type": "flow", "items": [
        {"label": "Planung: Wochenchargen", "icon": "calendar", "with": "example"},
        {"label": "Boxen stapeln sich", "sub": "Halbfertig, wartend", "icon": "stack", "tone": "bad", "with": "example"},
        {"label": "Test: eine Tagesrate", "icon": "test", "with": "example"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Arbeit gegen Warten", "icon": "clock", "with": 0},
        {"label": "Puffer ÷ Tagesbedarf", "icon": "count", "with": 1},
        {"label": "Wertschöpfungsanteil", "sub": "Ein Signal, kein Beweis", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 3.5, "decimals": 1, "suffix": " Tage", "icon": "clock", "label": "Warten",
                 "unit": "gegen nur 15 Minuten Bearbeitung", "with": "example"}},
    "p09": {"type": "flow", "items": [
        {"label": "Eine Karte zeigt wo, nicht warum", "icon": "search", "with": 0},
        {"label": "Schlangen, Eilaufträge, Nacharbeit", "icon": "stack", "with": 1},
        {"label": "Pareto, fünf Warum, Fischgräte", "icon": "gear", "with": 2}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Zu wenig Tester?", "icon": "test", "with": "example"},
            {"label": "Stillstand?", "icon": "clock", "with": "example"},
            {"label": "Firmware?", "icon": "chip", "with": "example"},
            {"label": "Chargenfreigaben?", "icon": "stack", "with": "example"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "Platinen aus einem Supermarkt gezogen", "icon": "tray"},
        {"label": "Montage", "icon": "wrench"},
        {"label": "Eine begrenzte FIFO-Bahn", "icon": "sequence"},
        {"label": "Verpackung: der Schrittmacher", "icon": "box", "tone": "good"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Pitch = TAKT × Packung", "icon": "count", "with": 0},
        {"label": "Kanban-Größe", "icon": "label", "with": 1},
        {"label": "Nachschub beweisen", "icon": "check", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Packungen zu 20: ein Pitch von 7 Minuten", "icon": "box", "with": "example"},
            {"label": "Ein Kit reicht 6 Min.; Nachschub dauert 12", "icon": "clock", "tone": "bad", "with": "example"},
            {"label": "Mehr Kits, oder schnellerer Nachschub", "icon": "check", "tone": "good", "with": "example"}]}},
    "p12": {"type": "stat", "value": 3.5, "decimals": 1, "suffix": " Tage", "icon": "clock", "label": "Wartezeit heute",
            "unit": "4.200 wartende Einheiten ÷ 1.200 am Tag", "with": 1,
            "then": {"type": "compare", "before": {"label": "Heute", "value": 4200}, "after": {"label": "Soll-Zustand", "value": 2100},
                     "unit": "wartende Einheiten in drei Puffern", "note": "Wartezeit halbiert (geplant)", "with": 2}},
    "p13": {"type": "icons", "items": [
        {"label": "Der ganze Fluss", "icon": "sequence"}, {"label": "Durchlaufzeit, WIP, Liefertreue, FPY", "icon": "chartUp"},
        {"label": "Ausgangswert, dann Wochen", "icon": "calendar"}, {"label": "Bestand, der nur wanderte", "icon": "stack", "tone": "bad"}],
        "then": {"type": "stat", "value": 31, "prefix": "₹", "suffix": " lakh", "icon": "box", "label": "Bestand freigesetzt",
                 "unit": "Einmal freigesetztes Geld: kein jährlicher Gewinn", "with": "example"}},
    "p14": {"type": "timeline", "items": [
        {"label": "Familie wählen, Ist abbilden", "sub": "Tag 1–30", "icon": "search", "with": 1},
        {"label": "Soll gestalten, Pull pilotieren", "sub": "31–60", "icon": "sequence", "with": 2},
        {"label": "Stabilisieren, auditieren, ausweiten", "sub": "61–90", "icon": "chartUp", "with": 3}]},
    "p15": {"type": "icons", "items": [
        {"label": "Bei Änderungen anpassen", "icon": "sequence", "tone": "good"},
        {"label": "Echter Fluss, mit Werkern", "icon": "person", "tone": "good"},
        {"label": "Zyklus ≠ Durchlaufzeit", "icon": "cross", "tone": "bad"},
        {"label": "Kapazität vor dem Pufferabbau", "icon": "warning", "tone": "bad"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Ein Puffer hält 2.400 Einheiten, und der Bedarf ist 1.200 am Tag. Wie viele Tage Bestand "
                    "sind das?",
        "options": ["Ein halber Tag", "2 Tage", "1.200 Tage"],
        "correct": 1,
        "explanation": "Bestandstage = wartende Einheiten ÷ Tagesbedarf = 2.400 ÷ 1.200 = 2 Tage.",
        "q_script": "Kurzer Check. Ein Puffer hält vierundzwanzighundert Einheiten, und der Bedarf ist "
                    "zwölfhundert am Tag. Wie viele Tage Bestand sind das? Nehmen Sie sich kurz Zeit.",
        "a_script": "Zwei Tage. Teilen Sie die wartenden Einheiten durch den Tagesbedarf. Der Puffer hält "
                    "genau zwei Tage Leistung.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Rahul findet 2.000 Boxen, die am Test warten. Was sollte das Team ZUERST tun?",
        "options": ["Sofort einen weiteren Tester kaufen", "Die Ursache bestätigen: Kapazität, Stillstand, Firmware oder Chargenfreigabe",
                    "Den Puffer halbieren, um Fluss zu erzwingen"],
        "correct": 1,
        "explanation": "Eine Karte zeigt, wo Sie suchen, nicht warum. Bestätigen Sie zuerst den Mechanismus; ein "
                       "Tester oder ein blind halbierter Puffer löst vielleicht nichts, oder lässt die Linie "
                       "leerlaufen.",
        "q_script": "Noch eine, ein Szenario. Rahul findet zweitausend Boxen, die am Test warten. Was sollte "
                    "das Team zuerst tun? Überlegen Sie kurz.",
        "a_script": "Bestätigen Sie zuerst die Ursache. Kapazität, Stillstand, Firmware oder große "
                    "Chargenfreigaben. Ein neuer Tester oder ein blind gesenkter Puffer löst vielleicht "
                    "nichts, oder lässt die Linie leerlaufen.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
