"""cycle_time_study in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh cycle_time_study_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ct_de"
NAME = "cycle_time_study_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Cycle Time Study": "Saikel Taim Stadi",
    "Design Thinking": "Disain Sinking",
    "Gemba": "Gemba",
    "TAKT": "Takt",
    "ECRS": "e ze err ess",
    "UPH": "u pe ha",
    "FPY": "eff pe üpsilon",
    "SOP": "ess o pe",
    "ESD": "e ess de",
    "A": "a",
    "C": "ze",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Laut Bericht war jede Station schneller als vierundzwanzig Sekunden. Trotzdem verfehlte "
    "die Monitorlinie ihr Stundenziel, Schicht um Schicht. Wessen Zahlen waren also falsch? "
    "Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie die Cycle Time Study kennen. "
    "Sie sehen, wie man eine Station richtig misst, den echten Engpass findet und ihn behebt, "
    "ohne Menschen anzutreiben. Wir begleiten Imran, Prozessingenieur an einer "
    "Monitor-Montagelinie."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Legen Sie zuerst die Grenze fest, sonst sind Ihre Zahlen "
    "nicht vergleichbar. Schauen Sie auf die Streuung, nicht nur auf den Durchschnitt. Und "
    "verbessern Sie die Methode am Engpass, nie durch ausgelassene Qualitätsprüfungen. Ihre "
    "Aufgabe für diese Woche. Messen Sie zehn Zyklen an einer Station, und vergleichen Sie "
    "den längsten mit dem TAKT. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie "
    "Design Thinking kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Zykluszeit ist",
        "points": [("Zeit zwischen fertigen Einheiten", "die Zeit zwischen"),
                   ("An einer festgelegten Grenze", "an einer Grenze, die Sie festlegen"),
                   ("Unter genannten Bedingungen", "unter Bedingungen, die Sie nennen")],
        "example": "Laut Bericht brauchte Station C 21 Sekunden. Imrans Stoppuhr sagte 28.",
        "example_cue": "Laut Bericht brauchte",
        "script": "Beginnen wir mit einer klaren Definition. Zykluszeit ist die Zeit zwischen einer "
                  "fertigen Einheit und der nächsten. Sie wird gemessen an einer Grenze, die Sie festlegen, "
                  "unter Bedingungen, die Sie nennen. Klingt einfach? Ist es nicht. Laut Bericht brauchte "
                  "die Display-Teststation einundzwanzig Sekunden. Imran stand mit einer Stoppuhr da und "
                  "maß achtundzwanzig. Beide Zahlen waren ehrlich. Wie können beide stimmen?",
    },
    {
        "key": "p02", "num": 2, "title": "Grenzen sind wichtig",
        "points": [("Manuelle Zeit: Handarbeit", "Manuelle Zeit ist"),
                   ("Maschinenzeit: Test, Dosieren, Aushärten", "Maschinenzeit läuft"),
                   ("Stationszyklus: der echte Wiederholabstand", "Der Stationszyklus"),
                   ("Gleiche Grenze, sonst kein Vergleich", "Wenn zwei Teams")],
        "example": "Die 21 Sekunden kamen aus alten Standardzeiten. Die 28 Sekunden waren der echte Abstand "
                   "von Einheit zu Einheit.",
        "example_cue": "Der Bericht nutzte",
        "script": "Weil sie Verschiedenes gemessen haben. Manuelle Zeit ist Handarbeit, wie Schrauben und "
                  "Stecken. Maschinenzeit läuft automatisch, wie ein Test oder das Aushärten. Der "
                  "Stationszyklus ist der echte Wiederholabstand, mit Überlappung. Sie können sie nicht "
                  "einfach addieren. Der Bericht nutzte alte Standardzeiten, ohne Wiederholungen oder "
                  "Warten. Imran maß von einem fertigen Monitor zum nächsten. Wenn zwei Teams verschiedene "
                  "Grenzen nutzen, sind ihre Zahlen nicht vergleichbar. Welche Zahl zählt für Ihren Kunden?",
    },
    {
        "key": "p03", "num": 3, "title": "Zykluszeit gegenüber TAKT, Durchlaufzeit, UPH",
        "points": [("Zykluszeit: wie oft Sie eine fertigstellen", "Die Zykluszeit fragt"),
                   ("TAKT: das Tempo, das die Nachfrage braucht", "Der TAKT fragt"),
                   ("Durchlaufzeit: Auftrag bis fertig, mit Warten", "Die Durchlaufzeit ist"),
                   ("UPH: gute Einheiten pro Stunde", "Die UPH zählt")],
        "example": "Imrans Linie: TAKT 24 Sekunden, also 150 Monitore pro Stunde nötig.",
        "example_cue": "An Imrans Linie",
        "script": "Vier Größen klingen ähnlich, beantworten aber verschiedene Fragen. Die Zykluszeit fragt, "
                  "wie oft stellen Sie eine fertig? Der TAKT fragt, welches Tempo braucht die Nachfrage? "
                  "Die Durchlaufzeit ist der ganze Weg, vom Auftrag bis fertig, mit Warten. Sie kann Tage "
                  "dauern, auch wenn Ihr Zyklus Sekunden dauert. Die UPH zählt gute Einheiten pro Stunde. "
                  "An Imrans Linie ist der TAKT vierundzwanzig Sekunden. Das sind hundertfünfzig Monitore "
                  "pro Stunde. Welche davon verfolgen Sie?",
    },
    {
        "key": "p04", "num": 4, "title": "Vergleich mit dem TAKT",
        "points": [("Über dem TAKT: Kapazitätslücke", "Liegt die Zykluszeit über"),
                   ("Gleich dem TAKT: kein Puffer", "Ist sie gleich"),
                   ("Unter dem TAKT: Puffer, keine Überproduktion", "Liegt sie darunter")],
        "example": "Station C liegt mit 28 Sekunden 4 Sekunden über einem TAKT von 24 Sekunden.",
        "example_cue": "Imrans Display-Teststation",
        "script": "Vergleichen Sie jetzt Ihren Zyklus mit dem TAKT. Liegt die Zykluszeit über dem TAKT, "
                  "kommt die Station nicht mit. Ihnen fehlt Kapazität. Ist sie gleich, haben Sie keinen "
                  "Raum für Störungen. Liegt sie darunter, haben Sie Puffer. Aber nutzen Sie ihn nicht zum "
                  "Überproduzieren. Imrans Display-Teststation lag bei achtundzwanzig Sekunden. Das sind "
                  "vier Sekunden über dem TAKT, in jedem Zyklus. Wie machen Sie eine Studie, der Sie trauen "
                  "können?",
    },
    {
        "key": "p05", "num": 5, "title": "Die Studie vorbereiten",
        "points": [("Ein klarer Zweck und eine Station", "Wählen Sie die Station"),
                   ("Bedingungen notieren", "Notieren Sie die Bedingungen"),
                   ("Nur normale Zyklen, Störungen erfasst", "Trennen Sie Anlauf"),
                   ("Dem Werker erklären", "Und sagen Sie dem Werker")],
        "example": "Imrans Zweck: den Wiederholabstand von Station C messen, um die Kapazität gegen den TAKT "
                   "zu prüfen.",
        "example_cue": "Imrans Zweck war",
        "script": "Eine gute Studie beginnt mit einem Zweck. Wählen Sie die Station, etwa einen vermuteten "
                  "Engpass oder eine stark schwankende. Notieren Sie die Bedingungen. Modell, Werker, "
                  "Schicht und Werkzeuge. Trennen Sie Anlauf, Umrüsten und Nacharbeit von normalen Zyklen. "
                  "Und sagen Sie dem Werker, warum Sie da sind. Sie untersuchen den Prozess, nicht ihn. "
                  "Imrans Zweck war ein Satz. Station C gegen den TAKT prüfen. Bereit, die Arbeit zu "
                  "zerlegen?",
    },
    {
        "key": "p06", "num": 6, "title": "Die Elemente zerlegen",
        "points": [("Arbeit in sichtbare Elemente teilen", "Teilen Sie die Arbeit"),
                   ("Klarer Start und klares Ende für jedes", "Jedes Element braucht"),
                   ("Warten getrennt erfassen", "Erfassen Sie Warten getrennt"),
                   ("Nie Qualitäts- oder Sicherheitsprüfungen streichen", "Streichen Sie nie")],
        "example": "Station C: Laden 4 s, Etikett scannen 3 s, Displaytest 13 s, Seriennummer 4 s, Entladen "
                   "3 s, Warten 1 s.",
        "example_cue": "Imran teilte Station C",
        "script": "Teilen Sie die Arbeit in kleine Elemente, die Sie wirklich sehen. Jedes Element braucht "
                  "einen klaren Start und ein klares Ende, damit nichts doppelt zählt. Erfassen Sie Warten "
                  "getrennt von der Arbeitszeit. Dann ordnen Sie jeden Schritt ein: wertschöpfend, "
                  "notwendig oder reine Verschwendung. Streichen Sie nie eine vorgeschriebene Qualitäts- "
                  "oder Sicherheitsprüfung. Imran teilte Station C in sechs Teile. Laden, Etikett scannen, "
                  "Displaytest, Seriennummer, Entladen und etwas Warten. Wo würden Sie zuerst hinschauen?",
    },
    {
        "key": "p07", "num": 7, "title": "Der Zeitaufnahmebogen",
        "points": [("Wiederholte Zyklen messen, nicht einen", "Messen Sie viele Zyklen"),
                   ("Durchschnitt: 28 s. Spanne: 26 bis 32 s", "Der Durchschnitt war"),
                   ("Jeden auffälligen Zyklus erfassen", "Erfassen Sie jeden auffälligen")],
        "example": "Der längste Zyklus: 32 Sekunden, als der Etikettenscan zweimal scheiterte.",
        "example_cue": "Der längste Zyklus",
        "script": "Trauen Sie nie einem einzigen schönen Zyklus. Messen Sie viele Zyklen hintereinander. "
                  "Imran maß zehn. Der Durchschnitt war achtundzwanzig Sekunden. Aber die Streuung reichte "
                  "von sechsundzwanzig bis zweiunddreißig. Erfassen Sie jeden auffälligen Zyklus mit Grund, "
                  "nicht nur die Zahl. Der längste Zyklus kam, als der Etikettenscan zweimal scheiterte. "
                  "Ein Durchschnitt allein hätte das versteckt. Was versteckt Ihr längster Zyklus?",
    },
    {
        "key": "p08", "num": 8, "title": "Kapazität berechnen",
        "points": [("Stundenleistung = 3.600 ÷ Zykluszeit", "Die Stundenleistung ist"),
                   ("Station C: etwa 129 pro Stunde", "Bei achtundzwanzig Sekunden"),
                   ("Nötige Stationen = Arbeitsinhalt ÷ TAKT", "Um zu wissen, wie viele")],
        "example": "Die Nachfrage braucht 150 pro Stunde. Station C schafft etwa 129. Das ist die Lücke.",
        "example_cue": "Die Nachfrage braucht",
        "script": "Machen Sie jetzt aus Zeit Kapazität. Die Stundenleistung ist die Sekundenzahl einer "
                  "Stunde, geteilt durch Ihre Zykluszeit. Bei achtundzwanzig Sekunden schafft Station C "
                  "etwa hundertneunundzwanzig Monitore pro Stunde. Die Nachfrage braucht hundertfünfzig. "
                  "Das ist die Lücke, in klaren Zahlen. Um zu wissen, wie viele Stationen Sie brauchen, "
                  "teilen Sie den Arbeitsinhalt durch den TAKT und runden auf. Nennen Sie jede Annahme. "
                  "Nutzt Ihr Plan die Nettozeit, nach Pausen?",
    },
    {
        "key": "p09", "num": 9, "title": "Streuung zählt",
        "points": [("Durchschnitte verstecken lange Zyklen", "Durchschnitte verstecken"),
                   ("Zyklen in zeitlicher Folge darstellen", "Tragen Sie Ihre Zyklen"),
                   ("Lange Zyklen nie löschen, um gut auszusehen", "Löschen Sie nie"),
                   ("Streuung und % über dem TAKT berichten", "Berichten Sie die typische Zeit")],
        "example": "Station C: 3 von 10 Zyklen dauerten 30 Sekunden oder länger.",
        "example_cue": "An Station C",
        "script": "Hier ist eine Falle. Zwei Stationen können denselben Durchschnitt haben und sich ganz "
                  "anders verhalten. Durchschnitte verstecken die langen Zyklen, die Warteschlangen bilden. "
                  "Tragen Sie Ihre Zyklen also in zeitlicher Folge auf. Trennen Sie nach Modell und "
                  "Schicht, bevor Sie sie zusammenfassen. Löschen Sie nie lange Zyklen, nur um den "
                  "Durchschnitt zu verbessern. Untersuchen Sie sie. Berichten Sie die typische Zeit, die "
                  "Streuung und wie oft Sie über dem TAKT liegen. An Station C dauerten drei von zehn "
                  "Zyklen dreißig Sekunden oder länger. Kommt Ihnen das bekannt vor?",
    },
    {
        "key": "p10", "num": 10, "title": "Den Engpass finden",
        "points": [("Die langsamste Station bestimmt das Tempo", "Die langsamste Station"),
                   ("Stau davor, Leerlauf danach", "Suchen Sie einen Stau"),
                   ("Zuerst den Engpass beheben", "Beheben Sie zuerst den Engpass")],
        "example": "Stationen A 19 s, B 22 s, C 28 s, D 21 s. Station C begrenzt die Linie.",
        "example_cue": "Imran maß alle vier",
        "script": "Welche Station begrenzt Ihre Linie wirklich? Meist bestimmt die langsamste Station das "
                  "Tempo. Suchen Sie einen Stau davor und Menschen, die danach warten. Imran maß alle vier "
                  "Stationen. Fuß und Abdeckung, Platine, Displaytest und Verpackung. Nur der Displaytest "
                  "lag über dem TAKT. Beheben Sie zuerst den Engpass. Jede andere Station zu beschleunigen, "
                  "stapelt nur mehr Umlauf. Warum war Station C also langsam?",
    },
    {
        "key": "p11", "num": 11, "title": "Warum ist sie langsam?",
        "points": [("Hingehen und schauen: die echte Station", "Imran ging an den Gemba"),
                   ("Methode, Konstruktion, Maschine oder Warten?", "Eine langsame Station kann"),
                   ("Wiederholungen, Alarme und Zeitstempel prüfen", "Er prüfte")],
        "example": "Wiederholte Etikettenscans, und eine Seriennummer, die direkt an der Teststation "
                   "aufgeklebt wurde.",
        "example_cue": "Er fand zwei Dinge",
        "script": "Imran ging an den Gemba und beobachtete die echte Station. Eine langsame Station kann "
                  "ein Methodenproblem, ein Konstruktionsproblem, eine langsame Maschine oder einfach "
                  "Warten sein. Jedes braucht eine andere Lösung. Er prüfte Scanwiederholungen, Alarmcodes "
                  "und Testzeitstempel. Er fand zwei Dinge. Die Etiketten saßen schief, also verfehlte der "
                  "Scanner oft. Und der Werker klebte die Seriennummer auch noch dort auf, im Zyklus. Was "
                  "würden Sie versuchen?",
    },
    {
        "key": "p12", "num": 12, "title": "Die Methode verbessern",
        "points": [("Eliminieren, Kombinieren, Umordnen, Vereinfachen", "Denken Sie an ECRS"),
                   ("Zuerst einfache, günstige Lösungen", "Dann suchen Sie"),
                   ("Nie Tests auslassen, um Zeit zu sparen", "Aber kürzen Sie nie einen Zyklus")],
        "example": "Eine Etikettenführung richtet jedes Etikett gerade aus. Der Scanner liest beim ersten "
                   "Mal.",
        "example_cue": "Imran ergänzte",
        "script": "Verbessern Sie die Methode, bevor Sie jemanden zum Tempo drängen. Denken Sie an ECRS. "
                  "Eliminieren, kombinieren, umordnen, vereinfachen. Dann suchen Sie einfache Lösungen, wie "
                  "Führungen, Zuführungen und Barcode-Prüfungen. Aber kürzen Sie nie einen Zyklus, indem "
                  "Sie einen Test, eine Drehmomentprüfung oder den ESD-Schutz auslassen. Imran ergänzte "
                  "eine kleine Etikettenführung. Jedes Etikett sitzt jetzt gerade, und der Scanner liest "
                  "beim ersten Mal. Und die Seriennummer?",
    },
    {
        "key": "p13", "num": 13, "title": "Die Linie neu austakten",
        "points": [("Arbeit zu Stationen mit freier Zeit verschieben", "Verschieben Sie Arbeit"),
                   ("Reihenfolge, Qualifikation und Prüfungen halten", "Prüfen Sie die Reihenfolge"),
                   ("Keine neuen Wege, kein ergonomisches Risiko", "Und stellen Sie sicher")],
        "example": "Seriennummer an Station A verlegt: A 23 s, C 23 s. Jede Station liegt jetzt unter dem "
                   "TAKT.",
        "example_cue": "Imran verlegte die Seriennummer",
        "script": "Takten Sie als Nächstes die Linie neu aus. Verschieben Sie Arbeit zu Stationen mit "
                  "freier Zeit, aber nur, wenn es sicher ist. Prüfen Sie die Reihenfolge, die Werkzeuge, "
                  "die Qualifikation und die Prüfungen an der neuen Station. Und stellen Sie sicher, dass "
                  "Sie keine Wege, Belastung oder Fehlerrisiken hinzufügen. Imran verlegte die Seriennummer "
                  "an Station A. Station A kam auf dreiundzwanzig Sekunden. Station C fiel auf "
                  "dreiundzwanzig. Jede Station liegt jetzt unter dem TAKT. Ist die Geschichte damit zu "
                  "Ende?",
    },
    {
        "key": "p14", "num": 14, "title": "Beweisen, dann standardisieren",
        "points": [("Versuch über Schichten und Modelle", "Führen Sie den Versuch"),
                   ("Streuung, FPY und Menge vergleichen", "Vergleichen Sie die Streuung"),
                   ("Standardarbeit aktualisieren und schulen", "aktualisieren Sie die Standardarbeit"),
                   ("Abweichungen schnell eskalieren", "Setzen Sie einen Auslöser")],
        "example": "Auslöser: 3 Zyklen hintereinander über dem TAKT, dann prüft der Teamleiter die Station.",
        "example_cue": "Imrans Auslöser",
        "script": "Noch nicht. Ein schneller Morgen beweist nichts. Führen Sie den Versuch über Schichten "
                  "und Modelle. Vergleichen Sie die Streuung, die Erstdurchlaufquote und die Menge, nicht "
                  "nur den Durchschnitt. Hält die Qualität, aktualisieren Sie die Standardarbeit und "
                  "schulen jede Schicht. Setzen Sie einen Auslöser, damit Abweichungen schnell auffallen. "
                  "Imrans Auslöser war einfach. Drei Zyklen hintereinander über dem TAKT, und der "
                  "Teamleiter prüft die Station. Wer würde Ihre prüfen?",
    },
    {
        "key": "p15", "num": 15, "title": "Ihr 30-Tage-Plan",
        "points": [("Woche 1: definieren und Ausgangslage messen", "In Woche eins"),
                   ("Woche 2: den Engpass finden", "In Woche zwei"),
                   ("Woche 3: eine Maßnahme testen", "In Woche drei"),
                   ("Woche 4: prüfen, standardisieren, schulen", "In Woche vier")],
        "example": "Imrans Linie schafft jetzt 150 Monitore pro Stunde, bei unveränderter "
                   "Erstdurchlaufquote.",
        "example_cue": "Imrans Linie schafft jetzt",
        "script": "Jetzt sind Sie dran. Hier ist ein einfacher Dreißig-Tage-Plan. In Woche eins legen Sie "
                  "die Grenze einer Station fest und messen mindestens zehn Zyklen. In Woche zwei finden "
                  "Sie den Engpass und seine Ursachen. In Woche drei testen Sie eine Maßnahme. In Woche "
                  "vier prüfen Sie sie, aktualisieren die SOP und schulen. Imrans Linie schafft jetzt ihre "
                  "hundertfünfzig pro Stunde, und die Erstdurchlaufquote hat sich nicht bewegt. Welche "
                  "Station messen Sie zuerst?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Von Einheit zu Einheit", "icon": "sequence", "with": 0},
        {"label": "Festgelegte Grenze", "icon": "pin", "with": 1},
        {"label": "Genannte Bedingungen", "icon": "clipboard", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "21 s", "sub": "Der Bericht", "icon": "clipboard", "with": "example"},
            {"label": "28 s", "sub": "Imrans Stoppuhr", "icon": "clock", "with": "example"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Manuell", "sub": "Handarbeit", "icon": "hand", "with": 0},
        {"label": "Maschine", "sub": "Test, Dosieren, Aushärten", "icon": "gear", "with": 1},
        {"label": "Stationszyklus", "sub": "Echter Wiederholabstand", "icon": "clock", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Alte Standardzeiten", "sub": "21 Sekunden", "icon": "clipboard", "with": "example"},
            {"label": "Von Einheit zu Einheit", "sub": "28 Sekunden", "icon": "sequence", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Zykluszeit", "sub": "Wie oft Sie fertigstellen", "icon": "clock", "with": 0},
        {"label": "TAKT", "sub": "Tempo, das die Nachfrage braucht", "icon": "wave", "with": 1},
        {"label": "Durchlaufzeit", "sub": "Auftrag bis fertig", "icon": "calendar", "with": 2},
        {"label": "UPH", "sub": "Gute Einheiten pro Stunde", "icon": "count", "with": 3}],
        "then": {"type": "stat", "value": 150, "icon": "count", "label": "Monitore pro Stunde nötig",
                 "unit": "TAKT 24 Sekunden", "with": "example"}},
    "p04": {"type": "ladder", "top": "KAPAZITÄTSLÜCKE", "bottom": "PUFFER", "items": [
        {"label": "Über dem TAKT", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Gleich dem TAKT", "icon": "scale", "with": 1},
        {"label": "Unter dem TAKT", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
            {"label": "Station C", "value": 28, "tone": "bad", "with": "example"}]}},
    "p05": {"type": "flow", "items": [
        {"label": "Zweck und Station", "icon": "pin", "with": 0},
        {"label": "Bedingungen", "icon": "clipboard", "with": 1},
        {"label": "Nur normale Zyklen", "icon": "clock", "with": 2},
        {"label": "Dem Werker erklären", "icon": "person", "tone": "good", "with": 3}]},
    "p06": {"type": "bars", "label": "", "note": "Elemente von Station C: insgesamt 28 s", "with": "example", "items": [
        {"label": "Laden", "value": 4, "with": "example"},
        {"label": "Scannen", "value": 3, "with": "example"},
        {"label": "Test", "value": 13, "with": "example"},
        {"label": "Seriennummer", "value": 4, "with": "example"},
        {"label": "Entladen", "value": 3, "with": "example"},
        {"label": "Warten", "value": 1, "tone": "bad", "with": "example"}]},
    "p07": {"type": "bars", "label": "", "note": "Zehn gemessene Zyklen an Station C (Sekunden)", "items": [
        {"label": "Schnellster", "value": 26, "tone": "good", "with": 1},
        {"label": "Durchschnitt", "value": 28, "with": 1},
        {"label": "Langsamster", "value": 32, "tone": "bad", "with": "example"}]},
    "p08": {"type": "compare", "before": {"label": "Station C", "value": 129}, "after": {"label": "Nachfrage", "value": 150},
            "unit": "Monitore pro Stunde", "note": "3,600 ÷ 28 ≈ 129", "with": 1},
    "p09": {"type": "icons", "items": [
        {"label": "Durchschnitte verstecken", "icon": "search", "tone": "bad", "with": 0},
        {"label": "Zeitliche Folge", "icon": "chartUp", "with": 1},
        {"label": "Lange Zyklen behalten", "icon": "lock", "with": 2},
        {"label": "Streuung, % über dem TAKT", "icon": "scale", "with": 3}],
        "then": {"type": "stat", "value": 3, "suffix": " / 10", "icon": "clock", "label": "Zyklen mit 30 Sekunden oder mehr",
                 "unit": "Station C", "with": "example"}},
    "p10": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
        {"label": "A", "value": 19, "with": "example"},
        {"label": "B", "value": 22, "with": "example"},
        {"label": "C", "value": 28, "tone": "bad", "with": "example"},
        {"label": "D", "value": 21, "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Methode", "icon": "clipboard", "with": 1},
        {"label": "Konstruktion", "icon": "shape", "with": 1},
        {"label": "Maschine", "icon": "gear", "with": 1},
        {"label": "Warten", "icon": "clock", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Etiketten schief", "icon": "label", "tone": "bad", "with": "example"},
            {"label": "Scanwiederholungen", "icon": "barcode", "tone": "bad", "with": "example"},
            {"label": "Seriennummer im Zyklus", "icon": "sticker", "tone": "bad", "with": "example"}]}},
    "p12": {"type": "steps", "items": [
        {"label": "Eliminieren", "with": 0}, {"label": "Kombinieren", "with": 0},
        {"label": "Umordnen", "with": 0}, {"label": "Vereinfachen", "with": 0}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Vorher", "sub": "Etiketten schief, Scanwiederholungen", "icon": "barcode", "tone": "bad", "with": "example"},
            {"label": "Etikettenführung", "sub": "Liest beim ersten Mal", "icon": "check", "tone": "good", "with": "example"}]}},
    "p13": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
        {"label": "A", "value": 23, "with": "example"},
        {"label": "B", "value": 22, "with": "example"},
        {"label": "C", "value": 23, "tone": "good", "with": "example"},
        {"label": "D", "value": 21, "with": "example"}]},
    "p14": {"type": "flow", "items": [
        {"label": "Versuch: Schichten, Modelle", "icon": "calendar", "with": 0},
        {"label": "Streuung, FPY, Menge", "icon": "chartUp", "with": 1},
        {"label": "Standardarbeit, Schulung", "icon": "clipboard", "with": 2},
        {"label": "Auslöser: 3 über dem TAKT", "icon": "warning", "tone": "good", "with": "example"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Definieren und Ausgangslage messen", "sub": "Woche 1", "icon": "clock", "with": 0},
        {"label": "Engpass", "sub": "Woche 2", "icon": "search", "with": 1},
        {"label": "Versuch", "sub": "Woche 3", "icon": "wrench", "with": 2},
        {"label": "Standardisieren", "sub": "Woche 4", "icon": "check", "tone": "good", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Die Zykluszeit einer Station beträgt 30 Sekunden. Wie hoch ist ihre theoretische "
                    "Leistung pro Stunde?",
        "options": ["90 Einheiten", "120 Einheiten", "180 Einheiten"],
        "correct": 1,
        "explanation": "Stundenleistung = 3.600 ÷ Zykluszeit = 3.600 ÷ 30 = 120 Einheiten pro Stunde, vor allen "
                       "Verlusten.",
        "q_script": "Kurzer Check. Die Zykluszeit einer Station beträgt dreißig Sekunden. Wie hoch ist ihre "
                    "theoretische Leistung pro Stunde? Nehmen Sie sich kurz Zeit.",
        "a_script": "Hundertzwanzig. Teilen Sie die Sekunden einer Stunde durch die Zykluszeit, und denken "
                    "Sie daran, das ist vor allen Verlusten.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Nach einer Änderung sinkt die Zykluszeit einer Station von 28 auf 22 Sekunden, aber die "
                    "Erstdurchlaufquote fällt. Was nun?",
        "options": ["Standardisieren: die Station ist schneller",
                    "Die Änderung stoppen und klären, warum die Qualität sank",
                    "Einen Endprüfer ergänzen, der die Fehler abfängt"],
        "correct": 1,
        "explanation": "Ein schnellerer Zyklus mit mehr Fehlern ist keine Verbesserung. Stoppen Sie die "
                       "Änderung, klären Sie, warum die Quote sank, und standardisieren Sie erst, wenn die "
                       "Qualität hält.",
        "q_script": "Noch eine, diesmal ein Szenario. Nach einer Änderung ist eine Station sechs Sekunden "
                    "schneller. Aber die Erstdurchlaufquote fällt. Was sollte das Team tun? Überlegen Sie "
                    "kurz.",
        "a_script": "Stoppen Sie die Änderung, und klären Sie, warum die Qualität sank. Ein schnellerer "
                    "Zyklus mit mehr Fehlern ist überhaupt keine Verbesserung.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
