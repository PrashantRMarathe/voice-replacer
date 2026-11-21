"""x_matrix in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh x_matrix_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "xm_de"
NAME = "x_matrix_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Hoshin Kanri": "Hoschin Kanri",
    "X-Matrix": "Ix-Matrix",
    "Yamazumi": "Jamasumi",
    "Kaizen": "Kaisen",
    "RACI": "Rassi",
    "KPI": "ka pe i",
    "BOM": "be o emm",
    "SMED": "Smed",
    "IT": "i te",
    "Plan": "plän",
    "Check": "tscheck",
    "Act": "äkt",
    "Do": "duh",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Vierzig Verbesserungsprojekte. Jedes Team beschäftigt. Und doch rutschte die Lieferung, "
    "Quartal für Quartal. Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie die "
    "X-Matrix kennen, das einseitige Herz von Hoshin Kanri. Sie sehen, wie Sie wenige große "
    "Ziele mit den Projekten und Zahlen verbinden, die sie beweisen. Wir begleiten Arjun, "
    "Betriebsleiter in einem Elektronikwerk, der ein volles Portfolio fokussiert."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Wählen Sie wenige echte Prioritäten, keine Wunschliste. "
    "Verbinden Sie jedes Ziel mit einem Projekt, einem KPI und einem Verantwortlichen. Und "
    "prüfen Sie ehrlich, denn die Zahlen müssen sich bewegen, nicht nur das Diagramm. Ihre "
    "Aufgabe für diese Woche. Schreiben Sie ein Ziel für Ihren Bereich als Ergebnis, nicht "
    "als Tätigkeit. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie Yamazumi "
    "kennen, das Abstimmen der Arbeit an Ihrer Linie."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "X-Matrix und Hoshin Kanri",
        "points": [("Ihre ganze Strategie auf einer Seite", "bringt Ihre ganze Strategie"),
                   ("Ziele → Jahresziele → Projekte → Zielwerte → Verantwortliche", "Sie verbindet langfristige Ziele"),
                   ("Eine kurze Liste echter Maßnahmen", "Ihre Aufgabe ist"),
                   ("Kein Diagramm für die Wand", "Sie ist kein buntes Diagramm")],
        "example": "Arjun will verlässliche Lieferung und weniger Fehler. Kann er dieses Ziel bis zur Arbeit "
                   "in der Fertigung verfolgen?",
        "example_cue": "Arjun will verlässliche Lieferung",
        "script": "Hier ist die Kernidee. Die X-Matrix bringt Ihre ganze Strategie auf eine Seite. Sie "
                  "verbindet langfristige Ziele, die Jahresziele, Verbesserungsprojekte, messbare Zielwerte "
                  "und die Verantwortlichen dahinter. Ihre Aufgabe ist, Strategie in eine kurze Liste "
                  "echter Maßnahmen zu verwandeln. Sie ist kein buntes Diagramm für die Wand. Arjun will "
                  "verlässliche Lieferung und weniger Fehler. Kann er dieses Ziel bis zur Arbeit in der "
                  "Fertigung verfolgen? Aber woher kommt die Methode?",
    },
    {
        "key": "p02", "num": 2, "title": "Ursprung und Ausrichtung",
        "points": [("Hoshin Kanri: Richtungsmanagement", "Grob heißt es"),
                   ("Richtung und tägliche Arbeit ausrichten", "Es richtet aus"),
                   ("Prioritäten auf das Machbare begrenzen", "Begrenzen Sie also Ihre Prioritäten"),
                   ("In beide Richtungen, nicht von oben", "Und führen Sie das Gespräch")],
        "example": "Arjuns Werk lief Dutzende lokale Kaizen-Projekte. Nur wenige halfen der Lieferung "
                   "wirklich.",
        "example_cue": "Sein Werk lief Dutzende",
        "script": "Hoshin Kanri ist ein japanischer Ansatz. Grob heißt es Richtungsmanagement. Es richtet "
                  "aus, wohin Sie gehen, mit dem, was Sie täglich wirklich tun. Die X-Matrix ist einfach "
                  "das Bild dieser Ausrichtung. Das ist die Falle, die Arjun fand. Sein Werk lief Dutzende "
                  "lokale Kaizen-Projekte. Nur wenige halfen der Lieferung an den Kunden wirklich. "
                  "Begrenzen Sie also Ihre Prioritäten auf das, was Sie ausstatten können. Und führen Sie "
                  "das Gespräch in beide Richtungen, nicht nur von oben. Was kommt auf die Seite?",
    },
    {
        "key": "p03", "num": 3, "title": "Vier Kernbereiche",
        "points": [("Durchbruchsziele: 3–5 Jahre", "Erstens, Durchbruchsziele"),
                   ("Jahresziele: dieses Jahr", "Zweitens, Jahresziele"),
                   ("Verbesserungsprojekte", "Drittens, Verbesserungsprojekte"),
                   ("KPI und Zielwerte: der Beweis", "Viertens, KPI und Zielwerte")],
        "example": "Arjuns Kette reicht von Weltklasse-Qualität bis zu einem Ausbeute-Zielwert.",
        "example_cue": "Arjuns Kette reicht",
        "script": "Eine typische X-Matrix hat vier verknüpfte Teile. Erstens, Durchbruchsziele, drei bis "
                  "fünf Jahre voraus. Zweitens, Jahresziele, der Fortschritt, den Sie dieses Jahr brauchen. "
                  "Drittens, Verbesserungsprojekte, die Arbeit, die Leistung verändert. Viertens, KPI und "
                  "Zielwerte, der Beweis, dass es wirkt. Verantwortliche stehen daneben, in einem "
                  "Verantwortungsraster. Layouts variieren je Vorlage, also ergänzen Sie immer eine "
                  "Legende. Arjuns Kette reicht von Weltklasse-Qualität bis zu einem Ausbeute-Zielwert. "
                  "Beginnen wir oben.",
    },
    {
        "key": "p04", "num": 4, "title": "Durchbruchsziele",
        "points": [("Wenige große Ergebnisse: 3 bis 5", "Wählen Sie drei bis fünf"),
                   ("Ergebnis, Horizont, heutiger Ausgangswert", "Nennen Sie das Ergebnis"),
                   ("Auf Ziele achten, die sich widersprechen", "Und prüfen Sie auf Ziele")],
        "example": "Arjuns Ergebnis: Kundenrücksendungen um zwei Drittel senken, bei wachsender Leistung.",
        "example_cue": "Arjun schrieb ein klares Ergebnis",
        "script": "Durchbruchsziele nennen wenige große Ergebnisse, jenseits der normalen täglichen "
                  "Verbesserung. Wählen Sie drei bis fünf, keine Wunschliste. Nennen Sie das Ergebnis, den "
                  "Zeithorizont und den heutigen Ausgangswert. Und prüfen Sie auf Ziele, die sich "
                  "widersprechen, wie Tempo gegen Sicherheit. Arjun schrieb ein klares Ergebnis. "
                  "Kundenrücksendungen um zwei Drittel senken, bei wachsender Leistung. Es ist ein "
                  "Ergebnis, keine Tätigkeit. Sie können es messen. Wie teilen Sie das auf dieses Jahr "
                  "herunter?",
    },
    {
        "key": "p05", "num": 5, "title": "Jahresziele",
        "points": [("Messbare Ergebnisse für dieses Jahr", "Jahresziele verwandeln"),
                   ("Ausgangswert, Zielwert, Zeitraum, Datenquelle", "Legen Sie den Ausgangswert fest"),
                   ("Catchball: Machbarkeit gemeinsam prüfen", "Dann nutzen Sie Catchball")],
        "example": "Jahr eins: ein Teil des Rückgangs, vereinbart nach Analyse der Feldausfälle.",
        "example_cue": "Für Jahr eins",
        "script": "Jahresziele verwandeln die Richtung in Ergebnisse, die Sie dieses Jahr messen können. "
                  "Verteilen Sie nicht einfach runde Prozente. Legen Sie den Ausgangswert fest, den "
                  "Zielwert, den Zeitraum und die Datenquelle. Halten Sie die Liste kurz. Dann nutzen Sie "
                  "Catchball. Das ist das Hin und Her, in dem Teams prüfen, ob ein Zielwert wirklich "
                  "machbar ist. Für Jahr eins zielt Arjun auf einen Teil des Rückgangs, nicht auf alles. "
                  "Seine Teams vereinbarten es nach Analyse der Feldausfälle. Welche Projekte bringen Sie "
                  "dorthin?",
    },
    {
        "key": "p06", "num": 6, "title": "Verbesserungsprojekte",
        "points": [("Problem, Umfang, Verantwortlicher, Meilensteine, Prüfung", "Ein gutes hat"),
                   ("Mehr Prüfung = selten ein Durchbruch", "Mehr Prüfung bringt"),
                   ("Nach Belegen wählen: Wirkung gegen Aufwand", "Wählen Sie Projekte nach Belegen")],
        "example": "Eine Verriegelung Barcode gegen BOM blockiert falsche Bauteile; Erfolg erst, wenn Tests "
                   "und Fehlerdaten übereinstimmen.",
        "example_cue": "An Arjuns Handylinie",
        "script": "Projekte sind die Änderungen, die Ihre Jahresziele bewegen. Ein gutes hat eine "
                  "Problembeschreibung, einen Umfang, einen Verantwortlichen, Meilensteine und einen Weg, "
                  "Ergebnisse zu prüfen. Ein häufiger Fehler. Mehr Prüfung bringt selten einen Durchbruch. "
                  "Wählen Sie Projekte nach Belegen, und wägen Sie Wirkung gegen Aufwand, Kosten und "
                  "Risiko. An Arjuns Handylinie blockiert eine Verriegelung von Barcode gegen BOM falsche "
                  "Bauteile. Aber er meldet Erfolg erst, wenn Tests und Fehlerdaten übereinstimmen. Woran "
                  "erkennen Sie, dass es wirkt?",
    },
    {
        "key": "p07", "num": 7, "title": "KPI: Früh- und Spätindikatoren",
        "points": [("Spätindikatoren: erreichte Ergebnisse", "Spätindikatoren messen"),
                   ("Frühindikatoren: Bedingungen, die sie vorhersagen", "Frühindikatoren messen"),
                   ("Nenner und Datenquelle festlegen", "Legen Sie für jeden den Nenner"),
                   ("Keine umdefinierten Zahlen belohnen", "Und belohnen Sie nie")],
        "example": "An Arjuns Linie bestehen 98 % der Einheiten beim ersten Mal.",
        "example_cue": "An Arjuns Linie",
        "script": "Das ist die Aufgabe der KPI. Spätindikatoren messen Ergebnisse, die Sie schon haben, wie "
                  "Erstdurchlaufquote, Rücksendungen und Liefertreue. Frühindikatoren messen die "
                  "Bedingungen, die sie vorhersagen, wie Audits, Rüstprüfungen und Schulung. Sie brauchen "
                  "beide. Legen Sie für jeden den Nenner und die Datenquelle fest. Und belohnen Sie nie "
                  "eine Zahl, die nur besser wurde, weil jemand ihre Definition änderte. An Arjuns Linie "
                  "bestehen achtundneunzig Prozent der Einheiten beim ersten Mal. Aber wie stark treibt "
                  "jedes Projekt jede Zahl?",
    },
    {
        "key": "p08", "num": 8, "title": "Stärke der Verknüpfung",
        "points": [("Symbole zeigen die Stärke", "Die Matrix nutzt Symbole"),
                   ("Zuerst die Legende vereinbaren", "vereinbaren Sie zuerst Ihre Legende"),
                   ("Die Verknüpfung bewerten, nicht die Wichtigkeit", "Bewerten Sie die Verknüpfung"),
                   ("Nach Lücken und Übertreibungen suchen", "Dann suchen Sie nach Lücken")],
        "example": "Arjuns Vorrichtungsverriegelung senkt falsche Teile stark und berührt den "
                   "Energieverbrauch kaum.",
        "example_cue": "Arjuns Vorrichtungsverriegelung",
        "script": "Die Matrix nutzt Symbole, um zu zeigen, wie stark zwei Punkte verknüpft sind. Oft heißt "
                  "ein gefüllter Kreis stark, ein offener Kreis mittel. Keine Regel ist universell, also "
                  "vereinbaren Sie zuerst Ihre Legende. Bewerten Sie die Verknüpfung, nicht wie wichtig der "
                  "Punkt wirkt. Dann suchen Sie nach Lücken. Gibt es ein Jahresziel ohne Projekt dahinter? "
                  "Gibt es ein Projekt, das angeblich bei allem hilft? Arjuns Vorrichtungsverriegelung "
                  "senkt falsche Teile stark. Den Energieverbrauch berührt sie kaum. Wer sorgt dafür, dass "
                  "es passiert?",
    },
    {
        "key": "p09", "num": 9, "title": "Verantwortung und Catchball",
        "points": [("Je ein verantwortlicher Eigentümer", "Geben Sie jedem Ziel"),
                   ("Unterstützende Teams benennen", "Benennen Sie die unterstützenden Teams"),
                   ("RACI: durchführend, verantwortlich, befragt, informiert", "Wer führt durch"),
                   ("Der Eigentümer braucht Budget und Befugnis", "Sorgen Sie dafür, dass Ihr Eigentümer")],
        "example": "Testautomatisierung der Set-Top-Box: Technik, Produktion, Qualität und IT helfen; ein "
                   "Projektleiter bleibt verantwortlich.",
        "example_cue": "Bei Arjuns Set-Top-Box-Testautomatisierung",
        "script": "Ziele scheitern, wenn die Verantwortung unklar ist. Geben Sie jedem Ziel und jedem "
                  "Projekt einen verantwortlichen Eigentümer. Benennen Sie die unterstützenden Teams auch. "
                  "Das ist die Idee hinter RACI. Wer führt durch, wer ist verantwortlich, wer wird befragt, "
                  "und wer wird informiert? Sorgen Sie dafür, dass Ihr Eigentümer Budget und Befugnis hat, "
                  "Hindernisse zu beseitigen. Bei Arjuns Set-Top-Box-Testautomatisierung helfen Technik, "
                  "Produktion, Qualität und IT. Aber ein Projektleiter bleibt verantwortlich. Stockt es, "
                  "wissen Sie, wen Sie fragen.",
    },
    {
        "key": "p10", "num": 10, "title": "Der Aufbau-Workshop",
        "points": [("Zuerst Belege sammeln", "Vor dem Workshop"),
                   ("Umfang, Ausgangswert, Ziele, Ergebnisse", "Vereinbaren Sie Umfang"),
                   ("Wirksame Projekte, jedes mit einem KPI", "Wählen Sie wirksame Projekte"),
                   ("Verknüpfungen bewerten, Eigentümer benennen, Prüfungen planen", "Zum Schluss bewerten Sie")],
        "example": "In Arjuns Workshop verknüpften drei Abteilungen Projekte mit einem Lieferziel.",
        "example_cue": "In Arjuns Workshop",
        "script": "Bauen Sie die Matrix von der Strategie bis zur echten Arbeit. Vor dem Workshop sammeln "
                  "Sie Belege zu Kunden, Leistung, Kapazität und Kosten. Dann Schritt für Schritt. "
                  "Vereinbaren Sie Umfang und Ausgangswert. Wählen Sie wenige Durchbruchsziele. Legen Sie "
                  "die Ergebnisse dieses Jahres fest. Wählen Sie wirksame Projekte, und geben Sie jedem "
                  "einen KPI. Zum Schluss bewerten Sie die Verknüpfungen, benennen Eigentümer und planen "
                  "den Prüfrhythmus. In Arjuns Workshop verknüpften drei Abteilungen Projekte mit einem "
                  "Lieferziel. Wie sieht die fertige Matrix aus?",
    },
    {
        "key": "p11", "num": 11, "title": "Durchgerechnetes Beispiel",
        "points": [("Liefertreue 90 % → 98 %", "steigt die Liefertreue"),
                   ("Erstdurchlaufquote → 99 %", "Die Erstdurchlaufquote steigt"),
                   ("Umrüstung 50 → 20 Minuten", "Die Umrüstung sinkt"),
                   ("Planung, Qualität, Technik verantworten je eines", "Die Planung verantwortet die Lieferung")],
        "example": "Projekte: ein Bereitschafts-Dashboard, eine Barcode-Verriegelung und ein SMED-Pilot.",
        "example_cue": "Die Projekte sind",
        "script": "Hier Arjuns fertige Matrix, mit Übungszahlen. Seine Durchbrüche sind verlässliche "
                  "Lieferung, Fehlervermeidung und flexible Kapazität. Dieses Jahr steigt die Liefertreue "
                  "von neunzig auf achtundneunzig Prozent. Die Erstdurchlaufquote steigt auf "
                  "neunundneunzig. Die Umrüstung sinkt von fünfzig auf zwanzig Minuten. Die Projekte sind "
                  "ein Bereitschafts-Dashboard, eine Barcode-Verriegelung und ein SMED-Pilot. Die Planung "
                  "verantwortet die Lieferung, die Qualität die Ausbeute, die Technik die Umrüstung. Sehen "
                  "Sie jede Sichtlinie?",
    },
    {
        "key": "p12", "num": 12, "title": "Prüfrhythmus: PDCA",
        "points": [("Ein lebendes Werkzeug: Plan, Do, Check, Act", "Plan, Do, Check"),
                   ("Täglich / wöchentlich: Ausnahmen, Meilensteine", "Täglich und wöchentlich"),
                   ("Monatlich: KPI-Trends und Risiken", "Monatlich prüfen Sie"),
                   ("Quartalsweise: stützt es noch die Strategie?", "Quartalsweise fragen Sie")],
        "example": "Die Ausbeute stockte trotz Schulung, also prüfte Arjun, ob sich die Prozesskontrolle "
                   "wirklich änderte.",
        "example_cue": "Die Ausbeute stockte",
        "script": "Die X-Matrix ist ein lebendes Werkzeug, kein Plakat. Prüfen Sie sie mit Plan, Do, Check, "
                  "Act. Vergleichen Sie Ergebnisse mit Zielwerten, finden Sie die Ursachen von Lücken, und "
                  "passen Sie an. Täglich und wöchentlich verfolgen Sie Ausnahmen und Meilensteine. "
                  "Monatlich prüfen Sie KPI-Trends und Risiken. Quartalsweise fragen Sie, ob jedes Projekt "
                  "noch die Strategie stützt. Das lernte Arjun. Die Ausbeute stockte, obwohl die Schulung "
                  "fertig war. Also prüfte er, ob sich die Prozesskontrolle wirklich geändert hatte. Welche "
                  "Fallen sollten Sie meiden?",
    },
    {
        "key": "p13", "num": 13, "title": "Was tun, was lassen",
        "points": [("Wenige messbare Ergebnisse, klare Eigentümer", "Halten Sie also wenige"),
                   ("Ursachenketten und Mittel prüfen", "Prüfen Sie die Ursachenketten"),
                   ("Nicht alles „stark verknüpft\"", "markieren Sie nicht jedes Projekt"),
                   ("Fertiges Projekt ≠ gelieferter Nutzen", "Verwechseln Sie kein fertiges Projekt")],
        "example": "Ein Projekt wurde als fertig markiert, doch die Beschwerden blieben gleich.",
        "example_cue": "Eines von Arjuns Projekten",
        "script": "Eine Matrix wird schnell zu totem Papier. Zu viele Ziele, vage Worte und ungeprüfte "
                  "Verknüpfungen sorgen dafür. Halten Sie also wenige messbare Ergebnisse mit klaren "
                  "Eigentümern. Prüfen Sie die Ursachenketten und die Mittel dahinter. Aber markieren Sie "
                  "nicht jedes Projekt als stark mit jedem KPI verknüpft. Verwechseln Sie kein fertiges "
                  "Projekt mit gelieferten Nutzen. Und schreiben Sie nie still einen Ausgangswert um. Eines "
                  "von Arjuns Projekten war als fertig markiert, doch die Beschwerden blieben gleich. Wie "
                  "beweisen Sie echten Wert?",
    },
    {
        "key": "p14", "num": 14, "title": "Kosten-Nutzen-Rechnung",
        "points": [("Liefertreue = pünktlich ÷ gesamt fällig", "Die Liefertreue ist"),
                   ("Relativer Rückgang = Rückgang ÷ alte Rate", "Ein relativer Rückgang ist"),
                   ("Amortisation = Investition ÷ monatliche Einsparung", "Die Amortisation ist")],
        "example": "Fehler 2 % → 1,2 % klingt klein, ist aber ein relativer Rückgang um 40 %. Die "
                   "Verriegelung amortisiert sich in 6 Monaten.",
        "example_cue": "Fehler, die von zwei",
        "script": "Nutzen braucht einheitliche Formeln, sonst traut ihm niemand. Die Liefertreue ist "
                  "pünktliche Lieferungen geteilt durch alle fälligen. Ein relativer Rückgang ist der "
                  "Rückgang geteilt durch die alte Rate. Die Amortisation ist die Investition geteilt durch "
                  "die bestätigte monatliche Einsparung. Eine Falle, die Ihnen begegnen wird. Fehler, die "
                  "von zwei auf eins Komma zwei Prozent sinken, klingen nach wenig. Es ist ein relativer "
                  "Rückgang um vierzig Prozent. Und Arjuns Verriegelung amortisiert sich in sechs Monaten. "
                  "Wie beginnen Sie morgen?",
    },
    {
        "key": "p15", "num": 15, "title": "Fahrplan für 90 Tage",
        "points": [("Tag 1–30: Ausgangswerte, Matrix-Entwurf", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: Catchball, Projekte, Eigentümer", "In den nächsten dreißig"),
                   ("Tag 61–90: Verknüpfungen prüfen, bewerten, auditieren", "In den letzten dreißig")],
        "example": "Welches Ergebnis? Welcher Zielwert? Welches Projekt? Welcher KPI? Wem gehört das "
                   "Ergebnis?",
        "example_cue": "Welches Ergebnis zählt",
        "script": "Beginnen Sie mit einem Piloten, und bauen Sie die Prüfgewohnheit auf, bevor Sie überall "
                  "ausrollen. In den ersten dreißig Tagen sammeln Sie Ausgangswerte und entwerfen die "
                  "Matrix. In den nächsten dreißig führen Sie Catchball, geben Projekte frei und benennen "
                  "Eigentümer. In den letzten dreißig prüfen Sie die Verknüpfungen, bewerten die Lücken und "
                  "auditieren das Ergebnis. Dann stellen Sie Ihre fünf Fragen. Welches Ergebnis zählt? "
                  "Welcher Zielwert stützt es? Welches Projekt ändert den Prozess? Welcher KPI beweist es? "
                  "Und wem gehört das Ergebnis?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Langfristige Ziele", "icon": "chartUp", "with": 1},
        {"label": "Ziele dieses Jahres", "icon": "calendar", "with": 1},
        {"label": "Verbesserungsprojekte", "icon": "wrench", "with": 1},
        {"label": "Zielwerte und Eigentümer", "icon": "person", "tone": "good", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Richtungsmanagement", "icon": "sequence", "with": 0},
        {"label": "Strategie trifft tägliche Arbeit", "icon": "calendar", "with": 1}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Dutzende lokale Kaizen-Projekte", "sub": "Wenige halfen der Lieferung", "icon": "stack", "with": "example"},
            {"label": "Wenige ausgestattete Prioritäten", "sub": "In beide Richtungen, nicht von oben", "icon": "key", "with": 2}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Durchbruch", "sub": "3–5 Jahre", "icon": "chartUp", "with": 0},
        {"label": "Jährlich", "sub": "Dieses Jahr", "icon": "calendar", "with": 1},
        {"label": "Projekte", "sub": "Die Arbeit", "icon": "wrench", "with": 2},
        {"label": "KPI und Zielwerte", "sub": "Der Beweis", "icon": "check", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "3 bis 5 große Ergebnisse", "icon": "key", "with": 0},
        {"label": "Ergebnis, Horizont, Ausgangswert", "icon": "clipboard", "with": 1},
        {"label": "Ziele im Widerspruch", "sub": "Tempo gegen Sicherheit", "icon": "scale", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 2, "suffix": "/3", "icon": "chartDown", "label": "weniger Kundenrücksendungen",
                 "unit": "Bei wachsender Leistung: ein Ergebnis, keine Tätigkeit", "with": "example"}},
    "p05": {"type": "doc", "items": [
        {"label": "Jahresziel · Jahr 1", "icon": "label", "with": 0},
        {"label": "Ausgangswert · Zielwert · Zeitraum", "icon": "clipboard", "with": 1},
        {"label": "Datenquelle benannt", "icon": "search", "with": 1},
        {"label": "Catchball: ist es machbar?", "icon": "sequence", "with": 2},
        {"label": "Aus Feldausfällen vereinbart", "icon": "check", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Problem, Umfang, Eigentümer", "icon": "clipboard", "with": 0},
        {"label": "Mehr Prüfung", "sub": "Selten ein Durchbruch", "icon": "search", "tone": "bad", "with": 1},
        {"label": "Wirkung gegen Aufwand", "icon": "scale", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Teile-Barcode scannen", "icon": "barcode", "with": "example"},
            {"label": "Gegen die BOM prüfen", "icon": "clipboard", "with": "example"},
            {"label": "Falsches Teil? Blockiert", "icon": "lock", "tone": "good", "with": "example"}]}},
    "p07": {"type": "versus", "items": [
        {"label": "Spät", "sub": "Ausbeute, Rücksendungen, Lieferung", "icon": "chartUp", "with": 0},
        {"label": "Früh", "sub": "Audits, Rüsten, Schulung", "icon": "search", "with": 1}],
        "then": {"type": "stat", "value": 98, "suffix": "%", "icon": "check", "label": "beim ersten Mal bestanden",
                 "unit": "Erstdurchlaufquote an Arjuns Linie", "with": "example"}},
    "p08": {"type": "matrix", "prefix": "check", "cols": ["Falsche Teile", "Ausbeute", "Energie"],
            "note": "Die Verknüpfung bewerten, nicht die Wichtigkeit", "items": [
        {"label": "Verriegelung", "cells": [3, 3, None], "with": "example"},
        {"label": "SMED-Pilot", "cells": [None, None, 3], "with": "example"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Durchführend", "icon": "wrench", "with": 2},
        {"label": "Verantwortlich", "sub": "Ein Eigentümer", "icon": "person", "tone": "good", "with": 0},
        {"label": "Befragt", "icon": "search", "with": 2},
        {"label": "Informiert", "icon": "clipboard", "with": 2}]},
    "p10": {"type": "steps", "items": [
        {"label": "Belege", "with": 0}, {"label": "Umfang, Ausgangswert", "with": 1},
        {"label": "Ziele", "with": 1}, {"label": "Projekte + KPI", "with": 2},
        {"label": "Verknüpfungen, Eigentümer", "with": 3}, {"label": "Prüfrhythmus", "with": 3}]},
    "p11": {"type": "compare", "before": {"label": "Heute", "value": 90}, "after": {"label": "Dieses Jahr", "value": 98},
            "suffix": "%", "unit": "Liefertreue", "note": "Die Planung verantwortet sie", "with": 0,
            "then": {"type": "icons", "with": "example", "items": [
                {"label": "Bereitschafts-Dashboard", "sub": "Lieferung", "icon": "chartUp", "with": "example"},
                {"label": "Barcode-Verriegelung", "sub": "Ausbeute auf 99 %", "icon": "barcode", "with": "example"},
                {"label": "SMED-Pilot", "sub": "Umrüstung 50 → 20 Min.", "icon": "clock", "with": "example"}]}},
    "p12": {"type": "timeline", "items": [
        {"label": "Ausnahmen, Meilensteine", "sub": "Täglich / wöchentlich", "icon": "calendar", "with": 1},
        {"label": "KPI-Trends, Risiken", "sub": "Monatlich", "icon": "chartUp", "with": 2},
        {"label": "Noch auf Strategie?", "sub": "Quartalsweise", "icon": "search", "with": 3}]},
    "p13": {"type": "icons", "items": [
        {"label": "Wenige Ergebnisse, klare Eigentümer", "icon": "person", "tone": "good", "with": 0},
        {"label": "Verknüpfungen + Mittel prüfen", "icon": "check", "tone": "good", "with": 1},
        {"label": "Alles „stark\"", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Fertig ≠ geliefert", "icon": "warning", "tone": "bad", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Vorher", "value": 2}, "after": {"label": "Nachher", "value": 1.2},
            "decimals": 1, "suffix": "%", "unit": "Fehlerrate", "note": "Relativer Rückgang 40 % · Amortisation in 6 Monaten", "with": "example"},
    "p15": {"type": "timeline", "items": [
        {"label": "Ausgangswerte, Matrix-Entwurf", "sub": "Tag 1–30", "icon": "clipboard", "with": 0},
        {"label": "Catchball, Projekte, Eigentümer", "sub": "31–60", "icon": "person", "with": 1},
        {"label": "Verknüpfungen prüfen, bewerten, auditieren", "sub": "61–90", "icon": "search", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Was davon gehört zu KPI / Zielwerten, nicht zu den Durchbruchszielen?",
        "options": ["Weltklasse in der Produktqualität werden", "Die Erstdurchlaufquote dieses Jahr auf 99 % heben", "Jeden Kunden begeistern"],
        "correct": 1,
        "explanation": "Ein Zielwert ist messbar, mit Zahl und Datum. Die anderen sind Richtungsziele, keine "
                       "Messgrößen.",
        "q_script": "Kurzer Check. Was davon gehört zu den KPI und Zielwerten, statt zu den "
                    "Durchbruchszielen? Nehmen Sie sich kurz Zeit.",
        "a_script": "Die Erstdurchlaufquote dieses Jahr auf neunundneunzig Prozent heben. Ein Zielwert hat "
                    "eine Zahl und ein Datum. Die anderen zwei sind Richtungen, keine Messgrößen.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Das jährliche Liefertreue-Ziel eines Werks hat kein verknüpftes Projekt. Was sollte das "
                    "Team ZUERST tun?",
        "options": ["Eine starke Verknüpfung zum nächstbesten Projekt eintragen", "Ein Projekt finden oder starten, das die Lieferung bewegt, oder das Ziel überdenken",
                    "Lassen: der KPI verbessert sich von selbst"],
        "correct": 1,
        "explanation": "Ein Ziel ohne stützendes Projekt ist eine Lücke. Schließen Sie sie mit echter Arbeit, "
                       "oder überarbeiten Sie das Ziel; füllen Sie das Feld nie mit einer Verknüpfung ohne "
                       "Mechanismus.",
        "q_script": "Noch eine, ein Szenario. Das jährliche Lieferziel eines Werks hat kein verknüpftes "
                    "Projekt. Was sollte das Team zuerst tun? Überlegen Sie kurz.",
        "a_script": "Finden oder starten Sie ein Projekt, das die Lieferung wirklich bewegt, oder überdenken "
                    "Sie das Ziel. Eine Verknüpfung ohne echten Mechanismus verbirgt nur die Lücke.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
