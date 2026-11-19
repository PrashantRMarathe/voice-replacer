"""zero_defects in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh zero_defects_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "zd_fr"
NAME = "zero_defects_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Zero Defects": "zirô difèctse",
    "Poka Yoke": "Poka Yoké",
    "Crosby": "Crosbi",
    "Jidoka": "Djidoka",
    "Andon": "Anndone",
    "PFMEA": "pé effe emme eu a",
    "DPMO": "dé pé emme o",
    "Cpk": "cé pé ka",
    "PPM": "pé pé emme",
    "FPY": "effe pé i grec",
    "SOP": "esse o pé",
    "SKU": "esse ka u",
    "Cp": "cé pé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Un connecteur, mal enfoncé. Il a passé tous les contrôles visuels. Puis quatre cents "
    "téléphones sont revenus en retouche. Ça vous dit quelque chose ? Dans cette leçon, vous "
    "allez découvrir Zero Defects. Vous verrez comment mesurer la qualité honnêtement, et "
    "comment rendre impossibles des erreurs comme celle-là. Nous suivrons Priya, ingénieure "
    "de ligne sur une ligne d'assemblage de téléphones mobiles, qui fait exactement cela."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Prévenez les défauts, ne vous contentez pas de les "
    "inspecter. Mesurez honnêtement, avec des définitions claires. Et quand quelque chose "
    "échoue, corrigez le système, pas la personne. Voici votre action pour cette semaine. "
    "Choisissez un défaut qui revient sans cesse sur votre ligne, et demandez-vous comment le "
    "rendre impossible. Bravo d'avoir terminé cette leçon, et tout le cours, de A à Z. "
    "Maintenant, allez faire une amélioration sur votre ligne."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Sens et philosophie",
        "points": [("Chaque défaut peut être évité", "traite chaque défaut comme évitable"),
                   ("Bien du premier coup", "Vous visez à faire"),
                   ("Concevoir et maîtriser le processus", "En concevant et en maîtrisant"),
                   ("Une discipline, pas une promesse", "C'est une discipline")],
        "example": "La ligne de Priya : un poste confirme maintenant que le connecteur est enfoncé avant le "
                   "test électrique.",
        "example_cue": "Sur la ligne de Priya",
        "script": "Voici l'idée centrale. Zero Defects traite chaque défaut comme évitable, pas comme un "
                  "coût normal de l'activité. Vous visez à faire chaque unité bien du premier coup. Comment "
                  "? En concevant et en maîtrisant bien le processus. C'est une discipline, pas une "
                  "promesse que rien ne tournera jamais mal. Sur la ligne de Priya, un poste confirme "
                  "maintenant que le connecteur est enfoncé avant le test électrique. Alors, d'où vient "
                  "cette idée ?",
    },
    {
        "key": "p02", "num": 2, "title": "Histoire et valeur pour l'entreprise",
        "points": [("Crosby, années 1960 : qualité = conformité aux exigences", "Philip Crosby a rendu"),
                   ("Le Lean ajoute la qualité intégrée et le détrompage", "Le Lean moderne ajoute"),
                   ("Corriger le système, pas la personne", "vous corrigez le système"),
                   ("Les responsables lèvent les obstacles ; les opérateurs arrêtent et réagissent", "Les responsables lèvent les obstacles")],
        "example": "Pour gagner le soutien des dirigeants, il faut montrer l'argent.",
        "example_cue": "Mais pour gagner ce soutien",
        "script": "Philip Crosby a rendu Zero Defects célèbre dans les années soixante. Sa définition est "
                  "simple. La qualité, c'est la conformité à des exigences clairement définies. Le Lean "
                  "moderne ajoute la qualité intégrée, le travail standard et le détrompage. Voici le "
                  "changement clé. Quand un défaut arrive, vous corrigez le système, au lieu de blâmer la "
                  "personne. Les responsables lèvent les obstacles, et on fait confiance aux opérateurs "
                  "pour arrêter et réagir. Mais pour gagner ce soutien, il faut montrer l'argent.",
    },
    {
        "key": "p03", "num": 3, "title": "Le coût de la non-qualité",
        "points": [("Défaillance interne : rebut, retouche, retest", "Les défaillances internes comprennent"),
                   ("Défaillance externe : garantie, retours", "Les défaillances externes comprennent"),
                   ("Cachés : retards, manutention, capacité perdue", "Puis viennent les coûts cachés"),
                   ("Prévenir coûte bien moins cher", "Prévenir coûte bien moins cher")],
        "example": "La ligne de Priya : 400 téléphones retouchés = ₹32 000 de retouche directe — avant même "
                   "une seule expédition en retard.",
        "example_cue": "Le mois dernier, la ligne de Priya",
        "script": "La non-qualité coûte plus cher que vous ne le pensez. Les défaillances internes "
                  "comprennent le rebut, la retouche et le retest. Les défaillances externes comprennent "
                  "les réclamations sous garantie et les retours. Puis viennent les coûts cachés, comme les "
                  "retards, la manutention supplémentaire et la capacité perdue. Le mois dernier, la ligne "
                  "de Priya a retouché quatre cents téléphones. Cela fait trente-deux mille roupies de "
                  "retouche directe, avant même une seule expédition en retard. Prévenir coûte bien moins "
                  "cher. Alors, comment mesurer où la qualité se perd ?",
    },
    {
        "key": "p04", "num": 4, "title": "FTR, FPY et RTY",
        "points": [("Bien du premier coup : aucune correction", "Bien du premier coup veut dire"),
                   ("Rendement au premier passage : réussir une étape du premier coup", "Le rendement au premier passage est"),
                   ("Rendement cumulé : multiplier chaque étape", "Le rendement cumulé multiplie")],
        "example": "Trois étapes à 98 % chacune ne donnent qu'environ 94 % ensemble.",
        "example_cue": "Trois étapes à quatre-vingt-dix-huit",
        "script": "Commencez par trois mesures de rendement. Bien du premier coup veut dire respecter les "
                  "exigences sans aucune correction. Le rendement au premier passage est la part des unités "
                  "qui réussissent une étape du premier coup. Le rendement cumulé multiplie les rendements "
                  "de chaque étape. Voici le piège. Trois étapes à quatre-vingt-dix-huit pour cent chacune, "
                  "cela paraît très bien. Ensemble, elles ne donnent qu'environ quatre-vingt-quatorze pour "
                  "cent. Quelle étape de votre ligne tire discrètement le total vers le bas ?",
    },
    {
        "key": "p05", "num": 5, "title": "PPM, DPMO et cibles",
        "points": [("PPM : unités défectueuses par million", "Le PPM compte"),
                   ("DPMO : défauts par million d'opportunités", "Le DPMO compte"),
                   ("Indiquer la taille d'échantillon et le périmètre", "Indiquez toujours votre échantillon"),
                   ("Ne jamais comparer PPM et DPMO", "Et ne comparez jamais")],
        "example": "Priya a trouvé 25 mauvais téléphones sur 50 000 = 500 PPM.",
        "example_cue": "Priya a trouvé vingt-cinq",
        "script": "Les taux de défauts ont besoin d'un dénominateur précis. Le PPM compte les unités "
                  "défectueuses par million. Le DPMO compte les défauts par million d'opportunités. Vous "
                  "devez donc d'abord définir les opportunités sur chaque unité. Priya a trouvé vingt-cinq "
                  "mauvais téléphones sur cinquante mille. Cela fait cinq cents PPM. Indiquez toujours "
                  "votre échantillon et votre périmètre. Et ne comparez jamais un PPM avec un DPMO. "
                  "Maintenant, comment empêcher les défauts d'être créés ?",
    },
    {
        "key": "p06", "num": 6, "title": "La qualité à la source",
        "points": [("Chaque opération est responsable de sa production", "chaque opération est responsable"),
                   ("Poste suivant = votre client", "Traitez le poste suivant"),
                   ("Vérifier entrées et réglage, suivre le SOP", "Vérifiez vos entrées"),
                   ("Anormal ? Arrêter, isoler, escalader", "Si quelque chose semble anormal")],
        "example": "Ligne de décodeurs : les opérateurs vérifient le pad thermique et le couple des vis "
                   "avant qu'une unité avance.",
        "example_cue": "Sur la ligne de décodeurs",
        "script": "La qualité à la source veut dire que chaque opération est responsable de sa propre "
                  "production. Traitez le poste suivant comme votre client. Vérifiez vos entrées et votre "
                  "réglage d'abord, puis suivez le SOP en vigueur. Si quelque chose semble anormal, "
                  "arrêtez, isolez et escaladez. Ne le transmettez pas. Sur la ligne de décodeurs voisine, "
                  "les opérateurs vérifient le pad thermique et le couple des vis avant qu'une unité "
                  "avance. L'inspection plus tard ne peut pas sauver un processus instable. Mais que faire "
                  "si les gens se trompent quand même ?",
    },
    {
        "key": "p07", "num": 7, "title": "Poka Yoke",
        "points": [("Poka Yoke = détrompage", "Il veut dire détrompage"),
                   ("Rendre les erreurs impossibles, ou les attraper", "Des formes, des verrouillages et des capteurs"),
                   ("La prévention bat une étiquette d'avertissement", "La prévention bat un avertissement"),
                   ("Tester avec de bons et de mauvais échantillons", "Testez chaque dispositif")],
        "example": "Le gabarit du connecteur de batterie de Priya ne rentre que dans un sens ; le téléphone "
                   "n'avance pas tant que le contrôle n'est pas enregistré.",
        "example_cue": "Priya a ajouté un gabarit",
        "script": "C'est là qu'intervient le Poka Yoke. Il veut dire détrompage. Des formes, des "
                  "verrouillages et des capteurs rendent une erreur impossible, ou l'attrapent "
                  "immédiatement. La prévention bat un avertissement, car les avertissements reposent sur "
                  "la mémoire. Priya a ajouté un gabarit pour le connecteur de batterie qui ne rentre que "
                  "dans un sens. Le téléphone n'avance pas tant que le contrôle n'est pas enregistré. "
                  "Testez chaque dispositif avec de bons et de mauvais échantillons, à chaque équipe. "
                  "Alors, que se passe-t-il quand quelque chose tourne mal quand même ?",
    },
    {
        "key": "p08", "num": 8, "title": "Jidoka, Andon et réaction",
        "points": [("Jidoka : le processus s'arrête de lui-même", "Jidoka veut dire"),
                   ("L'Andon rend le problème visible", "Un signal Andon"),
                   ("Des critères d'arrêt clairs, un responsable nommé", "Il vous faut des critères d'arrêt clairs"),
                   ("Redémarrer seulement quand la cause est maîtrisée", "vous ne redémarrez que quand")],
        "example": "Un testeur audio signale un déséquilibre de canal répété : la ligne s'arrête et les "
                   "unités suspectes sont bloquées.",
        "example_cue": "Imaginez un testeur audio",
        "script": "Jidoka veut dire que le processus détecte une anomalie et s'arrête de lui-même. Un "
                  "signal Andon rend le problème visible, pour que les bonnes personnes réagissent vite. Il "
                  "vous faut des critères d'arrêt clairs, et un responsable nommé pour chaque appel Andon. "
                  "Imaginez un testeur audio qui signale un déséquilibre de canal répété. La ligne "
                  "s'arrête, et les unités suspectes sont bloquées. Le gabarit est vérifié, et vous ne "
                  "redémarrez que quand la cause est maîtrisée. S'arrêter n'est pas un échec. Cacher le "
                  "problème, si.",
    },
    {
        "key": "p09", "num": 9, "title": "Travail standard et audits",
        "points": [("Travail standard : la meilleure méthode, la plus sûre", "Avec le travail standard"),
                   ("Vérifier la première unité après un changement de série", "vérifiez la première unité"),
                   ("Les audits par couches confirment les contrôles", "Puis des audits par couches"),
                   ("Auditer les contrôles, pas les papiers", "Auditez les contrôles")],
        "example": "La libération du firmware exige l'image approuvée, une recette correspondante et une "
                   "somme de contrôle.",
        "example_cue": "À un poste firmware",
        "script": "Alors, comment garder de bons résultats stables ? Avec le travail standard. C'est la "
                  "meilleure méthode actuelle et la plus sûre, avec les contrôles, les réglages et la "
                  "traçabilité. Gardez-le visible, et vérifiez la première unité après chaque changement de "
                  "série. Puis des audits par couches du processus confirment que vos contrôles critiques "
                  "fonctionnent toujours. Auditez les contrôles, pas les papiers. À un poste firmware, la "
                  "libération exige l'image approuvée, une recette correspondante et une somme de contrôle. "
                  "Mais quelle est la stabilité du processus lui-même ?",
    },
    {
        "key": "p10", "num": 10, "title": "SPC et capabilité du processus",
        "points": [("SPC : variation normale ou vrais signaux", "Elle sépare la variation normale"),
                   ("Cp : dispersion face à la spécification", "Le Cp compare"),
                   ("Cpk : vérifie aussi le centrage", "Le Cpk vérifie aussi"),
                   ("Seulement avec un processus stable et une jauge étalonnée", "Les deux n'ont de sens")],
        "example": "Couple de vissage sur la ligne de Priya : une variation serrée et centrée donne un Cpk ≈ "
                   "1,33. C'est capable.",
        "example_cue": "Prenez le couple de vissage",
        "script": "La maîtrise statistique des procédés répond à cela. Elle sépare la variation normale des "
                  "vrais signaux qui demandent une action. Le Cp compare la dispersion de votre processus à "
                  "la spécification. Le Cpk vérifie aussi si le processus est centré. Les deux n'ont de "
                  "sens que quand le processus est stable et la jauge étalonnée. Prenez le couple de "
                  "vissage sur la ligne de Priya. Avec une variation serrée et centrée, le Cpk est "
                  "d'environ un virgule trente-trois. C'est capable. Mais comment voir venir les risques ?",
    },
    {
        "key": "p11", "num": 11, "title": "PFMEA et plans de contrôle",
        "points": [("PFMEA : comment chaque étape peut échouer, et pourquoi", "Elle demande comment chaque étape"),
                   ("Le plan de contrôle en fait de vrais contrôles", "Puis le plan de contrôle"),
                   ("Méthode · fréquence · responsable · réaction", "Chaque contrôle a une méthode"),
                   ("Mettre les deux à jour après de vraies défaillances", "Mettez les deux à jour chaque fois")],
        "example": "Un isolant manquant peut causer un court-circuit → verrouillage de présence + règle "
                   "d'arrêt et de blocage.",
        "example_cue": "Sur un appareil audio",
        "script": "Vous utilisez une analyse des modes de défaillance du processus. Elle demande comment "
                  "chaque étape peut échouer, pourquoi, et ce qui l'empêche ou la détecte. Puis le plan de "
                  "contrôle en fait de vrais contrôles. Chaque contrôle a une méthode, une fréquence, un "
                  "responsable et une réaction. Sur un appareil audio, un isolant manquant peut causer un "
                  "court-circuit. L'analyse mène donc à un verrouillage de présence et à une règle claire "
                  "d'arrêt et de blocage. Mettez les deux à jour chaque fois qu'une vraie défaillance vous "
                  "apprend quelque chose.",
    },
    {
        "key": "p12", "num": 12, "title": "Analyse des causes racines",
        "points": [("Définir le problème avec précision", "commence par définir"),
                   ("Confiner d'abord le stock suspect", "Confinez le stock suspect"),
                   ("Faits, cinq pourquoi, tests contrôlés", "Puis utilisez des faits"),
                   ("Pourquoi est-ce arrivé ? Pourquoi n'a-t-on pas arrêté ?", "Votre correction doit répondre")],
        "example": "L'équipe de Priya a remonté ses échecs de charge jusqu'à un connecteur mal enfoncé.",
        "example_cue": "L'équipe de Priya a remonté",
        "script": "Et les défaillances vous apprendront quelque chose, si vous creusez bien. L'analyse des "
                  "causes racines commence par définir le problème avec précision. Confinez le stock "
                  "suspect d'abord. Puis utilisez des faits, les cinq pourquoi et des tests contrôlés, "
                  "jamais des suppositions. Votre correction doit répondre à deux questions. Pourquoi le "
                  "défaut est-il arrivé ? Et pourquoi nos contrôles ne l'ont-ils pas arrêté ? L'équipe de "
                  "Priya a remonté ses échecs de charge jusqu'à un connecteur mal enfoncé. Voyons ce qu'ils "
                  "ont fait ensuite.",
    },
    {
        "key": "p13", "num": 13, "title": "Cas pratique : téléphone mobile",
        "points": [("1 200 sur 40 000 en échec : 3 %", "Mille deux cents téléphones sur quarante"),
                   ("Données découpées par lot, gabarit, poste, équipe", "L'équipe a découpé les données"),
                   ("Gabarit détrompé + contrôle automatique de mise en place", "Ils ont donc essayé"),
                   ("FMEA et SOP mis à jour", "Ils ont mis à jour l'analyse des modes de défaillance")],
        "example": "Les échecs sont tombés à 0,5 % — une réduction de 83 %.",
        "example_cue": "Les échecs sont tombés à un demi",
        "script": "Voici le cas de Priya. Mille deux cents téléphones sur quarante mille ont échoué au "
                  "premier test de charge. C'est un taux d'échec de trois pour cent. L'équipe a découpé les "
                  "données par lot de connecteurs, gabarit, poste et équipe. La tendance désignait le "
                  "gabarit. Ils ont donc essayé un gabarit détrompé avec un contrôle automatique de mise en "
                  "place. Les échecs sont tombés à un demi pour cent. C'est une réduction de "
                  "quatre-vingt-trois pour cent. Et qu'est-ce qui l'a fait durer ? Ils ont mis à jour "
                  "l'analyse des modes de défaillance et le SOP.",
    },
    {
        "key": "p14", "num": 14, "title": "Décodeur et audio",
        "points": [("Même logique, contrôles adaptés", "Vous adaptez simplement les contrôles"),
                   ("Décodeur : firmware lié au SKU", "Faites donc correspondre le firmware"),
                   ("Audio : connecteurs détrompés, unités étalons", "Les connecteurs détrompés et les contrôles par unité étalon"),
                   ("Emballage : numéro de série lié au carton", "À l'emballage")],
        "example": "Décodeur : firmware, alimentation, étiquettes. Audio : polarité, étanchéité, équilibre "
                   "des canaux.",
        "example_cue": "Les défauts des décodeurs",
        "script": "La même logique marche sur chaque famille de produits. Vous adaptez simplement les "
                  "contrôles. Les défauts des décodeurs touchent souvent le firmware, l'alimentation et les "
                  "étiquettes. Faites donc correspondre le firmware au SKU, et bloquez tout mauvais "
                  "flashage. Les appareils audio échouent sur la polarité du haut-parleur, l'étanchéité et "
                  "l'équilibre des canaux. Les connecteurs détrompés et les contrôles par unité étalon s'en "
                  "chargent. À l'emballage, le système fait correspondre chaque numéro de série à son "
                  "carton. Que protégeriez-vous en premier sur votre ligne ?",
    },
    {
        "key": "p15", "num": 15, "title": "KPI et feuille de route sur 90 jours",
        "points": [("Retardés : FPY, PPM, coût de la non-qualité", "Surveillez vos résultats retardés"),
                   ("Avancés : mises à l'épreuve, notes d'audit", "Surveillez aussi les contrôles avancés"),
                   ("Jours 1–30 : référence et confinement", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : causes racines, pilote Poka Yoke", "Pendant les trente suivants"),
                   ("Jours 61–90 : vérifier les gains, déployer partout", "Pendant les trente derniers")],
        "example": "Les 30 derniers jours : vérifiez les gains et déployez-les sur chaque ligne.",
        "example_cue": "Pendant les trente derniers",
        "script": "Enfin, intégrez cela au management quotidien. Surveillez vos résultats retardés, comme "
                  "le FPY, le PPM et le coût de la non-qualité. Surveillez aussi les contrôles avancés, "
                  "comme les mises à l'épreuve des verrouillages et les notes d'audit. Voici un plan simple "
                  "sur quatre-vingt-dix jours. Pendant les trente premiers jours, établissez la référence "
                  "et confinez. Pendant les trente suivants, trouvez les causes racines et faites un pilote "
                  "de Poka Yoke. Pendant les trente derniers, vérifiez les gains et déployez-les sur chaque "
                  "ligne.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Chaque défaut évitable", "icon": "shield", "with": 0},
        {"label": "Bien du premier coup", "icon": "check", "tone": "good", "with": 1},
        {"label": "Concevoir le processus", "icon": "gear", "with": 2},
        {"label": "Une discipline", "icon": "clipboard", "with": 3}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Connecteur enfoncé ?", "icon": "sensor", "with": "example"},
            {"label": "Puis le test électrique", "icon": "test", "tone": "good", "with": "example"}]}},
    "p02": {"type": "timeline", "items": [
        {"label": "Qualité = conformité aux exigences", "sub": "Crosby, 1960s", "icon": "clipboard", "with": 0},
        {"label": "Qualité intégrée, détrompage", "sub": "Le Lean moderne", "icon": "key", "with": 1},
        {"label": "Corriger le système, pas la personne", "sub": "Aujourd'hui", "icon": "gear", "with": 2}]},
    "p03": {"type": "icons", "items": [
        {"label": "Interne", "sub": "Rebut, retouche, retest", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Externe", "sub": "Garantie, retours", "icon": "box", "tone": "bad", "with": 1},
        {"label": "Caché", "sub": "Retards, manutention, capacité", "icon": "clock", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 32000, "prefix": "₹", "icon": "wrench", "label": "de retouche directe",
                 "unit": "400 téléphones retouchés en un mois", "with": "example"}},
    "p04": {"type": "icons", "items": [
        {"label": "Bien du premier coup", "sub": "Aucune correction", "icon": "check", "with": 0},
        {"label": "Rendement au premier passage", "sub": "Réussir une étape du premier coup", "icon": "test", "with": 1},
        {"label": "Rendement cumulé", "sub": "Multiplier chaque étape", "icon": "sequence", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "98% × 98% × 98% ≈ 94%", "suffix": "%", "with": "example", "items": [
            {"label": "Étape 1", "value": 98, "with": "example"},
            {"label": "Étape 2", "value": 98, "with": "example"},
            {"label": "Étape 3", "value": 98, "with": "example"},
            {"label": "Ensemble", "value": 94, "tone": "bad", "with": "example"}]}},
    "p05": {"type": "versus", "items": [
        {"label": "PPM", "sub": "Unités défectueuses par million", "icon": "count", "with": 0},
        {"label": "DPMO", "sub": "Défauts par million d'opportunités", "icon": "search", "with": 1}],
        "then": {"type": "stat", "value": 500, "suffix": " PPM", "icon": "count", "label": "25 mauvais téléphones sur 50 000",
                 "unit": "Indiquez toujours la taille d'échantillon et le périmètre", "with": "example"}},
    "p06": {"type": "flow", "items": [
        {"label": "Responsable de sa production", "icon": "hand", "with": 0},
        {"label": "Poste suivant = client", "icon": "person", "with": 1},
        {"label": "Entrées, réglage, SOP", "icon": "clipboard", "with": 2},
        {"label": "Arrêter, isoler, escalader", "icon": "warning", "tone": "bad", "with": 3}]},
    "p07": {"type": "ladder", "top": "LE PLUS FORT", "bottom": "LE PLUS FAIBLE", "items": [
        {"label": "Le rendre impossible", "icon": "key", "with": 1},
        {"label": "L'attraper immédiatement", "icon": "sensor", "with": 1},
        {"label": "Étiquette d'avertissement", "icon": "warning", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Le gabarit ne rentre que dans un sens", "icon": "shape", "with": "example"},
            {"label": "Contrôle enregistré", "icon": "clipboard", "with": "example"},
            {"label": "Alors seulement le téléphone avance", "icon": "check", "tone": "good", "with": "example"}]}},
    "p08": {"type": "flow", "items": [
        {"label": "Anomalie détectée", "sub": "Jidoka", "icon": "sensor", "with": 0},
        {"label": "Andon : la rendre visible", "icon": "warning", "with": 1},
        {"label": "Arrêter, bloquer les suspects", "icon": "lock", "tone": "bad", "with": "example"},
        {"label": "Redémarrer quand c'est maîtrisé", "icon": "check", "tone": "good", "with": 3}]},
    "p09": {"type": "doc", "items": [
        {"label": "Travail standard · Poste firmware", "icon": "label", "with": 0},
        {"label": "Première unité vérifiée après changement", "icon": "check", "with": 1},
        {"label": "Image approuvée + recette correspondante", "icon": "chip", "with": "example"},
        {"label": "Somme de contrôle avant libération", "icon": "lock", "with": "example"},
        {"label": "Audit par couches : les contrôles, pas les papiers", "icon": "search", "with": 3}]},
    "p10": {"type": "icons", "items": [
        {"label": "Bruit ou vrai signal", "icon": "wave", "with": 0},
        {"label": "Cp : dispersion face à la spécification", "icon": "scale", "with": 1},
        {"label": "Cpk : centré aussi", "icon": "pin", "with": 2},
        {"label": "Processus stable, jauge étalonnée", "icon": "gear", "with": 3}],
        "then": {"type": "stat", "value": 1.33, "decimals": 2, "icon": "screw", "label": "Cpk du couple de vissage",
                 "unit": "Variation serrée et centrée : capable", "with": "example"}},
    "p11": {"type": "flow", "items": [
        {"label": "PFMEA : comment ça peut échouer", "icon": "search", "with": 0},
        {"label": "Plan de contrôle : de vrais contrôles", "icon": "clipboard", "with": 1},
        {"label": "Méthode · fréquence · responsable · réaction", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Isolant manquant", "sub": "Peut causer un court-circuit", "icon": "warning", "tone": "bad", "with": "example"},
            {"label": "Verrouillage de présence", "icon": "sensor", "with": "example"},
            {"label": "Règle d'arrêt et de blocage", "icon": "lock", "tone": "good", "with": "example"}]}},
    "p12": {"type": "flow", "items": [
        {"label": "Définir avec précision", "icon": "clipboard", "with": 0},
        {"label": "Confiner le stock suspect", "icon": "lock", "with": 1},
        {"label": "Faits, cinq pourquoi, tests", "icon": "test", "with": 2},
        {"label": "Pourquoi créé ? Pourquoi pas arrêté ?", "icon": "search", "tone": "good", "with": 3}]},
    "p13": {"type": "stat", "value": 3, "suffix": "%", "icon": "power", "label": "ont échoué au premier test de charge",
            "unit": "1 200 téléphones sur 40 000", "with": 0,
            "then": {"type": "compare", "before": {"label": "Avant", "value": 3}, "after": {"label": "Après", "value": 0.5},
                     "decimals": 1, "suffix": "%", "unit": "téléphones échouant au premier test de charge",
                     "note": "Une réduction de 83 %", "with": "example"}},
    "p14": {"type": "icons", "items": [
        {"label": "Décodeur", "sub": "Firmware lié au SKU", "icon": "chip", "with": 1},
        {"label": "Audio", "sub": "Connecteurs détrompés, unités étalons", "icon": "wave", "with": 2},
        {"label": "Emballage", "sub": "Numéro de série lié au carton", "icon": "barcode", "with": 3}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Référence et confinement", "sub": "Jours 1–30", "icon": "lock", "with": 2},
        {"label": "Causes racines, pilote Poka Yoke", "sub": "31–60", "icon": "search", "with": 3},
        {"label": "Vérifier les gains, déployer partout", "sub": "61–90", "icon": "chartUp", "with": 4}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "970 unités sur 1 000 réussissent le premier test sans retouche. Quel est le rendement au "
                    "premier passage ?",
        "options": ["3%", "97%", "9,7 par unité"],
        "correct": 1,
        "explanation": "FPY = acceptées du premier coup ÷ total = 970 ÷ 1 000 = 97 %. Il ne compte que les "
                       "unités réussies du premier coup, sans retouche.",
        "q_script": "Vérification rapide. Neuf cent soixante-dix unités sur mille réussissent le premier "
                    "test, sans retouche. Quel est le rendement au premier passage ? Prenez quelques "
                    "secondes.",
        "a_script": "C'est quatre-vingt-dix-sept pour cent. Le rendement au premier passage ne compte que les "
                    "unités réussies du premier coup, divisées par le total.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Une ligne audio trouve une polarité de haut-parleur inversée sur 30 unités dans cette "
                    "équipe. Que doit faire l'équipe EN PREMIER ?",
        "options": ["Reformer l'opérateur et continuer", "Arrêter, confiner les unités suspectes, puis trouver la cause racine",
                    "Ajouter une étiquette d'avertissement sur le haut-parleur", "Augmenter l'inspection finale"],
        "correct": 1,
        "explanation": "Confinez d'abord : arrêtez et bloquez les unités suspectes jusqu'au dernier point bon. "
                       "Puis trouvez la cause racine et prévenez-la, par exemple avec un connecteur de polarité "
                       "détrompé. Les reproches, les étiquettes et l'inspection en plus n'empêchent pas la "
                       "répétition.",
        "q_script": "Encore une, et cette fois c'est un scénario. Une ligne audio trouve une polarité de "
                    "haut-parleur inversée sur trente unités dans cette équipe. Que doit faire l'équipe en "
                    "premier ? Réfléchissez.",
        "a_script": "Arrêtez et confinez d'abord les unités suspectes. Puis trouvez la cause racine, et "
                    "prévenez-la, par exemple avec un connecteur de polarité détrompé. Les reproches, les "
                    "étiquettes et l'inspection en plus ne l'empêcheront pas de revenir.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
