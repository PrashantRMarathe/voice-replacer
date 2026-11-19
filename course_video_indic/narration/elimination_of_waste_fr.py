"""elimination_of_waste in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh elimination_of_waste_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ew_fr"
NAME = "elimination_of_waste_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Elimination of Waste": "éliminéïchone ov ouéïste",
    "TIMWOODS": "timme-oudz",
    "Pareto": "Paréto",
    "Gemba": "Guemba",
    "Muda": "Mouda",
    "ECRS": "eu cé erre esse",
    "FMEA": "effe emme eu a",
    "SOP": "esse o pé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Chaque mois, mille cinq cents barres de son repartaient en retouche. Chaque réparation "
    "coûtait quarante-deux roupies. Personne n'avait jamais fait le total. Ça vous dit "
    "quelque chose ? Dans cette leçon, vous allez découvrir Elimination of Waste. Vous verrez "
    "comment repérer le travail que votre client ne paierait pas, en supprimer la cause, et "
    "prouver le gain. Nous suivrons Deepak, responsable de production sur une ligne de barres "
    "de son."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Le gaspillage est tout ce que votre client ne paierait "
    "pas, mais jamais vos contrôles de sécurité ou de qualité. Trouvez-le avec des faits au "
    "Gemba, pas avec des opinions. Et supprimez la cause, puis prouvez le gain et "
    "maintenez-le. Voici votre action pour cette semaine. Parcourez votre ligne pendant "
    "trente minutes, et notez trois gaspillages sous forme de faits. Bravo d'avoir terminé "
    "cette leçon. Ensuite, vous découvrirez le FMEA, l'analyse des modes de défaillance et de "
    "leurs effets."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est vraiment le gaspillage",
        "points": [("Consomme des ressources, n'apporte aucune valeur au client", "Le gaspillage est toute activité"),
                   ("Pas une réduction de coûts ponctuelle", "L'éliminer n'est pas"),
                   ("Supprimer la cause, empêcher le retour", "supprimez sa cause racine")],
        "example": "La ligne de Deepak : 1 500 barres de son retouchées chaque mois.",
        "example_cue": "Sur la ligne de Deepak",
        "script": "Commençons par une définition. Le gaspillage est toute activité qui consomme du temps, "
                  "de la place, de la matière ou de l'effort, mais n'apporte aucune valeur à votre client. "
                  "L'éliminer n'est pas une campagne ponctuelle de réduction des coûts. Vous trouvez le "
                  "gaspillage, supprimez sa cause racine, et l'empêchez de revenir. Sur la ligne de Deepak, "
                  "mille cinq cents barres de son étaient retouchées chaque mois. Alors, comment décider ce "
                  "qui est de la valeur, et ce qui est du gaspillage ?",
    },
    {
        "key": "p02", "num": 2, "title": "Le test de la valeur",
        "points": [("Il transforme le produit", "Elle transforme le produit"),
                   ("Le client paierait pour cela", "Le client paierait"),
                   ("Bien fait, du premier coup", "C'est bien fait"),
                   ("Sinon : nécessaire, ou pur gaspillage", "Tout le reste")],
        "example": "Monter le haut-parleur : valeur. Le remonter après un bruit parasite : pur gaspillage.",
        "example_cue": "Monter le haut-parleur",
        "script": "Utilisez un test simple de la valeur. Une activité n'ajoute de la valeur que si trois "
                  "conditions sont réunies. Elle transforme le produit. Le client paierait pour cette "
                  "transformation. Et c'est bien fait, du premier coup. Tout le reste est soit nécessaire, "
                  "comme un contrôle légal, soit du pur gaspillage. Monter le haut-parleur, c'est de la "
                  "valeur. Le remonter après un bruit parasite, c'est du pur gaspillage. Quelle part de "
                  "votre journée passe ce test ?",
    },
    {
        "key": "p03", "num": 3, "title": "Pourquoi c'est important",
        "points": [("Flux plus rapide, délai plus court", "Le travail circule plus vite"),
                   ("Moins de défauts et de retouches", "Moins de défauts"),
                   ("Capacité libérée, sans nouvelle dépense", "Vous libérez des personnes"),
                   ("Les idées de ceux qui font le travail", "vos équipes peuvent")],
        "example": "L'objectif de Deepak : libérer de la capacité pour un nouveau modèle, sans ajouter "
                   "d'équipe.",
        "example_cue": "Deepak avait besoin",
        "script": "Pourquoi s'en donner la peine ? Parce que le gaspillage cache votre capacité. "
                  "Supprimez-le, et le travail circule plus vite, donc le délai raccourcit. Moins de "
                  "défauts signifie moins de retouches et moins de retours. Vous libérez des personnes, des "
                  "machines, de la place et de la trésorerie, sans nouvel investissement. Et vos équipes "
                  "peuvent utiliser leurs idées. Deepak avait besoin de place pour un nouveau modèle de "
                  "barre de son, sans ajouter d'équipe. D'où viendrait votre capacité libre ?",
    },
    {
        "key": "p04", "num": 4, "title": "Trois garde-fous",
        "points": [("Les contrôles sécurité et qualité ne sont pas du gaspillage", "N'appelez jamais gaspillage"),
                   ("Ne reportez pas le gaspillage sur les autres", "Ne reportez pas le gaspillage"),
                   ("Les personnes ne sont jamais le gaspillage", "les personnes ne sont jamais")],
        "example": "Le test audio final reste. Il protège le client.",
        "example_cue": "Sur la ligne de Deepak",
        "script": "Avant de commencer à couper, trois garde-fous. N'appelez jamais gaspillage un contrôle "
                  "de sécurité ou de qualité, sauf si une revue des risques l'approuve. Ne reportez pas le "
                  "gaspillage sur une autre équipe, un fournisseur ou votre client. Le déplacer, ce n'est "
                  "pas le supprimer. Et les personnes ne sont jamais le gaspillage. Les compétences "
                  "inutilisées, oui. Sur la ligne de Deepak, le test audio final reste. Il protège chaque "
                  "client. Alors, quels gaspillages cherchez-vous ?",
    },
    {
        "key": "p05", "num": 5, "title": "Les huit gaspillages",
        "points": [("Transport, stocks, mouvements, attente", "Transport, stocks"),
                   ("Surproduction, surtraitement", "surproduction"),
                   ("Défauts, compétences inutilisées", "défauts et compétences inutilisées")],
        "example": "Retenez-les sous le nom TIMWOODS.",
        "example_cue": "Retenez-les sous le nom TIMWOODS",
        "script": "Le Lean regroupe le gaspillage en huit types. Vous les reverrez dans la leçon sur le "
                  "Muda. Transport, stocks, mouvements et attente. Puis surproduction, et surtraitement, "
                  "c'est-à-dire faire plus que ce dont le client a besoin. Enfin, défauts et compétences "
                  "inutilisées. Retenez-les sous le nom TIMWOODS. Chacun d'eux se cache quelque part sur "
                  "chaque ligne, y compris la vôtre. Le vrai savoir-faire n'est pas de les nommer. C'est de "
                  "les voir sur votre propre ligne. Alors, comment les chercher ?",
    },
    {
        "key": "p06", "num": 6, "title": "La tournée des gaspillages",
        "points": [("Allez au Gemba pendant le travail normal", "Allez au Gemba"),
                   ("Notez des faits, n'accusez jamais", "Notez des faits"),
                   ("Où, quoi, combien de temps, à quelle fréquence", "Notez où ça s'est passé")],
        "example": "Fait : « Quatre opérateurs ont attendu 12 minutes des grilles manquantes. » Opinion : « "
                   "Le magasin est toujours en retard. »",
        "example_cue": "Comparez ces deux phrases",
        "script": "Faites une tournée des gaspillages. Allez au Gemba pendant la production normale, pas "
                  "pendant une visite. Notez des faits, et n'accusez jamais une personne. Notez où ça s'est "
                  "passé, quel produit, combien de temps et à quelle fréquence. Observez les personnes, les "
                  "pièces et les papiers. Comparez ces deux phrases. Quatre opérateurs ont attendu douze "
                  "minutes des grilles manquantes. Ou, le magasin est toujours en retard. Seule la première "
                  "vous dit où chercher, et quelle est l'ampleur. Laquelle pouvez-vous vraiment corriger ?",
    },
    {
        "key": "p07", "num": 7, "title": "Ce que Deepak a trouvé",
        "points": [("Attendre des kits en retard", "Les opérateurs attendaient"),
                   ("Tendre le bras et marcher pour les outils", "tendaient le bras et marchaient"),
                   ("Un double scan de code-barres", "le même code-barres"),
                   ("Retouches : barres de son qui grésillent", "le plus gros")],
        "example": "Les retouches étaient le plus gros : 1 500 barres de son qui grésillent par mois.",
        "example_cue": "le plus gros",
        "script": "En une heure, l'équipe de Deepak a rempli une page. Les opérateurs attendaient des kits "
                  "arrivés en retard. Ils tendaient le bras et marchaient pour les tournevis à chaque "
                  "cycle. L'emballage scannait le même code-barres deux fois, dans deux systèmes "
                  "différents. Mais le plus gros, c'était les retouches. Mille cinq cents barres de son par "
                  "mois échouaient au test de grésillement, et repartaient au banc de réparation. Comment "
                  "mesurer quelle part du temps est vraiment de la valeur ?",
    },
    {
        "key": "p08", "num": 8, "title": "Mesurer le flux",
        "points": [("Efficacité du flux = temps de valeur ÷ délai", "L'efficacité du flux est"),
                   ("18 min de valeur sur 240 min", "dix-huit minutes"),
                   ("Seulement 7,5 % du temps ajoute de la valeur", "sept et demi")],
        "example": "Une barre de son passe 4 heures dans l'usine. Seulement 18 minutes la transforment.",
        "example_cue": "Une barre de son passe",
        "script": "Mettez-y un chiffre. L'efficacité du flux est le temps à valeur ajoutée, divisé par le "
                  "délai total. Une barre de son passe quatre heures dans l'usine de Deepak. Seulement "
                  "dix-huit minutes la transforment réellement. C'est une efficacité du flux de sept et "
                  "demi pour cent. Tout le reste, c'est attendre, déplacer, contrôler ou réparer. Pas de "
                  "panique. C'est normal au départ. Mais quel gaspillage attaquer en premier ?",
    },
    {
        "key": "p09", "num": 9, "title": "Trouver la cause racine",
        "points": [("Pareto : choisir la plus grosse perte", "Utilisez un Pareto"),
                   ("Demander pourquoi, avec des preuves", "Puis demandez pourquoi"),
                   ("Corriger la cause, pas le symptôme", "Corrigez la cause")],
        "example": "Cause racine : pas de cheminement fixe pour le fil du haut-parleur, qui touchait donc la "
                   "membrane.",
        "example_cue": "Le fil n'avait pas",
        "script": "Utilisez un Pareto, et choisissez d'abord la plus grosse perte. Pour Deepak, c'était les "
                  "retouches. Puis demandez pourquoi, avec des preuves. Pourquoi les barres de son "
                  "grésillaient-elles ? Un fil du haut-parleur touchait la membrane. Pourquoi ? Le fil "
                  "n'avait pas de cheminement fixe, donc chaque opérateur le plaçait différemment. C'est "
                  "une cause de processus, pas une personne négligente. Corrigez la cause, pas le symptôme. "
                  "Alors, quelle contre-mesure choisiriez-vous ?",
    },
    {
        "key": "p10", "num": 10, "title": "Contre-mesures : ECRS",
        "points": [("Éliminer l'inutile", "Éliminez ce qui"),
                   ("Combiner tâches ou contrôles", "Combinez les tâches"),
                   ("Réordonner la séquence ou l'implantation", "Réordonnez"),
                   ("Simplifier ce qui reste", "Simplifiez")],
        "example": "Un clip de guidage du fil, des chariots de kits en ligne, un scan au lieu de deux.",
        "example_cue": "L'équipe de Deepak a choisi",
        "script": "Pensez ECRS. Éliminez ce qui n'est pas nécessaire. Combinez les tâches ou contrôles qui "
                  "vont ensemble. Réordonnez la séquence ou l'implantation. Simplifiez ce qui reste, et "
                  "rendez-le visuel. L'équipe de Deepak a choisi trois changements. Un petit clip qui guide "
                  "le fil du haut-parleur par un seul chemin. Des chariots de kits livrés à la ligne chaque "
                  "heure. Et un seul scan à l'emballage au lieu de deux. Quelle lettre de ECRS correspond à "
                  "chacun ?",
    },
    {
        "key": "p11", "num": 11, "title": "Le coût des défauts",
        "points": [("Internes : rebut, retouche, retest", "Les défaillances internes"),
                   ("Externes : retours, garantie, transport", "Les défaillances externes"),
                   ("Chaque réparation cache plus de gaspillage", "chaque réparation")],
        "example": "Retouche : ₹42 par barre de son, 1 500 par mois.",
        "example_cue": "Chaque retouche",
        "script": "Les défauts sont le gaspillage le plus coûteux. Les défaillances internes, ce sont le "
                  "rebut, la retouche, le retest et les lignes arrêtées. Les défaillances externes, ce sont "
                  "les retours, les réclamations sous garantie et les transports urgents. Et chaque "
                  "réparation cache plus de gaspillage, comme la manutention, l'attente et les papiers. Une "
                  "barre de son qui grésillait était ouverte, son fil repassé, retestée et enregistrée à "
                  "nouveau. Chaque retouche sur la ligne de Deepak coûtait quarante-deux roupies. À mille "
                  "cinq cents par mois, ça montait vite. Alors, le clip a-t-il marché ?",
    },
    {
        "key": "p12", "num": 12, "title": "Les résultats",
        "points": [("Retouches : de 1 500 à 300 par mois", "Les retouches sont passées"),
                   ("Rendement au premier passage jusqu'à 99 %", "Le rendement au premier passage"),
                   ("Prendre les outils : de 22 s à 13 s", "prendre les outils")],
        "example": "Mêmes personnes, même équipe. De la place pour le nouveau modèle.",
        "example_cue": "Mêmes personnes",
        "script": "Oui, après un essai de quatre semaines. Les retouches sont passées de mille cinq cents à "
                  "trois cents barres de son par mois. Le rendement au premier passage est monté à "
                  "quatre-vingt-dix-neuf pour cent. Avec les chariots de kits et les outils à portée de "
                  "main, prendre les outils est passé de vingt-deux à treize secondes par cycle. Mêmes "
                  "personnes, même équipe, et il y a maintenant de la place pour le nouveau modèle. Mais "
                  "combien cela valait-il en argent ?",
    },
    {
        "key": "p13", "num": 13, "title": "Prouver l'argent",
        "points": [("Économies = coût évité − coût de la solution", "Les économies sont"),
                   ("Séparez économies dures et capacité", "Séparez les économies dures"),
                   ("La finance confirme les chiffres", "La finance doit confirmer")],
        "example": "1 200 retouches de moins × ₹42 × 12 mois ≈ ₹6 lakh. Moins ₹1,2 lakh pour la solution : ≈ "
                   "₹4,8 lakh net.",
        "example_cue": "Mille deux cents retouches de moins",
        "script": "Les économies sont le coût que vous évitez, moins le coût de la solution. Mille deux "
                  "cents retouches de moins par mois, à quarante-deux roupies, sur un an. Cela fait environ "
                  "six cent mille roupies. Les clips, les chariots et le changement de système ont coûté "
                  "environ cent vingt mille. Le bénéfice net de la première année est donc d'environ quatre "
                  "cent quatre-vingt mille roupies. Séparez les économies dures de la capacité libérée. Et "
                  "la finance doit confirmer les chiffres. Comment faire durer le résultat ?",
    },
    {
        "key": "p14", "num": 14, "title": "Faire durer",
        "points": [("Mettre à jour le SOP, l'implantation, la formation", "Mettez à jour le SOP"),
                   ("Tableau quotidien : cible, réel, écart, action", "Un tableau quotidien"),
                   ("Audit à 7, 30 et 90 jours", "Auditez à sept")],
        "example": "L'audit de Deepak au jour 30 : une équipe avait arrêté d'utiliser le clip. Corrigé le "
                   "jour même.",
        "example_cue": "Au jour trente",
        "script": "Faites de la nouvelle méthode la méthode normale. Mettez à jour le SOP, l'implantation "
                  "et la formation. Un tableau quotidien montre la cible, le réel, l'écart et l'action, "
                  "avec un responsable. Auditez à sept, trente et quatre-vingt-dix jours, car la dérive est "
                  "silencieuse. Au jour trente, une équipe avait arrêté d'utiliser le clip. L'équipe de "
                  "Deepak l'a trouvé, et corrigé le jour même. Votre audit l'aurait-il repéré ?",
    },
    {
        "key": "p15", "num": 15, "title": "Votre plan sur 30 jours",
        "points": [("Jours 1–7 : choisir un produit, parcourir, cartographier", "La première semaine"),
                   ("Jours 8–18 : Pareto, cause racine, pilote", "Pendant les onze jours suivants"),
                   ("Jours 19–30 : mesurer, standardiser, auditer", "Pendant les douze derniers jours")],
        "example": "Puis partagez-le : d'autres lignes copient ce qui a marché, après avoir vérifié que ça "
                   "convient.",
        "example_cue": "Puis partagez-le",
        "script": "Voici un plan sur trente jours que vous pouvez commencer maintenant. La première "
                  "semaine, choisissez une famille de produits, parcourez le Gemba, et cartographiez le "
                  "flux. Pendant les onze jours suivants, utilisez un Pareto, trouvez la cause racine, et "
                  "menez un petit pilote. Pendant les douze derniers jours, mesurez le résultat, mettez à "
                  "jour le standard, et auditez-le. Puis partagez-le, pour que d'autres lignes copient ce "
                  "qui a marché. Quel produit parcourrez-vous en premier ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Aucune valeur pour le client", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Pas des coupes ponctuelles", "icon": "calendar", "with": 1},
        {"label": "Supprimer la cause", "icon": "key", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 1500, "icon": "wave", "label": "barres de son retouchées chaque mois",
                 "unit": "La ligne de Deepak", "with": "example"}},
    "p02": {"type": "steps", "items": [
        {"label": "Transforme le produit", "with": 0},
        {"label": "Le client paierait", "with": 1},
        {"label": "Bon du premier coup", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Remonter après un bruit parasite", "sub": "Pur gaspillage", "icon": "wrench", "tone": "bad", "with": "example"},
            {"label": "Monter le haut-parleur", "sub": "Valeur", "icon": "wave", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Flux plus rapide", "icon": "chartDown", "with": 0},
        {"label": "Moins de défauts", "icon": "check", "with": 1},
        {"label": "Capacité libérée", "icon": "box", "with": 2},
        {"label": "Idées des équipes", "icon": "person", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Garder les contrôles sécurité et qualité", "icon": "shield", "tone": "good", "with": 0},
        {"label": "Ne pas reporter le gaspillage", "icon": "sequence", "with": 1},
        {"label": "Les personnes ne sont pas du gaspillage", "icon": "person", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Transport", "icon": "sequence", "with": 0},
        {"label": "Stocks", "icon": "stack", "with": 0},
        {"label": "Mouvements", "icon": "walk", "with": 0},
        {"label": "Attente", "icon": "clock", "with": 0},
        {"label": "Surproduction", "icon": "box", "with": 1},
        {"label": "Surtraitement", "icon": "gear", "with": 1},
        {"label": "Défauts", "icon": "cross", "with": 2},
        {"label": "Compétences inutilisées", "icon": "person", "with": 2}]},
    "p06": {"type": "flow", "items": [
        {"label": "Production normale", "icon": "walk", "with": 0},
        {"label": "Des faits, pas de reproche", "icon": "clipboard", "with": 1},
        {"label": "Où · combien de temps · à quelle fréquence", "icon": "clock", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "« Le magasin est toujours en retard »", "sub": "Opinion", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "« 4 ont attendu 12 min des grilles »", "sub": "Fait", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Kits en retard", "icon": "clock", "tone": "bad", "with": 0},
        {"label": "Prendre les outils", "icon": "walk", "tone": "bad", "with": 1},
        {"label": "Double scan", "icon": "barcode", "tone": "bad", "with": 2},
        {"label": "Barres de son qui grésillent", "icon": "wave", "tone": "bad", "with": 3}]},
    "p08": {"type": "compare", "before": {"label": "Délai", "value": 240}, "after": {"label": "Valeur ajoutée", "value": 18},
            "unit": "minutes par barre de son", "note": "Efficacité du flux 7,5 %", "with": 1},
    "p09": {"type": "steps", "items": [
        {"label": "Les barres de son grésillent", "with": 1},
        {"label": "Le fil touche la membrane", "with": 1},
        {"label": "Pas de cheminement fixe du fil", "with": "example"}]},
    "p10": {"type": "steps", "items": [
        {"label": "Éliminer", "with": 0}, {"label": "Combiner", "with": 1},
        {"label": "Réordonner", "with": 2}, {"label": "Simplifier", "with": 3}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Clip de guidage du fil", "icon": "shape", "tone": "good", "with": "example"},
            {"label": "Chariots de kits chaque heure", "icon": "box", "with": "example"},
            {"label": "Un scan, pas deux", "icon": "barcode", "with": "example"}]}},
    "p11": {"type": "icons", "items": [
        {"label": "Internes", "sub": "Rebut, retouche, retest", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Externes", "sub": "Retours, garantie", "icon": "box", "tone": "bad", "with": 1},
        {"label": "Cachés", "sub": "Manutention, attente, papiers", "icon": "clock", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 42, "prefix": "₹", "icon": "wrench", "label": "par retouche",
                 "unit": "1 500 retouches par mois", "with": "example"}},
    "p12": {"type": "compare", "before": {"label": "Avant", "value": 1500}, "after": {"label": "Après", "value": 300},
            "unit": "barres de son retouchées par mois", "note": "FPY 99 % · prise d'outils 22 s → 13 s", "with": 0},
    "p13": {"type": "stat", "value": 4.8, "decimals": 1, "prefix": "₹", "suffix": " lakh", "icon": "chartUp",
            "label": "bénéfice net, première année", "unit": "₹6 lakh évités − ₹1,2 lakh pour la solution", "with": "example"},
    "p14": {"type": "timeline", "items": [
        {"label": "Standard mis à jour", "sub": "Jour 0", "icon": "clipboard", "with": 0},
        {"label": "Audit", "sub": "Jour 7", "icon": "search", "with": 2},
        {"label": "Dérive repérée", "sub": "Jour 30", "icon": "warning", "with": "example"},
        {"label": "Audit", "sub": "Jour 90", "icon": "check", "tone": "good", "with": 2}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Parcourir et cartographier", "sub": "Jours 1–7", "icon": "walk", "with": 0},
        {"label": "Cause et pilote", "sub": "Jours 8–18", "icon": "search", "with": 1},
        {"label": "Prouver et maintenir", "sub": "Jours 19–30", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un produit passe 300 minutes dans l'usine, mais seulement 30 minutes le transforment. "
                    "Quelle est l'efficacité du flux ?",
        "options": ["10%", "30%", "90%"],
        "correct": 0,
        "explanation": "Efficacité du flux = temps à valeur ajoutée ÷ délai total = 30 ÷ 300 = 10 %. Les 90 % "
                       "restants, c'est attendre, déplacer, contrôler ou réparer.",
        "q_script": "Vérification rapide. Un produit passe trois cents minutes dans l'usine. Seulement trente "
                    "minutes le transforment réellement. Quelle est l'efficacité du flux ? Prenez quelques "
                    "secondes.",
        "a_script": "C'est dix pour cent. Divisez le temps à valeur ajoutée par le délai total. Le reste, "
                    "c'est attendre, déplacer, contrôler ou réparer.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Pour réduire le temps de cycle, une équipe propose de supprimer le test audio final. Que "
                    "faut-il faire ?",
        "options": ["Le supprimer : les tests ne transforment pas le produit",
                    "Le garder sauf si une revue des risques l'approuve, et réduire les défauts qu'il attrape",
                    "Déplacer le test chez le client"],
        "correct": 1,
        "explanation": "Les contrôles qualité obligatoires ne sont pas un gaspillage à couper sur un coup de "
                       "tête. Gardez le test sauf si une revue des risques approuve un changement, et attaquez "
                       "les défauts qui sont derrière. Le déplacer chez le client ne fait que déplacer le "
                       "gaspillage.",
        "q_script": "Encore une, et cette fois c'est un scénario. Pour réduire le temps de cycle, une équipe "
                    "veut supprimer le test audio final. Que faut-il faire ? Réfléchissez.",
        "a_script": "Gardez le test, sauf si une revue des risques approuve un changement. Puis attaquez les "
                    "défauts qu'il attrape. Le déplacer chez le client ne fait que déplacer le gaspillage.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
