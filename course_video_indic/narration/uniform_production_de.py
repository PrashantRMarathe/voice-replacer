"""uniform_production in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh uniform_production_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "up_de"
NAME = "uniform_production_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Heijunka": "Hejdschunka",
    "Kanban": "Kanban",
    "Mura": "Mura",
    "Muri": "Muri",
    "Muda": "Muda",
    "TAKT": "Takt",
    "EPEI": "e pe e i",
    "SMED": "Smed",
    "WIP": "we i pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Montag, dreitausend Handys. Dienstag, fast nichts. Am Mittwoch ertrinkt der Prüfplatz, "
    "und die Überstunden steigen. Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie "
    "die Uniform Production kennen. Sie sehen, wie Sie Menge und Mix glätten, damit Ihre "
    "Linie ein stetiges Tempo hält, das sie wirklich schafft. Wir begleiten Kavya, "
    "Produktionsplanerin in einem Elektronikwerk, die einen sehr holprigen Plan beruhigt."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Glätten Sie Menge und Mix, passend zum echten Bedarf. "
    "Prüfen Sie Engpässe und Umrüstungen, bevor Sie einem Muster trauen. Und machen Sie den "
    "Plan sichtbar, mit klaren Regeln für Änderungen. Ihre Aufgabe für diese Woche. Suchen "
    "Sie ein Produkt, das Sie in großer Charge bauen, und skizzieren Sie ein kleineres, "
    "wiederholtes Muster. Gut gemacht, Lektion abgeschlossen. Als Nächstes bilden Sie Ihren "
    "ganzen Wertstrom ab."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Uniform Production heißt",
        "points": [("Glätten: Heijunka", "Uniform Production heißt glätten"),
                   ("Menge und Mix glätten", "Sie glätten beides"),
                   ("Ein stetiges Freigabemuster", "Unregelmäßige Aufträge werden"),
                   ("Echten Bedarf treffen, nicht gleiche Mengen", "Aber glätten heißt nicht")],
        "example": "Kavyas Werk baut Handys, Boxen und Audiogeräte, in kleinen, wiederholten Folgen, nicht "
                   "erst alle Handys.",
        "example_cue": "Kavyas Werk baut",
        "script": "Hier ist die Kernidee. Uniform Production heißt glätten. Lean nennt es Heijunka. Sie "
                  "glätten beides, Menge und Mix dessen, was Sie bauen, über einen festen Zeitraum. "
                  "Unregelmäßige Aufträge werden ein stetiges Freigabemuster, das Ihre Linie wirklich "
                  "schafft. Aber glätten heißt nicht, von allem gleich viel zu machen. Es heißt, Mix und "
                  "Rate dem echten Bedarf anzupassen. Kavyas Werk baut Handys, Set-Top-Boxen und "
                  "Audiogeräte. Statt erst alle Handys plant sie kleine, wiederholte Folgen. Warum zählt "
                  "das?",
    },
    {
        "key": "p02", "num": 2, "title": "Warum Glätten zählt",
        "points": [("Bedarf kommt nie gleichmäßig", "Bedarf kommt fast nie"),
                   ("Spitzen jagen: Überstunden, Bestand, wacklige Qualität", "Wenn Sie jeder Spitze"),
                   ("Glätten innerhalb eines Planungsfensters", "Glätten verteilt Ihre Freigaben"),
                   ("Etwas Puffer braucht es weiter", "Sie brauchen weiter etwas Puffer")],
        "example": "Am Montag kam ein großer Handyauftrag. Kavya verteilte ihn über die Woche, wie der "
                   "Liefertermin es erlaubte.",
        "example_cue": "Letzte Woche kam",
        "script": "Bedarf kommt fast nie gleichmäßig. Wenn Sie jeder Spitze nachjagen, gibt es Überstunden, "
                  "Berge an Fertigware, gehetzte Lieferanten und wacklige Qualität. Glätten verteilt Ihre "
                  "Freigaben innerhalb eines vereinbarten Planungsfensters. Es löscht Bedarfsschwankungen "
                  "nicht aus, und Sie brauchen weiter etwas Puffer. Letzte Woche kam am Montag ein großer "
                  "Handyauftrag. Kavya baute ihn nicht an einem Tag. Sie verteilte ihn über die Woche, weil "
                  "der Termin es erlaubte. Was genau geht schief bei ungleicher Arbeit?",
    },
    {
        "key": "p03", "num": 3, "title": "Mura, Muri und Muda",
        "points": [("Mura: Unausgeglichenheit", "Mura ist Unausgeglichenheit"),
                   ("Muri: Überlastung", "Muri ist Überlastung"),
                   ("Muda: Verschwendung", "Muda ist Verschwendung")],
        "example": "Der Tester schafft ~2.000 Einheiten am Tag; die Montage gab an einem Tag über 3.000 zum "
                   "Test frei, eine Warteschlange entstand.",
        "example_cue": "Kavyas Funktionstester",
        "script": "Lean nennt drei verknüpfte Probleme. Mura ist Unausgeglichenheit. Muri ist Überlastung. "
                  "Muda ist Verschwendung. So hängen sie zusammen. Ungleiche Freigaben schaffen Spitzen. "
                  "Spitzen überlasten Menschen und Maschinen. Und Überlastung bringt Fehler, Warten und "
                  "zusätzlichen Bestand. Kavyas Funktionstester schafft etwa zweitausend Einheiten am Tag. "
                  "Letzten Monat gab die Montage an einem Tag über dreitausend zum Test frei. Die Montage "
                  "erfüllte ihren Plan, aber am Test staute es sich. Sehen Sie diese Kette an Ihrer Linie?",
    },
    {
        "key": "p04", "num": 4, "title": "Mengenglättung",
        "points": [("Leistung über einen Horizont verteilen", "Die Mengenglättung verteilt"),
                   ("Nettobedarf = Bedarf + Endbestand − Bestand", "Ermitteln Sie zuerst den Nettobedarf"),
                   ("Durch die Produktionstage teilen", "Dann teilen Sie durch die Produktionstage"),
                   ("Material, Ausbeute, Verfügbarkeit, Personal prüfen", "Prüfen Sie Material")],
        "example": "30.000 Einheiten Nettobedarf über 5 Tage = stetig 6.000 gute Einheiten am Tag.",
        "example_cue": "Kavyas Nettobedarf",
        "script": "Beginnen Sie mit der Menge. Die Mengenglättung verteilt Ihre geplante Leistung über "
                  "einen sinnvollen Horizont. Ermitteln Sie zuerst den Nettobedarf. Das ist Kundenbedarf, "
                  "plus gewünschter Endbestand, minus nutzbarer Bestand. Dann teilen Sie durch die "
                  "Produktionstage. Kavyas Nettobedarf diese Woche ist dreißigtausend Einheiten, über fünf "
                  "Tage. Das sind stetig sechstausend gute Einheiten am Tag. Aber hält Ihre Linie das? "
                  "Prüfen Sie Material, Ausbeute, Verfügbarkeit und Personal.",
    },
    {
        "key": "p05", "num": 5, "title": "Mix-Glättung",
        "points": [("Kleine, wiederholte Muster nach Bedarf", "Die Mix-Glättung wiederholt"),
                   ("Verhältnis aus dem Bedarf", "Das ist ein Verhältnis drei, zwei, eins"),
                   ("Umrüstungen, Vorrichtungen, Teile prüfen", "Sie müssen Umrüstungen")],
        "example": "3.000 Handys, 2.000 Boxen, 1.000 Audio → 3 : 2 : 1 → Handy–Box–Handy–Audio–Box–Handy.",
        "example_cue": "Kavya braucht dreitausend",
        "script": "Nun der Mix. Die Mix-Glättung wiederholt Ihre Produkte in kleinen Mustern nach Bedarf, "
                  "statt einer großen Charge je Produkt. Kavya braucht dreitausend Handys, zweitausend "
                  "Boxen und tausend Audiogeräte. Das ist ein Verhältnis drei, zwei, eins. Ein Muster aus "
                  "sechs Einheiten wäre also Handy, Box, Handy, Audio, Box, Handy. Aber ein ordentliches "
                  "Muster auf Papier ist nicht automatisch baubar. Sie müssen Umrüstungen, Vorrichtungen "
                  "und Teile zuerst prüfen. Wie schnell sollte das Muster laufen?",
    },
    {
        "key": "p06", "num": 6, "title": "TAKT Zeit und Pitch",
        "points": [("TAKT: das Tempo, das der Kunde verlangt", "TAKT ist das Tempo"),
                   ("Nettozeit ÷ benötigte gute Einheiten", "Teilen Sie Ihre netto verfügbare"),
                   ("Pitch: Zeit für die Freigabe einer Charge", "Der Pitch ist die Zeit"),
                   ("Durchschnitts-TAKT ≠ jedes Modell hält mit", "Ein Durchschnitts-TAKT beweist nicht")],
        "example": "Eine Einheit alle 4,2 Sekunden → ein Pitch von 100 Einheiten in 7 Minuten.",
        "example_cue": "Kavyas Schicht braucht",
        "script": "Hier kommt der TAKT ins Spiel. TAKT ist das Tempo, das Ihr Kunde verlangt. Teilen Sie "
                  "Ihre netto verfügbare Zeit durch die benötigten guten Einheiten. Das Glätten legt dann "
                  "die Reihenfolge der Freigaben in diesem Tempo fest. Der Pitch ist die Zeit, eine Charge "
                  "freizugeben, oft hundert Einheiten. Kavyas Schicht braucht eine Einheit alle vier Komma "
                  "zwei Sekunden. Ein Pitch von hundert Einheiten dauert also sieben Minuten. Aber "
                  "Vorsicht. Ein Durchschnitts-TAKT beweist nicht, dass jedes Modell mithält. Wie zeigen "
                  "Sie den Plan?",
    },
    {
        "key": "p07", "num": 7, "title": "Die Glättungstafel",
        "points": [("Ein visueller Plan", "Sie ist ein visueller Plan"),
                   ("Zeitfenster quer, Produkte nach unten", "Zeitfenster laufen"),
                   ("Karten: was freigeben, wie viele", "Karten in jedem Fenster"),
                   ("Fehlende und Engpässe sichtbar", "Verpasste Fenster")],
        "example": "Alle 30 Minuten gibt Kavyas Tafel das nächste Los frei; die Kits werden in dieser Folge "
                   "vorbereitet.",
        "example_cue": "Alle dreißig Minuten",
        "script": "Mit einer Glättungstafel. Sie ist ein visueller Plan. Zeitfenster laufen über die "
                  "Spalten, Produkte über die Zeilen. Karten in jedem Fenster zeigen, was freigegeben wird, "
                  "und wie viel. Alle dreißig Minuten gibt Kavyas Tafel das nächste Los frei. Kits werden "
                  "in dieser Folge vorbereitet, nicht nach Bequemlichkeit. Verpasste Fenster und Engpässe "
                  "sind auf einen Blick sichtbar. Ein kurzer Test für Ihre Linie. Sieht ein Werker die "
                  "nächste Freigabe, und wen er anruft, ohne zu fragen?",
    },
    {
        "key": "p08", "num": 8, "title": "EPEI und Umrüstung",
        "points": [("Kleine Muster = mehr Umrüstungen", "Kleine Muster heißen"),
                   ("EPEI: jedes Teil in jedem Intervall", "EPEI misst"),
                   ("SMED: Rüsten außerhalb der Stillstandszeit", "Darum zählt SMED")],
        "example": "6 Umrüstungen am Tag: 20 → 8 Minuten = 72 Minuten zurück, jeden Tag.",
        "example_cue": "Kavyas sechs tägliche Umrüstungen",
        "script": "Kleine Muster heißen mehr Umrüstungen. EPEI misst, wie oft Sie jedes Teil fertigen. Es "
                  "steht für Every Part Every Interval. Kavya baut jede Familie einmal am Tag, also ist ihr "
                  "EPEI ein Tag. Jede zweimal pro Schicht zu bauen reagiert schneller, verdoppelt aber die "
                  "Umrüstungen. Darum zählt SMED. Sie verlegen Rüstarbeit aus der Stillstandszeit. Kavyas "
                  "sechs tägliche Umrüstungen sanken von zwanzig auf acht Minuten. Das sind zweiundsiebzig "
                  "Minuten zurück, jeden Tag. Wo verliert Ihre Linie Zeit?",
    },
    {
        "key": "p09", "num": 9, "title": "Engpässe und gemischte Modelle",
        "points": [("Glätten schlägt keine Kapazitätsgrenze", "Glätten überwindet"),
                   ("Stationen nach dem echten Mix belasten", "Sie müssen jede Station"),
                   ("Das langsamste Modell nicht blockweise", "Und plant sie")],
        "example": "40 % der Einheiten brauchen einen 12-Sekunden-Test = etwa 340 Tests/Stunde gegen ~300 "
                   "eines Testers. Zweiten Tester ergänzen.",
        "example_cue": "Vierzig Prozent der Einheiten",
        "script": "Eine harte Wahrheit. Glätten überwindet keine echte Kapazitätsgrenze. Sie müssen jede "
                  "Station nach dem echten Mix belasten, nicht nach dem Durchschnitt. Kavya prüfte ihren "
                  "Testbereich. Vierzig Prozent der Einheiten brauchen einen Test von zwölf Sekunden. Das "
                  "sind etwa dreihundertvierzig Tests pro Stunde. Ein Tester schafft etwa dreihundert, noch "
                  "vor Verlusten. Sie braucht also einen zweiten Tester, egal in welcher Folge. Und plant "
                  "sie das langsamste Modell in einem Block, ertrinkt der Tester. Kennen Sie Ihr "
                  "langsamstes Modell?",
    },
    {
        "key": "p10", "num": 10, "title": "Kanban und WIP-Steuerung",
        "points": [("Kanban: was nachfüllen, wann", "Kanban-Signale sagen"),
                   ("Standardbehälter, First-in-first-out-Bahnen", "Standardbehälter"),
                   ("WIP-Grenzen stoppen Überproduktion", "WIP-Grenzen stoppen"),
                   ("Kommissionierung passend zu Pitch und Mix", "Passen Sie die Kommissionierung")],
        "example": "Ein Kit für Set-Top-Boxen fehlte. Das Team erfasste es und folgte der freigegebenen "
                   "Umplanungsregel.",
        "example_cue": "Letzten Dienstag",
        "script": "Ein geglätteter Plan braucht stetiges Material. Kanban-Signale sagen dem Lager, was es "
                  "nachfüllen soll, und wann. Standardbehälter und First-in-first-out-Bahnen verhindern, "
                  "dass die Linie leerläuft. WIP-Grenzen stoppen die Überproduktion vorn. Passen Sie die "
                  "Kommissionierung an Pitch und Mix an. Letzten Dienstag fehlte ein Kit für Set-Top-Boxen. "
                  "Kavyas Team tauschte nicht still ein anderes Teil ein. Es erfasste den Fall und folgte "
                  "der freigegebenen Umplanungsregel. Was würde Ihr Team tun?",
    },
    {
        "key": "p11", "num": 11, "title": "Umgang mit Bedarfsänderungen",
        "points": [("Ein eingefrorenes kurzfristiges Fenster", "Sie brauchen also einen Planungshorizont"),
                   ("Umplanen in der Fertigung schafft Chaos", "Ständiges Umplanen"),
                   ("Festlegen, wer Änderungen freigibt", "Legen Sie fest, wer")],
        "example": "500 Audiogeräte früher gewünscht: Kavya prüfte zuerst Termine, Bestand, Teile und "
                   "Testkapazität.",
        "example_cue": "Eines Morgens wollte",
        "script": "Der Bedarf ändert sich trotzdem. Sie brauchen also einen Planungshorizont, und ein "
                  "kurzfristiges Fenster, das eingefroren oder streng gesteuert ist. Ständiges Umplanen in "
                  "der Fertigung schafft Chaos. Legen Sie fest, wer eine Änderung der Folge freigeben darf, "
                  "und warum. Eines Morgens wollte ein Kunde fünfhundert Audiogeräte früher. Kavya "
                  "drängelte nicht einfach vor. Sie prüfte zuerst Termine, Fertigware, Bauteile und "
                  "Testkapazität. Dann änderte sie die nächsten Fenster. Wer gibt bei Ihnen Änderungen "
                  "frei?",
    },
    {
        "key": "p12", "num": 12, "title": "KPI der Glättung",
        "points": [("Leistung und Stabilität zusammen verfolgen", "Verfolgen Sie Leistung und Stabilität"),
                   ("Plantreue", "Die Plantreue vergleicht"),
                   ("WIP-Tage", "Die WIP-Tage zeigen"),
                   ("Dazu FPY, Stillstand, Überstunden", "Ergänzen Sie die Erstdurchlaufquote")],
        "example": "95 % der geplanten Einheiten erledigt. 12.000 Einheiten WIP = 2 Tage Leistung.",
        "example_cue": "Kavyas Linie schaffte",
        "script": "Woran erkennen Sie, dass Glätten wirkt? Verfolgen Sie Leistung und Stabilität zusammen. "
                  "Die Plantreue vergleicht, was Sie fertig haben, mit dem, was geplant war. Kavyas Linie "
                  "schaffte fünfundneunzig Prozent der geplanten Einheiten. Die WIP-Tage zeigen, wie lange "
                  "Arbeit wartet. Ihre zwölftausend Einheiten WIP sind zwei Tage Leistung. Ergänzen Sie die "
                  "Erstdurchlaufquote, Stillstand und Überstunden. Sonst verbessern Sie die Plantreue und "
                  "schaden still der Qualität. Welche Zahlen prüft Ihr Team täglich?",
    },
    {
        "key": "p13", "num": 13, "title": "Fallstudie: gemeinsame Linie",
        "points": [("Mix 3 : 2 : 1, TAKT 4,2 s", "Der Mix ist drei"),
                   ("Muster aus 60 Einheiten: 30 · 20 · 10", "Sie testet ein Muster"),
                   ("Arbeitsfolge, Werkzeuge, Testgrenzen prüfen", "Aber zuerst prüft sie"),
                   ("Schnellere Umrüstungen, keine Abkürzungen", "Sie beschleunigte die Umrüstungen")],
        "example": "In der Theorie etwa alle vier Minuten ein Muster, aber ihr Rüsten war zu langsam für "
                   "dieses Tempo.",
        "example_cue": "In der Theorie ist das",
        "script": "Fügen wir es an Kavyas gemeinsamer Linie zusammen. Der Mix ist drei zu zwei zu eins. Der "
                  "Durchschnitts-TAKT ist vier Komma zwei Sekunden. Sie testet ein Muster aus sechzig "
                  "Einheiten. Dreißig Handys, zwanzig Boxen und zehn Audiogeräte. In der Theorie ist das "
                  "etwa alle vier Minuten ein Muster. Aber zuerst prüft sie Arbeitsfolge, gemeinsame "
                  "Werkzeuge und die Testgrenzen jedes Produkts. Ihr Rüsten war zu langsam für dieses "
                  "Tempo. Also? Sie beschleunigte die Umrüstungen, statt unsichere Abkürzungen zu "
                  "erzwingen. Und Sie?",
    },
    {
        "key": "p14", "num": 14, "title": "Häufige Fehler",
        "points": [("Glätten auf Bruttozeit", "Glätten auf Bruttozeit"),
                   ("Gleiche Mengen bei ungleichem Mix", "Gleiche Mengen erzwingen"),
                   ("Mehr Leistung, als die Linie schafft", "Mehr gute Leistung planen"),
                   ("Erstteilprüfung auslassen, um aufzuholen", "lassen Sie nie die Erstteilprüfung")],
        "example": "Firmware-Tester standen, während die Tafel Boxen verlangte: mehr WIP verschiebt nur den "
                   "Engpass. Eskalieren.",
        "example_cue": "Eines Tages verlangte Kavyas Tafel",
        "script": "Ein Plan kann auf Papier glatt aussehen, während die Fertigung chaotisch bleibt. Achten "
                  "Sie auf diese Fehler. Glätten auf Bruttozeit, ohne Pausen und Verluste. Gleiche Mengen "
                  "erzwingen, obwohl der Mix Ihres Kunden nicht gleich ist. Mehr gute Leistung planen, als "
                  "Ihre Linie wirklich schafft. Eines Tages verlangte Kavyas Tafel Set-Top-Boxen, aber die "
                  "Firmware-Tester standen. Mehr Arbeit freizugeben hätte nur den Engpass verschoben. Also "
                  "eskalierte sie und passte den Plan an. Und lassen Sie nie die Erstteilprüfung aus, um "
                  "aufzuholen.",
    },
    {
        "key": "p15", "num": 15, "title": "Fahrplan für 90 Tage",
        "points": [("Eine Familie, ein Horizont", "Beginnen Sie klein"),
                   ("Tag 1–30: Bedarf, Mix, TAKT, Rüsten", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: Pilottafel, Kommissionierung, Umrüstungen", "In den nächsten dreißig"),
                   ("Tag 61–90: bestätigen, standardisieren, ausweiten", "In den letzten dreißig")],
        "example": "Planung gibt frei, Produktion baut, Technik prüft Kapazität, Qualität schützt "
                   "Kontrollen, Materialwirtschaft hält Kits bereit.",
        "example_cue": "Die Planung gibt frei",
        "script": "Beginnen Sie klein, mit einer Produktfamilie und einem Planungshorizont. In den ersten "
                  "dreißig Tagen erfassen Sie Bedarf, Mix, TAKT, Engpässe und Rüstzeiten. In den nächsten "
                  "dreißig pilotieren Sie Glättungstafel, Kommissionierrhythmus und schnellere Umrüstungen. "
                  "In den letzten dreißig bestätigen Sie Ausbeute, Plantreue und Lieferung. Dann "
                  "standardisieren Sie und weiten aus. Geben Sie jedem eine klare Rolle. Die Planung gibt "
                  "frei, die Produktion baut, und die Technik prüft Kapazität. Die Qualität schützt "
                  "Kontrollen, die Materialwirtschaft hält Kits bereit. Wer leitet Ihren Pilot?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "versus", "items": [
        {"label": "Erst alle Handys", "sub": "Dann Boxen, dann Audio", "icon": "stack", "with": 1},
        {"label": "Kleine, wiederholte Folgen", "sub": "Passend zum echten Bedarf", "icon": "sequence", "with": "example"}]},
    "p02": {"type": "icons", "items": [
        {"label": "Der Bedarf ist ungleich", "icon": "wave"}, {"label": "Spitzen jagen", "sub": "Überstunden, Bestand", "icon": "clock", "tone": "bad"},
        {"label": "Freigaben glätten", "icon": "sequence"}, {"label": "Etwas Puffer", "icon": "box"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Alles am Montag bauen", "sub": "Überstunden, gehetzter Test", "icon": "stack"},
            {"label": "Über die Woche verteilen", "sub": "Der Termin erlaubte es", "icon": "calendar"}]}},
    "p03": {"type": "flow", "items": [
        {"label": "Mura", "sub": "Ungleiche Freigaben schaffen Spitzen", "icon": "wave", "tone": "bad", "with": 0},
        {"label": "Muri", "sub": "Spitzen überlasten Menschen, Maschinen", "icon": "weight", "tone": "bad", "with": 1},
        {"label": "Muda", "sub": "Fehler, Warten, Bestand", "icon": "trash", "tone": "bad", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "Am Test staut es sich", "unit": "Einheiten an einem Tag", "with": "example", "items": [
            {"label": "Tester schafft", "value": 2000, "tone": "good", "with": "example"},
            {"label": "Freigegeben", "value": 3200, "tone": "bad", "with": "example"}]}},
    "p04": {"type": "icons", "items": [
        {"label": "Ein sinnvoller Horizont", "icon": "calendar"}, {"label": "Nettobedarf", "icon": "count"},
        {"label": "÷ Produktionstage", "icon": "sequence"}, {"label": "Prüfen, ob es hält", "icon": "search"}],
        "then": {"type": "stat", "value": 6000, "icon": "chartUp", "label": "gute Einheiten am Tag, jeden Tag",
                 "unit": "30.000 Einheiten Nettobedarf ÷ 5 Tage", "with": "example"}},
    "p05": {"type": "steps", "items": [
        {"label": "Handy", "sub": "P", "with": "example"}, {"label": "Box", "sub": "B", "with": "example"},
        {"label": "Handy", "sub": "P", "with": "example"}, {"label": "Audio", "sub": "A", "with": "example"},
        {"label": "Box", "sub": "B", "with": "example"}, {"label": "Handy", "sub": "P", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Das Tempo des Kunden", "icon": "clock", "with": 0},
        {"label": "Nettozeit ÷ gute Einheiten", "icon": "count", "with": 1},
        {"label": "Pitch", "sub": "Zeit für die Freigabe einer Charge", "icon": "box", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Eine Einheit alle 4,2 s", "icon": "clock", "with": "example"},
            {"label": "× eine Charge von 100", "icon": "box", "with": "example"},
            {"label": "= ein Pitch von 7 Minuten", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "doc", "items": [
        {"label": "Glättungstafel · gemeinsame Linie", "icon": "calendar", "with": 0},
        {"label": "08:00  Handy · Box · Handy", "icon": "sequence", "with": 1},
        {"label": "08:30  Audio · Box · Handy", "icon": "sequence", "with": 1},
        {"label": "09:00  Nächstes Los: Kits bereit", "icon": "box", "with": 2},
        {"label": "Fenster verpasst? Sofort sichtbar", "icon": "warning", "with": 3}]},
    "p08": {"type": "icons", "items": [
        {"label": "Mehr Umrüstungen", "icon": "sequence", "with": 0},
        {"label": "EPEI", "sub": "Jedes Teil in jedem Intervall", "icon": "calendar", "with": 1},
        {"label": "SMED", "sub": "Rüsten außerhalb der Stillstandszeit", "icon": "wrench", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Vorher", "value": 20}, "after": {"label": "Nach SMED", "value": 8},
                 "suffix": " Min.", "unit": "pro Umrüstung, sechs am Tag", "note": "72 Minuten zurück, jeden Tag", "with": "example"}},
    "p09": {"type": "bars", "label": "Ein Tester", "value": 300, "note": "zu wenig schon vor Verlusten: zweiten Tester ergänzen", "unit": "Tests pro Stunde (40 % der Einheiten brauchen einen 12-s-Test)", "items": [
        {"label": "Benötigte Tests", "value": 343, "tone": "bad", "with": "example"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Kanban-Signale", "icon": "label"}, {"label": "FIFO-Bahnen", "icon": "sequence"},
        {"label": "WIP-Grenzen", "icon": "stack"}, {"label": "Kommissionierung im Pitch", "icon": "tray"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Ein eingefrorenes Fenster", "icon": "lock", "with": 0},
        {"label": "Umplanen in der Fertigung", "sub": "Schafft Chaos", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Wer freigibt", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "500 Audio früher gewünscht", "icon": "box", "with": "example"},
            {"label": "Termine, Bestand, Teile, Test prüfen", "icon": "search", "with": "example"},
            {"label": "Dann die nächsten Fenster ändern", "icon": "sequence", "tone": "good", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Leistung + Stabilität", "icon": "chartUp"}, {"label": "Plantreue", "icon": "check"},
        {"label": "WIP-Tage", "icon": "clock"}, {"label": "FPY, Stillstand, Überstunden", "icon": "shield"}],
        "then": {"type": "stat", "value": 95, "suffix": "%", "icon": "check", "label": "der geplanten Einheiten erledigt",
                 "unit": "12.000 Einheiten WIP = 2 Tage Leistung", "with": "example"}},
    "p13": {"type": "stat", "value": 4.2, "decimals": 1, "suffix": " s", "icon": "clock", "label": "Durchschnitts-TAKT, Mix 3 : 2 : 1",
            "unit": "Handys : Set-Top-Boxen : Audio", "with": 0,
            "then": {"type": "bars", "label": "", "note": "Etwa alle 4 Minuten ein Muster", "unit": "Einheiten in einem Muster aus 60", "with": 1, "items": [
                {"label": "Handys", "value": 30, "with": 1}, {"label": "Boxen", "value": 20, "with": 1},
                {"label": "Audio", "value": 10, "with": 1}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Bruttozeit", "icon": "clock", "tone": "bad"}, {"label": "Gleiche Mengen", "icon": "scale", "tone": "bad"},
        {"label": "Überplanung", "icon": "stack", "tone": "bad"}, {"label": "Erstteilprüfung auslassen", "icon": "warning", "tone": "bad"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Bedarf, Mix, TAKT, Rüsten", "sub": "Tag 1–30", "icon": "clipboard", "with": 1},
        {"label": "Pilottafel, Kommissionierung, Umrüstungen", "sub": "31–60", "icon": "calendar", "with": 2},
        {"label": "Bestätigen, standardisieren, ausweiten", "sub": "61–90", "icon": "chartUp", "with": 3}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Planung", "icon": "calendar", "with": "example"}, {"label": "Produktion", "icon": "wrench", "with": "example"},
            {"label": "Technik", "icon": "gear", "with": "example"}, {"label": "Qualität", "icon": "shield", "with": "example"},
            {"label": "Material", "icon": "box", "with": "example"}]}},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p06",
        "question": "Kavya braucht 3.000 Handys, 2.000 Boxen und 1.000 Audiogeräte. Welche Folge ist "
                    "mix-geglättet?",
        "options": ["Alle Handys, dann alle Boxen, dann alle Audio", "Handy–Box–Handy–Audio–Box–Handy, wiederholt",
                    "Je eins von jedem Produkt, abwechselnd"],
        "correct": 1,
        "explanation": "Das wiederholte Muster folgt dem Bedarfsverhältnis 3 : 2 : 1. Große Chargen schaffen "
                       "Spitzen; gleiche Mengen ignorieren den echten Mix.",
        "q_script": "Kurzer Check. Kavya braucht dreitausend Handys, zweitausend Boxen und tausend "
                    "Audiogeräte. Welche Folge ist mix-geglättet? Nehmen Sie sich kurz Zeit.",
        "a_script": "Das wiederholte Muster. Handy, Box, Handy, Audio, Box, Handy. Es folgt dem "
                    "Bedarfsverhältnis. Gleiche Mengen würden den echten Mix ignorieren.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Ein Kunde will plötzlich 500 Audiogeräte früher. Was sollte Kavya ZUERST tun?",
        "options": ["Sie ins nächste Fenster schieben", "Termine, Bestand, Teile und Testkapazität prüfen, dann die Fenster ändern",
                    "Ablehnen, der Plan ist eingefroren", "Überstunden machen und heute alle bauen"],
        "correct": 1,
        "explanation": "Zuerst die Wirkung prüfen, dann die nächsten Freigabefenster nach den vereinbarten "
                       "Regeln ändern. Blind vordrängeln oder glatt ablehnen bringt beides Ärger.",
        "q_script": "Noch eine, ein Szenario. Ein Kunde will plötzlich fünfhundert Audiogeräte früher. Was "
                    "sollte Kavya zuerst tun? Überlegen Sie kurz.",
        "a_script": "Prüfen Sie zuerst die Wirkung. Termine, Fertigware, Bauteile und Testkapazität. Dann "
                    "ändern Sie die nächsten Fenster nach den vereinbarten Regeln. Blind vordrängeln oder "
                    "glatt ablehnen bringt beides Ärger.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
