"""x_matrix in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh x_matrix_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "xm_fr"
NAME = "x_matrix_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Hoshin Kanri": "Hochine Kanri",
    "X-Matrix": "ixe matrix",
    "Yamazumi": "Yamazoumi",
    "Kaizen": "Kaïzène",
    "RACI": "rassi",
    "KPI": "ka pé i",
    "BOM": "bé o emme",
    "SMED": "smède",
    "IT": "i té",
    "Plan": "plane",
    "Check": "tchèk",
    "Act": "akte",
    "Do": "dou",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Quarante projets d'amélioration. Toutes les équipes occupées. Pourtant, la livraison "
    "glissait encore, trimestre après trimestre. Ça vous dit quelque chose ? Dans cette "
    "leçon, vous allez découvrir la X-Matrix, le cœur sur une page du Hoshin Kanri. Vous "
    "verrez comment relier quelques grands objectifs aux projets et aux chiffres qui les "
    "prouvent. Nous suivrons Arjun, directeur des opérations dans une usine d'électronique, "
    "qui transforme un portefeuille chargé en un portefeuille ciblé."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Choisissez quelques vraies priorités, pas une liste de "
    "souhaits. Reliez chaque objectif à un projet, un KPI, et un seul responsable. Et faites "
    "des revues honnêtes, car ce sont les chiffres qui doivent bouger, pas seulement le "
    "tableau. Voici votre action pour cette semaine. Écrivez un objectif pour votre zone sous "
    "forme de résultat, pas d'activité. Bravo d'avoir terminé cette leçon. Ensuite, vous "
    "découvrirez le Yamazumi, pour équilibrer le travail sur votre ligne."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "X-Matrix et Hoshin Kanri",
        "points": [("Toute votre stratégie sur une page", "met toute votre stratégie"),
                   ("Objectifs → buts → projets → cibles → responsables", "Elle relie les objectifs à long terme"),
                   ("Une courte liste d'actions réelles", "Son rôle est de transformer"),
                   ("Pas un tableau à afficher au mur", "Ce n'est pas un tableau coloré")],
        "example": "Arjun veut une livraison fiable et moins de défauts. Peut-il suivre ce but jusqu'au "
                   "travail sur le terrain ?",
        "example_cue": "Arjun veut une livraison fiable",
        "script": "Voici l'idée centrale. La X-Matrix met toute votre stratégie sur une page. Elle relie "
                  "les objectifs à long terme, les buts de l'année, les projets d'amélioration, les cibles "
                  "mesurables, et les responsables derrière eux. Son rôle est de transformer la stratégie "
                  "en une courte liste d'actions réelles. Ce n'est pas un tableau coloré à accrocher au "
                  "mur. Arjun veut une livraison fiable et moins de défauts. Peut-il suivre ce but jusqu'au "
                  "travail sur le terrain ? D'abord, d'où vient la méthode ?",
    },
    {
        "key": "p02", "num": 2, "title": "Origines et alignement",
        "points": [("Hoshin Kanri : le management par la direction", "Grossièrement, il veut dire"),
                   ("Aligne la direction et le travail quotidien", "Il aligne la direction"),
                   ("Limiter les priorités à ce que vous pouvez financer", "Limitez donc vos priorités"),
                   ("Dans les deux sens, pas du haut vers le bas", "Et gardez le dialogue")],
        "example": "Le site d'Arjun menait des dizaines de Kaizen locaux — seuls quelques-uns aidaient "
                   "vraiment la livraison client.",
        "example_cue": "Son site menait des dizaines",
        "script": "Le Hoshin Kanri est une approche japonaise. Grossièrement, il veut dire management par "
                  "la direction. Il aligne la direction que vous prenez avec ce que vous faites vraiment "
                  "chaque jour. La X-Matrix est simplement l'image de cet alignement. Voici le piège qu'a "
                  "trouvé Arjun. Son site menait des dizaines de Kaizen locaux. Seuls quelques-uns aidaient "
                  "vraiment la livraison client. Limitez donc vos priorités à ce que vous pouvez financer. "
                  "Et gardez le dialogue dans les deux sens, pas du haut vers le bas. Maintenant, que "
                  "met-on sur la page ?",
    },
    {
        "key": "p03", "num": 3, "title": "Quatre quadrants clés",
        "points": [("Objectifs de rupture : 3–5 ans", "D'abord, les objectifs de rupture"),
                   ("Objectifs annuels : cette année", "Ensuite, les objectifs annuels"),
                   ("Projets d'amélioration", "Troisièmement, les projets d'amélioration"),
                   ("KPI et cibles : la preuve", "Quatrièmement, les KPI et les cibles")],
        "example": "La chaîne d'Arjun va de la qualité de classe mondiale jusqu'à une cible de rendement.",
        "example_cue": "La chaîne d'Arjun va",
        "script": "Une X-Matrix typique a quatre parties reliées. D'abord, les objectifs de rupture, à "
                  "trois à cinq ans. Ensuite, les objectifs annuels, le progrès nécessaire cette année. "
                  "Troisièmement, les projets d'amélioration, le travail qui change la performance. "
                  "Quatrièmement, les KPI et les cibles, la preuve que ça marche. Les responsables sont à "
                  "côté, dans une grille des responsabilités. Les mises en page varient selon le modèle, "
                  "alors ajoutez toujours une légende. La chaîne d'Arjun va de la qualité de classe "
                  "mondiale jusqu'à une cible de rendement. Commençons par le haut.",
    },
    {
        "key": "p04", "num": 4, "title": "Objectifs de rupture",
        "points": [("Quelques grands résultats : 3 à 5", "Choisissez-en trois à cinq"),
                   ("Résultat, horizon, référence actuelle", "Énoncez le résultat"),
                   ("Repérer les objectifs qui se contredisent", "Et repérez les objectifs")],
        "example": "Le résultat d'Arjun : réduire de deux tiers les retours clients, tout en augmentant la "
                   "production.",
        "example_cue": "Arjun a écrit un résultat clair",
        "script": "Les objectifs de rupture nomment quelques grands résultats, au-delà de l'amélioration "
                  "normale du quotidien. Choisissez-en trois à cinq, pas une liste de souhaits. Énoncez le "
                  "résultat, l'horizon de temps, et la référence actuelle. Et repérez les objectifs qui se "
                  "contredisent, comme la vitesse face à la sécurité. Arjun a écrit un résultat clair. "
                  "Réduire de deux tiers les retours clients, tout en augmentant la production. Remarquez "
                  "que c'est un résultat, pas une activité. Vous pouvez le mesurer. Alors, comment le "
                  "découper pour cette année ?",
    },
    {
        "key": "p05", "num": 5, "title": "Objectifs annuels",
        "points": [("Des résultats mesurables pour cette année", "Les objectifs annuels transforment"),
                   ("Référence, cible, période, source de données", "Définissez la référence"),
                   ("Catchball : tester la faisabilité ensemble", "Puis utilisez le catchball")],
        "example": "Année un : une partie de la baisse des retours, convenue après étude des défaillances "
                   "terrain.",
        "example_cue": "Pour l'année un",
        "script": "Les objectifs annuels transforment cette direction en résultats mesurables cette année. "
                  "Ne distribuez pas simplement des pourcentages ronds. Définissez la référence, la cible, "
                  "la période et la source de données. Gardez la liste courte. Puis utilisez le catchball. "
                  "C'est l'aller-retour où les équipes vérifient si une cible est vraiment faisable. Pour "
                  "l'année un, Arjun vise une partie de la baisse, pas la totalité. Ses équipes l'ont "
                  "convenue après avoir étudié les défaillances terrain. Alors, quels projets vous y "
                  "mèneront ?",
    },
    {
        "key": "p06", "num": 6, "title": "Projets d'amélioration",
        "points": [("Problème, périmètre, responsable, jalons, vérification", "Un bon projet a"),
                   ("Plus d'inspection = rarement une rupture", "Ajouter de l'inspection"),
                   ("Choisir sur preuves : impact face à l'effort", "Choisissez les projets sur preuves")],
        "example": "Un verrouillage code-barres contre la BOM bloque les mauvais composants — le succès "
                   "n'est déclaré que quand les tests et les données de défauts concordent.",
        "example_cue": "Sur la ligne de téléphones d'Arjun",
        "script": "Les projets sont les changements qui font bouger vos cibles annuelles. Un bon projet a "
                  "un énoncé de problème, un périmètre, un responsable, des jalons, et un moyen de vérifier "
                  "les résultats. Voici une erreur fréquente. Ajouter de l'inspection apporte rarement une "
                  "rupture. Choisissez les projets sur preuves, et pesez l'impact face à l'effort, au coût "
                  "et au risque. Sur la ligne de téléphones d'Arjun, un verrouillage code-barres contre la "
                  "BOM bloque les mauvais composants. Mais il ne déclare le succès que quand les tests et "
                  "les données de défauts concordent. Comment saurez-vous que ça marche ?",
    },
    {
        "key": "p07", "num": 7, "title": "KPI avancés et retardés",
        "points": [("Retardés : les résultats déjà obtenus", "Les indicateurs retardés mesurent"),
                   ("Avancés : les conditions qui les prédisent", "Les indicateurs avancés mesurent"),
                   ("Définir dénominateur et source de données", "Définissez le dénominateur de chacun"),
                   ("Ne pas récompenser des chiffres redéfinis", "Et ne récompensez jamais")],
        "example": "Sur la ligne d'Arjun, 98 % des unités passent du premier coup.",
        "example_cue": "Sur la ligne d'Arjun",
        "script": "C'est le rôle des KPI. Les indicateurs retardés mesurent les résultats déjà obtenus, "
                  "comme le rendement au premier passage, les retours et la livraison à temps. Les "
                  "indicateurs avancés mesurent les conditions qui les prédisent, comme les audits, les "
                  "contrôles de réglage et la formation. Il vous faut les deux. Définissez le dénominateur "
                  "de chacun et sa source de données. Et ne récompensez jamais un chiffre qui ne s'est "
                  "amélioré que parce que quelqu'un a changé sa définition. Sur la ligne d'Arjun, "
                  "quatre-vingt-dix-huit pour cent des unités passent du premier coup. Mais avec quelle "
                  "force chaque projet fait-il bouger chaque chiffre ?",
    },
    {
        "key": "p08", "num": 8, "title": "Force de corrélation",
        "points": [("Les symboles montrent la force du lien", "La matrice utilise des symboles"),
                   ("Convenir d'abord de la légende", "convenez d'abord de votre légende"),
                   ("Noter le lien, pas l'importance", "Notez le lien"),
                   ("Chercher les trous et les prétentions excessives", "Puis cherchez les trous")],
        "example": "Le verrouillage de gabarit d'Arjun réduit fortement les mauvaises pièces — et touche à "
                   "peine la consommation d'énergie.",
        "example_cue": "Le verrouillage de gabarit d'Arjun",
        "script": "La matrice utilise des symboles pour montrer à quel point deux éléments sont liés. "
                  "Souvent, un cercle plein veut dire fort, et un cercle vide veut dire moyen. Aucune "
                  "convention n'est universelle, alors convenez d'abord de votre légende. Notez le lien, "
                  "pas l'importance que l'élément semble avoir. Puis cherchez les trous. Y a-t-il un "
                  "objectif annuel sans aucun projet derrière ? Y a-t-il un projet qui prétend tout aider ? "
                  "Le verrouillage de gabarit d'Arjun réduit fortement les mauvaises pièces. Il touche à "
                  "peine la consommation d'énergie. Alors, qui s'assure que ça se fait ?",
    },
    {
        "key": "p09", "num": 9, "title": "Responsabilité et catchball",
        "points": [("Un seul responsable pour chacun", "Donnez à chaque objectif"),
                   ("Nommer les équipes en appui", "Nommez aussi les équipes en appui"),
                   ("RACI : réalise, rend compte, consulté, informé", "Qui réalise"),
                   ("Le responsable a besoin d'un budget et d'autorité", "Assurez-vous que votre responsable")],
        "example": "Automatisation du test des décodeurs : ingénierie, production, qualité et IT aident — un "
                   "seul chef de projet reste responsable.",
        "example_cue": "Sur l'automatisation du test des décodeurs",
        "script": "Les objectifs échouent quand la responsabilité est floue. Donnez à chaque objectif et à "
                  "chaque projet un seul responsable qui rend compte. Nommez aussi les équipes en appui. "
                  "C'est l'idée derrière le RACI. Qui réalise, qui rend compte, qui est consulté, et qui "
                  "est informé ? Assurez-vous que votre responsable a le budget et l'autorité pour lever "
                  "les obstacles. Sur l'automatisation du test des décodeurs d'Arjun, l'ingénierie, la "
                  "production, la qualité et l'IT aident. Mais un seul chef de projet reste responsable. Si "
                  "ça bloque, vous savez à qui demander.",
    },
    {
        "key": "p10", "num": 10, "title": "Atelier de construction",
        "points": [("Rassembler d'abord les preuves", "Avant l'atelier"),
                   ("Périmètre, référence, objectifs, résultats", "Convenez du périmètre"),
                   ("Des projets à fort impact, chacun avec un KPI", "Choisissez des projets à fort impact"),
                   ("Noter les liens, nommer les responsables, fixer les revues", "Enfin, notez les liens")],
        "example": "Dans l'atelier d'Arjun, trois services ont relié des projets à une seule cible de "
                   "livraison.",
        "example_cue": "Dans l'atelier d'Arjun",
        "script": "Construisez la matrice de la stratégie jusqu'au travail réel. Avant l'atelier, "
                  "rassemblez des preuves sur les clients, la performance, la capacité et le coût. Puis "
                  "avancez pas à pas. Convenez du périmètre et de la référence. Choisissez quelques "
                  "objectifs de rupture. Définissez les résultats de cette année. Choisissez des projets à "
                  "fort impact, et donnez à chacun un KPI. Enfin, notez les liens, nommez les responsables, "
                  "et fixez un rythme de revue. Dans l'atelier d'Arjun, trois services ont relié des "
                  "projets à une seule cible de livraison. À quoi ressemble votre matrice terminée ?",
    },
    {
        "key": "p11", "num": 11, "title": "Exemple détaillé",
        "points": [("Livraison 90 % → 98 %", "la livraison à temps passe"),
                   ("Rendement au premier passage → 99 %", "Le rendement au premier passage monte"),
                   ("Changement de série 50 → 20 minutes", "Le changement de série passe"),
                   ("Planification, qualité, ingénierie : un chacun", "La planification porte la livraison")],
        "example": "Projets : un tableau de préparation, un verrouillage code-barres et un pilote SMED.",
        "example_cue": "Les projets sont",
        "script": "Voici la matrice terminée d'Arjun. Les chiffres sont des hypothèses de formation. Ses "
                  "ruptures sont une livraison fiable, la prévention des défauts, et une capacité flexible. "
                  "Cette année, la livraison à temps passe de quatre-vingt-dix à quatre-vingt-dix-huit pour "
                  "cent. Le rendement au premier passage monte à quatre-vingt-dix-neuf. Le changement de "
                  "série passe de cinquante minutes à vingt. Les projets sont un tableau de préparation, un "
                  "verrouillage code-barres, et un pilote SMED. La planification porte la livraison, la "
                  "qualité le rendement, et l'ingénierie le changement de série. Voyez-vous chaque ligne de "
                  "visée ?",
    },
    {
        "key": "p12", "num": 12, "title": "Rythme de revue — PDCA",
        "points": [("Un outil vivant : Plan, Do, Check, Act", "Plan, Do, Check"),
                   ("Quotidien / hebdomadaire : exceptions, jalons", "Chaque jour et chaque semaine"),
                   ("Mensuel : tendances des KPI et risques", "Chaque mois, revoyez"),
                   ("Trimestriel : soutient-il encore la stratégie ?", "Chaque trimestre, demandez")],
        "example": "Le rendement a stagné même après la formation — Arjun a donc vérifié si la maîtrise du "
                   "processus avait vraiment changé.",
        "example_cue": "Le rendement a stagné",
        "script": "La X-Matrix est un outil vivant, pas une affiche. Revoyez-la avec Plan, Do, Check, Act. "
                  "Comparez les résultats aux cibles, trouvez les causes des écarts, et adaptez. Chaque "
                  "jour et chaque semaine, suivez les exceptions et les jalons. Chaque mois, revoyez les "
                  "tendances des KPI et les risques. Chaque trimestre, demandez si chaque projet soutient "
                  "encore la stratégie. Voici ce qu'a appris Arjun. Le rendement a stagné même après la fin "
                  "de la formation. Il a donc vérifié si la maîtrise du processus avait vraiment changé. "
                  "Quels pièges éviter ?",
    },
    {
        "key": "p13", "num": 13, "title": "À faire et à éviter",
        "points": [("Quelques résultats mesurables, des responsables clairs", "Alors gardez quelques"),
                   ("Vérifier les liens de cause et les moyens", "Vérifiez les liens de cause"),
                   ("Pas tout « fortement lié »", "ne marquez pas chaque projet"),
                   ("Projet terminé ≠ bénéfice obtenu", "Ne prenez pas un projet terminé")],
        "example": "Un projet a été marqué terminé, mais les réclamations sont restées stables.",
        "example_cue": "Un des projets d'Arjun",
        "script": "Une matrice devient vite de la paperasse morte. Trop d'objectifs, des mots vagues et des "
                  "liens non vérifiés suffisent. Alors gardez quelques résultats mesurables avec des "
                  "responsables clairs. Vérifiez les liens de cause et les moyens qui sont derrière. Mais "
                  "ne marquez pas chaque projet comme fortement lié à chaque KPI. Ne prenez pas un projet "
                  "terminé pour un bénéfice obtenu. Et ne réécrivez jamais une référence en douce. Un des "
                  "projets d'Arjun a été marqué terminé, mais les réclamations sont restées stables. "
                  "Comment prouveriez-vous la vraie valeur ?",
    },
    {
        "key": "p14", "num": 14, "title": "Calcul coût–bénéfice",
        "points": [("Livraison à temps = à temps ÷ total dû", "La livraison à temps est"),
                   ("Baisse relative = baisse ÷ ancien taux", "Une réduction relative est"),
                   ("Retour = investissement ÷ économies mensuelles", "Le retour sur investissement est")],
        "example": "Défauts de 2 % → 1,2 % paraît peu — c'est une baisse relative de 40 %. Le verrouillage "
                   "est rentabilisé en 6 mois.",
        "example_cue": "Des défauts qui passent de deux",
        "script": "Les bénéfices demandent des formules cohérentes, sinon personne n'y croira. La livraison "
                  "à temps est le nombre d'expéditions à temps sur le total dû. Une réduction relative est "
                  "la baisse divisée par l'ancien taux. Le retour sur investissement est l'investissement "
                  "divisé par les économies mensuelles vérifiées. Voici un piège que vous rencontrerez. Des "
                  "défauts qui passent de deux pour cent à un virgule deux, cela paraît peu. C'est en fait "
                  "une baisse relative de quarante pour cent. Et le verrouillage d'Arjun est rentabilisé en "
                  "six mois. Alors, comment commencer demain ?",
    },
    {
        "key": "p15", "num": 15, "title": "Feuille de route sur 90 jours",
        "points": [("Jours 1–30 : références, brouillon de matrice", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : catchball, projets, responsables", "Pendant les trente suivants"),
                   ("Jours 61–90 : vérifier les liens, revue, audit", "Pendant les trente derniers")],
        "example": "Quel résultat ? Quelle cible ? Quel projet ? Quel KPI ? Qui est responsable du résultat "
                   "?",
        "example_cue": "Quel résultat compte",
        "script": "Commencez par un pilote, et construisez l'habitude de revue avant de l'étendre partout. "
                  "Pendant les trente premiers jours, rassemblez les références et faites un brouillon de "
                  "la matrice. Pendant les trente suivants, faites le catchball, approuvez les projets, et "
                  "nommez les responsables. Pendant les trente derniers, vérifiez les liens, revoyez les "
                  "écarts, et auditez le résultat. Puis posez vos cinq questions. Quel résultat compte ? "
                  "Quelle cible le soutient ? Quel projet change le processus ? Quel KPI le prouve ? Et qui "
                  "est responsable du résultat ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Objectifs à long terme", "icon": "chartUp", "with": 1},
        {"label": "Buts de cette année", "icon": "calendar", "with": 1},
        {"label": "Projets d'amélioration", "icon": "wrench", "with": 1},
        {"label": "Cibles et responsables", "icon": "person", "tone": "good", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Management par la direction", "icon": "sequence", "with": 0},
        {"label": "La stratégie rejoint le travail quotidien", "icon": "calendar", "with": 1}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Des dizaines de Kaizen locaux", "sub": "Peu ont aidé la livraison", "icon": "stack", "with": "example"},
            {"label": "Quelques priorités financées", "sub": "Dans les deux sens, pas du haut vers le bas", "icon": "key", "with": 2}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Rupture", "sub": "3–5 ans", "icon": "chartUp", "with": 0},
        {"label": "Annuel", "sub": "Cette année", "icon": "calendar", "with": 1},
        {"label": "Projets", "sub": "Le travail", "icon": "wrench", "with": 2},
        {"label": "KPI et cibles", "sub": "La preuve", "icon": "check", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "3 à 5 grands résultats", "icon": "key", "with": 0},
        {"label": "Résultat, horizon, référence", "icon": "clipboard", "with": 1},
        {"label": "Objectifs qui se contredisent", "sub": "Vitesse contre sécurité", "icon": "scale", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 2, "suffix": "/3", "icon": "chartDown", "label": "de retours clients en moins",
                 "unit": "Tout en augmentant la production : un résultat, pas une activité", "with": "example"}},
    "p05": {"type": "doc", "items": [
        {"label": "Objectif annuel · Année 1", "icon": "label", "with": 0},
        {"label": "Référence · cible · période", "icon": "clipboard", "with": 1},
        {"label": "Source de données nommée", "icon": "search", "with": 1},
        {"label": "Catchball : est-ce faisable ?", "icon": "sequence", "with": 2},
        {"label": "Convenu à partir des défaillances terrain", "icon": "check", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Problème, périmètre, responsable", "icon": "clipboard", "with": 0},
        {"label": "Plus d'inspection", "sub": "Rarement une rupture", "icon": "search", "tone": "bad", "with": 1},
        {"label": "Impact face à l'effort", "icon": "scale", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Scanner le code-barres de la pièce", "icon": "barcode", "with": "example"},
            {"label": "Vérifier contre la BOM", "icon": "clipboard", "with": "example"},
            {"label": "Mauvaise pièce ? Bloquée", "icon": "lock", "tone": "good", "with": "example"}]}},
    "p07": {"type": "versus", "items": [
        {"label": "Retardés", "sub": "Rendement, retours, livraison", "icon": "chartUp", "with": 0},
        {"label": "Avancés", "sub": "Audits, réglages, formation", "icon": "search", "with": 1}],
        "then": {"type": "stat", "value": 98, "suffix": "%", "icon": "check", "label": "passent du premier coup",
                 "unit": "Rendement au premier passage sur la ligne d'Arjun", "with": "example"}},
    "p08": {"type": "matrix", "prefix": "check", "cols": ["Mauvaises pièces", "Rendement", "Énergie"],
            "note": "Notez le lien, pas l'importance", "items": [
        {"label": "Verrouillage", "cells": [3, 3, None], "with": "example"},
        {"label": "Pilote SMED", "cells": [None, None, 3], "with": "example"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Réalise", "icon": "wrench", "with": 2},
        {"label": "Rend compte", "sub": "Un seul responsable", "icon": "person", "tone": "good", "with": 0},
        {"label": "Consulté", "icon": "search", "with": 2},
        {"label": "Informé", "icon": "clipboard", "with": 2}]},
    "p10": {"type": "steps", "items": [
        {"label": "Preuves", "with": 0}, {"label": "Périmètre, référence", "with": 1},
        {"label": "Objectifs", "with": 1}, {"label": "Projets + KPI", "with": 2},
        {"label": "Liens, responsables", "with": 3}, {"label": "Rythme de revue", "with": 3}]},
    "p11": {"type": "compare", "before": {"label": "Aujourd'hui", "value": 90}, "after": {"label": "Cette année", "value": 98},
            "suffix": "%", "unit": "livraison à temps", "note": "La planification en est responsable", "with": 0,
            "then": {"type": "icons", "with": "example", "items": [
                {"label": "Tableau de préparation", "sub": "Livraison", "icon": "chartUp", "with": "example"},
                {"label": "Verrouillage code-barres", "sub": "Rendement à 99 %", "icon": "barcode", "with": "example"},
                {"label": "Pilote SMED", "sub": "Changement de série 50 → 20 min", "icon": "clock", "with": "example"}]}},
    "p12": {"type": "timeline", "items": [
        {"label": "Exceptions, jalons", "sub": "Quotidien / hebdomadaire", "icon": "calendar", "with": 1},
        {"label": "Tendances des KPI, risques", "sub": "Mensuel", "icon": "chartUp", "with": 2},
        {"label": "Toujours dans la stratégie ?", "sub": "Trimestriel", "icon": "search", "with": 3}]},
    "p13": {"type": "icons", "items": [
        {"label": "Peu de résultats, responsables clairs", "icon": "person", "tone": "good", "with": 0},
        {"label": "Vérifier liens + moyens", "icon": "check", "tone": "good", "with": 1},
        {"label": "Tout « fort »", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Terminé ≠ obtenu", "icon": "warning", "tone": "bad", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Avant", "value": 2}, "after": {"label": "Après", "value": 1.2},
            "decimals": 1, "suffix": "%", "unit": "taux de défauts", "note": "Une baisse relative de 40 % · retour en 6 mois", "with": "example"},
    "p15": {"type": "timeline", "items": [
        {"label": "Références, brouillon de matrice", "sub": "Jours 1–30", "icon": "clipboard", "with": 0},
        {"label": "Catchball, projets, responsables", "sub": "31–60", "icon": "person", "with": 1},
        {"label": "Vérifier les liens, revue, audit", "sub": "61–90", "icon": "search", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Lequel de ces éléments va dans la dimension KPI / cibles, et non dans les objectifs de "
                    "rupture ?",
        "options": ["Devenir de classe mondiale en qualité produit", "Porter le rendement au premier passage à 99 % cette année", "Enchanter chaque client"],
        "correct": 1,
        "explanation": "Une cible est mesurable, avec un chiffre et une date. Les autres sont des objectifs de "
                       "direction, pas des mesures.",
        "q_script": "Vérification rapide. Lequel de ces éléments va dans les KPI et les cibles, plutôt que "
                    "dans les objectifs de rupture ? Prenez quelques secondes.",
        "a_script": "Porter le rendement au premier passage à quatre-vingt-dix-neuf pour cent cette année. "
                    "Une cible porte un chiffre et une date. Les deux autres sont des directions, pas des "
                    "mesures.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "L'objectif annuel de livraison à temps d'une usine n'a aucun projet lié. Que doit faire "
                    "l'équipe EN PREMIER ?",
        "options": ["Marquer un lien fort avec le projet le plus proche", "Trouver ou lancer un projet capable de faire bouger la livraison — ou repenser "
                                                                                                                                                          "l'objectif",
                    "Le laisser ; le KPI s'améliorera tout seul"],
        "correct": 1,
        "explanation": "Un objectif sans projet d'appui est un trou. Comblez-le avec du vrai travail, ou révisez "
                       "l'objectif ; ne remplissez jamais la case avec un lien sans mécanisme.",
        "q_script": "Encore une, et cette fois c'est un scénario. L'objectif annuel de livraison d'une usine "
                    "n'a aucun projet lié. Que doit faire l'équipe en premier ? Réfléchissez.",
        "a_script": "Trouvez ou lancez un projet qui peut vraiment faire bouger la livraison, ou repensez "
                    "l'objectif. Dessiner un lien sans vrai mécanisme ne fait que cacher le trou.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
