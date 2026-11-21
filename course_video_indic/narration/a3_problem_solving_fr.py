"""a3_problem_solving in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh a3_problem_solving_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "a3_fr"
NAME = "a3_problem_solving_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Burn Down Chart": "beurne daoune tchart",
    "Five Whys": "faïve ouaïze",
    "Ishikawa": "Ichikawa",
    "Genbutsu": "Guène-boutsou",
    "Genjitsu": "Guène-djitsou",
    "Pareto": "Paréto",
    "Gemba": "Guemba",
    "PDCA": "pé dé cé a",
    "MES": "emme eu esse",
    "SOP": "esse o pé",
    "A3": "a trois",
    "3G": "trois gé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Cinq cent soixante-seize serveurs ont échoué à leur premier test de démarrage en quatre "
    "semaines. La première solution proposée ? Ajouter deux contrôleurs de plus. Ça vous dit "
    "quelque chose ? Dans cette leçon, vous allez découvrir la résolution de problèmes A3. "
    "Vous verrez comment raconter toute l'histoire d'un problème sur une seule page, de "
    "l'écart réel à une solution prouvée. Nous suivrons Karthik, ingénieur de test sur une "
    "ligne d'assemblage de serveurs, qui rédige son premier A3."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Partez d'un écart mesurable, jamais d'une cause ou d'une "
    "solution. Allez voir, et prouvez chaque cause avec des preuves. Et ne standardisez que "
    "ce que votre pilote a vraiment prouvé. Voici votre action pour cette semaine. Choisissez "
    "un problème récurrent, et écrivez son énoncé sur une feuille A3. Bravo d'avoir terminé "
    "cette leçon. Ensuite, vous découvrirez le Burn Down Chart, pour suivre le travail par "
    "rapport au temps."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est un A3",
        "points": [("Nommé d'après le format de papier A3", "Un A3 doit son nom"),
                   ("Toute l'histoire du problème sur une page", "Il raconte toute l'histoire"),
                   ("Définir, trouver les causes, tester, pérenniser", "Vous définissez le problème"),
                   ("Visuel, et construit en équipe", "Il est visuel")],
        "example": "Le rapport de Karthik disait « les opérateurs sont négligents ». Son responsable lui a "
                   "rendu une feuille A3 vierge.",
        "example_cue": "Son rapport disait",
        "script": "Un A3 doit son nom à un format de papier. Il raconte toute l'histoire d'un problème sur "
                  "une seule page. Vous définissez le problème, trouvez ses vraies causes, testez des "
                  "solutions et maintenez les résultats. Il est visuel, et vous le construisez en équipe. "
                  "Voici comment Karthik a découvert son premier A3. Son rapport disait que les opérateurs "
                  "sont négligents. Son responsable le lui a rendu, avec une feuille A3 vierge. Alors, "
                  "qu'est-ce qui compte vraiment comme un problème ?",
    },
    {
        "key": "p02", "num": 2, "title": "Les problèmes sont des écarts",
        "points": [("Un problème est un écart mesurable", "Un problème est un écart"),
                   ("Ne sautez pas de la plainte à la solution", "L'A3 vous empêche de sauter"),
                   ("Un écart peut être mesuré et étudié", "Vous pouvez mesurer un écart")],
        "example": "« Les opérateurs sont négligents » est un reproche. « Les échecs de démarrage sont "
                   "passés à 4,8 % » est un écart.",
        "example_cue": "Comparez deux phrases",
        "script": "Voici l'idée clé. Un problème est un écart, entre ce qui se passe et le standard dont "
                  "vous avez besoin. L'A3 vous empêche de sauter d'une plainte directement à une solution. "
                  "Comparez deux phrases. Les opérateurs sont négligents, c'est un reproche. Les échecs de "
                  "démarrage sont passés à quatre virgule huit pour cent. Ça, c'est un écart. Vous pouvez "
                  "mesurer un écart. Vous pouvez aussi l'étudier. Quel type de phrase entendez-vous le plus "
                  "dans votre atelier ?",
    },
    {
        "key": "p03", "num": 3, "title": "Où se place l'A3 : PDCA",
        "points": [("Les problèmes qui reviennent sans cesse", "Utilisez-le pour les problèmes"),
                   ("Les problèmes que les équipes doivent résoudre ensemble", "Il est idéal quand"),
                   ("Basé sur Plan · Do · Check · Act", "il suit le PDCA")],
        "example": "Les échecs de démarrage de Karthik : répétés, coûteux et transverses.",
        "example_cue": "Les échecs de démarrage de Karthik",
        "script": "Où se place l'A3 ? Utilisez-le pour les problèmes qui reviennent sans cesse. Défauts "
                  "répétés, arrêts, ruptures et production manquée sont de bons candidats. Il est idéal "
                  "quand la production, la qualité et l'ingénierie doivent résoudre quelque chose ensemble. "
                  "Et au fond, il suit le PDCA. Vous planifiez, puis vous faites un petit pilote. Vous "
                  "vérifiez les résultats par rapport à la cible. Puis vous agissez, en standardisant ou en "
                  "repensant. Les échecs de démarrage de Karthik s'y prêtent parfaitement. Alors, que "
                  "met-on sur la feuille ?",
    },
    {
        "key": "p04", "num": 4, "title": "Anatomie d'un A3",
        "points": [("À gauche : contexte, situation actuelle, cible", "Le côté gauche"),
                   ("Analyse des causes racines : pourquoi l'écart existe", "L'analyse des causes racines explique"),
                   ("À droite : contre-mesures, plan, suivi", "Le côté droit"),
                   ("Chaque case répond à une question", "Chaque case répond")],
        "example": "La feuille de Karthik : sept cases, une page, lue de gauche à droite.",
        "example_cue": "La feuille de Karthik a",
        "script": "Imaginez la feuille. Le côté gauche raconte l'histoire jusqu'ici. Le contexte dit "
                  "pourquoi c'est important maintenant. La situation actuelle montre ce qui se passe "
                  "vraiment. La cible dit quel résultat, et pour quand. L'analyse des causes racines "
                  "explique pourquoi l'écart existe. Le côté droit passe à l'action, avec des "
                  "contre-mesures, un plan et un suivi. Chaque case répond à une question. La feuille de "
                  "Karthik a sept cases, lues de gauche à droite. Sauriez-vous nommer la question derrière "
                  "chacune ?",
    },
    {
        "key": "p05", "num": 5, "title": "L'énoncé du problème",
        "points": [("Nommez l'écart, jamais une cause", "nomme l'écart"),
                   ("Ligne · produit · période · mesure", "Nommez la ligne"),
                   ("Un dénominateur clair, mêmes définitions", "Utilisez un dénominateur clair"),
                   ("Pas de reproche, pas de solution", "Il n'y a pas de reproche")],
        "example": "Ligne 2, le mois dernier : 4,8 % de 12 000 serveurs ont échoué au premier test de "
                   "démarrage, contre une référence de 1,5 %.",
        "example_cue": "Voici la version de Karthik",
        "script": "Voici maintenant la case la plus difficile à réussir. Un bon énoncé nomme l'écart, mais "
                  "n'affirme jamais une cause. Nommez la ligne, le produit, la période et la mesure. "
                  "Utilisez un dénominateur clair et les mêmes définitions. Voici la version de Karthik. Le "
                  "mois dernier sur la ligne deux, les échecs au premier test de démarrage ont atteint en "
                  "moyenne quatre virgule huit pour cent. La référence était de un virgule cinq, sur douze "
                  "mille serveurs. Vous remarquez ce qui manque ? Il n'y a pas de reproche, ni de solution.",
    },
    {
        "key": "p06", "num": 6, "title": "Aller voir : les 3G",
        "points": [("Gemba : le lieu réel", "Gemba est le lieu réel"),
                   ("Genbutsu : les choses réelles", "Genbutsu veut dire"),
                   ("Genjitsu : les faits réels", "Genjitsu veut dire")],
        "example": "7 serveurs défaillants sur 10 au banc : un module mémoire légèrement soulevé.",
        "example_cue": "Karthik a posé dix",
        "script": "Avant d'ouvrir un tableur, allez voir. Le Lean appelle ça les 3G. Gemba est le lieu "
                  "réel, donc vous vous tenez au poste de test. Genbutsu veut dire les choses réelles, "
                  "comme les serveurs défaillants, les gabarits et les journaux de test. Genjitsu veut dire "
                  "les faits réels, que vous vérifiez vous-même. Karthik a posé dix serveurs défaillants "
                  "sur le banc. Sur sept d'entre eux, un module mémoire était légèrement soulevé. Un "
                  "rapport le lui aurait-il jamais montré ?",
    },
    {
        "key": "p07", "num": 7, "title": "Des données fiables",
        "points": [("Une définition claire", "commencent par une définition claire"),
                   ("Comptez les unités uniques : les retests ne peuvent pas cacher les échecs", "Pourquoi uniques ?"),
                   ("Vérifiez horodatages, numéros de série, étalonnage", "Les horodatages sont-ils justes"),
                   ("Le journal de ligne correspond au MES", "Le journal de la ligne")],
        "example": "Taux d'échec au premier passage = serveurs uniques échouant à leur premier test valide ÷ "
                   "serveurs uniques testés.",
        "example_cue": "Le taux d'échec au premier passage est",
        "script": "De bonnes données commencent par une définition claire. La règle de Karthik était "
                  "simple. Le taux d'échec au premier passage est le nombre de serveurs uniques échouant à "
                  "leur premier test valide, divisé par le nombre de serveurs uniques testés. Pourquoi "
                  "uniques ? Parce que les retests peuvent cacher des échecs, ou compter un serveur deux "
                  "fois. Ensuite, vérifiez les données elles-mêmes. Les horodatages sont-ils justes, et "
                  "chaque numéro de série est-il unique ? Le testeur est-il étalonné ? Le journal de la "
                  "ligne correspond-il au MES ? Alors seulement vous pouvez faire confiance à votre "
                  "graphique.",
    },
    {
        "key": "p08", "num": 8, "title": "Voir l'écart",
        "points": [("Tendance hebdomadaire : en hausse chaque semaine", "tendance hebdomadaire a grimpé"),
                   ("Environ 400 échecs en trop", "Cela fait près de quatre cents"),
                   ("Pareto : trier les échecs par mode", "Puis un diagramme de Pareto")],
        "example": "Mémoire non détectée : 288 sur 576 échecs, la moitié du total.",
        "example_cue": "Mémoire non détectée",
        "script": "Alors, qu'a montré le graphique ? La tendance hebdomadaire a grimpé chaque semaine sans "
                  "exception. À la semaine quatre, elle atteignait cinq et demi pour cent. Au taux de "
                  "référence, on attendrait environ cent quatre-vingts échecs. Il en avait cinq cent "
                  "soixante-seize. Cela fait près de quatre cents de trop. Puis un diagramme de Pareto les "
                  "a classés par mode de défaillance. Mémoire non détectée représentait la moitié. L'écart "
                  "est clair, mais il ne prouve pas une cause. Par où commenceriez-vous ?",
    },
    {
        "key": "p09", "num": 9, "title": "Cible et périmètre",
        "points": [("Cible : 2 % ou moins en 6 semaines", "Celle de Karthik était claire"),
                   ("Garde-fous : temps de test, retests, fuites", "Ajoutez aussi des garde-fous"),
                   ("Périmètre : ce qui est dedans, ce qui est dehors", "Puis fixez le périmètre")],
        "example": "Hors périmètre : assouplir les limites de test pour paraître meilleur.",
        "example_cue": "Assouplir les limites de test",
        "script": "Ensuite, fixez une cible que vous pouvez réellement tester. Celle de Karthik était "
                  "claire. Réduire les échecs au premier test de démarrage sur la ligne deux à deux pour "
                  "cent ou moins, en six semaines. Ajoutez aussi des garde-fous, comme le temps de test, le "
                  "taux de retest et les défauts échappés. Ils garantissent que vous ne gagnez pas en "
                  "trichant. Puis fixez le périmètre. Les échecs mémoire de la ligne deux sont dedans. "
                  "Assouplir les limites de test est dehors. Voyez-vous pourquoi c'est important ?",
    },
    {
        "key": "p10", "num": 10, "title": "Explorer les causes : Ishikawa",
        "points": [("D'abord, pensez large", "pensez large"),
                   ("Six M : main-d'œuvre, machine, méthode…", "Il classe les causes possibles"),
                   ("Chaque branche est une supposition tant qu'elle n'est pas vérifiée", "Chaque branche n'est")],
        "example": "L'insertion est-elle formée ? Le châssis a-t-il changé ? Le verrouillage varie-t-il "
                   "selon le lot ?",
        "example_cue": "L'équipe de Karthik a posé",
        "script": "Maintenant, pourquoi l'écart existe-t-il ? D'abord, pensez large avec un diagramme "
                  "d'Ishikawa. Il classe les causes possibles en six M. Main-d'œuvre, machine, méthode, "
                  "matière, mesure et milieu. L'équipe de Karthik a posé des questions dans chacune. La "
                  "méthode d'insertion est-elle formée ? Le châssis a-t-il changé ? Le verrouillage du "
                  "module varie-t-il selon le lot ? Mais attention. Chaque branche n'est qu'une supposition "
                  "tant que vous ne l'avez pas vérifiée. Alors, comment réduire les pistes ?",
    },
    {
        "key": "p11", "num": 11, "title": "Cause racine : Five Whys",
        "points": [("Demandez pourquoi, étape par étape", "creusez avec les Five Whys"),
                   ("Finissez sur une cause de processus que vous pouvez corriger", "C'est une cause de processus"),
                   ("Une chaîne n'est pas une preuve : testez-la", "Mais une chaîne")],
        "example": "Cause racine : les instructions de travail n'ont pas été revues lors du changement de "
                   "châssis.",
        "example_cue": "Les instructions de travail n'ont pas été revues",
        "script": "Puis creusez avec les Five Whys. Pourquoi les serveurs ont-ils échoué au test de "
                  "démarrage ? Un module mémoire n'était pas bien enfoncé. Pourquoi ? Le loquet s'est fermé "
                  "avant que le module soit complètement descendu. Pourquoi ? Le nouveau châssis laissait "
                  "moins de place pour appuyer droit. Pourquoi la méthode n'a-t-elle pas changé ? Les "
                  "instructions de travail n'ont pas été revues lors du changement de châssis. C'est une "
                  "cause de processus que vous pouvez corriger. Mais une chaîne n'est pas une preuve. "
                  "Karthik a enfoncé des modules en biais, et le défaut est apparu à chaque fois.",
    },
    {
        "key": "p12", "num": 12, "title": "Contre-mesures et confinement",
        "points": [("Casser la cause vérifiée", "cassent la cause"),
                   ("Juger : effet, risque, coût, durabilité", "Jugez chacune"),
                   ("Confiner maintenant, corriger pour de bon", "En attendant, confinez")],
        "example": "Guide d'insertion · contrôle du loquet · revue des instructions à chaque changement de "
                   "châssis",
        "example_cue": "L'équipe de Karthik en a choisi trois",
        "script": "Choisissez maintenant des contre-mesures qui cassent la cause. L'équipe de Karthik en a "
                  "choisi trois. Un guide d'insertion qui garde le module droit. Un contrôle du loquet "
                  "avant que le serveur quitte le poste. Et une revue des instructions de travail à chaque "
                  "changement de châssis. Jugez chacune selon son effet, son risque, son coût et sa "
                  "facilité à durer. En attendant, confinez. Les serveurs suspects ont été bloqués et "
                  "revérifiés. Le confinement protège votre client, mais ce n'est pas la solution.",
    },
    {
        "key": "p13", "num": 13, "title": "Plan et responsables",
        "points": [("Un responsable, une échéance, une preuve", "Votre plan nomme donc un responsable"),
                   ("Semaines 1–2 : confirmer la cause, pilote", "L'ingénierie de test confirme"),
                   ("Semaines 3–4 : mettre à jour le SOP, former chaque équipe", "La maintenance et la production"),
                   ("Semaines 5–6 : vérifier les résultats", "La qualité vérifie")],
        "example": "Bloqué ? Escaladez avec le blocage exact et la décision dont vous avez besoin.",
        "example_cue": "Bloqué ?",
        "script": "Une action sans responsable se fait rarement. Votre plan nomme donc un responsable, une "
                  "échéance et la preuve pour chaque action. L'ingénierie de test confirme la cause en "
                  "semaine une. L'ingénierie procédés pilote le guide d'insertion en semaine deux. La "
                  "maintenance et la production mettent à jour le SOP et forment chaque équipe pour la "
                  "semaine quatre. La qualité vérifie les résultats en semaines cinq et six. Bloqué ? "
                  "Escaladez avec le blocage exact. Alors, comment savoir que ça a marché ?",
    },
    {
        "key": "p14", "num": 14, "title": "Pilote et vérification",
        "points": [("Même mix de produits que la référence", "avec le même mix de produits"),
                   ("De 4,8 % à 1,6 % : cible atteinte", "Les échecs sont tombés"),
                   ("Garde-fous vérifiés aussi", "il a aussi vérifié les garde-fous"),
                   ("Raté ? Revoyez la cause, pas la cible", "Si ça n'avait pas")],
        "example": "Pilote : 48 échecs sur 3 000 serveurs = 1,6 %.",
        "example_cue": "Karthik l'a mené",
        "script": "Un pilote est une expérience, pas une annonce. Karthik l'a mené sur trois mille "
                  "serveurs, avec le même mix de produits que la référence. Les échecs sont tombés à un "
                  "virgule six pour cent. Cible atteinte. Mais il a aussi vérifié les garde-fous. Le temps "
                  "de test est resté stable, et aucun autre mode de défaillance n'a augmenté. Est-ce que ça "
                  "a tenu sur chaque équipe ? Oui. Si ça n'avait pas été le cas, vous reverriez la cause, "
                  "sans jamais changer la cible en douce.",
    },
    {
        "key": "p15", "num": 15, "title": "Pérenniser et votre A3 en 30 jours",
        "points": [("Mettre à jour le SOP, la check-list, la formation", "Mettez à jour le SOP"),
                   ("Contrôle en début d'équipe ; revue à 30/60/90 jours", "Ajoutez un contrôle du loquet"),
                   ("Ne dupliquez que sur des lignes vraiment comparables", "Dupliquez-le sur d'autres lignes"),
                   ("Votre propre A3 en 30 jours", "Maintenant, à vous")],
        "example": "Jours 1–5 : un vrai problème, la référence au Gemba. Jour 20 : causes et pilote. Jour 30 "
                   ": présentez votre A3.",
        "example_cue": "Pendant les cinq premiers jours",
        "script": "Enfin, faites de la nouvelle méthode la méthode normale. Mettez à jour le SOP, la "
                  "check-list et la formation. Ajoutez un contrôle du loquet à chaque début d'équipe, et "
                  "revoyez la tendance à trente, soixante et quatre-vingt-dix jours. Dupliquez-le sur "
                  "d'autres lignes seulement après avoir vérifié qu'elles sont vraiment comparables. "
                  "Maintenant, à vous. Pendant les cinq premiers jours, choisissez un vrai problème et "
                  "vérifiez sa référence au Gemba. Au jour vingt, vérifiez les causes et lancez un pilote. "
                  "Au jour trente, présentez votre A3.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Format de papier A3", "icon": "label", "with": 0},
        {"label": "L'histoire sur une page", "icon": "clipboard", "with": 1},
        {"label": "Causes, tests, résultats", "icon": "search", "with": 2},
        {"label": "Construit en équipe", "icon": "person", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "« Les opérateurs sont négligents »", "sub": "Le premier rapport de Karthik", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Une feuille A3 vierge", "sub": "La réponse de son responsable", "icon": "clipboard", "tone": "good", "with": "example"}]}},
    "p02": {"type": "versus", "items": [
        {"label": "Reproche", "sub": "« Les opérateurs sont négligents »", "icon": "person", "tone": "bad", "with": "example"},
        {"label": "Écart", "sub": "Échecs de démarrage jusqu'à 4,8 %", "icon": "chartUp", "tone": "good", "with": "example"}]},
    "p03": {"type": "icons", "items": [
        {"label": "Défauts répétés", "icon": "warning", "with": 0},
        {"label": "Arrêts, ruptures", "icon": "clock", "with": 0},
        {"label": "Transverse", "icon": "person", "with": 1}],
        "then": {"type": "flow", "with": 2, "items": [
            {"label": "Plan", "icon": "clipboard", "with": 2},
            {"label": "Do", "sub": "Petit pilote", "icon": "wrench", "with": 2},
            {"label": "Check", "sub": "Par rapport à la cible", "icon": "search", "with": 2},
            {"label": "Act", "sub": "Standardiser", "icon": "check", "tone": "good", "with": 2}]}},
    "p04": {"type": "doc", "items": [
        {"label": "Contexte · pourquoi maintenant", "icon": "label", "with": 0},
        {"label": "Situation actuelle · cible", "icon": "chartUp", "with": 0},
        {"label": "Cause racine · pourquoi l'écart", "icon": "search", "with": 1},
        {"label": "Contre-mesures · plan", "icon": "wrench", "with": 2},
        {"label": "Suivi · ça a marché ?", "icon": "check", "with": 2}]},
    "p05": {"type": "versus", "items": [
        {"label": "Faible", "sub": "« La qualité est mauvaise partout »", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Précis", "sub": "Ligne 2 · le mois dernier · 4,8 % contre 1,5 %", "icon": "check", "tone": "good", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Gemba", "sub": "Lieu réel", "icon": "walk", "with": 0},
        {"label": "Genbutsu", "sub": "Choses réelles", "icon": "chip", "with": 1},
        {"label": "Genjitsu", "sub": "Faits réels", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 7, "suffix": " / 10", "icon": "chip", "label": "serveurs défaillants sur le banc",
                 "unit": "un module mémoire légèrement soulevé", "with": "example"}},
    "p07": {"type": "flow", "items": [
        {"label": "Définition claire", "icon": "clipboard", "with": 0},
        {"label": "Serveurs uniques", "icon": "count", "with": 1},
        {"label": "Horodatages, numéros de série", "icon": "barcode", "with": 2},
        {"label": "Le journal correspond au MES", "icon": "check", "tone": "good", "with": 3}]},
    "p08": {"type": "bars", "label": "", "note": "Échecs au premier test de démarrage pour 1 000 serveurs, par semaine", "items": [
        {"label": "W1", "value": 41, "with": 0},
        {"label": "W2", "value": 46, "with": 0},
        {"label": "W3", "value": 50, "with": 0},
        {"label": "W4", "value": 55, "tone": "bad", "with": 0}],
        "then": {"type": "bars", "label": "", "note": "Modes de défaillance : 576 échecs au premier passage", "with": 2, "items": [
            {"label": "Mémoire", "value": 288, "tone": "bad", "with": 2},
            {"label": "Ventilateur", "value": 144, "with": 2},
            {"label": "Réseau", "value": 86, "with": 2},
            {"label": "Autre", "value": 58, "with": 2}]}},
    "p09": {"type": "icons", "items": [
        {"label": "Cible", "sub": "≤ 2 % en 6 semaines", "icon": "pin", "tone": "good", "with": 0},
        {"label": "Garde-fous", "sub": "Temps de test, retests, fuites", "icon": "shield", "with": 1}],
        "then": {"type": "versus", "with": 2, "items": [
            {"label": "Hors périmètre", "sub": "Assouplir les limites de test", "icon": "cross", "tone": "bad", "with": 2},
            {"label": "Dans le périmètre", "sub": "Échecs mémoire, ligne 2", "icon": "check", "tone": "good", "with": 2}]}},
    "p10": {"type": "icons", "items": [
        {"label": "Main-d'œuvre", "icon": "person", "with": 1},
        {"label": "Machine", "icon": "gear", "with": 1},
        {"label": "Méthode", "icon": "clipboard", "with": 1},
        {"label": "Matière", "icon": "box", "with": 1},
        {"label": "Mesure", "icon": "scale", "with": 1},
        {"label": "Milieu", "icon": "wave", "with": 1}]},
    "p11": {"type": "steps", "items": [
        {"label": "Module mal enfoncé", "with": 0},
        {"label": "Loquet fermé trop tôt", "with": 0},
        {"label": "Moins de place dans le nouveau châssis", "with": 0},
        {"label": "Instructions non revues", "with": "example"}],
        "then": {"type": "stat", "value": 100, "suffix": "%", "icon": "test", "label": "défaut reproduit",
                 "unit": "en enfonçant les modules en biais", "with": 2}},
    "p12": {"type": "flow", "items": [
        {"label": "Guide d'insertion", "icon": "shape", "with": "example"},
        {"label": "Contrôle du loquet", "icon": "sensor", "with": "example"},
        {"label": "Revue à chaque changement de châssis", "icon": "clipboard", "tone": "good", "with": "example"}],
        "then": {"type": "flow", "with": 2, "items": [
            {"label": "Confinement", "sub": "Protège le client maintenant", "icon": "lock", "with": 2},
            {"label": "Contre-mesure", "sub": "Supprime la cause pour de bon", "icon": "key", "tone": "good", "with": 2}]}},
    "p13": {"type": "timeline", "items": [
        {"label": "Confirmer la cause, pilote", "sub": "Semaines 1–2", "icon": "test", "with": 1},
        {"label": "Mettre à jour le SOP, former", "sub": "Semaines 3–4", "icon": "clipboard", "with": 2},
        {"label": "Vérifier les résultats", "sub": "Semaines 5–6", "icon": "check", "tone": "good", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Référence", "value": 4.8}, "after": {"label": "Pilote", "value": 1.6},
            "decimals": 1, "suffix": "%", "unit": "serveurs échouant au premier test de démarrage",
            "note": "Cible ≤ 2 % : atteinte", "with": 1},
    "p15": {"type": "timeline", "items": [
        {"label": "Un vrai problème, la référence", "sub": "Jours 1–5", "icon": "walk", "with": "example"},
        {"label": "Causes et pilote", "sub": "Au jour 20", "icon": "search", "with": "example"},
        {"label": "Présentez votre A3", "sub": "Jour 30", "icon": "clipboard", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Quel est le meilleur énoncé de problème pour un A3 ?",
        "options": ["Les opérateurs sont négligents en posant la mémoire",
                    "Les échecs au premier test de démarrage de la ligne 2 étaient en moyenne de 4,8 % contre "
                    "1,5 % sur 4 semaines",
                    "Il nous faut deux contrôleurs de plus au test"],
        "correct": 1,
        "explanation": "Il nomme la ligne, la période et la mesure, avec une référence, et n'affirme aucune "
                       "cause. Les autres sont un reproche et une solution.",
        "q_script": "Vérification rapide. Lequel de ces énoncés est le meilleur énoncé de problème pour un A3 "
                    "? Prenez quelques secondes.",
        "a_script": "C'est le deuxième. Il nomme la ligne, la période et la mesure, et n'affirme aucune "
                    "cause. Les autres sont un reproche et une solution.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Le pilote de Karthik atteint la cible, mais le taux de retest double. Que doit-il faire "
                    "?",
        "options": ["Standardiser quand même : la cible est atteinte",
                    "Étudier le garde-fou avant de standardiser",
                    "Monter la cible à 3 % par sécurité"],
        "correct": 1,
        "explanation": "Un garde-fou a bougé, donc le changement cache peut-être des échecs dans les retests au "
                       "lieu de les supprimer. Comprenez-le avant de standardiser.",
        "q_script": "Encore une, et cette fois c'est un scénario. Le pilote de Karthik atteint la cible, mais "
                    "le taux de retest double. Que doit-il faire ? Réfléchissez.",
        "a_script": "Étudiez avant de standardiser. Un garde-fou a bougé, donc la solution cache peut-être "
                    "des échecs, au lieu de les supprimer.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
