"""a3_problem_solving in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh a3_problem_solving_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "a3_de"
NAME = "a3_problem_solving_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Burn Down Chart": "Börn Daun Tschart",
    "Five Whys": "Faiw Wais",
    "Ishikawa": "Ischikawa",
    "Genbutsu": "Genbutsu",
    "Genjitsu": "Gendschitsu",
    "Pareto": "Pareto",
    "Gemba": "Gemba",
    "PDCA": "pe de ze a",
    "MES": "emm e ess",
    "SOP": "ess o pe",
    "A3": "a drei",
    "3G": "drei ge",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Fünfhundertsechsundsiebzig Server sind in vier Wochen beim ersten Boot-Test "
    "durchgefallen. Der erste Lösungsvorschlag? Zwei Prüfer mehr. Kommt Ihnen das bekannt "
    "vor? In dieser Lektion lernen Sie die A3-Problemlösung kennen. Sie sehen, wie man die "
    "ganze Geschichte eines Problems auf einer Seite erzählt, von der echten Lücke bis zur "
    "bewiesenen Lösung. Wir begleiten Karthik, Testingenieur an einer Server-Montagelinie, "
    "der sein erstes A3 schreibt."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Beginnen Sie mit einer messbaren Lücke, nie mit Ursache "
    "oder Lösung. Gehen Sie hin und schauen Sie, und belegen Sie jede Ursache. Und "
    "standardisieren Sie nur, was Ihr Pilot bewiesen hat. Ihre Aufgabe für diese Woche. "
    "Schreiben Sie für ein wiederkehrendes Problem die Problembeschreibung auf einen "
    "A3-Bogen. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie das Burn Down "
    "Chart kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was ein A3 ist",
        "points": [("Benannt nach dem Papierformat A3", "Ein A3 ist nach einem Papierformat"),
                   ("Die ganze Problemgeschichte auf einer Seite", "Es erzählt die ganze"),
                   ("Definieren, Ursachen finden, testen, sichern", "Sie definieren das Problem"),
                   ("Visuell, und im Team erstellt", "Es ist visuell")],
        "example": "Karthiks Bericht sagte „Die Werker sind nachlässig“. Sein Vorgesetzter gab ihm einen "
                   "leeren A3-Bogen zurück.",
        "example_cue": "Sein Bericht sagte",
        "script": "Ein A3 ist nach einem Papierformat benannt. Es erzählt die ganze Geschichte eines "
                  "Problems auf einer Seite. Sie definieren das Problem, finden seine echten Ursachen, "
                  "testen Lösungen und sichern die Ergebnisse. Es ist visuell, und Sie erstellen es im "
                  "Team. So lernte Karthik sein erstes A3 kennen. Sein Bericht sagte, die Werker seien "
                  "nachlässig. Sein Vorgesetzter gab ihn zurück, mit einem leeren A3-Bogen. Was zählt also "
                  "wirklich als Problem?",
    },
    {
        "key": "p02", "num": 2, "title": "Probleme sind Lücken",
        "points": [("Ein Problem ist eine messbare Lücke", "Ein Problem ist eine Lücke"),
                   ("Springen Sie nicht von der Klage zur Lösung", "Das A3 hält Sie davon ab"),
                   ("Eine Lücke lässt sich messen und untersuchen", "Sie können eine Lücke messen")],
        "example": "„Die Werker sind nachlässig“ ist eine Schuldzuweisung. „Boot-Fehler stiegen auf 4,8 %“ "
                   "ist eine Lücke.",
        "example_cue": "Vergleichen Sie zwei Aussagen",
        "script": "Hier ist die Kernidee. Ein Problem ist eine Lücke zwischen dem, was passiert, und dem "
                  "nötigen Standard. Das A3 hält Sie davon ab, von der Klage direkt zur Lösung zu springen. "
                  "Vergleichen Sie zwei Aussagen. Die Werker sind nachlässig, das ist Schuld. Boot-Fehler "
                  "stiegen auf vier Komma acht Prozent, das ist eine Lücke. Sie können eine Lücke messen "
                  "und untersuchen. Welche Aussage hören Sie in Ihrer Halle öfter?",
    },
    {
        "key": "p03", "num": 3, "title": "Wo das A3 passt: PDCA",
        "points": [("Probleme, die immer wiederkommen", "Nutzen Sie es für Probleme"),
                   ("Probleme, die Teams gemeinsam lösen müssen", "Es zeigt seine Stärke"),
                   ("Basiert auf Plan · Do · Check · Act", "folgt es dem PDCA")],
        "example": "Karthiks Boot-Fehler: wiederholt, teuer und bereichsübergreifend.",
        "example_cue": "Karthiks Boot-Fehler",
        "script": "Wo passt das A3? Nutzen Sie es für Probleme, die immer wiederkommen. Wiederholte Fehler, "
                  "Stillstände, Fehlteile und verpasste Mengen sind gute Kandidaten. Es zeigt seine Stärke, "
                  "wenn Produktion, Qualität und Technik gemeinsam etwas lösen müssen. Und im Kern folgt es "
                  "dem PDCA. Sie planen, dann machen Sie einen kleinen Pilot. Sie prüfen die Ergebnisse "
                  "gegen das Ziel. Dann handeln Sie, indem Sie standardisieren oder neu überlegen. Karthiks "
                  "Boot-Fehler passen perfekt. Was kommt also auf Ihren Bogen?",
    },
    {
        "key": "p04", "num": 4, "title": "Aufbau eines A3",
        "points": [("Links: Hintergrund, Ist-Zustand, Ziel", "Die linke Seite"),
                   ("Ursachenanalyse: warum die Lücke besteht", "Die Ursachenanalyse erklärt"),
                   ("Rechts: Maßnahmen, Plan, Nachverfolgung", "Die rechte Seite"),
                   ("Jedes Feld beantwortet eine Frage", "Jedes Feld beantwortet")],
        "example": "Karthiks Bogen: sieben Felder, eine Seite, von links nach rechts gelesen.",
        "example_cue": "Karthiks Bogen hat",
        "script": "Stellen Sie sich den Bogen vor. Die linke Seite erzählt die bisherige Geschichte. Der "
                  "Hintergrund sagt, warum es jetzt wichtig ist. Der Ist-Zustand zeigt, was wirklich "
                  "passiert. Das Ziel sagt, welches Ergebnis, bis wann. Die Ursachenanalyse erklärt, warum "
                  "die Lücke besteht. Die rechte Seite geht ins Handeln, mit Maßnahmen, einem Zeitplan und "
                  "Nachverfolgung. Jedes Feld beantwortet eine Frage. Karthiks Bogen hat sieben Felder, von "
                  "links nach rechts gelesen. Könnten Sie die Frage hinter jedem nennen?",
    },
    {
        "key": "p05", "num": 5, "title": "Die Problembeschreibung",
        "points": [("Die Lücke benennen, nie eine Ursache", "benennt die Lücke"),
                   ("Linie · Produkt · Zeitraum · Messgröße", "Nennen Sie die Linie"),
                   ("Ein klarer Nenner, gleiche Definitionen", "Nutzen Sie einen klaren Nenner"),
                   ("Keine Schuld, keine Lösung", "Es gibt keine Schuldzuweisung")],
        "example": "Linie 2, letzter Monat: 4,8 % von 12.000 Servern fielen beim ersten Boot-Test durch, "
                   "gegenüber einer Referenz von 1,5 %.",
        "example_cue": "Hier ist Karthiks Fassung",
        "script": "Jetzt das Feld, das am schwersten richtig zu machen ist. Eine gute Problembeschreibung "
                  "benennt die Lücke, behauptet aber nie eine Ursache. Nennen Sie die Linie, das Produkt, "
                  "den Zeitraum und die Messgröße. Nutzen Sie einen klaren Nenner und die gleichen "
                  "Definitionen. Hier ist Karthiks Fassung. Im letzten Monat lagen die Fehler beim ersten "
                  "Boot-Test an Linie zwei im Schnitt bei vier Komma acht Prozent. Die Referenz war eins "
                  "Komma fünf, bei zwölftausend Servern. Merken Sie, was fehlt? Es gibt keine "
                  "Schuldzuweisung und keine Lösung.",
    },
    {
        "key": "p06", "num": 6, "title": "Hingehen und schauen: die 3G",
        "points": [("Gemba: der echte Ort", "Gemba ist der echte Ort"),
                   ("Genbutsu: die echten Dinge", "Genbutsu bedeutet"),
                   ("Genjitsu: die echten Fakten", "Genjitsu bedeutet")],
        "example": "7 von 10 fehlerhaften Servern am Prüfplatz: ein Speichermodul leicht angehoben.",
        "example_cue": "Karthik holte zehn",
        "script": "Bevor Sie eine Tabelle öffnen, gehen Sie hin und schauen Sie. Lean nennt das die 3G. "
                  "Gemba ist der echte Ort, also stehen Sie an der Teststation. Genbutsu bedeutet die "
                  "echten Dinge, wie fehlerhafte Server, Vorrichtungen und Testprotokolle. Genjitsu "
                  "bedeutet die echten Fakten, die Sie selbst prüfen. Karthik holte zehn fehlerhafte Server "
                  "auf den Prüfplatz. Bei sieben davon saß ein Speichermodul leicht angehoben. Hätte ein "
                  "Bericht ihm das jemals gezeigt?",
    },
    {
        "key": "p07", "num": 7, "title": "Daten, denen Sie trauen können",
        "points": [("Eine klare Definition", "beginnen mit einer klaren Definition"),
                   ("Eindeutige Einheiten zählen: Nachtests verstecken keine Fehler", "Warum eindeutig?"),
                   ("Zeitstempel, Seriennummern, Kalibrierung prüfen", "Stimmen die Zeitstempel"),
                   ("Das Linienprotokoll stimmt mit dem MES überein", "Stimmt das Linienprotokoll")],
        "example": "Erstdurchlauf-Fehlerquote = eindeutige Server, die ihren ersten gültigen Test nicht "
                   "bestehen ÷ eindeutige getestete Server.",
        "example_cue": "Die Erstdurchlauf-Fehlerquote ist",
        "script": "Gute Daten beginnen mit einer klaren Definition. Die Erstdurchlauf-Fehlerquote ist die "
                  "Zahl eindeutiger Server, die den ersten gültigen Test nicht bestehen, geteilt durch alle "
                  "eindeutigen getesteten Server. Warum eindeutig? Nachtests können Fehler verstecken oder "
                  "Server doppelt zählen. Dann prüfen Sie die Daten. Stimmen die Zeitstempel, ist jede "
                  "Seriennummer eindeutig? Ist der Tester kalibriert? Stimmt das Linienprotokoll mit dem "
                  "MES überein? Erst dann trauen Sie Ihrem Diagramm.",
    },
    {
        "key": "p08", "num": 8, "title": "Die Lücke sehen",
        "points": [("Wochentrend: jede Woche steigend", "Wochentrend stieg"),
                   ("Etwa 400 zusätzliche Fehler", "Das sind fast vierhundert"),
                   ("Pareto: Fehler nach Fehlerbild sortieren", "Dann ein Pareto-Diagramm")],
        "example": "Speicher nicht erkannt: 288 von 576 Fehlern, die Hälfte der Gesamtzahl.",
        "example_cue": "Speicher nicht erkannt",
        "script": "Was zeigte also das Diagramm? Karthiks Wochentrend stieg jede einzelne Woche. In Woche "
                  "vier erreichte er fünfeinhalb Prozent. Bei der Referenzquote würden Sie etwa "
                  "hundertachtzig Fehler erwarten. Er hatte fünfhundertsechsundsiebzig. Das sind fast "
                  "vierhundert zusätzliche. Dann ein Pareto-Diagramm teilte sie nach Fehlerbild auf. "
                  "Speicher nicht erkannt war die Hälfte. Die Lücke ist klar, aber sie beweist keine "
                  "Ursache. Wo würden Sie anfangen?",
    },
    {
        "key": "p09", "num": 9, "title": "Ziel und Umfang",
        "points": [("Ziel: 2 % oder weniger innerhalb von 6 Wochen", "Karthiks Ziel war klar"),
                   ("Leitplanken: Testzeit, Nachtests, Durchschlupf", "Fügen Sie auch Leitplanken hinzu"),
                   ("Umfang: was drin ist, was nicht", "Dann legen Sie den Umfang fest")],
        "example": "Außerhalb des Umfangs: Testgrenzen lockern, um besser auszusehen.",
        "example_cue": "Testgrenzen zu lockern",
        "script": "Setzen Sie als Nächstes ein prüfbares Ziel. Karthiks Ziel war klar. Erstdurchlauf-Fehler "
                  "an Linie zwei in sechs Wochen auf höchstens zwei Prozent senken. Fügen Sie auch "
                  "Leitplanken hinzu, wie Testzeit, Nachtestquote und Durchschlupf. So gewinnen Sie nicht "
                  "durch Mogeln. Dann legen Sie den Umfang fest. Speicherfehler an Linie zwei sind drin. "
                  "Testgrenzen zu lockern ist draußen. Sehen Sie, warum?",
    },
    {
        "key": "p10", "num": 10, "title": "Ursachen erkunden: Ishikawa",
        "points": [("Zuerst breit denken", "denken Sie breit"),
                   ("Sechs M: Mensch, Maschine, Methode…", "Es ordnet mögliche Ursachen"),
                   ("Jeder Ast ist eine Vermutung, bis er geprüft ist", "Jeder Ast ist nur")],
        "example": "Ist das Einsetzen geschult? Hat sich das Gehäuse geändert? Schwankt das Einrasten je "
                   "Charge?",
        "example_cue": "Karthiks Team stellte",
        "script": "Warum gibt es die Lücke? Zuerst denken Sie breit, mit einem Ishikawa-Diagramm. Es ordnet "
                  "mögliche Ursachen in sechs M. Mensch, Maschine, Methode, Material, Messung und Mitwelt. "
                  "Karthiks Team stellte in jedem Bereich Fragen. Ist die Einsetzmethode geschult? Hat sich "
                  "das Gehäuse geändert? Schwankt das Einrasten der Module je Charge? Aber Vorsicht. Jeder "
                  "Ast ist nur eine Vermutung, bis Sie ihn prüfen. Wie grenzen Sie es also ein?",
    },
    {
        "key": "p11", "num": 11, "title": "Grundursache: Five Whys",
        "points": [("Fragen Sie warum, Schritt für Schritt", "gehen Sie mit den Five Whys in die Tiefe"),
                   ("Enden Sie bei einer Prozessursache, die Sie beheben können", "Das ist eine Prozessursache"),
                   ("Eine Kette ist kein Beweis: testen Sie sie", "Aber eine Kette")],
        "example": "Grundursache: Die Arbeitsanweisungen wurden bei der Gehäuseänderung nicht überprüft.",
        "example_cue": "Die Arbeitsanweisungen wurden",
        "script": "Dann gehen Sie mit den Five Whys in die Tiefe. Warum fielen Server durch? Ein "
                  "Speichermodul saß nicht ganz. Warum? Die Verriegelung schloss zu früh. Warum? Das neue "
                  "Gehäuse ließ weniger Platz zum geraden Drücken. Warum blieb die Methode gleich? Die "
                  "Arbeitsanweisungen wurden bei der Gehäuseänderung nicht überprüft. Das ist eine "
                  "Prozessursache, die Sie beheben können. Aber eine Kette ist kein Beweis. Karthik drückte "
                  "Module schräg ein, und der Fehler kam jedes Mal.",
    },
    {
        "key": "p12", "num": 12, "title": "Maßnahmen und Eindämmung",
        "points": [("Die bestätigte Ursache durchbrechen", "die Ursache durchbrechen"),
                   ("Bewerten: Wirkung, Risiko, Kosten, Nachhaltigkeit", "Bewerten Sie jede"),
                   ("Jetzt eindämmen, dauerhaft beheben", "Dämmen Sie in der Zwischenzeit ein")],
        "example": "Einsetzhilfe · Verriegelungsprüfung · Anweisungsprüfung bei jeder Gehäuseänderung",
        "example_cue": "Karthiks Team wählte drei",
        "script": "Wählen Sie jetzt Maßnahmen, die die Ursache durchbrechen. Karthiks Team wählte drei. "
                  "Eine Einsetzhilfe, die das Modul gerade hält. Eine Verriegelungsprüfung, bevor der "
                  "Server die Station verlässt. Und eine Überprüfung der Arbeitsanweisung bei jeder "
                  "Gehäuseänderung. Bewerten Sie jede nach Wirkung, Risiko, Kosten und wie leicht sie zu "
                  "halten ist. Dämmen Sie in der Zwischenzeit ein. Verdächtige Server wurden gesperrt und "
                  "erneut geprüft. Die Eindämmung schützt Ihren Kunden, aber sie ist nicht die Lösung.",
    },
    {
        "key": "p13", "num": 13, "title": "Plan und Verantwortliche",
        "points": [("Ein Verantwortlicher, ein Termin, ein Nachweis", "nennt Ihr Plan einen Verantwortlichen"),
                   ("Wochen 1–2: Ursache bestätigen, Pilot", "Die Testtechnik bestätigt"),
                   ("Wochen 3–4: SOP aktualisieren, jede Schicht schulen", "Instandhaltung und Produktion"),
                   ("Wochen 5–6: Ergebnisse prüfen", "Die Qualität prüft")],
        "example": "Festgefahren? Eskalieren Sie mit dem genauen Hindernis und der Entscheidung, die Sie "
                   "brauchen.",
        "example_cue": "Festgefahren?",
        "script": "Eine Maßnahme ohne Verantwortlichen passiert selten. Deshalb nennt Ihr Plan einen "
                  "Verantwortlichen, einen Termin und den Nachweis für jede Maßnahme. Die Testtechnik "
                  "bestätigt die Ursache in Woche eins. Die Prozesstechnik testet die Einsetzhilfe in Woche "
                  "zwei. Instandhaltung und Produktion aktualisieren die SOP und schulen jede Schicht bis "
                  "Woche vier. Die Qualität prüft die Ergebnisse in den Wochen fünf und sechs. "
                  "Festgefahren? Eskalieren Sie mit dem genauen Hindernis. Woher wissen Sie, dass es "
                  "funktioniert hat?",
    },
    {
        "key": "p14", "num": 14, "title": "Pilot und Prüfung",
        "points": [("Gleicher Produktmix wie in der Ausgangslage", "mit dem gleichen Produktmix"),
                   ("Von 4,8 % auf 1,6 %: Ziel erreicht", "Die Fehler sanken"),
                   ("Leitplanken ebenfalls geprüft", "er prüfte auch die Leitplanken"),
                   ("Verfehlt? Prüfen Sie die Ursache, nicht das Ziel", "Wäre es nicht so gewesen")],
        "example": "Pilot: 48 Fehler bei 3.000 Servern = 1,6 %.",
        "example_cue": "Karthik führte ihn",
        "script": "Ein Pilot ist ein Experiment, keine Ankündigung. Karthik führte ihn mit dreitausend "
                  "Servern durch, mit dem gleichen Produktmix wie in der Ausgangslage. Die Fehler sanken "
                  "auf eins Komma sechs Prozent. Ziel erreicht. Aber er prüfte auch die Leitplanken. Die "
                  "Testzeit blieb stabil, und kein anderes Fehlerbild nahm zu. Hielt es in jeder Schicht? "
                  "Ja. Wäre es nicht so gewesen, würden Sie die Ursache neu prüfen, und nie still das Ziel "
                  "ändern.",
    },
    {
        "key": "p15", "num": 15, "title": "Sichern und Ihr 30-Tage-A3",
        "points": [("SOP, Checkliste, Schulung aktualisieren", "Aktualisieren Sie die SOP"),
                   ("Prüfung zum Schichtbeginn; Überprüfung nach 30/60/90 Tagen", "Fügen Sie eine Verriegelungsprüfung"),
                   ("Nur auf Linien übertragen, die wirklich passen", "Übertragen Sie es auf andere Linien"),
                   ("Ihr eigenes A3 in 30 Tagen", "Jetzt sind Sie dran")],
        "example": "Tage 1–5: ein echtes Problem, Ausgangslage am Gemba. Tag 20: Ursachen und Pilot. Tag 30: "
                   "Ihr A3 vorstellen.",
        "example_cue": "In den ersten fünf Tagen",
        "script": "Machen Sie schließlich den neuen Weg zur Regel. Aktualisieren Sie die SOP, die "
                  "Checkliste und die Schulung. Fügen Sie eine Verriegelungsprüfung zu jedem Schichtbeginn "
                  "hinzu, und prüfen Sie den Trend nach dreißig, sechzig und neunzig Tagen. Übertragen Sie "
                  "es auf andere Linien nur, wenn sie wirklich passen. Jetzt sind Sie dran. In den ersten "
                  "fünf Tagen wählen Sie ein echtes Problem und prüfen die Ausgangslage am Gemba. Bis Tag "
                  "zwanzig: Ursachen bestätigen, Pilot fahren. Bis Tag dreißig: Ihr A3 vorstellen.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Papierformat A3", "icon": "label", "with": 0},
        {"label": "Die Geschichte auf einer Seite", "icon": "clipboard", "with": 1},
        {"label": "Ursachen, Tests, Ergebnisse", "icon": "search", "with": 2},
        {"label": "Im Team erstellt", "icon": "person", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "„Die Werker sind nachlässig“", "sub": "Karthiks erster Bericht", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Ein leerer A3-Bogen", "sub": "Die Antwort seines Vorgesetzten", "icon": "clipboard", "tone": "good", "with": "example"}]}},
    "p02": {"type": "versus", "items": [
        {"label": "Schuld", "sub": "„Die Werker sind nachlässig“", "icon": "person", "tone": "bad", "with": "example"},
        {"label": "Lücke", "sub": "Boot-Fehler bis 4,8 %", "icon": "chartUp", "tone": "good", "with": "example"}]},
    "p03": {"type": "icons", "items": [
        {"label": "Wiederholte Fehler", "icon": "warning", "with": 0},
        {"label": "Stillstände, Fehlteile", "icon": "clock", "with": 0},
        {"label": "Bereichsübergreifend", "icon": "person", "with": 1}],
        "then": {"type": "flow", "with": 2, "items": [
            {"label": "Plan", "icon": "clipboard", "with": 2},
            {"label": "Do", "sub": "Kleiner Pilot", "icon": "wrench", "with": 2},
            {"label": "Check", "sub": "Gegen das Ziel", "icon": "search", "with": 2},
            {"label": "Act", "sub": "Standardisieren", "icon": "check", "tone": "good", "with": 2}]}},
    "p04": {"type": "doc", "items": [
        {"label": "Hintergrund · warum jetzt", "icon": "label", "with": 0},
        {"label": "Ist-Zustand · Ziel", "icon": "chartUp", "with": 0},
        {"label": "Grundursache · warum die Lücke", "icon": "search", "with": 1},
        {"label": "Maßnahmen · Zeitplan", "icon": "wrench", "with": 2},
        {"label": "Nachverfolgung · hat es gewirkt?", "icon": "check", "with": 2}]},
    "p05": {"type": "versus", "items": [
        {"label": "Schwach", "sub": "„Die Qualität ist überall schlecht“", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Präzise", "sub": "Linie 2 · letzter Monat · 4,8 % gegenüber 1,5 %", "icon": "check", "tone": "good", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Gemba", "sub": "Echter Ort", "icon": "walk", "with": 0},
        {"label": "Genbutsu", "sub": "Echte Dinge", "icon": "chip", "with": 1},
        {"label": "Genjitsu", "sub": "Echte Fakten", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 7, "suffix": " / 10", "icon": "chip", "label": "fehlerhafte Server am Prüfplatz",
                 "unit": "ein Speichermodul leicht angehoben", "with": "example"}},
    "p07": {"type": "flow", "items": [
        {"label": "Klare Definition", "icon": "clipboard", "with": 0},
        {"label": "Eindeutige Server", "icon": "count", "with": 1},
        {"label": "Zeitstempel, Seriennummern", "icon": "barcode", "with": 2},
        {"label": "Protokoll stimmt mit dem MES überein", "icon": "check", "tone": "good", "with": 3}]},
    "p08": {"type": "bars", "label": "", "note": "Fehler beim ersten Boot-Test pro 1.000 Server, je Woche", "items": [
        {"label": "W1", "value": 41, "with": 0},
        {"label": "W2", "value": 46, "with": 0},
        {"label": "W3", "value": 50, "with": 0},
        {"label": "W4", "value": 55, "tone": "bad", "with": 0}],
        "then": {"type": "bars", "label": "", "note": "Fehlerbilder: 576 Erstdurchlauf-Fehler", "with": 2, "items": [
            {"label": "Speicher", "value": 288, "tone": "bad", "with": 2},
            {"label": "Lüfter", "value": 144, "with": 2},
            {"label": "Netzwerk", "value": 86, "with": 2},
            {"label": "Sonstige", "value": 58, "with": 2}]}},
    "p09": {"type": "icons", "items": [
        {"label": "Ziel", "sub": "≤ 2 % in 6 Wochen", "icon": "pin", "tone": "good", "with": 0},
        {"label": "Leitplanken", "sub": "Testzeit, Nachtests, Durchschlupf", "icon": "shield", "with": 1}],
        "then": {"type": "versus", "with": 2, "items": [
            {"label": "Außerhalb des Umfangs", "sub": "Testgrenzen lockern", "icon": "cross", "tone": "bad", "with": 2},
            {"label": "Innerhalb des Umfangs", "sub": "Speicherfehler, Linie 2", "icon": "check", "tone": "good", "with": 2}]}},
    "p10": {"type": "icons", "items": [
        {"label": "Mensch", "icon": "person", "with": 1},
        {"label": "Maschine", "icon": "gear", "with": 1},
        {"label": "Methode", "icon": "clipboard", "with": 1},
        {"label": "Material", "icon": "box", "with": 1},
        {"label": "Messung", "icon": "scale", "with": 1},
        {"label": "Mitwelt", "icon": "wave", "with": 1}]},
    "p11": {"type": "steps", "items": [
        {"label": "Modul nicht ganz eingesetzt", "with": 0},
        {"label": "Verriegelung zu früh geschlossen", "with": 0},
        {"label": "Weniger Platz im neuen Gehäuse", "with": 0},
        {"label": "Anweisungen nicht überprüft", "with": "example"}],
        "then": {"type": "stat", "value": 100, "suffix": "%", "icon": "test", "label": "Fehler nachgestellt",
                 "unit": "Module schräg eingedrückt", "with": 2}},
    "p12": {"type": "flow", "items": [
        {"label": "Einsetzhilfe", "icon": "shape", "with": "example"},
        {"label": "Verriegelungsprüfung", "icon": "sensor", "with": "example"},
        {"label": "Überprüfung bei Gehäuseänderung", "icon": "clipboard", "tone": "good", "with": "example"}],
        "then": {"type": "flow", "with": 2, "items": [
            {"label": "Eindämmung", "sub": "Schützt den Kunden jetzt", "icon": "lock", "with": 2},
            {"label": "Maßnahme", "sub": "Beseitigt die Ursache dauerhaft", "icon": "key", "tone": "good", "with": 2}]}},
    "p13": {"type": "timeline", "items": [
        {"label": "Ursache bestätigen, Pilot", "sub": "Wochen 1–2", "icon": "test", "with": 1},
        {"label": "SOP aktualisieren, schulen", "sub": "Wochen 3–4", "icon": "clipboard", "with": 2},
        {"label": "Ergebnisse prüfen", "sub": "Wochen 5–6", "icon": "check", "tone": "good", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Ausgangslage", "value": 4.8}, "after": {"label": "Pilot", "value": 1.6},
            "decimals": 1, "suffix": "%", "unit": "Server, die beim ersten Boot-Test durchfallen",
            "note": "Ziel ≤ 2 %: erreicht", "with": 1},
    "p15": {"type": "timeline", "items": [
        {"label": "Ein echtes Problem, Ausgangslage", "sub": "Tage 1–5", "icon": "walk", "with": "example"},
        {"label": "Ursachen und Pilot", "sub": "Bis Tag 20", "icon": "search", "with": "example"},
        {"label": "Ihr A3 vorstellen", "sub": "Tag 30", "icon": "clipboard", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Welche ist die beste A3-Problembeschreibung?",
        "options": ["Die Werker sind beim Einsetzen des Speichers nachlässig",
                    "Die Fehler beim ersten Boot-Test an Linie 2 lagen über 4 Wochen im Schnitt bei 4,8 % "
                    "gegenüber 1,5 %",
                    "Wir brauchen zwei Prüfer mehr am Test"],
        "correct": 1,
        "explanation": "Sie nennt Linie, Zeitraum und Messgröße, mit einer Referenz, und behauptet keine "
                       "Ursache. Die anderen sind eine Schuldzuweisung und eine Lösung.",
        "q_script": "Kurzer Check. Welche davon ist die beste A3-Problembeschreibung? Nehmen Sie sich ein "
                    "paar Sekunden.",
        "a_script": "Es ist die zweite. Sie nennt Linie, Zeitraum und Messgröße, und behauptet keine Ursache. "
                    "Die anderen sind eine Schuldzuweisung und eine Lösung.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Karthiks Pilot erreicht das Ziel, aber die Nachtestquote verdoppelt sich. Was sollte er "
                    "tun?",
        "options": ["Trotzdem standardisieren: das Ziel ist erreicht",
                    "Die Leitplanke untersuchen, bevor er standardisiert",
                    "Das Ziel sicherheitshalber auf 3 % anheben"],
        "correct": 1,
        "explanation": "Eine Leitplanke hat sich bewegt, also versteckt die Änderung vielleicht Fehler in "
                       "Nachtests, statt sie zu beseitigen. Verstehen Sie das, bevor Sie standardisieren.",
        "q_script": "Noch eine, und diesmal ist es ein Szenario. Karthiks Pilot erreicht das Ziel, aber die "
                    "Nachtestquote verdoppelt sich. Was sollte er tun? Überlegen Sie kurz.",
        "a_script": "Untersuchen Sie, bevor Sie standardisieren. Eine Leitplanke hat sich bewegt, also "
                    "versteckt die Lösung vielleicht Fehler, statt sie zu beseitigen.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
