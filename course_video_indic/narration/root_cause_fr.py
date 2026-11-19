"""root_cause in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh root_cause_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "rc_fr"
NAME = "root_cause_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Root Cause Analysis": "route côze analyse",
    "Skill Training Matrix": "skil tréïning matrix",
    "Poka Yoke": "Poka Yoké",
    "Ishikawa": "Ichikawa",
    "Pareto": "Paréto",
    "5W2H": "cinq double vé deux ache",
    "QRQC": "ku erre ku cé",
    "FMEA": "effe emme eu a",
    "RCA": "erre cé a",
    "DOE": "dé o eu",
    "MES": "emme eu esse",
    "SOP": "esse o pé",
    "SKU": "esse ka u",
    "AOI": "a o i",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Trente-six caméras ont échoué au test de mise au point en une matinée. En moins d'une "
    "heure, trois personnes avaient trois réponses différentes. Le gabarit. L'objectif. Le "
    "testeur. Qui avait raison ? Dans cette leçon, vous allez découvrir le Root Cause "
    "Analysis. Vous verrez comment passer d'un symptôme à une cause que vous pouvez prouver, "
    "et l'arrêter pour de bon. Nous suivrons Lakshmi, ingénieure qualité dans une usine de "
    "caméras, qui mène l'enquête."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Définissez le problème avec précision, et protégez "
    "d'abord votre client. Traitez chaque cause comme une hypothèse jusqu'à ce qu'un test la "
    "prouve. Et corrigez à la fois pourquoi c'est arrivé, et pourquoi ça s'est échappé. Voici "
    "votre action pour cette semaine. Prenez un problème clôturé, et vérifiez si sa cause "
    "racine a vraiment été testée. Bravo d'avoir terminé cette leçon. Ensuite, vous "
    "découvrirez la Skill Training Matrix."
)

# One story thread: Lakshmi's network-camera plant. Line 3: 36 of 1,200 units fail
# focus after the 10:00 changeover (3.0% vs 0.5% baseline); Line 2 has no failures.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est la RCA",
        "points": [("Symptôme : ce que vous observez", "Le symptôme est"),
                   ("Mécanisme : comment c'est arrivé", "Le mécanisme est"),
                   ("Cause racine : maîtrisable, avec des preuves", "La cause racine est")],
        "example": "Image floue = le symptôme. Une mauvaise entretoise pourrait être la cause — pas "
                   "confirmée tant qu'elle n'est pas testée.",
        "example_cue": "Sur la ligne de Lakshmi",
        "script": "Voici l'idée centrale. Le Root Cause Analysis est une enquête fondée sur des preuves "
                  "pour comprendre pourquoi quelque chose a mal tourné. Elle sépare trois choses. Le "
                  "symptôme est ce que vous observez. Le mécanisme est la façon dont c'est arrivé. La cause "
                  "racine est une condition que vous pouvez maîtriser, appuyée par des preuves. Sur la "
                  "ligne de Lakshmi, une image floue est le symptôme. Une mauvaise entretoise pourrait être "
                  "la cause. Mais rien n'est confirmé tant que ce n'est pas testé. Où cela s'inscrit-il ?",
    },
    {
        "key": "p02", "num": 2, "title": "La RCA dans le système qualité",
        "points": [("Détecter un écart", "D'abord, vous détectez"),
                   ("Confiner pour protéger le client", "Puis vous le confinez"),
                   ("Enquêter avec des données réelles", "Ensuite, vous enquêtez"),
                   ("Corriger, puis vérifier dans le temps", "Vous corrigez les causes vérifiées")],
        "example": "Un tri réussi protège le client — il ne prouve pas que la cause a disparu.",
        "example_cue": "Un tri réussi protège",
        "script": "La RCA est un maillon d'une boucle fermée. D'abord, vous détectez un écart. Puis vous le "
                  "confinez, pour protéger votre client. Ensuite, vous enquêtez avec des données réelles. "
                  "Vous corrigez les causes vérifiées, et vérifiez le résultat dans le temps. Elle va de "
                  "pair avec le QRQC, le FMEA, les plans de contrôle et le Poka Yoke. Et voici un point "
                  "clé. Un tri réussi protège le client. Mais prouve-t-il que la cause a disparu ? Pas du "
                  "tout.",
    },
    {
        "key": "p03", "num": 3, "title": "Définir : 5W2H et Is / Is Not",
        "points": [("Un problème précis et mesurable", "commence par un problème précis"),
                   ("Le 5W2H rassemble les faits", "Utilisez le 5W2H"),
                   ("Is / Is Not : où ça se produit, et où non", "appelée Est, N'est pas")],
        "example": "Ligne 3 : 36 caméras sur 1 200 ont échoué à la mise au point après le changement de "
                   "10:00. Ligne 2, autre gabarit : aucune.",
        "example_cue": "L'énoncé de Lakshmi était clair",
        "script": "Toute bonne RCA commence par un problème précis et mesurable. Utilisez le 5W2H pour "
                  "rassembler les faits. Puis ajoutez une comparaison puissante, appelée Est, N'est pas. Où "
                  "le problème se produit-il, et où ne se produit-il pas ? L'énoncé de Lakshmi était clair. "
                  "Sur la ligne trois, trente-six caméras sur mille deux cents ont échoué à la mise au "
                  "point. Cela a commencé après le changement de dix heures. La ligne deux, avec un autre "
                  "gabarit, n'en avait aucune. Que vous dit cette comparaison ?",
    },
    {
        "key": "p04", "num": 4, "title": "Preuves et traçabilité",
        "points": [("Rassembler les preuves avant de changer les réglages", "rassemblez les preuves"),
                   ("Garder des échantillons défaillants et bons connus", "Gardez les pièces défaillantes"),
                   ("Extraire les enregistrements MES, journaux de test, alarmes", "Extrayez les enregistrements MES"),
                   ("Noter chaque changement récent", "Notez chaque changement récent"),
                   ("Vérifier l'étalonnage des jauges", "Et confirmez que vos jauges")],
        "example": "Lakshmi a mis sous sachet dix caméras défaillantes et dix bonnes avant que quiconque "
                   "touche au gabarit.",
        "example_cue": "Lakshmi a mis sous sachet dix",
        "script": "Cela désigne le changement de série. Mais d'abord, rassemblez les preuves, avant que "
                  "quelqu'un ne change un réglage. Gardez les pièces défaillantes et des échantillons bons "
                  "connus. Extrayez les enregistrements MES, les journaux de test et les alarmes machine. "
                  "Notez chaque changement récent, d'outillage, de firmware, de recette et de lot de "
                  "matière. Et confirmez que vos jauges sont étalonnées avant de vous fier à de petites "
                  "différences. Lakshmi a mis sous sachet dix caméras défaillantes et dix bonnes. Un autre "
                  "ingénieur pourrait-il refaire vos constats à partir de vos preuves ?",
    },
    {
        "key": "p05", "num": 5, "title": "Pareto : choisir son combat",
        "points": [("Classer par nombre, coût ou risque", "Classez vos types de défauts"),
                   ("Trier et ajouter le % cumulé", "Triez-les"),
                   ("Découper le premier par équipe, poste, fournisseur", "Puis découpez le premier"),
                   ("Les risques graves passent devant", "Un risque grave de sécurité")],
        "example": "Mauvais PCB 40 · vis manquante 25 · mise au point 20 · étiquette 10 · autre 5 → les "
                   "trois premiers = 85 %.",
        "example_cue": "Sur la ligne de Lakshmi, trois",
        "script": "Face à de nombreux problèmes, le Pareto vous aide à choisir. Classez vos types de "
                  "défauts par nombre, coût ou risque. Triez-les, et ajoutez le pourcentage cumulé. "
                  "Souvent, quelques causes font l'essentiel de la perte. Sur la ligne de Lakshmi, trois "
                  "types de défauts représentaient quatre-vingt-cinq pour cent. Puis découpez le premier "
                  "par équipe, poste ou fournisseur. Mais un avertissement. Un risque grave de sécurité ou "
                  "client passe devant, quel que soit son rang. Alors, comment creuser ?",
    },
    {
        "key": "p06", "num": 6, "title": "5 Why : tester la chaîne",
        "points": [("Cinq n'est pas une règle", "Cinq n'est pas une règle"),
                   ("Une preuve pour chaque maillon", "Chaque maillon a besoin d'une preuve"),
                   ("Ramifier quand il y a plus d'une cause", "Ramifiez quand"),
                   ("Ne jamais s'arrêter à « erreur de l'opérateur »", "ne vous arrêtez jamais à l'erreur de l'opérateur")],
        "example": "Vis manquante → cycle terminé sans la confirmer → signal de couple non relié au MES.",
        "example_cue": "Prenez une vis manquante",
        "script": "Utilisez les cinq pourquoi, mais traitez-les comme une chaîne d'affirmations à vérifier. "
                  "Cinq n'est pas une règle. Chaque maillon a besoin d'une preuve. Ramifiez quand il y a "
                  "plus d'une cause. Et ne vous arrêtez jamais à l'erreur de l'opérateur, ou au manque de "
                  "formation. Demandez ce qui, dans la conception du travail, l'a permis. Prenez une vis "
                  "manquante. Le poste a laissé le cycle se terminer sans confirmer la vis. Pourquoi ? Le "
                  "signal de couple n'était pas relié au MES. Une histoire plausible n'est pas une preuve. "
                  "Avez-vous vérifié les journaux ?",
    },
    {
        "key": "p07", "num": 7, "title": "Arête de poisson et 6M",
        "points": [("Arête de poisson = diagramme d'Ishikawa", "L'arête de poisson, ou diagramme d'Ishikawa"),
                   ("Main-d'œuvre · machine · méthode", "Main-d'œuvre, machine, méthode"),
                   ("Matière · mesure · milieu", "matière, mesure et milieu"),
                   ("Elle ne prouve pas quelle cause est vraie", "Une arête de poisson ne prouve pas")],
        "example": "L'arête de Lakshmi : usure du gabarit, mauvaise recette, tolérance de l'objectif, "
                   "répétabilité du testeur, manutention, chaleur.",
        "example_cue": "L'équipe de Lakshmi l'a remplie",
        "script": "L'arête de poisson, ou diagramme d'Ishikawa, organise vos idées. Elle a six branches. "
                  "Main-d'œuvre, machine, méthode, matière, mesure et milieu. L'équipe de Lakshmi l'a "
                  "remplie. Usure du gabarit, mauvaise recette, tolérance de l'objectif, répétabilité du "
                  "testeur, manutention, et chaleur. C'est une belle liste de suspects. Mais voici le point "
                  "clé. Une arête de poisson ne prouve pas quelle cause est vraie. Pour chaque branche, "
                  "vous écrivez le test qui la confirmerait ou la rejetterait. Qu'est-ce qui a changé ?",
    },
    {
        "key": "p08", "num": 8, "title": "Analyse des changements et arbres de défaillance",
        "points": [("Analyse des changements : défaillant face au dernier état stable", "C'est l'analyse des changements"),
                   ("Arbre de défaillance : remonter avec AND / OR", "utilisez un arbre de défaillance"),
                   ("Ensemble ≠ cause", "Que deux choses")],
        "example": "Sans image ne s'échappe que si le firmware est faux AND que le verrouillage manque.",
        "example_cue": "Un enregistreur vidéo s'échappe",
        "script": "C'est l'analyse des changements. Vous comparez la condition défaillante au dernier état "
                  "stable, et listez chaque changement entre les deux. Pour les problèmes complexes, "
                  "utilisez un arbre de défaillance. Il remonte depuis la défaillance, avec une logique et, "
                  "ou. Un enregistreur vidéo s'échappe sans image seulement si le firmware est faux, et que "
                  "le verrouillage manque. Mais attention. Que deux choses soient arrivées ensemble ne veut "
                  "pas dire que l'une a causé l'autre. Alors, comment le prouver ?",
    },
    {
        "key": "p09", "num": 9, "title": "Tester votre hypothèse",
        "points": [("Écrire une prédiction", "Écrivez une prédiction"),
                   ("Un facteur à la fois, ou un DOE", "Changez un facteur"),
                   ("Assez d'échantillons, répété", "Utilisez assez d'échantillons"),
                   ("Vérifier d'abord la jauge", "elle a d'abord vérifié la jauge")],
        "example": "Entretoises approuvées contre suspectes, avec la même caméra, la même recette et la même "
                   "salle.",
        "example_cue": "Lakshmi a comparé des entretoises approuvées",
        "script": "Écrivez une prédiction. Si l'entretoise est mauvaise, les échecs de mise au point "
                  "doivent augmenter. Puis testez-la. Changez un facteur à la fois, ou utilisez une "
                  "expérience planifiée, appelée DOE, quand les facteurs interagissent. Utilisez assez "
                  "d'échantillons, et répétez l'essai. Lakshmi a comparé des entretoises approuvées et "
                  "suspectes, avec la même caméra, la même recette et la même salle. Et elle a d'abord "
                  "vérifié la jauge. Si votre mesure varie beaucoup, même une vraie différence peut se "
                  "cacher. Prêt pour la solution ?",
    },
    {
        "key": "p10", "num": 10, "title": "Confiner, corriger, prévenir",
        "points": [("Confiner : protéger le client maintenant", "Le confinement protège"),
                   ("Corriger : supprimer la cause vérifiée", "L'action corrective supprime"),
                   ("Prévenir : étendre aux lignes similaires", "Et l'action préventive"),
                   ("Corriger aussi la cause de la fuite", "Corrigez aussi la cause de la fuite")],
        "example": "Mauvaise carte : scanner le stock bloqué → ajouter une correspondance MES → la dupliquer "
                   "sur les autres variantes.",
        "example_cue": "Pour une mauvaise carte",
        "script": "Gardez trois actions séparées. Le confinement protège votre client maintenant. L'action "
                  "corrective supprime la cause vérifiée. Et l'action préventive étend la leçon aux lignes "
                  "similaires. Corrigez aussi la cause de la fuite, avec un verrouillage ou un contrôle de "
                  "présence. Pour une mauvaise carte, vous scannez le stock bloqué. Puis vous ajoutez une "
                  "correspondance MES, et la dupliquez sur les autres variantes. Une règle. Ne libérez "
                  "jamais le stock bloqué juste parce que la solution a été commandée. Comment faire durer "
                  "?",
    },
    {
        "key": "p11", "num": 11, "title": "Lien avec le FMEA et le Poka Yoke",
        "points": [("Relier chaque cause à un mode de défaillance", "Reliez chaque cause confirmée"),
                   ("Mettre à jour le plan de contrôle", "Mettez à jour le plan de contrôle"),
                   ("Valider le Poka Yoke : bon, mauvais, limite", "Validez tout Poka Yoke"),
                   ("Mettre à jour le SOP, la formation, les audits", "Puis mettez à jour le SOP")],
        "example": "Demandez : le nouveau contrôle empêche-t-il l'erreur, la détecte-t-il, ou la rend-il "
                   "seulement visible ?",
        "example_cue": "Le nouveau contrôle empêche-t-il",
        "script": "Réinjectez ce que vous avez appris dans le système. Reliez chaque cause confirmée à un "
                  "mode de défaillance dans votre FMEA, et réévaluez le risque. Mettez à jour le plan de "
                  "contrôle, avec la méthode, la réaction et le responsable. Validez tout Poka Yoke avec "
                  "des pièces bonnes connues, mauvaises connues et limites. Puis mettez à jour le SOP, la "
                  "formation et les questions d'audit. Posez-vous une question. Le nouveau contrôle "
                  "empêche-t-il l'erreur, la détecte-t-il, ou la rend-il seulement visible ?",
    },
    {
        "key": "p12", "num": 12, "title": "Indicateurs de la RCA",
        "points": [("Ne pas compter les formulaires clos comme un succès", "Ne déclarez pas le succès"),
                   ("Taux de défauts ≠ rendement au premier passage", "Suivez le taux de défauts"),
                   ("Suivre les répétitions après clôture", "Suivez à quelle fréquence"),
                   ("Coût et retour", "Combien cela coûte-t-il")],
        "example": "60 → 12 défauts pour 20 000 : une baisse de 80 %. Un contrôle de ₹90 000 qui économise "
                   "₹15 000/mois = retour en 6 mois.",
        "example_cue": "Un contrôle qui réduit les défauts",
        "script": "Mesurez à la fois la qualité de vos enquêtes, et leur impact sur l'entreprise. Ne "
                  "déclarez pas le succès juste parce qu'un formulaire a été clos. Suivez le taux de "
                  "défauts, et le rendement au premier passage, mais ne les confondez jamais. Suivez à "
                  "quelle fréquence les problèmes reviennent après clôture. Un contrôle qui réduit les "
                  "défauts de quatre-vingts pour cent, c'est très bien. Combien cela coûte-t-il, et en "
                  "combien de temps est-ce rentabilisé ? Celui de Lakshmi l'a été en six mois. Voici "
                  "maintenant son cas complet.",
    },
    {
        "key": "p13", "num": 13, "title": "Cas pratique : défaut de mise au point",
        "points": [("Bloqué chaque caméra depuis la dernière bonne première pièce", "Lakshmi a bloqué chaque caméra"),
                   ("Quatre suspects : entretoise, recette, mise en place, testeur", "Son équipe a listé quatre"),
                   ("Mesuré, comparé les journaux, test croisé", "Ils ont mesuré les entretoises"),
                   ("Entretoise détrompée + scan du gabarit lié à la recette", "La solution a été une entretoise détrompée")],
        "example": "Échanger les entretoises a déplacé les échecs. Échanger les testeurs, non. C'était la "
                   "preuve.",
        "example_cue": "Échanger les entretoises a déplacé",
        "script": "Lakshmi a bloqué chaque caméra depuis la dernière première pièce validée. Son équipe a "
                  "listé quatre suspects. L'épaisseur de l'entretoise, une recette non conforme, la mise en "
                  "place de l'objectif, et la dérive du testeur. Ils ont mesuré les entretoises, comparé "
                  "les journaux, et fait un test croisé. Échanger les entretoises a déplacé les échecs. "
                  "Échanger les testeurs, non. Ils avaient maintenant la preuve. La solution a été une "
                  "entretoise détrompée, et un scan du gabarit lié à la recette. De quelle preuve "
                  "auriez-vous eu besoin ?",
    },
    {
        "key": "p14", "num": 14, "title": "Deux autres cas : SMT et étiquette",
        "points": [("Ligne de cartes : mauvais composant posé", "Sur la ligne de cartes"),
                   ("Solution : verrouillage des chargeurs contre la BOM", "La solution a été un verrouillage"),
                   ("Emballage : étiquette du carton ≠ appareil", "À l'emballage"),
                   ("Solution : le carton ne ferme que si tout correspond", "Cette solution a empêché")],
        "example": "Les deux solutions ont été mises à l'épreuve avant la clôture.",
        "example_cue": "Les deux solutions ont été mises à l'épreuve",
        "script": "Deux cas plus courts montrent la même logique. Sur la ligne de cartes, un mauvais "
                  "composant a été posé. L'équipe a comparé la nomenclature, le réglage des chargeurs, le "
                  "code-barres de la bobine et les images AOI. La solution a été un verrouillage des "
                  "chargeurs contre la nomenclature. À l'emballage, une étiquette de carton ne "
                  "correspondait pas à l'appareil. Cette solution a empêché le carton de fermer tant que le "
                  "numéro de série, le SKU et l'étiquette ne concordaient pas. Les deux solutions ont été "
                  "mises à l'épreuve. Pourriez-vous prouver que chaque unité suspecte a été retrouvée ?",
    },
    {
        "key": "p15", "num": 15, "title": "Déploiement sur 90 jours",
        "points": [("Jours 1–30 : déclencheurs, rôles, formulaires, pilotes", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : former, enquêter", "Pendant les trente suivants"),
                   ("Jours 61–90 : auditer, mettre à jour le FMEA, étendre", "Pendant les trente derniers"),
                   ("Clôture : réconcilié, vérifié, testé", "Avant de clôturer un problème")],
        "example": "Faites de la RCA une routine, pas un atelier ponctuel.",
        "example_cue": "Faites de la RCA une routine",
        "script": "Faites de la RCA une routine, pas un atelier ponctuel. Pendant les trente premiers "
                  "jours, définissez vos déclencheurs, rôles, formulaires et zones pilotes. Pendant les "
                  "trente suivants, formez les équipes, et menez de vraies enquêtes. Pendant les trente "
                  "derniers, auditez les résultats, mettez à jour votre FMEA et vos plans de contrôle, et "
                  "étendez. Avant de clôturer un problème, vérifiez-le. Le confinement est-il réconcilié ? "
                  "Les causes sont-elles vérifiées, et les actions testées ? Prouvez la cause, puis "
                  "prévenez-la.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Symptôme", "sub": "Une image floue", "icon": "camera", "tone": "bad"},
        {"label": "Mécanisme", "sub": "Comment c'est arrivé", "icon": "gear"},
        {"label": "Cause racine", "sub": "Une mauvaise entretoise ? Testez-la d'abord", "icon": "search"}]},
    "p02": {"type": "flow", "items": [
        {"label": "Détecter", "icon": "sensor"}, {"label": "Confiner", "icon": "lock"},
        {"label": "Enquêter avec des données", "icon": "search"},
        {"label": "Corriger, vérifier dans le temps", "icon": "check", "tone": "good"}]},
    "p03": {"type": "compare", "before": {"label": "Ligne 3", "value": 36}, "after": {"label": "Ligne 2", "value": 0},
            "unit": "échecs de mise au point après le changement (la ligne 2 a un autre gabarit)",
            "note": "Is / Is Not désigne le gabarit", "with": "example"},
    "p04": {"type": "icons", "items": [
        {"label": "D'abord les preuves", "icon": "search"}, {"label": "Échantillons défaillants + bons", "icon": "box"},
        {"label": "Journaux et alarmes", "icon": "clipboard"}, {"label": "Changements récents", "icon": "sequence"},
        {"label": "Étalonnage", "icon": "scale"}]},
    "p05": {"type": "bars", "label": "", "note": "Les trois premiers = 85 % des défauts", "items": [
        {"label": "Mauvais PCB", "value": 40, "tone": "bad", "with": "example"},
        {"label": "Vis manquante", "value": 25, "tone": "bad", "with": "example"},
        {"label": "Mise au point", "value": 20, "tone": "bad", "with": "example"},
        {"label": "Étiquette", "value": 10, "with": "example"},
        {"label": "Autre", "value": 5, "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Cinq n'est pas une règle", "icon": "count"}, {"label": "Une preuve par maillon", "icon": "search"},
        {"label": "Ramifier si besoin", "icon": "sequence"}, {"label": "Jamais « erreur de l'opérateur »", "icon": "cross", "tone": "bad"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Une vis manquante", "icon": "screw", "tone": "bad", "with": "example"},
            {"label": "Pourquoi ? Le cycle s'est terminé quand même", "icon": "sequence", "with": "example"},
            {"label": "Pourquoi ? Couple non relié au MES", "icon": "chip", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Main-d'œuvre", "sub": "Manutention", "icon": "person", "with": 1},
        {"label": "Machine", "sub": "Usure du gabarit", "icon": "gear", "with": 1},
        {"label": "Méthode", "sub": "Mauvaise recette", "icon": "clipboard", "with": 1},
        {"label": "Matière", "sub": "Tolérance de l'objectif", "icon": "box", "with": 2},
        {"label": "Mesure", "sub": "Répétabilité du testeur", "icon": "scale", "with": 2},
        {"label": "Milieu", "sub": "Chaleur", "icon": "wave", "with": 2}]},
    "p08": {"type": "icons", "items": [
        {"label": "Analyse des changements", "sub": "Défaillant face au dernier état stable", "icon": "sequence", "with": 0},
        {"label": "Arbre de défaillance", "sub": "AND / OR, en remontant", "icon": "gear", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Le firmware est faux", "icon": "chip", "tone": "bad", "with": "example"},
            {"label": "AND le verrouillage manque", "icon": "lock", "tone": "bad", "with": "example"},
            {"label": "Une unité sans image s'échappe", "icon": "box", "tone": "bad", "with": "example"}]}},
    "p09": {"type": "icons", "items": [
        {"label": "Écrire une prédiction", "icon": "clipboard"}, {"label": "Un facteur, ou un DOE", "icon": "gear"},
        {"label": "Assez d'échantillons", "icon": "stack"}, {"label": "Vérifier la jauge", "icon": "scale"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Entretoise suspecte", "sub": "Même caméra, recette, salle", "icon": "shape"},
            {"label": "Entretoise approuvée", "sub": "Même caméra, recette, salle", "icon": "shape"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "Confiner", "sub": "Scanner le stock bloqué", "icon": "lock"},
        {"label": "Corriger", "sub": "Ajouter une correspondance MES", "icon": "barcode"},
        {"label": "Prévenir", "sub": "La dupliquer sur les autres variantes", "icon": "sequence", "tone": "good"}]},
    "p11": {"type": "icons", "items": [
        {"label": "FMEA", "icon": "clipboard"}, {"label": "Plan de contrôle", "icon": "shield"},
        {"label": "Valider le Poka Yoke", "icon": "test"}, {"label": "SOP, formation, audits", "icon": "person"}],
        "then": {"type": "ladder", "top": "LE MEILLEUR", "bottom": "LE PLUS FAIBLE", "with": "example", "items": [
            {"label": "Empêche l'erreur", "icon": "key", "with": "example"},
            {"label": "La détecte", "icon": "sensor", "with": "example"},
            {"label": "La rend seulement visible", "icon": "search", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Formulaire clos ≠ succès", "icon": "cross", "tone": "bad"},
        {"label": "Taux de défauts contre FPY", "icon": "chartUp"},
        {"label": "Répétitions après clôture", "icon": "sequence"}, {"label": "Coût et retour", "icon": "calendar"}],
        "then": {"type": "compare", "before": {"label": "Avant", "value": 60}, "after": {"label": "Après", "value": 12},
                 "unit": "défauts pour 20 000 caméras", "note": "80 % de moins, retour en 6 mois", "with": "example"}},
    "p13": {"type": "flow", "items": [
        {"label": "Bloquer depuis la dernière bonne première pièce", "icon": "lock"},
        {"label": "Quatre suspects listés", "icon": "search"},
        {"label": "Test croisé", "sub": "Les entretoises l'ont déplacé ; les testeurs, non", "icon": "test"},
        {"label": "Entretoise détrompée + scan du gabarit", "icon": "key", "tone": "good"}]},
    "p14": {"type": "icons", "items": [
        {"label": "Mauvais composant", "sub": "Ligne de cartes", "icon": "chip", "tone": "bad"},
        {"label": "Verrouillage des chargeurs", "sub": "Vérifié contre la BOM", "icon": "lock", "tone": "good"},
        {"label": "Étiquette ≠ appareil", "sub": "Emballage", "icon": "label", "tone": "bad"},
        {"label": "Le carton ne ferme pas", "sub": "Tant que les trois ne correspondent pas", "icon": "box", "tone": "good"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Déclencheurs, rôles, formulaires, pilotes", "sub": "Jours 1–30", "icon": "clipboard", "with": 0},
        {"label": "Former, mener de vraies enquêtes", "sub": "31–60", "icon": "person", "with": 1},
        {"label": "Auditer, mettre à jour le FMEA, étendre", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "L'arête de poisson d'une équipe liste six causes possibles. Que prouve-t-elle ?",
        "options": ["La plus grosse branche est la cause racine", "Rien encore — chaque cause doit être testée",
                    "Les six causes sont vraies"],
        "correct": 1,
        "explanation": "Une arête de poisson organise des hypothèses. Elle ne prouve rien tant que chaque "
                       "candidate n'est pas confirmée ou rejetée par un test.",
        "q_script": "Vérification rapide. L'arête de poisson d'une équipe liste six causes possibles. Que "
                    "prouve-t-elle ? Prenez quelques secondes.",
        "a_script": "Rien encore. Une arête de poisson est une liste d'hypothèses. Chacune doit être testée "
                    "avant d'être appelée une cause.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un défaut de mauvais PCB est trouvé. Le nouveau verrouillage MES est commandé mais pas "
                    "installé. Le WIP bloqué peut-il être libéré ?",
        "options": ["Oui — la solution arrive", "Non — seulement après tri et décision autorisée",
                    "Oui, si l'opérateur est reformé", "Oui, si l'équipe suivante est prévenue"],
        "correct": 1,
        "explanation": "Commander une solution ne protège pas le client. Le stock bloqué n'est libéré qu'après "
                       "avoir été trié et tranché par le processus qualité.",
        "q_script": "Encore une, et cette fois c'est un scénario. Un défaut de mauvaise carte est trouvé. Le "
                    "nouveau verrouillage est commandé, mais pas installé. Le stock bloqué peut-il être "
                    "libéré ? Réfléchissez.",
        "a_script": "Non. Libérez-le seulement après un tri, et une décision autorisée. Commander une "
                    "solution ne protège pas votre client.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
