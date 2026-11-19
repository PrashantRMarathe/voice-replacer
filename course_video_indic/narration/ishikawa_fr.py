"""ishikawa in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh ishikawa_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ik_fr"
NAME = "ishikawa_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Kaoru Ishikawa": "Kaorou Ichikawa",
    "Ishikawa": "Ichikawa",
    "Pareto": "Paréto",
    "Jidoka": "Djidoka",
    "Gemba": "Guemba",
    "PFMEA": "pé effe emme eu a",
    "SOP": "esse o pé",
    "ESD": "eu esse dé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Les échecs au test de ports sur la ligne de switchs ont été multipliés par six en une "
    "semaine. La première réunion a duré deux heures. Elle s'est terminée par une seule "
    "décision. Acheter un nouveau testeur. Ça vous dit quelque chose ? Dans cette leçon, vous "
    "allez découvrir le diagramme d'Ishikawa, aussi appelé arête de poisson. Vous verrez "
    "comment chercher les causes largement, puis prouver les vraies avant de dépenser une "
    "roupie. Nous suivrons Nikhil, ingénieur qualité sur une ligne de switchs réseau."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Mettez un effet précis et mesurable dans la tête. "
    "Cherchez largement dans les six M, sans reproche. Et traitez chaque arête comme une "
    "supposition tant qu'une preuve ne l'a pas confirmée. Voici votre action pour cette "
    "semaine. Dessinez une arête de poisson pour un problème récurrent, et choisissez les "
    "trois causes que vous testerez en premier. Bravo d'avoir terminé cette leçon. Ensuite, "
    "vous découvrirez le Jidoka."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est une arête de poisson",
        "points": [("Un problème dans la tête", "Un problème se place"),
                   ("Les causes possibles sur les arêtes", "causes possibles"),
                   ("Un outil de réflexion en équipe", "C'est un outil d'équipe")],
        "example": "Le problème de Nikhil : des switchs réseau qui échouent au test de liaison des ports.",
        "example_cue": "Le problème de Nikhil",
        "script": "Un diagramme d'Ishikawa ressemble au squelette d'un poisson. Un problème se place dans "
                  "la tête. Toutes les causes possibles partent des arêtes, classées par familles. C'est un "
                  "outil d'équipe, pour que chacun voie toute la recherche sur une page. Il vous empêche de "
                  "sauter sur la première idée. Le problème de Nikhil, c'étaient des switchs réseau qui "
                  "échouaient au test de liaison des ports. D'où vient cet outil ?",
    },
    {
        "key": "p02", "num": 2, "title": "Origines, et limites",
        "points": [("Kaoru Ishikawa, pionnier de la qualité", "Kaoru Ishikawa"),
                   ("Un des sept outils de base de la qualité", "sept outils de base de la qualité"),
                   ("Montre des causes possibles, ne prouve rien", "ne prouve")],
        "example": "Acheter un nouveau testeur était une supposition. L'arête de poisson en ferait une "
                   "supposition parmi d'autres.",
        "example_cue": "Acheter un nouveau testeur",
        "script": "Il a été popularisé par Kaoru Ishikawa, un expert japonais de la qualité. C'est un des "
                  "sept outils de base de la qualité. Mais voici l'essentiel. Il montre des causes "
                  "possibles, et ne prouve aucune d'elles. La preuve vient après, de l'observation, de la "
                  "mesure et des essais. Acheter un nouveau testeur n'était qu'une supposition. L'arête de "
                  "poisson en ferait une supposition parmi d'autres. Alors, à quoi ressemble le poisson ?",
    },
    {
        "key": "p03", "num": 3, "title": "Anatomie du poisson",
        "points": [("Tête : l'effet", "La tête est"),
                   ("Colonne et grandes arêtes : familles de causes", "La colonne relie"),
                   ("Petites arêtes : causes précises", "Les petites arêtes portent")],
        "example": "Écrivez une cause comme « suspectée » tant qu'elle n'est pas prouvée.",
        "example_cue": "La règle de Nikhil",
        "script": "Lisez-le de gauche à droite. La tête est l'effet, le problème que vous voulez résoudre. "
                  "La colonne relie tout à elle. Les grandes arêtes sont des familles de causes, comme la "
                  "machine ou la méthode. Les petites arêtes portent des causes possibles précises, et les "
                  "plus petites vont encore plus loin. La règle de Nikhil était simple. Chaque cause est "
                  "suspectée, tant qu'elle n'est pas prouvée. Que met-on dans la tête ?",
    },
    {
        "key": "p04", "num": 4, "title": "Un effet précis",
        "points": [("Quoi, où, quand, combien", "Dites ce qui échoue"),
                   ("Une référence et un dénominateur", "Ajoutez une référence"),
                   ("Un mode de défaut à la fois", "Limitez-vous à un seul")],
        "example": "« Les échecs de liaison des ports sur la ligne 3 de switchs sont passés de 5 à 32 pour "
                   "1 000 cette semaine. »",
        "example_cue": "Nikhil a écrit",
        "script": "Une tête vague donne un poisson vague. La qualité est mauvaise n'aide personne. Dites ce "
                  "qui échoue, où, quand, et combien. Ajoutez une référence, et un dénominateur clair. "
                  "Limitez-vous à un seul mode de défaut à la fois. Nikhil a écrit une phrase. Les échecs "
                  "de liaison des ports sur la ligne trois de switchs sont passés de cinq à trente-deux "
                  "pour mille cette semaine. Voyez-vous à quel point c'est plus précis ?",
    },
    {
        "key": "p05", "num": 5, "title": "Les 6M : main-d'œuvre, machine, méthode",
        "points": [("Main-d'œuvre : compétence, charge, passation", "La main-d'œuvre couvre"),
                   ("Machine : usure, réglages, maintenance", "La machine couvre"),
                   ("Méthode : séquence, SOP, changement de série", "La méthode couvre")],
        "example": "Utilisez les familles comme des pistes, pas comme des cases rigides.",
        "example_cue": "Utilisez-les comme des pistes",
        "script": "La plupart des équipes utilisent six familles, appelées les six M. La main-d'œuvre "
                  "couvre la compétence, la formation, la charge de travail et les passations. La machine "
                  "couvre l'usure des gabarits, les réglages, la maintenance et le logiciel. La méthode "
                  "couvre la séquence, le SOP, les changements de série et les contrôles de réglage. Pour "
                  "chaque famille, posez une question à votre équipe. Cela pourrait-il expliquer notre "
                  "effet ? Utilisez-les comme des pistes, pas comme des cases rigides. Une cause peut "
                  "toucher deux familles. Et les trois autres M ?",
    },
    {
        "key": "p06", "num": 6, "title": "Matière, mesure, milieu",
        "points": [("Matière : fournisseur, lot, manutention", "La matière couvre"),
                   ("Mesure : jauges, limites de test, faux rejets", "La mesure couvre"),
                   ("Milieu : ESD, humidité, poussière, chaleur", "Le milieu couvre")],
        "example": "La mesure est celle que les équipes oublient. Le testeur lui-même dit-il la vérité ?",
        "example_cue": "La mesure est celle",
        "script": "La matière couvre la variation du fournisseur, le mauvais lot, et les dommages de "
                  "manutention. La mesure couvre les jauges, les limites de test, l'étalonnage et les faux "
                  "rejets. Le milieu couvre l'ESD, l'humidité, la poussière, la lumière et la chaleur. La "
                  "mesure est celle que les équipes oublient le plus. Le testeur lui-même vous dit-il la "
                  "vérité ? Gardez cette question en tête. Un gabarit de test usé peut rejeter de bonnes "
                  "unités toute la journée. Avant de dessiner, que faut-il rassembler ?",
    },
    {
        "key": "p07", "num": 7, "title": "Rassembler les preuves d'abord",
        "points": [("Un Pareto des types de défauts", "un Pareto"),
                   ("Séparer par équipe, lot, poste, testeur", "Séparez les données"),
                   ("Comparer bonnes et mauvaises unités", "Comparez les bonnes unités")],
        "example": "Les échecs se concentraient sur deux des quatre postes de test.",
        "example_cue": "La première séparation de Nikhil",
        "script": "Apportez des données dans la salle. Commencez par un Pareto des types de défauts, pour "
                  "travailler sur le plus gros. Séparez les données par équipe, lot, poste et testeur. "
                  "Comparez les bonnes unités aux mauvaises, côte à côte. La première séparation de Nikhil "
                  "a été une surprise. La plupart des échecs venaient de seulement deux des quatre postes "
                  "de test. Que soupçonneriez-vous, rien qu'avec ça ?",
    },
    {
        "key": "p08", "num": 8, "title": "Le construire : huit étapes",
        "points": [("Définir l'effet, réunir l'équipe", "Définissez l'effet"),
                   ("Dessiner les arêtes, brainstormer, sans reproche", "Dessinez la tête"),
                   ("Demander pourquoi, regrouper, prioriser", "Demandez pourquoi cela pourrait"),
                   ("Attribuer des responsables pour tester les causes", "Attribuez un responsable")],
        "example": "L'équipe de Nikhil : production, qualité, test, maintenance et magasin.",
        "example_cue": "L'équipe de Nikhil",
        "script": "Construisez-le en huit étapes. Définissez l'effet, et réunissez une équipe transverse. "
                  "Dessinez la tête, la colonne et les familles. Faites un brainstorming des causes sans "
                  "débat et sans reproche. Demandez pourquoi cela pourrait arriver, pour creuser. Regroupez "
                  "les doublons, et priorisez avec des données. Attribuez un responsable pour tester chaque "
                  "cause. L'équipe de Nikhil réunissait la production, la qualité, le test, la maintenance "
                  "et le magasin. Pourquoi inclure le magasin ?",
    },
    {
        "key": "p09", "num": 9, "title": "L'arête de poisson de Nikhil",
        "points": [("Machine : dérive de la hauteur d'emmanchement", "La machine avait"),
                   ("Mesure : câbles de test usés", "La mesure avait"),
                   ("Matière, méthode, main-d'œuvre, milieu", "Les autres arêtes")],
        "example": "Vingt-trois causes possibles en quarante minutes.",
        "example_cue": "En quarante minutes",
        "script": "Parce que les problèmes de matière commencent souvent au magasin. Voici ce que l'équipe "
                  "a trouvé. La machine avait un outil d'emmanchement dont la butée en hauteur pouvait "
                  "dériver. La mesure avait des câbles de bouclage, branchés des milliers de fois. Les "
                  "autres arêtes portaient un nouveau lot de ports du fournisseur, un contrôle d'engagement "
                  "manquant, une équipe intérimaire et les enregistrements ESD. En quarante minutes, ils "
                  "avaient vingt-trois causes possibles. Laquelle tester en premier ?",
    },
    {
        "key": "p10", "num": 10, "title": "Arête de poisson, puis cinq pourquoi",
        "points": [("L'arête de poisson va en largeur", "L'arête de poisson va en largeur"),
                   ("Les cinq pourquoi vont en profondeur", "Les cinq pourquoi vont en profondeur"),
                   ("Ne jamais s'arrêter à l'erreur de l'opérateur", "ne vous arrêtez jamais")],
        "example": "Pourquoi des câbles usés ? Pas de limite de remplacement. Pourquoi ? Les câbles "
                   "n'étaient pas dans le plan de maintenance.",
        "example_cue": "Prenez les câbles de test",
        "script": "Utilisez deux outils ensemble. L'arête de poisson va en largeur, pour trouver des "
                  "candidats. Les cinq pourquoi vont en profondeur, sur un chemin choisi. Prenez les câbles "
                  "de test. Pourquoi étaient-ils usés ? Personne ne les remplaçait. Pourquoi ? Ils "
                  "n'étaient dans aucun plan de maintenance. Et ne vous arrêtez jamais à l'erreur de "
                  "l'opérateur. Demandez ce qui a rendu l'erreur possible. Mais une chaîne convaincante "
                  "n'est toujours pas une preuve. Comment prouver une cause ?",
    },
    {
        "key": "p11", "num": 11, "title": "Le prouver : l'échelle des preuves",
        "points": [("L'observer au Gemba", "Observez la condition au Gemba"),
                   ("Tracer et mesurer", "Tracez les échecs"),
                   ("Expérimenter, puis reproduire", "Faites une expérience contrôlée")],
        "example": "Les votes ne comptent pas. Un seul bon essai n'est pas une preuve non plus.",
        "example_cue": "Les votes ne comptent pas",
        "script": "Montez une échelle des preuves. Observez la condition au Gemba. Tracez les échecs "
                  "jusqu'aux lots, équipes, postes et équipements. Mesurez avec des instruments étalonnés. "
                  "Faites une expérience contrôlée, en changeant un facteur à la fois. Puis reproduisez-la, "
                  "pour montrer que l'effet disparaît vraiment. Les votes ne comptent pas comme preuve. Et "
                  "un seul bon essai n'est pas une preuve non plus. Alors, qu'a prouvé Nikhil ?",
    },
    {
        "key": "p12", "num": 12, "title": "Deux causes, toutes deux réelles",
        "points": [("Câbles usés : faux échecs", "Des câbles neufs ont supprimé"),
                   ("Dérive de hauteur : vrais échecs", "la butée d'emmanchement"),
                   ("Les causes peuvent coexister", "Deux causes")],
        "example": "Retest avec des câbles neufs : 6 switchs « défaillants » sur 10 ont réussi. Les 4 autres "
                   "avaient des ports trop peu enfoncés.",
        "example_cue": "Il a retesté",
        "script": "Il a retesté dix switchs défaillants, avec des câbles tout neufs. Six d'entre eux ont "
                  "réussi. Des câbles neufs ont supprimé immédiatement les faux échecs. Les quatre autres "
                  "échouaient vraiment. Leurs ports étaient trop peu enfoncés, parce que la butée "
                  "d'emmanchement avait dérivé. Deux causes, toutes deux réelles, en même temps. Cela "
                  "arrive plus souvent qu'on ne le pense. N'en corriger qu'une laisserait la moitié du "
                  "problème. Un nouveau testeur n'aurait corrigé ni l'une ni l'autre. Alors, quelles "
                  "actions mèneriez-vous ?",
    },
    {
        "key": "p13", "num": 13, "title": "Des actions correctives fortes",
        "points": [("Supprimer la cause par conception avant de reformer", "Supprimez la cause par la conception"),
                   ("Verrous, interverrouillages, compteurs", "Utilisez des verrous"),
                   ("Mettre à jour le SOP, le PFMEA, le plan de contrôle", "mettez à jour le SOP")],
        "example": "Compteur d'insertions sur le câble avec une limite de remplacement. Contrôle et "
                   "verrouillage de la hauteur à chaque début d'équipe.",
        "example_cue": "L'équipe de Nikhil a ajouté",
        "script": "Supprimez la cause par la conception, avant de compter sur des rappels ou une nouvelle "
                  "formation. Utilisez des verrous, des interverrouillages, des compteurs et des gabarits. "
                  "Puis mettez à jour le SOP, le PFMEA, le plan de contrôle et la formation, ensemble. "
                  "L'équipe de Nikhil a ajouté un compteur d'insertions sur chaque câble de test, avec une "
                  "limite de remplacement. Et la hauteur d'emmanchement était contrôlée et verrouillée à "
                  "chaque début d'équipe. Comment sauriez-vous que ça a marché ?",
    },
    {
        "key": "p14", "num": 14, "title": "Prouver que ça a marché",
        "points": [("Fixer la cible avant de commencer", "Fixez votre cible"),
                   ("Une fenêtre fixe et une taille d'échantillon", "Décidez d'une fenêtre fixe"),
                   ("32 → 4 pour 1 000, tenu pendant 30 jours", "Les échecs sont tombés")],
        "example": "Zéro faux échec dû à des câbles usés, sur 30 jours de production.",
        "example_cue": "Et pas un seul",
        "script": "Fixez votre cible avant le changement, pas après avoir vu les résultats. Décidez d'une "
                  "fenêtre fixe et d'une taille d'échantillon. Nikhil a choisi trente jours de production. "
                  "Il a aussi mis le compteur à l'épreuve avec un câble usé, pour prouver qu'il bloquait "
                  "son usage. Les échecs sont tombés de trente-deux pour mille à quatre, et y sont restés. "
                  "Et pas un seul faux échec n'est venu d'un câble usé. Le budget du testeur est retourné "
                  "dans le tiroir. Quelles erreurs faut-il éviter ?",
    },
    {
        "key": "p15", "num": 15, "title": "Erreurs et bonnes pratiques",
        "points": [("Effets vagues et défauts mélangés", "Un effet vague"),
                   ("Des fonctions absentes de la salle", "Laisser de côté"),
                   ("Pas de validation après la séance", "S'arrêter après")],
        "example": "Gardez les causes rejetées sur le diagramme, avec la preuve qui les a écartées.",
        "example_cue": "Gardez les causes rejetées",
        "script": "Attention à quelques erreurs. Un effet vague, ou plusieurs défauts mélangés. Laisser de "
                  "côté la maintenance, le test ou le magasin. Écrire négligence de l'opérateur au lieu de "
                  "regarder le système. S'arrêter après le brainstorming, sans tests et sans responsables. "
                  "Gardez les causes rejetées sur le diagramme, avec la preuve qui les a écartées. Votre "
                  "prochaine équipe vous remerciera. Quelle erreur avez-vous déjà vue ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Causes possibles", "icon": "search", "with": 1},
        {"label": "Familles de causes", "icon": "stack", "with": 1},
        {"label": "Le problème", "sub": "Dans la tête", "icon": "warning", "tone": "bad", "with": 0}]},
    "p02": {"type": "versus", "items": [
        {"label": "Preuve", "sub": "Ne vient pas de l'arête de poisson", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Causes possibles", "sub": "Ce qu'elle montre", "icon": "search", "tone": "good", "with": 2}]},
    "p03": {"type": "icons", "items": [
        {"label": "Tête", "sub": "L'effet", "icon": "warning", "with": 0},
        {"label": "Grandes arêtes", "sub": "Familles de causes", "icon": "stack", "with": 1},
        {"label": "Petites arêtes", "sub": "Causes précises", "icon": "search", "with": 2}]},
    "p04": {"type": "versus", "items": [
        {"label": "« La qualité est mauvaise »", "sub": "Vague", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "5 → 32 pour 1 000", "sub": "Ligne 3, liaison des ports, cette semaine", "icon": "check", "tone": "good", "with": "example"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Main-d'œuvre", "icon": "person", "with": 0},
        {"label": "Machine", "icon": "gear", "with": 1},
        {"label": "Méthode", "icon": "clipboard", "with": 2}]},
    "p06": {"type": "icons", "items": [
        {"label": "Matière", "icon": "box", "with": 0},
        {"label": "Mesure", "icon": "scale", "tone": "bad", "with": 1},
        {"label": "Milieu", "icon": "wave", "with": 2}]},
    "p07": {"type": "bars", "label": "", "note": "Échecs de liaison des ports par poste de test", "with": "example", "items": [
        {"label": "T1", "value": 14, "tone": "bad", "with": "example"},
        {"label": "T2", "value": 3, "with": "example"},
        {"label": "T3", "value": 12, "tone": "bad", "with": "example"},
        {"label": "T4", "value": 3, "with": "example"}]},
    "p08": {"type": "steps", "items": [
        {"label": "Définir, équipe", "with": 0}, {"label": "Dessiner, brainstormer", "with": 1},
        {"label": "Pourquoi ? Regrouper, classer", "with": 2}, {"label": "Les responsables testent", "with": 3}]},
    "p09": {"type": "icons", "items": [
        {"label": "Machine", "sub": "Dérive de hauteur d'emmanchement", "icon": "gear", "with": 0},
        {"label": "Mesure", "sub": "Câbles de test usés", "icon": "scale", "with": 1},
        {"label": "Matière", "sub": "Nouveau lot de ports", "icon": "box", "with": 2},
        {"label": "Méthode", "sub": "Pas de contrôle d'engagement", "icon": "clipboard", "with": 2},
        {"label": "Main-d'œuvre", "sub": "Équipe intérimaire", "icon": "person", "with": 2},
        {"label": "Milieu", "sub": "Enregistrements ESD", "icon": "wave", "with": 2}],
        "then": {"type": "stat", "value": 23, "icon": "search", "label": "causes possibles en 40 minutes",
                 "unit": "chacune reste une supposition", "with": "example"}},
    "p10": {"type": "steps", "items": [
        {"label": "Câbles usés", "with": "example"},
        {"label": "Jamais remplacés", "with": "example"},
        {"label": "Absents du plan de maintenance", "with": "example"}]},
    "p11": {"type": "ladder", "top": "LE PLUS FORT", "bottom": "LE PLUS FAIBLE", "items": [
        {"label": "Reproduire", "icon": "check", "with": 2},
        {"label": "Expérimenter", "icon": "test", "with": 2},
        {"label": "Tracer et mesurer", "icon": "scale", "with": 1},
        {"label": "Observer", "icon": "search", "with": 0}]},
    "p12": {"type": "bars", "label": "", "note": "10 switchs défaillants retestés avec des câbles neufs : 6 ont réussi, 4 avaient des "
                                                 "ports trop peu enfoncés", "with": "example", "items": [
        {"label": "Faux échecs", "value": 6, "with": "example"},
        {"label": "Vrais échecs", "value": 4, "tone": "bad", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Compteur d'insertions sur le câble", "icon": "count", "with": "example"},
        {"label": "Verrouillage de la hauteur d'emmanchement", "icon": "lock", "with": "example"},
        {"label": "SOP, PFMEA, plan de contrôle", "icon": "clipboard", "tone": "good", "with": 2}]},
    "p14": {"type": "compare", "before": {"label": "Avant", "value": 32}, "after": {"label": "Après", "value": 4},
            "unit": "échecs de liaison des ports pour 1 000 switchs", "note": "Tenu pendant 30 jours de production", "with": 2},
    "p15": {"type": "icons", "items": [
        {"label": "Effet vague", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Fonctions absentes", "icon": "person", "tone": "bad", "with": 1},
        {"label": "Pas de validation", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Garder les causes rejetées", "icon": "clipboard", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Quel est le meilleur effet à mettre dans la tête d'une arête de poisson ?",
        "options": ["« Problèmes de qualité sur la ligne de switchs »",
                    "« Les échecs de liaison des ports sur la ligne 3 sont passés de 5 à 32 pour 1 000 cette "
                    "semaine »",
                    "« Le testeur est mauvais »"],
        "correct": 1,
        "explanation": "Une bonne tête nomme un défaut, le lieu, la période et l'ampleur, avec une référence. « "
                       "Le testeur est mauvais » est déjà une cause.",
        "q_script": "Vérification rapide. Lequel de ces effets est le meilleur à mettre dans la tête d'une "
                    "arête de poisson ? Prenez quelques secondes.",
        "a_script": "C'est le deuxième. Il nomme un défaut, le lieu, la période et l'ampleur. Le dernier est "
                    "déjà une cause.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Après le brainstorming, l'équipe vote « négligence de l'opérateur » comme cause "
                    "principale. Et ensuite ?",
        "options": ["Reformer les opérateurs : l'équipe est d'accord",
                    "Demander ce qui a rendu l'erreur possible, et tester les causes avec des preuves",
                    "Mettre un panneau d'avertissement au poste"],
        "correct": 1,
        "explanation": "Un vote n'est pas une preuve, et la négligence n'est pas une cause maîtrisable. Demandez "
                       "quelle condition du processus a rendu l'erreur possible, puis prouvez-la.",
        "q_script": "Encore une, et cette fois c'est un scénario. Après le brainstorming, l'équipe vote "
                    "négligence de l'opérateur comme cause principale. Que faut-il faire ensuite ? "
                    "Réfléchissez.",
        "a_script": "Demandez ce qui a rendu l'erreur possible, et testez chaque cause avec des preuves. Un "
                    "vote n'est pas une preuve, et la négligence n'est pas une cause que vous pouvez "
                    "maîtriser.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
