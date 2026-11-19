"""yamazumi in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh yamazumi_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "yz_fr"
NAME = "yamazumi_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Zero Defects": "zirô difèctse",
    "Yamazumi": "Yamazoumi",
    "Heijunka": "Héïdjounka",
    "Gemba": "Guemba",
    "TAKT": "takte",
    "ECRS": "eu cé erre esse",
    "SMED": "smède",
    "ESD": "eu esse dé",
    "SOP": "esse o pé",
    "A": "a",
    "B": "bé",
    "C": "cé",
    "D": "dé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Chaque après-midi, la cellule de décodeurs de Meera prend du retard. Trois opérateurs "
    "attendent, pendant qu'un seul croule sous les vis. Personne n'est paresseux. Le travail "
    "est simplement empilé de façon inégale. Dans cette leçon, vous allez découvrir le "
    "Yamazumi, un diagramme simple qui montre exactement où le travail s'accumule. Et vous "
    "verrez comment Meera rééquilibre sa ligne avec des données réelles."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Mesurez le vrai travail, pas le meilleur cas. Empilez-le "
    "face au TAKT pour voir où il s'accumule. Et rééquilibrez avec soin, jamais au détriment "
    "de la sécurité ou de la qualité. Votre action cette semaine : chronométrez un poste de "
    "votre ligne, et tracez sa barre face au TAKT. Bravo d'avoir terminé cette leçon. "
    "Ensuite, vous découvrirez Zero Defects, la dernière leçon du cours."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le Yamazumi",
        "points": [("Un diagramme en barres empilées du travail par poste", "C'est un diagramme en barres empilées"),
                   ("En japonais : « s'empiler »", "Le mot japonais veut dire"),
                   ("Chaque barre : les tâches d'un opérateur", "Chaque barre empile"),
                   ("Au-dessus de la ligne du TAKT = ne peut pas suivre", "Toute barre au-dessus")],
        "example": "La cellule de décodeurs de Meera : quatre opérateurs, quatre barres empilées, une ligne "
                   "du TAKT.",
        "example_cue": "Voici la cellule de Meera",
        "script": "Alors, qu'est-ce que le Yamazumi ? C'est un diagramme en barres empilées du travail à "
                  "chaque poste. Le mot japonais veut dire s'empiler. Chaque barre empile les tâches d'un "
                  "opérateur, en secondes. Une ligne horizontale marque le temps TAKT, le rythme dont votre "
                  "client a besoin. Toute barre au-dessus de cette ligne ne peut pas suivre. Il transforme "
                  "vos études de temps en conversation sur l'équilibrage. Voici la cellule de Meera, avec "
                  "quatre opérateurs. Voyez-vous déjà le problème ?",
    },
    {
        "key": "p02", "num": 2, "title": "Objectif et bénéfices",
        "points": [("Déséquilibre, attente, surcharge d'un coup d'œil", "Vous voyez le déséquilibre"),
                   ("Une base objective pour l'effectif", "Il vous donne une base objective"),
                   ("Montre où la polyvalence aide", "Il montre aussi où"),
                   ("Ne remplace jamais les vérifications d'ingénierie", "Mais le Yamazumi ne remplace jamais")],
        "example": "Un opérateur attend pendant qu'un autre se bat avec un long vissage — déplacer une "
                   "petite tâche pourrait fluidifier le flux.",
        "example_cue": "Dans la cellule de Meera",
        "script": "Pourquoi s'en donner la peine ? Parce que le diagramme rend les problèmes visibles. Vous "
                  "voyez le déséquilibre, l'attente et la surcharge d'un coup d'œil. Il vous donne une base "
                  "objective pour l'effectif, pas une intuition. Il montre aussi où la polyvalence "
                  "aiderait. Dans la cellule de Meera, un opérateur attend pendant qu'un autre se bat avec "
                  "un long vissage. Déplacer une petite tâche pourrait fluidifier le flux. Mais le Yamazumi "
                  "ne remplace jamais les vérifications d'ingénierie. D'abord, il vous faut trois temps "
                  "clés.",
    },
    {
        "key": "p03", "num": 3, "title": "TAKT, cycle et contenu de travail",
        "points": [("TAKT : temps net ÷ bonnes unités nécessaires", "C'est votre temps net disponible"),
                   ("Temps de cycle : à quelle fréquence une unité sort", "Le temps de cycle est"),
                   ("Contenu de travail : la somme des tâches manuelles", "Le contenu de travail est"),
                   ("Garder le temps machine à part", "Gardez le temps machine à part")],
        "example": "420 minutes nettes ÷ 840 unités = TAKT de 30 secondes. Le poste B demande 35.",
        "example_cue": "Meera a quatre cent",
        "script": "D'abord, le temps TAKT. C'est votre temps net disponible divisé par les bonnes unités "
                  "dont le client a besoin. Le temps de cycle est la fréquence à laquelle une unité sort "
                  "réellement d'un poste. Le contenu de travail est la somme des tâches manuelles sur une "
                  "unité. Gardez le temps machine à part. Meera a quatre cent vingt minutes nettes. La "
                  "demande est de huit cent quarante unités. Cela fait un TAKT de trente secondes. Son "
                  "poste B demande trente-cinq. Peut-il suivre seul ?",
    },
    {
        "key": "p04", "num": 4, "title": "Structure du diagramme",
        "points": [("Une barre par opérateur ou par poste", "Vous tracez une barre verticale"),
                   ("Secondes sur le côté, ligne du TAKT en travers", "L'axe vertical"),
                   ("Chaque bloc = une tâche, dans l'ordre", "Chaque bloc de couleur"),
                   ("Les couleurs montrent des types de tâches, pas des notes", "Les couleurs montrent des types de tâches")],
        "example": "Le poste A empile 22 secondes ; le poste B atteint 35, bien au-dessus de la ligne.",
        "example_cue": "Dans le diagramme de Meera",
        "script": "Construisons maintenant le diagramme. Vous tracez une barre verticale par opérateur ou "
                  "par poste. L'axe vertical montre les secondes. Une ligne horizontale marque le TAKT. "
                  "Chaque bloc de couleur est une tâche, empilée dans l'ordre du travail standard. Les "
                  "couleurs montrent des types de tâches, jamais des notes de performance. Étiquetez chaque "
                  "barre avec son échantillon et son équipe. Dans le diagramme de Meera, le poste A empile "
                  "vingt-deux secondes. Le poste B atteint trente-cinq, bien au-dessus de la ligne. Alors, "
                  "d'où viennent ces chiffres ?",
    },
    {
        "key": "p05", "num": 5, "title": "Une étude de temps fiable",
        "points": [("Définir où chaque tâche commence et finit", "Définissez où chaque tâche"),
                   ("De nombreux cycles, sur plusieurs équipes", "Observez de nombreux cycles"),
                   ("Noter marches, arrêts, changements de série", "Notez aussi les marches"),
                   ("Séparer temps machine et temps manuel", "Séparez le temps machine")],
        "example": "Le flashage du firmware tourne pendant que l'opérateur visse, donc Meera chronomètre "
                   "chaque élément séparément.",
        "example_cue": "Dans la cellule de Meera",
        "script": "Ils viennent de l'observation réelle au Gemba. Votre diagramme ne vaut que ce que valent "
                  "ses données. Définissez où chaque tâche commence et finit. Observez de nombreux cycles, "
                  "sur plusieurs équipes, pas seulement le plus rapide. Notez aussi les marches, les "
                  "micro-arrêts et les changements de série. Séparez le temps machine de la manipulation "
                  "manuelle. Dans la cellule de Meera, le flashage du firmware tourne pendant que "
                  "l'opérateur visse. Elle chronomètre donc chaque élément séparément. Quels types de "
                  "travail allez-vous trouver ?",
    },
    {
        "key": "p06", "num": 6, "title": "Classer le travail",
        "points": [("Valeur ajoutée : ce que veut le client", "Le travail à valeur ajoutée change"),
                   ("Nécessaire sans valeur ajoutée : contrôles, traçabilité", "Le travail nécessaire sans valeur ajoutée"),
                   ("Gaspillage : chercher, marcher, attendre", "Le gaspillage, c'est chercher"),
                   ("ECRS — mais garder les contrôles qualité et sécurité", "Remettez en question chaque étape")],
        "example": "L'opérateur de Meera marche 5 secondes pour chercher les vis. Des bacs au point "
                   "d'utilisation suppriment ce gaspillage.",
        "example_cue": "L'opérateur de Meera marche",
        "script": "Vous trouverez trois types de travail. Le travail à valeur ajoutée change le produit "
                  "comme le client le veut. Le travail nécessaire sans valeur ajoutée couvre les contrôles "
                  "obligatoires et la traçabilité. Le gaspillage, c'est chercher, marcher et attendre. "
                  "Remettez en question chaque étape avec ECRS : éliminer, combiner, réordonner, "
                  "simplifier. Mais ne supprimez jamais un contrôle qualité ou sécurité obligatoire. "
                  "L'opérateur de Meera marche cinq secondes pour chercher les vis. Des bacs au point "
                  "d'utilisation suppriment ce gaspillage. Vous pouvez maintenant cartographier l'état "
                  "actuel.",
    },
    {
        "key": "p07", "num": 7, "title": "Construire l'état actuel",
        "points": [("Demande approuvée → TAKT", "Partez de la demande approuvée"),
                   ("Une barre par poste, ligne du TAKT tracée", "Construisez une barre par poste"),
                   ("Comparer le diagramme à la réalité", "Puis parcourez le terrain"),
                   ("Une barre courte ≠ de la capacité libre", "une barre courte ne prouve pas")],
        "example": "TAKT de 30 s : A = 22, B = 35, C = 27, D = 20. B dépasse de 5 secondes — la première "
                   "priorité.",
        "example_cue": "Voici l'état actuel de Meera",
        "script": "Partez de la demande approuvée, et calculez le TAKT. Construisez une barre par poste, "
                  "empilez chaque tâche, et tracez la ligne du TAKT. Puis parcourez le terrain et comparez "
                  "le diagramme à la réalité. Voici l'état actuel de Meera. Le poste A tourne à vingt-deux "
                  "secondes, et le B à trente-cinq. Le C tourne à vingt-sept, et le D à vingt. Le poste B "
                  "dépasse le TAKT de cinq secondes. C'est sa première priorité. Et rappelez-vous, une "
                  "barre courte ne prouve pas que vous avez de la capacité libre.",
    },
    {
        "key": "p08", "num": 8, "title": "Équilibrage de ligne",
        "points": [("Déplacer des tâches ou améliorer les méthodes", "Équilibrer veut dire déplacer"),
                   ("Pas des barres parfaitement égales", "L'objectif n'est pas des barres parfaitement égales"),
                   ("Respecter implantation, séquence, compétences, contrôles", "Vous devez respecter l'implantation"),
                   ("Essayer ECRS avant d'ajouter des personnes", "Essayez ECRS")],
        "example": "Une tâche d'étiquetage de 5 secondes passe de B à D : B = 30, D = 25. Puis pilote et "
                   "nouvelle mesure.",
        "example_cue": "Meera trouve une tâche d'étiquetage",
        "script": "Équilibrer veut dire déplacer des tâches possibles, ou améliorer les méthodes, pour que "
                  "chaque poste tienne le rythme. L'objectif n'est pas des barres parfaitement égales. Vous "
                  "devez respecter l'implantation, la séquence des tâches, les gabarits, les compétences et "
                  "les contrôles qualité. Essayez ECRS avant d'ajouter des personnes. Meera trouve une "
                  "tâche d'étiquetage de cinq secondes qui ne dépend pas du reste du travail de B. Elle la "
                  "déplace au poste D. B descend à trente, et D monte à vingt-cinq. Puis elle fait un "
                  "pilote et mesure de nouveau.",
    },
    {
        "key": "p09", "num": 9, "title": "Effectif et efficacité",
        "points": [("Travail manuel ÷ TAKT, arrondi au-dessus", "Additionnez le travail manuel"),
                   ("Efficacité d'équilibrage : travail face à capacité", "L'efficacité d'équilibrage compare"),
                   ("Un plancher de planification, pas une promesse", "Prenez-le comme un plancher de planification"),
                   ("Prouver la production avant de réduire l'effectif", "Ne réduisez jamais le nombre d'opérateurs")],
        "example": "104 secondes de travail avec un TAKT de 30 secondes = 4 opérateurs ; efficacité "
                   "d'environ 87 %.",
        "example_cue": "La cellule de Meera a cent",
        "script": "De combien de personnes avez-vous vraiment besoin ? Additionnez le travail manuel, "
                  "divisez par le TAKT, et arrondissez au-dessus. La cellule de Meera a cent quatre "
                  "secondes de travail. Avec un TAKT de trente secondes, cela fait quatre opérateurs. "
                  "L'efficacité d'équilibrage compare le travail affecté à la capacité de l'effectif. La "
                  "sienne est d'environ quatre-vingt-sept pour cent. Prenez-le comme un plancher de "
                  "planification, pas comme une promesse. Ne réduisez jamais le nombre d'opérateurs avant "
                  "d'avoir prouvé la bonne production, en sécurité et de façon constante.",
    },
    {
        "key": "p10", "num": 10, "title": "Goulots et machines",
        "points": [("Toute barre longue n'est pas un goulot opérateur", "Toute barre longue"),
                   ("Les machines partagées demandent leur propre vérification", "Les machines peuvent tourner"),
                   ("Séparer manuel, automatique, chargement, attente", "Séparez le temps manuel"),
                   ("Ajuster pour disponibilité, changements, rendement", "Puis ajustez pour la disponibilité")],
        "example": "Deux testeurs audio : 160 unités/heure sur le papier — environ 140 bonnes en réalité.",
        "example_cue": "Regardez les deux testeurs",
        "script": "Voici une erreur fréquente. Toute barre longue n'est pas un goulot opérateur. Les "
                  "machines peuvent tourner pendant que les personnes travaillent, donc l'équipement "
                  "partagé demande sa propre vérification de capacité. Séparez le temps manuel, le cycle "
                  "automatique, le chargement et l'attente. Puis ajustez pour la disponibilité, les "
                  "changements de série et le rendement au premier passage. Regardez les deux testeurs de "
                  "la ligne audio à l'écran. Sur le papier, ils traitent cent soixante unités par heure. En "
                  "réalité, environ cent quarante bonnes. L'auriez-vous prévu ?",
    },
    {
        "key": "p11", "num": 11, "title": "Lignes multi-modèles",
        "points": [("Un seul diagramme peut cacher des problèmes", "Alors un seul diagramme peut cacher"),
                   ("Barres par modèle, le pire cas", "Utilisez donc des barres par modèle"),
                   ("Un effectif polyvalent et qualifié", "Prévoyez un effectif polyvalent et qualifié"),
                   ("Heijunka et SMED lissent le mix", "Et utilisez le Heijunka")],
        "example": "27 s en moyenne sur le mix, mais 42 s sur le modèle audio — un long lot accumule vite le "
                   "travail.",
        "example_cue": "Un poste peut avoir une moyenne",
        "script": "Et si votre ligne fabrique plusieurs modèles ? Alors un seul diagramme peut cacher des "
                  "problèmes. Un poste peut avoir une moyenne de vingt-sept secondes sur le mix. Mais sur "
                  "le modèle audio, il en demande quarante-deux. Lancez un long lot de ce modèle, et le "
                  "travail s'accumule vite. Utilisez donc des barres par modèle, et vérifiez le pire cas. "
                  "Prévoyez un effectif polyvalent et qualifié. Et utilisez le Heijunka et le SMED pour "
                  "lisser le mix. Alors, comment savoir qu'un nouvel équilibrage a vraiment marché ?",
    },
    {
        "key": "p12", "num": 12, "title": "KPI et vérification",
        "points": [("Un diagramme équilibré est une hypothèse", "Un diagramme équilibré n'est"),
                   ("Avancés : respect du travail standard", "Surveillez les indicateurs avancés"),
                   ("Retardés : bonne production, défauts, UPPH", "Surveillez les retardés"),
                   ("Vérifier l'ergonomie avec les opérateurs", "vérifiez l'ergonomie")],
        "example": "L'atteinte du plan compte les bonnes unités face au plan ; le rendement au premier "
                   "passage compte les unités réussies du premier coup.",
        "example_cue": "L'atteinte du plan compte",
        "script": "Un diagramme équilibré n'est qu'une hypothèse. Vous le prouvez par les résultats. "
                  "Surveillez les indicateurs avancés, comme le respect du travail standard. Surveillez les "
                  "retardés, comme la bonne production, les défauts et les unités par heure-personne. "
                  "Gardez vos définitions cohérentes. À l'écran, deux mesures se ressemblent mais veulent "
                  "dire des choses différentes. L'atteinte du plan compte les bonnes unités face au plan. "
                  "Le rendement au premier passage compte les unités qui réussissent du premier coup. Et "
                  "après tout changement, vérifiez l'ergonomie avec vos opérateurs.",
    },
    {
        "key": "p13", "num": 13, "title": "Cas : cellule de décodeurs",
        "points": [("Avant : B plafonnait la production vers 103/heure", "Avant, le poste B plafonnait"),
                   ("Après : B descend à 30 secondes", "Après le pilote"),
                   ("Environ 116 bonnes/heure contre 120 théoriques", "La production est montée"),
                   ("Terminé seulement après deux semaines stables", "Elle ne l'a déclaré terminé")],
        "example": "Rester sous 120 est normal : la disponibilité et le rendement coûtent toujours quelque "
                   "chose.",
        "example_cue": "Et c'est normal",
        "script": "Voyons comment s'est déroulé le changement de Meera. Avant, le poste B plafonnait la "
                  "cellule vers cent trois unités par heure. Après le pilote, le poste B est descendu à "
                  "trente secondes. La production est montée à environ cent seize bonnes unités par heure. "
                  "C'est moins que les cent vingt théoriques. Et c'est normal, car la disponibilité et le "
                  "rendement coûtent toujours quelque chose. Elle ne l'a déclaré terminé qu'après deux "
                  "semaines stables. Que vérifieriez-vous ensuite ?",
    },
    {
        "key": "p14", "num": 14, "title": "À faire et à éviter",
        "points": [("Mesurer le vrai travail, garder les données à jour", "Mesurez le vrai travail"),
                   ("Impliquer opérateurs, qualité, ingénierie", "Impliquez les opérateurs"),
                   ("Protéger sécurité, ESD, tests, traçabilité", "Protégez la sécurité, l'ESD"),
                   ("Pas de temps du meilleur cas, pas de réduction d'effectif", "N'utilisez pas les temps de cycle du meilleur cas")],
        "example": "Supprimer un contrôle code-barres semble faire gagner 6 secondes. Ce n'est pas un "
                   "équilibrage — c'est un risque de traçabilité.",
        "example_cue": "Supprimer un contrôle code-barres",
        "script": "Quelques règles strictes. Mesurez le vrai travail, et gardez vos données à jour. "
                  "Impliquez les opérateurs, la qualité et l'ingénierie. Protégez la sécurité, l'ESD, les "
                  "tests et la traçabilité. N'utilisez pas les temps de cycle du meilleur cas. Et ne faites "
                  "pas du Yamazumi un outil de réduction d'effectif, sinon les gens arrêtent de partager "
                  "les vraies données. Voici un piège. Supprimer un contrôle code-barres semble faire "
                  "gagner six secondes. Ce n'est pas un équilibrage. C'est un risque de traçabilité. Votre "
                  "équipe le repérerait-elle ?",
    },
    {
        "key": "p15", "num": 15, "title": "Feuille de route sur 90 jours",
        "points": [("Jours 1–30 : ligne pilote, études de temps, référence", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : ECRS, rééquilibrer, qualifier", "Pendant les trente suivants"),
                   ("Jours 61–90 : vérifier, mettre à jour les SOP, étendre", "Pendant les trente derniers"),
                   ("Garder les diagrammes à jour", "Puis gardez vos diagrammes à jour")],
        "example": "Un diagramme périmé est pire que pas de diagramme du tout.",
        "example_cue": "Un diagramme périmé",
        "script": "Prêt à commencer ? Voici un plan sur quatre-vingt-dix jours. Pendant les trente premiers "
                  "jours, choisissez une ligne pilote, rassemblez la demande et les études de temps, et "
                  "construisez les diagrammes de référence. Pendant les trente suivants, menez des ateliers "
                  "ECRS, rééquilibrez et qualifiez les opérateurs. Pendant les trente derniers, vérifiez le "
                  "rendement et la production, mettez à jour les SOP, et étendez aux lignes similaires. "
                  "Puis gardez vos diagrammes à jour chaque fois que la demande, le mix ou l'effectif "
                  "change. Un diagramme périmé est pire que pas de diagramme du tout.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson). Station bars use the
# current state from p07 (TAKT 30 s).
CURRENT = [("A", 22, None), ("B", 35, "bad"), ("C", 27, None), ("D", 20, None)]


def takt_bars(stations, note, unit, with_="example"):
    return {"type": "bars", "label": "TAKT", "value": 30, "suffix": " s", "note": note, "unit": unit,
            "with": with_, "items": [{"label": f"poste {s}", "value": v, "tone": t, "with": with_}
                                     for s, v, t in stations]}


VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Barres empilées", "icon": "stack", "with": 0},
        {"label": "« S'empiler »", "icon": "box", "with": 1},
        {"label": "Les tâches d'un opérateur", "icon": "person", "with": 2},
        {"label": "Au-dessus du TAKT : ne suit pas", "icon": "warning", "tone": "bad", "with": 3}],
        "then": takt_bars(CURRENT, "B ne peut pas suivre", "La cellule de Meera : secondes de travail à chaque poste")},
    "p02": {"type": "icons", "items": [
        {"label": "Le déséquilibre d'un coup d'œil", "icon": "search", "with": 0},
        {"label": "Un effectif fondé sur des faits", "icon": "person", "with": 1},
        {"label": "Où former en polyvalence", "icon": "sequence", "with": 2},
        {"label": "Les vérifications d'ingénierie restent nécessaires", "icon": "wrench", "tone": "bad", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Long vissage", "sub": "Surcharge", "icon": "screw", "with": "example"},
            {"label": "Retirer une petite tâche", "sub": "Flux fluide", "icon": "sequence", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Temps net ÷ bonnes unités", "icon": "clock", "with": 0},
        {"label": "Temps de cycle", "sub": "À quelle fréquence une unité sort", "icon": "sequence", "with": 1},
        {"label": "Contenu de travail", "sub": "Somme des tâches manuelles", "icon": "hand", "with": 2},
        {"label": "Temps machine", "sub": "À part", "icon": "gear", "with": 3}],
        "then": {"type": "stat", "value": 30, "suffix": " s", "icon": "clock", "label": "Temps TAKT",
                 "unit": "420 minutes nettes ÷ 840 unités", "with": "example"}},
    "p04": takt_bars([("A", 22, None), ("B", 35, "bad")], "B est au-dessus de la ligne",
                     "Une barre par poste, ligne du TAKT horizontale", with_=0),
    "p05": {"type": "flow", "items": [
        {"label": "Définir début et fin", "icon": "pin", "with": 0},
        {"label": "De nombreux cycles, chaque équipe", "icon": "clock", "with": 1},
        {"label": "Marches, arrêts, changements de série", "icon": "walk", "with": 2},
        {"label": "Machine, à part du manuel", "icon": "gear", "tone": "good", "with": 3}]},
    "p06": {"type": "icons", "items": [
        {"label": "Valeur ajoutée", "icon": "check", "tone": "good", "with": 0},
        {"label": "Nécessaire : contrôles, traçabilité", "icon": "shield", "with": 1},
        {"label": "Gaspillage : chercher, marcher, attendre", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "ECRS, garder les contrôles", "icon": "wrench", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "5 s de marche pour les vis", "sub": "Gaspillage", "icon": "walk", "with": "example"},
            {"label": "Bacs au point d'utilisation", "sub": "Marche supprimée", "icon": "tray", "with": "example"}]}},
    "p07": takt_bars(CURRENT, "B dépasse de 5 s : première priorité", "L'état actuel de Meera"),
    "p08": {"type": "icons", "items": [
        {"label": "Déplacer le travail, améliorer la méthode", "icon": "sequence", "with": 0},
        {"label": "Pas exactement égales", "icon": "scale", "with": 1},
        {"label": "Implantation, séquence, compétence, contrôles", "icon": "clipboard", "with": 2},
        {"label": "ECRS avant d'ajouter des personnes", "icon": "person", "with": 3}],
        "then": takt_bars([("A", 22, None), ("B", 30, "good"), ("C", 27, None), ("D", 25, None)],
                          "Étiquetage de 5 s de B → D", "Après le changement : pilote, puis nouvelle mesure")},
    "p09": {"type": "stat", "value": 4, "suffix": " opérateurs", "icon": "person", "label": "104 s de travail ÷ TAKT de 30 s, arrondi au-dessus",
            "unit": "Efficacité d'équilibrage d'environ 87 %", "with": "example"},
    "p10": {"type": "icons", "items": [
        {"label": "Barre longue ≠ problème d'opérateur", "icon": "person", "with": 0},
        {"label": "Machines partagées", "icon": "gear", "with": 1},
        {"label": "Manuel · automatique · chargement · attente", "icon": "clock", "with": 2},
        {"label": "Disponibilité, changements, rendement", "icon": "chartDown", "with": 3}],
        "then": {"type": "compare", "before": {"label": "Sur le papier", "value": 160}, "after": {"label": "Réelles, bonnes", "value": 140},
                 "unit": "unités par heure, deux testeurs audio", "note": "Planifiez avec le chiffre réel", "with": "example"}},
    "p11": {"type": "bars", "label": "TAKT", "value": 30, "suffix": " s", "note": "La moyenne le cache",
            "unit": "Un poste, secondes par unité", "with": "example", "items": [
        {"label": "Moyenne du mix", "value": 27, "with": "example"},
        {"label": "Modèle audio", "value": 42, "tone": "bad", "with": "example"}]},
    "p12": {"type": "icons", "items": [
        {"label": "Une hypothèse à prouver", "icon": "test", "with": 0},
        {"label": "Avancé : travail standard", "icon": "clipboard", "with": 1},
        {"label": "Retardé : production, défauts, UPPH", "icon": "chartUp", "with": 2},
        {"label": "Ergonomie avec les opérateurs", "icon": "person", "with": 3}]},
    "p13": {"type": "compare", "before": {"label": "Avant", "value": 103}, "after": {"label": "Après", "value": 116},
            "unit": "bonnes unités par heure (théorie : 120)", "note": "Terminé après deux semaines stables", "with": 2},
    "p14": {"type": "icons", "items": [
        {"label": "Vrai travail, données à jour", "icon": "clock", "tone": "good", "with": 0},
        {"label": "Opérateurs, qualité, ingénierie", "icon": "person", "tone": "good", "with": 1},
        {"label": "Sécurité, ESD, tests, traçabilité", "icon": "shield", "tone": "good", "with": 2},
        {"label": "Meilleur cas, réduction d'effectif", "icon": "cross", "tone": "bad", "with": 3}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Ligne pilote, études de temps, référence", "sub": "Jours 1–30", "icon": "clock", "with": 0},
        {"label": "ECRS, rééquilibrage, qualification", "sub": "31–60", "icon": "sequence", "with": 1},
        {"label": "Vérifier, mettre à jour le SOP, étendre", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Le poste 4 tourne à 33 s contre un TAKT de 30 secondes ; le poste 1 tourne à 22 s. Que "
                    "faut-il essayer en premier ?",
        "options": ["Demander à l'opérateur du poste 4 d'aller plus vite",
                    "Déplacer une tâche possible du poste 4 au poste 1, ou améliorer sa méthode, puis faire "
                    "un pilote et mesurer de nouveau",
                    "Supprimer un contrôle qualité au poste 4",
                    "Passer le TAKT à 33 secondes"],
        "correct": 1,
        "explanation": "Équilibrer, c'est déplacer du travail possible ou améliorer la méthode. Pousser les "
                       "gens, supprimer des contrôles ou redéfinir le TAKT cache le problème au lieu de le "
                       "corriger.",
        "q_script": "Vérification rapide, et c'est un scénario. Le poste quatre tourne à trente-trois "
                    "secondes contre un TAKT de trente secondes. Le poste un tourne à vingt-deux. Que faut-il "
                    "essayer en premier ? Prenez quelques secondes.",
        "a_script": "Cherchez une tâche possible à déplacer du poste quatre au poste un, ou améliorez sa "
                    "méthode. Puis faites un pilote et mesurez de nouveau. Pousser les gens ou supprimer des "
                    "contrôles, ce n'est pas équilibrer.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "420 minutes nettes servent une demande de 840 bonnes unités. Quel est le temps TAKT ?",
        "options": ["20 secondes par unité",
                    "30 secondes par unité",
                    "2 secondes par unité",
                    "60 secondes par unité"],
        "correct": 1,
        "explanation": "TAKT = temps net ÷ demande = 420 × 60 ÷ 840 = 30 secondes par unité.",
        "q_script": "Encore une. Votre ligne a quatre cent vingt minutes nettes. La demande est de huit cent "
                    "quarante bonnes unités. Quel est votre temps TAKT ? Réfléchissez.",
        "a_script": "C'est trente secondes par unité. Convertissez les minutes en secondes, puis divisez par "
                    "la demande.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
