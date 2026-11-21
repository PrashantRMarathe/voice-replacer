"""muda_mura_muri in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh muda_mura_muri_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "mm_de"
NAME = "muda_mura_muri_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Next Inspection": "Next Inspektschen",
    "Poka Yoke": "Poka Joke",
    "TIMWOODS": "Tim Wuds",
    "Heijunka": "Hejdschunka",
    "Gemba": "Gemba",
    "CCTV": "ze ze te fau",
    "SMED": "Smed",
    "TAKT": "Takt",
    "Muda": "Muda",
    "Mura": "Mura",
    "Muri": "Muri",
    "TPM": "te pe emm",
    "WIP": "we i pe",
    "3M": "drei emm",
    "5S": "fünf ess",
    "M": "emm",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Achtzehn Uhr. Die Schicht endet in einer Stunde, und Sanjays Linie liegt vierzig Kameras "
    "zurück. Alle hetzen. Am Test häufen sich Fehler. Morgen passiert es wieder. Kommt Ihnen "
    "das bekannt vor? In dieser Lektion lernen Sie die 3M des Lean kennen: Muda, Mura und "
    "Muri. Sie sehen, wie Verschwendung, Unausgeglichenheit und Überlastung einander nähren. "
    "Wir begleiten Sanjay, Linienleiter an einer Linie für CCTV-Kameras, der diesen Kreislauf "
    "durchbricht."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Muda ist Verschwendung, Mura Unausgeglichenheit, und Muri "
    "Überlastung. Sie nähren einander, also verbessern Sie sie gemeinsam. Und das Ziel ist "
    "ein stabiler Fluss, nicht schnelleres Arbeiten. Ihre Aufgabe für diese Woche. Begleiten "
    "Sie ein Produkt durch Ihre Linie, und markieren Sie ein Beispiel für jedes M. Gut "
    "gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie Next Inspection kennen, den "
    "Schutz des nachfolgenden Prozesses."
)

# One story thread: Sanjay's CCTV camera assembly line. Big work-order releases,
# WIP waves before test, walking for parts, end-of-shift rush and overtime.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Die 3M kennenlernen",
        "points": [("Muda: Verschwendung, kein Wert für den Kunden", "Muda ist Verschwendung"),
                   ("Mura: Unausgeglichenheit, die Last schwankt", "Mura ist Unausgeglichenheit"),
                   ("Muri: Überlastung, über die sichere Kapazität", "Muri ist Überlastung")],
        "example": "Sanjays Linie, in einer Stunde: Werker warten auf Kits (Muda), die Leistung schwankt "
                   "(Mura), dann hetzen alle (Muri).",
        "example_cue": "An Sanjays Linie",
        "script": "Hier ist die Kernidee. Lean sucht drei Feinde eines guten Flusses. Muda ist "
                  "Verschwendung, Arbeit ohne Wert für Ihren Kunden. Mura ist Unausgeglichenheit, eine "
                  "Last, die auf und ab schwankt. Muri ist Überlastung, also mehr von Menschen oder "
                  "Maschinen verlangen, als sie sicher leisten. An Sanjays Linie sehen Sie alle drei in "
                  "einer Stunde. Werker warten auf Kits, die Leistung schwankt, dann hetzen alle. Welches "
                  "greifen Sie zuerst an?",
    },
    {
        "key": "p02", "num": 2, "title": "Wie die 3M zusammenhängen",
        "points": [("Nicht eines nach dem anderen lösbar", "Sie können sie nicht"),
                   ("Mura erzeugt Muri, Muri erzeugt Muda", "Mura erzeugt oft Muri"),
                   ("Nur die Verschwendung jagen, und sie kehrt zurück", "Wenn Sie nur")],
        "example": "Riesige Charge am Montag (Mura) → Werker und Tester gehetzt (Muri) → Fehler, Nacharbeit, "
                   "Überstunden (Muda).",
        "example_cue": "Sanjays Planer gab",
        "script": "Hier ist die Überraschung. Sie können sie nicht einzeln lösen. Mura erzeugt oft Muri, "
                  "und Muri erzeugt Muda. Sanjays Planer gab am Montagmorgen eine riesige Charge frei. Das "
                  "ist Mura. Um aufzuholen, hetzten die Werker, und der Tester ruhte nie. Das ist Muri. "
                  "Dann kamen Fehler, Nacharbeit und Überstunden. Das ist Muda. Wenn Sie nur die "
                  "Verschwendung jagen, kehrt sie zurück. Schauen wir uns jedes an, zuerst die "
                  "Verschwendung.",
    },
    {
        "key": "p03", "num": 3, "title": "Muda: der Werttest",
        "points": [("Verändert es das Produkt, wie der Kunde es braucht?", "Verändert dieser Schritt"),
                   ("Wird es beim ersten Mal richtig gemacht?", "Wird es beim ersten Mal"),
                   ("Würde der Kunde dafür zahlen?", "Würde der Kunde"),
                   ("Wenn nicht: hinterfragen", "Wenn die Antwort nein ist")],
        "example": "Die Linse einsetzen schafft Wert. Etiketten holen, auf ein Kit warten und zweimal testen "
                   "nicht.",
        "example_cue": "An Sanjays Linie schafft",
        "script": "Wie erkennen Sie Verschwendung? Mit einem einfachen Werttest. Verändert dieser Schritt "
                  "das Produkt so, wie Ihr Kunde es braucht? Wird es beim ersten Mal richtig gemacht? Würde "
                  "der Kunde gern dafür zahlen? Wenn die Antwort nein ist, hinterfragen Sie ihn. An Sanjays "
                  "Linie schafft das Einsetzen der Linse Wert. Etiketten holen nicht. Auf ein Kit warten "
                  "oder eine Kamera zweimal testen auch nicht. Aber können Sie jeden solchen Schritt "
                  "streichen?",
    },
    {
        "key": "p04", "num": 4, "title": "Notwendig oder reine Verschwendung",
        "points": [("Typ 1: heute nötig, vereinfachen", "Manche Schritte schaffen keinen Wert"),
                   ("Typ 2: reine Verschwendung, entfernen", "Typ zwei ist reine Verschwendung"),
                   ("Nie einen Menschen Verschwendung nennen", "Nennen Sie nie einen Menschen")],
        "example": "Typ 1: eine vorgeschriebene Sicherheitsprüfung. Typ 2: dieselbe Seriennummer in zwei "
                   "Systeme tippen.",
        "example_cue": "Eine vorgeschriebene Sicherheitsprüfung",
        "script": "Nicht immer. Manche Schritte schaffen keinen Wert, aber Sie brauchen sie heute noch. "
                  "Eine vorgeschriebene Sicherheitsprüfung ist so einer. Das ist Verschwendung vom Typ "
                  "eins. Vereinfachen Sie sie, oder gestalten Sie um. Typ zwei ist reine Verschwendung, "
                  "etwa dieselbe Seriennummer in zwei Systeme tippen. Entfernen Sie sie. Und eine feste "
                  "Regel. Nennen Sie nie einen Menschen Verschwendung. Verschwendung steckt im Prozess. Wie "
                  "sieht sie aus?",
    },
    {
        "key": "p05", "num": 5, "title": "Die 8 Verschwendungen: TIMWOODS",
        "points": [("Transport · Bestand · Bewegung · Warten", "Transport, Bestand"),
                   ("Überproduktion · Überbearbeitung", "Überproduktion und Überbearbeitung"),
                   ("Fehler · ungenutzte Fähigkeiten", "Fehler, und ungenutzte Fähigkeiten"),
                   ("Verschwendungsrundgang: einem Produkt folgen", "Sanjay machte einen Verschwendungsrundgang")],
        "example": "Sanjays Rundgang: 3 Kit-Wartezeiten in 2 Stunden, weite Wege für Etiketten, eine Wand "
                   "aus WIP vor dem Test.",
        "example_cue": "Dreimal Warten auf Kits",
        "script": "Merken Sie sich die acht Verschwendungen mit einem Wort, TIMWOODS. Transport, Bestand, "
                  "Bewegung und Warten. Überproduktion und Überbearbeitung. Fehler, und ungenutzte "
                  "Fähigkeiten. Sanjay machte einen Verschwendungsrundgang. Er folgte einer Kamera vom "
                  "Kommissionieren bis zum Verpacken. Dreimal Warten auf Kits in zwei Stunden. Weite Wege "
                  "für Etiketten. Und eine Wand aus WIP vor dem Test. Welche der acht fänden Sie zuerst?",
    },
    {
        "key": "p06", "num": 6, "title": "Mura: Unausgeglichenheit",
        "points": [("Große Chargen, dann nichts", "Große Chargen kommen"),
                   ("Material kommt stoßweise", "Material kommt stoßweise"),
                   ("Gleiche Arbeit, andere Methoden", "Zwei Werker machen"),
                   ("Durchschnitte verbergen Spitzen und Täler", "Der Durchschnitt sieht gut aus")],
        "example": "Sanjays Stundentafel: 60, dann 105, dann 70. Der Durchschnitt sieht gut aus, die Linie "
                   "nicht.",
        "example_cue": "Schauen Sie auf Sanjays Stundentafel",
        "script": "Nun zu Mura. Es ist Unausgeglichenheit in Nachfrage, Arbeitslast oder Fluss. Große "
                  "Chargen kommen, dann nichts. Material kommt stoßweise. Zwei Werker machen dieselbe "
                  "Arbeit verschieden. Schauen Sie auf Sanjays Stundentafel. Sechzig, dann hundertfünf, "
                  "dann siebzig. Der Durchschnitt sieht gut aus. Aber Ihre Linie lebt nicht im "
                  "Durchschnitt, sondern in Spitzen und Tälern. Und Spitzen setzen jemanden unter Druck. "
                  "Wer zahlt?",
    },
    {
        "key": "p07", "num": 7, "title": "Muri: Überlastung",
        "points": [("Menschen: Heben, Strecken, Alarme, zu wenig Schulung", "Für Menschen ist es"),
                   ("Maschinen: über Nennlast, ausgelassene Wartung", "Für Maschinen ist es"),
                   ("Führt zu Ermüdung, Fehlern, Ausfällen", "Muri führt zu Ermüdung")],
        "example": "Eine Werkerin greift 120 Mal pro Stunde über Schulterhöhe; der Tester läuft durch jede "
                   "Pause.",
        "example_cue": "Eine von Sanjays Werkerinnen",
        "script": "Menschen und Maschinen zahlen. Das ist Muri, Überlastung. Für Menschen ist es schweres "
                  "Heben, unbequemes Strecken, zu viele Alarme oder zu wenig Schulung. Für Maschinen ist es "
                  "Betrieb über Nennlast, und ausgelassene Wartung für die Leistung. Eine von Sanjays "
                  "Werkerinnen greift hundertzwanzig Mal pro Stunde über die Schulter. Und der Tester läuft "
                  "durch jede Pause. Muri führt zu Ermüdung, Fehlern und Ausfällen. Wie wirken die drei "
                  "zusammen?",
    },
    {
        "key": "p08", "num": 8, "title": "Wenn alle drei zusammenstoßen",
        "points": [("4 Stunden Bedarf in einer Freigabe", "Vier Stunden Bedarf"),
                   ("Stationen arbeiten vor, WIP stapelt sich", "Die ersten Stationen arbeiteten vor"),
                   ("Der Test wurde zum Engpass", "Der Test wurde zum Engpass"),
                   ("Überstunden, Hetze, Fehler, Nacharbeit", "Die Leiter holten")],
        "example": "Sah aus wie „zu wenig Testkapazität\". In Wahrheit: ungleiche Freigabe (Mura) + Hetze "
                   "(Muri) + Nacharbeit (Muda).",
        "example_cue": "Es sah nach einem Problem",
        "script": "Das geschah am Montag. Vier Stunden Bedarf kamen in einer Freigabe. Die ersten Stationen "
                  "arbeiteten vor, und WIP stapelte sich. Der Test wurde zum Engpass. Die Leiter holten "
                  "Leute und machten Überstunden. Werker hetzten, Fehler stiegen, und Nacharbeit belastete "
                  "den Test noch mehr. Es sah nach einem Problem der Testkapazität aus. Aber in dieser "
                  "Geschichte stecken alle drei M. Wie finden Sie sie an Ihrer Linie?",
    },
    {
        "key": "p09", "num": 9, "title": "Die 3M am Gemba finden",
        "points": [("Beobachten, bevor Sie etwas ändern", "beobachten Sie, bevor"),
                   ("Zeiten, Warten, Wege, WIP, Nacharbeit erfassen", "Erfassen Sie Zykluszeiten"),
                   ("Werker fragen, was schwer ist", "Dann fragen Sie die Werker"),
                   ("Daten prüfen, bevor Sie eine Lösung wählen", "Dann prüfen Sie die Daten")],
        "example": "Sanjay markierte jeden Befund als Muda, Mura oder Muri. 20 Minuten Warten auf ein Kit "
                   "bekamen zwei: Verschwendung und Unausgeglichenheit.",
        "example_cue": "Sanjay markierte jeden Befund",
        "script": "Gehen Sie zum Gemba, und beobachten Sie, bevor Sie etwas ändern. Folgen Sie einer "
                  "Produktfamilie. Erfassen Sie Zykluszeiten, Warten, Wege, WIP und Nacharbeit. Dann fragen "
                  "Sie die Werker, was die Arbeit schwer oder unsicher macht. Sanjay markierte jeden Befund "
                  "als Muda, Mura oder Muri. Warten auf ein Kit ist oft beides, Verschwendung und "
                  "Unausgeglichenheit. Dann prüfen Sie die Daten, bevor Sie eine Lösung wählen.",
    },
    {
        "key": "p10", "num": 10, "title": "Werkzeuge gegen Muda",
        "points": [("5S: weniger Suchen und Gehen", "5S verringert"),
                   ("Standardarbeit: die beste, sicherste Methode", "Standardarbeit legt"),
                   ("Poka Yoke: Fehler an der Quelle stoppen", "Poka Yoke stoppt Fehler"),
                   ("SMED und TPM: Rüsten, Zuverlässigkeit", "SMED verkürzt"),
                   ("Ursachenanalyse: keine Wiederholfehler", "Die Ursachenanalyse stoppt"),
                   ("Keine Verschwendung automatisieren", "Automatisieren Sie keine Verschwendung")],
        "example": "Etiketten und Schrauben in Regale an jeder Station: der Weg sank von 40 m auf 8 m.",
        "example_cue": "Sanjay legte Etiketten",
        "script": "Beginnen wir, Verschwendung zu beseitigen. 5S verringert Suchen und Gehen. "
                  "Standardarbeit legt die beste, sicherste Methode fest. Poka Yoke stoppt Fehler an der "
                  "Quelle. SMED verkürzt das Rüsten, und TPM hält Maschinen zuverlässig. Die "
                  "Ursachenanalyse stoppt Wiederholfehler. Sanjay legte Etiketten und Schrauben in Regale "
                  "an jeder Station. Der Weg sank von vierzig auf acht Meter. Eine Warnung. Automatisieren "
                  "Sie keine Verschwendung. Sie wird nur schneller.",
    },
    {
        "key": "p11", "num": 11, "title": "Werkzeuge gegen Mura",
        "points": [("Heijunka: Menge und Mix glätten", "Heijunka glättet"),
                   ("TAKT verbindet Ihr Tempo mit dem Bedarf", "Die TAKT Zeit verbindet"),
                   ("Freigabe in jedem Pitch, nicht in Wellen", "Also gibt er jetzt"),
                   ("Pull und First-in-first-out-Bahnen", "Pull-Signale")],
        "example": "TAKT = 27.000 s ÷ 450 Kameras = eine Kamera alle 60 Sekunden.",
        "example_cue": "Sanjays Schicht hat",
        "script": "Als Nächstes glätten Sie den Fluss. Heijunka glättet Menge und Mix. Die TAKT Zeit "
                  "verbindet Ihr Tempo mit dem Kundenbedarf. Sanjays Schicht hat siebenundzwanzigtausend "
                  "Sekunden Arbeitszeit. Der Kunde braucht vierhundertfünfzig Kameras. Das ist eine Kamera "
                  "alle sechzig Sekunden. Also gibt er jetzt in jedem Pitch Arbeit frei, nicht in Wellen. "
                  "Pull-Signale und First-in-first-out-Bahnen halten es stabil. TAKT ist ein Rhythmus, "
                  "keine Peitsche. Wie schützen Sie Ihre Leute?",
    },
    {
        "key": "p12", "num": 12, "title": "Werkzeuge gegen Muri",
        "points": [("Jede Station auf TAKT abstimmen", "Stimmen Sie jede Station"),
                   ("Greifen und Heben im sicheren Bereich", "Halten Sie Greifen"),
                   ("Vorrichtungen, wo Hände Teile halten", "Ergänzen Sie Vorrichtungen"),
                   ("Maschinengrenzen und Wartung achten", "Achten Sie die Grenzen")],
        "example": "Eine Vorrichtung hält jetzt die Kamera beim Schrauben; der hohe Behälter kam in leichte "
                   "Reichweite.",
        "example_cue": "Sanjay ergänzte eine Vorrichtung",
        "script": "Gestalten Sie die Arbeit passend für Menschen und Maschinen. Stimmen Sie jede Station "
                  "auf TAKT ab, mit echten Zykluszeiten. Halten Sie Greifen und Heben im sicheren Bereich. "
                  "Ergänzen Sie Vorrichtungen, wo Hände Teile halten. Achten Sie die Grenzen der Maschinen, "
                  "und lassen Sie nie Wartung aus. Sanjay ergänzte eine Vorrichtung, die die Kamera beim "
                  "Schrauben hält. Der hohe Behälter kam nach unten. Planen Sie nie hundert Prozent "
                  "Auslastung. Wie fügen Sie alles zusammen?",
    },
    {
        "key": "p13", "num": 13, "title": "Eine 3M-Methode in 8 Schritten",
        "points": [("Definieren, dann am Gemba beobachten", "Definieren Sie das Problem"),
                   ("In die drei M einordnen", "Ordnen Sie das Gesehene"),
                   ("Ausgangswert messen, Ursachen finden", "Messen Sie einen Ausgangswert"),
                   ("Kleine Änderungen mit PDCA testen", "Testen Sie kleine Änderungen"),
                   ("Standardisieren, weiter auditieren", "Wenn eine Änderung wirkt")],
        "example": "Sanjays Ausgangswert: stark schwankende Stundenleistung, 2,5 Stunden Überstunden pro "
                   "Tag.",
        "example_cue": "Sanjays Ausgangswert war klar",
        "script": "Nutzen Sie eine einfache Methode in acht Schritten. Definieren Sie das Problem, dann "
                  "beobachten Sie am Gemba. Ordnen Sie das Gesehene in die drei M ein. Messen Sie einen "
                  "Ausgangswert, dann finden Sie die Ursachen. Testen Sie kleine Änderungen mit Plan, Do, "
                  "Check, Act. Wenn eine Änderung wirkt, machen Sie sie zum Standard, und auditieren Sie "
                  "weiter. Sanjays Ausgangswert war klar. Die Leistung schwankte stark, mit zweieinhalb "
                  "Stunden Überstunden am Tag. Nun die Ergebnisse.",
    },
    {
        "key": "p14", "num": 14, "title": "Fallstudie: CCTV-Linie",
        "points": [("Kleinere, stetige Freigaben + First-in-first-out-Bahn", "Kleinere, stetige Freigaben"),
                   ("Teile und Etiketten am Verwendungsort", "Teile und Etiketten"),
                   ("Freigabe passend zur Testkapazität", "Arbeit, passend zur Testkapazität"),
                   ("Stundentafel, Probleme früh gemeldet", "Und eine Stundentafel")],
        "example": "Nach 6 Wochen: Stundenschwankung fast weg, Überstunden nahe null, Erstdurchlaufquote auf "
                   "98 %.",
        "example_cue": "Nach sechs Wochen",
        "script": "Das hat Sanjay geändert. Kleinere, stetige Freigaben, mit einer First-in-first-out-Bahn "
                  "vor dem Test. Teile und Etiketten am Verwendungsort. Arbeit, passend zur Testkapazität "
                  "freigegeben. Und eine Stundentafel, damit Probleme früh gemeldet werden, nicht um "
                  "achtzehn Uhr. Nach sechs Wochen war die Stundenschwankung fast verschwunden. Überstunden "
                  "nahe null. Die Erstdurchlaufquote stieg auf achtundneunzig Prozent. Niemand musste "
                  "schneller arbeiten. Wie beweisen Sie, dass es hält?",
    },
    {
        "key": "p15", "num": 15, "title": "KPI und Nachhaltigkeit",
        "points": [("Fluss: Durchlaufzeit, WIP", "Für den Fluss"),
                   ("Mura: Spanne der Stundenleistung", "Für Mura"),
                   ("Qualität: FPY, Nacharbeit", "Für die Qualität"),
                   ("Muri: Überstunden, ergonomisches Risiko", "Für Muri")],
        "example": "Mehr Einheiten pro Stunde, aber weniger Qualität und mehr Überstunden? Dann haben Sie "
                   "den Verlust nur verschoben.",
        "example_cue": "Wenn die Einheiten",
        "script": "Messen Sie alle drei M, nicht nur die Leistung. Für den Fluss, Durchlaufzeit und WIP. "
                  "Für Mura, die Spanne der Stundenleistung, nicht nur den Durchschnitt. Für die Qualität, "
                  "Erstdurchlaufquote und Nacharbeit. Für Muri, Überstunden und ergonomische Risiken. Und "
                  "jagen Sie nie nur eine Zahl. Wenn die Einheiten pro Stunde steigen, aber Qualität fällt "
                  "und Überstunden steigen, ist der Verlust nur verschoben. Prüfen Sie es jede Woche am "
                  "Gemba.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Muda", "sub": "Verschwendung: Warten auf Kits", "icon": "trash", "tone": "bad"},
        {"label": "Mura", "sub": "Unausgeglichenheit: Leistung schwankt", "icon": "wave", "tone": "bad"},
        {"label": "Muri", "sub": "Überlastung: alle hetzen", "icon": "weight", "tone": "bad"}]},
    "p02": {"type": "flow", "items": [
        {"label": "Mura", "sub": "Eine riesige Montagscharge", "icon": "wave", "tone": "bad", "with": 1},
        {"label": "Muri", "sub": "Hetze; der Tester ruht nie", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Muda", "sub": "Fehler, Nacharbeit, Überstunden", "icon": "trash", "tone": "bad", "with": "example"}]},
    "p03": {"type": "versus", "items": [
        {"label": "Wege für Etiketten", "sub": "Kein Wert (auch Warten, Doppeltest nicht)", "icon": "walk", "with": "example"},
        {"label": "Linse einsetzen", "sub": "Schafft Wert", "icon": "camera", "with": "example"}]},
    "p04": {"type": "icons", "items": [
        {"label": "Typ 1: vereinfachen", "sub": "Eine vorgeschriebene Sicherheitsprüfung", "icon": "shield"},
        {"label": "Typ 2: entfernen", "sub": "Eine Seriennummer doppelt getippt", "icon": "cross", "tone": "bad"},
        {"label": "Menschen sind nie Verschwendung", "sub": "Verschwendung steckt im Prozess", "icon": "person", "tone": "good"}]},
    "p05": {"type": "steps", "items": [
        {"label": "Transport", "sub": "T", "with": 0}, {"label": "Bestand", "sub": "I", "with": 0},
        {"label": "Bewegung", "sub": "M", "with": 0}, {"label": "Warten", "sub": "W", "with": 0},
        {"label": "Überproduktion", "sub": "O", "with": 1}, {"label": "Überbearbeitung", "sub": "O", "with": 1},
        {"label": "Fehler", "sub": "D", "with": 2}, {"label": "Ungenutzte Fähigkeiten", "sub": "S", "with": 2}]},
    "p06": {"type": "bars", "label": "Durchschnitt", "note": "sieht gut aus, verbirgt Schwankungen", "unit": "Sanjays Stundentafel: Kameras pro Stunde", "items": [
        {"label": "Stunde 1", "value": 60, "with": "example"},
        {"label": "Stunde 2", "value": 105, "tone": "bad", "with": "example"},
        {"label": "Stunde 3", "value": 70, "with": "example"}]},
    "p07": {"type": "icons", "items": [
        {"label": "Menschen", "sub": "Heben, Strecken, Alarme", "icon": "person", "tone": "bad", "with": 0},
        {"label": "Maschinen", "sub": "Über Nennlast", "icon": "gear", "tone": "bad", "with": 1}],
        "then": {"type": "stat", "value": 120, "icon": "hand", "label": "Griffe über Schulterhöhe",
                 "unit": "pro Stunde, bei einer Werkerin", "with": "example"}},
    "p08": {"type": "flow", "items": [
        {"label": "4 Stunden Bedarf auf einmal", "icon": "wave", "tone": "bad"},
        {"label": "WIP stapelt sich", "icon": "stack", "tone": "bad"},
        {"label": "Test wird zum Engpass", "icon": "test", "tone": "bad"},
        {"label": "Überstunden, Hetze, Nacharbeit", "icon": "clock", "tone": "bad"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Zuerst beobachten", "icon": "search"}, {"label": "Erfassen", "icon": "clipboard"},
        {"label": "Werker fragen", "icon": "person"}, {"label": "Daten prüfen", "icon": "chartUp"}]},
    "p10": {"type": "icons", "items": [
        {"label": "5S", "icon": "tray", "with": 0}, {"label": "Standardarbeit", "icon": "clipboard", "with": 1},
        {"label": "Poka Yoke", "icon": "key", "with": 2}, {"label": "SMED + TPM", "icon": "wrench", "with": 3},
        {"label": "Grundursache", "icon": "search", "with": 4}],
        "then": {"type": "compare", "before": {"label": "Vorher", "value": 40}, "after": {"label": "Nachher", "value": 8},
                 "suffix": " m", "unit": "Weg pro Kamera", "note": "80 % weniger Gehen", "with": "example"}},
    "p11": {"type": "icons", "items": [
        {"label": "Heijunka", "sub": "Menge und Mix glätten", "icon": "sequence", "with": 0},
        {"label": "TAKT", "sub": "Tempo nach Bedarf", "icon": "clock", "with": 1}],
        "then": {"type": "stat", "value": 60, "suffix": " s", "icon": "camera", "label": "eine Kamera alle 60 Sekunden",
                 "unit": "27.000 s Arbeitszeit ÷ 450 Kameras", "with": "example"}},
    "p12": {"type": "icons", "items": [
        {"label": "Auf TAKT abstimmen", "icon": "scale"}, {"label": "Sicherer Greifbereich", "icon": "person"},
        {"label": "Vorrichtungen", "icon": "wrench"}, {"label": "Maschinengrenzen", "icon": "gear"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Hände halten die Kamera", "sub": "Hoher Behälter über der Schulter", "icon": "hand"},
            {"label": "Eine Vorrichtung hält sie", "sub": "Behälter in leichter Reichweite", "icon": "wrench"}]}},
    "p13": {"type": "steps", "items": [
        {"label": "Definieren", "with": 0}, {"label": "Beobachten", "with": 0}, {"label": "3M einordnen", "with": 1},
        {"label": "Messen", "with": 2}, {"label": "Ursachen finden", "with": 2}, {"label": "Testen (PDCA)", "with": 3},
        {"label": "Standardisieren", "with": 4}, {"label": "Auditieren", "with": 4}]},
    "p14": {"type": "flow", "items": [
        {"label": "Kleine, stetige Freigaben", "icon": "sequence", "tone": "good"},
        {"label": "Teile am Verwendungsort", "icon": "tray", "tone": "good"},
        {"label": "Freigabe = Testkapazität", "icon": "test", "tone": "good"},
        {"label": "Stundentafel", "icon": "chartUp", "tone": "good"}],
        "then": {"type": "stat", "value": 98, "suffix": "%", "icon": "check", "label": "Erstdurchlaufquote nach 6 Wochen",
                 "unit": "Überstunden nahe null. Niemand arbeitete schneller.", "with": "example"}},
    "p15": {"type": "icons", "items": [
        {"label": "Fluss", "sub": "Durchlaufzeit, WIP", "icon": "clock"},
        {"label": "Mura", "sub": "Stundenspanne", "icon": "wave"},
        {"label": "Qualität", "sub": "FPY, Nacharbeit", "icon": "check"},
        {"label": "Muri", "sub": "Überstunden, Ergonomie", "icon": "weight"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Die Stundenleistung einer Linie lautet 60, 105, 70, 110. Welches M zeigt das am "
                    "deutlichsten?",
        "options": ["Muda: Verschwendung", "Mura: Unausgeglichenheit", "Muri: Überlastung"],
        "correct": 1,
        "explanation": "Leistung, die von Stunde zu Stunde schwankt, ist Mura: Unausgeglichenheit in Last und "
                       "Fluss. Unbehandelt erzeugt sie meist Muri (Hetze) und dann Muda (Fehler, Überstunden).",
        "q_script": "Kurzer Check. Die Stundenleistung einer Linie schwankt zwischen sechzig und hundertzehn. "
                    "Welches M zeigt das am deutlichsten? Nehmen Sie sich kurz Zeit.",
        "a_script": "Es ist Mura, Unausgeglichenheit. Die Last schwankt von Stunde zu Stunde. Unbehandelt "
                    "erzeugt sie meist Hetze, und dann Verschwendung.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Ein Leiter erfüllt den Tagesplan mit zwei Überstunden pro Tag. Was sollte das Team "
                    "ZUERST tun?",
        "options": ["Die Werker bitten, schneller zu arbeiten", "Mehr Überstunden für einen Puffer",
                    "Den Fluss beobachten und Mura und Muri hinter dem Rückstand finden",
                    "Einen weiteren Tester kaufen"],
        "correct": 2,
        "explanation": "Überstunden verbergen das Problem. Gehen Sie zum Gemba, finden Sie die "
                       "Unausgeglichenheit und Überlastung hinter dem Verlust, dann glätten und neu abstimmen. "
                       "Tempo, Puffer oder neue Maschinen verschieben den Verlust nur.",
        "q_script": "Noch eine, ein Szenario. Ein Leiter erfüllt den Plan jeden Tag mit zwei Überstunden. Was "
                    "sollte das Team zuerst tun? Überlegen Sie kurz.",
        "a_script": "Beobachten Sie zuerst den Fluss. Finden Sie die Unausgeglichenheit und Überlastung "
                    "hinter dem Rückstand, dann glätten und neu abstimmen. Überstunden verbergen das Problem "
                    "nur.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
