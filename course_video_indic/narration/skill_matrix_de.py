"""skill_matrix in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh skill_matrix_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "sk_de"
NAME = "skill_matrix_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Skill Training Matrix": "Skill Treening Matrix",
    "One Point Lesson": "Wann Peunt Lessen",
    "Dojo": "Dodscho",
    "TAKT": "Takt",
    "SOP": "ess o pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Montagmorgen. Bala meldet sich krank. Er ist der Einzige, der den Linsenfokus einrichten "
    "kann. Um zehn Uhr steht die ganze Kamerazelle. Kommt Ihnen das bekannt vor? In dieser "
    "Lektion lernen Sie die Skill Training Matrix kennen. Sie sehen, wer welche Arbeit "
    "wirklich kann, wo die Lücken sind, und wie Sie sie schließen. Wir begleiten Vikram, "
    "Zellenleiter, der eine für sein Team aufbaut."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Eine Qualifikationsmatrix zeigt nachgewiesenes Können, "
    "nicht Anwesenheit. Zählen Sie qualifizierte Vertretungen für jede kritische Arbeit, in "
    "jeder Schicht. Und halten Sie sie lebendig, mit Belegen hinter jeder Bewertung. Ihre "
    "Aufgabe für diese Woche. Listen Sie Ihre drei kritischsten Stationen, und zählen Sie die "
    "Qualifizierten für jede. Gut gemacht, Lektion abgeschlossen. Als Nächstes lernen Sie die "
    "TAKT Zeit kennen, den Takt Ihrer Linie."
)

# One story thread: Vikram's network-camera cell. Operators Asha, Bala, Chitra,
# Deepa; skills ESD, PCB assembly, lens focus, test, packing; L0-L4, L3 = qualified.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was eine Qualifikationsmatrix ist",
        "points": [("Wer welche Arbeit kann, und wie gut", "wer welche Arbeit"),
                   ("Die nachgewiesene Stufe jeder Person", "Sie zeigt die nachgewiesene Stufe"),
                   ("Die Lücken", "Und sie zeigt die Lücken"),
                   ("Keine Anwesenheitsliste", "Sie ist keine Anwesenheitsliste")],
        "example": "Vikrams Zelle: Platinenmontage, Linsenfokus, Test und Verpackung, mit freigegebenen "
                   "Vertretungen für jede.",
        "example_cue": "Vikrams Zelle hat",
        "script": "Hier ist die Kernidee. Eine Skill Training Matrix ist ein visueller Nachweis, wer welche "
                  "Arbeit kann, und wie gut. Sie zeigt die nachgewiesene Stufe jeder Person, für jeden "
                  "Arbeitsgang. Und sie zeigt die Lücken. Sie ist keine Anwesenheitsliste und keine "
                  "Kursliste. Vikrams Zelle hat Platinenmontage, Linsenfokus, Test und Verpackung. Seine "
                  "Übersicht zeigt die freigegebenen Vertretungen für jede. Warum zählt das so sehr an "
                  "Ihrer Linie?",
    },
    {
        "key": "p02", "num": 2, "title": "Warum sie zählt",
        "points": [("Personal planen, Abwesenheit abdecken, ausgleichen", "Schichtleiter nutzen sie"),
                   ("Kompetenz bei kritischen Schritten bestätigen", "Die Qualität nutzt sie"),
                   ("Ein klarer Entwicklungsweg", "Und die Leute sehen")],
        "example": "Geübt im Feeder-Einrichten ≠ befugt, ein Programm freizugeben. Zwei verschiedene "
                   "Fähigkeiten.",
        "example_cue": "Ein Techniker kann geübt",
        "script": "Weil sie Ihre Leute mit Ihren Ergebnissen verbindet. Schichtleiter nutzen sie, um "
                  "Personal zu planen, Abwesenheiten abzudecken und die Linie auszugleichen. Die Qualität "
                  "nutzt sie, um Kompetenz bei kritischen Schritten zu bestätigen. Und die Leute sehen "
                  "einen klaren Entwicklungsweg. Eine feine Sache. Ein Techniker kann geübt im "
                  "Feeder-Einrichten sein, aber nicht befugt, ein Programm freizugeben. Zwei verschiedene "
                  "Fähigkeiten. Welche drei Stationen träfe es am härtesten?",
    },
    {
        "key": "p03", "num": 3, "title": "Aufbau der Matrix",
        "points": [("Zeilen: Personen", "Personen stehen in den Zeilen"),
                   ("Spalten: Fähigkeiten", "Fähigkeiten stehen in den Spalten"),
                   ("Jede Zelle: Stufe + letzte Bewertung", "Jede Zelle zeigt"),
                   ("Jede Fähigkeit mit ihrer SOP verknüpft", "Jede Fähigkeit ist"),
                   ("Aufgaben nicht zu einer Fähigkeit bündeln", "Bündeln Sie nie verschiedene Aufgaben")],
        "example": "Die Produktion hält sie aktuell; Trainer bewerten; die Qualität bestätigt die kritischen "
                   "Fähigkeiten.",
        "example_cue": "Die Produktion hält die Matrix",
        "script": "Der Aufbau ist einfach. Personen stehen in den Zeilen. Fähigkeiten stehen in den "
                  "Spalten. Jede Zelle zeigt die Stufe der Person, und wann sie zuletzt bewertet wurde. "
                  "Jede Fähigkeit ist mit ihrer SOP verknüpft und zeigt, wie kritisch sie ist. Die "
                  "Produktion hält die Matrix aktuell. Trainer bewerten, und die Qualität bestätigt die "
                  "kritischen Fähigkeiten. Eine Regel. Bündeln Sie nie verschiedene Aufgaben zu einer "
                  "Fähigkeit, nur damit die Tabelle voll aussieht. Was bedeuten die Stufen?",
    },
    {
        "key": "p04", "num": 4, "title": "Kompetenzstufen L0–L4",
        "points": [("L0 nicht geschult", "Stufe null heißt"),
                   ("L1 kennt Sicherheit und Ablauf", "Stufe eins heißt"),
                   ("L2 arbeitet unter Aufsicht", "Stufe zwei heißt"),
                   ("L3 qualifiziert, allein zu arbeiten", "Stufe drei heißt"),
                   ("L4 schult andere, behebt Störungen", "Stufe vier heißt")],
        "example": "Eine Stufe ist keine Erlaubnis: Maschinen- und Sicherheitsbefugnis werden getrennt "
                   "erfasst.",
        "example_cue": "Aber eine Stufe ist keine Erlaubnis",
        "script": "Nutzen Sie eine Skala mit fünf Stufen. Stufe null heißt nicht geschult. Stufe eins "
                  "heißt, Sie kennen Sicherheit, Ablauf und Hauptrisiken. Stufe zwei heißt, Sie können es "
                  "unter Aufsicht. Stufe drei heißt, Sie sind qualifiziert, allein zu arbeiten, in "
                  "Zykluszeit und Qualitätsgrenzen. Stufe vier heißt, Sie können andere schulen und "
                  "Störungen beheben. Aber eine Stufe ist keine Erlaubnis. Maschinen- und "
                  "Sicherheitsbefugnis werden getrennt erfasst. Welche Fähigkeiten zuerst?",
    },
    {
        "key": "p05", "num": 5, "title": "Die kritischen Fähigkeiten finden",
        "points": [("Jeden Schritt und seine SOP erfassen", "Listen Sie jeden Schritt"),
                   ("Sicherheit, Qualität, Kundenwirkung markieren", "Dann markieren Sie die Fähigkeiten"),
                   ("Wirkung, Schwierigkeit, Vertretungen bewerten", "Bewerten Sie die Wirkung"),
                   ("Mindestzahl Qualifizierter pro Schicht", "legen Sie eine Mindestzahl")],
        "example": "Vikrams Zelle: Linsenfokus und Firmware-Aufspielen stehen ganz oben; Kartonhandling "
                   "weiter unten.",
        "example_cue": "In Vikrams Zelle",
        "script": "Beginnen Sie mit Ihrer Prozesskarte. Listen Sie jeden Schritt, und die SOP, die ihn "
                  "regelt. Dann markieren Sie die Fähigkeiten, bei denen ein Fehler Sicherheit, Qualität "
                  "oder Kunden trifft. Bewerten Sie die Wirkung, wie schwer die Fähigkeit zu lernen ist, "
                  "und wie viele Vertretungen Sie haben. In Vikrams Zelle stehen Linsenfokus und "
                  "Firmware-Aufspielen ganz oben. Ein Fehler dort erreicht den Kunden. Kartonhandling steht "
                  "tiefer. Für jede kritische Fähigkeit legen Sie eine Mindestzahl Qualifizierter pro "
                  "Schicht fest.",
    },
    {
        "key": "p06", "num": 6, "title": "Echtes Können bewerten",
        "points": [("Kurze Theorieprüfung", "Prüfen Sie kurz die Theorie"),
                   ("Echte Zyklen + eine Abweichung beobachten", "Beobachten Sie mehrere echte Zyklen"),
                   ("Datum, Prüfer, Ergebnis erfassen", "Erfassen Sie Datum")],
        "example": "Eine Testerin bestand die Theorie, übersah aber fehlgeschlagene Seriennummer-Scans. Sie "
                   "bleibt auf Stufe zwei.",
        "example_cue": "Eine von Vikrams Testerinnen",
        "script": "Wie wissen Sie, dass jemand wirklich auf Stufe drei ist? Sie testen, was die Person "
                  "wirklich kann. Prüfen Sie kurz die Theorie, dann beobachten Sie die praktische Arbeit. "
                  "Beobachten Sie mehrere echte Zyklen, und mindestens eine Abweichung. Erfassen Sie Datum, "
                  "Prüfer und Ergebnis. Eine von Vikrams Testerinnen bestand die Theorie leicht. Aber sie "
                  "übersah immer wieder fehlgeschlagene Scans. Also bleibt sie vorerst auf Stufe zwei. Wann "
                  "bewerten Sie neu?",
    },
    {
        "key": "p07", "num": 7, "title": "Schulungsbedarf und Lücken",
        "points": [("Neu bewerten nach Abwesenheit oder Änderungen", "Bewerten Sie neu nach"),
                   ("Bedarf = geforderte Stufe − nachgewiesene Stufe", "Ein Bedarf ist die Lücke"),
                   ("Qualifizierte gegen Positionen zählen", "Zählen Sie Ihre Qualifizierten"),
                   ("Einzelne Ausfallpunkte finden", "Suchen Sie gezielt nach einzelnen")],
        "example": "Vikrams Schicht braucht 4 qualifizierte Firmware-Werker und hat 2: eine Lücke von 2.",
        "example_cue": "Vikrams Schicht braucht",
        "script": "Bewerten Sie neu nach langer Abwesenheit, einer Prozessänderung oder wiederholten "
                  "Fehlern. Dann ermitteln Sie den Schulungsbedarf. Ein Bedarf ist die Lücke zwischen der "
                  "geforderten und der nachgewiesenen Stufe. Zählen Sie Ihre Qualifizierten gegen die "
                  "Positionen, die Sie besetzen müssen. Vikrams Schicht braucht vier qualifizierte "
                  "Firmware-Werker. Er hat zwei. Eine Lücke von zwei. Suchen Sie gezielt nach einzelnen "
                  "Ausfallpunkten, wie Bala beim Linsenfokus. Wie schließen Sie die Lücke?",
    },
    {
        "key": "p08", "num": 8, "title": "Schulungsmethoden",
        "points": [("Strukturierte Schulung am Arbeitsplatz", "strukturierter Schulung am Arbeitsplatz"),
                   ("Ein unabhängiger Prüfer prüft das Ergebnis", "Ein unabhängiger Prüfer"),
                   ("Dojo: sicheres Üben neben der Linie", "Ein Dojo ist"),
                   ("Die One Point Lesson für Kernpunkte", "Eine One Point Lesson festigt")],
        "example": "Vikrams Verpackungs-Dojo nutzt absichtlich falsche Etiketten und fehlendes Zubehör.",
        "example_cue": "Vikrams Verpackungs-Dojo",
        "script": "Schulen Sie Ihre Leute mit strukturierter Schulung am Arbeitsplatz. Der Trainer bereitet "
                  "vor, zeigt es im Standardtempo, dann übt der Lernende mit Rückmeldung. Ein unabhängiger "
                  "Prüfer prüft das Ergebnis. Ein Dojo ist ein Schulungsbereich neben der Linie, wo man "
                  "sicher üben kann. Vikrams Verpackungs-Dojo nutzt absichtlich falsche Etiketten und "
                  "fehlendes Zubehör. Eine One Point Lesson festigt einzelne Kernpunkte. Und lehren Sie die "
                  "Reaktion auf Probleme, nicht nur die normalen Schritte.",
    },
    {
        "key": "p09", "num": 9, "title": "Der Schulungsplan für 90 Tage",
        "points": [("Tag 1–30: erfassen, Stufen festlegen, bewerten", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: kritische Lücken schulen", "In den nächsten dreißig"),
                   ("Tag 61–90: Vertretungen zertifizieren, ausweiten", "In den letzten dreißig")],
        "example": "Vikrams erste Priorität: einen zweiten Experten für Linsenfokus qualifizieren.",
        "example_cue": "Vikrams erste Priorität",
        "script": "Jeder Schulungsplan braucht Verantwortliche, Termine und ein klares Ergebnis. Hier eine "
                  "Version für neunzig Tage. In den ersten dreißig Tagen erfassen Sie die Fähigkeiten, "
                  "legen die Stufen fest und bewerten den Stand. In den nächsten dreißig schulen Sie die "
                  "kritischen Lücken, und bestätigen den Aufstieg auf Stufe drei. In den letzten dreißig "
                  "zertifizieren Sie Vertretungen und weiten aus. Vikrams erste Priorität war klar. Einen "
                  "zweiten Experten für Linsenfokus qualifizieren. Was wäre Ihre?",
    },
    {
        "key": "p10", "num": 10, "title": "KPI der Matrix",
        "points": [("Qualifikationsabdeckung", "Die Qualifikationsabdeckung fragt"),
                   ("Kompetenzerreichung", "Die Kompetenzerreichung verfolgt"),
                   ("Quote der Mehrfachqualifizierung", "Die Quote der Mehrfachqualifizierung zählt"),
                   ("Abgelaufene Qualifikationen", "zählen Sie abgelaufene Qualifikationen")],
        "example": "18 von 24 kritischen Positionen besetzt = 75 %. Pro Schicht berechnen.",
        "example_cue": "Vikram hat achtzehn",
        "script": "Messen Sie Ihre echte Belastbarkeit, nicht Schulungsstunden. Die Qualifikationsabdeckung "
                  "fragt, wie viele Positionen eine qualifizierte Person haben. Die Kompetenzerreichung "
                  "verfolgt die bestätigten geplanten Aufstiege. Die Quote der Mehrfachqualifizierung zählt "
                  "Leute mit zwei oder mehr Arbeiten. Und zählen Sie abgelaufene Qualifikationen. Vikram "
                  "hat achtzehn von vierundzwanzig kritischen Positionen besetzt. Das sind fünfundsiebzig "
                  "Prozent. Rechnen Sie pro Schicht, denn eine Person kann nicht zwei Stationen zugleich "
                  "besetzen.",
    },
    {
        "key": "p11", "num": 11, "title": "Beispiel: Vikrams Zelle",
        "points": [("Asha: Platinenmontage L4", "Asha ist auf Stufe vier"),
                   ("Chitra jetzt neben Bala: Linsenfokus L3", "Chitra ist jetzt neben Bala"),
                   ("Chitra, Deepa: Test L3+", "Chitra und Deepa sind"),
                   ("Nächste Priorität: eine weitere Fokus-Vertretung", "Was ist also die nächste")],
        "example": "Fokus + Test gleichzeitig: Bala am Fokus, Deepa am Test. Chitra kann nicht beides.",
        "example_cue": "Wer deckt also Fokus",
        "script": "Hier Vikrams Matrix nach neunzig Tagen. Asha ist auf Stufe vier bei der Platinenmontage. "
                  "Chitra ist jetzt neben Bala auf Stufe drei beim Linsenfokus. Chitra und Deepa sind für "
                  "den Test qualifiziert. Wer deckt also Fokus und Test gleichzeitig? Bala am Fokus, und "
                  "Deepa am Test. Chitra kann nicht beides zugleich. Fehlt Bala, muss Chitra zum Fokus "
                  "wechseln. Was ist also die nächste Schulungspriorität? Eine weitere Vertretung für den "
                  "Linsenfokus.",
    },
    {
        "key": "p12", "num": 12, "title": "Verbindung zu Qualität und Sicherheit",
        "points": [("Stufe + Befugnis + SOP-Schulung", "wenn drei Dinge aktuell sind"),
                   ("Jede Fähigkeit an ihre SOP-Revision gebunden", "Binden Sie jede Fähigkeit"),
                   ("Prozessänderung → neu bewerten", "Wenn sich der Prozess ändert"),
                   ("Schulung ersetzt nie Prozessgestaltung", "Schulung ersetzt nie")],
        "example": "Vikrams Firmware-Techniker war L3 auf dem alten Rezept. Das neue änderte kritische "
                   "Schritte, also wurde er neu bewertet.",
        "example_cue": "Vikrams Firmware-Techniker",
        "script": "Eine Qualifikationsmatrix ist eine Qualitätssicherung. Jemand sollte nur allein an einem "
                  "kritischen Schritt arbeiten, wenn drei Dinge aktuell sind. Die Stufe, die Befugnis und "
                  "die SOP-Schulung. Binden Sie jede Fähigkeit an ihre SOP-Revision. Wenn sich der Prozess "
                  "ändert, bewerten Sie neu. Vikrams Firmware-Techniker war auf Stufe drei beim alten "
                  "Rezept. Das neue änderte kritische Schritte, also wurde er neu bewertet. Und Schulung "
                  "ersetzt nie gute Prozessgestaltung. Hilft Software?",
    },
    {
        "key": "p13", "num": 13, "title": "Digitale Matrix und visuelle Tafel",
        "points": [("Eindeutige Codes für Personen und Fähigkeiten", "Nutzen Sie eindeutige Codes"),
                   ("Prüfpfad jeder Änderung", "führen Sie einen Prüfpfad"),
                   ("Erinnerungen bei ablaufenden Qualifikationen", "Richten Sie Erinnerungen"),
                   ("Keine Selbstfreigabe kritischer Fähigkeiten", "Lassen Sie nie jemanden")],
        "example": "Vikrams Dashboard warnt ihn, wenn eine Befugnis bald abläuft.",
        "example_cue": "Vikrams Dashboard warnt",
        "script": "Ja, wenn die Daten verlässlich sind. Eine digitale Matrix verknüpft Bewertungen, "
                  "SOP-Revisionen und Schichtpläne. Nutzen Sie eindeutige Codes für Personen und "
                  "Fähigkeiten, und führen Sie einen Prüfpfad jeder Änderung. Richten Sie Erinnerungen für "
                  "ablaufende Qualifikationen ein. Lassen Sie nie jemanden seine eigene kritische Fähigkeit "
                  "freigeben. Vikrams Dashboard warnt ihn, wenn eine Befugnis bald abläuft. Und eine "
                  "Auditfrage. Können Sie die Belege hinter jeder Stufe drei zeigen?",
    },
    {
        "key": "p14", "num": 14, "title": "Steuerung und Überprüfung",
        "points": [("Täglich: qualifizierte Besetzung beim Anlauf", "Jeden Tag"),
                   ("Wöchentlich: Lücken, Mehrfachqualifizierung, Überfälliges", "Jede Woche"),
                   ("Monatlich: Abdeckung, Abgänge", "Jeden Monat"),
                   ("Quartalsweise: Einheitlichkeit der Prüfer", "Jedes Quartal")],
        "example": "Dienstalter und Anwesenheit sind keine Qualifikation.",
        "example_cue": "Dienstalter und Anwesenheit",
        "script": "Halten Sie die Matrix mit festem Rhythmus lebendig. Jeden Tag prüfen Sie, dass kritische "
                  "Stationen beim Anlauf qualifiziert besetzt sind. Jede Woche prüfen Sie Lücken, "
                  "Mehrfachqualifizierung und überfällige Bewertungen. Jeden Monat schauen Sie auf "
                  "Abdeckung und das Risiko von Abgängen. Jedes Quartal prüfen Sie, ob die Prüfer "
                  "einheitlich bewerten. Und ändern Sie Stufen, wenn sich das Können ändert, nicht nach "
                  "Kalender. Dienstalter und Anwesenheit sind keine Qualifikation. Bereit?",
    },
    {
        "key": "p15", "num": 15, "title": "Vorlagen und Audit",
        "points": [("Matrix: Fähigkeit, SOP-Rev., Stufe, Ablauf", "Die Matrix enthält"),
                   ("Bewertungsbogen: Theorie, Zyklen, Sicherheit", "Der Bewertungsbogen"),
                   ("Ein Schulungsplan für jede Lücke", "Jede Lücke bekommt"),
                   ("Zellen gegen echte Arbeit auditieren", "Dann auditieren Sie sie")],
        "example": "Ein anderer Schichtleiter sollte auf einen Blick sehen, wer heute qualifiziert ist.",
        "example_cue": "Ein anderer Schichtleiter sollte",
        "script": "Nutzen Sie eine gelenkte Vorlage für Ihre Matrix. Die Matrix enthält Person, Fähigkeit, "
                  "SOP-Revision, Stufe, Bewertungsdatum und Ablauf. Der Bewertungsbogen erfasst Theorie, "
                  "beobachtete Zyklen, Sicherheitsprüfungen und Ergebnis. Jede Lücke bekommt einen "
                  "Schulungsplan. Dann auditieren Sie sie. Wählen Sie ein paar Zellen, und prüfen Sie die "
                  "Belege gegen echte Arbeit. Ein anderer Schichtleiter sollte auf einen Blick sehen, wer "
                  "heute qualifiziert ist. Ein lebendes Steuersystem, keine Dekoration.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Wer welche Arbeit macht", "icon": "person"}, {"label": "Nachgewiesene Stufe", "icon": "check"},
        {"label": "Die Lücken", "icon": "warning", "tone": "bad"},
        {"label": "Keine Anwesenheit", "icon": "cross", "tone": "bad"}]},
    "p02": {"type": "icons", "items": [
        {"label": "Personal, Abwesenheit", "icon": "calendar"},
        {"label": "Kompetenz bei kritischen Schritten", "icon": "shield"},
        {"label": "Ein Entwicklungsweg", "icon": "chartUp", "tone": "good"}]},
    "p03": {"type": "matrix", "cols": ["Linse", "Schrauben", "Test", "Packen"], "note": "Darstellung: jede Zelle ist eine nachgewiesene Stufe", "items": [
        {"label": "Person A", "cells": [3, 4, 2, None], "with": 0},
        {"label": "Person B", "cells": [1, 3, 3, 2], "with": 1},
        {"label": "Person C", "cells": [None, 2, 4, 3], "with": 2}]},
    "p04": {"type": "steps", "items": [
        {"label": "Nicht geschult", "sub": "L0"}, {"label": "Versteht", "sub": "L1"},
        {"label": "Unter Aufsicht", "sub": "L2"}, {"label": "Arbeitet allein", "sub": "L3"},
        {"label": "Schult andere", "sub": "L4"}]},
    "p05": {"type": "flow", "items": [
        {"label": "Jeden Schritt + SOP erfassen", "icon": "clipboard"},
        {"label": "Sicherheit, Qualität, Kunde markieren", "icon": "warning"},
        {"label": "Wirkung, Schwierigkeit, Vertretungen", "icon": "scale"},
        {"label": "Mindestzahl pro Schicht", "icon": "person", "tone": "good"}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Linsenfokus", "sub": "Höchstes Risiko", "icon": "camera", "tone": "bad", "with": "example"},
            {"label": "Firmware aufspielen", "sub": "Höchstes Risiko", "icon": "chip", "tone": "bad", "with": "example"},
            {"label": "Kartonhandling", "sub": "Niedriger", "icon": "box", "with": "example"}]}},
    "p06": {"type": "icons", "items": [
        {"label": "Kurze Theorieprüfung", "icon": "clipboard", "with": 0},
        {"label": "Echte Zyklen + eine Abweichung", "icon": "search", "with": 1},
        {"label": "Datum, Prüfer, Ergebnis", "icon": "calendar", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Theorie: bestanden", "icon": "clipboard", "tone": "good", "with": "example"},
            {"label": "Echte Arbeit: fehlgeschlagene Scans übersehen", "icon": "search", "tone": "bad", "with": "example"},
            {"label": "Sie bleibt auf Stufe 2", "icon": "person", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Nach Änderungen neu bewerten", "icon": "sequence", "with": 0},
        {"label": "Bedarf = gefordert − nachgewiesen", "icon": "count", "with": 1}],
        "then": {"type": "bars", "label": "", "note": "Eine Lücke von 2", "unit": "qualifizierte Firmware-Werker pro Schicht", "with": "example", "items": [
            {"label": "Benötigt", "value": 4, "with": "example"},
            {"label": "Vorhanden", "value": 2, "tone": "bad", "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Schulung am Arbeitsplatz", "icon": "person"}, {"label": "Unabhängiger Prüfer", "icon": "shield"},
        {"label": "Dojo", "sub": "Sicheres Üben neben der Linie", "icon": "tray"}, {"label": "One Point Lesson", "icon": "clipboard"}]},
    "p09": {"type": "timeline", "items": [
        {"label": "Fähigkeiten erfassen, Stufen festlegen, bewerten", "sub": "Tag 1–30", "icon": "clipboard"},
        {"label": "Kritische Lücken schulen", "sub": "31–60", "icon": "person"},
        {"label": "Vertretungen zertifizieren, ausweiten", "sub": "61–90", "icon": "check"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Qualifikationsabdeckung", "icon": "count"}, {"label": "Kompetenzerreichung", "icon": "chartUp"},
        {"label": "Mehrfachqualifizierung", "icon": "sequence"}, {"label": "Abgelaufene Qualifikationen", "icon": "clock", "tone": "bad"}],
        "then": {"type": "stat", "value": 75, "suffix": "%", "icon": "person", "label": "der kritischen Positionen besetzt",
                 "unit": "18 von 24: pro Schicht berechnen", "with": "example"}},
    "p11": {"type": "matrix", "cols": ["Platine", "Fokus", "Test"], "note": "Nach 90 Tagen. Fokus + Test gleichzeitig: Bala und Deepa. Als Nächstes: eine weitere "
                                                                                                         "Fokus-Vertretung.", "items": [
        {"label": "Asha", "cells": [4, None, None], "with": 0},
        {"label": "Bala", "cells": [None, 3, None], "with": 1},
        {"label": "Chitra", "cells": [None, 3, 3], "with": 1},
        {"label": "Deepa", "cells": [None, None, 3], "with": 2}]},
    "p12": {"type": "icons", "items": [
        {"label": "Stufe", "icon": "person", "with": 0}, {"label": "Befugnis", "icon": "key", "with": 0},
        {"label": "SOP-Schulung", "icon": "clipboard", "with": 0},
        {"label": "Prozessänderung: neu bewerten", "icon": "sequence", "with": 2}]},
    "p13": {"type": "icons", "items": [
        {"label": "Eindeutige Codes", "icon": "barcode"}, {"label": "Prüfpfad", "icon": "sequence"},
        {"label": "Ablauf-Erinnerungen", "icon": "clock"}, {"label": "Keine Selbstfreigabe", "icon": "cross", "tone": "bad"}]},
    "p14": {"type": "timeline", "items": [
        {"label": "Qualifizierte Besetzung beim Anlauf", "sub": "Täglich", "icon": "person"},
        {"label": "Lücken, Mehrfachqualifizierung, Überfälliges", "sub": "Wöchentlich", "icon": "calendar"},
        {"label": "Abdeckung, Abgänge", "sub": "Monatlich", "icon": "chartUp"},
        {"label": "Einheitlichkeit der Prüfer", "sub": "Quartalsweise", "icon": "scale"}]},
    "p15": {"type": "doc", "items": [
        {"label": "Qualifikationsmatrix · Zelle 2 · Rev C", "icon": "label", "with": 0},
        {"label": "Fähigkeit · SOP-Rev. · Stufe · Ablauf", "icon": "clipboard", "with": 0},
        {"label": "Bewertung: Theorie, Zyklen, Sicherheit", "icon": "test", "with": 1},
        {"label": "Ein Schulungsplan für jede Lücke", "icon": "calendar", "with": 2},
        {"label": "Gegen echte Arbeit auditiert", "icon": "search", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Ein Werker hat den Kurs beendet, wurde aber noch nicht bewertet. Darf er als L3 zählen?",
        "options": ["Ja, der Kurs ist abgeschlossen", "Nein, L3 braucht nachgewiesene, bewertete Leistung",
                    "Ja, wenn er schon lange dort arbeitet"],
        "correct": 1,
        "explanation": "Anwesenheit und Dienstalter sind keine Kompetenz. Stufe 3 heißt selbstständige Leistung, "
                       "durch eine Bewertung mit Belegen nachgewiesen.",
        "q_script": "Kurzer Check. Ein Werker hat den Kurs beendet, wurde aber noch nicht bewertet. Darf er "
                    "als Stufe drei zählen? Nehmen Sie sich kurz Zeit.",
        "a_script": "Nein. Stufe drei braucht bewertete und nachgewiesene Leistung. Einen Kurs besuchen ist "
                    "nicht dasselbe wie qualifiziert sein.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Nur eine Person der Schicht ist für den Linsenfokus qualifiziert, und die Leistung hängt "
                    "davon ab. Was sollte der Zellenleiter ZUERST tun?",
        "options": ["Alle in allem schulen", "Eine Vertretung für den Linsenfokus als oberste Priorität qualifizieren",
                    "Den Experten bitten, nie Urlaub zu nehmen", "Zuerst Fähigkeiten mit geringem Risiko schulen, weil es schneller geht"],
        "correct": 1,
        "explanation": "Die Abhängigkeit von einer Person bei einer kritischen Fähigkeit ist das größte Risiko. "
                       "Qualifizieren Sie dort zuerst eine Vertretung, dann weiten Sie die "
                       "Mehrfachqualifizierung aus.",
        "q_script": "Noch eine, ein Szenario. Nur eine Person der Schicht ist für den Linsenfokus "
                    "qualifiziert, und die ganze Zelle hängt davon ab. Was sollte der Zellenleiter zuerst "
                    "tun? Überlegen Sie kurz.",
        "a_script": "Qualifizieren Sie zuerst eine Vertretung für den Linsenfokus. Ein einzelner Ausfallpunkt "
                    "bei einer kritischen Fähigkeit ist das größte Risiko. Dann weiten Sie die "
                    "Mehrfachqualifizierung aus.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
