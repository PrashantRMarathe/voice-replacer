"""why_why in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh why_why_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ww_fr"
NAME = "why_why_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "X-Matrix": "ixe matrix",
    "Why-Why": "ouaï ouaï",
    "Pareto": "Paréto",
    "Gemba": "Guemba",
    "5W2H": "cinq double vé deux ache",
    "FMEA": "effe emme eu a",
    "HDMI": "ache dé emme i",
    "SOP": "esse o pé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Vingt et un téléphones ont échoué à la charge au test final. La première réponse est "
    "venue vite. Erreur de l'opérateur. Deux jours plus tard, c'est arrivé de nouveau. Ça "
    "vous dit quelque chose ? Dans cette leçon, vous allez découvrir l'analyse Why-Why, "
    "souvent appelée les cinq pourquoi. Vous verrez comment dépasser la réponse facile, "
    "jusqu'à une cause que vous pouvez prouver et maîtriser. Nous suivrons Neha, ingénieure "
    "qualité sur une ligne de téléphones mobiles, qui fait exactement cela."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Partez d'un problème précis, et protégez d'abord votre "
    "client. Appuyez chaque pourquoi sur une preuve, et testez-le avant de l'appeler cause "
    "racine. Et corrigez à la fois comment c'est arrivé, et pourquoi ça s'est échappé. Voici "
    "votre action pour cette semaine. Prenez un défaut répété, et écrivez son énoncé 5W2H. "
    "Bravo d'avoir terminé cette leçon. Ensuite, vous découvrirez la X-Matrix, qui relie la "
    "stratégie à l'action."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le Why-Why",
        "points": [("Demander pourquoi, encore et encore, avec des faits", "L'analyse Why-Why veut dire"),
                   ("Cinq n'est pas une règle", "mais cinq n'est pas une règle"),
                   ("S'arrêter à une cause que l'on peut prouver et maîtriser", "Vous vous arrêtez quand")],
        "example": "L'échec de charge est le symptôme : la mise en place du connecteur, une carte abîmée, le "
                   "contact du gabarit ou le réglage du testeur pourraient le causer.",
        "example_cue": "Sur la ligne de Neha",
        "script": "Voici l'idée centrale. L'analyse Why-Why veut dire demander pourquoi un problème est "
                  "arrivé, encore et encore, avec des faits derrière chaque réponse. On l'appelle souvent "
                  "les cinq pourquoi, mais cinq n'est pas une règle. Vous vous arrêtez quand vous atteignez "
                  "une cause que vous pouvez prouver et maîtriser. Sur la ligne de Neha, l'échec de charge "
                  "est le symptôme. Cela pourrait être la mise en place du connecteur, une carte abîmée, le "
                  "contact du gabarit, ou le réglage du testeur. Aucune n'est la cause racine tant qu'elle "
                  "n'est pas testée. Alors, comment cela s'articule-t-il avec les autres outils ?",
    },
    {
        "key": "p02", "num": 2, "title": "Why-Why et analyse des causes racines",
        "points": [("Un outil dans l'analyse des causes racines", "Le Why-Why est un outil"),
                   ("Aller au lieu réel, voir le produit réel", "Allez au lieu réel"),
                   ("Quelle preuve appuie ce pourquoi ?", "demandez quelle preuve"),
                   ("L'action humaine est un indice, pas la réponse", "Et traitez l'action humaine")],
        "example": "Vis manquantes sur une ligne audio : « l'opérateur a oublié » ne suffisait pas — "
                   "l'équipe a vérifié le chargeur et la séquence.",
        "example_cue": "Quand des vis ont manqué",
        "script": "Le Why-Why est un outil dans l'analyse des causes racines. L'arête de poisson, les "
                  "diagrammes de Pareto et les expériences l'accompagnent. Il marche le mieux pour une "
                  "chaîne claire de cause à effet. Allez au lieu réel, et regardez le produit réel. À "
                  "chaque étape, demandez quelle preuve appuie ce pourquoi. Et traitez l'action humaine "
                  "comme un indice, pas comme la réponse finale. Quand des vis ont manqué sur une ligne "
                  "audio, l'opérateur a oublié ne suffisait pas. L'équipe a vérifié le chargeur et la "
                  "séquence. Alors, par où commencer ?",
    },
    {
        "key": "p03", "num": 3, "title": "Étape 1 : définir avec le 5W2H",
        "points": [("Un énoncé de problème précis", "Partez d'un énoncé précis"),
                   ("5W2H : quoi, où, quand, comment trouvé, combien", "Utilisez le 5W2H"),
                   ("Inclure le dernier état bon connu", "Incluez le dernier état bon")],
        "example": "Ligne 2 : 21 téléphones sur 700 (3 %) ont échoué à la charge après le changement de "
                   "gabarit de 11 h ; l'équipe d'avant était sous 0,5 %.",
        "example_cue": "Sur la ligne deux",
        "script": "Partez d'un énoncé précis du problème. Un problème vague reçoit des réponses vagues. "
                  "Utilisez le 5W2H. Ce qui a échoué, où, quand, comment cela a été trouvé, et combien. "
                  "Incluez le dernier état bon connu. Voici l'énoncé de Neha. Sur la ligne deux, vingt et "
                  "un téléphones sur sept cents ont échoué à la charge. C'est trois pour cent, juste après "
                  "un changement de gabarit à onze heures. L'équipe d'avant était sous un demi pour cent. "
                  "Remarquez tout ce que cela vous dit déjà. Mais que faire des téléphones déjà fabriqués ?",
    },
    {
        "key": "p04", "num": 4, "title": "Étape 2 : confiner d'abord",
        "points": [("Protéger d'abord votre client", "protégez votre client"),
                   ("Trouver le dernier point bon connu", "Trouvez le dernier point bon"),
                   ("Bloquer le stock physiquement et dans le système", "Bloquez ce stock"),
                   ("Réconcilier chaque unité", "Puis réconciliez chaque unité")],
        "example": "Trier à 100 % protège le client — cela ne prouve pas que vous avez supprimé la cause.",
        "example_cue": "Trier à cent pour cent",
        "script": "Avant d'analyser, protégez votre client. Le confinement limite le risque pendant "
                  "l'enquête. Trouvez le dernier point bon connu, et chaque numéro de série ou lot fabriqué "
                  "depuis. Bloquez ce stock physiquement, et aussi dans le système. Puis réconciliez chaque "
                  "unité. Triée, défaillante, retouchée, libérée ou en attente. Neha a bloqué chaque "
                  "téléphone fabriqué depuis le changement de gabarit. Mais voici un piège. Trier à cent "
                  "pour cent protège le client. Cela ne prouve pas que vous avez supprimé la cause. Alors, "
                  "et ensuite ?",
    },
    {
        "key": "p05", "num": 5, "title": "Étape 3 : les faits au Gemba",
        "points": [("Comparer unités défaillantes et bonnes connues", "comparez les unités défaillantes"),
                   ("Vérifier réglages, gabarits, versions, lots", "Vérifiez les réglages"),
                   ("Préserver les preuves avant d'ajuster", "Préservez les preuves"),
                   ("Vu · source · pourrait signifier", "Tenez trois colonnes")],
        "example": "Neha a photographié et étiqueté chaque téléphone défaillant par numéro de série, puis a "
                   "extrait les journaux du testeur et de maintenance.",
        "example_cue": "Neha a photographié",
        "script": "Votre analyse ne vaut que ce que valent vos preuves. Allez au Gemba, et comparez les "
                  "unités défaillantes à des unités bonnes connues. Vérifiez les réglages, les gabarits, "
                  "l'étalonnage, les versions logicielles et les lots fournisseurs. Préservez les preuves "
                  "avant que quelqu'un n'ajuste quoi que ce soit. Neha a photographié et étiqueté chaque "
                  "téléphone défaillant par numéro de série. Puis elle a extrait les journaux du testeur et "
                  "les registres de maintenance. Tenez trois colonnes. Ce que vous avez vu, d'où ça vient, "
                  "et ce que ça pourrait signifier. Vous êtes maintenant prêt à demander pourquoi.",
    },
    {
        "key": "p06", "num": 6, "title": "Étape 4 : construire la chaîne",
        "points": [("Partir de l'événement observé", "Écrivez l'événement observé"),
                   ("Chaque flèche est une affirmation vérifiable", "Chaque flèche est une affirmation"),
                   ("Des faits, pas « négligence »", "Utilisez des faits précis"),
                   ("Ramifier quand les causes se combinent", "Ramifiez la chaîne")],
        "example": "Mauvaise étiquette de carton → ancienne impression → le logiciel l'a permis → imprimante "
                   "non reliée au produit scanné.",
        "example_cue": "Une mauvaise étiquette de carton",
        "script": "Écrivez l'événement observé en haut. Demandez pourquoi c'est arrivé. Puis demandez "
                  "pourquoi cette condition existait. Chaque flèche est une affirmation que vous devez "
                  "pouvoir vérifier. Demandez pourquoi le défaut s'est produit, jamais qui blâmer. Utilisez "
                  "des faits précis, pas des étiquettes comme négligence. Voici un exemple à l'emballage. "
                  "Une mauvaise étiquette de carton venait d'une ancienne impression. Le logiciel l'a "
                  "permis, parce que l'imprimante n'était pas reliée au produit scanné. Ramifiez la chaîne "
                  "chaque fois que plus d'une cause a contribué.",
    },
    {
        "key": "p07", "num": 7, "title": "Apparition, fuite et système",
        "points": [("Apparition : comment le défaut a été créé", "La cause d'apparition"),
                   ("Fuite : pourquoi personne ne l'a attrapé", "La cause de fuite"),
                   ("Système : pourquoi les contrôles n'ont pas vu le risque", "Et la cause système"),
                   ("Chacune demande sa propre correction", "Chacune demande")],
        "example": "Le gabarit permet une mise en place partielle de la batterie (apparition) ; le test "
                   "final n'a pas vu le contact intermittent (fuite).",
        "example_cue": "Sur la ligne de Neha",
        "script": "Une analyse complète a en général plus d'une chaîne. La cause d'apparition explique "
                  "comment le défaut a été créé. La cause de fuite explique pourquoi personne ne l'a "
                  "attrapé. Et la cause système explique pourquoi vos contrôles n'ont pas vu le risque au "
                  "départ. Sur la ligne de Neha, un gabarit pouvait permettre une mise en place partielle "
                  "de la batterie. C'est l'apparition. Le test final ne vérifiait pas le contact "
                  "intermittent. C'est la fuite. Chacune demande sa propre correction. Mais que faire s'il "
                  "y a beaucoup de causes possibles ?",
    },
    {
        "key": "p08", "num": 8, "title": "Arête de poisson et Pareto",
        "points": [("Arête de poisson : 6 groupes de causes", "Une arête de poisson regroupe"),
                   ("Pareto : classer par fréquence", "Un diagramme de Pareto classe"),
                   ("Les risques sécurité rares comptent quand même", "Mais un risque sécurité rare"),
                   ("Une arête de poisson, ce sont des suppositions, pas des preuves", "une arête de poisson est une liste")],
        "example": "Les deux premiers types de défauts de Neha représentaient 65 % du total — c'est là "
                   "qu'elle s'est concentrée d'abord.",
        "example_cue": "Les deux premiers types de Neha",
        "script": "Quand beaucoup de causes sont possibles, commencez large. Une arête de poisson regroupe "
                  "les idées par main-d'œuvre, machine, méthode, matière, mesure et milieu. Un diagramme de "
                  "Pareto classe les défauts selon leur fréquence. Les deux premiers types de Neha "
                  "représentaient soixante-cinq pour cent du total. C'est là qu'elle s'est concentrée "
                  "d'abord. Mais un risque sécurité rare compte quand même, même avec un faible nombre. Et "
                  "rappelez-vous, une arête de poisson est une liste de suppositions, pas une preuve. "
                  "Alors, comment prouver une cause ?",
    },
    {
        "key": "p09", "num": 9, "title": "Prouver la cause",
        "points": [("Prédire ce qui devrait changer", "Avant l'essai"),
                   ("Garder les autres facteurs fixes", "Gardez les autres facteurs fixes"),
                   ("Tester le bon et le mauvais, sur plusieurs équipes", "Testez les conditions bonnes et mauvaises")],
        "example": "Broches de gabarit bonnes contre usées, avec les mêmes pièces : les échecs ont suivi les "
                   "broches usées.",
        "example_cue": "Neha soupçonnait",
        "script": "Une chaîne logique ne suffit pas. Vous devez la tester. Avant l'essai, écrivez ce qui "
                  "devrait changer si votre cause est vraie. Gardez les autres facteurs fixes, comme le lot "
                  "de matière et la version du programme. Testez les conditions bonnes et mauvaises, sur "
                  "plusieurs équipes. Neha soupçonnait une broche de gabarit usée. Elle a essayé des "
                  "broches bonnes et des broches usées, avec les mêmes pièces. Les échecs ont suivi les "
                  "broches usées. Qu'est-ce qui lui aurait donné tort ? Des échecs restés avec les bonnes "
                  "broches.",
    },
    {
        "key": "p10", "num": 10, "title": "Action corrective et Poka Yoke",
        "points": [("Corriger la cause, pas le symptôme", "Corrigez maintenant la cause"),
                   ("La prévention technique bat les rappels", "La prévention technique"),
                   ("Corriger l'apparition + contrôle indépendant de la fuite", "Corrigez l'apparition"),
                   ("Mettre à jour le FMEA, le SOP, la formation", "Puis mettez à jour le FMEA")],
        "example": "Mauvaises étiquettes audio : l'imprimante exige maintenant d'abord un scan de série "
                   "correspondant. Reformer repose sur la mémoire.",
        "example_cue": "Pour les mauvaises étiquettes",
        "script": "Corrigez maintenant la cause, pas seulement le symptôme. La prévention technique bat les "
                  "rappels. Pensez gabarits détrompés, verrouillages par code-barres et capteurs de "
                  "présence. Corrigez l'apparition, et ajoutez un contrôle indépendant pour la fuite. Puis "
                  "mettez à jour le FMEA, le SOP et la formation. Pour les mauvaises étiquettes sur les "
                  "appareils audio, l'imprimante exige maintenant d'abord un scan de série correspondant. "
                  "Pourquoi reformer est-il souvent une correction faible ? Parce que cela repose sur la "
                  "mémoire, et la mémoire flanche. Comment savoir que votre correction a marché ?",
    },
    {
        "key": "p11", "num": 11, "title": "Vérifier et clôturer",
        "points": [("Terminé ≠ prouvé", "Terminer une action"),
                   ("Mise à l'épreuve : échantillons bons, mauvais, limites", "Mettez le nouveau contrôle à l'épreuve"),
                   ("Surveiller répétition et rendement", "Surveillez la répétition"),
                   ("Pas de nouveaux arrêts ni de faux rejets", "Vérifiez que vous n'avez pas")],
        "example": "La règle de clôture de Neha : zéro répétition sur 10 jours de production, mises à "
                   "l'épreuve réussies, chaque unité suspecte retrouvée.",
        "example_cue": "Neha a fixé une règle de clôture",
        "script": "Terminer une action n'est pas la même chose que prouver qu'elle marche. Mettez le "
                  "nouveau contrôle à l'épreuve avec des échantillons bons connus, mauvais connus et "
                  "limites. Surveillez la répétition et le rendement au premier passage sur plusieurs "
                  "équipes, modèles et changements de série. Vérifiez que vous n'avez pas créé de nouveaux "
                  "arrêts ni de faux rejets. Neha a fixé une règle de clôture avec son usine. Zéro "
                  "répétition sur dix jours de production, mises à l'épreuve réussies, et chaque unité "
                  "suspecte retrouvée. Votre usine doit fixer sa propre règle. Puis la qualité la signe.",
    },
    {
        "key": "p12", "num": 12, "title": "KPI du Why-Why",
        "points": [("Mesurer la rapidité et les résultats", "Mesurez à la fois la rapidité"),
                   ("Avancés : confinement rapide, actions vérifiées", "Les indicateurs avancés"),
                   ("Retardés : taux de défauts, répétition", "Les indicateurs retardés"),
                   ("Garder des définitions stables", "Gardez des définitions stables")],
        "example": "50 → 15 défauts = une baisse de 70 %. Coût de ₹1,2 lakh, ₹30 000 économisées par mois = "
                   "retour en 4 mois.",
        "example_cue": "Les défauts de Neha sont passés",
        "script": "Mesurez à la fois la rapidité et les résultats. Les indicateurs avancés incluent le "
                  "confinement rapide et les actions vérifiées. Les indicateurs retardés incluent le taux "
                  "de défauts et la répétition. Gardez des définitions stables, pour que personne "
                  "n'améliore un chiffre en le redéfinissant. Les défauts de Neha sont passés de cinquante "
                  "à quinze, à volume égal. C'est une baisse de soixante-dix pour cent. Sa correction a "
                  "coûté cent vingt mille roupies, et économise trente mille par mois. Elle est donc "
                  "rentabilisée en quatre mois. Lesquels de ces indicateurs votre équipe suit-elle "
                  "aujourd'hui ?",
    },
    {
        "key": "p13", "num": 13, "title": "Cas pratique : échec de charge",
        "points": [("Téléphone ou testeur ? Le tester d'abord", "Le défaut était-il dans le téléphone"),
                   ("Retestés sur un deuxième testeur : toujours en échec", "Elle a retesté les téléphones défaillants"),
                   ("Broche usée sur le gabarit d'assemblage", "Le connecteur de batterie était"),
                   ("Correction : broches neuves, limites de durée de vie, contrôle de réglage", "Sa correction a été")],
        "example": "Les téléphones défaillants ont de nouveau échoué sur un deuxième testeur : les "
                   "téléphones étaient vraiment défectueux.",
        "example_cue": "Ils y ont échoué aussi",
        "script": "Voici comment le cas de Neha s'est assemblé. Le défaut était-il dans le téléphone, ou "
                  "dans le testeur ? Elle a retesté les téléphones défaillants sur un deuxième testeur. Ils "
                  "y ont échoué aussi, donc les téléphones étaient vraiment défectueux. La chaîne était la "
                  "suivante. Le connecteur de batterie était à moitié enfoncé, parce qu'une broche à "
                  "ressort usée sur le nouveau gabarit d'assemblage ne l'enfonçait pas complètement. Elle "
                  "était usée parce qu'aucun intervalle de remplacement n'existait. Sa correction a été des "
                  "broches neuves, des limites de durée de vie, et un contrôle de réglage. Auriez-vous "
                  "vérifié le testeur d'abord ?",
    },
    {
        "key": "p14", "num": 14, "title": "Décodeur et audio",
        "points": [("Produits différents, preuves différentes", "Des produits différents demandent"),
                   ("Décodeur : soudure HDMI, firmware, testeur", "Sur un décodeur"),
                   ("Audio : tracer le kit, la séquence d'emballage, les scans", "Sur un appareil audio"),
                   ("Déployer les corrections prouvées sur les lignes similaires", "Une fois une correction prouvée")],
        "example": "Télécommande manquante : le kit l'a sautée, puis le carton s'est fermé sans scan de la "
                   "télécommande.",
        "example_cue": "Le kit a sauté la télécommande",
        "script": "Des produits différents demandent des preuves différentes. Sur un décodeur sans image, "
                  "vous vérifieriez la soudure HDMI, le firmware et les réglages du testeur. Et vous "
                  "demanderiez pourquoi le contrôle d'affichage en fin de ligne l'a raté. Sur un appareil "
                  "audio sans sa télécommande, vous traceriez le kit, la séquence d'emballage et les scans. "
                  "Le kit a sauté la télécommande. Puis le carton s'est fermé sans scan de la télécommande. "
                  "Une fois une correction prouvée, déployez-la aussi sur les lignes similaires. Prêt pour "
                  "le plan de déploiement ?",
    },
    {
        "key": "p15", "num": 15, "title": "Déploiement sur 90 jours",
        "points": [("Ligne pilote + quelques animateurs", "Commencez par une ligne pilote"),
                   ("Jours 1–30 : déclencheurs, rôles, modèles", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : enquêter, tester les hypothèses", "Pendant les trente suivants"),
                   ("Jours 61–90 : mettre à l'épreuve, mettre à jour, diffuser", "Pendant les trente derniers")],
        "example": "Auditer la présence de vraies pièces et de liens vérifiés — pas de beaux formulaires.",
        "example_cue": "Auditez la présence de vraies pièces",
        "script": "Intégrez le Why-Why au management quotidien. Commencez par une ligne pilote à haut "
                  "risque, et formez quelques animateurs. Pendant les trente premiers jours, définissez les "
                  "déclencheurs, les rôles et les modèles. Pendant les trente suivants, menez de vraies "
                  "enquêtes et testez vos hypothèses. Pendant les trente derniers, mettez les corrections à "
                  "l'épreuve, mettez les contrôles à jour, et diffusez les leçons. Auditez la présence de "
                  "vraies pièces et de liens vérifiés, pas de beaux formulaires. Rappelez-vous, demandez "
                  "pourquoi jusqu'à pouvoir prouver la cause. Puis rendez la répétition impossible.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Pourquoi ?", "sub": "Appuyé sur un fait", "icon": "search", "with": 0},
        {"label": "Pourquoi encore ?", "sub": "Cinq n'est pas une règle", "icon": "count", "with": 1},
        {"label": "Une cause que vous pouvez prouver et maîtriser", "icon": "key", "tone": "good", "with": 2}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Mise en place du connecteur", "icon": "pin", "with": "example"},
            {"label": "Carte abîmée", "icon": "chip", "with": "example"},
            {"label": "Contact du gabarit", "icon": "wrench", "with": "example"},
            {"label": "Réglage du testeur", "icon": "test", "with": "example"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Why-Why", "sub": "Un outil parmi d'autres", "icon": "search", "tone": "good", "with": 0},
        {"label": "Lieu réel, produit réel", "icon": "walk", "with": 1},
        {"label": "Une preuve pour chaque pourquoi", "icon": "clipboard", "with": 2},
        {"label": "Les personnes sont un indice", "icon": "person", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "L'opérateur a oublié", "sub": "Insuffisant", "icon": "person", "with": "example"},
            {"label": "Vérifier le chargeur et la séquence", "sub": "Faits", "icon": "search", "with": "example"}]}},
    "p03": {"type": "doc", "items": [
        {"label": "Énoncé du problème · Ligne 2", "icon": "label", "with": 0},
        {"label": "Quoi : échec de charge au test final", "icon": "power", "with": 1},
        {"label": "Quand : après le changement de gabarit de 11 h", "icon": "clock", "with": 1},
        {"label": "Combien : 21 téléphones sur 700 (3 %)", "icon": "count", "with": 1},
        {"label": "Dernier état bon : sous 0,5 %", "icon": "check", "with": 2}]},
    "p04": {"type": "flow", "items": [
        {"label": "Protéger le client", "icon": "shield", "with": 0},
        {"label": "Trouver le dernier point bon", "icon": "search", "with": 1},
        {"label": "Bloquer le stock : terrain et système", "icon": "lock", "with": 2},
        {"label": "Réconcilier chaque unité", "icon": "count", "tone": "good", "with": 3}]},
    "p05": {"type": "icons", "items": [
        {"label": "Défaillantes contre bonnes connues", "icon": "scale", "with": 0},
        {"label": "Réglages, versions, lots", "icon": "gear", "with": 1},
        {"label": "Préserver les preuves", "icon": "camera", "with": 2},
        {"label": "Vu · source · sens", "icon": "clipboard", "with": 3}]},
    "p06": {"type": "icons", "items": [
        {"label": "Partir de l'événement", "icon": "search", "with": 0},
        {"label": "Chaque flèche : une affirmation à vérifier", "icon": "check", "with": 1},
        {"label": "Des faits, pas des étiquettes", "icon": "cross", "tone": "bad", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Mauvaise étiquette de carton", "icon": "label", "tone": "bad", "with": "example"},
            {"label": "Ancienne impression", "icon": "sequence", "with": "example"},
            {"label": "Le logiciel l'a permis", "icon": "chip", "with": "example"},
            {"label": "Imprimante non reliée au scan", "icon": "barcode", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Apparition", "sub": "Comment il a été créé", "icon": "wrench", "with": 0},
        {"label": "Fuite", "sub": "Pourquoi personne ne l'a attrapé", "icon": "search", "with": 1},
        {"label": "Système", "sub": "Pourquoi les contrôles l'ont raté", "icon": "gear", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Le gabarit permet une mise en place partielle", "sub": "Apparition", "icon": "pin", "tone": "bad", "with": "example"},
            {"label": "Le test final rate le contact intermittent", "sub": "Fuite", "icon": "test", "tone": "bad", "with": "example"},
            {"label": "Une correction pour chacune", "icon": "check", "tone": "good", "with": 3}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Arête de poisson : 6 groupes", "icon": "gear", "with": 0},
        {"label": "Pareto : classer par nombre", "icon": "chartUp", "with": 1},
        {"label": "Risques sécurité rares", "icon": "warning", "tone": "bad", "with": 2},
        {"label": "Suppositions, pas preuves", "icon": "search", "with": 3}],
        "then": {"type": "bars", "label": "", "note": "Les deux premiers = 65 % des défauts", "with": "example", "items": [
            {"label": "Type 1", "value": 40, "tone": "bad", "with": "example"},
            {"label": "Type 2", "value": 25, "tone": "bad", "with": "example"},
            {"label": "Type 3", "value": 15, "with": "example"},
            {"label": "Type 4", "value": 12, "with": "example"},
            {"label": "Autre", "value": 8, "with": "example"}]}},
    "p09": {"type": "steps", "items": [
        {"label": "Prédire le changement", "with": 0}, {"label": "Fixer les autres facteurs", "with": 1},
        {"label": "Tester le bon et le mauvais", "with": 2}, {"label": "Sur plusieurs équipes", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Broches usées", "sub": "Les échecs ont suivi", "icon": "pin", "with": "example"},
            {"label": "Bonnes broches", "sub": "Les mêmes pièces ont réussi", "icon": "check", "with": "example"}]}},
    "p10": {"type": "ladder", "top": "LE PLUS FORT", "bottom": "LE PLUS FAIBLE", "items": [
        {"label": "Gabarit détrompé, verrouillage", "icon": "key", "with": 1},
        {"label": "Capteur de présence", "icon": "sensor", "with": 1},
        {"label": "Contrôle indépendant de la fuite", "icon": "search", "with": 2},
        {"label": "Reformation, rappels", "icon": "warning", "tone": "bad", "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Bonne connue", "icon": "check", "tone": "good", "with": 1},
        {"label": "Mauvaise connue", "icon": "cross", "tone": "bad", "with": 1},
        {"label": "Échantillons limites", "icon": "scale", "with": 1},
        {"label": "Répétition et rendement", "icon": "chartUp", "with": 2}],
        "then": {"type": "doc", "with": "example", "items": [
            {"label": "Règle de clôture · Ligne 2", "icon": "label", "with": "example"},
            {"label": "Zéro répétition en 10 jours de production", "icon": "calendar", "with": "example"},
            {"label": "Mises à l'épreuve réussies", "icon": "test", "with": "example"},
            {"label": "Chaque unité suspecte retrouvée", "icon": "count", "with": "example"},
            {"label": "La qualité signe", "icon": "person", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Rapidité et résultats", "icon": "clock", "with": 0},
        {"label": "Avancé : confinement rapide", "icon": "shield", "with": 1},
        {"label": "Retardé : défauts, répétitions", "icon": "chartDown", "with": 2},
        {"label": "Définitions stables", "icon": "scale", "with": 3}],
        "then": {"type": "compare", "before": {"label": "Avant", "value": 50}, "after": {"label": "Après", "value": 15},
                 "unit": "défauts de charge, volume égal", "note": "Une baisse de 70 % · retour en 4 mois", "with": "example"}},
    "p13": {"type": "flow", "items": [
        {"label": "Téléphone ou testeur ?", "icon": "search", "with": 0},
        {"label": "Deuxième testeur : toujours en échec", "icon": "test", "with": 1},
        {"label": "Broche usée du gabarit d'assemblage, pas d'intervalle de remplacement", "icon": "pin", "tone": "bad", "with": 2},
        {"label": "Broches neuves, limites de durée de vie, contrôle de réglage", "icon": "check", "tone": "good", "with": 3}]},
    "p14": {"type": "icons", "items": [
        {"label": "Décodeur", "sub": "HDMI, firmware, testeur", "icon": "chip", "with": 1},
        {"label": "Appareil audio", "sub": "Kit, séquence, scans", "icon": "wave", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Le kit a sauté la télécommande", "icon": "tray", "tone": "bad", "with": "example"},
            {"label": "Carton fermé, sans scan de la télécommande", "icon": "box", "tone": "bad", "with": "example"},
            {"label": "Diffuser la correction prouvée", "icon": "sequence", "tone": "good", "with": 3}]}},
    "p15": {"type": "timeline", "items": [
        {"label": "Déclencheurs, rôles, modèles", "sub": "Jours 1–30", "icon": "clipboard", "with": 1},
        {"label": "Enquêter, tester les hypothèses", "sub": "31–60", "icon": "search", "with": 2},
        {"label": "Mettre à l'épreuve, mettre à jour, diffuser", "sub": "61–90", "icon": "chartUp", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Le test final n'a pas détecté un connecteur de batterie à moitié enfoncé. Quel type de "
                    "cause est-ce ?",
        "options": ["Cause d'apparition", "Cause de fuite", "Cause système"],
        "correct": 1,
        "explanation": "Le défaut a été créé plus tôt (apparition). La cause de fuite explique pourquoi la "
                       "barrière de détection — ici, le test final — ne l'a pas attrapé.",
        "q_script": "Vérification rapide. Le test final n'a pas détecté un connecteur de batterie à moitié "
                    "enfoncé. Quel type de cause est-ce ? Prenez quelques secondes.",
        "a_script": "C'est une cause de fuite. Le défaut a été créé plus tôt. La fuite explique pourquoi nos "
                    "contrôles ne l'ont pas attrapé.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "30 cartons ont reçu de mauvaises étiquettes et quelqu'un dit « erreur de l'opérateur ». "
                    "Que doit faire l'équipe EN PREMIER ?",
        "options": ["Reformer l'opérateur et clôturer", "Confiner les cartons suspects, puis demander pourquoi le processus l'a permis",
                    "Mettre un panneau de rappel à l'emballage"],
        "correct": 1,
        "explanation": "Confinez d'abord, puis trouvez pourquoi le processus a permis une mauvaise étiquette. "
                       "Reformer ou un panneau reposent sur la mémoire, donc empêchent rarement la répétition.",
        "q_script": "Encore une, et cette fois c'est un scénario. Trente cartons ont reçu de mauvaises "
                    "étiquettes, et quelqu'un dit erreur de l'opérateur. Que doit faire l'équipe en premier ? "
                    "Réfléchissez.",
        "a_script": "Confinez d'abord les cartons suspects. Puis demandez pourquoi le processus a permis une "
                    "mauvaise étiquette. Reformer ou un panneau reposent sur la mémoire, donc empêchent "
                    "rarement la répétition.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
