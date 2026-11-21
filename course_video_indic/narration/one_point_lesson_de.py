"""one_point_lesson in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh one_point_lesson_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "op_de"
NAME = "one_point_lesson_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "One Point Lesson": "Wann Peunt Lessen",
    "Poka Yoke": "Poka Joke",
    "Kaizen": "Kaisen",
    "Gemba": "Gemba",
    "OPL": "o pe ell",
    "SOP": "ess o pe",
    "PCB": "pe ze be",
    "AOI": "a o i",
    "ESD": "e ess de",
    "TPM": "te pe emm",
    "5S": "fünf ess",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Nachtschicht. Ein neuer Werker steckt einen Stecker falsch herum ein und bricht ihn. Die "
    "Tagschicht kannte den Trick. Niemand hatte ihn geteilt. Kommt Ihnen das bekannt vor? In "
    "dieser Lektion lernen Sie die One Point Lesson kennen. Eine Seite, visuell, um eine "
    "Sache gut zu lehren, direkt am Arbeitsplatz. Wir begleiten Ravi, Schichtleiter an einer "
    "Linie für Videorekorder, bei seinen ersten."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Ein Thema, ein klarer Punkt, und ein starkes Bild. Lehren "
    "Sie sie am Gemba, und bestätigen Sie sie, indem Sie die Arbeit beobachten. Und lenken "
    "Sie sie, damit sie immer zum aktuellen Standard passt. Ihre Aufgabe für diese Woche. "
    "Wählen Sie einen Fehler, der sich wiederholt, und entwerfen Sie eine One Point Lesson "
    "dazu. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie Poka Yoke kennen, die "
    "Fehlervermeidung."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was eine One Point Lesson ist",
        "points": [("Eine Sache, auf einer Seite", "lehrt eine Sache auf einer"),
                   ("Kurz: in Minuten gelernt", "Sie ist kurz"),
                   ("Visuell: gute und schlechte Beispiele", "Sie ist visuell"),
                   ("Am Arbeitsplatz gelehrt", "sie wird direkt am Arbeitsplatz")],
        "example": "Ravis erste OPL, Stecker einsetzen: der richtige Griff, der falsche Griff, und das "
                   "Klicken, auf das man hört.",
        "example_cue": "Ravis erste",
        "script": "Hier ist die Kernidee. Eine One Point Lesson, kurz OPL, lehrt eine Sache auf einer "
                  "Seite. Sie ist kurz, Sie lernen sie in wenigen Minuten. Sie ist visuell, mit Fotos und "
                  "klaren guten und schlechten Beispielen. Und sie wird direkt am Arbeitsplatz gelehrt. "
                  "Ravis erste behandelte das Einsetzen des Steckers. Ein Foto vom richtigen Griff, eines "
                  "vom falschen, und das Klicken, auf das man hört. Was sollte sie nie ersetzen?",
    },
    {
        "key": "p02", "num": 2, "title": "Was eine OPL nicht ist",
        "points": [("Ersetzt nie Ihre SOP", "Eine OPL ersetzt nie Ihre SOP"),
                   ("Kein großes Thema auf eine Seite gequetscht", "Sie quetscht auch"),
                   ("Festigt einen kritischen Punkt", "festigt sie einen kritischen Punkt")],
        "example": "Ravis Steckerlektion hängt neben der SOP und zeigt auf den genauen Schritt, den sie "
                   "stützt.",
        "example_cue": "Ravis Steckerlektion",
        "script": "Eine OPL ersetzt nie Ihre SOP. Sie ist keine Arbeitsanweisung, keine volle Spezifikation "
                  "und keine Zertifizierung. Sie quetscht auch kein großes Thema auf eine volle Seite. "
                  "Stattdessen festigt sie einen kritischen Punkt, damit man ihn behält. Ravis "
                  "Steckerlektion hängt direkt neben der SOP. Sie zeigt auf den genauen Schritt, den sie "
                  "stützt. So bleibt der Standard das Original, und die OPL macht ihn haltbar. Warum lohnt "
                  "sich das?",
    },
    {
        "key": "p03", "num": 3, "title": "Warum sich OPL lohnen",
        "points": [("Schließt Lücken zwischen Schichten", "OPL schließen Lücken"),
                   ("Neue lernen schneller", "Neue lernen schneller"),
                   ("Lehren aus Fehlern schnell geteilt", "Lehren aus Fehlern"),
                   ("Erfahrene Werker werden Trainer", "Ihre erfahrenen Werker")],
        "example": "Nachtschicht brach 14 Stecker pro Woche, Tagschicht 2. Gleiche SOP, anderes Wissen.",
        "example_cue": "Ravis Nachtschicht brach",
        "script": "OPL schließen Lücken zwischen Menschen und Schichten. Ravis Nachtschicht brach vierzehn "
                  "Stecker pro Woche. Die Tagschicht zwei. Gleiche SOP, aber anderes Wissen. Eine One Point "
                  "Lesson verbreitet dieses Wissen in Minuten. Neue lernen schneller. Lehren aus Fehlern "
                  "und Ausfällen werden schnell geteilt. Und Ihre erfahrenen Werker werden Trainer, das "
                  "schafft echte Verantwortung. Der Nutzen zeigt sich bei Qualität, Sicherheit und Kosten. "
                  "Welche Arten gibt es?",
    },
    {
        "key": "p04", "num": 4, "title": "Arten der OPL",
        "points": [("Grundwissen, z. B. Umgang mit ESD", "Eine Grundwissen-Lektion"),
                   ("Problem: Fehler, Ursache und Lösung", "Eine Problem-Lektion"),
                   ("Verbesserung: eine bessere Methode aus Kaizen", "Eine Verbesserungs-Lektion"),
                   ("Sicherheit · Qualität · Instandhaltung", "Dann gibt es Sicherheit")],
        "example": "Ravis Lektion zum gebrochenen Stecker ist vom Typ Problem.",
        "example_cue": "Ravis Lektion zum gebrochenen Stecker",
        "script": "Es gibt sechs gängige Arten. Eine Grundwissen-Lektion lehrt, was jeder wissen muss, wie "
                  "den Umgang mit ESD. Eine Problem-Lektion erklärt einen Fehler, seine Ursache und Lösung. "
                  "Eine Verbesserungs-Lektion teilt eine bessere Methode aus einem Kaizen. Dann gibt es "
                  "Sicherheit, Qualität und Instandhaltung. Ravis Lektion zum gebrochenen Stecker ist vom "
                  "Typ Problem. Die Namen können abweichen, die Regel nicht. Ein klarer Punkt. Wann "
                  "erstellen Sie eine?",
    },
    {
        "key": "p05", "num": 5, "title": "Wann eine erstellen",
        "points": [("Ein Wiederholfehler, gerade gelöst", "Ein Wiederholfehler wurde"),
                   ("Neues Produkt, neue Maschine oder Vorrichtung", "Ein neues Produkt"),
                   ("Ein Schritt wird immer wieder missverstanden", "Ein Schritt der SOP"),
                   ("Ein Beinaheunfall oder der Trick eines Könners", "Ein Beinaheunfall")],
        "example": "Ravis Anlass: die Ursache der gebrochenen Stecker war gefunden. Nun musste die Lösung "
                   "jede Schicht erreichen.",
        "example_cue": "Für Ravi war der Anlass",
        "script": "Erstellen Sie eine, wenn ein kleines Wissen Verhalten ändern kann. Ein Wiederholfehler "
                  "wurde gerade gelöst. Ein neues Produkt, eine Maschine oder Vorrichtung kommt. Ein "
                  "Schritt der SOP wird immer wieder missverstanden. Ein Beinaheunfall zeigt eine Lücke. "
                  "Oder ein Könner kennt einen Trick, den sonst keiner kennt. Für Ravi war der Anlass klar. "
                  "Die Ursache der gebrochenen Stecker war gefunden. Nun musste die Lösung jede Schicht "
                  "erreichen. Was kommt auf die Seite?",
    },
    {
        "key": "p06", "num": 6, "title": "Aufbau einer guten OPL",
        "points": [("Nummer, Titel, Revision, Datum", "Beginnen Sie mit einer Nummer"),
                   ("Warum es wichtig ist + der eine Kernpunkt", "Dann sagen Sie, warum"),
                   ("Bilder, Schritte, Warnung", "Ergänzen Sie die Bilder"),
                   ("Verantwortlicher, Freigabe, Schulungsnachweis", "Enden Sie mit dem Verantwortlichen")],
        "example": "Die Seite sollte auf einen Blick verständlich sein. Könnte Ihr neuester Werker sie in "
                   "einer Minute lesen?",
        "example_cue": "Die Seite sollte auf einen Blick",
        "script": "Jede OPL hat dasselbe Layout, damit man weiß, wohin man schaut. Beginnen Sie mit einer "
                  "Nummer, einem kurzen Titel, der Revision und dem Datum. Dann sagen Sie, warum es wichtig "
                  "ist, und nennen den einen Kernpunkt. Ergänzen Sie die Bilder und einfache Schritte. "
                  "Fügen Sie eine Warnung hinzu, wo es ein Risiko gibt. Enden Sie mit dem Verantwortlichen, "
                  "der Freigabe und dem Schulungsnachweis. Die Seite sollte auf einen Blick verständlich "
                  "sein. Könnte Ihr neuester Werker sie in einer Minute lesen?",
    },
    {
        "key": "p07", "num": 7, "title": "Wie Sie sie vorbereiten",
        "points": [("Ein Lernziel festlegen", "ein Lernziel festzulegen"),
                   ("Zum Gemba gehen, den Standard prüfen", "Dann gehen Sie zum Gemba"),
                   ("Einfache Worte, echte Fotos, gut gegen schlecht", "Dann fassen Sie es"),
                   ("Prüfen, dann freigeben", "Dann lassen Sie die Qualität")],
        "example": "Ravi fotografierte den echten Stecker, an der echten Station.",
        "example_cue": "Ravi fotografierte",
        "script": "Beginnen Sie damit, ein Lernziel festzulegen. Dann gehen Sie zum Gemba, und beobachten "
                  "die echte Arbeit. Prüfen Sie den freigegebenen Standard und die Grundursache. Dann "
                  "fassen Sie es in einfache Worte Ihrer Werker. Ergänzen Sie echte Fotos, Pfeile und gute "
                  "und schlechte Beispiele. Entwerfen Sie es auf der Standardvorlage. Dann lassen Sie die "
                  "Qualität oder die Technik prüfen und freigeben. Ravi fotografierte den echten Stecker, "
                  "an der echten Station. Wie wirken die Bilder?",
    },
    {
        "key": "p08", "num": 8, "title": "Visuelle Kommunikation",
        "points": [("Echte Fotos, Pfeile auf die genaue Stelle", "Nutzen Sie echte Fotos"),
                   ("Gut und schlecht nebeneinander", "Stellen Sie gut und schlecht"),
                   ("Große Schrift, viel Platz", "Nutzen Sie große Schrift"),
                   ("Farbe nie als einziges Signal", "nutzen Sie Farbe nie")],
        "example": "Ravis OPL zeigt einen Haken, ein Kreuz und die Worte gut und nicht gut.",
        "example_cue": "Ravi ergänzte einen Haken",
        "script": "Bilder sind das Herz einer OPL. Der Lernende sollte den Punkt verstehen, bevor er einen "
                  "Satz liest. Nutzen Sie echte Fotos, mit Pfeilen und Kreisen auf der genauen Stelle. "
                  "Stellen Sie gut und schlecht nebeneinander. Nutzen Sie große Schrift und viel Platz. "
                  "Vermeiden Sie lange Absätze und Fachjargon. Und nutzen Sie Farbe nie als einziges "
                  "Signal. Ravi ergänzte einen Haken, ein Kreuz, und die Worte gut und nicht gut. Wie "
                  "lehren Sie sie nun?",
    },
    {
        "key": "p09", "num": 9, "title": "Vermitteln am Gemba",
        "points": [("Erklären, warum es wichtig ist", "Erklären Sie, warum es wichtig ist"),
                   ("Zeigen, vormachen, vergleichen", "Zeigen Sie das echte Teil"),
                   ("Fragen stellen, selbst versuchen lassen", "Stellen Sie kurze Fragen"),
                   ("Eine Unterschrift allein beweist nichts", "Eine Unterschrift allein")],
        "example": "Ravi lehrt jede Lektion in 5 Minuten zu Schichtbeginn und beobachtet dann jeden Werker "
                   "dabei.",
        "example_cue": "Ravi lehrt jede Lektion",
        "script": "Lehren Sie dort, wo die Arbeit passiert. Erklären Sie, warum es wichtig ist, für "
                  "Qualität oder Sicherheit. Zeigen Sie das echte Teil. Machen Sie es langsam vor, dann "
                  "vergleichen Sie gut und schlecht. Stellen Sie kurze Fragen, um das Verständnis zu "
                  "prüfen. Lassen Sie den Lernenden es versuchen, und korrigieren Sie sofort. Ravi lehrt "
                  "jede Lektion in fünf Minuten zu Schichtbeginn. Dann beobachtet er jeden Werker dabei. "
                  "Eine Unterschrift allein beweist nichts. Wo helfen OPL noch?",
    },
    {
        "key": "p10", "num": 10, "title": "OPL für Box Build und Qualität",
        "points": [("Platinen: AOI-Fehlalarm oder echter Fehler", "Bei Platinen"),
                   ("Montage: Schraubenreihenfolge, Steckerverriegelung", "In der Montage"),
                   ("Test: Prüfung der Firmware-Version", "Im Test"),
                   ("Verpackung: Etiketten- und Zubehörprüfung", "Bei der Verpackung")],
        "example": "Falsche PCB vermeiden: wo die Platinennummer steht, wie man das Modell abgleicht, was "
                   "bei Abweichung zu tun ist.",
        "example_cue": "Ravis nächste Lektion",
        "script": "Fast jeder Prozess hat ein gutes Thema für eine OPL. Bei Platinen, wie man einen "
                  "AOI-Fehlalarm von einem echten Fehler unterscheidet. In der Montage, die "
                  "Schraubenreihenfolge und die Steckerverriegelung. Im Test, die Prüfung der "
                  "Firmware-Version. Bei der Verpackung, Etiketten- und Zubehörprüfung. Ravis nächste "
                  "Lektion war, eine falsche PCB zu vermeiden. Wo die Platinennummer steht, wie man das "
                  "Modell abgleicht, und was bei Abweichung zu tun ist. Welches Thema hilft Ihnen?",
    },
    {
        "key": "p11", "num": 11, "title": "OPL und andere Lean-Werkzeuge",
        "points": [("Nach einem Kaizen: die neue Methode", "Nach einem Kaizen"),
                   ("Nach einem Poka Yoke: was sein Alarm bedeutet", "Nach einem Poka Yoke"),
                   ("5S-Standards und Maschinenpflege", "Sie lehrt 5S-Standards"),
                   ("Lehren aus der Ursachenanalyse", "Sie teilt die Lehren")],
        "example": "Neue Vorrichtung → eine OPL, wie man sie belädt und was das rote Licht bedeutet.",
        "example_cue": "Ravis Team baute",
        "script": "OPL helfen anderen Lean-Werkzeugen in der Fertigung. Nach einem Kaizen lehrt eine OPL "
                  "die neue Methode. Nach einem Poka Yoke erklärt sie, wie die Vorrichtung arbeitet und was "
                  "ihr Alarm bedeutet. Sie lehrt 5S-Standards und Maschinenpflege für TPM. Sie teilt die "
                  "Lehren aus der Ursachenanalyse. Ravis Team baute eine neue Vorrichtung ein. Ihre OPL "
                  "lehrte, wie man sie belädt und was das rote Licht bedeutet. Aber wie halten Sie OPL "
                  "korrekt?",
    },
    {
        "key": "p12", "num": 12, "title": "Lenkung und Revisionen",
        "points": [("Nummer, Verantwortlicher, Freigeber", "Geben Sie ihr eine eindeutige Nummer"),
                   ("Mit der SOP verknüpft, die sie stützt", "Verknüpfen Sie sie mit der SOP"),
                   ("Bei jeder Änderung geprüft", "Prüfen Sie sie, wann immer"),
                   ("Alte Kopien von der Linie entfernt", "Und entfernen Sie alte Kopien")],
        "example": "Als der Steckerlieferant wechselte, überarbeitete Ravi die Lektion und zog jede alte "
                   "Kopie ein.",
        "example_cue": "Als Ravis Steckerlieferant",
        "script": "Eine OPL ist ein gelenktes Dokument, auch wenn sie kurz ist. Geben Sie ihr eine "
                  "eindeutige Nummer, einen Verantwortlichen und einen Freigeber. Verknüpfen Sie sie mit "
                  "der SOP, die sie stützt. Prüfen Sie sie, wann immer sich Produkt, Prozess oder Standard "
                  "ändern. Und entfernen Sie alte Kopien von der Linie. Als Ravis Steckerlieferant "
                  "wechselte, überarbeitete er die Lektion und zog jede alte Kopie ein. Die goldene Regel: "
                  "eine OPL darf nie dem Standard widersprechen. Hat es gewirkt?",
    },
    {
        "key": "p13", "num": 13, "title": "Wirksamkeit messen",
        "points": [("Geändertes Verhalten ist das Ergebnis", "Geändertes Verhalten ist es"),
                   ("Wissen mit Fragen prüfen", "Prüfen Sie also das Wissen"),
                   ("Die Methode Tage später beobachten", "Dann beobachten Sie die Methode"),
                   ("Den Zielfehler verfolgen", "Und verfolgen Sie den Fehler")],
        "example": "Nachtschicht: 14 gebrochene Stecker pro Woche → 1 pro Woche, sechs Wochen nach der "
                   "Lektion.",
        "example_cue": "Ravis Nachtschicht brach",
        "script": "Hier ist der echte Test. Abgeschlossene Schulung ist nicht das Ergebnis. Geändertes "
                  "Verhalten ist es. Prüfen Sie also das Wissen mit ein paar Fragen. Dann beobachten Sie "
                  "die Methode am Gemba, Tage später. Und verfolgen Sie den Fehler, auf den Sie zielten. "
                  "Ravis Nachtschicht brach vierzehn Stecker pro Woche. Sechs Wochen nach der Lektion "
                  "einen. Bleibt ein Problem, schulen Sie nicht nur neu. Prüfen Sie auch Standard und "
                  "Prozess. Welche Fehler sollten Sie meiden?",
    },
    {
        "key": "p14", "num": 14, "title": "Häufige Fehler",
        "points": [("Zu viel Inhalt → aufteilen", "Zu viel Inhalt"),
                   ("Nur Text → echte Fotos ergänzen", "Nur Text"),
                   ("Nur Unterschrift → vormachen und beobachten", "Schulung nur per Unterschrift"),
                   ("Alte Version an der Wand → Revisionslenkung", "Eine alte Version")],
        "example": "Ravis erster Entwurf behandelte vier Themen. Er teilte ihn in vier Lektionen.",
        "example_cue": "Ravis erster Entwurf",
        "script": "Achten Sie auf klassische Fehler. Zu viel Inhalt auf einer Seite? Teilen Sie ihn. Nur "
                  "Text? Ergänzen Sie echte Fotos. Schulung nur per Unterschrift? Vormachen und beobachten. "
                  "Eine alte Version noch an der Wand? Nutzen Sie Revisionslenkung. Und nutzen Sie eine OPL "
                  "nie, um jemanden zu beschuldigen. Ravis erster Entwurf behandelte vier Themen. Er teilte "
                  "ihn in vier Lektionen.",
    },
    {
        "key": "p15", "num": 15, "title": "Fahrplan und Checkliste",
        "points": [("Vorlage, Nummerierung, Freigabe planen", "Planen Sie Ihre Vorlage"),
                   ("Pilot bei den größten Fehlern oder Risiken", "Pilotieren Sie ein paar Lektionen"),
                   ("Trainer schulen, am Gemba nutzen", "Schulen Sie Schichtleiter"),
                   ("Wirkung messen, Bibliothek aufbauen", "Messen Sie die Wirkung")],
        "example": "Vor der Freigabe fragen: Ist sie korrekt? Ist der Punkt klar?",
        "example_cue": "Bevor Sie eine Lektion freigeben",
        "script": "Führen Sie es in einfachen Phasen ein. Planen Sie Ihre Vorlage, Nummerierung und "
                  "Freigabe. Pilotieren Sie ein paar Lektionen bei Ihren größten Fehlern oder "
                  "Sicherheitsrisiken. Schulen Sie Schichtleiter und erfahrene Werker, sie zu lehren. Dann "
                  "nutzen Sie sie in Schichtbesprechungen und am Gemba. Messen Sie die Wirkung, und bauen "
                  "Sie eine gelenkte Bibliothek auf. Bevor Sie eine Lektion freigeben, fragen Sie sich. Ist "
                  "sie korrekt? Ist der Punkt klar? Lehren Sie einen Punkt gut, und halten Sie ihn aktuell.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Eine Sache", "icon": "check"}, {"label": "Minuten zum Lernen", "icon": "clock"},
        {"label": "Visuell", "icon": "camera"}, {"label": "Am Arbeitsplatz", "icon": "wrench"}]},
    "p02": {"type": "versus", "items": [
        {"label": "Die SOP ersetzen", "sub": "oder ein großes Thema quetschen", "icon": "cross", "with": 0},
        {"label": "Neben der SOP", "sub": "Zeigt auf den genauen Schritt", "icon": "clipboard", "with": 2}]},
    "p03": {"type": "compare", "before": {"label": "Nachtschicht", "value": 14}, "after": {"label": "Tagschicht", "value": 2},
            "unit": "gebrochene Stecker pro Woche", "note": "Gleiche SOP, anderes Wissen", "with": "example"},
    "p04": {"type": "icons", "items": [
        {"label": "Grundwissen", "icon": "chip", "with": 0}, {"label": "Problem", "icon": "warning", "with": 1},
        {"label": "Verbesserung", "icon": "chartUp", "with": 2}, {"label": "Sicherheit", "icon": "shield", "with": 3},
        {"label": "Qualität", "icon": "check", "with": 3}, {"label": "Instandhaltung", "icon": "wrench", "with": 3}]},
    "p05": {"type": "icons", "items": [
        {"label": "Wiederholfehler gelöst", "icon": "check"}, {"label": "Neues Produkt oder Vorrichtung", "icon": "box"},
        {"label": "Missverstandener Schritt", "icon": "search"}, {"label": "Beinaheunfall, oder ein Trick", "icon": "warning"}]},
    "p06": {"type": "doc", "items": [
        {"label": "OPL-012 · Stecker einsetzen · Rev B", "icon": "label", "with": 0},
        {"label": "Kernpunkt: drücken, bis es klickt", "icon": "key", "with": 1},
        {"label": "", "icon": "goodbad", "with": 2},
        {"label": "Warnung: nie mit Gewalt", "icon": "warning", "with": 2},
        {"label": "Verantwortlich · freigegeben · geschult", "icon": "person", "with": 3}]},
    "p07": {"type": "flow", "items": [
        {"label": "Ein Lernziel", "icon": "search"},
        {"label": "Zum Gemba gehen", "sub": "Den Standard prüfen", "icon": "walk"},
        {"label": "Einfache Worte, echte Fotos", "icon": "camera"},
        {"label": "Prüfen, dann freigeben", "icon": "check", "tone": "good"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Echte Fotos, Pfeile", "icon": "camera", "with": 0},
        {"label": "Gut und schlecht nebeneinander", "icon": "shape", "with": 1},
        {"label": "Große Schrift, Platz", "icon": "label", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Nur Farbe", "sub": "Nicht jeder sieht sie", "icon": "warning"},
            {"label": "Haken, Kreuz + Worte", "sub": "Gut / nicht gut", "icon": "check"}]}},
    "p09": {"type": "flow", "items": [
        {"label": "Erklären, warum es wichtig ist", "icon": "person"},
        {"label": "Zeigen, vormachen, vergleichen", "icon": "camera"},
        {"label": "Fragen, dann versuchen lassen", "icon": "hand"},
        {"label": "Eine Unterschrift beweist nichts", "icon": "cross", "tone": "bad"}]},
    "p10": {"type": "flow", "items": [
        {"label": "Platinen", "sub": "AOI-Fehlalarm oder echter Fehler", "icon": "chip"},
        {"label": "Montage", "sub": "Schraubenreihenfolge, Steckerverriegelung", "icon": "screw"},
        {"label": "Test", "sub": "Prüfung der Firmware-Version", "icon": "test"},
        {"label": "Verpackung", "sub": "Etikett und Zubehör", "icon": "label"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Kaizen", "icon": "chartUp"}, {"label": "Poka Yoke", "icon": "key"},
        {"label": "5S + TPM", "icon": "tray"}, {"label": "Grundursache", "icon": "search"}]},
    "p12": {"type": "flow", "items": [
        {"label": "Nummer, Verantwortlicher, Freigeber", "icon": "label"},
        {"label": "Mit ihrer SOP verknüpft", "icon": "clipboard"},
        {"label": "Bei jeder Änderung geprüft", "icon": "sequence"},
        {"label": "Alte Kopien entfernt", "icon": "trash", "tone": "good"}]},
    "p13": {"type": "icons", "items": [
        {"label": "Geändertes Verhalten", "icon": "person", "with": 0},
        {"label": "Ein paar Fragen", "icon": "search", "with": 1},
        {"label": "Beobachten, Tage später", "icon": "clock", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Vorher", "value": 14}, "after": {"label": "6 Wochen danach", "value": 1},
                 "unit": "gebrochene Stecker pro Woche, Nachtschicht", "note": "Die Lektion änderte das Verhalten", "with": "example"}},
    "p14": {"type": "icons", "items": [
        {"label": "Zu viel?", "sub": "Aufteilen", "icon": "stack"},
        {"label": "Nur Text?", "sub": "Echte Fotos ergänzen", "icon": "camera"},
        {"label": "Nur Unterschrift?", "sub": "Die Arbeit beobachten", "icon": "hand"},
        {"label": "Alte Version?", "sub": "Revisionslenkung", "icon": "sequence"}]},
    "p15": {"type": "steps", "items": [
        {"label": "Vorlage + Nummerierung", "with": 0}, {"label": "Pilot bei großen Fehlern", "with": 1},
        {"label": "Trainer schulen", "with": 2}, {"label": "Am Gemba nutzen", "with": 2},
        {"label": "Wirkung messen", "with": 3}, {"label": "Bibliothek aufbauen", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Ein OPL-Entwurf behandelt Stecker einsetzen, Schraubendrehmoment, Etikettenprüfung und "
                    "ESD auf einer Seite. Was ist das Problem?",
        "options": ["Sie braucht mehr Text", "Zu viele Punkte: in einzelne OPL aufteilen",
                    "Sie sollte nur farbig sein"],
        "correct": 1,
        "explanation": "Eine OPL lehrt EINEN Punkt. Vier Themen auf einer Seite verwässern die Botschaft. Machen "
                       "Sie lieber vier fokussierte OPL.",
        "q_script": "Kurzer Check. Ein Entwurf behandelt Stecker einsetzen, Schraubendrehmoment, "
                    "Etikettenprüfung und ESD, alles auf einer Seite. Was ist das Problem? Nehmen Sie sich "
                    "kurz Zeit.",
        "a_script": "Er hat zu viele Punkte. Eine One Point Lesson lehrt eine Sache. Teilen Sie ihn in vier "
                    "fokussierte Lektionen.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Alle haben die OPL vor zwei Wochen unterschrieben, aber derselbe Fehler ist zurück. Was "
                    "sollte der Schichtleiter ZUERST tun?",
        "options": ["Alle noch einmal unterschreiben lassen", "Die Arbeit beobachten und Standard, Methode und Lektion prüfen",
                    "Die Werker beschuldigen, die unterschrieben", "Die OPL von der Linie nehmen"],
        "correct": 1,
        "explanation": "Unterschriften beweisen kein Lernen. Beobachten Sie: Wird die Methode befolgt, stimmt "
                       "der Standard, ist die OPL klar? Dann beheben Sie die Ursache.",
        "q_script": "Noch eine, ein Szenario. Alle haben die Lektion vor zwei Wochen unterschrieben, aber "
                    "derselbe Fehler ist zurück. Was sollte der Schichtleiter zuerst tun? Überlegen Sie kurz.",
        "a_script": "Beobachten Sie die Arbeit. Prüfen Sie Methode, Standard und die Lektion selbst. Eine "
                    "Unterschrift beweist kein Lernen, also finden Sie die echte Ursache.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
