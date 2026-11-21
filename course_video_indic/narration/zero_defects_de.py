"""zero_defects in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh zero_defects_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "zd_de"
NAME = "zero_defects_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Zero Defects": "Siro Difekts",
    "Poka Yoke": "Poka Joke",
    "Crosby": "Krosbi",
    "Jidoka": "Dschidoka",
    "Andon": "Andon",
    "PFMEA": "pe eff emm e a",
    "DPMO": "de pe emm o",
    "Cpk": "ze pe ka",
    "PPM": "pe pe emm",
    "FPY": "eff pe üpsilon",
    "SOP": "ess o pe",
    "SKU": "ess ka u",
    "Cp": "ze pe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Ein Stecker, schlecht gesetzt. Er bestand jede Sichtprüfung. Dann kamen vierhundert "
    "Handys zur Nacharbeit zurück. Kommt Ihnen das bekannt vor? In dieser Lektion lernen Sie "
    "Zero Defects kennen. Sie sehen, wie Sie Qualität ehrlich messen, und Fehler wie diesen "
    "unmöglich machen. Wir begleiten Priya, Linieningenieurin an einer Montagelinie für "
    "Handys."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. Verhindern Sie Fehler, statt nur nach ihnen zu prüfen. "
    "Messen Sie ehrlich, mit klaren Definitionen. Und wenn etwas schiefgeht, beheben Sie das "
    "System, nicht die Person. Ihre Aufgabe für diese Woche. Wählen Sie einen Fehler, der an "
    "Ihrer Linie immer wiederkommt, und fragen Sie, wie Sie ihn unmöglich machen. Gut "
    "gemacht, Lektion und ganzer Kurs abgeschlossen, von A bis Z. Nun gehen Sie und machen "
    "eine Verbesserung an Ihrer Linie."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Bedeutung und Haltung",
        "points": [("Jeder Fehler ist vermeidbar", "sieht jeden Fehler als vermeidbar"),
                   ("Beim ersten Mal richtig", "Ihr Ziel ist"),
                   ("Den Prozess gestalten und steuern", "Indem Sie den Prozess"),
                   ("Eine Disziplin, kein Versprechen", "Es ist eine Disziplin")],
        "example": "Priyas Linie: eine Station bestätigt jetzt den Steckersitz vor dem elektrischen Test.",
        "example_cue": "An Priyas Linie",
        "script": "Hier ist die Kernidee. Zero Defects sieht jeden Fehler als vermeidbar, nicht als normale "
                  "Geschäftskosten. Ihr Ziel ist, jede Einheit beim ersten Mal richtig zu machen. Wie? "
                  "Indem Sie den Prozess gut gestalten und steuern. Es ist eine Disziplin, kein "
                  "Versprechen, dass nie etwas schiefgeht. An Priyas Linie bestätigt eine Station jetzt den "
                  "Steckersitz vor dem elektrischen Test. Woher kommt diese Idee?",
    },
    {
        "key": "p02", "num": 2, "title": "Geschichte und Geschäftswert",
        "points": [("Crosby, 1960er: Qualität = Anforderungen erfüllen", "Philip Crosby machte"),
                   ("Lean ergänzt eingebaute Qualität und Fehlervermeidung", "Modernes Lean ergänzt"),
                   ("Das System beheben, nicht die Person", "beheben Sie das System"),
                   ("Führung räumt Hindernisse weg; Werker stoppen und reagieren", "Die Führung räumt Hindernisse")],
        "example": "Für die Unterstützung der Führung müssen Sie das Geld zeigen.",
        "example_cue": "Aber für diese Unterstützung",
        "script": "Philip Crosby machte Zero Defects in den neunzehnhundertsechziger Jahren bekannt. Seine "
                  "Definition ist einfach. Qualität heißt, klar festgelegte Anforderungen zu erfüllen. "
                  "Modernes Lean ergänzt eingebaute Qualität, Standardarbeit und Fehlervermeidung. Der "
                  "entscheidende Wandel. Wenn ein Fehler passiert, beheben Sie das System, statt die Person "
                  "zu beschuldigen. Die Führung räumt Hindernisse weg, und Werkern wird vertraut, zu "
                  "stoppen und zu reagieren. Aber für diese Unterstützung müssen Sie das Geld zeigen.",
    },
    {
        "key": "p03", "num": 3, "title": "Kosten schlechter Qualität",
        "points": [("Interne Fehler: Ausschuss, Nacharbeit, Nachtest", "Interne Fehler umfassen"),
                   ("Externe Fehler: Garantie, Rücksendungen", "Externe Fehler umfassen"),
                   ("Versteckt: Verzug, Handling, verlorene Kapazität", "Dann kommen die versteckten Kosten"),
                   ("Vorbeugung kostet viel weniger", "Vorbeugung kostet viel weniger")],
        "example": "Priyas Linie: 400 nachgearbeitete Handys = ₹32.000 direkte Nacharbeit, noch vor jeder "
                   "späten Lieferung.",
        "example_cue": "Letzten Monat arbeitete Priyas Linie",
        "script": "Schlechte Qualität kostet mehr, als Sie denken. Interne Fehler umfassen Ausschuss, "
                  "Nacharbeit und Nachtest. Externe Fehler umfassen Garantiefälle und Rücksendungen. Dann "
                  "kommen die versteckten Kosten, wie Verzug, zusätzliches Handling und verlorene "
                  "Kapazität. Letzten Monat arbeitete Priyas Linie vierhundert Handys nach. Das sind "
                  "zweiunddreißigtausend Rupien direkte Nacharbeit, noch vor jeder späten Lieferung. "
                  "Vorbeugung kostet viel weniger. Wie messen Sie, wo Qualität verloren geht?",
    },
    {
        "key": "p04", "num": 4, "title": "FTR, FPY und RTY",
        "points": [("First Time Right: gar keine Korrektur", "First Time Right heißt"),
                   ("First Pass Yield: einen Schritt beim ersten Mal bestehen", "First Pass Yield ist"),
                   ("Rolled Throughput Yield: alle Schritte multiplizieren", "Rolled Throughput Yield multipliziert")],
        "example": "Drei Stufen mit je 98 % ergeben zusammen nur etwa 94 %.",
        "example_cue": "Drei Stufen mit je achtundneunzig",
        "script": "Beginnen Sie mit drei Ausbeutemaßen. First Time Right heißt, Anforderungen ganz ohne "
                  "Korrektur zu erfüllen. First Pass Yield ist der Anteil der Einheiten, die einen Schritt "
                  "beim ersten Mal bestehen. Rolled Throughput Yield multipliziert die Ausbeuten aller "
                  "Schritte. Die Falle. Drei Stufen mit je achtundneunzig Prozent klingen toll. Zusammen "
                  "ergeben sie nur etwa vierundneunzig Prozent. Welcher Schritt Ihrer Linie zieht die Summe "
                  "still nach unten?",
    },
    {
        "key": "p05", "num": 5, "title": "PPM, DPMO und Zielwerte",
        "points": [("PPM: fehlerhafte Einheiten pro Million", "PPM zählt"),
                   ("DPMO: Fehler pro Million Möglichkeiten", "DPMO zählt"),
                   ("Stichprobengröße und Umfang angeben", "Geben Sie immer Ihre Stichprobe"),
                   ("PPM nie mit DPMO vergleichen", "Und vergleichen Sie nie")],
        "example": "Priya fand 25 schlechte Handys unter 50.000 = 500 PPM.",
        "example_cue": "Priya fand fünfundzwanzig",
        "script": "Fehlerraten brauchen einen genauen Nenner. PPM zählt fehlerhafte Einheiten pro Million. "
                  "DPMO zählt Fehler pro Million Möglichkeiten. Sie müssen also zuerst die Möglichkeiten je "
                  "Einheit festlegen. Priya fand fünfundzwanzig schlechte Handys unter fünfzigtausend. Das "
                  "sind fünfhundert PPM. Geben Sie immer Ihre Stichprobe und den Umfang an. Und vergleichen "
                  "Sie nie PPM mit DPMO. Wie verhindern Sie, dass Fehler überhaupt entstehen?",
    },
    {
        "key": "p06", "num": 6, "title": "Qualität an der Quelle",
        "points": [("Jeder Arbeitsgang verantwortet sein Ergebnis", "jeder Arbeitsgang verantwortet"),
                   ("Nächste Station = Ihr Kunde", "Behandeln Sie die nächste Station"),
                   ("Eingänge und Einrichtung prüfen, der SOP folgen", "Prüfen Sie Ihre Eingänge"),
                   ("Falsch? Stoppen, aussortieren, eskalieren", "Wirkt etwas falsch")],
        "example": "Set-Top-Box-Linie: Werker prüfen Wärmeleitpad und Schraubendrehmoment, bevor eine "
                   "Einheit weitergeht.",
        "example_cue": "An der Set-Top-Box-Linie",
        "script": "Qualität an der Quelle heißt, jeder Arbeitsgang verantwortet sein eigenes Ergebnis. "
                  "Behandeln Sie die nächste Station als Ihren Kunden. Prüfen Sie Ihre Eingänge und die "
                  "Einrichtung zuerst, dann folgen Sie der aktuellen SOP. Wirkt etwas falsch, stoppen, "
                  "aussortieren und eskalieren Sie. Geben Sie es nicht weiter. An der Set-Top-Box-Linie "
                  "nebenan prüfen Werker Wärmeleitpad und Schraubendrehmoment, bevor eine Einheit "
                  "weitergeht. Spätere Prüfung rettet keinen instabilen Prozess. Und wenn Menschen trotzdem "
                  "Fehler machen?",
    },
    {
        "key": "p07", "num": 7, "title": "Poka Yoke",
        "points": [("Poka Yoke = Fehlervermeidung", "Es heißt Fehlervermeidung"),
                   ("Fehler unmöglich machen, oder sofort fangen", "Formen, Verriegelungen und Sensoren"),
                   ("Vorbeugung schlägt ein Warnschild", "Vorbeugung schlägt ein Warnschild"),
                   ("Mit guten und schlechten Mustern herausfordern", "Fordern Sie jede Vorrichtung")],
        "example": "Priyas Vorrichtung für den Akkustecker passt nur in einer Richtung; das Handy geht erst "
                   "weiter, wenn die Prüfung erfasst ist.",
        "example_cue": "Priya ergänzte eine Vorrichtung",
        "script": "Hier kommt Poka Yoke ins Spiel. Es heißt Fehlervermeidung. Formen, Verriegelungen und "
                  "Sensoren machen einen Fehler unmöglich, oder fangen ihn sofort. Vorbeugung schlägt ein "
                  "Warnschild, denn Warnungen bauen auf Gedächtnis. Priya ergänzte eine Vorrichtung für den "
                  "Akkustecker, die nur in einer Richtung passt. Das Handy geht erst weiter, wenn die "
                  "Prüfung erfasst ist. Fordern Sie jede Vorrichtung in jeder Schicht mit guten und "
                  "schlechten Mustern heraus. Was passiert, wenn trotzdem etwas schiefgeht?",
    },
    {
        "key": "p08", "num": 8, "title": "Jidoka, Andon und Reaktion",
        "points": [("Jidoka: der Prozess stoppt sich selbst", "Jidoka heißt"),
                   ("Andon macht das Problem sichtbar", "Ein Andon-Signal"),
                   ("Klare Stoppkriterien, ein benannter Verantwortlicher", "Sie brauchen klare Stoppkriterien"),
                   ("Neustart erst, wenn die Ursache beherrscht ist", "Sie starten erst neu")],
        "example": "Ein Audiotester meldet wiederholt Kanalungleichgewicht: die Linie stoppt, verdächtige "
                   "Einheiten werden gesperrt.",
        "example_cue": "Stellen Sie sich einen Audiotester vor",
        "script": "Jidoka heißt, der Prozess erkennt eine Abweichung und stoppt sich selbst. Ein "
                  "Andon-Signal macht das Problem sichtbar, damit die richtigen Leute schnell reagieren. "
                  "Sie brauchen klare Stoppkriterien, und einen benannten Verantwortlichen für jeden "
                  "Andon-Ruf. Stellen Sie sich einen Audiotester vor, der wiederholt Kanalungleichgewicht "
                  "meldet. Die Linie stoppt, und verdächtige Einheiten werden gesperrt. Die Vorrichtung "
                  "wird geprüft. Sie starten erst neu, wenn die Ursache beherrscht ist. Stoppen ist kein "
                  "Versagen. Das Problem zu verstecken schon.",
    },
    {
        "key": "p09", "num": 9, "title": "Standardarbeit und Audits",
        "points": [("Standardarbeit: die beste, sicherste Methode", "Mit Standardarbeit"),
                   ("Die erste Einheit nach dem Umrüsten bestätigen", "bestätigen Sie die erste Einheit"),
                   ("Gestufte Audits bestätigen Kontrollen", "Dann bestätigen gestufte Prozessaudits"),
                   ("Kontrollen auditieren, nicht Papier", "Auditieren Sie die Kontrollen")],
        "example": "Die Firmware-Freigabe braucht das freigegebene Image, einen Rezeptabgleich und eine "
                   "Prüfsumme.",
        "example_cue": "An einer Firmware-Station",
        "script": "Wie halten Sie gute Ergebnisse stabil? Mit Standardarbeit. Das ist die aktuell beste und "
                  "sicherste Methode, mit Prüfungen, Einstellungen und Rückverfolgbarkeit. Halten Sie sie "
                  "sichtbar, und bestätigen Sie die erste Einheit nach jedem Umrüsten. Dann bestätigen "
                  "gestufte Prozessaudits, dass Ihre kritischen Kontrollen noch wirken. Auditieren Sie die "
                  "Kontrollen, nicht das Papier. An einer Firmware-Station braucht die Freigabe das "
                  "freigegebene Image, einen Rezeptabgleich und eine Prüfsumme. Aber wie stabil ist der "
                  "Prozess selbst?",
    },
    {
        "key": "p10", "num": 10, "title": "SPC und Prozessfähigkeit",
        "points": [("SPC: normale Streuung gegen echte Signale", "Sie trennt normale Streuung"),
                   ("Cp: Streuung gegen Spezifikation", "Der Cp vergleicht"),
                   ("Cpk: prüft auch die Zentrierung", "Der Cpk prüft auch"),
                   ("Nur bei stabilem Prozess und kalibriertem Messmittel", "Beide bedeuten nur etwas")],
        "example": "Schraubendrehmoment an Priyas Linie: enge, zentrierte Streuung ergibt Cpk ≈ 1,33. Das "
                   "ist fähig.",
        "example_cue": "Nehmen Sie das Schraubendrehmoment",
        "script": "Die statistische Prozesslenkung beantwortet das. Sie trennt normale Streuung von echten "
                  "Signalen, die Handeln verlangen. Der Cp vergleicht die Streuung Ihres Prozesses mit der "
                  "Spezifikation. Der Cpk prüft auch, ob der Prozess zentriert ist. Beide bedeuten nur "
                  "etwas, wenn der Prozess stabil und das Messmittel kalibriert ist. Nehmen Sie das "
                  "Schraubendrehmoment an Priyas Linie. Bei enger, zentrierter Streuung liegt der Cpk bei "
                  "etwa eins Komma drei drei. Das ist fähig. Aber wie sehen Sie Risiken kommen?",
    },
    {
        "key": "p11", "num": 11, "title": "PFMEA und Kontrollpläne",
        "points": [("PFMEA: wie jeder Schritt versagen kann, und warum", "Sie fragt, wie jeder Schritt"),
                   ("Der Kontrollplan macht echte Prüfungen daraus", "Dann macht der Kontrollplan"),
                   ("Methode · Häufigkeit · Verantwortlicher · Reaktion", "Jede Prüfung hat eine Methode"),
                   ("Beide nach echten Ausfällen aktualisieren", "Aktualisieren Sie beide")],
        "example": "Fehlendes Isolierpad kann einen Kurzschluss auslösen → Anwesenheitsverriegelung + "
                   "Stopp-und-Sperr-Regel.",
        "example_cue": "Bei einem Audiogerät",
        "script": "Sie nutzen eine PFMEA. Sie fragt, wie jeder Schritt versagen kann, warum, und was das "
                  "verhindert oder erkennt. Dann macht der Kontrollplan echte Prüfungen daraus. Jede "
                  "Prüfung hat eine Methode, eine Häufigkeit, einen Verantwortlichen und eine Reaktion. Bei "
                  "einem Audiogerät kann ein fehlendes Isolierpad einen Kurzschluss auslösen. Die PFMEA "
                  "führt also zu einer Anwesenheitsverriegelung und einer klaren Stopp-und-Sperr-Regel. "
                  "Aktualisieren Sie beide, wann immer ein echter Ausfall Sie etwas lehrt.",
    },
    {
        "key": "p12", "num": 12, "title": "Root Cause Analysis",
        "points": [("Das Problem genau definieren", "beginnt damit, das Problem"),
                   ("Zuerst verdächtigen Bestand eingrenzen", "Grenzen Sie zuerst verdächtigen Bestand"),
                   ("Fakten, fünf Warum, kontrollierte Tests", "Dann nutzen Sie Fakten"),
                   ("Warum entstand es? Warum wurde es nicht gestoppt?", "Ihre Lösung muss")],
        "example": "Priyas Team führte die Ladefehler auf einen lockeren Steckersitz zurück.",
        "example_cue": "Priyas Team führte",
        "script": "Ausfälle lehren Sie etwas, wenn Sie richtig graben. Die Root Cause Analysis beginnt "
                  "damit, das Problem genau zu definieren. Grenzen Sie zuerst verdächtigen Bestand ein. "
                  "Dann nutzen Sie Fakten, fünf Warum und kontrollierte Tests, nie Annahmen. Ihre Lösung "
                  "muss zwei Fragen beantworten. Warum entstand der Fehler? Und warum stoppten ihn unsere "
                  "Kontrollen nicht? Priyas Team führte die Ladefehler auf einen lockeren Steckersitz "
                  "zurück. Sehen wir, was sie dann taten.",
    },
    {
        "key": "p13", "num": 13, "title": "Fallstudie: Handy",
        "points": [("1.200 von 40.000 fielen durch: 3 %", "Zwölfhundert von vierzigtausend"),
                   ("Daten nach Los, Vorrichtung, Station, Schicht aufgeteilt", "Das Team teilte die Daten"),
                   ("Codierte Vorrichtung + automatische Sitzprüfung", "Also testeten sie"),
                   ("FMEA und SOP aktualisiert", "Sie aktualisierten die")],
        "example": "Die Ausfälle sanken auf 0,5 %, 83 % weniger.",
        "example_cue": "Die Ausfälle sanken",
        "script": "Hier Priyas Fall. Zwölfhundert von vierzigtausend Handys fielen im ersten Ladetest "
                  "durch. Das ist eine Ausfallrate von drei Prozent. Das Team teilte die Daten nach "
                  "Steckerlos, Vorrichtung, Station und Schicht auf. Das Muster zeigte auf die Vorrichtung. "
                  "Also testeten sie eine codierte Vorrichtung mit automatischer Sitzprüfung. Die Ausfälle "
                  "sanken auf ein halbes Prozent. Das sind dreiundachtzig Prozent weniger. Und was machte "
                  "es dauerhaft? Sie aktualisierten die PFMEA und die SOP.",
    },
    {
        "key": "p14", "num": 14, "title": "Set-Top-Box und Audio",
        "points": [("Gleiches Denken, angepasste Kontrollen", "Sie passen nur die Kontrollen an"),
                   ("Set-Top-Box: Firmware passend zur SKU", "Gleichen Sie also die Firmware"),
                   ("Audio: codierte Stecker, Golden Units", "Codierte Stecker und Prüfungen"),
                   ("Verpackung: Seriennummer passend zum Karton", "In der Verpackung")],
        "example": "Set-Top-Box: Firmware, Stromversorgung, Etiketten. Audio: Polarität, Dichtung, "
                   "Kanalbalance.",
        "example_cue": "Fehler an Set-Top-Boxen",
        "script": "Dasselbe Denken wirkt bei jeder Produktfamilie. Sie passen nur die Kontrollen an. Fehler "
                  "an Set-Top-Boxen betreffen oft Firmware, Stromversorgung und Etiketten. Gleichen Sie "
                  "also die Firmware mit der SKU ab, und blockieren Sie falsches Aufspielen. Audiogeräte "
                  "versagen bei Lautsprecherpolarität, Dichtung und Kanalbalance. Codierte Stecker und "
                  "Prüfungen mit Referenzgeräten decken das ab. In der Verpackung gleicht das System jede "
                  "Seriennummer mit ihrem Karton ab. Was würden Sie an Ihrer Linie zuerst schützen?",
    },
    {
        "key": "p15", "num": 15, "title": "KPI und Fahrplan für 90 Tage",
        "points": [("Spät: FPY, PPM, Kosten schlechter Qualität", "Beobachten Sie Ihre Spätindikatoren"),
                   ("Früh: Prüftests, Auditnoten", "Beobachten Sie auch Frühindikatoren"),
                   ("Tag 1–30: Ausgangswert und Eingrenzung", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: Grundursachen, Poka Yoke pilotieren", "In den nächsten dreißig"),
                   ("Tag 61–90: Gewinne bestätigen, überall einführen", "In den letzten dreißig")],
        "example": "Letzte 30 Tage: die Gewinne bestätigen und an jeder Linie einführen.",
        "example_cue": "In den letzten dreißig",
        "script": "Machen Sie es zum Schluss zum Teil der täglichen Führung. Beobachten Sie Ihre "
                  "Spätindikatoren, wie FPY, PPM und die Kosten schlechter Qualität. Beobachten Sie auch "
                  "Frühindikatoren, wie Prüftests der Verriegelungen und Auditnoten. Hier ein einfacher "
                  "Plan für neunzig Tage. In den ersten dreißig Tagen legen Sie den Ausgangswert fest und "
                  "grenzen ein. In den nächsten dreißig finden Sie Grundursachen und pilotieren Poka Yoke. "
                  "In den letzten dreißig bestätigen Sie die Gewinne und führen sie an jeder Linie ein.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Jeder Fehler vermeidbar", "icon": "shield", "with": 0},
        {"label": "Beim ersten Mal richtig", "icon": "check", "tone": "good", "with": 1},
        {"label": "Den Prozess gestalten", "icon": "gear", "with": 2},
        {"label": "Eine Disziplin", "icon": "clipboard", "with": 3}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Stecker gesetzt?", "icon": "sensor", "with": "example"},
            {"label": "Dann elektrischer Test", "icon": "test", "tone": "good", "with": "example"}]}},
    "p02": {"type": "timeline", "items": [
        {"label": "Qualität = Anforderungen erfüllen", "sub": "Crosby, 1960s", "icon": "clipboard", "with": 0},
        {"label": "Eingebaute Qualität, Fehlervermeidung", "sub": "Modernes Lean", "icon": "key", "with": 1},
        {"label": "Das System beheben, nicht die Person", "sub": "Heute", "icon": "gear", "with": 2}]},
    "p03": {"type": "icons", "items": [
        {"label": "Intern", "sub": "Ausschuss, Nacharbeit, Nachtest", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Extern", "sub": "Garantie, Rücksendungen", "icon": "box", "tone": "bad", "with": 1},
        {"label": "Versteckt", "sub": "Verzug, Handling, Kapazität", "icon": "clock", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 32000, "prefix": "₹", "icon": "wrench", "label": "direkte Nacharbeit",
                 "unit": "400 Handys in einem Monat nachgearbeitet", "with": "example"}},
    "p04": {"type": "icons", "items": [
        {"label": "First Time Right", "sub": "Gar keine Korrektur", "icon": "check", "with": 0},
        {"label": "First Pass Yield", "sub": "Einen Schritt beim ersten Mal bestehen", "icon": "test", "with": 1},
        {"label": "Rolled Throughput Yield", "sub": "Alle Schritte multiplizieren", "icon": "sequence", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "98% × 98% × 98% ≈ 94%", "suffix": "%", "with": "example", "items": [
            {"label": "Stufe 1", "value": 98, "with": "example"},
            {"label": "Stufe 2", "value": 98, "with": "example"},
            {"label": "Stufe 3", "value": 98, "with": "example"},
            {"label": "Zusammen", "value": 94, "tone": "bad", "with": "example"}]}},
    "p05": {"type": "versus", "items": [
        {"label": "PPM", "sub": "Fehlerhafte Einheiten pro Million", "icon": "count", "with": 0},
        {"label": "DPMO", "sub": "Fehler pro Million Möglichkeiten", "icon": "search", "with": 1}],
        "then": {"type": "stat", "value": 500, "suffix": " PPM", "icon": "count", "label": "25 schlechte Handys unter 50.000",
                 "unit": "Immer Stichprobengröße und Umfang angeben", "with": "example"}},
    "p06": {"type": "flow", "items": [
        {"label": "Ihr Ergebnis verantworten", "icon": "hand", "with": 0},
        {"label": "Nächste Station = Kunde", "icon": "person", "with": 1},
        {"label": "Eingänge, Einrichtung, SOP", "icon": "clipboard", "with": 2},
        {"label": "Stoppen, aussortieren, eskalieren", "icon": "warning", "tone": "bad", "with": 3}]},
    "p07": {"type": "ladder", "top": "AM STÄRKSTEN", "bottom": "AM SCHWÄCHSTEN", "items": [
        {"label": "Unmöglich machen", "icon": "key", "with": 1},
        {"label": "Sofort fangen", "icon": "sensor", "with": 1},
        {"label": "Warnschild", "icon": "warning", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Vorrichtung passt nur einseitig", "icon": "shape", "with": "example"},
            {"label": "Prüfung erfasst", "icon": "clipboard", "with": "example"},
            {"label": "Erst dann geht das Handy weiter", "icon": "check", "tone": "good", "with": "example"}]}},
    "p08": {"type": "flow", "items": [
        {"label": "Abweichung erkannt", "sub": "Jidoka", "icon": "sensor", "with": 0},
        {"label": "Andon: sichtbar machen", "icon": "warning", "with": 1},
        {"label": "Stoppen, Verdächtige sperren", "icon": "lock", "tone": "bad", "with": "example"},
        {"label": "Neustart, wenn beherrscht", "icon": "check", "tone": "good", "with": 3}]},
    "p09": {"type": "doc", "items": [
        {"label": "Standardarbeit · Firmware-Station", "icon": "label", "with": 0},
        {"label": "Erste Einheit nach dem Umrüsten bestätigt", "icon": "check", "with": 1},
        {"label": "Freigegebenes Image + Rezeptabgleich", "icon": "chip", "with": "example"},
        {"label": "Prüfsumme vor der Freigabe", "icon": "lock", "with": "example"},
        {"label": "Gestuftes Audit: Kontrollen, nicht Papier", "icon": "search", "with": 3}]},
    "p10": {"type": "icons", "items": [
        {"label": "Rauschen gegen echtes Signal", "icon": "wave", "with": 0},
        {"label": "Cp: Streuung gegen Spezifikation", "icon": "scale", "with": 1},
        {"label": "Cpk: auch zentriert", "icon": "pin", "with": 2},
        {"label": "Stabiler Prozess, kalibriertes Messmittel", "icon": "gear", "with": 3}],
        "then": {"type": "stat", "value": 1.33, "decimals": 2, "icon": "screw", "label": "Cpk beim Schraubendrehmoment",
                 "unit": "Enge, zentrierte Streuung: fähig", "with": "example"}},
    "p11": {"type": "flow", "items": [
        {"label": "PFMEA: wie es versagen kann", "icon": "search", "with": 0},
        {"label": "Kontrollplan: echte Prüfungen", "icon": "clipboard", "with": 1},
        {"label": "Methode · Häufigkeit · Verantwortlicher · Reaktion", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Fehlendes Isolierpad", "sub": "Kann einen Kurzschluss auslösen", "icon": "warning", "tone": "bad", "with": "example"},
            {"label": "Anwesenheitsverriegelung", "icon": "sensor", "with": "example"},
            {"label": "Stopp-und-Sperr-Regel", "icon": "lock", "tone": "good", "with": "example"}]}},
    "p12": {"type": "flow", "items": [
        {"label": "Genau definieren", "icon": "clipboard", "with": 0},
        {"label": "Verdächtigen Bestand eingrenzen", "icon": "lock", "with": 1},
        {"label": "Fakten, fünf Warum, Tests", "icon": "test", "with": 2},
        {"label": "Warum entstanden? Warum nicht gestoppt?", "icon": "search", "tone": "good", "with": 3}]},
    "p13": {"type": "stat", "value": 3, "suffix": "%", "icon": "power", "label": "fielen im ersten Ladetest durch",
            "unit": "1.200 von 40.000 Handys", "with": 0,
            "then": {"type": "compare", "before": {"label": "Vorher", "value": 3}, "after": {"label": "Nachher", "value": 0.5},
                     "decimals": 1, "suffix": "%", "unit": "Handys, die im ersten Ladetest durchfallen",
                     "note": "83 % weniger", "with": "example"}},
    "p14": {"type": "icons", "items": [
        {"label": "Set-Top-Box", "sub": "Firmware passend zur SKU", "icon": "chip", "with": 1},
        {"label": "Audio", "sub": "Codierte Stecker, Golden Units", "icon": "wave", "with": 2},
        {"label": "Verpackung", "sub": "Seriennummer passend zum Karton", "icon": "barcode", "with": 3}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Ausgangswert und Eingrenzung", "sub": "Tag 1–30", "icon": "lock", "with": 2},
        {"label": "Grundursachen, Poka Yoke pilotieren", "sub": "31–60", "icon": "search", "with": 3},
        {"label": "Gewinne bestätigen, überall einführen", "sub": "61–90", "icon": "chartUp", "with": 4}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "970 von 1.000 Einheiten bestehen den ersten Test ohne Nacharbeit. Wie hoch ist der First "
                    "Pass Yield?",
        "options": ["3%", "97%", "9,7 pro Einheit"],
        "correct": 1,
        "explanation": "FPY = beim ersten Mal angenommen ÷ gesamt = 970 ÷ 1.000 = 97 %. Er zählt nur Einheiten, "
                       "die beim ersten Mal bestanden, ohne Nacharbeit.",
        "q_script": "Kurzer Check. Neunhundertsiebzig von tausend Einheiten bestehen den ersten Test, ohne "
                    "Nacharbeit. Wie hoch ist der First Pass Yield? Nehmen Sie sich kurz Zeit.",
        "a_script": "Siebenundneunzig Prozent. Der First Pass Yield zählt nur die Einheiten, die beim ersten "
                    "Mal bestanden, geteilt durch die Gesamtzahl.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Eine Audiolinie findet in dieser Schicht an 30 Einheiten vertauschte "
                    "Lautsprecherpolarität. Was sollte das Team ZUERST tun?",
        "options": ["Den Werker nachschulen und weitermachen", "Stoppen, verdächtige Einheiten eingrenzen, dann die Grundursache finden",
                    "Ein Warnschild am Lautsprecher anbringen", "Die Endprüfung verstärken"],
        "correct": 1,
        "explanation": "Zuerst eingrenzen: stoppen und verdächtige Einheiten bis zum letzten guten Punkt "
                       "sperren. Dann die Grundursache finden und vorbeugen, z. B. mit einem codierten "
                       "Polaritätsstecker. Schuld, Schilder und mehr Prüfung stoppen keine Wiederholung.",
        "q_script": "Noch eine, ein Szenario. Eine Audiolinie findet in dieser Schicht an dreißig Einheiten "
                    "vertauschte Lautsprecherpolarität. Was sollte das Team zuerst tun? Überlegen Sie kurz.",
        "a_script": "Stoppen und grenzen Sie zuerst die verdächtigen Einheiten ein. Dann finden Sie die "
                    "Grundursache und beugen vor, zum Beispiel mit einem codierten Polaritätsstecker. Schuld, "
                    "Schilder und mehr Prüfung verhindern keine Wiederholung.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
