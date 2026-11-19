"""low_cost_automation in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh low_cost_automation_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "lc_de"
NAME = "low_cost_automation_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Low Cost Automation": "Lou Kost Otomeeschen",
    "Gemba": "Gemba",
    "Muda": "Muda",
    "Mura": "Mura",
    "Muri": "Muri",
    "ECRS": "e ze err ess",
    "LCA": "ell ze a",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Jedes Lautsprechergitter an Gauravs Linie wurde mit einem Gummihammer eingesetzt. "
    "Vierhundert Schläge pro Stunde, pro Werker. Schmerzende Handgelenke, und lockere Gitter, "
    "die beim Test klapperten. Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie Low "
    "Cost Automation kennen. Sie sehen, wie einfache, sichere Vorrichtungen wiederholte "
    "Arbeit und Fehler beseitigen, ohne eine ganze Roboterlinie. Wir begleiten Gaurav, "
    "Prozessingenieur an einer Linie für Bluetooth-Lautsprecher."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Vereinfachen Sie zuerst, und automatisieren Sie nie "
    "Verschwendung. Wählen Sie die einfachste sichere Lösung, mit Sicherheit als erster "
    "Hürde. Und beweisen Sie den echten Nutzen, dann warten Sie sie wie jede Maschine. Ihre "
    "Aufgabe für diese Woche. Suchen Sie eine wiederholte Bewegung an Ihrer Linie, und fragen "
    "Sie, ob sie wegfallen kann, bevor Sie sie automatisieren. Gut gemacht, Lektion "
    "abgeschlossen. Als Nächstes lernen Sie Muda, Mura und Muri kennen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Low Cost Automation ist",
        "points": [("Einfache, zuverlässige, günstige Vorrichtungen", "einfache, zuverlässige"),
                   ("Wiederholte Arbeit und Fehler beseitigen", "um wiederholte Arbeit"),
                   ("Keine Vollautomatisierung nötig", "ohne direkt")],
        "example": "Gauravs Ziel: Gitter einsetzen, von Hand mit einem Gummihammer.",
        "example_cue": "Gauravs Ziel",
        "script": "Low Cost Automation, kurz LCA, heißt einfache, zuverlässige und günstige Vorrichtungen "
                  "nutzen. Sie nutzen sie, um wiederholte Arbeit zu beseitigen, Fehler zu verhindern und "
                  "die Sicherheit zu verbessern. Und das, ohne direkt auf eine vollautomatische Linie zu "
                  "springen. Denken Sie an Spanner, Führungen, Sensoren und kleine Luftzylinder. Gauravs "
                  "Ziel war das Einsetzen der Gitter, noch von Hand mit einem Gummihammer. Welche Ideen "
                  "leiten die LCA?",
    },
    {
        "key": "p02", "num": 2, "title": "Die Grundhaltung",
        "points": [("Den Bedarf automatisieren, nicht die Komplexität", "Automatisieren Sie den Bedarf"),
                   ("Vereinfachen vor dem Automatisieren", "Vereinfachen Sie, bevor"),
                   ("Menschen in der Schleife halten", "Halten Sie Menschen"),
                   ("Messen, warten", "Und messen Sie")],
        "example": "Ein schicker Roboter wurde mit ₹18 lakh angeboten. Gaurav fragte: Was braucht die Arbeit "
                   "wirklich?",
        "example_cue": "Ein Roboter wurde für",
        "script": "Ein paar Ideen leiten jede gute LCA. Automatisieren Sie den Bedarf, nicht die "
                  "Komplexität. Beginnen Sie beim Problem und der Funktion, die Sie brauchen. Vereinfachen "
                  "Sie, bevor Sie irgendetwas automatisieren. Halten Sie Menschen in der Schleife, damit "
                  "Abweichungen sichtbar bleiben. Und messen Sie den Nutzen, dann warten Sie ihn. Ein "
                  "Roboter wurde für eine Million achthunderttausend Rupien angeboten. Gaurav stellte eine "
                  "Frage. Was braucht diese Arbeit wirklich?",
    },
    {
        "key": "p03", "num": 3, "title": "Wann LCA sinnvoll ist",
        "points": [("Häufige, wiederholte Bewegungen", "in jedem Zyklus wiederholt"),
                   ("Ergonomisches oder Sicherheitsrisiko", "Menschen schadet"),
                   ("Schritte vergessen oder falsch gemacht", "Schritte vergessen werden"),
                   ("Engpass, aber kein Fall für einen Roboter", "einen Engpass")],
        "example": "Gitter einsetzen: jeder Zyklus, Handgelenkbelastung, ungleicher Sitz. Alle vier Punkte "
                   "erfüllt.",
        "example_cue": "Gitter einsetzen erfüllte",
        "script": "LCA ist sinnvoll, wenn eine Bewegung in jedem Zyklus wiederholt wird, viele Male pro "
                  "Schicht. Wenn die Arbeit Menschen schadet oder ein Sicherheitsrisiko schafft. Wenn "
                  "Schritte vergessen werden, vertauscht oder falsch platziert. Und wenn es einen Engpass "
                  "gibt, Vollautomatisierung aber das Geld nicht wert ist. Sie passt auch zu Produkten mit "
                  "unsicherer Menge. Gitter einsetzen erfüllte jeden Punkt. Aber was darf geringe Kosten "
                  "nie bedeuten?",
    },
    {
        "key": "p04", "num": 4, "title": "Geringe Kosten, nie geringe Sicherheit",
        "points": [("Sicherheit ist die erste Konstruktionshürde", "Sicherheit ist die erste"),
                   ("Schutzeinrichtungen, Not-Halt, Risikobeurteilung", "Schutzeinrichtungen, Not-Halt"),
                   ("Ein normaler Sensor ist keine Sicherheitseinrichtung", "ein normaler Sensor")],
        "example": "Gauravs Regel: keine Vorrichtung läuft, bevor das Sicherheitsteam die Risikobeurteilung "
                   "unterschreibt.",
        "example_cue": "Gauravs Regel",
        "script": "Geringe Kosten dürfen nie geringe Sicherheit oder schlechte Technik bedeuten. Sicherheit "
                  "ist die erste Konstruktionshürde, vor Kosten oder Tempo. Schutzeinrichtungen, Not-Halt, "
                  "Risikobeurteilung und Elektronormen gelten weiter. Und denken Sie daran, ein normaler "
                  "Sensor oder eine Steuerung ist nicht automatisch eine Sicherheitseinrichtung. Gauravs "
                  "Regel war einfach. Keine Vorrichtung läuft, bevor das Sicherheitsteam die "
                  "Risikobeurteilung unterschreibt. Welche Arten von LCA gibt es?",
    },
    {
        "key": "p05", "num": 5, "title": "Stufen der LCA",
        "points": [("Mechanisch: Schwerkraft, Federn, Führungen", "Mechanische Hilfen"),
                   ("Pneumatisch: Spanner, Pressen, Greifer", "Pneumatische Hilfen"),
                   ("Sensoren und einfache Steuerungen", "Sensoren erkennen"),
                   ("Die niedrigste Stufe wählen, die funktioniert", "Wählen Sie die niedrigste Stufe")],
        "example": "Manuell → unterstützt → halbautomatisch → automatisch.",
        "example_cue": "Denken Sie an eine Leiter",
        "script": "Es gibt mehrere Stufen. Mechanische Hilfen nutzen Schwerkraft, Federn, Hebel und "
                  "Führungen, ganz ohne Energie. Pneumatische Hilfen nutzen kleine Luftzylinder zum Spannen "
                  "oder Pressen. Sensoren erkennen Anwesenheit, Lage oder Reihenfolge, und einfache "
                  "Steuerungen führen die Schritte aus. Denken Sie an eine Leiter, von manuell bis "
                  "vollautomatisch. Wählen Sie die niedrigste Stufe, die Ihren Bedarf sicher erfüllt. Wo "
                  "fangen Sie an?",
    },
    {
        "key": "p06", "num": 6, "title": "Die LCA-Methode",
        "points": [("Beobachten und messen", "Beobachten Sie die echte Arbeit"),
                   ("Vereinfachen, dann die Funktion definieren", "vereinfachen Sie sie"),
                   ("Konzept, Risikoprüfung, Prototyp", "skizzieren Sie ein Konzept"),
                   ("Prüfen, standardisieren, übertragen", "prüfen Sie es")],
        "example": "Gauravs Ausgangslage: Zyklus 28 s, 18 lockere Gitter pro 1.000 Lautsprecher.",
        "example_cue": "Gauravs Ausgangslage",
        "script": "Folgen Sie einer klaren Methode. Beobachten Sie die echte Arbeit, und messen Sie Zeit, "
                  "Bewegung, Fehler und Risiko. Dann vereinfachen Sie sie, und definieren Sie genau, welche "
                  "Funktion die Vorrichtung erfüllen muss. Als Nächstes skizzieren Sie ein Konzept, prüfen "
                  "die Risiken und bauen einen Prototyp. Schließlich prüfen Sie es, standardisieren es und "
                  "übertragen es, wo es passt. Gauravs Ausgangslage war ein Zyklus von achtundzwanzig "
                  "Sekunden und achtzehn lockere Gitter pro tausend. Was kommt zuerst?",
    },
    {
        "key": "p07", "num": 7, "title": "ECRS vor der Automatisierung",
        "points": [("Eliminieren, kombinieren, umordnen, vereinfachen", "Eliminieren, kombinieren"),
                   ("Erst dann automatisieren", "Erst dann"),
                   ("Automatisierte Verschwendung bleibt Verschwendung", "Automatisierte Verschwendung")],
        "example": "Gaurav strich einen separaten Klopftest: die neue Presse würde den Sitz selbst "
                   "bestätigen.",
        "example_cue": "Gaurav fand",
        "script": "Vereinfachen Sie zuerst, mit ECRS. Eliminieren, kombinieren, umordnen und vereinfachen. "
                  "Erst dann automatisieren Sie, was bleibt. Warum? Weil automatisierte Verschwendung "
                  "Verschwendung bleibt. Nur schneller, teurer und später schwerer zu ändern. Gaurav fand "
                  "einen Schritt, den er vorher streichen konnte. Werker klopften jedes Gitter noch einmal "
                  "ab, nur zur Kontrolle. Eine gut konstruierte Presse konnte den Sitz selbst bestätigen. "
                  "Was sah er am Gemba?",
    },
    {
        "key": "p08", "num": 8, "title": "Gauravs Chance",
        "points": [("Gleiche Bewegung in jedem Zyklus", "dieselbe Bewegung"),
                   ("Ungleiche Kraft, ungleicher Sitz", "ungleiche Kraft"),
                   ("Handgelenkbelastung, jede Schicht", "Handgelenkbelastung")],
        "example": "Lockere Gitter: 18 pro 1.000 Lautsprecher, alle beim Klappertest gefunden.",
        "example_cue": "Lockere Gitter lagen",
        "script": "Am Gemba sah er dieselbe Bewegung in jedem Zyklus. Hammer nehmen, rund um das Gitter "
                  "klopfen, prüfen, Hammer ablegen. Jeder Werker nutzte ungleiche Kraft, also schwankte der "
                  "Sitz. Manche Gitter saßen locker und klapperten beim Test. Und Werker meldeten "
                  "Handgelenkbelastung ab der Schichtmitte. Lockere Gitter lagen bei achtzehn pro tausend "
                  "Lautsprecher. Welche Technik würden Sie wählen?",
    },
    {
        "key": "p09", "num": 9, "title": "Einfache Technik wählen",
        "points": [("Technik passend zur Funktion", "Wählen Sie nach Funktion"),
                   ("Wenige Teile, Normteile", "Nutzen Sie wenige Teile"),
                   ("Leicht zu reinigen, einzustellen und zu reparieren", "Machen Sie es leicht")],
        "example": "Gauravs Wahl: ein kleiner Luftzylinder, ein Aufnahmenest und ein Anwesenheitssensor.",
        "example_cue": "Gaurav wählte",
        "script": "Wählen Sie nach Funktion, nicht weil etwas modern aussieht. Denken Sie an Genauigkeit, "
                  "Zykluszeit, Umgebung und wer es wartet. Nutzen Sie wenige Teile, und Normteile, wo "
                  "möglich. Machen Sie es leicht zu reinigen, einzustellen und zu reparieren. Und der "
                  "Zustand sollte auf einen Blick erkennbar sein. Gaurav wählte einen kleinen Luftzylinder, "
                  "ein Aufnahmenest und einen Anwesenheitssensor. Wie machen Sie das sicher?",
    },
    {
        "key": "p10", "num": 10, "title": "Sicher konstruieren",
        "points": [("Quetschstellen und gespeicherte Energie finden", "Suchen Sie Quetschstellen"),
                   ("Schutz und Zweihandstart", "Ergänzen Sie Schutz"),
                   ("Sicherer Stopp, sicherer Neustart", "Nach einem Stopp")],
        "example": "Ein Zweihandstart hält beide Hände aus dem Pressbereich. Der Luftdruck wird beim Stopp "
                   "abgelassen.",
        "example_cue": "Gauravs Presse",
        "script": "Suchen Sie Quetschstellen, Quetschgefahr, bewegte Teile und gespeicherten Luftdruck. "
                  "Ergänzen Sie Schutz und eine Startart, die Hände aus der Gefahr hält. Nach einem Stopp "
                  "oder Luftverlust muss die Vorrichtung in einen sicheren Zustand gehen, nicht von selbst "
                  "neu starten. Gauravs Presse nutzt einen Zweihandstart, also bleiben beide Hände frei. "
                  "Der Luftdruck wird bei jedem Stopp abgelassen. Würden Ihre Vorrichtungen diesen Test "
                  "bestehen?",
    },
    {
        "key": "p11", "num": 11, "title": "Gauravs Presse",
        "points": [("Nest positioniert den Lautsprecher", "Ein Nest positioniert"),
                   ("Sensor bestätigt, dass das Gitter da ist", "Ein Sensor bestätigt"),
                   ("Geregelte Kraft, Lampe OK oder nicht OK", "geregelter Kraft")],
        "example": "Kein Gitter, kein Pressen. Falsche Lage, kein Pressen. Sitzt: grüne Lampe.",
        "example_cue": "Kein Gitter",
        "script": "Das hat er gebaut. Ein Nest positioniert den Lautsprecher jedes Mal gleich. Ein Sensor "
                  "bestätigt, dass das Gitter da ist und richtig liegt. Dann presst der Zylinder mit "
                  "geregelter Kraft, und eine Lampe zeigt okay oder nicht okay. Kein Gitter, kein Pressen. "
                  "Falsche Lage, kein Pressen. Richtig gesetzt, grünes Licht. Der Werker lädt und entlädt, "
                  "die Presse macht den Rest. Wie viel schneller war es?",
    },
    {
        "key": "p12", "num": 12, "title": "Den echten Gewinn zählen",
        "points": [("Zykluszeit: von 28 s auf 22 s", "Die Zykluszeit sank"),
                   ("Theoretische Leistung: etwa 35 mehr pro Stunde", "etwa fünfunddreißig"),
                   ("Stopps und Wiederanlauf einrechnen", "Rechnen Sie Laden")],
        "example": "Realitätscheck: zwei kurze Klemmer pro Schicht, je eine Minute. Der Gewinn hielt.",
        "example_cue": "Gaurav maß",
        "script": "Die Zykluszeit sank von achtundzwanzig auf zweiundzwanzig Sekunden. Theoretisch sind das "
                  "etwa fünfunddreißig Lautsprecher mehr pro Stunde. Aber trauen Sie nicht nur der Theorie. "
                  "Eine schnelle Station, die ständig stoppt, bremst die ganze Linie. Rechnen Sie Laden, "
                  "Entladen, Kurzstopps, Klemmer und Fehlerbehebung ein. Gaurav maß zwei Wochen lang die "
                  "echte Produktion. Es gab zwei kurze Klemmer pro Schicht, je etwa eine Minute. Der Gewinn "
                  "hielt. Aber war es das Geld wert?",
    },
    {
        "key": "p13", "num": 13, "title": "Kosten und Amortisation",
        "points": [("Gesamtkosten des Besitzes", "Zählen Sie die Gesamtkosten"),
                   ("Nettonutzen, geprüft", "Zählen Sie nur Nutzen"),
                   ("Amortisation = Investition ÷ monatlicher Nutzen", "Amortisation ist")],
        "example": "₹1,2 lakh investiert ÷ ₹30.000 Nettonutzen pro Monat = Amortisation in 4 Monaten.",
        "example_cue": "Gauravs Presse kostete",
        "script": "Zählen Sie die Gesamtkosten des Besitzes. Konstruktion, Teile, Einbau, Schulung, Luft, "
                  "Ersatzteile und Wartung. Zählen Sie nur Nutzen, den Sie prüfen können, wie weniger "
                  "Nacharbeit und frei gewordene Arbeitszeit. Amortisation ist die Investition, geteilt "
                  "durch den monatlichen Nettonutzen. Gauravs Presse kostete hundertzwanzigtausend Rupien. "
                  "Sie sparte dreißigtausend im Monat. Das ist eine Amortisation in vier Monaten. Wie "
                  "halten Sie sie am Laufen?",
    },
    {
        "key": "p14", "num": 14, "title": "Prüfen und warten",
        "points": [("Über alle Modelle und Schichten testen", "Testen Sie sie"),
                   ("Vorbeugende Wartung und Ersatzteile", "Geben Sie ihr einen Wartungsplan"),
                   ("Klare Fehlercodes und Wiederanlauf", "Schreiben Sie klare Fehlercodes")],
        "example": "Lockere Gitter: 18 → 2 pro 1.000. Handgelenkbeschwerden: keine in 60 Tagen.",
        "example_cue": "Lockere Gitter sanken",
        "script": "Testen Sie sie über Modelle und Schichten, bevor Sie sie fertig nennen. Prüfen Sie "
                  "Sicherheit, Qualität, Tempo, Zuverlässigkeit und wie leicht Werker sich von einem Fehler "
                  "erholen. Geben Sie ihr einen Wartungsplan, kritische Ersatzteile und Sensorprüfungen. "
                  "Schreiben Sie klare Fehlercodes, damit Techniker schnell reparieren. Lockere Gitter "
                  "sanken von achtzehn auf zwei pro tausend. Und keine Handgelenkbeschwerden in sechzig "
                  "Tagen. Welche Fehler sollten Sie vermeiden?",
    },
    {
        "key": "p15", "num": 15, "title": "Fehler und Ihr nächster Schritt",
        "points": [("Einen Prozess automatisieren, den Sie nicht verstehen", "Einen Prozess automatisieren"),
                   ("Zuerst die Technik wählen", "Die Technik wählen"),
                   ("Wartung und Ersatzteile vergessen", "Wartung, Ersatzteile")],
        "example": "Gauravs Presse läuft jetzt an drei Linien, übertragen nach der Prüfung, ob sie passt.",
        "example_cue": "Gauravs Presse läuft jetzt",
        "script": "Achten Sie auf häufige Fehler. Einen Prozess automatisieren, den Sie nicht verstehen. "
                  "Die Technik wählen, bevor das Problem definiert ist. Wartung, Ersatzteile und "
                  "Fehlerbehebung vergessen. Theoretische Einsparungen behaupten, die nie geprüft wurden. "
                  "Ignorieren, was Werker Ihnen sagen. Und die Standards danach nicht aktualisieren. "
                  "Gauravs Presse läuft jetzt an drei Linien, übertragen erst nach der Prüfung, ob sie "
                  "jeweils passt. Welche wiederholte Arbeit schauen Sie sich zuerst an?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Einfache Vorrichtungen", "icon": "gear", "with": 0},
        {"label": "Weniger Wiederholung, weniger Fehler", "icon": "check", "with": 1},
        {"label": "Keine ganze Roboterlinie", "icon": "scale", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 400, "icon": "hand", "label": "Hammerschläge pro Stunde",
                 "unit": "pro Werker", "with": "example"}},
    "p02": {"type": "icons", "items": [
        {"label": "Bedarf, nicht Komplexität", "icon": "key", "with": 0},
        {"label": "Zuerst vereinfachen", "icon": "shape", "with": 1},
        {"label": "Menschen in der Schleife", "icon": "person", "with": 2},
        {"label": "Messen, warten", "icon": "wrench", "tone": "good", "with": 3}]},
    "p03": {"type": "icons", "items": [
        {"label": "Wiederholt", "icon": "sequence", "with": 0},
        {"label": "Ergonomisches Risiko", "icon": "warning", "with": 1},
        {"label": "Vergessene Schritte", "icon": "cross", "with": 2},
        {"label": "Engpass", "icon": "clock", "with": 3}]},
    "p04": {"type": "flow", "items": [
        {"label": "Zuerst die Sicherheitshürde", "icon": "shield", "tone": "good", "with": 0},
        {"label": "Schutz, Not-Halt, Risikoprüfung", "icon": "lock", "with": 1},
        {"label": "Vor dem Lauf unterschrieben", "icon": "clipboard", "with": "example"}]},
    "p05": {"type": "ladder", "top": "AUTOMATISCH", "bottom": "MANUELL", "items": [
        {"label": "Sensoren und einfache Steuerungen", "icon": "sensor", "with": 2},
        {"label": "Pneumatische Hilfe", "icon": "gear", "with": 1},
        {"label": "Mechanische Hilfe", "icon": "shape", "with": 0},
        {"label": "Manuell", "icon": "hand", "with": 3}]},
    "p06": {"type": "steps", "items": [
        {"label": "Beobachten, messen", "with": 0}, {"label": "Vereinfachen, definieren", "with": 1},
        {"label": "Konzept, Risiko, Prototyp", "with": 2}, {"label": "Prüfen, standardisieren, übertragen", "with": 3}]},
    "p07": {"type": "steps", "items": [
        {"label": "Eliminieren", "with": 0}, {"label": "Kombinieren", "with": 0},
        {"label": "Umordnen", "with": 0}, {"label": "Vereinfachen", "with": 0},
        {"label": "Dann automatisieren", "with": 1}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Jedes Gitter nachklopfen", "sub": "Gestrichen", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Presse bestätigt den Sitz", "sub": "Eingebaut", "icon": "check", "tone": "good", "with": "example"}]}},
    "p08": {"type": "flow", "items": [
        {"label": "Gleiche Bewegung jeden Zyklus", "icon": "hand", "tone": "bad", "with": 0},
        {"label": "Ungleiche Kraft", "icon": "scale", "tone": "bad", "with": 1},
        {"label": "Handgelenkbelastung", "icon": "warning", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 18, "icon": "wave", "label": "lockere Gitter pro 1.000",
                 "unit": "beim Klappertest gefunden", "with": "example"}},
    "p09": {"type": "icons", "items": [
        {"label": "Luftzylinder", "icon": "gear", "with": "example"},
        {"label": "Aufnahmenest", "icon": "shape", "with": "example"},
        {"label": "Anwesenheitssensor", "icon": "sensor", "with": "example"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Quetschstellen", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Zweihandstart", "icon": "hand", "with": 1},
        {"label": "Luft beim Stopp abgelassen", "icon": "lock", "tone": "good", "with": 2}]},
    "p11": {"type": "flow", "items": [
        {"label": "Nest positioniert", "icon": "shape", "with": 0},
        {"label": "Sensor bestätigt", "icon": "sensor", "with": 1},
        {"label": "Geregeltes Pressen", "icon": "gear", "with": 2},
        {"label": "Grün: sitzt", "icon": "check", "tone": "good", "with": "example"}]},
    "p12": {"type": "compare", "before": {"label": "Hammer", "value": 28}, "after": {"label": "Presse", "value": 22},
            "suffix": " s", "unit": "Zykluszeit pro Lautsprecher", "note": "Etwa 35 mehr pro Stunde, theoretisch", "with": 0},
    "p13": {"type": "bars", "label": "", "note": "Bisherige Einsparung, Tausend ₹: amortisiert in Monat 4", "with": "example", "items": [
        {"label": "Monat 1", "value": 30, "with": "example"},
        {"label": "Monat 2", "value": 60, "with": "example"},
        {"label": "Monat 3", "value": 90, "with": "example"},
        {"label": "Monat 4", "value": 120, "tone": "good", "with": "example"}]},
    "p14": {"type": "compare", "before": {"label": "Hammer", "value": 18}, "after": {"label": "Presse", "value": 2},
            "unit": "lockere Gitter pro 1.000 Lautsprecher", "note": "Keine Handgelenkbeschwerden in 60 Tagen", "with": "example"},
    "p15": {"type": "icons", "items": [
        {"label": "Unbekanntes automatisieren", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Zuerst die Technik", "icon": "gear", "tone": "bad", "with": 1},
        {"label": "Keine Ersatzteile, keine PM", "icon": "wrench", "tone": "bad", "with": 2},
        {"label": "Auf 3 Linien übertragen", "icon": "check", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Was sollten Sie zuerst tun, bevor Sie einen manuellen Schritt automatisieren?",
        "options": ["Die schnellste verfügbare Maschine kaufen",
                    "Ihn mit ECRS vereinfachen und Verschwendung beseitigen",
                    "Die Werker bitten, schneller zu arbeiten"],
        "correct": 1,
        "explanation": "Zuerst vereinfachen: eliminieren, kombinieren, umordnen und vereinfachen. Automatisierte "
                       "Verschwendung bleibt Verschwendung, nur schneller und schwerer zu ändern.",
        "q_script": "Kurzer Check. Was sollten Sie tun, bevor Sie einen manuellen Schritt automatisieren? "
                    "Nehmen Sie sich kurz Zeit.",
        "a_script": "Ihn mit ECRS vereinfachen und Verschwendung beseitigen. Automatisierte Verschwendung "
                    "bleibt Verschwendung, nur schneller und schwerer zu ändern.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Eine neue LCA-Station spart auf dem Papier 6 Sekunden, klemmt aber zehnmal pro Schicht. "
                    "Was sollte das Team tun?",
        "options": ["Ausrollen: die Zykluszeit ist besser",
                    "Die echte Leistung mit den Stopps messen und zuerst die Zuverlässigkeit beheben",
                    "Den Sensor entfernen, damit sie weniger klemmt"],
        "correct": 1,
        "explanation": "Theoretische Zykluszeit ist keine echte Kapazität. Rechnen Sie Klemmer und Wiederanlauf "
                       "ein, beheben Sie die Zuverlässigkeit, und rollen Sie erst dann aus. Einen Sensor zu "
                       "entfernen schwächt die Qualitätskontrolle.",
        "q_script": "Noch eine, ein Szenario. Eine neue Station spart auf dem Papier sechs Sekunden. Aber sie "
                    "klemmt zehnmal pro Schicht. Was sollte das Team tun? Überlegen Sie kurz.",
        "a_script": "Messen Sie die echte Leistung mit den Stopps, und beheben Sie zuerst die "
                    "Zuverlässigkeit. Theorie ist keine Kapazität, und den Sensor zu entfernen würde nur die "
                    "Qualität schwächen.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
