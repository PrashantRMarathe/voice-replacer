"""takt_time in German, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft German neural female voice (de-DE-KatjaNeural).

  bash tools/build_hindi.sh takt_time_de --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "tt_de"
NAME = "takt_time_de"
LANG = "de"
VOICE = "de-DE-KatjaNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> German script for the voice. Longest first.
SPOKEN = {
    "Uniform Production": "Juniform Prodakschen",
    "Yamazumi": "Jamasumi",
    "Heijunka": "Hejdschunka",
    "Kanban": "Kanban",
    "SMED": "Smed",
    "TAKT": "Takt",
    "UPPH": "u pe pe ha",
    "UPH": "u pe ha",
    "WIP": "we i pe",
    "SOP": "ess o pe",
    "A": "a",
    "B": "be",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Jede Maschine an Rohans Kameralinie wirkte beschäftigt. Die vorderen Stationen rasten. "
    "Und trotzdem verpasste der Versand den Lkw. Wie kann eine beschäftigte Linie zu spät "
    "sein? In dieser Lektion lernen Sie die TAKT Zeit kennen, den Takt, den Ihr Kunde "
    "vorgibt. Sie sehen, wie Sie sie richtig berechnen und damit Ihre Linie abstimmen, "
    "besetzen und führen. Wir begleiten Rohan, Planungsingenieur in einem Kamerawerk."
)
OUTRO_SCRIPT = (
    "Also, drei Dinge zum Merken. TAKT ist die netto verfügbare Zeit, geteilt durch den "
    "Kundenbedarf. Es ist das nötige Tempo, nicht die Zeit, die eine Station wirklich "
    "braucht. Und planen Sie mit echten Verlusten, wie Stillstand und Ausbeute, nicht mit "
    "theoretischem Tempo. Ihre Aufgabe für diese Woche. Berechnen Sie den TAKT für eine Ihrer "
    "Linien, und vergleichen Sie ihn mit Ihrer langsamsten Station. Gut gemacht, Lektion "
    "abgeschlossen. Als Nächstes lernen Sie Uniform Production kennen."
)

# One story thread: Rohan's network-camera plant. 7,200 good cameras/day, 1,200 net
# minutes/day over three shifts -> TAKT 10 s; final test 18 s per unit is the constraint.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Was die TAKT Zeit ist",
        "points": [("Takt: Schlag oder Rhythmus", "TAKT kommt vom"),
                   ("Das Tempo, das den Kundenbedarf deckt", "Es ist das Tempo"),
                   ("TAKT = netto verfügbare Zeit ÷ Bedarf", "Teilen Sie Ihre netto")],
        "example": "420 Netto-Minuten ÷ 840 Kameras = eine Kamera alle 30 Sekunden.",
        "example_cue": "Angenommen, eine Schicht hat",
        "script": "Hier ist die Kernidee. TAKT kommt vom deutschen Wort für Schlag oder Rhythmus. Es ist "
                  "das Tempo, in dem Sie Einheiten fertigstellen müssen, um den Kundenbedarf zu decken. Die "
                  "Formel ist einfach. Teilen Sie Ihre netto verfügbare Zeit durch den Bedarf. Angenommen, "
                  "eine Schicht hat vierhundertzwanzig Minuten. Der Kunde braucht achthundertvierzig "
                  "Kameras. Das ist eine Kamera alle dreißig Sekunden. Ist das die Zeit, die ein Werker "
                  "wirklich braucht? Nein.",
    },
    {
        "key": "p02", "num": 2, "title": "Warum die TAKT Zeit zählt",
        "points": [("Verbindet Ihren Kunden mit der Fertigung", "TAKT verbindet Ihren Kunden"),
                   ("Kein gemeinsames Tempo → Überproduktion, WIP", "Ohne gemeinsames Tempo"),
                   ("Personal planen, Arbeit abstimmen, Material takten", "TAKT hilft Ihnen")],
        "example": "Rohans Montage baute 1.000 Kameras vor dem Test auf Vorrat. Die Auslastung sah toll aus; "
                   "die Lkw fuhren trotzdem zu spät.",
        "example_cue": "Seine Montage baute",
        "script": "TAKT verbindet Ihren Kunden mit der Fertigung. Ohne gemeinsames Tempo überproduzieren "
                  "frühe Stationen, und WIP stapelt sich. Engpässe verstecken sich, und der Versand wird "
                  "zur Hetze. Genau das passierte Rohan. Seine Montage baute tausend Kameras vor dem Test "
                  "auf Vorrat. Die Auslastung sah toll aus. Aber die Lkw fuhren trotzdem zu spät. TAKT "
                  "hilft Ihnen, Personal zu planen, Arbeit abzustimmen und Material zu takten. Aber zuerst "
                  "brauchen Sie die richtigen Zahlen. Wo beginnen Sie?",
    },
    {
        "key": "p03", "num": 3, "title": "Netto verfügbare Zeit",
        "points": [("Mit der Schichtlänge beginnen", "Nehmen Sie Ihre Schichtlänge"),
                   ("Geplante Pausen, Besprechungen, Reinigung abziehen", "Dann ziehen Sie geplante"),
                   ("Zufällige Stillstände hier nicht abziehen", "ziehen Sie zufällige Stillstände"),
                   ("Ihre Annahmen aufschreiben", "schreiben Sie Ihre Annahmen auf")],
        "example": "480 Min. Schicht − Pausen − kurze Besprechung = 420 Netto-Minuten.",
        "example_cue": "Eine Achtstundenschicht",
        "script": "Beginnen Sie mit der netto verfügbaren Zeit. Nehmen Sie Ihre Schichtlänge. Dann ziehen "
                  "Sie geplante Pausen, Besprechungen und geplante Reinigung ab. Eine Achtstundenschicht "
                  "hat vierhundertachtzig Minuten. Ohne Pausen und eine kurze Besprechung bleiben "
                  "vierhundertzwanzig. Aber ziehen Sie zufällige Stillstände hier nicht ab. Das ist ein "
                  "Verlust, den Sie bei der Kapazitätsprüfung behandeln. Bleiben Sie einheitlich, und "
                  "schreiben Sie Ihre Annahmen auf. Und die andere Hälfte der Formel?",
    },
    {
        "key": "p04", "num": 4, "title": "Kundenbedarf",
        "points": [("Bedarf und Zeit: gleicher Zeitraum", "Der Bedarf muss"),
                   ("Benötigte gute Einheiten, nicht gestartete", "Nutzen Sie die guten Einheiten"),
                   ("Gemischte Modelle: jedes prüfen", "Auf einer Linie mit gemischten Modellen"),
                   ("Neu berechnen, wenn Bedarf oder Schichten sich ändern", "berechnen Sie neu")],
        "example": "Tagesbedarf mit der Zeit einer Schicht = Unsinn.",
        "example_cue": "Tagesbedarf mit der Zeit",
        "script": "Der Bedarf muss denselben Zeitraum abdecken wie Ihre Zeit. Nutzen Sie Tagesbedarf, dann "
                  "auch die tägliche Nettozeit. Tagesbedarf mit der Zeit einer Schicht ergibt Unsinn. "
                  "Nutzen Sie die guten Einheiten, die Ihr Kunde braucht, nicht die gestarteten. Auf einer "
                  "Linie mit gemischten Modellen ist der Gesamt-TAKT ein Richtwert. Aber jedes Modell "
                  "braucht seine eigene Kapazitätsprüfung. Und berechnen Sie neu, wenn Bedarf oder "
                  "Schichten sich ändern. Wie unterscheidet sich TAKT von der Zykluszeit?",
    },
    {
        "key": "p05", "num": 5, "title": "TAKT, Zykluszeit, Durchlaufzeit",
        "points": [("TAKT: das nötige Tempo", "TAKT ist das nötige Tempo"),
                   ("Zykluszeit: was eine Station braucht", "Die Zykluszeit ist"),
                   ("Durchlaufzeit: der ganze Weg", "Die Durchlaufzeit ist"),
                   ("Zyklus > TAKT = hält nicht mit", "Ist Ihre Zykluszeit")],
        "example": "Eine von Rohans Linien: Endtest 38 s gegen TAKT 30 s. Er brauchte Verbesserung, oder "
                   "einen zweiten Tester.",
        "example_cue": "An einer von Rohans Linien",
        "script": "Das ist die häufigste Verwechslung. TAKT ist das nötige Tempo. Die Zykluszeit ist, was "
                  "eine Station wirklich braucht, gemessen in der Fertigung. Die Durchlaufzeit ist der "
                  "ganze Weg, mit Warten und Transport. Ist Ihre Zykluszeit länger als der TAKT, hält diese "
                  "Station nicht mit. An einer von Rohans Linien dauerte der Endtest achtunddreißig "
                  "Sekunden, bei einem TAKT von dreißig. Er brauchte Verbesserung, oder einen zweiten "
                  "Tester. Legen Sie immer zuerst Start und Ende fest.",
    },
    {
        "key": "p06", "num": 6, "title": "Pitch, UPH und UPPH",
        "points": [("UPH: die nötige Stundenrate", "Einheiten pro Stunde"),
                   ("Pitch: Zeit für eine volle Packung", "Der Pitch ist"),
                   ("UPPH: gute Leistung pro Personenstunde", "UPPH misst"),
                   ("Theorie ist keine Leistung", "Theorie ist keine Leistung")],
        "example": "TAKT 24 s → 150 Einheiten pro Stunde. Packung zu 20 → ein Pitch von 8 Minuten.",
        "example_cue": "Bei einem TAKT von",
        "script": "TAKT hängt mit ein paar nützlichen Zahlen zusammen. Einheiten pro Stunde, kurz UPH, ist "
                  "die nötige Stundenrate. Der Pitch ist die Zeit, um eine Standardpackung zu füllen. Bei "
                  "einem TAKT von vierundzwanzig Sekunden brauchen Sie hundertfünfzig Einheiten pro Stunde. "
                  "Eine Packung zu zwanzig ergibt einen Pitch von acht Minuten. UPPH misst gute Leistung "
                  "pro Personenstunde. Aber denken Sie daran, Theorie ist keine Leistung. Die echte "
                  "Leistung hängt von Verfügbarkeit und Ausbeute ab. Wie stimmen Sie die Arbeit ab?",
    },
    {
        "key": "p07", "num": 7, "title": "Abstimmen mit Yamazumi",
        "points": [("Jedes Arbeitselement messen", "Zerlegen Sie jede Arbeit"),
                   ("Die Arbeit jedes Werkers als Balken stapeln", "Stapeln Sie die Arbeit"),
                   ("Die TAKT Linie quer ziehen", "Dann ziehen Sie die TAKT Linie"),
                   ("Verlegen oder umgestalten, im Rahmen von Sicherheit und Können", "Also verlegen oder gestalten Sie")],
        "example": "TAKT 40 s: Werker A hat 52 s Arbeit, Werker B nur 25 s.",
        "example_cue": "In einer von Rohans Zellen",
        "script": "Sie nutzen ein Yamazumi-Diagramm. Zerlegen Sie jede Arbeit in wiederholbare Elemente, "
                  "und messen Sie sie. Stapeln Sie die Arbeit jedes Werkers als Balken. Dann ziehen Sie die "
                  "TAKT Linie quer. Jeder Balken über der Linie ist überlastet. In einer von Rohans Zellen "
                  "war der TAKT vierzig Sekunden. Werker A hatte zweiundfünfzig Sekunden Arbeit. Werker B "
                  "nur fünfundzwanzig. Also verlegen oder gestalten Sie Aufgaben um, im Rahmen von "
                  "Sicherheit und Können. Wie viele Leute brauchen Sie?",
    },
    {
        "key": "p08", "num": 8, "title": "Mindestzahl an Werkern",
        "points": [("Arbeitsinhalt ÷ TAKT, aufrunden", "Teilen Sie den gesamten"),
                   ("Nur ein Ausgangspunkt", "nehmen Sie das als Ausgangspunkt"),
                   ("Eine stabile Zeitstudie nutzen", "Nutzen Sie eine stabile Zeitstudie")],
        "example": "310 s Arbeit ÷ 40 s TAKT = 7,75 → mindestens 8 Werker.",
        "example_cue": "Rohans Zelle hatte",
        "script": "Hier eine schnelle Schätzung. Teilen Sie den gesamten manuellen Arbeitsinhalt durch den "
                  "TAKT, dann runden Sie auf. Rohans Zelle hatte dreihundertzehn Sekunden Arbeit pro "
                  "Kamera. Bei einem TAKT von vierzig sind das sieben Komma sieben fünf. Sie brauchen also "
                  "mindestens acht Werker. Aber nehmen Sie das als Ausgangspunkt. Wege, Nachschub, "
                  "Qualitätsprüfungen und Können zählen alle. Nutzen Sie eine stabile Zeitstudie, nicht "
                  "einen Bestfall-Zyklus. Was begrenzt Ihre Leistung?",
    },
    {
        "key": "p09", "num": 9, "title": "Engpässe und parallele Stationen",
        "points": [("Der Engpass begrenzt die gute Leistung", "Es ist der Schritt"),
                   ("Kapazität = 3.600 ÷ Zykluszeit", "Die Stundenkapazität einer Station"),
                   ("Verfügbarkeit und Erstdurchlaufquote anwenden", "Wenden Sie Verfügbarkeit"),
                   ("Belege vor dem Maschinenkauf", "Prüfen Sie die Belege")],
        "example": "Zwei Tester zu 50 s = 144 Versuche pro Stunde → etwa 127 gute Einheiten nach "
                   "Verfügbarkeit und Ausbeute.",
        "example_cue": "Zwei Tester zu je fünfzig",
        "script": "Der Engpass. Es ist der Schritt, der Ihre gute Leistung begrenzt. Die Stundenkapazität "
                  "einer Station ist dreitausendsechshundert Sekunden, geteilt durch ihre Zykluszeit. Zwei "
                  "Tester zu je fünfzig Sekunden ergeben hundertvierundvierzig Versuche pro Stunde. Aber "
                  "Tester stoppen, und manche Einheiten fallen durch. Wenden Sie Verfügbarkeit und "
                  "Erstdurchlaufquote an, und Sie erhalten etwa hundertsiebenundzwanzig gute Einheiten. "
                  "Prüfen Sie die Belege, bevor Sie eine Maschine kaufen. Und gemischte Modelle?",
    },
    {
        "key": "p10", "num": 10, "title": "Gemischte Modelle und Heijunka",
        "points": [("Ein TAKT passt nicht für jedes Modell", "Ein einziger TAKT"),
                   ("Stationszeiten jedes Modells prüfen", "Prüfen Sie also die Stationszeiten"),
                   ("Heijunka: Menge und Mix glätten", "Nutzen Sie Heijunka"),
                   ("SMED: Rüstverluste senken", "nutzen Sie SMED")],
        "example": "60 % Modell A, 40 % Modell B mit längerem Test: alle B zusammen einplanen, und der Test "
                   "ertrinkt.",
        "example_cue": "Angenommen, sechzig Prozent",
        "script": "Ein einziger TAKT garantiert nicht, dass jedes Modell passt. Angenommen, sechzig Prozent "
                  "von Rohans Bedarf ist Modell A, und vierzig Prozent Modell B. Modell B braucht einen "
                  "längeren Test. Plant man alle B zusammen ein, ertrinkt der Test, obwohl der Durchschnitt "
                  "gut aussieht. Prüfen Sie also die Stationszeiten jedes Modells. Nutzen Sie Heijunka, um "
                  "Menge und Mix zu glätten. Und nutzen Sie SMED, um Rüstverluste zu senken. Und das "
                  "Material?",
    },
    {
        "key": "p11", "num": 11, "title": "Materialfluss und Kanban",
        "points": [("TAKT gibt den Materialrhythmus vor", "TAKT gibt auch"),
                   ("Kanban: Wiederbeschaffungszeit, Behältergröße", "Kanban-Mengen"),
                   ("WIP-Grenzen zwischen Prozessen", "Setzen Sie WIP-Grenzen"),
                   ("Keine Arbeit freigeben, nur um beschäftigt zu sein", "Geben Sie keine neuen")],
        "example": "TAKT 30 s, Kiste mit 40 → reicht 20 Minuten; der Nachschub muss schneller sein.",
        "example_cue": "Bei einem TAKT von dreißig",
        "script": "TAKT gibt auch den Rhythmus für Material vor. Bei einem TAKT von dreißig Sekunden reicht "
                  "eine Kiste mit vierzig Teilen zwanzig Minuten. Der Nachschub muss also vorher kommen, "
                  "mit etwas Schutz für Schwankungen. Kanban-Mengen hängen auch von Wiederbeschaffungszeit "
                  "und Behältergröße ab. Setzen Sie WIP-Grenzen zwischen Prozessen. Und eine harte Regel. "
                  "Geben Sie keine neuen Aufträge frei, nur damit jede Station beschäftigt ist. Wie führen "
                  "Sie den Tag?",
    },
    {
        "key": "p12", "num": 12, "title": "Stündlich Plan gegen Ist",
        "points": [("Plan = Nettosekunden ÷ TAKT", "Geplante Einheiten sind"),
                   ("Ist mit Plan vergleichen", "Angenommen, Sie schaffen"),
                   ("Grund erfassen: Stillstand, Ausschuss, Material", "Nun erfassen Sie den Grund"),
                   ("Nicht das Werkertempo beschuldigen", "Schieben Sie nicht jeden Rückstand")],
        "example": "TAKT 30 s → 120 geplant pro Stunde. 108 geschafft = 90 %, eine Lücke von 12.",
        "example_cue": "Bei einem TAKT von dreißig",
        "script": "Nutzen Sie eine stündliche Tafel Plan gegen Ist. Geplante Einheiten sind die "
                  "Nettosekunden der Stunde, geteilt durch den TAKT. Bei einem TAKT von dreißig Sekunden "
                  "planen Sie hundertzwanzig gute Kameras. Angenommen, Sie schaffen hundertacht. Das sind "
                  "neunzig Prozent, eine Lücke von zwölf. Nun erfassen Sie den Grund. Stillstand, "
                  "Ausschuss, Material oder Personal. Schieben Sie nicht jeden Rückstand auf das "
                  "Werkertempo. Bereit für Rohans ganzen Fall?",
    },
    {
        "key": "p13", "num": 13, "title": "Fallstudie: Kamerawerk",
        "points": [("7.200 gute Kameras pro Tag, 1.200 Netto-Min.", "Rohans Werk muss"),
                   ("TAKT = 10 Sekunden", "Also ist der TAKT zehn Sekunden"),
                   ("Test braucht 18 s: der Engpass", "Aber der Test braucht"),
                   ("Zwei Tester ≈ 353 gute/Stunde gegen 360", "Zwei Tester ergeben")],
        "example": "2 Tester = 400 Versuche/Stunde auf dem Papier → ≈ 353 gute bei echter Verfügbarkeit und "
                   "Ausbeute. Ziel: 360.",
        "example_cue": "Bei echter Verfügbarkeit",
        "script": "Rohans Werk muss siebentausendzweihundert gute Kameras am Tag liefern. Es hat "
                  "zwölfhundert Netto-Minuten, über drei Schichten. Also ist der TAKT zehn Sekunden. "
                  "Linsen- und Montagestationen sind schneller. Aber der Test braucht achtzehn Sekunden. "
                  "Zwei Tester ergeben auf dem Papier vierhundert Versuche pro Stunde. Bei echter "
                  "Verfügbarkeit und Ausbeute sind das etwa dreihundertdreiundfünfzig gute Einheiten. Das "
                  "Ziel ist dreihundertsechzig. Was würden Sie tun?",
    },
    {
        "key": "p14", "num": 14, "title": "Häufige Fehler",
        "points": [("JA: freigegebener Bedarf und Nettozeit", "Nutzen Sie freigegebenen Bedarf"),
                   ("JA: TAKT bei Änderungen anpassen", "Passen Sie den TAKT an"),
                   ("NEIN: mit Zykluszeit verwechseln", "Verwechseln Sie ihn nicht"),
                   ("NEIN: Tests, Schritte oder Pausen auslassen", "Tests, SOP-Schritte oder Pausen")],
        "example": "Rohan verbesserte die Verfügbarkeit der Tester und kürzte den Testzyklus, bevor er einen "
                   "dritten Tester kaufte.",
        "example_cue": "Rohan verbesserte die Verfügbarkeit",
        "script": "Rohan verbesserte die Verfügbarkeit der Tester, und kürzte den Testzyklus, bevor er "
                  "einen dritten kaufte. Nun, achten Sie auf häufige Fehler. Nutzen Sie freigegebenen "
                  "Bedarf und die richtige Nettozeit. Passen Sie den TAKT an, wenn Bedarf oder Schichten "
                  "sich ändern. Verwechseln Sie ihn nicht mit der Zykluszeit. Nutzen Sie keine "
                  "Brutto-Schichtstunden. Und jagen Sie nie Tempo, indem Sie Tests, SOP-Schritte oder "
                  "Pausen auslassen. Können Ihre Führungskräfte die Zahlen hinter dem TAKT erklären?",
    },
    {
        "key": "p15", "num": 15, "title": "Fahrplan für 90 Tage",
        "points": [("Tag 1–30: Bedarf, Nettozeit, Zykluszeiten", "In den ersten dreißig Tagen"),
                   ("Tag 31–60: Yamazumi, Stundentafeln", "In den nächsten dreißig"),
                   ("Tag 61–90: Leistung und Ausbeute bestätigen, ausweiten", "In den letzten dreißig"),
                   ("Ziel: verlässliche gute Leistung", "Denken Sie an das Ziel")],
        "example": "Verlässliche gute Leistung im Tempo des Kunden, nicht jede Station beschäftigt halten.",
        "example_cue": "Es ist verlässliche gute Leistung",
        "script": "Beginnen Sie mit einer typischen Linie Ihres Werks. In den ersten dreißig Tagen sammeln "
                  "Sie Bedarf, Nettozeit und echte Zykluszeiten, und bilden die aktuelle Abstimmung ab. In "
                  "den nächsten dreißig pilotieren Sie Yamazumi, Standardarbeit und Stundentafeln. Gehen "
                  "Sie den Engpass an. In den letzten dreißig bestätigen Sie Leistung und Ausbeute, schulen "
                  "Vertretungen und weiten aus. Denken Sie an das Ziel. Es ist verlässliche gute Leistung "
                  "im Tempo des Kunden. Nicht jede Station beschäftigt halten.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Takt = Schlag", "icon": "wave", "with": 0}, {"label": "Das Tempo, das der Bedarf vorgibt", "icon": "clock", "with": 1},
        {"label": "Nettozeit ÷ Bedarf", "icon": "count", "with": 2}],
        "then": {"type": "stat", "value": 30, "suffix": " s", "icon": "camera", "label": "eine Kamera alle 30 Sekunden",
                 "unit": "420 Netto-Minuten ÷ 840 Kameras", "with": "example"}},
    "p02": {"type": "versus", "items": [
        {"label": "1.000 vor dem Test gebaut", "sub": "Beschäftigte Stationen, späte Lkw", "icon": "stack", "with": "example"},
        {"label": "Ein gemeinsames Tempo", "sub": "Personal, Abstimmung, Material", "icon": "clock", "with": 2}]},
    "p03": {"type": "flow", "items": [
        {"label": "480 Min. Schicht", "icon": "clock", "with": 0},
        {"label": "− Pausen, Besprechung, Reinigung", "icon": "calendar", "with": 1},
        {"label": "= 420 Netto-Minuten", "sub": "Zufälliger Stillstand wird hier nicht abgezogen", "icon": "check", "tone": "good", "with": "example"}]},
    "p04": {"type": "versus", "items": [
        {"label": "Tagesbedarf ÷ eine Schicht", "sub": "Ergibt Unsinn", "icon": "cross", "with": "example"},
        {"label": "Gleicher Zeitraum für beide", "sub": "Gute Einheiten, nicht gestartete", "icon": "calendar", "with": 0}]},
    "p05": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Das nötige Tempo", "icon": "clock", "with": 0},
        {"label": "Zykluszeit", "sub": "Was eine Station braucht", "icon": "gear", "with": 1},
        {"label": "Durchlaufzeit", "sub": "Der ganze Weg", "icon": "sequence", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "Test hält nicht mit: verbessern, oder einen Tester ergänzen", "unit": "Sekunden pro Kamera", "with": "example", "items": [
            {"label": "TAKT", "value": 30, "tone": "good", "with": "example"},
            {"label": "Endtest", "value": 38, "tone": "bad", "with": "example"}]}},
    "p06": {"type": "icons", "items": [
        {"label": "UPH", "sub": "Nötige Stundenrate", "icon": "chartUp", "with": 0},
        {"label": "Pitch", "sub": "Zeit für eine volle Packung", "icon": "box", "with": 1},
        {"label": "UPPH", "sub": "Gute Leistung pro Personenstunde", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "TAKT 24 s", "icon": "clock", "with": "example"},
            {"label": "= 150 Einheiten pro Stunde", "icon": "chartUp", "with": "example"},
            {"label": "Packung zu 20 = Pitch von 8 Min.", "icon": "box", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Jedes Element messen", "icon": "clock"}, {"label": "Jeden Werker stapeln", "icon": "stack"},
        {"label": "Die TAKT Linie ziehen", "icon": "sequence"}, {"label": "Arbeit sicher verlegen", "icon": "person"}],
        "then": {"type": "bars", "label": "TAKT", "value": 40, "suffix": " s", "note": "A ist überlastet", "unit": "Sekunden Arbeit pro Werker", "with": "example", "items": [
            {"label": "Werker A", "value": 52, "tone": "bad", "with": "example"},
            {"label": "Werker B", "value": 25, "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Arbeit ÷ TAKT, aufrunden", "icon": "count", "with": 0},
        {"label": "Ein Ausgangspunkt", "icon": "sequence", "with": 1},
        {"label": "Stabile Zeitstudie", "icon": "clock", "with": 2}],
        "then": {"type": "stat", "value": 8, "icon": "person", "label": "Werker, mindestens",
                 "unit": "310 s Arbeit ÷ 40 s TAKT = 7,75, aufgerundet", "with": "example"}},
    "p09": {"type": "icons", "items": [
        {"label": "Der Engpass", "icon": "warning", "tone": "bad"}, {"label": "3.600 ÷ Zykluszeit", "icon": "count"},
        {"label": "Verfügbarkeit × Ausbeute", "icon": "chartUp"}, {"label": "Zuerst Belege", "icon": "search"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "2 Tester zu 50 s", "icon": "test", "with": "example"},
            {"label": "144 Versuche pro Stunde", "icon": "count", "with": "example"},
            {"label": "≈ 127 gute nach Verfügbarkeit, Ausbeute", "icon": "check", "tone": "good", "with": "example"}]}},
    "p10": {"type": "versus", "items": [
        {"label": "Alle B zusammen", "sub": "Der Test ertrinkt", "icon": "stack", "with": "example"},
        {"label": "Den Mix glätten", "sub": "Heijunka + SMED", "icon": "sequence", "with": 2}]},
    "p11": {"type": "stat", "value": 20, "suffix": " Min.", "icon": "box", "label": "eine Kiste mit 40 Teilen reicht",
            "unit": "bei TAKT 30 s: der Nachschub muss schneller sein", "with": "example"},
    "p12": {"type": "bars", "label": "", "note": "90 %: eine Lücke von 12. Grund erfassen.", "unit": "gute Kameras in einer Stunde, TAKT 30 s", "items": [
        {"label": "Geplant", "value": 120, "with": "example"},
        {"label": "Geschafft", "value": 108, "tone": "bad", "with": "example"}]},
    "p13": {"type": "stat", "value": 10, "suffix": " s", "icon": "clock", "label": "TAKT für 7.200 gute Kameras pro Tag",
            "unit": "1.200 Netto-Minuten ÷ 7.200 Kameras", "with": 1,
            "then": {"type": "bars", "label": "Ziel", "value": 360, "unit": "gute Kameras pro Stunde, zwei Tester", "with": 3, "items": [
                {"label": "Auf dem Papier", "value": 400, "with": 3},
                {"label": "Echt", "value": 353, "tone": "bad", "with": 3}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Freigegebener Bedarf + Nettozeit", "icon": "check", "tone": "good"},
        {"label": "Bei Änderungen anpassen", "icon": "sequence", "tone": "good"},
        {"label": "Nicht die Zykluszeit", "icon": "cross", "tone": "bad"},
        {"label": "Nie Tests oder Pausen auslassen", "icon": "warning", "tone": "bad"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Bedarf, Nettozeit, Zykluszeiten", "sub": "Tag 1–30", "icon": "clipboard", "with": 0},
        {"label": "Yamazumi, Stundentafeln", "sub": "31–60", "icon": "stack", "with": 1},
        {"label": "Leistung und Ausbeute bestätigen, ausweiten", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Eine Schicht hat 25.200 Nettosekunden, und der Kunde braucht 840 Einheiten. Wie lang ist "
                    "die TAKT Zeit?",
        "options": ["20 Sekunden", "30 Sekunden", "40 Sekunden"],
        "correct": 1,
        "explanation": "TAKT = netto verfügbare Zeit ÷ Bedarf = 25.200 ÷ 840 = 30 Sekunden pro Einheit.",
        "q_script": "Kurzer Check. Eine Schicht hat fünfundzwanzigtausendzweihundert Nettosekunden. Der Kunde "
                    "braucht achthundertvierzig Einheiten. Wie lang ist die TAKT Zeit? Nehmen Sie sich kurz "
                    "Zeit.",
        "a_script": "Dreißig Sekunden. TAKT ist die netto verfügbare Zeit, geteilt durch den Bedarf. Also "
                    "eine Einheit alle dreißig Sekunden.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Der Endtest braucht 38 s pro Einheit, aber der TAKT ist 30 s. Ein Manager sagt: „Die "
                    "Tester sollen schneller arbeiten.\" Was sollte das Team ZUERST tun?",
        "options": ["Einen Teil des Tests auslassen, um Zeit zu sparen", "Verluste und Kapazität der Teststation analysieren",
                    "Vorn zusätzlichen Bestand aufbauen", "Den TAKT mit Brutto-Schichtzeit neu berechnen"],
        "correct": 1,
        "explanation": "Eine Zykluszeit über dem TAKT ist ein Kapazitätsproblem. Untersuchen Sie Verluste, "
                       "Zyklus und Verfügbarkeit der Station, dann verbessern Sie oder ergänzen bestätigte "
                       "Kapazität. Tests auslassen oder mit Bestand verdecken schafft neue Probleme.",
        "q_script": "Noch eine, ein Szenario. Der Endtest braucht achtunddreißig Sekunden, aber der TAKT ist "
                    "dreißig. Ein Manager sagt, die Tester sollen schneller arbeiten. Was sollte das Team "
                    "zuerst tun? Überlegen Sie kurz.",
        "a_script": "Analysieren Sie zuerst die Teststation. Untersuchen Sie Verluste, Zyklus und "
                    "Verfügbarkeit, dann verbessern Sie sie, oder ergänzen bewiesene Kapazität. Tests "
                    "auslassen oder Bestand aufbauen schafft nur neue Probleme.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
