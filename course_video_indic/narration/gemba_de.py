"""gemba in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh gemba_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "gb_de"
NAME = "gemba_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Genbutsu": "Genbutsu",
    "Genjitsu": "Gendschitsu",
    "Hancho": "Hantscho",
    "Gemba": "Gemba",
    "PPE": "pe pe e",
    "ESD": "e ess de",
    "3G": "drei ge",
    "G": "ge",
    "A": "a",
    "B": "be",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Laut Dashboard war Schicht B nachlässig. Doppelt so viele Ohrhörer fielen beim Audiotest "
    "durch wie in Schicht A. Der Plan war einfach. Schicht B neu schulen. Niemand hatte einen "
    "einzigen defekten Ohrhörer angesehen. Kommt Ihnen das bekannt vor? In dieser Lektion "
    "lernen Sie Gemba kennen, und die 3G dahinter. Sie sehen, wie man an den echten Ort geht, "
    "das echte Ding prüft und die echten Fakten checkt. Wir begleiten Manoj, "
    "Produktionsleiter an einer Linie für kabellose Ohrhörer."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Gehen Sie an den echten Ort, und beobachten Sie echte "
    "Zyklen, bevor Sie entscheiden. Nehmen Sie das echte Ding in die Hand, und vergleichen "
    "Sie es mit einem guten. Und prüfen Sie die echten Fakten, mit Zählungen, Zeiten und "
    "einem Nenner. Ihre Aufgabe für diese Woche. Nehmen Sie ein wiederkehrendes Problem, und "
    "machen Sie einen dreißigminütigen 3G-Besuch. Gut gemacht, Lektion abgeschlossen. Als "
    "Nächstes lernen Sie Hancho kennen, Führung in der Fertigung."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Hingehen und schauen",
        "points": [("Gemba: der echte Ort", "Gemba bedeutet"),
                   ("Genbutsu: das echte Ding", "Genbutsu bedeutet"),
                   ("Genjitsu: die echten Fakten", "Genjitsu bedeutet")],
        "example": "Manojs Regel: keine Entscheidung über Schicht B, bevor er einen defekten Ohrhörer in der "
                   "Hand hatte.",
        "example_cue": "Manoj stellte eine Regel auf",
        "script": "Lean hat eine einfache Gewohnheit. Hingehen und schauen, bevor Sie entscheiden. Sie "
                  "kommt als drei japanische Wörter, oft die 3G genannt. Gemba bedeutet der echte Ort, wo "
                  "die Arbeit passiert. Genbutsu bedeutet das echte Ding, wie das defekte Teil. Genjitsu "
                  "bedeutet die echten Fakten. Manoj stellte eine Regel auf. Keine Entscheidung über "
                  "Schicht B, bevor er einen defekten Ohrhörer in der Hand hielt. Warum ist das wichtig?",
    },
    {
        "key": "p02", "num": 2, "title": "Warum Berichte nicht reichen",
        "points": [("Dashboards zeigen Symptome", "Dashboards zeigen"),
                   ("Berichte verbergen den Zusammenhang", "Berichte verbergen"),
                   ("Fakten stoppen die Schuldzuweisung", "Und Fakten stoppen")],
        "example": "Das Dashboard zeigte die Fehler von Schicht B. Es zeigte nicht, warum.",
        "example_cue": "Manojs Dashboard",
        "script": "Weil Berichte nur einen Teil der Geschichte erzählen. Dashboards zeigen Symptome, keine "
                  "Ursachen. Berichte verbergen Abläufe, Umgehungen und den Zusammenhang. Ein Teil, eine "
                  "Vorrichtung oder ein Arbeitsplatz zeigt oft Belege, die keine Tabelle zeigen kann. Und "
                  "Fakten stoppen die Schuldzuweisung, und das Geld für die falsche Lösung. Manojs "
                  "Dashboard zeigte, dass Schicht B mehr Fehler hatte. Es konnte nicht zeigen, warum. Wo "
                  "fangen Sie also an?",
    },
    {
        "key": "p03", "num": 3, "title": "3G auf einen Blick",
        "points": [("Wo ist es passiert?", "Gemba fragt"),
                   ("Was genau war betroffen?", "Genbutsu fragt"),
                   ("Was ist wirklich passiert?", "Genjitsu fragt")],
        "example": "Linie 2 · Audiotest · linker Ohrhörer · 22 von 1.100 in Schicht B",
        "example_cue": "Für Manoj",
        "script": "Sehen Sie jedes G als Frage. Gemba fragt, wo ist es passiert? Die Linie, die Station, "
                  "der Schritt. Genbutsu fragt, was genau war betroffen? Die Einheit, das Teil, das "
                  "Werkzeug. Genjitsu fragt, was ist wirklich passiert? Zeiten, Zählungen und Messungen. "
                  "Für Manoj waren es Linie zwei, der Audiotest und der linke Ohrhörer. Zweiundzwanzig "
                  "Fehler von elfhundert, in Schicht B. Gehen wir also an den Ort.",
    },
    {
        "key": "p04", "num": 4, "title": "Gemba: der echte Ort",
        "points": [("Eine klare Frage haben", "Beginnen Sie mit einer klaren Frage"),
                   ("Den Bereichsverantwortlichen informieren, PPE tragen", "Informieren Sie den Bereichsverantwortlichen"),
                   ("Mehrere ganze Zyklen beobachten", "Beobachten Sie mehrere"),
                   ("Mit dem Standard vergleichen", "Vergleichen Sie, was Sie sehen")],
        "example": "Manojs Frage: Was ist beim Audiotest in Schicht B anders?",
        "example_cue": "Manojs Frage",
        "script": "Beginnen Sie mit einer klaren Frage und einem Zielprozess. Informieren Sie den "
                  "Bereichsverantwortlichen, dass Sie kommen, und halten Sie die Regeln für PPE und ESD "
                  "ein. Beobachten Sie mehrere ganze Zyklen, ohne einzugreifen. Vergleichen Sie, was Sie "
                  "sehen, mit der freigegebenen Standardarbeit. Dann stellen Sie neutrale Fragen und "
                  "notieren jede Lücke mit Zeit und Ort. Manojs Frage war kurz. Was ist beim Audiotest in "
                  "Schicht B anders? Wie sollten Sie sich dort verhalten?",
    },
    {
        "key": "p05", "num": 5, "title": "Gemba-Umgangsformen",
        "points": [("Keine Überraschungsprüfung", "ist keine Überraschungsprüfung"),
                   ("Zuhören vor Vorschlägen", "Hören Sie zu, bevor"),
                   ("Nie nach einem Zyklus urteilen", "urteilen Sie nie")],
        "example": "Manoj blieb eine ganze Stunde in Schicht B und fragte: „Was macht diese Arbeit schwer?“",
        "example_cue": "Manoj blieb eine ganze Stunde in Schicht B",
        "script": "Ein Gemba-Besuch ist keine Überraschungsprüfung und keine Suche nach Schuldigen. Hören "
                  "Sie zu, bevor Sie etwas vorschlagen. Unterbrechen Sie keine kritische Arbeit. Und "
                  "urteilen Sie nie nach einem Zyklus, denn ein Zyklus kann täuschen. Manoj blieb eine "
                  "ganze Stunde in Schicht B. Er stellte eine Frage. Was macht diese Arbeit für Sie schwer? "
                  "Die Antworten überraschten ihn. Aber was sollten Sie in die Hand nehmen?",
    },
    {
        "key": "p06", "num": 6, "title": "Genbutsu: das echte Ding",
        "points": [("Die defekte Einheit, das Teil, das Werkzeug", "Das heißt die defekte Einheit"),
                   ("Modell, Charge, Zeit, Station notieren", "Notieren Sie Modell"),
                   ("Schlecht mit gut vergleichen", "Vergleichen Sie eine schlechte Einheit")],
        "example": "Defekte linke Ohrhörer: matte, körnige Lötstelle am Lautsprecherdraht. Gute: glänzend "
                   "und glatt.",
        "example_cue": "Manoj verglich",
        "script": "Nehmen Sie das echte Ding in die Hand. Das heißt die defekte Einheit, das Bauteil, die "
                  "Vorrichtung oder das Werkzeug. Notieren Sie Modell, Charge, Zeit und Station, bevor Sie "
                  "es anfassen. Prüfen Sie es, ohne den Beleg zu verändern. Vergleichen Sie eine schlechte "
                  "Einheit mit einer guten, nebeneinander, im gleichen Licht. Manoj verglich defekte linke "
                  "Ohrhörer mit guten. Die fehlerhaften Lötstellen sahen matt und körnig aus. Was könnte "
                  "das verursachen?",
    },
    {
        "key": "p07", "num": 7, "title": "Sicherheit zuerst",
        "points": [("Nie eine Verriegelung überbrücken", "Überbrücken Sie nie"),
                   ("Vor dem Öffnen sperren", "Sperren Sie zuerst"),
                   ("ESD-Handhabung für Elektronik", "behandeln Sie Elektronik")],
        "example": "Manoj bat den Techniker, den Lötkolben abkühlen zu lassen und zu sperren, bevor er ihn "
                   "prüfte.",
        "example_cue": "Manoj bat den Techniker",
        "script": "Eine Regel schlägt die Neugier. Überbrücken Sie nie eine Verriegelung, und öffnen Sie "
                  "nie eine Anlage unter Spannung, nur um das echte Ding zu sehen. Sperren Sie zuerst, und "
                  "lassen Sie eine qualifizierte Person ran. Behandeln Sie Elektronik mit ESD-Schutz, sonst "
                  "schaffen Sie beim Untersuchen neue Fehler. Manoj bat den Techniker, die Lötstation "
                  "abkühlen zu lassen und zu sperren, bevor er sie prüfte. Ein sicherer Beleg ist ein guter "
                  "Beleg. Und die Fakten?",
    },
    {
        "key": "p08", "num": 8, "title": "Genjitsu: die echten Fakten",
        "points": [("Fakten, keine Meinungen", "Ersetzen Sie Meinungen"),
                   ("Zählungen mit Nenner", "Nutzen Sie Zählungen"),
                   ("Ein Signal ist kein Beweis", "ist ein Signal")],
        "example": "Schicht B: 22 von 1.100 (2,0 %). Schicht A: 9 von 1.050 (0,9 %).",
        "example_cue": "Schicht B hatte",
        "script": "Ersetzen Sie Meinungen durch Fakten. Der Test ist langsam, ist eine Meinung. Die "
                  "mittlere Testzeit stieg von sechsundvierzig auf einundsechzig Sekunden, ist ein Fakt. "
                  "Nutzen Sie Zählungen mit Nenner und Zeitstempel, denen Sie trauen können. Schicht B "
                  "hatte zweiundzwanzig Fehler von elfhundert. Schicht A hatte neun von etwa tausend. "
                  "Dieser Unterschied ist ein Signal zum Untersuchen. Aber beweist er, dass Schicht B die "
                  "Ursache war?",
    },
    {
        "key": "p09", "num": 9, "title": "Eine verbundene Untersuchung",
        "points": [("Zuerst definieren und eindämmen", "Definieren Sie das Problem"),
                   ("Ort, Ding, Fakten, zusammen", "gehen Sie an den Ort"),
                   ("Ursachen testen, bevor Sie beheben", "Dann testen Sie")],
        "example": "Manoj sperrte zuerst die verdächtigen Ohrhörer aus Schicht B.",
        "example_cue": "Manoj sperrte zuerst",
        "script": "Nein. Nutzen Sie die 3G also als eine verbundene Untersuchung, nicht als drei Kästchen "
                  "zum Abhaken. Definieren Sie das Problem in Zahlen, und schützen Sie zuerst Ihren Kunden. "
                  "Dann gehen Sie an den Ort, prüfen das Ding und sammeln die Fakten, zusammen. Dann testen "
                  "Sie mögliche Ursachen, bevor Sie etwas dauerhaft ändern. Manoj sperrte zuerst alle "
                  "verdächtigen Ohrhörer aus Schicht B. Dann ging er zurück zur Station. Was zeigte ihm der "
                  "Ort?",
    },
    {
        "key": "p10", "num": 10, "title": "Was der Ort zeigte",
        "points": [("Gleiche Menschen, gleiche Methode", "folgte derselben Methode"),
                   ("Eine andere Lötspitze", "die Lötspitze"),
                   ("Am Montagabend gewechselt", "am Montagabend gewechselt")],
        "example": "Der Lötkolben von Schicht B hatte eine kleinere Spitze aus dem Ersatzteillager. Nicht "
                   "die Standardspitze.",
        "example_cue": "Sie stammte",
        "script": "Zuerst sah nichts falsch aus. Schicht B folgte derselben Methode wie Schicht A, Schritt "
                  "für Schritt. Dann sah Manoj sich die Lötspitze genau an. Sie war kleiner als die an der "
                  "Station von Schicht A. Sie war am Montagabend gewechselt worden. Sie stammte aus dem "
                  "Ersatzteillager und war nicht die Standardspitze. Könnte eine kleinere Spitze eine "
                  "schwächere Lötstelle machen? Wie würden Sie es herausfinden?",
    },
    {
        "key": "p11", "num": 11, "title": "Was die Fakten zeigten",
        "points": [("Fehler nach Station und Zeit", "Manoj ordnete"),
                   ("Begannen direkt nach dem Spitzenwechsel", "begannen in der Schicht"),
                   ("Ein kontrollierter Versuch bestätigte es", "Dann ein kontrollierter Versuch")],
        "example": "Versuch: Standardspitze 1 Fehler von 300. Kleinere Spitze: 7 von 300.",
        "example_cue": "Mit der Standardspitze",
        "script": "Manoj ordnete jeden Fehler nach Station, Zeit und Charge. Sie begannen in der Schicht "
                  "nach dem Spitzenwechsel, und nur an dieser Station. Dann ein kontrollierter Versuch, von "
                  "der Technik freigegeben, testete beide Spitzen. Mit der Standardspitze fiel ein Ohrhörer "
                  "von dreihundert aus. Mit der kleineren Spitze fielen sieben aus. Die kleinere Spitze "
                  "brachte nicht genug Wärme in die Lötstelle. War Schicht B also nachlässig?",
    },
    {
        "key": "p12", "num": 12, "title": "3G liefert die Grundursache",
        "points": [("Jedes Warum mit Belegen", "Jedes Warum"),
                   ("Nie bei „Werkerfehler“ aufhören", "Hören Sie nie"),
                   ("Fragen, was den Fehler möglich machte", "Fragen Sie, welcher Zustand")],
        "example": "Grundursache: das Ersatzteillager führte die falsche Spitze, und der Standard nannte sie "
                   "nicht.",
        "example_cue": "Manojs letztes Warum",
        "script": "Nein. Die 3G liefern Ihren Ursachenwerkzeugen echte Belege. Bei den fünf Warum muss "
                  "jedes Warum auf etwas beruhen, das Sie gesehen oder gemessen haben. Hören Sie nie bei "
                  "Werkerfehler oder mehr Schulung auf. Fragen Sie, welcher Zustand im Prozess den Fehler "
                  "möglich machte. Manojs letztes Warum war klar. Das Ersatzteillager führte die falsche "
                  "Spitze, und der Standard nannte den Spitzentyp nicht. Was änderte er also?",
    },
    {
        "key": "p13", "num": 13, "title": "Beheben und prüfen",
        "points": [("Richtige Spitze, im Standard genannt", "nannte jetzt den Spitzentyp"),
                   ("Spitzenprüfung zu jedem Schichtbeginn", "eine Spitzenprüfung"),
                   ("Über fünf Schichten geprüft", "prüfte er das Ergebnis")],
        "example": "Schicht B: von 20 auf 8 pro 1.000, gleichauf mit Schicht A.",
        "example_cue": "Die Fehler von Schicht B",
        "script": "Die Lösung war einfach. Der Standard nannte jetzt den Spitzentyp, und das "
                  "Ersatzteillager führte nur die richtige. Eine Spitzenprüfung kam in die Routine zum "
                  "Schichtbeginn. Dann prüfte er das Ergebnis über fünf ganze Schichten, nicht über eine "
                  "gute Stunde. Die Fehler von Schicht B sanken von zwanzig pro tausend auf acht, gleichauf "
                  "mit Schicht A. Und Schicht B brauchte nie eine neue Schulung. Wie machen Sie daraus eine "
                  "tägliche Gewohnheit?",
    },
    {
        "key": "p14", "num": 14, "title": "Der 30-Minuten-Gemba-Rundgang",
        "points": [("Zuerst Zweck und Sicherheit", "prüfen Sie zuerst Sicherheit"),
                   ("Beobachten, dann Ding und Daten prüfen", "beobachten Sie den Prozess"),
                   ("Eindämmung und Verantwortlichen vereinbaren", "vereinbaren Sie die Eindämmung")],
        "example": "Manojs Frage an jedem Halt: „Was ist der Standard, und was passiert wirklich?“",
        "example_cue": "Manojs Lieblingsfrage",
        "script": "Machen Sie es zur Standardarbeit. Bei einem dreißigminütigen Rundgang prüfen Sie zuerst "
                  "Sicherheit, Lücke und Zweck. Dann beobachten Sie den Prozess zehn Minuten am "
                  "Arbeitsplatz. Prüfen Sie das betroffene Teil und die wichtigen Daten. Fragen Sie das "
                  "Team nach Ursachen, vereinbaren Sie die Eindämmung, und benennen Sie einen "
                  "Verantwortlichen mit Termin. Manojs Lieblingsfrage ist einfach. Was ist der Standard, "
                  "und was passiert wirklich? Was würden Sie fragen?",
    },
    {
        "key": "p15", "num": 15, "title": "Fehler, die Sie vermeiden sollten",
        "points": [("Vom Dashboard aus führen", "Nur vom Dashboard"),
                   ("Eine Probe für die Wahrheit halten", "Eine einzelne Probe"),
                   ("Nach einer Schulung abschließen", "Ein Problem abschließen")],
        "example": "Manoj verbringt jetzt die ersten 30 Minuten jeder Schicht am Gemba.",
        "example_cue": "Manoj verbringt jetzt",
        "script": "Achten Sie auf ein paar häufige Fehler. Nur vom Dashboard aus führen. Sich auf Gespräche "
                  "verlassen, ohne das Teil in der Hand. Eine einzelne Probe für die Wahrheit halten. "
                  "Einstellungen während der Untersuchung ändern und Belege zerstören. Ein Problem "
                  "abschließen nach einer Schulung, ohne zu prüfen, ob es aufhörte. Manoj verbringt jetzt "
                  "die ersten dreißig Minuten jeder Schicht am Gemba. Könnten Sie das auch?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Gemba", "sub": "Echter Ort", "icon": "walk", "with": 0},
        {"label": "Genbutsu", "sub": "Echtes Ding", "icon": "wave", "with": 1},
        {"label": "Genjitsu", "sub": "Echte Fakten", "icon": "search", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Dashboard", "sub": "Zeigt Symptome", "icon": "chartUp", "with": 0},
        {"label": "Der echte Ort", "sub": "Zeigt Ursachen", "icon": "walk", "tone": "good", "with": 2}]},
    "p03": {"type": "flow", "items": [
        {"label": "Wo?", "sub": "Linie 2, Audiotest", "icon": "pin", "with": 0},
        {"label": "Was?", "sub": "Linker Ohrhörer", "icon": "wave", "with": 1},
        {"label": "Was ist passiert?", "sub": "22 von 1.100", "icon": "count", "with": 2}]},
    "p04": {"type": "steps", "items": [
        {"label": "Klare Frage", "with": 0}, {"label": "Verantwortlicher, PPE, ESD", "with": 1},
        {"label": "Ganze Zyklen beobachten", "with": 2}, {"label": "Mit Standard vergleichen", "with": 3}]},
    "p05": {"type": "versus", "items": [
        {"label": "Überraschungsprüfung", "sub": "Schuldige suchen", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Respektvoller Besuch", "sub": "„Was macht das schwer?“", "icon": "person", "tone": "good", "with": "example"}]},
    "p06": {"type": "versus", "items": [
        {"label": "Defekter Ohrhörer", "sub": "Matte, körnige Lötstelle", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "Guter Ohrhörer", "sub": "Glänzende, glatte Lötstelle", "icon": "check", "tone": "good", "with": "example"}]},
    "p07": {"type": "icons", "items": [
        {"label": "Keine überbrückten Verriegelungen", "icon": "lock", "with": 0},
        {"label": "Zuerst sperren", "icon": "key", "with": 1},
        {"label": "ESD-Schutz", "icon": "shield", "tone": "good", "with": 2}]},
    "p08": {"type": "bars", "label": "", "note": "Fehler pro 1.000 Ohrhörer: ein Signal, kein Beweis", "with": "example", "items": [
        {"label": "Schicht A", "value": 9, "with": "example"},
        {"label": "Schicht B", "value": 20, "tone": "bad", "with": "example"}]},
    "p09": {"type": "steps", "items": [
        {"label": "Definieren und eindämmen", "with": 0},
        {"label": "Ort", "with": 1}, {"label": "Ding", "with": 1}, {"label": "Fakten", "with": 1},
        {"label": "Ursachen testen", "with": 2}]},
    "p10": {"type": "versus", "items": [
        {"label": "Spitze von Schicht B", "sub": "Kleiner, aus dem Ersatzteillager", "icon": "wrench", "tone": "bad", "with": 1},
        {"label": "Standardspitze", "sub": "Schicht A", "icon": "check", "tone": "good", "with": 1}]},
    "p11": {"type": "bars", "label": "", "note": "Kontrollierter Versuch: Fehler bei 300 Ohrhörern", "with": "example", "items": [
        {"label": "Standardspitze", "value": 1, "tone": "good", "with": "example"},
        {"label": "Kleinere Spitze", "value": 7, "tone": "bad", "with": "example"}]},
    "p12": {"type": "steps", "items": [
        {"label": "Schwache Lötstellen", "with": 0},
        {"label": "Kleinere Spitze, zu wenig Wärme", "with": 0},
        {"label": "Falsche Spitze im Ersatzteillager", "with": "example"},
        {"label": "Spitzentyp nicht im Standard", "with": "example"}]},
    "p13": {"type": "compare", "before": {"label": "Vorher", "value": 20}, "after": {"label": "Nachher", "value": 8},
            "unit": "Fehler pro 1.000 Ohrhörer, Schicht B", "note": "Gleichauf mit Schicht A, über 5 Schichten geprüft", "with": "example"},
    "p14": {"type": "timeline", "items": [
        {"label": "Sicherheit, Lücke, Zweck", "sub": "0–5", "icon": "shield", "with": 0, "span": 5},
        {"label": "Beobachten", "sub": "5–15", "icon": "walk", "with": 1, "span": 10},
        {"label": "Ding und Daten", "sub": "15–22", "icon": "search", "with": 1, "span": 7},
        {"label": "Ursachen, Verantwortlicher", "sub": "22–30", "icon": "person", "tone": "good", "with": 2, "span": 8}]},
    "p15": {"type": "icons", "items": [
        {"label": "Nur Dashboard", "icon": "chartUp", "tone": "bad", "with": 0},
        {"label": "Eine Probe", "icon": "count", "tone": "bad", "with": 1},
        {"label": "Nach Schulung geschlossen", "icon": "clipboard", "tone": "bad", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Welche Aussage ist ein echter Fakt (Genjitsu)?",
        "options": ["„Schicht B ist immer nachlässig.“",
                    "„Der Lieferant hat es verursacht.“",
                    "„18 von 24 Fehlern kamen aus Charge B.“"],
        "correct": 2,
        "explanation": "Ein Fakt hat Zählungen, einen Nenner und einen prüfbaren Umfang. Die anderen sind "
                       "Meinungen, und die Lieferantenbehauptung ist unbewiesen.",
        "q_script": "Kurzer Check. Welche dieser Aussagen ist ein echter Fakt? Nehmen Sie sich kurz Zeit.",
        "a_script": "Die letzte. Sie hat eine Zählung, einen Nenner und einen prüfbaren Umfang. Die anderen "
                    "zwei sind nur Meinungen.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Das Dashboard zeigt eine Schicht mit doppelt so vielen Fehlern. Der Leiter will diese "
                    "Schicht neu schulen. Was zuerst?",
        "options": ["Heute schulen: die Daten sind klar",
                    "An die Station gehen, die defekten Einheiten in die Hand nehmen und die Fakten prüfen",
                    "Die Werker der zwei Schichten tauschen"],
        "correct": 1,
        "explanation": "Ein Unterschied zwischen Schichten ist ein Signal, kein Beweis. Gehen Sie hin: echter "
                       "Ort, echtes Ding und echte Fakten, bevor Sie über eine Lösung entscheiden.",
        "q_script": "Noch eine, diesmal ein Szenario. Das Dashboard zeigt eine Schicht mit doppelt so vielen "
                    "Fehlern. Der Leiter will sie neu schulen. Was sollte zuerst passieren? Überlegen Sie "
                    "kurz.",
        "a_script": "Hingehen und schauen. Besuchen Sie die Station, nehmen Sie defekte Einheiten in die "
                    "Hand, und prüfen Sie Fakten. Ein Schichtunterschied ist kein Beweis.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
