"""takt_time in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh takt_time_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "tt_fr"
NAME = "takt_time_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Uniform Production": "iounifôrme prodeuction",
    "Yamazumi": "Yamazoumi",
    "Heijunka": "Héïdjounka",
    "Kanban": "Kanne-banne",
    "SMED": "smède",
    "TAKT": "takte",
    "UPPH": "u pé pé ache",
    "UPH": "u pé ache",
    "WIP": "double vé i pé",
    "SOP": "esse o pé",
    "A": "a",
    "B": "bé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Chaque machine de la ligne de caméras de Rohan semblait occupée. Les postes en amont "
    "allaient à toute vitesse. Pourtant, l'expédition ratait sans cesse le camion. Comment "
    "une ligne occupée peut-elle être en retard ? Dans cette leçon, vous allez découvrir le "
    "temps TAKT, le battement fixé par votre client. Vous verrez comment le calculer "
    "correctement, et l'utiliser pour équilibrer, staffer et piloter votre ligne. Nous "
    "suivrons Rohan, ingénieur planification dans une usine de caméras."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Le TAKT est le temps net disponible divisé par la demande "
    "client. C'est le rythme nécessaire, pas le temps que prend réellement un poste. Et "
    "planifiez avec les pertes réelles, comme les arrêts et le rendement, pas avec la vitesse "
    "théorique. Voici votre action pour cette semaine. Calculez le TAKT d'une de vos lignes, "
    "et comparez-le à votre poste le plus lent. Bravo d'avoir terminé cette leçon. Ensuite, "
    "vous découvrirez Uniform Production."
)

# One story thread: Rohan's network-camera plant. 7,200 good cameras/day, 1,200 net
# minutes/day over three shifts -> TAKT 10 s; final test 18 s per unit is the constraint.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le temps TAKT",
        "points": [("Takt : en allemand, la mesure, le rythme", "Le TAKT vient"),
                   ("Le rythme qui répond à la demande client", "C'est le rythme"),
                   ("TAKT = temps net disponible ÷ demande", "Divisez votre temps net")],
        "example": "420 minutes nettes ÷ 840 caméras = une caméra toutes les 30 secondes.",
        "example_cue": "Disons qu'une équipe a",
        "script": "Voici l'idée centrale. Le TAKT vient du mot allemand pour la mesure, ou le rythme. C'est "
                  "le rythme auquel vous devez terminer les unités pour répondre à la demande client. La "
                  "formule est simple. Divisez votre temps net disponible par la demande. Disons qu'une "
                  "équipe a quatre cent vingt minutes. Le client a besoin de huit cent quarante caméras. "
                  "Cela fait une caméra toutes les trente secondes. Est-ce le temps que prend réellement un "
                  "opérateur ? Non.",
    },
    {
        "key": "p02", "num": 2, "title": "Pourquoi le TAKT compte",
        "points": [("Relie votre client au terrain", "Le TAKT relie votre client"),
                   ("Pas de rythme commun → surproduction, WIP", "Sans rythme commun"),
                   ("Planifier l'effectif, équilibrer le travail, cadencer les matières", "Le TAKT vous aide à planifier")],
        "example": "L'assemblage de Rohan a fabriqué 1 000 caméras d'avance sur le test. Le taux "
                   "d'utilisation était superbe ; les camions partaient quand même en retard.",
        "example_cue": "Son assemblage a fabriqué",
        "script": "Le TAKT relie votre client au terrain. Sans rythme commun, les premiers postes "
                  "surproduisent, et le WIP s'accumule. Les manques se cachent, et l'expédition devient une "
                  "course. C'est exactement ce qui est arrivé à Rohan. Son assemblage a fabriqué mille "
                  "caméras d'avance sur le test. Le taux d'utilisation était superbe. Mais les camions "
                  "partaient quand même en retard. Le TAKT vous aide à planifier l'effectif, équilibrer le "
                  "travail, et cadencer les matières. Mais d'abord, il vous faut les bons chiffres. Par où "
                  "commencer ?",
    },
    {
        "key": "p03", "num": 3, "title": "Temps net disponible",
        "points": [("Partir de la durée de l'équipe", "Prenez la durée de votre équipe"),
                   ("Soustraire pauses, réunions, nettoyage prévus", "Puis soustrayez les pauses prévues"),
                   ("Ne pas soustraire ici les arrêts aléatoires", "ne soustrayez pas ici les arrêts aléatoires"),
                   ("Noter vos hypothèses", "notez vos hypothèses")],
        "example": "Équipe de 480 min − pauses − une courte réunion = 420 minutes nettes.",
        "example_cue": "Une équipe de huit heures",
        "script": "Partez du temps net disponible. Prenez la durée de votre équipe. Puis soustrayez les "
                  "pauses prévues, les réunions et le nettoyage prévu. Une équipe de huit heures fait "
                  "quatre cent quatre-vingts minutes. Retirez les pauses et une courte réunion, et il reste "
                  "quatre cent vingt. Mais ne soustrayez pas ici les arrêts aléatoires. C'est une perte que "
                  "vous traitez quand vous vérifiez la capacité. Soyez cohérent, et notez vos hypothèses. "
                  "Et l'autre moitié de la formule ?",
    },
    {
        "key": "p04", "num": 4, "title": "La demande client",
        "points": [("Demande et temps : même période", "La demande doit couvrir"),
                   ("Les bonnes unités nécessaires, pas les unités lancées", "Utilisez les bonnes unités"),
                   ("Multi-modèles : vérifier chacun", "Sur une ligne multi-modèles"),
                   ("Recalculer quand la demande ou les équipes changent", "recalculez chaque fois")],
        "example": "Demande journalière avec le temps d'une équipe = aucun sens.",
        "example_cue": "Mélanger la demande journalière",
        "script": "La demande doit couvrir la même période que votre temps. Si vous utilisez la demande "
                  "journalière, utilisez aussi le temps net journalier. Mélanger la demande journalière "
                  "avec le temps d'une seule équipe n'a aucun sens. Utilisez les bonnes unités dont votre "
                  "client a besoin, pas les unités que vous lancez. Sur une ligne multi-modèles, le TAKT "
                  "global est un repère. Mais chaque modèle a quand même besoin de sa propre vérification "
                  "de capacité. Et recalculez chaque fois que la demande ou les équipes changent. Alors, en "
                  "quoi le TAKT diffère-t-il du temps de cycle ?",
    },
    {
        "key": "p05", "num": 5, "title": "TAKT, temps de cycle et délai",
        "points": [("TAKT : le rythme nécessaire", "Le TAKT est le rythme nécessaire"),
                   ("Temps de cycle : ce que prend un poste", "Le temps de cycle est"),
                   ("Délai : tout le parcours", "Le délai est"),
                   ("Cycle > TAKT = ne peut pas suivre", "Si votre temps de cycle")],
        "example": "Une des lignes de Rohan : test final de 38 s contre un TAKT de 30 s. Il fallait "
                   "l'améliorer, ou ajouter un deuxième testeur.",
        "example_cue": "Sur une des lignes de Rohan",
        "script": "Voici la confusion la plus fréquente. Le TAKT est le rythme nécessaire. Le temps de "
                  "cycle est ce que prend réellement un poste, mesuré sur le terrain. Le délai est tout le "
                  "parcours, attentes et déplacements compris. Si votre temps de cycle est plus long que le "
                  "TAKT, ce poste ne peut pas suivre. Sur une des lignes de Rohan, le test final prenait "
                  "trente-huit secondes, contre un TAKT de trente. Il fallait l'améliorer, ou ajouter un "
                  "deuxième testeur. Définissez toujours d'abord vos points de début et de fin.",
    },
    {
        "key": "p06", "num": 6, "title": "Pitch, UPH et UPPH",
        "points": [("UPH : le rythme horaire nécessaire", "Les unités par heure"),
                   ("Pitch : le temps pour remplir un conditionnement", "Le pitch est"),
                   ("UPPH : production bonne par heure-personne", "L'UPPH mesure"),
                   ("La théorie n'est pas la production", "la théorie n'est pas la production")],
        "example": "TAKT de 24 s → 150 unités par heure. Conditionnement de 20 → un pitch de 8 minutes.",
        "example_cue": "Avec un TAKT de",
        "script": "Le TAKT se relie à d'autres chiffres utiles. Les unités par heure, ou UPH, sont le "
                  "rythme horaire nécessaire. Le pitch est le temps pour remplir un conditionnement "
                  "standard. Avec un TAKT de vingt-quatre secondes, il vous faut cent cinquante unités par "
                  "heure. Un conditionnement de vingt donne un pitch de huit minutes. L'UPPH mesure la "
                  "production bonne par heure-personne. Mais rappelez-vous, la théorie n'est pas la "
                  "production. La production réelle dépend de la disponibilité et du rendement. Alors, "
                  "comment équilibrer le travail ?",
    },
    {
        "key": "p07", "num": 7, "title": "Équilibrer avec le Yamazumi",
        "points": [("Chronométrer chaque élément de travail", "Découpez chaque travail"),
                   ("Empiler le travail de chaque opérateur en barre", "Empilez le travail de chaque opérateur"),
                   ("Tracer la ligne du TAKT en travers", "Puis tracez la ligne du TAKT"),
                   ("Déplacer ou repenser dans les limites de sécurité et de compétence", "Vous déplacez donc ou repensez")],
        "example": "TAKT de 40 s : l'opérateur A a 52 s de travail, l'opérateur B seulement 25 s.",
        "example_cue": "Sur une des cellules de Rohan",
        "script": "Vous utilisez un diagramme Yamazumi. Découpez chaque travail en éléments répétables, et "
                  "chronométrez-les. Empilez le travail de chaque opérateur en une barre. Puis tracez la "
                  "ligne du TAKT en travers. Toute barre au-dessus de la ligne est surchargée. Sur une des "
                  "cellules de Rohan, le TAKT était de quarante secondes. L'opérateur A avait "
                  "cinquante-deux secondes de travail. L'opérateur B en avait seulement vingt-cinq. Vous "
                  "déplacez donc ou repensez les tâches, dans les limites de sécurité et de compétence. De "
                  "combien de personnes avez-vous besoin ?",
    },
    {
        "key": "p08", "num": 8, "title": "Nombre minimum d'opérateurs",
        "points": [("Contenu de travail ÷ TAKT, arrondi au-dessus", "Divisez le contenu total de travail manuel"),
                   ("Seulement un point de départ", "prenez-le comme un point de départ"),
                   ("Utiliser une étude de temps stable", "Utilisez une étude de temps stable")],
        "example": "310 s de travail ÷ TAKT de 40 s = 7,75 → au moins 8 opérateurs.",
        "example_cue": "La cellule de Rohan avait",
        "script": "Voici une estimation rapide. Divisez le contenu total de travail manuel par le TAKT, "
                  "puis arrondissez au-dessus. La cellule de Rohan avait trois cent dix secondes de travail "
                  "par caméra. Avec un TAKT de quarante, cela donne sept virgule soixante-quinze. Il vous "
                  "faut donc au moins huit opérateurs. Mais prenez-le comme un point de départ. La marche, "
                  "l'approvisionnement, les contrôles qualité et les niveaux de compétence comptent tous. "
                  "Utilisez une étude de temps stable, pas un seul cycle idéal. Qu'est-ce qui limite votre "
                  "production ?",
    },
    {
        "key": "p09", "num": 9, "title": "Goulots et postes en parallèle",
        "points": [("Le goulot limite la bonne production", "C'est l'étape qui limite"),
                   ("Capacité = 3 600 ÷ temps de cycle", "La capacité horaire d'un poste"),
                   ("Appliquer disponibilité et rendement au premier passage", "Appliquez la disponibilité"),
                   ("Des preuves avant d'acheter une machine", "Vérifiez les preuves")],
        "example": "Deux testeurs à 50 s = 144 tentatives par heure → environ 127 bonnes unités après "
                   "disponibilité et rendement.",
        "example_cue": "Deux testeurs à cinquante",
        "script": "Le goulot. C'est l'étape qui limite votre bonne production. La capacité horaire d'un "
                  "poste est de trois mille six cents secondes, divisées par son temps de cycle. Deux "
                  "testeurs à cinquante secondes chacun donnent cent quarante-quatre tentatives par heure. "
                  "Mais les testeurs s'arrêtent, et certaines unités échouent. Appliquez la disponibilité "
                  "et le rendement au premier passage, et vous obtenez environ cent vingt-sept bonnes "
                  "unités. Vérifiez les preuves avant d'acheter une autre machine. Et les modèles mélangés "
                  "?",
    },
    {
        "key": "p10", "num": 10, "title": "Modèles mélangés et Heijunka",
        "points": [("Un seul TAKT ne convient pas à tous les modèles", "Un seul TAKT"),
                   ("Vérifier les temps de poste de chaque modèle", "Vérifiez donc les temps de chaque modèle"),
                   ("Heijunka : lisser le volume et le mix", "Utilisez le Heijunka"),
                   ("SMED : réduire les pertes de changement de série", "utilisez le SMED")],
        "example": "60 % modèle A, 40 % modèle B avec un test plus long : planifiez tous les B ensemble et "
                   "le test est noyé.",
        "example_cue": "Disons que soixante pour cent",
        "script": "Un seul TAKT ne garantit pas que tous les modèles passent. Disons que soixante pour cent "
                  "de la demande de Rohan est le modèle A, et quarante pour cent le modèle B. Le modèle B "
                  "demande un test plus long. Si le plan regroupe tous les B ensemble, le test est noyé, "
                  "même si la moyenne paraît correcte. Vérifiez donc les temps de chaque modèle. Utilisez "
                  "le Heijunka pour lisser le volume et le mix. Et utilisez le SMED pour réduire vos pertes "
                  "de changement de série. Et les matières ?",
    },
    {
        "key": "p11", "num": 11, "title": "Flux matière et Kanban",
        "points": [("Le TAKT fixe le rythme des matières", "Le TAKT fixe aussi"),
                   ("Kanban : délai, taille du contenant", "Les quantités Kanban"),
                   ("Limites de WIP entre processus", "Fixez des limites de WIP"),
                   ("Ne pas lancer du travail juste pour rester occupé", "Ne lancez pas de nouveau travail")],
        "example": "TAKT de 30 s, bac de 40 → dure 20 minutes ; le réapprovisionnement doit arriver avant.",
        "example_cue": "Avec un TAKT de trente secondes",
        "script": "Le TAKT fixe aussi le rythme des matières. Avec un TAKT de trente secondes, un bac de "
                  "quarante pièces dure vingt minutes. Le réapprovisionnement doit donc arriver avant qu'il "
                  "ne soit vide, avec une marge pour la variation. Les quantités Kanban dépendent aussi du "
                  "délai et de la taille du contenant. Fixez des limites de WIP entre processus. Et voici "
                  "une règle stricte. Ne lancez pas de nouveau travail juste pour occuper chaque poste. "
                  "Alors, comment piloter la journée ?",
    },
    {
        "key": "p12", "num": 12, "title": "Plan face au réel chaque heure",
        "points": [("Prévu = secondes nettes ÷ TAKT", "Les unités prévues sont égales"),
                   ("Comparer le réel au plan", "Disons que vous en faites"),
                   ("Noter pourquoi : arrêts, rejets, matières", "Notez maintenant pourquoi"),
                   ("Ne pas accuser la vitesse de l'opérateur", "N'accusez pas chaque manque")],
        "example": "TAKT de 30 s → 120 prévues par heure. Faites 108 = 90 %, un écart de 12.",
        "example_cue": "Avec un TAKT de trente secondes",
        "script": "Utilisez un tableau horaire plan face au réel. Les unités prévues sont égales aux "
                  "secondes nettes de l'heure, divisées par le TAKT. Avec un TAKT de trente secondes, vous "
                  "prévoyez cent vingt bonnes caméras. Disons que vous en faites cent huit. Cela fait "
                  "quatre-vingt-dix pour cent, et un écart de douze. Notez maintenant pourquoi. Arrêts, "
                  "rejets, matières, ou effectif. N'accusez pas chaque manque sur la vitesse de "
                  "l'opérateur. Prêt pour le cas complet de Rohan ?",
    },
    {
        "key": "p13", "num": 13, "title": "Cas pratique : usine de caméras",
        "points": [("7 200 bonnes caméras par jour, 1 200 min nettes", "L'usine de Rohan doit expédier"),
                   ("TAKT = 10 secondes", "Le TAKT est donc de dix secondes"),
                   ("Le test prend 18 s — la contrainte", "Mais le test prend"),
                   ("Deux testeurs ≈ 353 bonnes/heure contre 360", "Deux testeurs donnent")],
        "example": "2 testeurs = 400 tentatives/heure sur le papier → ≈ 353 bonnes avec la disponibilité et "
                   "le rendement réels. Cible : 360.",
        "example_cue": "Avec la disponibilité",
        "script": "L'usine de Rohan doit expédier sept mille deux cents bonnes caméras par jour. Elle a "
                  "mille deux cents minutes nettes, sur trois équipes. Le TAKT est donc de dix secondes. "
                  "Les postes d'objectif et d'assemblage sont plus rapides que cela. Mais le test prend "
                  "dix-huit secondes. Deux testeurs donnent quatre cents tentatives par heure sur le "
                  "papier. Avec la disponibilité et le rendement réels, cela fait environ trois cent "
                  "cinquante-trois bonnes unités. La cible est trois cent soixante. Que feriez-vous ?",
    },
    {
        "key": "p14", "num": 14, "title": "Erreurs fréquentes",
        "points": [("À FAIRE : utiliser la demande approuvée et le temps net", "Utilisez la demande approuvée"),
                   ("À FAIRE : mettre à jour le TAKT quand les choses changent", "Mettez à jour le TAKT"),
                   ("À ÉVITER : le confondre avec le temps de cycle", "Ne le confondez pas"),
                   ("À ÉVITER : sauter des tests, des étapes ou des pauses", "ne cherchez jamais la vitesse en sautant des tests, des étapes du SOP")],
        "example": "Rohan a amélioré la disponibilité du testeur et réduit le cycle de test avant d'acheter "
                   "un troisième testeur.",
        "example_cue": "Rohan a amélioré la disponibilité",
        "script": "Rohan a amélioré la disponibilité du testeur, et réduit le cycle de test, avant "
                  "d'acheter un troisième testeur. Maintenant, attention aux erreurs fréquentes. Utilisez "
                  "la demande approuvée et le bon temps net. Mettez à jour le TAKT quand la demande ou les "
                  "équipes changent. Ne le confondez pas avec le temps de cycle. N'utilisez pas les heures "
                  "brutes de l'équipe. Et ne cherchez jamais la vitesse en sautant des tests, des étapes du "
                  "SOP ou des pauses. Vos responsables savent-ils expliquer les chiffres derrière le TAKT "
                  "de votre tableau ?",
    },
    {
        "key": "p15", "num": 15, "title": "Feuille de route sur 90 jours",
        "points": [("Jours 1–30 : demande, temps net, temps de cycle", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : Yamazumi, tableaux horaires", "Pendant les trente suivants"),
                   ("Jours 61–90 : vérifier production et rendement, élargir", "Pendant les trente derniers"),
                   ("Objectif : une bonne production fiable", "Rappelez-vous l'objectif")],
        "example": "Une bonne production fiable au rythme du client — pas occuper chaque poste.",
        "example_cue": "C'est une bonne production fiable",
        "script": "Commencez par une ligne représentative de votre usine. Pendant les trente premiers "
                  "jours, rassemblez la demande, le temps net et les vrais temps de cycle, et cartographiez "
                  "l'équilibre actuel. Pendant les trente suivants, faites un pilote de Yamazumi, de "
                  "travail standard et de tableaux horaires. Attaquez le goulot. Pendant les trente "
                  "derniers, vérifiez la production et le rendement, formez des remplaçants, et élargissez. "
                  "Rappelez-vous l'objectif. C'est une bonne production fiable au rythme du client. Pas "
                  "occuper chaque poste.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Takt = mesure", "icon": "wave", "with": 0}, {"label": "Le rythme fixé par la demande", "icon": "clock", "with": 1},
        {"label": "Temps net ÷ demande", "icon": "count", "with": 2}],
        "then": {"type": "stat", "value": 30, "suffix": " s", "icon": "camera", "label": "une caméra toutes les 30 secondes",
                 "unit": "420 minutes nettes ÷ 840 caméras", "with": "example"}},
    "p02": {"type": "versus", "items": [
        {"label": "1 000 fabriquées avant le test", "sub": "Postes occupés, camions en retard", "icon": "stack", "with": "example"},
        {"label": "Un rythme commun", "sub": "Effectif, équilibre, matières", "icon": "clock", "with": 2}]},
    "p03": {"type": "flow", "items": [
        {"label": "Équipe de 480 min", "icon": "clock", "with": 0},
        {"label": "− pauses, réunion, nettoyage", "icon": "calendar", "with": 1},
        {"label": "= 420 minutes nettes", "sub": "Les arrêts aléatoires ne sont pas retirés ici", "icon": "check", "tone": "good", "with": "example"}]},
    "p04": {"type": "versus", "items": [
        {"label": "Demande journalière ÷ une équipe", "sub": "Aucun sens", "icon": "cross", "with": "example"},
        {"label": "Même période pour les deux", "sub": "Bonnes unités, pas unités lancées", "icon": "calendar", "with": 0}]},
    "p05": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Le rythme nécessaire", "icon": "clock", "with": 0},
        {"label": "Temps de cycle", "sub": "Ce que prend un poste", "icon": "gear", "with": 1},
        {"label": "Délai", "sub": "Tout le parcours", "icon": "sequence", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "Le test ne suit pas : améliorez-le, ou ajoutez un testeur", "unit": "secondes par caméra", "with": "example", "items": [
            {"label": "TAKT", "value": 30, "tone": "good", "with": "example"},
            {"label": "Test final", "value": 38, "tone": "bad", "with": "example"}]}},
    "p06": {"type": "icons", "items": [
        {"label": "UPH", "sub": "Rythme horaire nécessaire", "icon": "chartUp", "with": 0},
        {"label": "Pitch", "sub": "Temps pour remplir un conditionnement", "icon": "box", "with": 1},
        {"label": "UPPH", "sub": "Production bonne par heure-personne", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "TAKT 24 s", "icon": "clock", "with": "example"},
            {"label": "= 150 unités par heure", "icon": "chartUp", "with": "example"},
            {"label": "Conditionnement de 20 = pitch de 8 min", "icon": "box", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Chronométrer chaque élément", "icon": "clock"}, {"label": "Empiler chaque opérateur", "icon": "stack"},
        {"label": "Tracer la ligne du TAKT", "icon": "sequence"}, {"label": "Déplacer le travail, en sécurité", "icon": "person"}],
        "then": {"type": "bars", "label": "TAKT", "value": 40, "suffix": " s", "note": "A est surchargé", "unit": "secondes de travail par opérateur", "with": "example", "items": [
            {"label": "Opérateur A", "value": 52, "tone": "bad", "with": "example"},
            {"label": "Opérateur B", "value": 25, "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Travail ÷ TAKT, arrondi au-dessus", "icon": "count", "with": 0},
        {"label": "Un point de départ", "icon": "sequence", "with": 1},
        {"label": "Étude de temps stable", "icon": "clock", "with": 2}],
        "then": {"type": "stat", "value": 8, "icon": "person", "label": "opérateurs, au moins",
                 "unit": "310 s de travail ÷ TAKT de 40 s = 7,75, arrondi au-dessus", "with": "example"}},
    "p09": {"type": "icons", "items": [
        {"label": "Le goulot", "icon": "warning", "tone": "bad"}, {"label": "3 600 ÷ temps de cycle", "icon": "count"},
        {"label": "Disponibilité × rendement", "icon": "chartUp"}, {"label": "Les preuves d'abord", "icon": "search"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "2 testeurs à 50 s", "icon": "test", "with": "example"},
            {"label": "144 tentatives par heure", "icon": "count", "with": "example"},
            {"label": "≈ 127 bonnes après disponibilité et rendement", "icon": "check", "tone": "good", "with": "example"}]}},
    "p10": {"type": "versus", "items": [
        {"label": "Tous les B ensemble", "sub": "Le test est noyé", "icon": "stack", "with": "example"},
        {"label": "Lisser le mix", "sub": "Heijunka + SMED", "icon": "sequence", "with": 2}]},
    "p11": {"type": "stat", "value": 20, "suffix": " min", "icon": "box", "label": "un bac de 40 pièces dure",
            "unit": "avec un TAKT de 30 s : le réapprovisionnement doit arriver avant", "with": "example"},
    "p12": {"type": "bars", "label": "", "note": "90 % : un écart de 12. Notez pourquoi.", "unit": "bonnes caméras en une heure, TAKT de 30 s", "items": [
        {"label": "Prévu", "value": 120, "with": "example"},
        {"label": "Fait", "value": 108, "tone": "bad", "with": "example"}]},
    "p13": {"type": "stat", "value": 10, "suffix": " s", "icon": "clock", "label": "TAKT pour 7 200 bonnes caméras par jour",
            "unit": "1 200 minutes nettes ÷ 7 200 caméras", "with": 1,
            "then": {"type": "bars", "label": "Cible", "value": 360, "unit": "bonnes caméras par heure, deux testeurs", "with": 3, "items": [
                {"label": "Sur le papier", "value": 400, "with": 3},
                {"label": "Réel", "value": 353, "tone": "bad", "with": 3}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Demande approuvée + temps net", "icon": "check", "tone": "good"},
        {"label": "Mettre à jour quand ça change", "icon": "sequence", "tone": "good"},
        {"label": "Pas le temps de cycle", "icon": "cross", "tone": "bad"},
        {"label": "Ne jamais sauter tests ou pauses", "icon": "warning", "tone": "bad"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Demande, temps net, temps de cycle", "sub": "Jours 1–30", "icon": "clipboard", "with": 0},
        {"label": "Yamazumi, tableaux horaires", "sub": "31–60", "icon": "stack", "with": 1},
        {"label": "Vérifier production et rendement, élargir", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Une équipe a 25 200 secondes nettes et le client a besoin de 840 unités. Quel est le "
                    "temps TAKT ?",
        "options": ["20 secondes", "30 secondes", "40 secondes"],
        "correct": 1,
        "explanation": "TAKT = temps net disponible ÷ demande = 25 200 ÷ 840 = 30 secondes par unité.",
        "q_script": "Vérification rapide. Une équipe a vingt-cinq mille deux cents secondes nettes. Le client "
                    "a besoin de huit cent quarante unités. Quel est le temps TAKT ? Prenez quelques "
                    "secondes.",
        "a_script": "C'est trente secondes. Le TAKT est le temps net disponible divisé par la demande. Donc "
                    "une unité toutes les trente secondes.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Le test final prend 38 s par unité, mais le TAKT est de 30 s. Un responsable dit : « "
                    "Dites aux testeurs d'aller plus vite. » Que doit faire l'équipe EN PREMIER ?",
        "options": ["Sauter une partie du test pour gagner du temps", "Analyser les pertes et la capacité du poste de test",
                    "Constituer du stock en amont", "Recalculer le TAKT avec le temps brut de l'équipe"],
        "correct": 1,
        "explanation": "Un temps de cycle au-dessus du TAKT est un problème de capacité. Étudiez les pertes, le "
                       "cycle et la disponibilité du poste, puis améliorez-le ou ajoutez une capacité vérifiée. "
                       "Sauter des tests ou masquer le problème avec du stock crée de nouveaux problèmes.",
        "q_script": "Encore une, et cette fois c'est un scénario. Le test final prend trente-huit secondes, "
                    "mais le TAKT est de trente. Un responsable dit, dites aux testeurs d'aller plus vite. "
                    "Que doit faire l'équipe en premier ? Réfléchissez.",
        "a_script": "Analysez d'abord le poste de test. Étudiez ses pertes, son cycle et sa disponibilité, "
                    "puis améliorez-le, ou ajoutez une capacité prouvée. Sauter des tests ou constituer du "
                    "stock ne fait que créer de nouveaux problèmes.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
