"""burn_down_chart in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh burn_down_chart_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "bd_de"
NAME = "burn_down_chart_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Cycle Time Study": "Saikel Taim Stadi",
    "Burn Down Chart": "Börn Daun Tschart",
    "Kaizen": "Kaisen",
    "RF": "err eff",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Letzten Monat fuhr der Lkw mit achtzig Routern zu wenig ab. Niemand sah es kommen, bis "
    "Freitagnachmittag. Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie das Burn "
    "Down Chart kennen. Sie sehen, wie man die verbleibende Arbeit verfolgt. Sie erkennen "
    "eine Verzögerung an Tag zwei, nicht an Tag fünf, und holen sie rechtzeitig auf. Wir "
    "begleiten Sneha, Produktionsleiterin an einer Linie für Wi-Fi-Router, die dafür sorgt, "
    "dass das nie wieder passiert."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Zeichnen Sie zuerst die Ideallinie, und nie neu, um besser "
    "auszusehen. Zählen Sie nur Arbeit, die fertig und gut ist. Und wenn die Linie über die "
    "Ideallinie steigt, handeln Sie am selben Tag, mit einem Verantwortlichen. Ihre Aufgabe "
    "für diese Woche. Zeichnen Sie für eine Arbeit mit Termin das Diagramm vor der morgigen "
    "Schicht. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie die Cycle Time "
    "Study kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was das Diagramm zeigt",
        "points": [("Restarbeit gegenüber verfügbarer Zeit", "wie viel Arbeit übrig ist"),
                   ("Senkrecht: Restarbeit. Waagerecht: Zeit", "Die senkrechte Achse"),
                   ("Die Linie fällt Richtung null", "sollte die Linie Richtung null")],
        "example": "Snehas Diagramm: ein Whiteboard neben der Linie, für jede Schicht sichtbar.",
        "example_cue": "Sneha zeichnet ihres",
        "script": "Hier ist die Idee. Ein Restarbeitsdiagramm zeigt, wie viel Arbeit übrig ist, gegenüber "
                  "der Zeit, die Sie haben. Die senkrechte Achse ist die Restarbeit. Die waagerechte Achse "
                  "ist die Zeit. Während Ihr Team Arbeit erledigt, sollte die Linie Richtung null fallen. "
                  "Das ist alles. Einfach, aber wirkungsvoll. Sneha zeichnet ihres auf ein Whiteboard neben "
                  "der Linie, damit jede Schicht es sieht. Warum liebt Lean also so ein einfaches Diagramm?",
    },
    {
        "key": "p02", "num": 2, "title": "Warum Lean es nutzt",
        "points": [("Ein Ziel wird zu einem sichtbaren Weg", "aus einem Ziel einen Weg"),
                   ("Eine Lücke sehen, solange sie klein ist", "Sie sehen eine Lücke"),
                   ("Auf den Engpass konzentrieren", "Ihre Leute auf den einen Engpass")],
        "example": "Letzten Monat: nur ein Termin. Die Lücke zeigte sich am Freitagnachmittag.",
        "example_cue": "Letzten Monat hatte Sneha",
        "script": "Weil es aus einem Ziel einen Weg macht, den Sie sehen können. Ein Termin allein sagt "
                  "Ihnen nichts, bis er verpasst ist. Dieses Diagramm zeigt Ihnen jeden Tag, ob Sie im Plan "
                  "sind. Sie sehen eine Lücke, solange sie noch klein ist. Und Sie können Ihre Leute auf "
                  "den einen Engpass konzentrieren, der den Abschluss verhindert. Letzten Monat hatte Sneha "
                  "nur einen Termin. Sie fand die Lücke am Freitag. Was wären Ihnen zwei zusätzliche Tage "
                  "wert?",
    },
    {
        "key": "p03", "num": 3, "title": "Wofür es da ist",
        "points": [("Restarbeit für alle sichtbar", "Es macht die Restarbeit"),
                   ("Tatsächlicher Fortschritt gegenüber nötigem Tempo", "Es vergleicht den echten Fortschritt"),
                   ("Verzögerungen früh erkennen", "Es erkennt Verzögerungen früh"),
                   ("Aufholmaßnahmen mit Fakten belegt", "belegt Ihre Aufholmaßnahmen")],
        "example": "Das Ziel: jede geplante Einheit erreicht bis zum Termin null.",
        "example_cue": "Das Ziel ist einfach",
        "script": "Was tut dieses Diagramm also wirklich für Sie? Es macht die Restarbeit für das ganze "
                  "Team sichtbar, nicht nur für den Planer. Es vergleicht den echten Fortschritt mit dem "
                  "Tempo, das Sie brauchen. Es erkennt Verzögerungen früh, solange Aufholen noch günstig "
                  "ist. Und es belegt Ihre Aufholmaßnahmen mit Fakten, nicht mit Gefühlen. Das Ziel ist "
                  "einfach. Jede geplante Einheit erreicht bis zum Termin null. Schauen wir uns an, was im "
                  "Diagramm steht.",
    },
    {
        "key": "p04", "num": 4, "title": "Die fünf Elemente",
        "points": [("Achsen: Restarbeit, Zeit", "Die senkrechte Achse"),
                   ("Ideallinie: das nötige Tempo", "Die Ideallinie"),
                   ("Istlinie: was wirklich passiert ist", "Die Istlinie"),
                   ("Lücke: Ist minus Ideal", "die Lücke ist")],
        "example": "Sneha verfolgt die Router, die noch fertig werden müssen, Tag für Tag.",
        "example_cue": "Sneha verfolgt die Router",
        "script": "Das Diagramm hat fünf Teile. Die senkrechte Achse ist die Restarbeit, in Einheiten, "
                  "Fehlern, Maßnahmen oder Stunden. Die waagerechte Achse ist die Zeit, in Schichten, Tagen "
                  "oder Wochen. Die Ideallinie ist das Tempo, das Sie brauchen. Die Istlinie ist das, was "
                  "wirklich passiert ist. Und die Lücke ist der Abstand dazwischen. Sneha verfolgt die "
                  "Router, die noch fertig werden müssen, Tag für Tag. Welche Einheit würden Sie an Ihrer "
                  "Linie zählen?",
    },
    {
        "key": "p05", "num": 5, "title": "Snehas Herausforderung",
        "points": [("1.000 Router im Umlauf", "Tausend Router"),
                   ("5 Arbeitstage bis zum Lkw", "Der Lkw fährt"),
                   ("Rest = geplant − erledigt", "Die Restarbeit ist gleich")],
        "example": "Tag 0: nichts erledigt, 1.000 Router übrig.",
        "example_cue": "An Tag null",
        "script": "Hier ist Snehas Herausforderung in diesem Monat. Tausend Router stecken im Umlauf fest. "
                  "Sie brauchen noch den Endtest und die Verpackung, und nur gute Einheiten zählen. Der Lkw "
                  "fährt in fünf Arbeitstagen. Die Rechnung beginnt einfach. Die Restarbeit ist gleich der "
                  "gesamten geplanten Arbeit, minus dem, was Sie schon erledigt haben. An Tag null ist "
                  "nichts erledigt, also sind alle tausend übrig. Können Sie das Tempo erraten, das sie pro "
                  "Tag braucht?",
    },
    {
        "key": "p06", "num": 6, "title": "Das ideale Tempo",
        "points": [("Tempo = Gesamtarbeit ÷ Perioden", "Gesamtarbeit geteilt"),
                   ("1.000 ÷ 5 = 200 pro Tag", "Zweihundert pro Tag"),
                   ("Zuerst zeichnen, nie neu zeichnen", "Zeichnen Sie sie, bevor")],
        "example": "Ideallinie: 1.000 → 800 → 600 → 400 → 200 → 0",
        "example_cue": "Ihre Ideallinie fällt also",
        "script": "Das ideale Tempo ist die Gesamtarbeit geteilt durch die Perioden, die Sie haben. Für "
                  "Sneha sind das tausend Router in fünf Tagen. Zweihundert pro Tag. Ihre Ideallinie fällt "
                  "also in fünf gleichen Schritten auf null. Diese gerade Linie ist ihr Plan. Zeichnen Sie "
                  "sie, bevor die Arbeit beginnt, und zeichnen Sie sie nie neu, um besser auszusehen. Wenn "
                  "Sie den Plan verschieben, verstecken Sie die Lücke. Was ist also nach zwei Tagen "
                  "passiert?",
    },
    {
        "key": "p07", "num": 7, "title": "Tag zwei: die Lücke finden",
        "points": [("Erledigt: 320", "Ihr Team hat"),
                   ("Übrig: 680. Ideal: 600", "Es sind also sechshundertachtzig übrig"),
                   ("Lücke: 80 hinter dem Plan", "Die Lücke beträgt"),
                   ("Drei Tage zum Aufholen, Qualität unangetastet", "Sie hat drei Tage")],
        "example": "Am Dienstag erkannt, nicht am Freitag.",
        "example_cue": "sie weiß es am Dienstag",
        "script": "Am Ende von Tag zwei aktualisiert Sneha ihr Diagramm. Ihr Team hat dreihundertzwanzig "
                  "Router erledigt. Es sind also sechshundertachtzig übrig. Aber ihre Ideallinie sagt, dass "
                  "sechshundert übrig sein sollten. Die Lücke beträgt achtzig Router hinter dem Plan. Ist "
                  "das eine Katastrophe? Nein, aber ein Signal. Sie hat drei Tage, um sie aufzuholen, ohne "
                  "bei der Qualität zu sparen. Und sie weiß es am Dienstag, nicht am Freitag.",
    },
    {
        "key": "p08", "num": 8, "title": "Die Linien lesen",
        "points": [("Über der Ideallinie: im Rückstand. Engpass finden", "Istlinie über der Ideallinie liegt"),
                   ("Unter der Ideallinie: im Vorsprung. Qualität bestätigen", "Liegt sie darunter"),
                   ("Vorsprung mit schlechten Einheiten ist kein Vorsprung", "Vorsprung mit schlechten Einheiten")],
        "example": "Snehas Linie liegt über der Ideallinie. Was hindert die Router daran, fertig zu werden?",
        "example_cue": "Snehas Linie lag darüber",
        "script": "Wie lesen Sie die Linien? Wenn die Istlinie über der Ideallinie liegt, ist mehr Arbeit "
                  "übrig als geplant. Finden Sie den Engpass und legen Sie eine Aufholmaßnahme fest. Liegt "
                  "sie darunter, sind Sie im Vorsprung. Gut, aber bestätigen Sie die Qualität. Vorsprung "
                  "mit schlechten Einheiten ist kein Vorsprung. Snehas Linie lag darüber. Also fragte sie: "
                  "Was hindert die Router am Fertigwerden? Was würden Sie zuerst prüfen?",
    },
    {
        "key": "p09", "num": 9, "title": "Flache Linien und null erreichen",
        "points": [("Flache Linie: nichts abgeschlossen", "Eine flache Linie bedeutet"),
                   ("Stillstand, Verantwortlichen, Daten prüfen", "Prüfen Sie also auf einen Stillstand"),
                   ("Bei null: prüfen, dann abschließen", "wenn die Linie null erreicht")],
        "example": "Mittwoch: Snehas Linie blieb eine ganze Schicht lang flach.",
        "example_cue": "Am Mittwoch",
        "script": "Zwei weitere Muster zählen. Eine flache Linie bedeutet, dass nichts abgeschlossen wurde. "
                  "Entweder stand die Arbeit, oder niemand aktualisierte das Diagramm. Prüfen Sie also auf "
                  "einen Stillstand, den Verantwortlichen und die Daten. Und wenn die Linie null erreicht? "
                  "Nicht nur feiern. Prüfen Sie die Abnahmekriterien jeder Einheit, dann schließen Sie "
                  "formal ab. Am Mittwoch blieb Snehas Linie eine Schicht lang flach. Warum wohl?",
    },
    {
        "key": "p10", "num": 10, "title": "Die tägliche Überprüfung",
        "points": [("Aktualisieren und vergleichen", "Aktualisieren Sie, indem Sie"),
                   ("Die Hauptursache erklären", "Erklären Sie die Hauptursache"),
                   ("Handeln: ein Verantwortlicher und eine Uhrzeit", "Handeln Sie, mit einem Verantwortlichen"),
                   ("Bei der nächsten Aktualisierung bestätigen", "Dann bestätigen Sie beim")],
        "example": "Sneha macht die Überprüfung in 10 Minuten, zu Beginn jeder Schicht.",
        "example_cue": "Sneha macht das",
        "script": "Vorher die Gewohnheit, die es erkennt. Ein Diagramm hilft nur bei täglicher, gleicher "
                  "Prüfung. Aktualisieren Sie, indem Sie Erledigtes erfassen und den Rest neu berechnen. "
                  "Vergleichen Sie Ist mit Ideal. Erklären Sie die Hauptursache jeder schlechten Lücke. "
                  "Handeln Sie, mit einem Verantwortlichen und einer Uhrzeit. Dann bestätigen Sie beim "
                  "nächsten Mal, dass die Linie wieder fällt. Sneha macht das in zehn Minuten zu "
                  "Schichtbeginn. Und Sie?",
    },
    {
        "key": "p11", "num": 11, "title": "Snehas Aufholjagd",
        "points": [("Engpass: ein RF-Tester ausgefallen", "Eine RF-Teststation"),
                   ("Zweiter Tester, Personal mit Vorrang", "Ein Techniker nahm"),
                   ("Ein einziger Verantwortlicher aktualisiert das Diagramm", "Sie benannte einen Verantwortlichen")],
        "example": "Freitag: null Router übrig, ein paar Stunden vor dem Lkw.",
        "example_cue": "Bis Freitag",
        "script": "Das bedeutete also die flache Linie vom Mittwoch. Eine RF-Teststation war zur "
                  "Kalibrierung außer Betrieb. Router stauten sich davor. Und niemand aktualisierte das "
                  "Diagramm, weil niemand dafür benannt war. Sneha behob beides. Ein Techniker nahm einen "
                  "zweiten Tester in Betrieb, und der Test bekam Personal mit Vorrang. Sie benannte einen "
                  "Verantwortlichen, der das Diagramm zu einer festen Zeit aktualisiert. Bis Freitag "
                  "berührte die Linie null, ein paar Stunden vor dem Lkw. Wo könnten Sie das sonst noch "
                  "nutzen?",
    },
    {
        "key": "p12", "num": 12, "title": "Wo man es nutzt",
        "points": [("Ein klarer Start, ein klares Ende, ein Termin", "wann immer die Arbeit"),
                   ("Produktion: Umlauf, Aufholen", "Bauen Sie den Umlauf"),
                   ("Qualität: kritische Fehler auf null", "Schließen Sie jeden kritischen"),
                   ("Instandhaltungs- und Kaizen-Maßnahmen", "Erledigen Sie offene Instandhaltungsmaßnahmen")],
        "example": "Snehas Qualitätsteam bringt offene Fehler jetzt vor dem Versand auf null.",
        "example_cue": "Snehas Qualitätsteam",
        "script": "Dieses Diagramm ist nicht nur für die Produktion. Nutzen Sie es, wann immer die Arbeit "
                  "eine klare Startmenge, ein klares Ende und einen Termin hat. Bauen Sie den Umlauf vor "
                  "einem Typwechsel ab. Holen Sie eine Unterdeckung vor dem Versandschluss auf. Schließen "
                  "Sie jeden kritischen Fehler vor dem Versand. Erledigen Sie offene "
                  "Instandhaltungsmaßnahmen oder Kaizen-Aufgaben vor einer Überprüfung. Snehas "
                  "Qualitätsteam bringt jetzt auch offene Fehler auf null. Was hat diese Woche in Ihrer "
                  "Halle einen Termin?",
    },
    {
        "key": "p13", "num": 13, "title": "Ehrliche Daten",
        "points": [("Eine Einheit, eine eingefrorene Startmenge", "Nutzen Sie eine Einheit"),
                   ("„Fertig“ vor dem Start definieren", "Definieren Sie genau, wann"),
                   ("Nur gute Menge zählen", "zählen Sie nur Menge")],
        "example": "Router, die auf den Nachtest warten: nicht als fertig gezählt.",
        "example_cue": "Am Donnerstag",
        "script": "Ein Diagramm ist nur so ehrlich wie seine Daten. Nutzen Sie eine Einheit durchgehend. "
                  "Frieren Sie die Startmenge ein, außer eine Umfangsänderung ist genehmigt. Definieren Sie "
                  "genau, wann etwas als fertig zählt. Und zählen Sie nur Menge, die die Qualität erfüllt. "
                  "Am Donnerstag wollte Snehas Team Router zählen, die auf den Nachtest warteten. Sie sagte "
                  "nein. Halb fertig ist nicht fertig, und eine durchgefallene Einheit auch nicht. Hätten "
                  "Sie sie gezählt?",
    },
    {
        "key": "p14", "num": 14, "title": "Häufige Fehler",
        "points": [("Die Startmenge ändern", "Die Startmenge zu ändern"),
                   ("Späte oder unregelmäßige Aktualisierungen", "Späte Aktualisierungen"),
                   ("Teilweise oder abgelehnte Einheiten zählen", "Teilarbeit zu zählen"),
                   ("Ein Diagramm ohne Maßnahmen", "Ein Diagramm ohne Maßnahmen")],
        "example": "Sneha notiert genehmigte Umfangsänderungen in einem eigenen Feld neben ihrem Diagramm.",
        "example_cue": "Sneha notiert genehmigte",
        "script": "Achten Sie auf ein paar häufige Fehler. Die Startmenge zu ändern versteckt die "
                  "ursprüngliche Lücke. Späte Aktualisierungen bedeuten, dass Sie reagieren, wenn die "
                  "Verzögerung schon gewachsen ist. Teilarbeit zu zählen, oder abgelehnte Einheiten, lässt "
                  "den Fortschritt besser aussehen, als er ist. Und ein Diagramm ohne Maßnahmen ist nur ein "
                  "Bericht. Sneha notiert genehmigte Umfangsänderungen in einem eigenen Feld neben ihrem "
                  "Diagramm. Die ursprüngliche Lücke bleibt sichtbar. Welchen Fehler haben Sie schon "
                  "gesehen?",
    },
    {
        "key": "p15", "num": 15, "title": "Stärken, Grenzen und Checkliste",
        "points": [("Einfach, schnell, eine Frühwarnung", "Dieses Diagramm ist einfach"),
                   ("Findet die Grundursache nicht allein", "es erklärt die Grundursache"),
                   ("Definieren, bestätigen, berechnen, Verantwortlichen benennen", "hier ist Ihre Checkliste"),
                   ("Aktualisieren, handeln, erst bei null abschließen", "Dann aktualisieren Sie")],
        "example": "Sneha hängt diese Checkliste neben jedes neue Diagramm.",
        "example_cue": "Sneha hängt diese Checkliste",
        "script": "Das Fazit? Dieses Diagramm ist einfach, schnell lesbar, und warnt vor dem Termin. Aber "
                  "es erklärt die Grundursache nicht allein. Und es braucht ehrliche, pünktliche "
                  "Aktualisierungen. Also, hier ist Ihre Checkliste. Arbeit definieren, und was fertig "
                  "heißt. Startmenge und Termin bestätigen. Ideales Tempo berechnen, Verantwortlichen "
                  "benennen. Dann aktualisieren Sie, handeln und schließen erst bei null ab. Sneha hängt "
                  "diese Checkliste neben jedes neue Diagramm.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Restarbeit", "icon": "stack", "with": 0},
        {"label": "Verfügbare Zeit", "icon": "clock", "with": 1},
        {"label": "Fällt auf null", "icon": "chartDown", "tone": "good", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Nur ein Termin", "sub": "Lücke am Freitag gefunden", "icon": "calendar", "tone": "bad", "with": "example"},
        {"label": "Ein Restarbeitsdiagramm", "sub": "Lücke gesehen, solange sie klein ist", "icon": "chartDown", "tone": "good", "with": 1}]},
    "p03": {"type": "icons", "items": [
        {"label": "Für alle sichtbar", "icon": "search", "with": 0},
        {"label": "Ist gegenüber Tempo", "icon": "scale", "with": 1},
        {"label": "Frühwarnung", "icon": "warning", "with": 2},
        {"label": "Fakten, keine Gefühle", "icon": "clipboard", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Restarbeit", "sub": "Senkrechte Achse", "icon": "stack", "with": 0},
        {"label": "Zeit", "sub": "Waagerechte Achse", "icon": "calendar", "with": 0},
        {"label": "Ideallinie", "icon": "chartDown", "with": 1},
        {"label": "Istlinie", "icon": "pin", "with": 2},
        {"label": "Lücke", "icon": "scale", "tone": "bad", "with": 3}]},
    "p05": {"type": "stat", "value": 1000, "icon": "box", "label": "Router im Umlauf",
            "unit": "5 Arbeitstage bis zum Lkw", "with": 0},
    "p06": {"type": "bars", "label": "", "note": "Ideallinie: jeden Tag 200 Router weniger", "with": "example", "items": [
        {"label": "Tag 0", "value": 1000, "with": "example"},
        {"label": "Tag 1", "value": 800, "with": "example"},
        {"label": "Tag 2", "value": 600, "with": "example"},
        {"label": "Tag 3", "value": 400, "with": "example"},
        {"label": "Tag 4", "value": 200, "with": "example"},
        {"label": "Tag 5", "value": 0, "tone": "good", "with": "example"}]},
    "p07": {"type": "bars", "label": "", "note": "Router übrig, Ende von Tag 2: 80 hinter dem Plan", "items": [
        {"label": "Ideal", "value": 600, "tone": "good", "with": 1},
        {"label": "Ist", "value": 680, "tone": "bad", "with": 1}]},
    "p08": {"type": "versus", "items": [
        {"label": "Über der Ideallinie", "sub": "Im Rückstand: Engpass finden", "icon": "chartUp", "tone": "bad", "with": 0},
        {"label": "Unter der Ideallinie", "sub": "Im Vorsprung: Qualität bestätigen", "icon": "chartDown", "tone": "good", "with": 1}]},
    "p09": {"type": "flow", "items": [
        {"label": "Flache Linie", "sub": "Nichts abgeschlossen", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Stillstand? Verantwortlicher? Daten?", "icon": "search", "with": 1},
        {"label": "Bei null: prüfen, abschließen", "icon": "check", "tone": "good", "with": 2}]},
    "p10": {"type": "steps", "items": [
        {"label": "Aktualisieren", "with": 0}, {"label": "Vergleichen", "with": 0},
        {"label": "Erklären", "with": 1}, {"label": "Handeln", "with": 2},
        {"label": "Bestätigen", "with": 3}]},
    "p11": {"type": "flow", "items": [
        {"label": "RF-Tester ausgefallen", "icon": "test", "tone": "bad", "with": 0},
        {"label": "Zweiter Tester in Betrieb", "icon": "wrench", "with": 1},
        {"label": "Ein Verantwortlicher für das Diagramm", "icon": "person", "with": 2}],
        "then": {"type": "stat", "value": 0, "icon": "check", "label": "Router übrig am Freitag",
                 "unit": "ein paar Stunden vor dem Lkw", "with": "example"}},
    "p12": {"type": "icons", "items": [
        {"label": "Umlauf", "icon": "box", "with": 1},
        {"label": "Unterdeckung aufholen", "icon": "chartUp", "with": 1},
        {"label": "Kritische Fehler", "icon": "warning", "with": 2},
        {"label": "Instandhaltung, Kaizen", "icon": "wrench", "with": 3}]},
    "p13": {"type": "icons", "items": [
        {"label": "Eine Einheit, eingefrorener Start", "icon": "lock", "with": 0},
        {"label": "„Fertig“ definiert", "icon": "clipboard", "with": 1},
        {"label": "Nur gute Menge", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Wartet auf Nachtest", "sub": "Nicht fertig", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Bestanden und verpackt", "sub": "Zählt", "icon": "check", "tone": "good", "with": "example"}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Startmenge verschoben", "icon": "stack", "tone": "bad", "with": 0},
        {"label": "Späte Aktualisierungen", "icon": "clock", "tone": "bad", "with": 1},
        {"label": "Teilweise oder abgelehnt", "icon": "trash", "tone": "bad", "with": 2},
        {"label": "Keine Maßnahmen", "icon": "cross", "tone": "bad", "with": 3}]},
    "p15": {"type": "doc", "items": [
        {"label": "Arbeit und „fertig“ definieren", "icon": "clipboard", "with": 2},
        {"label": "Startmenge und Termin bestätigen", "icon": "calendar", "with": 2},
        {"label": "Ideales Tempo, ein Verantwortlicher", "icon": "person", "with": 2},
        {"label": "Aktualisieren, handeln, erst bei null abschließen", "icon": "check", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "800 Einheiten müssen in 4 Tagen erledigt sein. Nach Tag 2 sind 340 fertig. Wo steht das "
                    "Team?",
        "options": ["60 Einheiten vor dem Plan", "60 Einheiten hinter dem Plan", "Genau im Plan"],
        "correct": 1,
        "explanation": "Ideal übrig an Tag 2 = 800 − 2 × 200 = 400. Tatsächlich übrig = 800 − 340 = 460. 460 − "
                       "400 = 60 hinter dem Plan.",
        "q_script": "Kurzer Check. Achthundert Einheiten müssen in vier Tagen erledigt sein. Nach Tag zwei "
                    "sind dreihundertvierzig fertig. Wo steht das Team? Nehmen Sie sich ein paar Sekunden.",
        "a_script": "Es ist sechzig Einheiten im Rückstand. Vierhundert sollten übrig sein, aber es sind noch "
                    "vierhundertsechzig. Die Istlinie liegt über der Ideallinie.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Ein Restarbeitsdiagramm für Fehler ist seit zwei Tagen flach. Was sollte das Team zuerst "
                    "prüfen?",
        "options": ["Nichts: eine flache Linie bedeutet, dass alles stabil ist",
                    "Ob die Arbeit stillstand, wer verantwortlich ist, und ob die Daten aktualisiert wurden",
                    "Die Ideallinie an die Realität anpassen"],
        "correct": 1,
        "explanation": "Eine flache Linie bedeutet, dass nichts abgeschlossen wurde. Prüfen Sie auf Stillstand, "
                       "den Verantwortlichen und die Daten. Die Ideallinie neu zu zeichnen versteckt nur die "
                       "Lücke.",
        "q_script": "Noch eine, ein Szenario. Ein Fehler-Restarbeitsdiagramm ist seit zwei Tagen flach. Was "
                    "prüft das Team zuerst? Überlegen Sie kurz.",
        "a_script": "Prüfen Sie, ob die Arbeit stillstand, wer verantwortlich ist, und ob jemand die Daten "
                    "aktualisiert hat. Die Ideallinie neu zu zeichnen würde nur die Lücke verstecken.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
