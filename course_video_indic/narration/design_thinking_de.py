"""design_thinking in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh design_thinking_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "dt_de"
NAME = "design_thinking_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Elimination of Waste": "Elimineeschen of Weest",
    "Design Thinking": "Disain Sinking",
    "Poka Yoke": "Poka Joke",
    "SCAMPER": "Skämper",
    "Kaizen": "Kaisen",
    "Gemba": "Gemba",
    "TAKT": "Takt",
    "A3": "a drei",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Die Verpackungslinie verfehlte ständig ihr Ziel. Falsche Etiketten rutschten immer "
    "wieder durch. Die erste Idee war ein schnellerer Drucker, für viel Geld. Niemand hatte "
    "die Packer gefragt. Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie Design "
    "Thinking kennen. Sie sehen, wie man die Menschen versteht, die die Arbeit machen, das "
    "richtige Problem löst und Ideen günstig testet. Wir begleiten Pooja, "
    "Verbesserungsingenieurin in einem Werk für Medizinprodukte."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Beginnen Sie bei den Menschen, die die Arbeit machen, und "
    "beobachten Sie, bevor Sie entscheiden. Definieren Sie den Bedarf, ohne eine Lösung darin "
    "zu verstecken. Und testen Sie klein, mit Ergebnissen und echter Nutzung. Ihre Aufgabe "
    "für diese Woche. Beobachten Sie zehn Zyklen einer mühsamen Arbeit, und sprechen Sie mit "
    "drei Menschen, die sie machen. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen "
    "Sie Elimination of Waste kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Design Thinking ist",
        "points": [("Bei den Menschen im Prozess beginnen", "der bei den Menschen"),
                   ("Verstehen, definieren, Ideen finden", "Sie fühlen sich ein"),
                   ("Prototyp bauen und testen, dann wiederholen", "Dann bauen Sie einen kleinen Prototyp")],
        "example": "Poojas Packstation: Infusionspumpen, Etiketten, und Packer, die niemand gefragt hatte.",
        "example_cue": "Poojas Aufgabe",
        "script": "Design Thinking ist ein Weg, Probleme zu lösen, der bei den Menschen im Prozess beginnt. "
                  "Bei denen, die die Arbeit machen, unterstützen oder empfangen. Sie fühlen sich ein, "
                  "indem Sie echte Arbeit beobachten. Sie definieren den echten Bedarf und finden viele "
                  "Ideen. Dann bauen Sie einen kleinen Prototyp, testen ihn und lernen. Und wiederholen. "
                  "Poojas Aufgabe war die Packstation für Infusionspumpen. Wie passt das zu Lean?",
    },
    {
        "key": "p02", "num": 2, "title": "Design Thinking und Lean",
        "points": [("Ersetzt keine Lean-Werkzeuge", "Es ersetzt nicht A3"),
                   ("Findet zuerst das richtige Problem", "Es hilft Ihnen"),
                   ("Menschen übernehmen, was sie mitgestalten", "Menschen übernehmen")],
        "example": "Die neue Packmethode vom letzten Jahr hielt zwei Wochen. Die Packer kehrten zur alten "
                   "Art zurück.",
        "example_cue": "Letztes Jahr",
        "script": "Es ersetzt nicht A3, Kaizen oder Poka Yoke. Es hilft Ihnen, das richtige Problem zu "
                  "finden, bevor Sie eines davon wählen. Lean beseitigt Verschwendung. Design Thinking "
                  "stellt sicher, dass die Änderung zu echten Menschen und echter Arbeit passt. Und der "
                  "Bonus: Menschen übernehmen, was sie mitgestaltet haben. Letztes Jahr hielt eine neue "
                  "Packmethode zwei Wochen. Dann kehrten die Packer still zur alten Art zurück. Warum, "
                  "glauben Sie?",
    },
    {
        "key": "p03", "num": 3, "title": "Arbeitsprinzipien",
        "points": [("Beobachten, ohne anzunehmen", "Beobachten Sie, ohne anzunehmen"),
                   ("Fakten von Meinungen trennen", "Trennen Sie Fakten"),
                   ("Klein testen vor großen Änderungen", "Testen Sie Ideen klein"),
                   ("Ergebnisse und Akzeptanz messen", "Messen Sie beides")],
        "example": "Poojas Regel: „Zeig es mir“ vor „Erzähl es mir“.",
        "example_cue": "Poojas Regel",
        "script": "Ein paar Prinzipien halten Sie ehrlich. Beobachten Sie, ohne anzunehmen, dass Sie die "
                  "Antwort schon kennen. Trennen Sie Fakten von Meinungen und von Lösungsvorschlägen. "
                  "Behandeln Sie Werker und Unterstützungsteams als Ihre Nutzer. Testen Sie Ideen klein, "
                  "bevor Sie den ganzen Prozess ändern. Messen Sie beides, die Ergebnisse und ob Menschen "
                  "die Änderung annehmen. Poojas Regel war einfach. Zeig es mir, vor erzähl es mir. Welches "
                  "davon überspringen Sie am häufigsten?",
    },
    {
        "key": "p04", "num": 4, "title": "Was es verhindert",
        "points": [("Einen kaputten Prozess automatisieren", "Einen kaputten Prozess"),
                   ("Nur das sichtbare Symptom beheben", "Nur das sichtbare"),
                   ("Lösungen, denen niemand folgen kann", "Eine Lösung erzwingen"),
                   ("Viel Geld vor jedem Test", "Viel Geld ausgeben")],
        "example": "Der schnellere Drucker: viel Geld, für ein Problem, das niemand geprüft hatte.",
        "example_cue": "Der schnellere Drucker",
        "script": "Warum der Aufwand? Weil es teure Fehler verhindert. Einen kaputten Prozess "
                  "automatisieren, den Sie nicht verstehen. Nur das sichtbare Symptom beheben. Eine Lösung "
                  "erzwingen, der niemand in einer vollen Schicht folgen kann. Und viel Geld ausgeben, "
                  "bevor eine Annahme getestet ist. Der schnellere Drucker war das perfekte Beispiel. Viel "
                  "Geld, für ein Problem, das niemand geprüft hatte. Welchen Schritten folgen Sie also?",
    },
    {
        "key": "p05", "num": 5, "title": "Fünf Phasen, eine Schleife",
        "points": [("Verstehen · Definieren · Ideen finden", "Verstehen fragt"),
                   ("Prototyp · Test", "Der Prototyp fragt"),
                   ("Erwünscht, machbar, wirtschaftlich", "Eine gute Antwort ist"),
                   ("Mit Belegen weitergehen, nicht mit Meetings", "Gehen Sie zur nächsten Phase")],
        "example": "Poojas Schranke: keine Ideen ohne echte Beobachtungen und eine Ausgangslage.",
        "example_cue": "Pooja setzte eine Schranke",
        "script": "Es gibt fünf Phasen, als Schleife. Verstehen fragt, was die Nutzer erleben. Definieren, "
                  "welches Problem am meisten zählt. Ideen finden, was es lösen könnte. Der Prototyp fragt, "
                  "wie es funktionieren könnte. Der Test, ob es Wert schafft. Eine gute Antwort ist "
                  "erwünscht, machbar und wirtschaftlich. Gehen Sie zur nächsten Phase mit Belegen, nicht "
                  "nach Meetings. Pooja setzte eine Schranke. Keine Ideen ohne Beobachtungen.",
    },
    {
        "key": "p06", "num": 6, "title": "Einfühlen am Gemba",
        "points": [("Über Schichten hinweg beobachten", "Beobachten Sie mehrere Zyklen"),
                   ("Nach dem Beobachten befragen", "Dann stellen Sie offene Fragen"),
                   ("Eine Rolle von Anfang bis Ende begleiten", "Begleiten Sie eine Person"),
                   ("Empathiekarte: sagt, denkt, tut, fühlt", "Eine Empathiekarte")],
        "example": "Pooja beobachtete zehn Zyklen in jeder Schicht und sprach dann mit fünf Packern.",
        "example_cue": "Pooja beobachtete",
        "script": "Einfühlen beginnt am Gemba. Beobachten Sie mehrere Zyklen, in normalen und vollen "
                  "Schichten. Dann stellen Sie offene Fragen, nachdem Sie die Arbeit gesehen haben. "
                  "Begleiten Sie eine Person durch die ganze Arbeit, um die Übergaben zu sehen. Eine "
                  "Empathiekarte hilft beim Ordnen. Was sagen, denken, tun und fühlen sie? Pooja "
                  "beobachtete zehn Zyklen in jeder Schicht. Dann sprach sie mit fünf Packern. Was glauben "
                  "Sie, hat sie gesehen?",
    },
    {
        "key": "p07", "num": 7, "title": "Was Pooja sah",
        "points": [("Laufen, um Etiketten zu holen", "Packer liefen"),
                   ("Zwei ähnliche Etiketten nebeneinander", "Zwei Etiketten, die fast"),
                   ("Auf den Drucker warten", "der Drucker pausierte")],
        "example": "„Ich bin nicht langsam. Ich suche.“ Ein Packer aus der Nachtschicht.",
        "example_cue": "Ein Packer sagte es",
        "script": "Keine langsamen Packer. Die Packer liefen für jedes Etikett zu einem gemeinsamen Regal. "
                  "Zwei Etiketten, die fast gleich aussahen, lagen nebeneinander. Und der Drucker pausierte "
                  "manchmal, also warteten sie. Ein Packer sagte es perfekt. Ich bin nicht langsam. Ich "
                  "suche. Merken Sie, was fehlt? Niemand gab jemandem die Schuld. Das sind Fakten über die "
                  "Arbeit, nicht über Menschen. Wie machen Sie daraus ein lösenswertes Problem?",
    },
    {
        "key": "p08", "num": 8, "title": "Den Bedarf definieren",
        "points": [("Nutzer · Bedarf · Erkenntnis", "Nutzer, einen Bedarf"),
                   ("Keine Lösung in der Aussage", "Sie nennt nicht"),
                   ("Eine messbare Ausgangslage", "Ergänzen Sie eine Ausgangslage")],
        "example": "Packer brauchen das richtige Etikett griffbereit, weil ähnliche Etiketten und Laufwege "
                   "Fehler verursachen. Jetzt: 52 s gegenüber TAKT 45 s, 12 Fehler pro 1.000.",
        "example_cue": "Pooja schrieb",
        "script": "Definieren Sie jetzt den Bedarf. Eine gute Aussage nennt einen Nutzer, einen Bedarf und "
                  "eine Erkenntnis. Sie nennt nicht die Lösung. Pooja schrieb einen Satz. Packer brauchen "
                  "das richtige Etikett griffbereit, weil ähnliche Etiketten und Laufwege Fehler "
                  "verursachen. Ergänzen Sie eine Ausgangslage. Die Station brauchte zweiundfünfzig "
                  "Sekunden, gegenüber einem TAKT von fünfundvierzig. Und zwölf von tausend Pumpen hatten "
                  "einen Etikettenfehler. Sehen Sie den Drucker irgendwo in dieser Aussage?",
    },
    {
        "key": "p09", "num": 9, "title": "Ideen finden: zuerst breit",
        "points": [("Erst schreiben, dann diskutieren", "Brainwriting bedeutet"),
                   ("„Wie könnten wir…?“ fragen", "Stellen Sie Wie-könnten-wir-Fragen"),
                   ("SCAMPER und der Blick auf Verschwendung", "Probieren Sie SCAMPER")],
        "example": "Poojas Team: 23 Ideen in 30 Minuten, von Packern, Qualität und Lager.",
        "example_cue": "Poojas Team",
        "script": "Gehen Sie jetzt breit, bevor Sie wählen. Brainwriting bedeutet, dass jeder Ideen allein "
                  "aufschreibt, bevor die Gruppe spricht. So gewinnt nicht die lauteste Stimme. Stellen Sie "
                  "Wie-könnten-wir-Fragen, um Grenzen in Chancen zu verwandeln. Probieren Sie SCAMPER, oder "
                  "gehen Sie die acht Verschwendungsarten durch. Poojas Team schrieb dreiundzwanzig Ideen "
                  "in dreißig Minuten. Packer, Qualität und Lager machten mit. Wie wählen Sie nur eine?",
    },
    {
        "key": "p10", "num": 10, "title": "Mit einer Bewertungsmatrix wählen",
        "points": [("Jedes Kriterium gewichten", "Gewichten Sie jedes Kriterium"),
                   ("Jedes Konzept bewerten, Punkte addieren", "Bewerten Sie jedes Konzept"),
                   ("Sicherheit und Qualität sind K.-o.-Kriterien", "Sicherheit und Qualität")],
        "example": "Etikettenfächer + Scanprüfung: 4,15. Neuer Drucker an der Station: 4,10.",
        "example_cue": "Die zwei besten",
        "script": "Nutzen Sie eine einfache Bewertungsmatrix. Gewichten Sie jedes Kriterium, wie Qualität, "
                  "Akzeptanz, Wirkung, Machbarkeit und Kosten. Bewerten Sie jedes Konzept von eins bis "
                  "fünf. Aber Sicherheit und Qualität sind nicht nur Punkte. Sie sind K.-o.-Kriterien. Die "
                  "zwei besten lagen knapp beieinander. Etikettenfächer je Modell mit Scanprüfung, und ein "
                  "neuer Drucker an der Station. Die Fächer gewannen, knapp. Was testen Sie zuerst?",
    },
    {
        "key": "p11", "num": 11, "title": "Prototyp: klein und günstig",
        "points": [("Zuerst Papier, Karton oder Klebeband", "Beginnen Sie mit Papier"),
                   ("Eine Station vor der Linie", "Testen Sie eine Station"),
                   ("Stunden, nicht Monate", "wird in Stunden gemessen")],
        "example": "Etikettenfächer aus Karton, eines pro Modell, neben dem Packer festgeklebt.",
        "example_cue": "Poojas erster Prototyp",
        "script": "Machen Sie die Idee so günstig wie möglich real. Beginnen Sie mit Papier, Karton oder "
                  "Klebeband auf dem Boden. Testen Sie eine Station vor der ganzen Linie. Ein guter "
                  "Prototyp wird in Stunden gemessen, nicht in Monaten. Poojas erster Prototyp war aus "
                  "Karton. Ein Etikettenfach pro Modell, direkt neben dem Packer festgeklebt, mit dem "
                  "Scanner griffbereit. Er kostete fast nichts. Aber woher wüsste sie, ob er funktioniert?",
    },
    {
        "key": "p12", "num": 12, "title": "Den Test planen",
        "points": [("Eine klare Hypothese", "Schreiben Sie eine Hypothese"),
                   ("Umfang, Kennzahlen und Vergleich", "Legen Sie den Umfang"),
                   ("Eine vorab vereinbarte Entscheidungsregel", "Vereinbaren Sie vorab")],
        "example": "Hypothese: Fächer + Scanprüfung bringen die Zykluszeit unter den TAKT und senken "
                   "Etikettenfehler um mindestens 75 %.",
        "example_cue": "Poojas Hypothese",
        "script": "Planen Sie den Test, bevor Sie beginnen. Schreiben Sie eine Hypothese. Wenn wir das "
                  "ändern, erwarten wir dies. Legen Sie den Umfang, die Kennzahlen und den Vergleich fest. "
                  "Vereinbaren Sie vorab eine Entscheidungsregel. Übernehmen, anpassen oder stoppen. Poojas "
                  "Hypothese war klar. Die Fächer und eine Scanprüfung bringen die Zykluszeit unter den "
                  "TAKT. Und die Etikettenfehler sinken um mindestens drei Viertel. Was ist passiert, "
                  "glauben Sie?",
    },
    {
        "key": "p13", "num": 13, "title": "Die Ergebnisse",
        "points": [("Zykluszeit: von 52 s auf 44 s", "Die Zykluszeit sank"),
                   ("Gute Pumpen pro Schicht: von 500 auf 610", "Gute Pumpen pro Schicht"),
                   ("Etikettenfehler: von 12 auf 2 pro 1.000", "Etikettenfehler sanken"),
                   ("Laufweg: von 4 m auf 1,2 m", "Der Laufweg sank")],
        "example": "18 von 20 Packern nutzten die neue Methode: 90 % Akzeptanz.",
        "example_cue": "Achtzehn von zwanzig",
        "script": "Der Versuch funktionierte, fast ganz. Die Zykluszeit sank von zweiundfünfzig auf "
                  "vierundvierzig Sekunden. Das liegt jetzt unter dem TAKT. Gute Pumpen pro Schicht stiegen "
                  "von fünfhundert auf sechshundertzehn. Etikettenfehler sanken von zwölf auf zwei pro "
                  "tausend. Der Laufweg sank um mehr als die Hälfte. Und achtzehn von zwanzig Packern "
                  "nutzten die neue Methode. Das sind neunzig Prozent. Sollte Pooja es also morgen "
                  "ausrollen?",
    },
    {
        "key": "p14", "num": 14, "title": "Anpassen vor dem Ausrollen",
        "points": [("Keine 100 % Akzeptanz? Fragen Sie, warum", "Zwei Packer"),
                   ("Den schweren Schritt vereinfachen, neu testen", "vereinfachte diesen Schritt"),
                   ("Prüfen, dass nichts anderes es verursacht hat", "Und prüfen Sie")],
        "example": "Die zwei Packer waren Linkshänder. Die Fächer waren rechts. Spiegeln Sie das Layout.",
        "example_cue": "Es stellte sich heraus",
        "script": "Noch nicht. Zwei Packer folgten der Methode nicht. Also fragte sie, warum. Es stellte "
                  "sich heraus, dass sie Linkshänder waren, und die Fächer waren rechts. Sie vereinfachte "
                  "diesen Schritt mit einem gespiegelten Layout und testete neu. Und prüfen Sie, dass "
                  "nichts anderes den Gewinn verursacht hat, wie ein leichterer Modellmix oder mehr "
                  "Personal. Erst dann standardisieren Sie. Wie würden Sie Erfolg messen?",
    },
    {
        "key": "p15", "num": 15, "title": "Messen, standardisieren, starten",
        "points": [("Ergebnis, Prozess, Akzeptanz, Ausgewogenheit", "Messen Sie das Ergebnis"),
                   ("Standardisieren, schulen, nach 30/60/90 prüfen", "Dann standardisieren Sie"),
                   ("Morgen starten: 10 Zyklen, 3 Menschen", "Starten Sie morgen")],
        "example": "Poojas 90-Tage-Prüfung: Fehler hielten bei 2 pro 1.000, Akzeptanz bei 100 %.",
        "example_cue": "Nach neunzig Tagen",
        "script": "Messen Sie das Ergebnis, den Prozess, die Akzeptanz und die Ausgewogenheit. Wurde etwas "
                  "anderes schlechter, wie Sicherheit oder Kosten? Dann standardisieren Sie, schulen jede "
                  "Schicht und prüfen nach dreißig, sechzig und neunzig Tagen. Nach neunzig Tagen hielten "
                  "Poojas Fehler bei zwei pro tausend, und jeder Packer nutzte die Methode. Starten Sie "
                  "morgen. Beobachten Sie zehn Zyklen einer mühsamen Arbeit, sprechen Sie mit drei "
                  "Menschen, und schreiben Sie einen Bedarf auf.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "steps", "items": [
        {"label": "Verstehen", "with": 1}, {"label": "Definieren", "with": 1},
        {"label": "Ideen finden", "with": 1}, {"label": "Prototyp", "with": 2},
        {"label": "Test", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Lean-Werkzeuge bleiben", "icon": "wrench", "with": 0},
        {"label": "Zuerst das richtige Problem", "icon": "search", "with": 1},
        {"label": "Von den Nutzern getragen", "icon": "hand", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Verordnete Methode", "sub": "Nach zwei Wochen weg", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Gemeinsam gestaltete Methode", "sub": "Menschen behalten sie", "icon": "check", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Beobachten", "icon": "search", "with": 0},
        {"label": "Zuerst Fakten", "icon": "clipboard", "with": 1},
        {"label": "Kleine Versuche", "icon": "shape", "with": 2},
        {"label": "Akzeptanz", "icon": "person", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Chaos automatisieren", "icon": "gear", "tone": "bad", "with": 0},
        {"label": "Nur das Symptom", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Nicht umsetzbar", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Viel Geld, kein Test", "icon": "trash", "tone": "bad", "with": 3}]},
    "p05": {"type": "steps", "items": [
        {"label": "Verstehen", "with": 0}, {"label": "Definieren", "with": 0},
        {"label": "Ideen finden", "with": 0}, {"label": "Prototyp", "with": 1},
        {"label": "Test", "with": 1}],
        "then": {"type": "icons", "with": 2, "items": [
            {"label": "Erwünscht", "sub": "Nutzer brauchen es", "icon": "person", "with": 2},
            {"label": "Machbar", "sub": "Wir können es", "icon": "wrench", "with": 2},
            {"label": "Wirtschaftlich", "sub": "Den Preis wert", "icon": "scale", "tone": "good", "with": 2}]}},
    "p06": {"type": "icons", "items": [
        {"label": "Beobachten", "icon": "search", "with": 0},
        {"label": "Befragen", "icon": "person", "with": 1},
        {"label": "Begleiten", "icon": "walk", "with": 2},
        {"label": "Sagt · denkt · tut · fühlt", "icon": "clipboard", "with": 3}]},
    "p07": {"type": "flow", "items": [
        {"label": "Zum Regal laufen", "icon": "walk", "tone": "bad", "with": 0},
        {"label": "Ähnliche Etiketten", "icon": "label", "tone": "bad", "with": 1},
        {"label": "Auf den Drucker warten", "icon": "clock", "tone": "bad", "with": 2}]},
    "p08": {"type": "doc", "items": [
        {"label": "Nutzer: die Packer", "icon": "person", "with": 0},
        {"label": "Bedarf: das richtige Etikett griffbereit", "icon": "label", "with": "example"},
        {"label": "Erkenntnis: ähnliche Etiketten und Laufwege", "icon": "search", "with": "example"},
        {"label": "Ausgangslage: 52 s gegenüber 45 s, 12 pro 1.000", "icon": "chartUp", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Brainwriting", "icon": "clipboard", "with": 0},
        {"label": "Wie könnten wir…?", "icon": "key", "with": 1},
        {"label": "SCAMPER, 8 Verschwendungsarten", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 23, "icon": "key", "label": "Ideen in 30 Minuten",
                 "unit": "Packer, Qualität und Lager", "with": "example"}},
    "p10": {"type": "versus", "items": [
        {"label": "Neuer Drucker", "sub": "Bewertung 4,10 von 5", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "Etikettenfächer + Scanprüfung", "sub": "Bewertung 4,15 von 5", "icon": "check", "tone": "good", "with": "example"}]},
    "p11": {"type": "ladder", "top": "AM GÜNSTIGSTEN", "bottom": "AM GRÖSSTEN", "items": [
        {"label": "Papier, Karton, Klebeband", "icon": "shape", "with": 0},
        {"label": "Pilot an einer Station", "icon": "pin", "with": 1},
        {"label": "Linienversuch", "icon": "sequence", "with": 1}],
        "then": {"type": "stat", "value": 1, "suffix": " Fach pro Modell", "icon": "label", "label": "aus Karton, neben dem Packer festgeklebt",
                 "unit": "Scanner griffbereit", "with": "example"}},
    "p12": {"type": "flow", "items": [
        {"label": "Hypothese", "icon": "key", "with": 0},
        {"label": "Umfang und Kennzahlen", "icon": "clipboard", "with": 1},
        {"label": "Übernehmen · anpassen · stoppen", "icon": "scale", "tone": "good", "with": 2}]},
    "p13": {"type": "compare", "before": {"label": "Vorher", "value": 12}, "after": {"label": "Versuch", "value": 2},
            "unit": "Etikettenfehler pro 1.000 Pumpen", "note": "Zyklus 52 s → 44 s · 500 → 610 gute Pumpen", "with": 2,
            "then": {"type": "stat", "value": 90, "suffix": "%", "icon": "person", "label": "Akzeptanz",
                     "unit": "18 von 20 Packern", "with": "example"}},
    "p14": {"type": "flow", "items": [
        {"label": "Fragen, warum", "icon": "person", "with": 0},
        {"label": "Layout spiegeln", "icon": "shape", "with": 1},
        {"label": "Modellmix prüfen", "icon": "search", "with": 2},
        {"label": "Dann standardisieren", "icon": "check", "tone": "good", "with": 2}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Standardisieren, schulen", "sub": "Tag 0", "icon": "clipboard", "with": 1},
        {"label": "Prüfung", "sub": "30 · 60", "icon": "search", "with": 1},
        {"label": "Fehler hielten bei 2", "sub": "90 Tage", "icon": "check", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Welche ist die beste Design Thinking Aufgabenstellung?",
        "options": ["Wir brauchen einen schnelleren Etikettendrucker beim Verpacken",
                    "Packer brauchen das richtige Etikett griffbereit, weil ähnliche Etiketten und Laufwege "
                    "Fehler verursachen",
                    "Packer müssen bei Etiketten sorgfältiger sein"],
        "correct": 1,
        "explanation": "Sie nennt Nutzer, Bedarf und Erkenntnis, ohne eine Lösung zu wählen oder jemandem die "
                       "Schuld zu geben. Die anderen sind eine Lösung und eine Schuldzuweisung.",
        "q_script": "Kurzer Check. Welche ist die beste Aufgabenstellung? Nehmen Sie sich kurz Zeit.",
        "a_script": "Die zweite. Sie nennt Nutzer, Bedarf und Erkenntnis. Die erste ist schon eine Lösung, "
                    "und die letzte nur eine Schuldzuweisung.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Ein Pilot senkt die Zykluszeit, aber nur 6 von 10 Werkern nutzen die neue Methode. Was "
                    "nun?",
        "options": ["Ausrollen: die Zahlen sind besser",
                    "Die anderen vier nach dem Grund fragen, vereinfachen und neu testen",
                    "Pflicht machen und täglich auditieren"],
        "correct": 1,
        "explanation": "Geringe Akzeptanz ist auch ein Beleg. Finden Sie heraus, was die Methode für diese "
                       "Nutzer schwer macht, verbessern Sie sie, und testen Sie neu, bevor Sie standardisieren.",
        "q_script": "Noch eine, diesmal ein Szenario. Ein Pilot senkt die Zykluszeit. Aber nur sechs von zehn "
                    "Werkern nutzen die neue Methode. Was sollte das Team tun? Überlegen Sie kurz.",
        "a_script": "Fragen Sie die anderen vier nach dem Grund, vereinfachen Sie den schweren Teil, und "
                    "testen Sie neu. Geringe Akzeptanz ist auch ein Beleg, behandeln Sie sie wie jedes andere "
                    "Ergebnis.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
