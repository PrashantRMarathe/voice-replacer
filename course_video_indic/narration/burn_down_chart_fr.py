"""burn_down_chart in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh burn_down_chart_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "bd_fr"
NAME = "burn_down_chart_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Cycle Time Study": "saïkeul taïme steudi",
    "Burn Down Chart": "beurne daoune tchart",
    "Kaizen": "Kaïzène",
    "RF": "erre effe",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Le mois dernier, le camion est parti avec quatre-vingts routeurs en moins. Personne ne "
    "l'a vu venir, jusqu'au vendredi après-midi. Ça vous dit quelque chose ? Dans cette "
    "leçon, vous allez découvrir le Burn Down Chart. Vous verrez comment suivre le travail "
    "restant. Vous repérerez un retard le jour deux, pas le jour cinq, et vous rattraperez à "
    "temps. Nous suivrons Sneha, superviseure de production sur une ligne de routeurs Wi-Fi, "
    "qui fait en sorte que cela n'arrive plus jamais."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Tracez d'abord la ligne idéale, et ne la redessinez "
    "jamais pour paraître meilleur. Ne comptez que le travail vraiment terminé et bon. Et "
    "quand la ligne passe au-dessus de l'idéal, agissez le jour même, avec un responsable. "
    "Voici votre action pour cette semaine. Choisissez un travail avec une échéance, et "
    "tracez son graphique de travail restant avant l'équipe de demain. Bravo d'avoir terminé "
    "cette leçon. Ensuite, vous découvrirez le Cycle Time Study."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce que montre le graphique",
        "points": [("Travail restant face au temps disponible", "combien de travail il reste"),
                   ("Verticalement : travail restant. Horizontalement : temps", "L'axe vertical"),
                   ("La ligne descend vers zéro", "la ligne doit descendre")],
        "example": "Le graphique de Sneha : un tableau blanc à côté de la ligne, visible par chaque équipe.",
        "example_cue": "Sneha trace le sien",
        "script": "Voici l'idée. Un graphique de travail restant montre combien de travail il reste, face "
                  "au temps dont vous disposez. L'axe vertical est le travail restant. L'axe horizontal est "
                  "le temps. À mesure que votre équipe termine du travail, la ligne doit descendre vers "
                  "zéro. C'est tout. Simple, mais puissant. Sneha trace le sien sur un tableau blanc à côté "
                  "de la ligne, pour que chaque équipe le voie. Alors, pourquoi le Lean aime-t-il un "
                  "graphique aussi simple ?",
    },
    {
        "key": "p02", "num": 2, "title": "Pourquoi le Lean l'utilise",
        "points": [("Une cible devient un chemin visible", "transforme une cible en chemin"),
                   ("Voir un écart tant qu'il est petit", "Vous voyez un écart"),
                   ("Se concentrer sur la contrainte", "concentrer vos équipes")],
        "example": "Le mois dernier : seulement une échéance. L'écart est apparu le vendredi après-midi.",
        "example_cue": "Le mois dernier, Sneha",
        "script": "Parce qu'il transforme une cible en chemin que vous pouvez voir. Une échéance seule ne "
                  "vous dit rien, jusqu'à ce qu'elle soit manquée. Ce graphique vous montre chaque jour si "
                  "vous êtes dans les temps. Vous voyez un écart tant qu'il est encore petit. Et vous "
                  "pouvez concentrer vos équipes sur la seule contrainte qui empêche de finir. Le mois "
                  "dernier, Sneha n'avait qu'une échéance. Elle a trouvé l'écart le vendredi. Que "
                  "vaudraient pour vous deux jours de plus ?",
    },
    {
        "key": "p03", "num": 3, "title": "À quoi il sert",
        "points": [("Travail restant visible par tous", "rend le travail restant visible"),
                   ("Avancement réel face au rythme nécessaire", "Il compare l'avancement réel"),
                   ("Détecter les retards tôt", "Il détecte les retards tôt"),
                   ("Rattrapage appuyé sur des faits", "appuie vos actions de rattrapage")],
        "example": "L'objectif : chaque unité prévue atteint zéro à l'échéance.",
        "example_cue": "L'objectif est simple",
        "script": "Alors, que fait vraiment ce graphique pour vous ? Il rend le travail restant visible par "
                  "toute l'équipe, pas seulement par le planificateur. Il compare l'avancement réel au "
                  "rythme dont vous avez besoin. Il détecte les retards tôt, quand rattraper coûte encore "
                  "peu. Et il appuie vos actions de rattrapage sur des faits, pas sur des impressions. "
                  "L'objectif est simple. Chaque unité prévue atteint zéro à l'échéance. Regardons ce qu'il "
                  "y a sur le graphique.",
    },
    {
        "key": "p04", "num": 4, "title": "Les cinq éléments",
        "points": [("Axes : travail restant, temps", "L'axe vertical"),
                   ("Ligne idéale : le rythme nécessaire", "La ligne idéale"),
                   ("Ligne réelle : ce qui s'est vraiment passé", "La ligne réelle"),
                   ("Écart : réel moins idéal", "l'écart est")],
        "example": "Sneha suit les routeurs qui restent à terminer, jour après jour.",
        "example_cue": "Sneha suit les routeurs",
        "script": "Ce graphique a cinq parties. L'axe vertical est le travail restant, en unités, défauts, "
                  "actions ou heures. L'axe horizontal est le temps, en équipes, jours ou semaines. La "
                  "ligne idéale est le rythme dont vous avez besoin. La ligne réelle est ce qui s'est "
                  "vraiment passé. Et l'écart est la distance entre les deux. Sneha suit les routeurs qui "
                  "restent à terminer, jour après jour. Quelle unité compteriez-vous sur votre ligne ?",
    },
    {
        "key": "p05", "num": 5, "title": "Le défi de Sneha",
        "points": [("1 000 routeurs en cours de fabrication", "Mille routeurs"),
                   ("5 jours ouvrés avant le camion", "Le camion part"),
                   ("Restant = prévu − terminé", "Le travail restant est égal")],
        "example": "Jour 0 : rien de terminé, 1 000 routeurs restants.",
        "example_cue": "Au jour zéro",
        "script": "Voici le défi de Sneha ce mois-ci. Mille routeurs sont bloqués en cours de fabrication. "
                  "Il leur faut encore le test final et l'emballage, et seules les bonnes unités comptent. "
                  "Le camion part dans cinq jours ouvrés. Le calcul commence simplement. Le travail restant "
                  "est égal au travail total prévu, moins ce que vous avez déjà terminé. Au jour zéro, rien "
                  "n'est fait, donc les mille restent. Devinez-vous le rythme dont elle a besoin chaque "
                  "jour ?",
    },
    {
        "key": "p06", "num": 6, "title": "Le rythme idéal",
        "points": [("Rythme = travail total ÷ périodes", "travail total divisé"),
                   ("1 000 ÷ 5 = 200 par jour", "Deux cents par jour"),
                   ("Tracez-la d'abord, ne la redessinez jamais", "Tracez-la avant")],
        "example": "Ligne idéale : 1 000 → 800 → 600 → 400 → 200 → 0",
        "example_cue": "Sa ligne idéale descend donc",
        "script": "Le rythme idéal est le travail total divisé par le nombre de périodes dont vous "
                  "disposez. Pour Sneha, ce sont mille routeurs en cinq jours. Deux cents par jour. Sa "
                  "ligne idéale descend donc à zéro en cinq paliers égaux. Cette ligne droite est son plan. "
                  "Tracez-la avant le début du travail, et ne la redessinez jamais pour paraître meilleur. "
                  "Si vous déplacez le plan, vous cachez l'écart. Alors, que s'est-il passé après deux "
                  "jours ?",
    },
    {
        "key": "p07", "num": 7, "title": "Jour deux : trouver l'écart",
        "points": [("Terminés : 320", "Son équipe a terminé"),
                   ("Restants : 680. Idéal : 600", "Il en reste donc six cent quatre-vingts"),
                   ("Écart : 80 de retard sur le plan", "L'écart est"),
                   ("Trois jours pour rattraper, sans toucher à la qualité", "Elle a trois jours")],
        "example": "Repéré le mardi, pas le vendredi.",
        "example_cue": "elle le sait le mardi",
        "script": "À la fin du jour deux, Sneha met à jour son graphique. Son équipe a terminé trois cent "
                  "vingt routeurs. Il en reste donc six cent quatre-vingts. Mais sa ligne idéale dit qu'il "
                  "devrait en rester six cents. L'écart est de quatre-vingts routeurs de retard sur le "
                  "plan. Est-ce une catastrophe ? Non, mais c'est un signal. Elle a trois jours pour le "
                  "rattraper, sans rogner sur la qualité. Et elle le sait le mardi, pas le vendredi.",
    },
    {
        "key": "p08", "num": 8, "title": "Lire les lignes",
        "points": [("Au-dessus de l'idéal : en retard. Trouvez la contrainte", "ligne réelle est au-dessus"),
                   ("En dessous de l'idéal : en avance. Confirmez la qualité", "Si elle est en dessous"),
                   ("En avance avec de mauvaises unités, ce n'est pas être en avance", "Être en avance avec de mauvaises unités")],
        "example": "La ligne de Sneha est au-dessus de l'idéal. Qu'est-ce qui empêche les routeurs d'être "
                   "terminés ?",
        "example_cue": "La ligne de Sneha était au-dessus",
        "script": "Alors, comment lire les lignes ? Si la ligne réelle est au-dessus de l'idéal, il reste "
                  "plus de travail que prévu. Trouvez la contrainte, et attribuez une action de rattrapage. "
                  "Si elle est en dessous, vous êtes en avance. Très bien, mais confirmez la qualité, et "
                  "maintenez le rythme. Être en avance avec de mauvaises unités, ce n'est pas être en "
                  "avance. La ligne de Sneha était au-dessus. Sa question était donc simple. Qu'est-ce qui "
                  "empêche les routeurs d'être terminés ? Que vérifieriez-vous en premier ?",
    },
    {
        "key": "p09", "num": 9, "title": "Lignes plates et arrivée à zéro",
        "points": [("Ligne plate : rien n'est clos", "Une ligne plate signifie"),
                   ("Vérifiez arrêt, responsable, données", "Vérifiez donc s'il y a un arrêt"),
                   ("À zéro : vérifiez, puis clôturez", "quand la ligne atteint zéro")],
        "example": "Mercredi : la ligne de Sneha est restée plate pendant toute une équipe.",
        "example_cue": "Mercredi",
        "script": "Deux autres tendances comptent. Une ligne plate signifie que rien n'a été clos. Soit le "
                  "travail s'est arrêté, soit personne n'a mis à jour le graphique. Parfois les deux. "
                  "Vérifiez donc s'il y a un arrêt, vérifiez le responsable, et vérifiez les données. Et "
                  "quand la ligne atteint zéro ? Ne vous contentez pas de fêter. Vérifiez que chaque unité "
                  "respecte les critères d'acceptation, puis clôturez officiellement. Mercredi, la ligne de "
                  "Sneha est restée plate pendant toute une équipe. Devinez-vous pourquoi ?",
    },
    {
        "key": "p10", "num": 10, "title": "La revue quotidienne",
        "points": [("Mettre à jour et comparer", "Mettez à jour, en enregistrant"),
                   ("Expliquer la cause principale", "Expliquez la cause principale"),
                   ("Agir : un responsable et une heure limite", "Agissez, avec un responsable"),
                   ("Confirmer à la mise à jour suivante", "Puis confirmez")],
        "example": "Sneha mène la revue en 10 minutes, au début de chaque équipe.",
        "example_cue": "Sneha la mène",
        "script": "Avant de le découvrir, voici l'habitude qui le détecte. Un graphique n'aide que si vous "
                  "le revoyez de la même façon chaque jour. Mettez à jour, en enregistrant ce qui est "
                  "terminé et en recalculant ce qui reste. Comparez le réel à l'idéal. Expliquez la cause "
                  "principale de tout mauvais écart. Agissez, avec un responsable et une heure limite. Puis "
                  "confirmez, à la mise à jour suivante, que la ligne redescend. Sneha la mène en dix "
                  "minutes, au début de chaque équipe. Et vous, le pourriez-vous ?",
    },
    {
        "key": "p11", "num": 11, "title": "Le rattrapage de Sneha",
        "points": [("Contrainte : un testeur RF en panne", "Un poste de test RF"),
                   ("Deuxième testeur, personnel prioritaire", "Un technicien a mis"),
                   ("Un seul responsable met à jour le graphique", "Elle a nommé un responsable")],
        "example": "Vendredi : zéro routeur restant, quelques heures avant le camion.",
        "example_cue": "Vendredi",
        "script": "Voici ce que signifiait la ligne plate du mercredi. Un poste de test RF était arrêté "
                  "pour étalonnage. Les routeurs s'entassaient devant lui. Et personne ne mettait à jour le "
                  "graphique, parce que personne n'avait été désigné pour le faire. Sneha a réglé les deux. "
                  "Un technicien a mis en service un deuxième testeur, et le test a reçu du personnel en "
                  "priorité. Elle a nommé un responsable pour mettre à jour le graphique à heure fixe. "
                  "Vendredi, la ligne a touché zéro, quelques heures avant le camion. Où d'autre "
                  "pourriez-vous l'utiliser ?",
    },
    {
        "key": "p12", "num": 12, "title": "Où l'utiliser",
        "points": [("Un début clair, une fin claire, une échéance", "chaque fois que le travail a"),
                   ("Production : en-cours, rattrapage", "Videz l'en-cours"),
                   ("Qualité : défauts critiques à zéro", "Clôturez chaque défaut critique"),
                   ("Actions de maintenance et de Kaizen", "Terminez les actions de maintenance")],
        "example": "L'équipe qualité de Sneha ramène maintenant les défauts ouverts à zéro avant "
                   "l'expédition.",
        "example_cue": "L'équipe qualité de Sneha",
        "script": "Ce graphique ne sert pas qu'à la production. Utilisez-le chaque fois que le travail a "
                  "une quantité de départ claire, une fin claire et une échéance. Videz l'en-cours avant un "
                  "changement de série. Rattrapez un manque avant la limite d'expédition. Clôturez chaque "
                  "défaut critique avant l'expédition. Terminez les actions de maintenance ouvertes, ou les "
                  "tâches de Kaizen, avant une revue. L'équipe qualité de Sneha suit maintenant aussi les "
                  "défauts ouverts jusqu'à zéro. Qu'est-ce qui a une échéance dans votre atelier cette "
                  "semaine ?",
    },
    {
        "key": "p13", "num": 13, "title": "Des données honnêtes",
        "points": [("Une unité, une quantité de départ figée", "Utilisez une seule unité"),
                   ("Définir « terminé » avant de commencer", "Définissez exactement quand"),
                   ("Ne compter que la bonne production", "ne comptez que la production")],
        "example": "Routeurs en attente de retest : pas comptés comme terminés.",
        "example_cue": "Jeudi",
        "script": "Un graphique n'est honnête que si ses données le sont. Utilisez une seule unité de "
                  "mesure du début à la fin. Figez la quantité de départ, sauf si un changement de "
                  "périmètre est approuvé. Définissez exactement quand quelque chose compte comme terminé. "
                  "Et ne comptez que la production conforme. Jeudi, l'équipe de Sneha voulait compter les "
                  "routeurs en attente de retest. Elle a dit non. À moitié fait n'est pas fait, et une "
                  "unité en échec non plus. Les auriez-vous comptés ?",
    },
    {
        "key": "p14", "num": 14, "title": "Erreurs fréquentes",
        "points": [("Changer la quantité de départ", "Changer la quantité de départ"),
                   ("Mises à jour tardives ou irrégulières", "Les mises à jour tardives"),
                   ("Compter des unités partielles ou rejetées", "Compter du travail partiel"),
                   ("Un graphique sans actions", "Un graphique sans actions")],
        "example": "Sneha note les changements de périmètre approuvés dans un encadré séparé à côté de son "
                   "graphique.",
        "example_cue": "Sneha note les changements",
        "script": "Attention à quelques erreurs fréquentes. Changer la quantité de départ cache l'écart "
                  "d'origine. Les mises à jour tardives vous font réagir quand le retard a déjà grandi. "
                  "Compter du travail partiel, ou des unités rejetées, fait paraître l'avancement meilleur "
                  "qu'il n'est. Et un graphique sans actions n'est qu'un rapport. Sneha note les "
                  "changements de périmètre approuvés dans un encadré séparé à côté de son graphique. "
                  "L'écart d'origine reste visible. Quelle erreur avez-vous déjà vue ?",
    },
    {
        "key": "p15", "num": 15, "title": "Forces, limites et check-list",
        "points": [("Simple, rapide, une alerte précoce", "Ce graphique est simple"),
                   ("Ne trouve pas la cause racine à lui seul", "il n'explique pas"),
                   ("Définir, confirmer, calculer, nommer un responsable", "voici votre check-list"),
                   ("Mettre à jour, agir, clôturer seulement à zéro", "Puis mettez à jour")],
        "example": "Sneha affiche cette check-list à côté de chaque nouveau graphique.",
        "example_cue": "Sneha affiche cette check-list",
        "script": "Alors, quel est le verdict ? Ce graphique est simple, rapide à lire, et il vous alerte "
                  "avant l'échéance. Mais il n'explique pas la cause racine à lui seul. Et il dépend de "
                  "mises à jour honnêtes et à l'heure. Alors voici votre check-list. Définissez le travail, "
                  "et ce que terminé veut dire. Confirmez la quantité de départ et la date. Calculez le "
                  "rythme idéal, et nommez un responsable. Puis mettez à jour, agissez, et ne clôturez qu'à "
                  "zéro. Sneha affiche cette check-list à côté de chaque nouveau graphique.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Travail restant", "icon": "stack", "with": 0},
        {"label": "Temps disponible", "icon": "clock", "with": 1},
        {"label": "Descend à zéro", "icon": "chartDown", "tone": "good", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Seulement une échéance", "sub": "Écart trouvé le vendredi", "icon": "calendar", "tone": "bad", "with": "example"},
        {"label": "Un graphique de travail restant", "sub": "Écart vu tant qu'il est petit", "icon": "chartDown", "tone": "good", "with": 1}]},
    "p03": {"type": "icons", "items": [
        {"label": "Visible par tous", "icon": "search", "with": 0},
        {"label": "Réel face au rythme", "icon": "scale", "with": 1},
        {"label": "Alerte précoce", "icon": "warning", "with": 2},
        {"label": "Des faits, pas des impressions", "icon": "clipboard", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Travail restant", "sub": "Axe vertical", "icon": "stack", "with": 0},
        {"label": "Temps", "sub": "Axe horizontal", "icon": "calendar", "with": 0},
        {"label": "Ligne idéale", "icon": "chartDown", "with": 1},
        {"label": "Ligne réelle", "icon": "pin", "with": 2},
        {"label": "Écart", "icon": "scale", "tone": "bad", "with": 3}]},
    "p05": {"type": "stat", "value": 1000, "icon": "box", "label": "routeurs en cours de fabrication",
            "unit": "5 jours ouvrés avant le camion", "with": 0},
    "p06": {"type": "bars", "label": "", "note": "Ligne idéale : 200 routeurs de moins chaque jour", "with": "example", "items": [
        {"label": "Jour 0", "value": 1000, "with": "example"},
        {"label": "Jour 1", "value": 800, "with": "example"},
        {"label": "Jour 2", "value": 600, "with": "example"},
        {"label": "Jour 3", "value": 400, "with": "example"},
        {"label": "Jour 4", "value": 200, "with": "example"},
        {"label": "Jour 5", "value": 0, "tone": "good", "with": "example"}]},
    "p07": {"type": "bars", "label": "", "note": "Routeurs restants, fin du jour 2 : 80 de retard sur le plan", "items": [
        {"label": "Idéal", "value": 600, "tone": "good", "with": 1},
        {"label": "Réel", "value": 680, "tone": "bad", "with": 1}]},
    "p08": {"type": "versus", "items": [
        {"label": "Au-dessus de l'idéal", "sub": "En retard : trouvez la contrainte", "icon": "chartUp", "tone": "bad", "with": 0},
        {"label": "En dessous de l'idéal", "sub": "En avance : confirmez la qualité", "icon": "chartDown", "tone": "good", "with": 1}]},
    "p09": {"type": "flow", "items": [
        {"label": "Ligne plate", "sub": "Rien de clos", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Arrêt ? Responsable ? Données ?", "icon": "search", "with": 1},
        {"label": "À zéro : vérifier, clôturer", "icon": "check", "tone": "good", "with": 2}]},
    "p10": {"type": "steps", "items": [
        {"label": "Mettre à jour", "with": 0}, {"label": "Comparer", "with": 0},
        {"label": "Expliquer", "with": 1}, {"label": "Agir", "with": 2},
        {"label": "Confirmer", "with": 3}]},
    "p11": {"type": "flow", "items": [
        {"label": "Testeur RF en panne", "icon": "test", "tone": "bad", "with": 0},
        {"label": "Deuxième testeur en service", "icon": "wrench", "with": 1},
        {"label": "Un responsable du graphique", "icon": "person", "with": 2}],
        "then": {"type": "stat", "value": 0, "icon": "check", "label": "routeurs restants le vendredi",
                 "unit": "quelques heures avant le camion", "with": "example"}},
    "p12": {"type": "icons", "items": [
        {"label": "En-cours", "icon": "box", "with": 1},
        {"label": "Rattrapage d'un manque", "icon": "chartUp", "with": 1},
        {"label": "Défauts critiques", "icon": "warning", "with": 2},
        {"label": "Maintenance, Kaizen", "icon": "wrench", "with": 3}]},
    "p13": {"type": "icons", "items": [
        {"label": "Une unité, départ figé", "icon": "lock", "with": 0},
        {"label": "« Terminé » défini", "icon": "clipboard", "with": 1},
        {"label": "Seulement la bonne production", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "En attente de retest", "sub": "Pas terminé", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Réussi et emballé", "sub": "Compte", "icon": "check", "tone": "good", "with": "example"}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Quantité de départ modifiée", "icon": "stack", "tone": "bad", "with": 0},
        {"label": "Mises à jour tardives", "icon": "clock", "tone": "bad", "with": 1},
        {"label": "Partiel ou rejeté", "icon": "trash", "tone": "bad", "with": 2},
        {"label": "Pas d'actions", "icon": "cross", "tone": "bad", "with": 3}]},
    "p15": {"type": "doc", "items": [
        {"label": "Définir le travail et « terminé »", "icon": "clipboard", "with": 2},
        {"label": "Confirmer la quantité de départ et la date", "icon": "calendar", "with": 2},
        {"label": "Rythme idéal, un responsable", "icon": "person", "with": 2},
        {"label": "Mettre à jour, agir, clôturer seulement à zéro", "icon": "check", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "800 unités doivent être terminées en 4 jours. Après le jour 2, 340 sont faites. Où en "
                    "est l'équipe ?",
        "options": ["60 unités d'avance sur le plan", "60 unités de retard sur le plan", "Exactement dans le plan"],
        "correct": 1,
        "explanation": "Restant idéal au jour 2 = 800 − 2 × 200 = 400. Restant réel = 800 − 340 = 460. 460 − 400 "
                       "= 60 de retard sur le plan.",
        "q_script": "Vérification rapide. Huit cents unités doivent être terminées en quatre jours. Après le "
                    "jour deux, trois cent quarante sont faites. Où en est l'équipe ? Prenez quelques "
                    "secondes.",
        "a_script": "Elle a soixante unités de retard. Il devrait en rester quatre cents, mais il en reste "
                    "encore quatre cent soixante. La ligne réelle est au-dessus de l'idéal.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un graphique des défauts restants est plat depuis deux jours. Que doit vérifier l'équipe "
                    "en premier ?",
        "options": ["Rien : une ligne plate veut dire que tout est stable",
                    "Si le travail s'est arrêté, qui en est responsable, et si les données ont été mises à "
                    "jour",
                    "Redessiner la ligne idéale pour coller à la réalité"],
        "correct": 1,
        "explanation": "Une ligne plate signifie que rien n'a été clos. Vérifiez s'il y a un arrêt, le "
                       "responsable et les données. Redessiner la ligne idéale ne fait que cacher l'écart.",
        "q_script": "Encore une, et cette fois c'est un scénario. Un graphique des défauts restants est plat "
                    "depuis deux jours. Que doit vérifier l'équipe en premier ? Réfléchissez.",
        "a_script": "Vérifiez si le travail s'est arrêté, qui en est responsable, et si quelqu'un a mis à "
                    "jour les données. Redessiner la ligne idéale ne ferait que cacher l'écart.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
