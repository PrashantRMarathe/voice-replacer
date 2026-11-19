"""skill_matrix in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh skill_matrix_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "sk_fr"
NAME = "skill_matrix_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Skill Training Matrix": "skil tréïning matrix",
    "One Point Lesson": "ouane poïnnte lèsseune",
    "Dojo": "Dodjo",
    "TAKT": "takte",
    "SOP": "esse o pé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Lundi matin. Bala est malade. C'est la seule personne capable de régler la mise au point "
    "des objectifs. À dix heures, toute la cellule caméras est à l'arrêt. Ça vous dit quelque "
    "chose ? Dans cette leçon, vous allez découvrir la Skill Training Matrix. Vous verrez qui "
    "peut vraiment faire quel travail, où sont les écarts, et comment les combler. Nous "
    "suivrons Vikram, chef de cellule, qui en construit une pour son équipe."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Une matrice de compétences montre une capacité démontrée, "
    "pas une présence. Comptez les remplaçants qualifiés pour chaque travail critique, dans "
    "chaque équipe. Et gardez-la vivante, avec une preuve derrière chaque niveau. Voici votre "
    "action pour cette semaine. Listez vos trois postes les plus critiques, et comptez les "
    "personnes qualifiées pour chacun. Bravo d'avoir terminé cette leçon. Ensuite, vous "
    "découvrirez le temps TAKT, le battement de votre ligne."
)

# One story thread: Vikram's network-camera cell. Operators Asha, Bala, Chitra,
# Deepa; skills ESD, PCB assembly, lens focus, test, packing; L0-L4, L3 = qualified.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est une matrice de compétences",
        "points": [("Qui peut faire quel travail, et à quel niveau", "qui peut faire"),
                   ("Le niveau prouvé de chaque personne", "Elle montre le niveau prouvé"),
                   ("Les écarts", "Et elle montre les écarts"),
                   ("Pas une feuille de présence", "Ce n'est pas une feuille de présence")],
        "example": "La cellule de Vikram : assemblage des cartes, mise au point des objectifs, test et "
                   "emballage — avec des remplaçants approuvés pour chacun.",
        "example_cue": "La cellule de Vikram comprend",
        "script": "Voici l'idée centrale. Une Skill Training Matrix est un registre visuel de qui peut "
                  "faire quel travail, et à quel niveau. Elle montre le niveau prouvé de chaque personne, "
                  "sur chaque opération. Et elle montre les écarts. Ce n'est pas une feuille de présence, "
                  "ni une liste de cours. La cellule de Vikram comprend l'assemblage des cartes, la mise au "
                  "point des objectifs, le test et l'emballage. Sa matrice montre les remplaçants approuvés "
                  "pour chacun. Pourquoi est-ce si important sur votre ligne ?",
    },
    {
        "key": "p02", "num": 2, "title": "Pourquoi c'est important",
        "points": [("Planifier l'effectif, couvrir les absences, équilibrer", "Les superviseurs l'utilisent"),
                   ("Confirmer la compétence sur les étapes critiques", "La qualité l'utilise"),
                   ("Un chemin clair pour progresser", "Et les personnes voient")],
        "example": "Compétent pour régler les chargeurs ≠ autorisé à libérer un programme. Deux compétences "
                   "différentes.",
        "example_cue": "Un technicien peut être compétent",
        "script": "Parce qu'elle relie vos personnes à vos résultats. Les superviseurs l'utilisent pour "
                  "planifier l'effectif, couvrir les absences, et équilibrer la ligne. La qualité l'utilise "
                  "pour confirmer qui est compétent sur les étapes critiques. Et les personnes voient un "
                  "chemin clair pour progresser. Voici un point subtil. Un technicien peut être compétent "
                  "pour régler les chargeurs, mais pas autorisé à libérer un programme. Ce sont deux "
                  "compétences différentes. Quels trois postes vous feraient le plus mal si leur seul "
                  "expert était absent ?",
    },
    {
        "key": "p03", "num": 3, "title": "Structure de la matrice",
        "points": [("Lignes : les personnes", "Les personnes vont en lignes"),
                   ("Colonnes : les compétences", "Les compétences vont en colonnes"),
                   ("Chaque case : niveau + dernière évaluation", "Chaque case montre"),
                   ("Chaque compétence liée à son SOP", "Chaque compétence est liée"),
                   ("Ne pas regrouper plusieurs tâches en une compétence", "Ne regroupez jamais des tâches différentes")],
        "example": "La production la tient à jour ; les formateurs évaluent ; la qualité valide les "
                   "compétences critiques.",
        "example_cue": "La production tient la matrice",
        "script": "La mise en page est simple. Les personnes vont en lignes. Les compétences vont en "
                  "colonnes. Chaque case montre le niveau de la personne, et la date de sa dernière "
                  "évaluation. Chaque compétence est liée à son SOP, et indique sa criticité. La production "
                  "tient la matrice à jour. Les formateurs évaluent, et la qualité valide les compétences "
                  "critiques. Et voici une règle. Ne regroupez jamais des tâches différentes en une seule "
                  "compétence, juste pour que le tableau paraisse plein. Alors, que veulent dire les "
                  "niveaux ?",
    },
    {
        "key": "p04", "num": 4, "title": "Niveaux de maîtrise L0–L4",
        "points": [("L0 non formé", "Le niveau zéro veut dire"),
                   ("L1 comprend la sécurité et la séquence", "Le niveau un veut dire"),
                   ("L2 travaille sous supervision", "Le niveau deux veut dire"),
                   ("L3 qualifié pour travailler seul", "Le niveau trois veut dire"),
                   ("L4 forme les autres, dépanne", "Le niveau quatre veut dire")],
        "example": "Un niveau n'est pas une habilitation : l'autorisation machine et sécurité est "
                   "enregistrée à part.",
        "example_cue": "Mais un niveau n'est pas une habilitation",
        "script": "Utilisez une échelle à cinq niveaux. Le niveau zéro veut dire non formé. Le niveau un "
                  "veut dire que vous comprenez la sécurité, la séquence et les principaux risques. Le "
                  "niveau deux veut dire que vous pouvez le faire sous supervision. Le niveau trois veut "
                  "dire que vous êtes qualifié pour travailler seul, dans le temps de cycle et les limites "
                  "qualité. Le niveau quatre veut dire que vous pouvez former les autres et dépanner. Mais "
                  "un niveau n'est pas une habilitation. L'autorisation machine et sécurité est enregistrée "
                  "à part. Quelles compétences d'abord ?",
    },
    {
        "key": "p05", "num": 5, "title": "Trouver les compétences critiques",
        "points": [("Cartographier chaque étape et son SOP", "Listez chaque étape"),
                   ("Repérer l'impact sécurité, qualité, client", "Puis repérez les compétences"),
                   ("Noter impact, difficulté, remplaçants", "Notez l'impact"),
                   ("Effectif qualifié minimum par équipe", "fixez un effectif qualifié minimum")],
        "example": "La cellule de Vikram : la mise au point des objectifs et le flashage du firmware sont en "
                   "tête ; la manutention des cartons, plus bas.",
        "example_cue": "Dans la cellule de Vikram",
        "script": "Partez de votre cartographie du processus. Listez chaque étape, et le SOP qui la régit. "
                  "Puis repérez les compétences où une erreur touche la sécurité, la qualité ou le client. "
                  "Notez l'impact, la difficulté d'apprentissage, et le nombre de remplaçants que vous "
                  "avez. Dans la cellule de Vikram, la mise au point des objectifs et le flashage du "
                  "firmware sont en tête. Un mauvais réglage là arrive jusqu'au client. La manutention des "
                  "cartons est plus bas. Pour chaque compétence critique, fixez un effectif qualifié "
                  "minimum par équipe.",
    },
    {
        "key": "p06", "num": 6, "title": "Évaluer la vraie compétence",
        "points": [("Bref contrôle théorique", "Vérifiez brièvement la théorie"),
                   ("Observer de vrais cycles + une situation anormale", "Observez plusieurs vrais cycles"),
                   ("Noter la date, l'évaluateur, les résultats", "Notez la date")],
        "example": "Une opératrice de test a réussi la théorie mais ratait encore des scans de séries "
                   "défaillantes — elle reste au niveau deux.",
        "example_cue": "Une des opératrices de test de Vikram",
        "script": "Alors, comment savoir que quelqu'un est vraiment au niveau trois ? Vous testez ce qu'il "
                  "sait réellement faire. Vérifiez brièvement la théorie, puis observez le travail "
                  "pratique. Observez plusieurs vrais cycles, et au moins une situation anormale. Notez la "
                  "date, l'évaluateur et les résultats. Une des opératrices de test de Vikram a réussi la "
                  "théorie facilement. Mais elle ratait encore des scans de séries défaillantes. Elle reste "
                  "donc au niveau deux pour l'instant. Quand faut-il réévaluer ?",
    },
    {
        "key": "p07", "num": 7, "title": "Besoins de formation et écarts",
        "points": [("Réévaluer après une absence ou un changement", "Réévaluez après"),
                   ("Besoin = niveau requis − niveau prouvé", "Un besoin est l'écart"),
                   ("Compter les personnes qualifiées face aux postes", "Comptez vos personnes qualifiées"),
                   ("Trouver les points de défaillance uniques", "Cherchez bien les points de défaillance")],
        "example": "L'équipe de Vikram a besoin de 4 opérateurs firmware qualifiés et en a 2 : un écart de "
                   "2.",
        "example_cue": "L'équipe de Vikram a besoin",
        "script": "Réévaluez après une longue absence, un changement de processus ou des défauts répétés. "
                  "Puis calculez vos besoins de formation. Un besoin est l'écart entre le niveau exigé et "
                  "le niveau prouvé. Comptez vos personnes qualifiées face aux postes à tenir. L'équipe de "
                  "Vikram a besoin de quatre opérateurs firmware qualifiés. Elle en a deux. C'est un écart "
                  "de deux. Cherchez bien les points de défaillance uniques, comme Bala sur la mise au "
                  "point des objectifs. Comment combler l'écart ?",
    },
    {
        "key": "p08", "num": 8, "title": "Méthodes de formation",
        "points": [("Formation structurée au poste", "formation structurée au poste"),
                   ("Un évaluateur indépendant vérifie le résultat", "Un évaluateur indépendant"),
                   ("Dojo : pratique sûre hors ligne", "Un Dojo est"),
                   ("One Point Lesson pour les points clés", "Les One Point Lesson renforcent")],
        "example": "Le Dojo d'emballage de Vikram utilise exprès de mauvaises étiquettes et des accessoires "
                   "manquants.",
        "example_cue": "Le Dojo d'emballage de Vikram",
        "script": "Formez vos équipes par une formation structurée au poste. Le formateur prépare, démontre "
                  "au rythme standard, puis l'apprenant pratique avec des retours. Un évaluateur "
                  "indépendant vérifie le résultat. Un Dojo est une zone de formation hors ligne, où l'on "
                  "peut pratiquer en sécurité. Le Dojo d'emballage de Vikram utilise exprès de mauvaises "
                  "étiquettes et des accessoires manquants. Les One Point Lesson renforcent des points clés "
                  "isolés. Et n'oubliez pas d'enseigner la réaction aux problèmes, pas seulement les étapes "
                  "normales.",
    },
    {
        "key": "p09", "num": 9, "title": "Le plan de formation sur 90 jours",
        "points": [("Jours 1–30 : cartographier, définir les niveaux, évaluer", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : former sur les écarts critiques", "Pendant les trente suivants"),
                   ("Jours 61–90 : certifier les remplaçants, élargir", "Pendant les trente derniers")],
        "example": "La première priorité de Vikram : qualifier un deuxième expert en mise au point des "
                   "objectifs.",
        "example_cue": "La première priorité de Vikram",
        "script": "Tout plan de formation a besoin de responsables, de dates et d'un résultat clair. Voici "
                  "une version sur quatre-vingt-dix jours. Pendant les trente premiers jours, cartographiez "
                  "les compétences, définissez les niveaux, et évaluez où vous en êtes. Pendant les trente "
                  "suivants, formez sur les écarts critiques, et vérifiez ceux qui passent au niveau trois. "
                  "Pendant les trente derniers, certifiez les remplaçants et élargissez. La première "
                  "priorité de Vikram était évidente. Qualifier un deuxième expert en mise au point des "
                  "objectifs. Quelle serait la vôtre ?",
    },
    {
        "key": "p10", "num": 10, "title": "KPI de la matrice",
        "points": [("Couverture de qualification", "La couverture de qualification demande"),
                   ("Atteinte des compétences", "L'atteinte des compétences suit"),
                   ("Taux de polyvalence", "Le taux de polyvalence compte"),
                   ("Qualifications expirées", "comptez les qualifications expirées")],
        "example": "18 postes critiques couverts sur 24 = 75 %. Calculez-le par équipe.",
        "example_cue": "Vikram a dix-huit",
        "script": "Mesurez votre vraie résilience, pas les heures de formation. La couverture de "
                  "qualification demande combien de postes requis ont une personne qualifiée. L'atteinte "
                  "des compétences suit les montées de niveau prévues qui sont vérifiées. Le taux de "
                  "polyvalence compte les personnes qualifiées sur deux travaux ou plus. Et comptez les "
                  "qualifications expirées. Vikram a dix-huit postes critiques couverts sur vingt-quatre. "
                  "Cela fait soixante-quinze pour cent. Calculez-le par équipe, car une personne ne peut "
                  "pas tenir deux postes à la fois.",
    },
    {
        "key": "p11", "num": 11, "title": "Exemple concret : la cellule de Vikram",
        "points": [("Asha : assemblage des cartes L4", "Asha est de niveau quatre"),
                   ("Chitra rejoint maintenant Bala : mise au point des objectifs L3", "Chitra a maintenant rejoint"),
                   ("Chitra, Deepa : test L3+", "Chitra et Deepa sont"),
                   ("Prochaine priorité : un autre remplaçant en mise au point", "Alors, quelle est la prochaine")],
        "example": "Mise au point + test en même temps : Bala à la mise au point, Deepa au test. Chitra ne "
                   "peut pas faire les deux.",
        "example_cue": "Alors, qui couvre la mise au point",
        "script": "Voici la matrice de Vikram après quatre-vingt-dix jours. Asha est de niveau quatre en "
                  "assemblage des cartes. Chitra a maintenant rejoint Bala au niveau trois en mise au point "
                  "des objectifs. Chitra et Deepa sont qualifiées au test. Alors, qui couvre la mise au "
                  "point et le test en même temps ? Bala à la mise au point, et Deepa au test. Chitra ne "
                  "peut pas faire les deux à la fois. Si Bala est absent, Chitra doit passer à la mise au "
                  "point. Alors, quelle est la prochaine priorité de formation ? Un autre remplaçant en "
                  "mise au point des objectifs.",
    },
    {
        "key": "p12", "num": 12, "title": "Lien avec la qualité et la sécurité",
        "points": [("Niveau + autorisation + formation au SOP", "que quand trois choses sont à jour"),
                   ("Chaque compétence liée à la révision de son SOP", "Liez chaque compétence"),
                   ("Changement de processus → réévaluer", "Quand le processus change"),
                   ("La formation ne remplace jamais la conception du processus", "la formation ne remplace jamais")],
        "example": "Le technicien firmware de Vikram était L3 sur l'ancienne recette — la nouvelle a changé "
                   "des étapes critiques, il a donc été réévalué.",
        "example_cue": "Le technicien firmware de Vikram",
        "script": "Une matrice de compétences est une protection qualité. Quelqu'un ne doit travailler seul "
                  "sur une étape critique que quand trois choses sont à jour. Son niveau, son autorisation, "
                  "et sa formation au SOP. Liez chaque compétence à la révision de son SOP. Quand le "
                  "processus change, réévaluez. Le technicien firmware de Vikram était de niveau trois sur "
                  "l'ancienne recette. La nouvelle a changé des étapes critiques, il a donc été réévalué. "
                  "Et rappelez-vous, la formation ne remplace jamais une bonne conception du processus. Le "
                  "logiciel peut-il aider ?",
    },
    {
        "key": "p13", "num": 13, "title": "Matrice numérique et tableau visuel",
        "points": [("Codes uniques pour les personnes et les compétences", "Utilisez des codes uniques"),
                   ("Traçabilité de chaque modification", "gardez une trace de chaque modification"),
                   ("Rappels pour les qualifications qui expirent", "Mettez des rappels"),
                   ("Pas d'auto-approbation des compétences critiques", "Ne laissez jamais personne approuver")],
        "example": "Le tableau de bord de Vikram l'avertit quand une autorisation va expirer.",
        "example_cue": "Le tableau de bord de Vikram l'avertit",
        "script": "Oui, si les données sont fiables. Une matrice numérique relie les évaluations, les "
                  "révisions du SOP et les plannings d'équipe. Utilisez des codes uniques pour les "
                  "personnes et les compétences, et gardez une trace de chaque modification. Mettez des "
                  "rappels pour les qualifications qui expirent. Ne laissez jamais personne approuver sa "
                  "propre compétence critique. Le tableau de bord de Vikram l'avertit quand une "
                  "autorisation va expirer. Et voici une question d'audit. Pouvez-vous montrer la preuve "
                  "derrière n'importe quel niveau trois ?",
    },
    {
        "key": "p14", "num": 14, "title": "Gouvernance et revue",
        "points": [("Chaque jour : effectif qualifié au démarrage", "Chaque jour"),
                   ("Chaque semaine : écarts, polyvalence, retards", "Chaque semaine"),
                   ("Chaque mois : couverture, départs", "Chaque mois"),
                   ("Chaque trimestre : cohérence des évaluateurs", "Chaque trimestre")],
        "example": "L'ancienneté et la présence ne valent pas qualification.",
        "example_cue": "L'ancienneté et la présence",
        "script": "Gardez la matrice vivante avec un rythme de revue régulier. Chaque jour, vérifiez que "
                  "les postes critiques sont tenus par des personnes qualifiées au démarrage. Chaque "
                  "semaine, revoyez les écarts, la polyvalence et les évaluations en retard. Chaque mois, "
                  "regardez la couverture et le risque de départs. Chaque trimestre, vérifiez que les "
                  "évaluateurs notent de façon cohérente. Et mettez à jour les niveaux quand la capacité "
                  "change vraiment, pas selon le calendrier. L'ancienneté et la présence ne valent pas "
                  "qualification. Prêt à construire la vôtre ?",
    },
    {
        "key": "p15", "num": 15, "title": "Modèles et audit",
        "points": [("Matrice : compétence, rév. du SOP, niveau, expiration", "La matrice contient"),
                   ("Fiche d'évaluation : théorie, cycles, sécurité", "La fiche d'évaluation"),
                   ("Un plan de formation pour chaque écart", "Chaque écart reçoit"),
                   ("Auditer les cases face au travail réel", "Puis auditez-la")],
        "example": "Un autre superviseur doit voir d'un coup d'œil qui est qualifié aujourd'hui.",
        "example_cue": "Un autre superviseur doit voir",
        "script": "Utilisez un modèle maîtrisé pour votre matrice. La matrice contient chaque personne, "
                  "compétence, révision du SOP, niveau, date d'évaluation et expiration. La fiche "
                  "d'évaluation enregistre la théorie, les cycles observés, les contrôles de sécurité et le "
                  "résultat. Chaque écart reçoit un plan de formation. Puis auditez-la. Choisissez quelques "
                  "cases, et vérifiez la preuve face au travail réel sur le terrain. Un autre superviseur "
                  "doit voir d'un coup d'œil qui est qualifié aujourd'hui. C'est un système de maîtrise "
                  "vivant, pas une décoration.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Qui fait quel travail", "icon": "person"}, {"label": "Niveau prouvé", "icon": "check"},
        {"label": "Les écarts", "icon": "warning", "tone": "bad"},
        {"label": "Pas la présence", "icon": "cross", "tone": "bad"}]},
    "p02": {"type": "icons", "items": [
        {"label": "Effectif, absences", "icon": "calendar"},
        {"label": "Compétence sur les étapes critiques", "icon": "shield"},
        {"label": "Un chemin pour progresser", "icon": "chartUp", "tone": "good"}]},
    "p03": {"type": "matrix", "cols": ["Objectif", "Vissage", "Test", "Emballage"], "note": "Illustration : chaque case est un niveau prouvé", "items": [
        {"label": "Personne A", "cells": [3, 4, 2, None], "with": 0},
        {"label": "Personne B", "cells": [1, 3, 3, 2], "with": 1},
        {"label": "Personne C", "cells": [None, 2, 4, 3], "with": 2}]},
    "p04": {"type": "steps", "items": [
        {"label": "Non formé", "sub": "L0"}, {"label": "Comprend", "sub": "L1"},
        {"label": "Supervisé", "sub": "L2"}, {"label": "Travaille seul", "sub": "L3"},
        {"label": "Forme les autres", "sub": "L4"}]},
    "p05": {"type": "flow", "items": [
        {"label": "Cartographier chaque étape + SOP", "icon": "clipboard"},
        {"label": "Repérer sécurité, qualité, client", "icon": "warning"},
        {"label": "Noter impact, difficulté, remplaçants", "icon": "scale"},
        {"label": "Minimum qualifié par équipe", "icon": "person", "tone": "good"}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Mise au point des objectifs", "sub": "Risque le plus élevé", "icon": "camera", "tone": "bad", "with": "example"},
            {"label": "Flashage du firmware", "sub": "Risque le plus élevé", "icon": "chip", "tone": "bad", "with": "example"},
            {"label": "Manutention des cartons", "sub": "Plus bas", "icon": "box", "with": "example"}]}},
    "p06": {"type": "icons", "items": [
        {"label": "Bref contrôle théorique", "icon": "clipboard", "with": 0},
        {"label": "Vrais cycles + une situation anormale", "icon": "search", "with": 1},
        {"label": "Date, évaluateur, résultat", "icon": "calendar", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Théorie : réussie", "icon": "clipboard", "tone": "good", "with": "example"},
            {"label": "Travail réel : scans défaillants ratés", "icon": "search", "tone": "bad", "with": "example"},
            {"label": "Elle reste au niveau 2", "icon": "person", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Réévaluer après un changement", "icon": "sequence", "with": 0},
        {"label": "Besoin = requis − prouvé", "icon": "count", "with": 1}],
        "then": {"type": "bars", "label": "", "note": "Un écart de 2", "unit": "opérateurs firmware qualifiés par équipe", "with": "example", "items": [
            {"label": "Nécessaires", "value": 4, "with": "example"},
            {"label": "Disponibles", "value": 2, "tone": "bad", "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Formation au poste", "icon": "person"}, {"label": "Évaluateur indépendant", "icon": "shield"},
        {"label": "Dojo", "sub": "Pratique sûre hors ligne", "icon": "tray"}, {"label": "One Point Lesson", "icon": "clipboard"}]},
    "p09": {"type": "timeline", "items": [
        {"label": "Cartographier les compétences, définir les niveaux, évaluer", "sub": "Jours 1–30", "icon": "clipboard"},
        {"label": "Former sur les écarts critiques", "sub": "31–60", "icon": "person"},
        {"label": "Certifier les remplaçants, élargir", "sub": "61–90", "icon": "check"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Couverture de qualification", "icon": "count"}, {"label": "Atteinte des compétences", "icon": "chartUp"},
        {"label": "Taux de polyvalence", "icon": "sequence"}, {"label": "Qualifications expirées", "icon": "clock", "tone": "bad"}],
        "then": {"type": "stat", "value": 75, "suffix": "%", "icon": "person", "label": "des postes critiques couverts",
                 "unit": "18 sur 24 : calculez-le par équipe", "with": "example"}},
    "p11": {"type": "matrix", "cols": ["Cartes", "Mise au point", "Test"], "note": "Après 90 jours. Mise au point + test en même temps : Bala et Deepa. Ensuite : un autre "
                                                                                                         "remplaçant en mise au point.", "items": [
        {"label": "Asha", "cells": [4, None, None], "with": 0},
        {"label": "Bala", "cells": [None, 3, None], "with": 1},
        {"label": "Chitra", "cells": [None, 3, 3], "with": 1},
        {"label": "Deepa", "cells": [None, None, 3], "with": 2}]},
    "p12": {"type": "icons", "items": [
        {"label": "Niveau", "icon": "person", "with": 0}, {"label": "Autorisation", "icon": "key", "with": 0},
        {"label": "Formation au SOP", "icon": "clipboard", "with": 0},
        {"label": "Changement de processus : réévaluer", "icon": "sequence", "with": 2}]},
    "p13": {"type": "icons", "items": [
        {"label": "Codes uniques", "icon": "barcode"}, {"label": "Traçabilité", "icon": "sequence"},
        {"label": "Rappels d'expiration", "icon": "clock"}, {"label": "Pas d'auto-approbation", "icon": "cross", "tone": "bad"}]},
    "p14": {"type": "timeline", "items": [
        {"label": "Effectif qualifié au démarrage", "sub": "Chaque jour", "icon": "person"},
        {"label": "Écarts, polyvalence, retards", "sub": "Chaque semaine", "icon": "calendar"},
        {"label": "Couverture, départs", "sub": "Chaque mois", "icon": "chartUp"},
        {"label": "Cohérence des évaluateurs", "sub": "Chaque trimestre", "icon": "scale"}]},
    "p15": {"type": "doc", "items": [
        {"label": "Matrice de compétences · Cellule 2 · Rev C", "icon": "label", "with": 0},
        {"label": "Compétence · rév. du SOP · niveau · expiration", "icon": "clipboard", "with": 0},
        {"label": "Évaluation : théorie, cycles, sécurité", "icon": "test", "with": 1},
        {"label": "Un plan de formation pour chaque écart", "icon": "calendar", "with": 2},
        {"label": "Auditée face au travail réel", "icon": "search", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Un opérateur a terminé le cours de formation mais n'a pas encore été évalué. Peut-on le "
                    "compter comme L3 ?",
        "options": ["Oui — le cours est terminé", "Non — le L3 demande une performance démontrée et évaluée",
                    "Oui, s'il est là depuis longtemps"],
        "correct": 1,
        "explanation": "La présence et l'ancienneté ne sont pas de la compétence. Le niveau 3 veut dire une "
                       "performance autonome prouvée par une évaluation avec preuves.",
        "q_script": "Vérification rapide. Un opérateur a terminé le cours de formation, mais n'a pas encore "
                    "été évalué. Peut-on le compter comme niveau trois ? Prenez quelques secondes.",
        "a_script": "Non. Le niveau trois demande une performance évaluée et prouvée. Suivre un cours n'est "
                    "pas la même chose qu'être qualifié.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Une seule personne de l'équipe est qualifiée sur la mise au point des objectifs, et la "
                    "production en dépend. Que doit faire le chef de cellule EN PREMIER ?",
        "options": ["Former tout le monde sur toutes les compétences", "Qualifier un remplaçant en mise au point comme priorité absolue",
                    "Demander à l'expert de ne jamais prendre de congé", "Former d'abord les compétences à faible risque car c'est plus rapide"],
        "correct": 1,
        "explanation": "Dépendre d'une seule personne sur une compétence critique est le plus grand risque. "
                       "Qualifiez d'abord un remplaçant là, puis élargissez la polyvalence.",
        "q_script": "Encore une, et cette fois c'est un scénario. Une seule personne de l'équipe est "
                    "qualifiée sur la mise au point des objectifs, et toute la cellule en dépend. Que doit "
                    "faire le chef de cellule en premier ? Réfléchissez.",
        "a_script": "Qualifiez d'abord un remplaçant en mise au point. Un point de défaillance unique sur une "
                    "compétence critique est le plus grand risque. Puis élargissez la polyvalence.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
