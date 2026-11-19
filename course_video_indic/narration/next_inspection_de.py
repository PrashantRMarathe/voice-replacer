"""next_inspection in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh next_inspection_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ni_de"
NAME = "next_inspection_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "One Point Lesson": "Wann Peunt Lessen",
    "Next Inspection": "Next Inspektschen",
    "Poka Yoke": "Poka Joke",
    "Pareto": "Pareto",
    "Jidoka": "Dschidoka",
    "Andon": "Andon",
    "FMEA": "eff emm e a",
    "CTQ": "ze te ku",
    "SOP": "ess o pe",
    "SMT": "ess emm te",
    "PCB": "pe ze be",
    "MSA": "emm ess a",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Ein lockerer Stecker, an Station drei. Niemand bemerkte ihn. Er lief durch vier weitere "
    "Stationen, Endtest und Verpackung. Dann öffnete ein Kunde den Karton. Kommt Ihnen das "
    "bekannt vor? In dieser Lektion lernen Sie Next Inspection kennen. Sie sehen, wie jeder "
    "Prozess den nächsten schützt und Fehler dort fängt, wo sie entstehen. Wir begleiten "
    "Anita, Qualitätsingenieurin an einer Linie für Sicherheitskameras."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Keinen Fehler machen, keinen weitergeben, keinen annehmen. "
    "Prüfen Sie kritische Punkte so früh wie möglich, und reagieren Sie schnell. Und verlegen "
    "Sie Ihre Kontrollen immer weiter nach vorn, zur Vorbeugung. Ihre Aufgabe für diese "
    "Woche. Wählen Sie eine Übergabe an Ihrer Linie, und notieren Sie, was der nächste "
    "Prozess davon braucht. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie die "
    "One Point Lesson kennen."
)

# One story thread: Anita's security-camera line. Assembly -> firmware -> test ->
# packing. Loose connectors and wrong labels were escaping downstream.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was Next Inspection ist",
        "points": [("Jeder Prozess schützt den nächsten", "jeder Prozess den nächsten schützt"),
                   ("Kritische Punkte vor der Übergabe bestätigen", "Bevor Sie Arbeit weitergeben"),
                   ("Keinen Fehler machen", "Keinen Fehler machen"),
                   ("Keinen Fehler weitergeben", "Keinen Fehler weitergeben"),
                   ("Keinen Fehler annehmen", "Keinen Fehler annehmen")],
        "example": "Anitas Gehäusestation prüft jetzt zuerst die Steckerverriegelung.",
        "example_cue": "An Anitas Linie",
        "script": "Hier ist die Kernidee. Next Inspection heißt, dass jeder Prozess den nächsten schützt. "
                  "Bevor Sie Arbeit weitergeben, bestätigen Sie die kritischen Punkte. Und die empfangende "
                  "Station nimmt einen Fehler nicht stillschweigend an. Sie schickt ihn direkt zurück. Drei "
                  "Regeln fassen es zusammen. Keinen Fehler machen. Keinen Fehler weitergeben. Keinen "
                  "Fehler annehmen. An Anitas Linie prüft die Gehäusestation jetzt zuerst die "
                  "Steckerverriegelung. Warum ist das so wichtig?",
    },
    {
        "key": "p02", "num": 2, "title": "Warum früh fangen",
        "points": [("Fehler kosten bei jedem Schritt mehr", "Ein Fehler wird teurer"),
                   ("Früh erkennen = schnelle Rückmeldung", "Frühes Erkennen gibt"),
                   ("Mehr Prüfung ≠ Qualität", "Mehr Prüfung schafft")],
        "example": "Lockerer Stecker: Sekunden in der Montage → öffnen, reparieren, neu testen nach dem Test "
                   "→ eine Rücksendung beim Kunden.",
        "example_cue": "In der Montage",
        "script": "Ein Fehler wird teurer bei jedem Schritt, den er weiterläuft. In der Montage braucht ein "
                  "lockerer Stecker Sekunden. Nach dem Test öffnen Sie das Gehäuse, reparieren und testen "
                  "neu. Beim Kunden ist es eine Rücksendung, und ein Schaden für Ihren Ruf. Frühes Erkennen "
                  "gibt auch schnelle Rückmeldung. Die Ursache ist noch frisch und leicht zu finden. Aber "
                  "Vorsicht. Mehr Prüfung schafft keine Qualität. Wo sollten Prüfungen also stattfinden?",
    },
    {
        "key": "p03", "num": 3, "title": "Drei Prüfebenen",
        "points": [("Quelle: zuerst die Bedingung prüfen", "Die Quellenprüfung prüft"),
                   ("Selbst: die eigene Arbeit prüfen", "Selbstprüfung heißt"),
                   ("Nächster Prozess: vor der Annahme prüfen", "Die Prüfung im nächsten Prozess")],
        "example": "Anitas Linie: ein Sensor prüft die Ausrichtung, der Monteur bestätigt die Verriegelung, "
                   "der Tester das Modell.",
        "example_cue": "An Anitas Linie",
        "script": "Es gibt drei Ebenen. Die Quellenprüfung prüft die Bedingung, die den Fehler erzeugen "
                  "könnte, bevor er entsteht. Selbstprüfung heißt, Sie prüfen Ihre eigene Arbeit, genau "
                  "dort, wo sie entstand. Die Prüfung im nächsten Prozess heißt, die empfangende Station "
                  "prüft vor der Annahme. An Anitas Linie prüft ein Sensor die Ausrichtung. Der Monteur "
                  "bestätigt die Verriegelung. Und der Tester bestätigt das Modell. Welche Ebene ist am "
                  "stärksten? Die nächste an der Quelle.",
    },
    {
        "key": "p04", "num": 4, "title": "Der nächste Prozess ist mein Kunde",
        "points": [("Der nächste Prozess ist Ihr Kunde", "Der nächste Prozess ist Ihr Kunde"),
                   ("Richtiges Produkt, Menge, Qualität, Etikett, Zeitpunkt", "Er braucht das richtige Produkt"),
                   ("Nie wissentlich ein abweichendes Teil weitergeben", "Geben Sie nie wissentlich"),
                   ("Über Andon melden", "Melden Sie es über Andon")],
        "example": "Anitas Monteure fragten das Firmware-Team: Was braucht ihr von uns?",
        "example_cue": "Anitas Monteure fragten einfach",
        "script": "Sehen Sie jede Übergabe als Verkauf. Der nächste Prozess ist Ihr Kunde. Er braucht das "
                  "richtige Produkt, die richtige Menge und Qualität, das richtige Etikett und den "
                  "richtigen Zeitpunkt. Also folgen Sie der SOP, und bestätigen Sie Ihre kritischen Punkte. "
                  "Geben Sie nie wissentlich ein abweichendes Teil weiter. Melden Sie es über Andon. Anitas "
                  "Monteure fragten einfach das Firmware-Team: Was braucht ihr von uns? Haben Sie Ihren "
                  "nächsten Prozess das je gefragt?",
    },
    {
        "key": "p05", "num": 5, "title": "Führung macht es echt",
        "points": [("Führung stärkt jeden, der für Qualität stoppt", "Führungskräfte müssen jeden stärken"),
                   ("Schnell reagieren, wenn gerufen", "Sie müssen schnell reagieren"),
                   ("Fehler erfassen, um zu lernen, nie um zu beschuldigen", "Und Fehler werden erfasst")],
        "example": "Eine Werkerin stoppte Anitas Linie wegen einer gesprungenen Linse. Ihr Manager dankte "
                   "ihr vor dem Team.",
        "example_cue": "Als eine Werkerin",
        "script": "Das entscheidet über Next Inspection. Ihre Führungskräfte. Wenn Leute trotz Problem "
                  "weiterlaufen sollen, werden Prüfungen zum Abhaken. Führungskräfte müssen jeden stärken, "
                  "der für Qualität stoppt. Sie müssen schnell reagieren, wenn sie gerufen werden. Und "
                  "Fehler werden erfasst, um zu lernen, nie um zu beschuldigen. Als eine Werkerin Anitas "
                  "Linie wegen einer gesprungenen Linse stoppte, dankte ihr der Manager vor dem Team. Was "
                  "würde an Ihrer Linie passieren?",
    },
    {
        "key": "p06", "num": 6, "title": "Was prüfen?",
        "points": [("Prüfungen nach Risiko wählen", "Wählen Sie also nach Risiko"),
                   ("Kunden-CTQ: Funktion, Sicherheit, Passung", "Beginnen Sie mit dem"),
                   ("FMEA und wiederholte Durchschlupfe", "Dann schauen Sie in Ihre FMEA"),
                   ("Wo kann ein falsches Teil oder Etikett hineinrutschen?", "Fragen Sie, wo ein falsches Teil")],
        "example": "Anita wählte vier: Steckerverriegelung, Firmware-Version, Gehäusedichtung und Etikett.",
        "example_cue": "Anita wählte vier",
        "script": "Sie können nicht alles gleich sorgfältig prüfen. Wählen Sie also nach Risiko. Beginnen "
                  "Sie mit dem, was Ihr Kunde spürt, wie Funktion, Sicherheit und Passung. Das sind Ihre "
                  "CTQ-Punkte. Dann schauen Sie in Ihre FMEA, und auf Fehler, die immer wieder "
                  "durchrutschen. Fragen Sie, wo ein falsches Teil, eine Einstellung oder ein Etikett "
                  "hineinrutschen kann. Anita wählte vier: Steckerverriegelung, Firmware-Version, "
                  "Gehäusedichtung und Etikett. Bei hohen Risiken gilt Vorbeugung vor Sichtprüfung. Wie "
                  "bauen Sie ein gutes Prüftor?",
    },
    {
        "key": "p07", "num": 7, "title": "Ein Prüftor gestalten",
        "points": [("Gut und schlecht festlegen, mit Mustern", "Legen Sie zuerst fest"),
                   ("Die Methode wählen", "Dann wählen Sie die Methode"),
                   ("Die Prüfhäufigkeit festlegen", "Legen Sie fest, wie oft"),
                   ("Die Reaktion vorab festlegen", "Und legen Sie die Reaktion")],
        "example": "Anitas Dichtungstor: Grenzmuster auf dem Tisch und eine rote Kiste für Ausschuss.",
        "example_cue": "Anitas Dichtungstor",
        "script": "Ein gutes Tor ist schnell, klar und schwer zu umgehen. Legen Sie zuerst fest, wie gut "
                  "und schlecht aussehen, wo möglich mit Grenzmustern. Dann wählen Sie die Methode, eine "
                  "Lehre, einen Sensor, einen Scan oder eine Sichtprüfung. Legen Sie fest, wie oft Sie "
                  "prüfen. Und legen Sie die Reaktion fest, bevor je ein Fehler auftaucht. Anitas "
                  "Dichtungstor hat Muster auf dem Tisch, und eine rote Kiste für Ausschuss. Was passiert, "
                  "wenn das Tor etwas findet?",
    },
    {
        "key": "p08", "num": 8, "title": "Der Reaktionsplan",
        "points": [("Stoppen oder mit Andon melden", "Stoppen oder melden Sie mit Andon"),
                   ("Fehler, Modell, Seriennummer erfassen", "Erfassen Sie den Fehler"),
                   ("Bis zur letzten guten Einheit eingrenzen", "Grenzen Sie jede Einheit"),
                   ("Korrigieren, bestätigen, vorbeugen", "Korrigieren Sie den Prozess")],
        "example": "Falsche Firmware im Test: jede Einheit seit der letzten guten Prüfung wurde gesperrt.",
        "example_cue": "Als Anitas Tester",
        "script": "Sie reagieren schnell und in fester Reihenfolge. Stoppen oder melden Sie mit Andon. "
                  "Erfassen Sie den Fehler, das Modell und die Seriennummer. Grenzen Sie jede Einheit bis "
                  "zur letzten bekannten guten ein. Korrigieren Sie den Prozess, und bestätigen Sie die "
                  "erste gute Einheit vor dem Neustart. Dann finden Sie die Grundursache und beugen vor. "
                  "Als Anitas Tester falsche Firmware fand, wurde jede Einheit seit der letzten guten "
                  "Prüfung gesperrt. Ein vager Plan bringt Verzögerung und gemischten Bestand.",
    },
    {
        "key": "p09", "num": 9, "title": "Hilfreiche Lean-Werkzeuge",
        "points": [("Poka Yoke stoppt das falsche Teil oder den falschen Schritt", "Poka Yoke verhindert"),
                   ("Jidoka und Andon stoppen und rufen Hilfe", "Jidoka und Andon"),
                   ("Standardarbeit macht gut und schlecht sichtbar", "Standardarbeit und visuelle"),
                   ("FMEA legt Risiken fest, Audits prüfen Kontrollen", "Ihre FMEA legt")],
        "example": "Anita ersetzte eine Sichtprüfung des Etiketts durch einen Scan-Abgleich. Jetzt kann das "
                   "falsche Etikett nicht drucken.",
        "example_cue": "Anita ersetzte eine",
        "script": "Next Inspection wirkt am besten mit anderen Lean-Werkzeugen. Poka Yoke verhindert das "
                  "falsche Teil oder den falschen Schritt ganz. Jidoka und Andon stoppen die Linie und "
                  "rufen Hilfe. Standardarbeit und visuelle Standards machen gut und schlecht sichtbar. "
                  "Ihre FMEA legt die Risiken fest, und Audits prüfen, ob die Kontrollen genutzt werden. "
                  "Anita ersetzte eine Sichtprüfung des Etiketts durch einen Scan-Abgleich. Jetzt kann das "
                  "falsche Etikett nicht drucken. Wo noch?",
    },
    {
        "key": "p10", "num": 10, "title": "Beispiele aus der Elektronik",
        "points": [("SMT: optische Prüfung, geprüfte Feeder", "Bei SMT"),
                   ("Montage: Barcode für die PCB, Schraubenzähler", "In der Montage"),
                   ("Firmware: Versionsverriegelung", "Bei der Firmware"),
                   ("Verpackung: Gewichtsprüfung und Scans", "Bei der Verpackung")],
        "example": "Jede Prüfung sitzt direkt nach dem Schritt, den sie schützt. Die Endprüfung ist das "
                   "letzte Sicherheitsnetz.",
        "example_cue": "Jede Prüfung sitzt direkt",
        "script": "Gehen wir die Linie ab. Bei SMT prüft eine automatische optische Inspektion die "
                  "Platinen, und die Feeder werden geprüft. In der Montage bestätigt ein Barcode die "
                  "richtige PCB, und ein Zähler jede Schraube. Bei der Firmware prüft eine Verriegelung die "
                  "Version vor der Freigabe. Bei der Verpackung fangen Gewichtsprüfung und Scans fehlendes "
                  "Zubehör. Das Muster? Jede Prüfung sitzt direkt nach dem Schritt, den sie schützt. Die "
                  "Endprüfung ist Ihr letztes Netz, nicht Ihr Qualitätssystem.",
    },
    {
        "key": "p11", "num": 11, "title": "Qualität an der Quelle",
        "points": [("Vorn wird nach Standard gebaut", "Vorn wird nach Standard"),
                   ("Hinten wird nur Gutes angenommen", "Hinten wird"),
                   ("Probleme gehen zurück zur Station, die sie verursacht hat", "Jedes Problem geht direkt zurück"),
                   ("Vorsicht vor der Prüffalle", "Vorsicht vor der Prüffalle")],
        "example": "Anitas Linie hatte einst nach jeder Station einen Prüfer. Sie setzte drei in "
                   "Vorbeugeprojekte.",
        "example_cue": "Anitas Linie arbeitete",
        "script": "Next Inspection stützt Qualität an der Quelle. Vorn wird nach Standard gebaut. Hinten "
                  "wird nur gute Arbeit angenommen. Jedes Problem geht direkt zurück zur Station, die es "
                  "verursacht hat, und die Ursache wird behoben. Nun, Vorsicht vor der Prüffalle. Ein "
                  "Prüfer nach jeder Station kostet viel und verbirgt schwache Prozesse. Anitas Linie "
                  "arbeitete früher so. Sie setzte drei Prüfer stattdessen in Vorbeugeprojekte. Können Sie "
                  "den übrigen Prüfungen trauen?",
    },
    {
        "key": "p12", "num": 12, "title": "Können Sie der Prüfung trauen?",
        "points": [("Falsche Annahmen lassen Fehler durch", "Eine falsche Annahme"),
                   ("Falsche Ablehnungen verleiten zum Umgehen", "Eine falsche Ablehnung"),
                   ("Klare Definitionen, Fotos, Grenzmuster", "Definieren Sie Fehler also klar"),
                   ("Prüfer schulen", "Schulen Sie die Prüfer"),
                   ("Lehren kalibrieren, MSA durchführen", "Kalibrieren Sie Lehren"),
                   ("Licht und Sichtabstand steuern", "Steuern Sie Licht")],
        "example": "Anitas zwei Prüfer waren sich bei einer von fünf Dichtungen uneinig. Bessere Muster "
                   "lösten das.",
        "example_cue": "Anitas zwei Prüfer",
        "script": "Eine Prüfung nützt nur, wenn Sie ihr trauen. Eine falsche Annahme lässt einen Fehler "
                  "durch. Eine falsche Ablehnung schafft unnötige Nacharbeit, und Leute umgehen die "
                  "Prüfung. Definieren Sie Fehler also klar, mit Fotos und Grenzmustern. Schulen Sie die "
                  "Prüfer. Kalibrieren Sie Lehren, und machen Sie eine Messsystemanalyse, kurz MSA. Steuern "
                  "Sie Licht und Sichtabstand. Anitas zwei Prüfer waren sich bei einer von fünf Dichtungen "
                  "uneinig. Bessere Muster lösten das. Wie messen Sie Erfolg?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI für Next Inspection",
        "points": [("Erstdurchlaufquote steigt", "Die Erstdurchlaufquote sollte steigen"),
                   ("Durchschlupfquote sinkt", "Die Durchschlupfquote sollte sinken"),
                   ("Nacharbeit, Wiederholfehler, Reaktionszeit", "Beobachten Sie die Nacharbeit"),
                   ("Fehlalarme erfasst", "Und erfassen Sie Fehlalarme")],
        "example": "Quote steigt, Prüfaufwand sinkt = Sie gewinnen.",
        "example_cue": "Wenn die Quote steigt",
        "script": "Erfassen Sie ausgewogene Zahlen. Die Erstdurchlaufquote sollte steigen. Die "
                  "Durchschlupfquote sollte sinken, also Fehler, die später gefunden werden, aber früher "
                  "hätten auffallen sollen. Beobachten Sie die Nacharbeit und Wiederholfehler. Messen Sie "
                  "die Reaktionszeit, vom Signal bis zur Eingrenzung. Und erfassen Sie Fehlalarme, damit "
                  "Sie wissen, dass die Prüfungen verlässlich sind. Wenn die Quote steigt und der "
                  "Prüfaufwand sinkt, gewinnen Sie. Bereit für Anitas Ergebnisse?",
    },
    {
        "key": "p14", "num": 14, "title": "Fallstudie: Kameralinie",
        "points": [("Übergabeprüfungen an 4 Risikopunkten", "Sie setzte Übergabeprüfungen"),
                   ("Reaktionsplan an jedem Tor", "Jedes Tor bekam"),
                   ("Dichtungs- und Etikettprüfung wurden Verriegelungen", "Die Dichtungs- und Etikettprüfung"),
                   ("Wöchentliche Durchschlupfprüfung mit der Quelle", "Und jede Woche")],
        "example": "Nach 8 Wochen: Durchschlupfe 18 → 3 pro Woche, Nacharbeit mehr als halbiert, "
                   "Erstdurchlaufquote 98,5 %.",
        "example_cue": "Nach acht Wochen",
        "script": "Das tat Anita. Sie setzte Übergabeprüfungen an vier Risikopunkte. Jedes Tor bekam einen "
                  "ausgehängten Reaktionsplan. Die Dichtungs- und Etikettprüfung wurden zu Verriegelungen. "
                  "Und jede Woche prüfte sie jeden Durchschlupf mit der verursachenden Station. Nach acht "
                  "Wochen sanken die Durchschlupfe von achtzehn pro Woche auf drei. Die Nacharbeit sank um "
                  "mehr als die Hälfte. Die Erstdurchlaufquote stieg auf achtundneunzigeinhalb Prozent. Wie "
                  "würden Sie das einführen?",
    },
    {
        "key": "p15", "num": 15, "title": "Fahrplan und tägliche Checkliste",
        "points": [("Nach Risiko und Pareto wählen, den Fluss abbilden", "Wählen Sie ein Produkt nach Risiko und Pareto"),
                   ("Prüfungen mit Reaktionsplänen gestalten", "Gestalten Sie die Prüfungen"),
                   ("Pilot an einer Linie, vorher / nachher vergleichen", "Pilotieren Sie an einer Linie"),
                   ("SOP, FMEA, Schulung standardisieren", "Dann standardisieren Sie SOP")],
        "example": "Tägliche Fragen: Sind die Kriterien sichtbar? Können Ihre Werker den Reaktionsplan "
                   "erklären?",
        "example_cue": "Fragen Sie jeden Tag",
        "script": "Führen Sie es Schritt für Schritt ein. Wählen Sie ein Produkt nach Risiko und Pareto. "
                  "Bilden Sie den Fluss ab, und listen Sie die kritischen Punkte. Gestalten Sie die "
                  "Prüfungen an Quelle, selbst und im nächsten Prozess, mit Reaktionsplänen. Pilotieren Sie "
                  "an einer Linie, und vergleichen Sie vorher und nachher. Dann standardisieren Sie SOP, "
                  "FMEA und Schulung. Fragen Sie jeden Tag. Sind die Kriterien sichtbar? Können Ihre Werker "
                  "den Reaktionsplan erklären? Schützen Sie den nächsten Prozess, immer.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Keinen", "sub": "Fehler machen", "icon": "wrench", "with": 2},
        {"label": "Keinen", "sub": "Fehler weitergeben", "icon": "lock", "with": 3},
        {"label": "Keinen", "sub": "Fehler annehmen", "icon": "shield", "with": 4}]},
    "p02": {"type": "flow", "items": [
        {"label": "In der Montage", "sub": "Sekunden zum Beheben", "icon": "wrench", "tone": "good", "with": "example"},
        {"label": "Nach dem Test", "sub": "Öffnen, reparieren, neu testen", "icon": "test", "with": "example"},
        {"label": "Beim Kunden", "sub": "Eine Rücksendung, und ein Schaden für den Ruf", "icon": "box", "tone": "bad", "with": "example"}]},
    "p03": {"type": "ladder", "top": "AM STÄRKSTEN: NAH AN DER QUELLE", "bottom": "LETZTE VERTEIDIGUNGSLINIE", "items": [
        {"label": "Quelle", "icon": "sensor"}, {"label": "Selbst", "icon": "hand"},
        {"label": "Nächster Prozess", "icon": "search"}]},
    "p04": {"type": "flow", "items": [
        {"label": "Ihre Station", "sub": "Der SOP folgen", "icon": "wrench", "with": 0},
        {"label": "Kritische Punkte prüfen", "sub": "Produkt, Menge, Etikett, Zeitpunkt", "icon": "check", "with": 1},
        {"label": "Nächster Prozess", "sub": "Ihr Kunde", "icon": "person", "tone": "good", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Den Stopp stärken", "icon": "shield"}, {"label": "Schnell reagieren", "icon": "clock"},
        {"label": "Lernen, nie beschuldigen", "icon": "person", "tone": "good"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Kunden-CTQ", "sub": "Funktion, Sicherheit, Passung", "icon": "person", "with": 1},
        {"label": "FMEA + Durchschlupfe", "sub": "Was immer wieder durchrutscht", "icon": "clipboard", "with": 2},
        {"label": "Einschleichpunkte", "sub": "Falsches Teil, Einstellung, Etikett", "icon": "label", "with": 3}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Steckerverriegelung", "icon": "lock", "with": "example"},
            {"label": "Firmware-Version", "icon": "chip", "with": "example"},
            {"label": "Gehäusedichtung", "icon": "shield", "with": "example"},
            {"label": "Etikett", "icon": "label", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Gut- und Schlechtmuster", "icon": "shape"}, {"label": "Die Methode", "icon": "sensor"},
        {"label": "Wie oft", "icon": "clock"}, {"label": "Die Reaktion", "icon": "warning"}]},
    "p08": {"type": "flow", "items": [
        {"label": "Stopp: Andon", "icon": "warning", "tone": "bad"},
        {"label": "Erfassen", "sub": "Fehler, Modell, Seriennummer", "icon": "search"},
        {"label": "Eingrenzen", "sub": "Bis zur letzten guten Einheit", "icon": "lock"},
        {"label": "Korrigieren, bestätigen, vorbeugen", "icon": "check", "tone": "good"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Poka Yoke", "icon": "key"}, {"label": "Jidoka + Andon", "icon": "warning"},
        {"label": "Standardarbeit", "icon": "clipboard"}, {"label": "FMEA + Audits", "icon": "shield"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Sichtprüfung des Etiketts", "sub": "Leicht zu übersehen", "icon": "search"},
            {"label": "Scan-Abgleich", "sub": "Falsches Etikett druckt nicht", "icon": "barcode"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "SMT", "sub": "Optische Prüfung, geprüfte Feeder", "icon": "chip"},
        {"label": "Montage", "sub": "PCB-Barcode, Schraubenzähler", "icon": "barcode"},
        {"label": "Firmware", "sub": "Versionsverriegelung", "icon": "lock"},
        {"label": "Verpackung", "sub": "Gewichtsprüfung und Scans", "icon": "scale"}]},
    "p11": {"type": "flow", "items": [
        {"label": "Vorn wird nach Standard gebaut", "icon": "wrench", "with": 0},
        {"label": "Hinten wird nur Gutes angenommen", "icon": "check", "with": 1},
        {"label": "Probleme gehen zurück zur Quelle", "icon": "sequence", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Ein Prüfer nach jeder Station", "sub": "Teuer; verbirgt schwache Prozesse", "icon": "person"},
            {"label": "3 in die Vorbeugung", "sub": "Qualität an der Quelle", "icon": "shield"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Falsche Annahme", "icon": "cross", "tone": "bad"}, {"label": "Falsche Ablehnung", "icon": "warning", "tone": "bad"},
        {"label": "Klare Definitionen", "icon": "clipboard"}, {"label": "Geschulte Prüfer", "icon": "person"},
        {"label": "Kalibrieren, MSA", "icon": "gear"}, {"label": "Licht", "icon": "sensor"}],
        "then": {"type": "stat", "value": 5, "prefix": "1 / ", "icon": "search", "label": "Dichtungen, bei denen die Prüfer uneinig waren",
                 "unit": "Bessere Grenzmuster lösten es", "with": "example"}},
    "p13": {"type": "icons", "items": [
        {"label": "Erstdurchlaufquote", "sub": "Hoch", "icon": "chartUp", "tone": "good"},
        {"label": "Durchschlupfquote", "sub": "Runter", "icon": "chartDown", "tone": "good"},
        {"label": "Nacharbeit, Reaktionszeit", "icon": "clock"},
        {"label": "Fehlalarme", "icon": "warning"}]},
    "p14": {"type": "flow", "items": [
        {"label": "Prüfungen an 4 Risikopunkten", "icon": "search", "tone": "good"},
        {"label": "Reaktionsplan an jedem Tor", "icon": "clipboard", "tone": "good"},
        {"label": "Dichtung + Etikett verriegelt", "icon": "lock", "tone": "good"},
        {"label": "Wöchentliche Durchschlupfprüfung", "icon": "calendar", "tone": "good"}],
        "then": {"type": "compare", "before": {"label": "Vorher", "value": 18}, "after": {"label": "Nach 8 Wochen", "value": 3},
                 "unit": "Durchschlupfe pro Woche", "note": "Erstdurchlaufquote 98,5 %", "with": "example"}},
    "p15": {"type": "steps", "items": [
        {"label": "Nach Risiko wählen", "with": 0}, {"label": "Fluss abbilden", "with": 0},
        {"label": "Prüfungen gestalten", "with": 1}, {"label": "Pilot an einer Linie", "with": 2},
        {"label": "Standardisieren", "with": 3}, {"label": "Täglich fragen", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Ein Sensor stoppt die falsche Steckerausrichtung, bevor das Teil eingebaut wird. Welche "
                    "Prüfebene ist das?",
        "options": ["Quellenprüfung", "Selbstprüfung", "Prüfung im nächsten Prozess"],
        "correct": 0,
        "explanation": "Sie prüft die Bedingung, die den Fehler erzeugen würde, bevor er entsteht. Das ist die "
                       "Quellenprüfung, die stärkste Ebene.",
        "q_script": "Kurzer Check. Ein Sensor stoppt die falsche Steckerausrichtung, bevor das Teil eingebaut "
                    "wird. Welche Prüfebene ist das? Nehmen Sie sich kurz Zeit.",
        "a_script": "Es ist die Quellenprüfung. Sie prüft die Bedingung, bevor der Fehler entstehen kann. Das "
                    "ist die stärkste Ebene.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Der Test findet immer wieder denselben lockeren Stecker aus der Montage, also setzt ein "
                    "Manager einen Prüfer nach die Montage. Was ist besser?",
        "options": ["Sicherheitshalber einen zweiten Prüfer ergänzen", "Den Prüfer behalten und die Ursache in der Montage beheben",
                    "Alle Prüfungen streichen, um Kosten zu sparen", "Den Test bitten, es nicht mehr zu melden"],
        "correct": 1,
        "explanation": "Ein zusätzlicher Prüfer kann das Risiko vorerst eingrenzen, aber ein Wiederholfehler "
                       "heißt, der Prozess muss an der Quelle behoben werden. Dann kann die vorläufige Prüfung "
                       "weg.",
        "q_script": "Noch eine, ein Szenario. Der Test findet immer wieder denselben lockeren Stecker aus der "
                    "Montage. Ein Manager setzt einen Prüfer nach die Montage. Was ist besser? Überlegen Sie "
                    "kurz.",
        "a_script": "Behalten Sie die Prüfung vorerst, aber beheben Sie die Ursache in der Montage. Ein "
                    "Wiederholfehler heißt, der Prozess muss an der Quelle besser werden. Dann kann die "
                    "Zusatzprüfung weg.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
