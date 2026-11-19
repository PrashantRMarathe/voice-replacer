"""value_stream in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh value_stream_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "vs_fr"
NAME = "value_stream_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Value Stream Mapping": "valiou strime mapingue",
    "Why-Why": "ouaï ouaï",
    "Pareto": "Paréto",
    "Kanban": "Kanne-banne",
    "Kaizen": "Kaïzène",
    "Gemba": "Guemba",
    "TAKT": "takte",
    "WIP": "double vé i pé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Un décodeur prend quinze minutes à fabriquer et à tester. Pourtant, il met près de "
    "quatre jours à arriver chez le client. Où passe tout ce temps ? Dans cette leçon, vous "
    "allez découvrir Value Stream Mapping. Vous verrez comment dessiner le flux réel de "
    "matière et d'information. Puis vous trouverez les attentes, et concevrez un meilleur "
    "état futur. Nous suivrons Rahul, ingénieur amélioration, qui cartographie la ligne de "
    "décodeurs de son usine."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Cartographiez le flux réel, de la matière comme de "
    "l'information. La plus grande partie de votre délai se cache dans l'attente, pas dans le "
    "travail. Et concevez un état futur que vous pouvez prouver, avant de réduire le moindre "
    "stock. Voici votre action pour cette semaine. Parcourez une famille de produits à "
    "rebours depuis l'expédition, et comptez chaque tas que vous croisez. Bravo d'avoir "
    "terminé cette leçon. Ensuite, vous découvrirez l'analyse Why-Why, pour trouver les "
    "vraies causes."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce que montre une VSM",
        "points": [("Une famille de produits, de la commande à la livraison", "montre tout le parcours"),
                   ("La matière et l'information qui la pilote", "Elle inclut la matière"),
                   ("Travail à valeur ajoutée, attente, stock", "Elle montre le travail à valeur ajoutée"),
                   ("Une image partagée de la réalité", "C'est une image partagée")],
        "example": "Rahul suit un décodeur des cartes reçues jusqu'à l'expédition — signaux de planification "
                   "et libération entrepôt compris.",
        "example_cue": "Rahul suit un décodeur",
        "script": "Voici l'idée centrale. Une cartographie de la chaîne de valeur montre tout le parcours "
                  "d'une famille de produits, de la commande client à la livraison. Elle inclut la matière, "
                  "et l'information qui la pilote. Elle montre le travail à valeur ajoutée, l'attente, les "
                  "piles de stock, et les signaux lents. C'est une image partagée de la réalité, pas un "
                  "organigramme décoratif. Rahul suit un décodeur des cartes reçues jusqu'à l'expédition. "
                  "Il inclut les signaux de planification et la libération entrepôt, pas seulement la "
                  "ligne. Alors, qu'est-ce qui compte comme valeur pour vous ?",
    },
    {
        "key": "p02", "num": 2, "title": "Valeur, flux et gaspillage",
        "points": [("Valeur : ce que le client paierait", "La valeur, c'est ce que votre client"),
                   ("Nécessaire aujourd'hui, mais sans valeur", "Certains travaux n'ajoutent aucune valeur"),
                   ("Pur gaspillage : attente, transport, retouche", "Puis il y a le pur gaspillage")],
        "example": "Le décodeur de Rahul : 15 minutes de fabrication et de test contre 2 jours d'attente de "
                   "libération matière.",
        "example_cue": "Le décodeur de Rahul passe",
        "script": "La valeur, c'est ce que votre client paierait volontiers. Elle change la forme, "
                  "l'ajustement ou la fonction du produit, du premier coup. Certains travaux n'ajoutent "
                  "aucune valeur mais restent nécessaires aujourd'hui, comme une inspection obligatoire. "
                  "Puis il y a le pur gaspillage, comme l'attente, le transport et la retouche. Le décodeur "
                  "de Rahul passe quinze minutes en fabrication et en test. Il passe deux jours à attendre "
                  "la libération de la matière. Qu'attaqueriez-vous en premier ? Des secondes d'assemblage, "
                  "ou des jours d'attente ?",
    },
    {
        "key": "p03", "num": 3, "title": "Familles de produits et périmètre",
        "points": [("Ne pas tout cartographier d'un coup", "Ne cartographiez pas tout"),
                   ("Famille : mêmes étapes et équipements", "Une famille de produits est"),
                   ("Grille produits × processus", "Construisez une grille simple"),
                   ("Regrouper les produits qui partagent un parcours", "Puis regroupez les produits")],
        "example": "Les téléphones et les appareils audio partagent l'emballage mais sont testés très "
                   "différemment — ils ont donc des cartes séparées.",
        "example_cue": "Rahul a remarqué que les téléphones",
        "script": "Ne cartographiez pas tout d'un coup. Une famille de produits est un groupe d'articles "
                  "qui suivent à peu près les mêmes étapes et équipements. Mélanger des produits sans "
                  "rapport cache la variation, et les moyennes commencent à mentir. Construisez une grille "
                  "simple, avec les produits sur le côté et les processus en haut. Puis regroupez les "
                  "produits qui partagent un parcours. Rahul a remarqué que les téléphones et les appareils "
                  "audio partagent l'emballage, mais sont testés très différemment. Ils ont donc des cartes "
                  "séparées. Quelle famille cartographieriez-vous en premier ?",
    },
    {
        "key": "p04", "num": 4, "title": "Symboles et conventions",
        "points": [("Icônes d'usine : client et fournisseur", "Les icônes d'usine montrent"),
                   ("Boîtes de processus + boîtes de données", "Les boîtes de processus montrent"),
                   ("Triangles : stock en attente", "Les triangles montrent"),
                   ("Flèches matière et flèches information", "Les flèches pleines portent")],
        "example": "Les éclairs Kaizen marquent les idées ; une ligne de temps sépare le traitement de "
                   "l'attente. Ajoutez toujours une légende.",
        "example_cue": "Les éclairs Kaizen marquent",
        "script": "Les cartographies de la chaîne de valeur utilisent un langage visuel simple. Les icônes "
                  "d'usine montrent votre client et votre fournisseur. Les boîtes de processus montrent les "
                  "opérations. En dessous, des boîtes de données donnent le temps de cycle, le changement "
                  "de série, la disponibilité et le rendement. Les triangles montrent le stock en attente. "
                  "Les flèches pleines portent la matière, et les flèches plus fines portent l'information. "
                  "Les éclairs Kaizen marquent les idées d'amélioration. Une ligne de temps en bas sépare "
                  "le traitement de l'attente. Les symboles varient selon les entreprises, alors ajoutez "
                  "toujours une légende. Prêt à collecter de vraies données ?",
    },
    {
        "key": "p05", "num": 5, "title": "Tournée Gemba et données",
        "points": [("Commencer au Gemba", "La cartographie commence au Gemba"),
                   ("Marcher de l'expédition vers le fournisseur", "Marchez de l'expédition"),
                   ("Chronométrer vous-même de vrais cycles", "Chronométrez de vrais cycles"),
                   ("Compter le WIP à chaque stock tampon", "Comptez le WIP")],
        "example": "Le système de Rahul affichait un chiffre pour le WIP du test, son comptage physique un "
                   "autre. Il les a réconciliés avant tout calcul.",
        "example_cue": "Le système de Rahul affichait",
        "script": "La cartographie commence au Gemba, là où le travail se fait vraiment. Marchez de "
                  "l'expédition vers le fournisseur. Vous verrez les vraies files, et si la matière est "
                  "tirée ou poussée. Chronométrez de vrais cycles vous-même, plusieurs fois, au lieu de "
                  "vous fier aux temps standard. Comptez le WIP à chaque stock tampon. Le système de Rahul "
                  "affichait un chiffre pour le WIP du test. Son comptage physique en affichait un autre. "
                  "Il les a réconciliés avant tout calcul. Ensuite, à quelle vitesse votre client a-t-il "
                  "besoin que vous alliez ?",
    },
    {
        "key": "p06", "num": 6, "title": "Demande client et TAKT",
        "points": [("TAKT : le rythme dont votre client a besoin", "Le TAKT fixe le rythme"),
                   ("Temps net ÷ bonnes unités, même période", "Divisez votre temps net disponible"),
                   ("Comparer chaque poste à lui", "Comparez maintenant chaque poste")],
        "example": "1 200 bons décodeurs en une équipe → TAKT de 21 secondes, environ 170 par heure. Un "
                   "poste à 24 secondes ne peut pas suivre seul.",
        "example_cue": "La ligne de Rahul tourne",
        "script": "Le TAKT fixe le rythme dont votre client a besoin. Divisez votre temps net disponible "
                  "par les bonnes unités demandées, sur la même période. Le temps net exclut les pauses et "
                  "les arrêts prévus. La ligne de Rahul tourne sur une équipe, et a besoin de mille deux "
                  "cents bons décodeurs par jour. Cela donne un TAKT de vingt et une secondes par unité, "
                  "soit environ cent soixante-dix par heure. Comparez maintenant chaque poste à lui. Un "
                  "poste tourne à vingt-quatre secondes. Qu'est-ce que cela veut dire pour vous ? Il ne "
                  "peut pas suivre, sauf si un deuxième poste tourne en parallèle.",
    },
    {
        "key": "p07", "num": 7, "title": "La carte de l'état actuel",
        "points": [("La demande à droite, le travail vers l'amont", "Mettez la demande client"),
                   ("Des données sous chaque boîte", "Ajoutez les données"),
                   ("Dessiner le flux d'information", "Puis dessinez le flux d'information"),
                   ("Le vérifier avec vos opérateurs", "Enfin, demandez à vos opérateurs")],
        "example": "La planification lançait des lots hebdomadaires ; le test ne pouvait suivre qu'un rythme "
                   "journalier — les décodeurs s'accumulaient entre les deux.",
        "example_cue": "La carte de Rahul a révélé",
        "script": "Dessinez maintenant l'état actuel. Mettez la demande client à droite, puis remontez à "
                  "travers chaque processus et chaque stock tampon. Ajoutez les données sous chaque boîte. "
                  "Puis dessinez le flux d'information. Prévisions, plannings journaliers, ordres de "
                  "fabrication et signaux Kanban. La carte de Rahul a révélé un décalage. La planification "
                  "lançait des lots hebdomadaires vers l'assemblage, mais le test ne pouvait suivre qu'un "
                  "rythme journalier. Les décodeurs semi-finis s'accumulaient donc entre les deux. Enfin, "
                  "demandez à vos opérateurs. Les flèches correspondent-elles à une journée normale ?",
    },
    {
        "key": "p08", "num": 8, "title": "Délai et stocks",
        "points": [("Ligne de temps : travail face à l'attente", "La ligne de temps sépare"),
                   ("Attente = stock tampon ÷ demande journalière", "Pour estimer l'attente"),
                   ("Ratio de valeur ajoutée : un signal, pas une preuve", "Cette toute petite part")],
        "example": "Trois stocks tampons à 1 200 par jour = 3,5 jours d'attente contre 15 minutes de "
                   "traitement.",
        "example_cue": "Rahul a trois stocks tampons",
        "script": "La ligne de temps sépare le temps de travail du temps d'attente. Pour estimer l'attente, "
                  "divisez le stock de chaque tampon par la demande journalière. Rahul a trois stocks "
                  "tampons, et une demande de mille deux cents par jour. Ensemble, ils représentent trois "
                  "jours et demi d'attente. Le traitement réel ne fait que quinze minutes. Voyez-vous "
                  "l'écart ? Cette toute petite part est le ratio de valeur ajoutée. Prenez-le comme un "
                  "signal, pas comme la preuve que toute l'attente peut disparaître. Alors, pourquoi ce "
                  "stock est-il là ?",
    },
    {
        "key": "p09", "num": 9, "title": "Contraintes et causes",
        "points": [("Une carte montre où, pas pourquoi", "Une carte vous dit"),
                   ("Longues files, urgences, boucles de retouche", "Cherchez les longues files"),
                   ("Creuser : Pareto, cinq pourquoi, arête de poisson", "Puis creusez")],
        "example": "2 000 décodeurs en attente au test : trop peu de testeurs, des arrêts, le firmware ou "
                   "des lancements en lots ? Vérifiez avant d'acheter.",
        "example_cue": "Rahul a trouvé deux mille",
        "script": "Une carte vous dit où regarder, pas pourquoi cela arrive. Cherchez les longues files, "
                  "les urgences fréquentes et les boucles de retouche. Puis creusez avec des diagrammes de "
                  "Pareto, les cinq pourquoi ou une arête de poisson. Rahul a trouvé deux mille décodeurs "
                  "en attente au test. Trop peu de testeurs ? Des arrêts ? Un firmware instable ? Ou de "
                  "gros lancements en lots ? Chacun demande une solution différente. Il a donc vérifié les "
                  "données avant que quiconque n'achète un nouveau testeur. Que vérifieriez-vous en premier "
                  "?",
    },
    {
        "key": "p10", "num": 10, "title": "État futur : flux et flux tiré",
        "points": [("Flux continu au TAKT ou en dessous", "Utilisez le flux continu"),
                   ("Couloirs premier entré, premier sorti plafonnés", "utilisez un couloir premier entré, premier sorti"),
                   ("Supermarché avec signaux de tirage", "utilisez un supermarché"),
                   ("Un seul processus stimulateur", "Puis choisissez un stimulateur")],
        "example": "La conception de Rahul : l'assemblage et l'emballage partagent un couloir plafonné ; les "
                   "cartes sont tirées d'un supermarché.",
        "example_cue": "Dans la conception de Rahul",
        "script": "Concevez maintenant l'état futur. Il doit être meilleur, et aussi réaliste. Utilisez le "
                  "flux continu partout où les étapes peuvent tourner au TAKT ou en dessous. Là où ce n'est "
                  "pas possible, utilisez un couloir premier entré, premier sorti avec un plafond strict. "
                  "Là où le flux ne peut pas du tout se connecter, utilisez un supermarché avec des signaux "
                  "de tirage. Puis choisissez un stimulateur, le seul processus que vous planifiez. Dans la "
                  "conception de Rahul, l'assemblage et l'emballage partagent un couloir plafonné. Les "
                  "cartes sont tirées d'un supermarché. Où votre ligne pourrait-elle couler ?",
    },
    {
        "key": "p11", "num": 11, "title": "Pitch, Kanban et réapprovisionnement",
        "points": [("Pitch = TAKT × quantité du conditionnement", "Le pitch est le rythme"),
                   ("Taille du Kanban : délai et demande", "Les tailles de Kanban dépendent"),
                   ("Prouver le réapprovisionnement avant de réduire le stock", "Prouvez que le réapprovisionnement marche")],
        "example": "Conditionnements de 20 → un pitch de 7 minutes. Un kit dure 6 minutes mais un "
                   "réapprovisionnement en prend 12 : plus de kits, ou un réapprovisionnement plus rapide.",
        "example_cue": "Les conditionnements de Rahul contiennent",
        "script": "Le lissage rend les signaux de tirage prévisibles. Le pitch est le rythme pour déplacer "
                  "un conditionnement standard. C'est le TAKT multiplié par la quantité du conditionnement. "
                  "Les conditionnements de Rahul contiennent vingt décodeurs, donc son pitch est de sept "
                  "minutes. Les tailles de Kanban dépendent du délai de réapprovisionnement et de la "
                  "demande. Un kit dure six minutes, mais un réapprovisionnement en prend douze. Il lui "
                  "faut donc plus de kits, ou un réapprovisionnement plus rapide. Voici la règle pour vous. "
                  "Prouvez que le réapprovisionnement marche avant de réduire le moindre stock. Prêt pour "
                  "le cas complet ?",
    },
    {
        "key": "p12", "num": 12, "title": "Cas pratique détaillé",
        "points": [("1 200 décodeurs par jour ; 4 200 en attente", "La demande est de mille deux cents"),
                   ("3,5 jours de file d'attente", "Cela fait trois jours et demi"),
                   ("État futur : stocks tampons divisés par deux", "Son état futur divise par deux"),
                   ("Valider d'abord capacité, matière, qualité", "La capacité de test")],
        "example": "Le temps de file tombe sous deux jours — une baisse de 50 %. Mais il n'appuie pas encore "
                   "sur le bouton.",
        "example_cue": "Le temps de file tombe",
        "script": "Voici le cas de Rahul, avec des chiffres de formation. La demande est de mille deux "
                  "cents décodeurs par jour. Aujourd'hui, quatre mille deux cents unités attendent dans "
                  "trois stocks tampons. Cela fait trois jours et demi de file d'attente. Son état futur "
                  "divise par deux chaque stock tampon, à deux mille cent unités. Le temps de file tombe "
                  "sous deux jours. C'est une baisse de cinquante pour cent. Mais il n'appuie pas encore "
                  "sur le bouton. La capacité de test, la livraison des matières et les contrôles qualité "
                  "tiennent-ils avec moins de tampon ? Comment le vérifieriez-vous ?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI et bénéfices réels",
        "points": [("Mesurer tout le flux", "Mesurez tout le flux"),
                   ("Délai, WIP, livraison, FPY", "Suivez le délai, le WIP"),
                   ("Référence, puis vérifier sur des semaines", "Fixez une référence"),
                   ("Méfiez-vous du stock qui a seulement bougé", "Méfiez-vous du stock")],
        "example": "Moins de WIP libère environ ₹31 lakh de stock — de la trésorerie libérée une fois, pas "
                   "un profit chaque année.",
        "example_cue": "Le WIP réduit de Rahul",
        "script": "Mesurez tout le flux, pas seulement la vitesse des postes. Suivez le délai, le WIP, la "
                  "livraison à temps et le rendement au premier passage. Fixez une référence, puis vérifiez "
                  "sur plusieurs semaines représentatives. Méfiez-vous du stock qui a simplement bougé "
                  "ailleurs. Voici un piège financier. Le WIP réduit de Rahul libère environ trois millions "
                  "cent mille roupies de stock. C'est de la trésorerie libérée une seule fois. Ce n'est pas "
                  "trois millions cent mille de profit chaque année. Votre équipe financière ferait-elle la "
                  "différence ? Rapportez-le honnêtement.",
    },
    {
        "key": "p14", "num": 14, "title": "Gouvernance et 90 jours",
        "points": [("Chaque fonction a un rôle", "L'amélioration de la chaîne de valeur demande"),
                   ("Jours 1–30 : choisir la famille, cartographier l'actuel", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : concevoir le futur, piloter le flux tiré", "Pendant les trente suivants"),
                   ("Jours 61–90 : stabiliser, auditer, élargir", "Pendant les trente derniers")],
        "example": "Rahul a corrigé le goulot du test avant de réduire son stock tampon — sinon la ligne "
                   "manque de matière.",
        "example_cue": "Rahul a corrigé le goulot du test",
        "script": "L'amélioration de la chaîne de valeur demande toutes les fonctions. La planification "
                  "porte la logique du planning. La production porte le flux, la qualité les contrôles, et "
                  "les matières le réapprovisionnement. La direction lève les obstacles. Pendant les trente "
                  "premiers jours, choisissez la famille et cartographiez l'état actuel. Pendant les trente "
                  "suivants, concevez l'état futur et pilotez le flux tiré. Pendant les trente derniers, "
                  "stabilisez, auditez et élargissez. Rahul a corrigé le goulot du test avant de réduire "
                  "son stock tampon. Sinon, la ligne manque de matière. Quel serait votre premier pilote ?",
    },
    {
        "key": "p15", "num": 15, "title": "À faire, à éviter et modèle",
        "points": [("Mettre à jour quand la demande ou le parcours change", "Mettez-la à jour quand"),
                   ("Cartographier le flux réel, avec les opérateurs", "Alors cartographiez le flux réel"),
                   ("Temps de cycle ≠ délai", "ne confondez pas le temps de cycle"),
                   ("Vérifier la capacité avant de supprimer des tampons", "ne supprimez pas de tampons")],
        "example": "Une carte avec seulement des boîtes de processus n'est pas une cartographie de la chaîne "
                   "de valeur. C'est juste un organigramme.",
        "example_cue": "Une carte avec seulement des boîtes de processus",
        "script": "Une bonne carte est un outil de décision vivant. Mettez-la à jour quand la demande, le "
                  "parcours ou les grandes contraintes changent. Alors cartographiez le flux réel, avec des "
                  "unités cohérentes, et impliquez vos opérateurs. Montrez les boucles de retouche et les "
                  "signaux de planification. Mais ne confondez pas le temps de cycle avec le délai. "
                  "N'appelez pas une trésorerie libérée une fois une économie annuelle. Et ne supprimez pas "
                  "de tampons avant d'avoir vérifié la capacité et le réapprovisionnement. Une carte avec "
                  "seulement des boîtes de processus n'est pas une cartographie de la chaîne de valeur. "
                  "C'est juste un organigramme.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Une famille de produits", "icon": "box"}, {"label": "Matière + information", "icon": "sequence"},
        {"label": "Travail face à l'attente", "icon": "clock"}, {"label": "Une image partagée", "icon": "person"}]},
    "p02": {"type": "versus", "items": [
        {"label": "2 jours d'attente", "sub": "pour la libération matière", "icon": "clock", "with": "example"},
        {"label": "15 minutes de vrai travail", "sub": "fabriqué et testé", "icon": "wrench", "with": "example"}]},
    "p03": {"type": "matrix", "prefix": "check", "cols": ["Assemblage", "Test téléphone", "Test audio", "Emballage"],
            "note": "Même emballage, test différent : cartes séparées", "items": [
        {"label": "Téléphones", "cells": [3, 3, None, 3], "with": 2},
        {"label": "Audio", "cells": [3, None, 3, 3], "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Client, fournisseur", "icon": "box"}, {"label": "Boîtes de processus + de données", "icon": "clipboard"},
        {"label": "Triangles : stock", "icon": "stack"}, {"label": "Matière et information", "icon": "sequence"}]},
    "p05": {"type": "flow", "items": [
        {"label": "Allez au Gemba", "icon": "walk"},
        {"label": "Remontez depuis l'expédition", "icon": "sequence"},
        {"label": "Chronométrez de vrais cycles", "icon": "clock"},
        {"label": "Comptez chaque stock tampon", "sub": "Réconciliez avec le système", "icon": "count", "tone": "good"}]},
    "p06": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Le rythme du client", "icon": "clock", "with": 0},
        {"label": "Temps net ÷ bonnes unités", "icon": "count", "with": 1},
        {"label": "Comparer chaque poste", "icon": "scale", "with": 2}],
        "then": {"type": "bars", "label": "TAKT", "value": 21, "suffix": " s", "note": "ne peut pas suivre seul",
                 "unit": "1 200 bons décodeurs par équipe ≈ 170 par heure", "with": "example", "items": [
            {"label": "Un poste", "value": 24, "tone": "bad", "with": "example"}]}},
    "p07": {"type": "flow", "items": [
        {"label": "Planification : lots hebdomadaires", "icon": "calendar", "with": "example"},
        {"label": "Les décodeurs s'accumulent", "sub": "Semi-finis, en attente", "icon": "stack", "tone": "bad", "with": "example"},
        {"label": "Test : un rythme journalier", "icon": "test", "with": "example"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Travail face à l'attente", "icon": "clock", "with": 0},
        {"label": "Stock tampon ÷ demande journalière", "icon": "count", "with": 1},
        {"label": "Ratio de valeur ajoutée", "sub": "Un signal, pas une preuve", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 3.5, "decimals": 1, "suffix": " jours", "icon": "clock", "label": "d'attente",
                 "unit": "contre seulement 15 minutes de traitement", "with": "example"}},
    "p09": {"type": "flow", "items": [
        {"label": "Une carte montre où, pas pourquoi", "icon": "search", "with": 0},
        {"label": "Files, urgences, retouches", "icon": "stack", "with": 1},
        {"label": "Pareto, cinq pourquoi, arête de poisson", "icon": "gear", "with": 2}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Trop peu de testeurs ?", "icon": "test", "with": "example"},
            {"label": "Des arrêts ?", "icon": "clock", "with": "example"},
            {"label": "Le firmware ?", "icon": "chip", "with": "example"},
            {"label": "Des lancements en lots ?", "icon": "stack", "with": "example"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "Cartes tirées d'un supermarché", "icon": "tray"},
        {"label": "Assemblage", "icon": "wrench"},
        {"label": "Un couloir FIFO plafonné", "icon": "sequence"},
        {"label": "Emballage : le stimulateur", "icon": "box", "tone": "good"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Pitch = TAKT × conditionnement", "icon": "count", "with": 0},
        {"label": "Taille du Kanban", "icon": "label", "with": 1},
        {"label": "Prouvez le réapprovisionnement", "icon": "check", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Conditionnements de 20 : un pitch de 7 minutes", "icon": "box", "with": "example"},
            {"label": "Un kit dure 6 min ; un réapprovisionnement en prend 12", "icon": "clock", "tone": "bad", "with": "example"},
            {"label": "Plus de kits, ou un réapprovisionnement plus rapide", "icon": "check", "tone": "good", "with": "example"}]}},
    "p12": {"type": "stat", "value": 3.5, "decimals": 1, "suffix": " jours", "icon": "clock", "label": "de file d'attente aujourd'hui",
            "unit": "4 200 unités en attente ÷ 1 200 par jour", "with": 1,
            "then": {"type": "compare", "before": {"label": "Aujourd'hui", "value": 4200}, "after": {"label": "État futur", "value": 2100},
                     "unit": "unités en attente dans trois stocks tampons", "note": "Temps de file divisé par deux (prévu)", "with": 2}},
    "p13": {"type": "icons", "items": [
        {"label": "Tout le flux", "icon": "sequence"}, {"label": "Délai, WIP, livraison, FPY", "icon": "chartUp"},
        {"label": "Référence, puis semaines", "icon": "calendar"}, {"label": "Stock qui a seulement bougé", "icon": "stack", "tone": "bad"}],
        "then": {"type": "stat", "value": 31, "prefix": "₹", "suffix": " lakh", "icon": "box", "label": "de stock libéré",
                 "unit": "Trésorerie libérée une fois : pas un profit chaque année", "with": "example"}},
    "p14": {"type": "timeline", "items": [
        {"label": "Choisir la famille, cartographier l'actuel", "sub": "Jours 1–30", "icon": "search", "with": 1},
        {"label": "Concevoir le futur, piloter le flux tiré", "sub": "31–60", "icon": "sequence", "with": 2},
        {"label": "Stabiliser, auditer, élargir", "sub": "61–90", "icon": "chartUp", "with": 3}]},
    "p15": {"type": "icons", "items": [
        {"label": "Mettre à jour quand ça change", "icon": "sequence", "tone": "good"},
        {"label": "Flux réel, avec les opérateurs", "icon": "person", "tone": "good"},
        {"label": "Cycle ≠ délai", "icon": "cross", "tone": "bad"},
        {"label": "Capacité avant de réduire les tampons", "icon": "warning", "tone": "bad"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un stock tampon contient 2 400 unités et la demande est de 1 200 par jour. Combien de "
                    "jours de stock cela fait-il ?",
        "options": ["Une demi-journée", "2 jours", "1 200 jours"],
        "correct": 1,
        "explanation": "Jours de stock = unités en attente ÷ demande journalière = 2 400 ÷ 1 200 = 2 jours.",
        "q_script": "Vérification rapide. Un stock tampon contient deux mille quatre cents unités, et la "
                    "demande est de mille deux cents par jour. Combien de jours de stock cela fait-il ? "
                    "Prenez quelques secondes.",
        "a_script": "Deux jours. Divisez les unités en attente par la demande journalière. Le tampon contient "
                    "exactement deux jours de production.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Rahul trouve 2 000 décodeurs en attente au test. Que doit faire l'équipe EN PREMIER ?",
        "options": ["Acheter tout de suite un autre testeur", "Confirmer la cause : capacité, arrêts, firmware ou lancement en lots",
                    "Diviser le tampon par deux pour forcer le flux"],
        "correct": 1,
        "explanation": "Une carte montre où regarder, pas pourquoi. Confirmez d'abord le mécanisme ; acheter un "
                       "testeur ou réduire le tampon à l'aveugle peut ne rien corriger, ou affamer la ligne.",
        "q_script": "Encore une, et cette fois c'est un scénario. Rahul trouve deux mille décodeurs en "
                    "attente au test. Que doit faire l'équipe en premier ? Réfléchissez.",
        "a_script": "Confirmez d'abord la cause. Cela peut être la capacité, des arrêts, le firmware, ou de "
                    "gros lancements en lots. Acheter un testeur ou réduire le tampon à l'aveugle peut ne "
                    "rien corriger, ou affamer la ligne.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
