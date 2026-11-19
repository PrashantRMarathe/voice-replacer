"""low_cost_automation in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh low_cost_automation_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "lc_fr"
NAME = "low_cost_automation_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Low Cost Automation": "lo coste otoméïchone",
    "Gemba": "Guemba",
    "Muda": "Mouda",
    "Mura": "Moura",
    "Muri": "Mouri",
    "ECRS": "eu cé erre esse",
    "LCA": "elle cé a",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Chaque grille de haut-parleur de la ligne de Gaurav était mise en place au maillet en "
    "caoutchouc. Quatre cents coups par heure, par opérateur. Des poignets douloureux, et des "
    "grilles mal fixées qui vibraient au test. Ça vous dit quelque chose ? Dans cette leçon, "
    "vous allez découvrir Low Cost Automation. Vous verrez comment des dispositifs simples et "
    "sûrs peuvent supprimer le travail répétitif et les erreurs, sans acheter une ligne "
    "complète de robots. Nous suivrons Gaurav, ingénieur procédés sur une ligne d'enceintes "
    "Bluetooth."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Simplifiez d'abord, et n'automatisez jamais le "
    "gaspillage. Choisissez la solution sûre la plus simple qui fait le travail, avec la "
    "sécurité comme premier filtre. Et prouvez le bénéfice réel, puis entretenez-la comme "
    "toute autre machine. Voici votre action pour cette semaine. Trouvez un mouvement "
    "répétitif sur votre ligne, et demandez-vous s'il peut être éliminé avant d'être "
    "automatisé. Bravo d'avoir terminé cette leçon. Ensuite, vous découvrirez Muda, Mura et "
    "Muri."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est Low Cost Automation",
        "points": [("Des dispositifs simples, fiables et économiques", "simples, fiables"),
                   ("Supprimer le travail répétitif et les erreurs", "pour supprimer le travail répétitif"),
                   ("Pas besoin d'automatisation complète", "sans passer")],
        "example": "La cible de Gaurav : la mise en place des grilles, faite à la main au maillet en "
                   "caoutchouc.",
        "example_cue": "La cible de Gaurav",
        "script": "Low Cost Automation, ou LCA, veut dire utiliser des dispositifs simples, fiables et "
                  "économiques. Vous les utilisez pour supprimer le travail répétitif, éviter les erreurs "
                  "et améliorer la sécurité. Et vous le faites sans passer directement à une ligne "
                  "entièrement automatisée. Pensez à des brides, des guides, des capteurs et de petits "
                  "vérins pneumatiques. La cible de Gaurav était la mise en place des grilles, encore faite "
                  "à la main au maillet en caoutchouc. Quelles idées guident la LCA ?",
    },
    {
        "key": "p02", "num": 2, "title": "La philosophie de base",
        "points": [("Automatiser le besoin, pas la complexité", "Automatisez le besoin"),
                   ("Simplifier avant d'automatiser", "Simplifiez avant"),
                   ("Garder les personnes dans la boucle", "Gardez les personnes"),
                   ("Le mesurer, l'entretenir", "Et mesurez")],
        "example": "Un robot sophistiqué a été chiffré à ₹18 lakh. Gaurav a demandé : de quoi le travail "
                   "a-t-il vraiment besoin ?",
        "example_cue": "Un robot a été chiffré",
        "script": "Quelques idées guident toute bonne LCA. Automatisez le besoin, pas la complexité. Partez "
                  "du problème, et de la fonction dont vous avez besoin. Simplifiez avant d'automatiser "
                  "quoi que ce soit. Gardez les personnes dans la boucle, pour que les anomalies restent "
                  "visibles. Et mesurez le bénéfice, puis entretenez-le. Un robot a été chiffré à un "
                  "million huit cent mille roupies. Gaurav a posé une question. De quoi ce travail a-t-il "
                  "vraiment besoin ?",
    },
    {
        "key": "p03", "num": 3, "title": "Quand la LCA a du sens",
        "points": [("Des mouvements fréquents et répétitifs", "répété à chaque cycle"),
                   ("Risque ergonomique ou de sécurité", "fait mal aux personnes"),
                   ("Étapes oubliées ou faites à l'envers", "des étapes sont oubliées"),
                   ("Un goulot, mais pas de quoi justifier un robot", "un goulot")],
        "example": "Mise en place des grilles : à chaque cycle, douleur au poignet, et mise en place "
                   "inégale. Les quatre cases cochées.",
        "example_cue": "La mise en place des grilles cochait",
        "script": "La LCA a du sens quand un mouvement est répété à chaque cycle, de nombreuses fois par "
                  "équipe. Quand le travail fait mal aux personnes, ou crée un risque pour la sécurité. "
                  "Quand des étapes sont oubliées, inversées ou mal placées. Et quand il y a un goulot, "
                  "mais que l'automatisation complète ne vaut pas l'argent. Elle convient aussi aux "
                  "produits aux volumes incertains. La mise en place des grilles cochait toutes les cases. "
                  "Mais que ne doit jamais vouloir dire bas coût ?",
    },
    {
        "key": "p04", "num": 4, "title": "Bas coût, jamais basse sécurité",
        "points": [("La sécurité est le premier filtre de conception", "La sécurité est le premier"),
                   ("Protecteurs, arrêts, évaluation des risques", "Protecteurs, arrêts d'urgence"),
                   ("Un capteur normal n'est pas un dispositif de sécurité", "un capteur ordinaire")],
        "example": "La règle de Gaurav : aucun dispositif ne tourne avant que l'équipe sécurité ait signé "
                   "l'évaluation des risques.",
        "example_cue": "La règle de Gaurav",
        "script": "Bas coût ne doit jamais vouloir dire basse sécurité, ou mauvaise ingénierie. La sécurité "
                  "est le premier filtre de conception, avant le coût ou la vitesse. Protecteurs, arrêts "
                  "d'urgence, évaluation des risques et normes électriques s'appliquent toujours. Et "
                  "rappelez-vous, un capteur ordinaire ou un automate n'est pas automatiquement un "
                  "dispositif de sécurité. La règle de Gaurav était simple. Aucun dispositif ne tourne "
                  "avant que l'équipe sécurité ait signé l'évaluation des risques. Quels types de LCA "
                  "existent ?",
    },
    {
        "key": "p05", "num": 5, "title": "Niveaux de LCA",
        "points": [("Mécanique : gravité, ressorts, guides", "Les aides mécaniques"),
                   ("Pneumatique : brides, presses, préhenseurs", "Les aides pneumatiques"),
                   ("Capteurs et commandes simples", "Les capteurs détectent"),
                   ("Choisir le niveau le plus bas qui marche", "Choisissez le niveau le plus bas")],
        "example": "Manuel → assisté → semi-automatique → automatique.",
        "example_cue": "Pensez à une échelle",
        "script": "Il y a plusieurs niveaux. Les aides mécaniques utilisent la gravité, des ressorts, des "
                  "leviers et des guides, sans aucune énergie. Les aides pneumatiques utilisent de petits "
                  "vérins pour brider ou presser. Les capteurs détectent la présence, la position ou la "
                  "séquence, et des commandes simples enchaînent les étapes. Pensez à une échelle, du "
                  "manuel à l'entièrement automatique. Choisissez le niveau le plus bas qui répond à votre "
                  "besoin en sécurité. Par où commencer ?",
    },
    {
        "key": "p06", "num": 6, "title": "La méthode LCA",
        "points": [("Observer et mesurer", "Observez le travail réel"),
                   ("Simplifier, puis définir la fonction", "simplifiez-le"),
                   ("Concept, revue des risques, prototype", "esquissez un concept"),
                   ("Valider, standardiser, dupliquer", "validez-le")],
        "example": "La référence de Gaurav : cycle de 28 s, 18 grilles mal fixées pour 1 000 enceintes.",
        "example_cue": "La référence de Gaurav",
        "script": "Suivez une méthode claire. Observez le travail réel, et mesurez le temps, les gestes, "
                  "les défauts et le risque. Puis simplifiez-le, et définissez exactement la fonction que "
                  "le dispositif doit remplir. Ensuite, esquissez un concept, revoyez ses risques, et "
                  "construisez un prototype. Enfin, validez-le, standardisez-le, et dupliquez-le là où il "
                  "convient. La référence de Gaurav était un cycle de vingt-huit secondes, et dix-huit "
                  "grilles mal fixées pour mille. Qu'est-ce qui vient en premier ?",
    },
    {
        "key": "p07", "num": 7, "title": "ECRS avant l'automatisation",
        "points": [("Éliminer, combiner, réordonner, simplifier", "Éliminer, combiner"),
                   ("Seulement ensuite automatiser", "Seulement ensuite"),
                   ("Le gaspillage automatisé reste du gaspillage", "Le gaspillage automatisé")],
        "example": "Gaurav a éliminé une étape séparée de vérification au maillet : la nouvelle presse "
                   "confirmerait elle-même la mise en place.",
        "example_cue": "Gaurav a trouvé",
        "script": "Simplifiez d'abord, avec ECRS. Éliminer, combiner, réordonner et simplifier. Seulement "
                  "ensuite, automatisez ce qui reste. Pourquoi ? Parce que le gaspillage automatisé reste "
                  "du gaspillage. Il est juste plus rapide, plus cher, et plus difficile à changer ensuite. "
                  "Gaurav a trouvé une étape à éliminer avant tout le reste. Les opérateurs retapaient "
                  "chaque grille, juste pour la vérifier. Une presse bien conçue pouvait confirmer "
                  "elle-même la mise en place. Qu'a-t-il vu au Gemba ?",
    },
    {
        "key": "p08", "num": 8, "title": "L'opportunité de Gaurav",
        "points": [("Mouvement répété à chaque cycle", "le même mouvement"),
                   ("Force inégale, mise en place inégale", "une force inégale"),
                   ("Douleur au poignet, à chaque équipe", "une douleur au poignet")],
        "example": "Grilles mal fixées : 18 pour 1 000 enceintes, toutes trouvées au test de vibration.",
        "example_cue": "Les grilles mal fixées",
        "script": "Au Gemba, il a vu le même mouvement, à chaque cycle. Prendre le maillet, taper autour de "
                  "la grille, la vérifier, poser le maillet. Chaque opérateur utilisait une force inégale, "
                  "donc la mise en place variait. Certaines grilles restaient mal fixées, et vibraient au "
                  "test. Et les opérateurs signalaient une douleur au poignet dès le milieu d'équipe. Les "
                  "grilles mal fixées atteignaient dix-huit pour mille enceintes. Quelle technologie "
                  "choisiriez-vous ?",
    },
    {
        "key": "p09", "num": 9, "title": "Choisir une technologie simple",
        "points": [("Adapter la technologie à la fonction", "Choisissez selon la fonction"),
                   ("Le moins de pièces possible, des pièces standard", "Utilisez le moins de pièces"),
                   ("Facile à nettoyer, régler et réparer", "Rendez-le facile")],
        "example": "Le choix de Gaurav : un petit vérin pneumatique, un nid de positionnement et un capteur "
                   "de présence.",
        "example_cue": "Gaurav a choisi",
        "script": "Choisissez selon la fonction, pas parce que quelque chose a l'air avancé. Pensez à la "
                  "précision, au temps de cycle, à l'environnement, et à qui en assurera la maintenance. "
                  "Utilisez le moins de pièces possible, et des pièces standard quand vous le pouvez. "
                  "Rendez-le facile à nettoyer, régler et réparer. Et que son état soit visible d'un coup "
                  "d'œil. Gaurav a choisi un petit vérin pneumatique, un nid de positionnement et un "
                  "capteur de présence. Comment le rendre sûr ?",
    },
    {
        "key": "p10", "num": 10, "title": "Le concevoir sûr",
        "points": [("Repérer les points de pincement et l'énergie stockée", "Cherchez les points de pincement"),
                   ("Protecteurs et démarrage bimanuel", "Ajoutez des protecteurs"),
                   ("Arrêt sûr, redémarrage sûr", "Après un arrêt")],
        "example": "Un démarrage bimanuel garde les deux mains hors de la zone de presse. La pression d'air "
                   "est relâchée à l'arrêt.",
        "example_cue": "La presse de Gaurav",
        "script": "Cherchez les points de pincement, d'écrasement, les pièces mobiles, et l'air comprimé "
                  "stocké. Ajoutez des protecteurs, et un mode de démarrage qui garde les mains loin du "
                  "danger. Après un arrêt ou une perte d'air, le dispositif doit revenir à un état sûr, et "
                  "ne pas redémarrer seul. La presse de Gaurav utilise un démarrage bimanuel, donc les deux "
                  "mains restent dégagées. La pression d'air est relâchée à chaque arrêt. Vos gabarits "
                  "actuels passeraient-ils ce test ?",
    },
    {
        "key": "p11", "num": 11, "title": "La presse de Gaurav",
        "points": [("Le nid positionne l'enceinte", "Un nid positionne"),
                   ("Le capteur confirme la présence de la grille", "Un capteur confirme"),
                   ("Force maîtrisée, voyant OK ou pas OK", "force maîtrisée")],
        "example": "Pas de grille, pas de presse. Mauvaise position, pas de presse. En place : voyant vert.",
        "example_cue": "Pas de grille",
        "script": "Voici ce qu'il a construit. Un nid positionne l'enceinte de la même façon à chaque fois. "
                  "Un capteur confirme que la grille est présente et en position. Puis le vérin presse avec "
                  "une force maîtrisée, et un voyant indique si c'est bon ou pas. Pas de grille, pas de "
                  "presse. Mauvaise position, pas de presse. Bien en place, voyant vert. L'opérateur charge "
                  "et décharge, et la presse fait le reste. Combien plus rapide était-ce ?",
    },
    {
        "key": "p12", "num": 12, "title": "Compter le vrai gain",
        "points": [("Temps de cycle : de 28 s à 22 s", "Le temps de cycle est passé"),
                   ("Production théorique : environ 35 de plus par heure", "environ trente-cinq"),
                   ("Inclure arrêts et reprises", "Incluez le chargement")],
        "example": "Vérification en réel : deux petits bourrages par équipe, d'une minute chacun. Le gain a "
                   "tenu.",
        "example_cue": "Gaurav a mesuré",
        "script": "Le temps de cycle est passé de vingt-huit secondes à vingt-deux. En théorie, cela fait "
                  "environ trente-cinq enceintes de plus par heure. Mais ne vous fiez pas à la théorie "
                  "seule. Un poste rapide qui s'arrête sans cesse peut ralentir toute la ligne. Incluez le "
                  "chargement, le déchargement, les micro-arrêts, les bourrages et la reprise après défaut. "
                  "Gaurav a mesuré la production réelle pendant deux semaines. Il y a eu deux petits "
                  "bourrages par équipe, d'une minute chacun environ. Le gain a tenu. Mais valait-il "
                  "l'argent ?",
    },
    {
        "key": "p13", "num": 13, "title": "Coût et retour sur investissement",
        "points": [("Coût total de possession", "Comptez le coût total"),
                   ("Bénéfice net, validé", "Ne comptez que les bénéfices"),
                   ("Retour = investissement ÷ bénéfice mensuel", "Le retour sur investissement est")],
        "example": "₹1,2 lakh investis ÷ ₹30 000 de bénéfice net par mois = retour en 4 mois.",
        "example_cue": "La presse de Gaurav a coûté",
        "script": "Comptez le coût total de possession. C'est-à-dire la conception, les pièces, "
                  "l'installation, la formation, l'air, les pièces de rechange et la maintenance. Ne "
                  "comptez que les bénéfices que vous pouvez valider, comme moins de retouches et du temps "
                  "de main-d'œuvre libéré. Le retour sur investissement est l'investissement, divisé par le "
                  "bénéfice net mensuel. La presse de Gaurav a coûté cent vingt mille roupies. Elle en "
                  "économisait trente mille par mois. C'est un retour en quatre mois. Comment la faire "
                  "tourner durablement ?",
    },
    {
        "key": "p14", "num": 14, "title": "Valider et entretenir",
        "points": [("Essayer tous les modèles et toutes les équipes", "Essayez-la"),
                   ("Maintenance préventive et pièces de rechange", "Donnez-lui un plan de maintenance"),
                   ("Codes de défaut et reprises clairs", "Écrivez des codes de défaut clairs")],
        "example": "Grilles mal fixées : de 18 à 2 pour 1 000. Plaintes au poignet : aucune en 60 jours.",
        "example_cue": "Les grilles mal fixées sont passées",
        "script": "Essayez-la sur plusieurs modèles et équipes, avant de la déclarer terminée. Vérifiez la "
                  "sécurité, la qualité, la vitesse, la fiabilité et la facilité avec laquelle les "
                  "opérateurs se remettent d'un défaut. Donnez-lui un plan de maintenance, des pièces de "
                  "rechange critiques, et des contrôles de capteurs. Écrivez des codes de défaut clairs, "
                  "pour que les techniciens la réparent vite. Les grilles mal fixées sont passées de "
                  "dix-huit à deux pour mille. Et aucune plainte au poignet en soixante jours. Quelles "
                  "erreurs faut-il éviter ?",
    },
    {
        "key": "p15", "num": 15, "title": "Erreurs et prochaine étape",
        "points": [("Automatiser un processus que vous ne comprenez pas", "Automatiser un processus"),
                   ("Choisir d'abord la technologie", "Choisir la technologie"),
                   ("Oublier la maintenance et les pièces de rechange", "Oublier")],
        "example": "La presse de Gaurav tourne maintenant sur trois lignes, dupliquée après avoir vérifié "
                   "que chacune convenait.",
        "example_cue": "La presse de Gaurav tourne maintenant",
        "script": "Attention aux erreurs fréquentes. Automatiser un processus que vous ne comprenez pas. "
                  "Choisir la technologie avant de définir le problème. Oublier la maintenance, les pièces "
                  "de rechange et la reprise après défaut. Annoncer des économies théoriques jamais "
                  "validées. Et ignorer ce que les opérateurs vous disent. Et ne pas mettre à jour les "
                  "standards ensuite. La presse de Gaurav tourne maintenant sur trois lignes, dupliquée "
                  "seulement après avoir vérifié que chacune convenait. Quel travail répétitif "
                  "regarderez-vous en premier ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Des dispositifs simples", "icon": "gear", "with": 0},
        {"label": "Moins de répétition, moins d'erreurs", "icon": "check", "with": 1},
        {"label": "Pas de ligne complète de robots", "icon": "scale", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 400, "icon": "hand", "label": "coups de maillet par heure",
                 "unit": "par opérateur", "with": "example"}},
    "p02": {"type": "icons", "items": [
        {"label": "Le besoin, pas la complexité", "icon": "key", "with": 0},
        {"label": "Simplifier d'abord", "icon": "shape", "with": 1},
        {"label": "Les personnes dans la boucle", "icon": "person", "with": 2},
        {"label": "Mesurer, entretenir", "icon": "wrench", "tone": "good", "with": 3}]},
    "p03": {"type": "icons", "items": [
        {"label": "Répétitif", "icon": "sequence", "with": 0},
        {"label": "Risque ergonomique", "icon": "warning", "with": 1},
        {"label": "Étapes oubliées", "icon": "cross", "with": 2},
        {"label": "Goulot", "icon": "clock", "with": 3}]},
    "p04": {"type": "flow", "items": [
        {"label": "La sécurité d'abord", "icon": "shield", "tone": "good", "with": 0},
        {"label": "Protecteurs, arrêts d'urgence, revue des risques", "icon": "lock", "with": 1},
        {"label": "Signé avant de tourner", "icon": "clipboard", "with": "example"}]},
    "p05": {"type": "ladder", "top": "AUTOMATIQUE", "bottom": "MANUEL", "items": [
        {"label": "Capteurs et commandes simples", "icon": "sensor", "with": 2},
        {"label": "Aide pneumatique", "icon": "gear", "with": 1},
        {"label": "Aide mécanique", "icon": "shape", "with": 0},
        {"label": "Manuel", "icon": "hand", "with": 3}]},
    "p06": {"type": "steps", "items": [
        {"label": "Observer, mesurer", "with": 0}, {"label": "Simplifier, définir", "with": 1},
        {"label": "Concept, risque, prototype", "with": 2}, {"label": "Valider, standardiser, dupliquer", "with": 3}]},
    "p07": {"type": "steps", "items": [
        {"label": "Éliminer", "with": 0}, {"label": "Combiner", "with": 0},
        {"label": "Réordonner", "with": 0}, {"label": "Simplifier", "with": 0},
        {"label": "Puis automatiser", "with": 1}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Retaper chaque grille", "sub": "Éliminé", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "La presse confirme la mise en place", "sub": "Intégré", "icon": "check", "tone": "good", "with": "example"}]}},
    "p08": {"type": "flow", "items": [
        {"label": "Le même mouvement à chaque cycle", "icon": "hand", "tone": "bad", "with": 0},
        {"label": "Force inégale", "icon": "scale", "tone": "bad", "with": 1},
        {"label": "Douleur au poignet", "icon": "warning", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 18, "icon": "wave", "label": "grilles mal fixées pour 1 000",
                 "unit": "trouvées au test de vibration", "with": "example"}},
    "p09": {"type": "icons", "items": [
        {"label": "Vérin pneumatique", "icon": "gear", "with": "example"},
        {"label": "Nid de positionnement", "icon": "shape", "with": "example"},
        {"label": "Capteur de présence", "icon": "sensor", "with": "example"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Points de pincement", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Démarrage bimanuel", "icon": "hand", "with": 1},
        {"label": "Air relâché à l'arrêt", "icon": "lock", "tone": "good", "with": 2}]},
    "p11": {"type": "flow", "items": [
        {"label": "Le nid positionne", "icon": "shape", "with": 0},
        {"label": "Le capteur confirme", "icon": "sensor", "with": 1},
        {"label": "Presse maîtrisée", "icon": "gear", "with": 2},
        {"label": "Vert : en place", "icon": "check", "tone": "good", "with": "example"}]},
    "p12": {"type": "compare", "before": {"label": "Maillet", "value": 28}, "after": {"label": "Presse", "value": 22},
            "suffix": " s", "unit": "temps de cycle par enceinte", "note": "Environ 35 de plus par heure, en théorie", "with": 0},
    "p13": {"type": "bars", "label": "", "note": "Économies cumulées, milliers de ₹ : rentabilisé au mois 4", "with": "example", "items": [
        {"label": "Mois 1", "value": 30, "with": "example"},
        {"label": "Mois 2", "value": 60, "with": "example"},
        {"label": "Mois 3", "value": 90, "with": "example"},
        {"label": "Mois 4", "value": 120, "tone": "good", "with": "example"}]},
    "p14": {"type": "compare", "before": {"label": "Maillet", "value": 18}, "after": {"label": "Presse", "value": 2},
            "unit": "grilles mal fixées pour 1 000 enceintes", "note": "Aucune plainte au poignet en 60 jours", "with": "example"},
    "p15": {"type": "icons", "items": [
        {"label": "Automatiser l'inconnu", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "La technologie d'abord", "icon": "gear", "tone": "bad", "with": 1},
        {"label": "Pas de pièces de rechange, pas de PM", "icon": "wrench", "tone": "bad", "with": 2},
        {"label": "Dupliquée sur 3 lignes", "icon": "check", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Avant d'ajouter de l'automatisation à une étape manuelle, que faut-il faire d'abord ?",
        "options": ["Acheter la machine la plus rapide disponible",
                    "La simplifier avec ECRS, et éliminer le gaspillage",
                    "Demander aux opérateurs de travailler plus vite"],
        "correct": 1,
        "explanation": "Simplifiez d'abord : éliminer, combiner, réordonner et simplifier. Le gaspillage "
                       "automatisé reste du gaspillage, juste plus rapide et plus difficile à changer.",
        "q_script": "Vérification rapide. Avant d'automatiser une étape manuelle, que faut-il faire d'abord ? "
                    "Prenez quelques secondes.",
        "a_script": "La simplifier avec ECRS, et éliminer le gaspillage. Le gaspillage automatisé reste du "
                    "gaspillage, juste plus rapide et plus difficile à changer.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un nouveau poste LCA gagne 6 secondes sur le papier, mais se bloque dix fois par équipe. "
                    "Que doit faire l'équipe ?",
        "options": ["Le généraliser : le temps de cycle est meilleur",
                    "Mesurer la production réelle avec les arrêts, et corriger d'abord la fiabilité",
                    "Retirer le capteur pour qu'il se bloque moins"],
        "correct": 1,
        "explanation": "Le temps de cycle théorique n'est pas la capacité réelle. Incluez les bourrages et les "
                       "reprises, corrigez la fiabilité, et seulement ensuite généralisez. Retirer un capteur "
                       "affaiblirait le contrôle qualité.",
        "q_script": "Encore une, et cette fois c'est un scénario. Un nouveau poste gagne six secondes sur le "
                    "papier. Mais il se bloque dix fois par équipe. Que doit faire l'équipe ? Réfléchissez.",
        "a_script": "Mesurez la production réelle, arrêts compris, et corrigez d'abord la fiabilité. La "
                    "théorie n'est pas la capacité, et retirer le capteur ne ferait qu'affaiblir la qualité.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
