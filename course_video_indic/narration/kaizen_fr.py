"""kaizen in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh kaizen_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "kz_fr"
NAME = "kaizen_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Low Cost Automation": "lo coste otoméïchone",
    "Kaizen": "Kaïzène",
    "Gemba": "Guemba",
    "Check": "tchèk",
    "Plan": "plane",
    "PDCA": "pé dé cé a",
    "SDCA": "esse dé cé a",
    "ECRS": "eu cé erre esse",
    "TAKT": "takte",
    "SOP": "esse o pé",
    "Act": "akte",
    "Do": "dou",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Chaque moniteur de la ligne de Suresh était retourné deux fois. Face contre la table, "
    "puis de nouveau face visible. Personne ne demandait pourquoi. On avait toujours fait "
    "comme ça. Ça vous dit quelque chose ? Dans cette leçon, vous allez découvrir le Kaizen, "
    "l'amélioration continue. Vous verrez comment de petits changements testés, faits par les "
    "personnes qui font le travail, s'additionnent en grands résultats. Nous suivrons Suresh, "
    "chef de ligne en assemblage de moniteurs."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Le Kaizen est une habitude quotidienne, pas un événement "
    "ponctuel. Testez en petit, mesurez honnêtement, et vérifiez que rien d'autre ne s'est "
    "dégradé. Et standardisez chaque gain, pour qu'il devienne le point de départ du suivant. "
    "Voici votre action pour cette semaine. Demandez à un opérateur ce qui rend son travail "
    "difficile, et testez une petite solution. Bravo d'avoir terminé cette leçon. Ensuite, "
    "vous découvrirez Low Cost Automation."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce que veut dire Kaizen",
        "points": [("Changer pour le meilleur", "changer pour le meilleur"),
                   ("Beaucoup de petits changements disciplinés", "beaucoup de petits changements"),
                   ("Faits par les personnes les plus proches du travail", "Ce sont les personnes")],
        "example": "La ligne de Suresh : deux retournements de chaque moniteur, chaque unité, chaque équipe.",
        "example_cue": "Sur la ligne de Suresh",
        "script": "Kaizen est un mot japonais qui veut dire changer pour le meilleur. Dans une usine, il "
                  "désigne l'amélioration continue par beaucoup de petits changements. Ce sont les "
                  "personnes les plus proches du travail qui les font, chaque jour. Pas un grand projet, "
                  "une fois par an. Sur la ligne de Suresh, chaque moniteur était retourné deux fois, dans "
                  "chaque équipe. Cela fait des milliers de levages lourds par semaine. Alors, qu'est-ce "
                  "qui fait d'une amélioration un Kaizen ?",
    },
    {
        "key": "p02", "num": 2, "title": "Ce qui en fait un Kaizen",
        "points": [("Continu et porté par les personnes", "Il est continu"),
                   ("Commence au Gemba", "Il commence au Gemba"),
                   ("D'abord peu coûteux, appuyé sur des données", "Il essaie d'abord"),
                   ("Se termine par un nouveau standard", "Et il se termine")],
        "example": "Chaque standard amélioré est la base du Kaizen suivant.",
        "example_cue": "Puis le cycle",
        "script": "Quelques éléments le distinguent. Il est continu, et porté par les personnes, pas "
                  "seulement par les ingénieurs. Il commence au Gemba, avec ce que vous voyez réellement. "
                  "Il essaie d'abord des idées peu coûteuses, et vérifie les résultats avec des données. Et "
                  "il se termine par un nouveau standard, la meilleure méthode connue aujourd'hui. Puis le "
                  "cycle recommence, à partir de cette nouvelle base. Quel état d'esprit cela demande-t-il "
                  "?",
    },
    {
        "key": "p03", "num": 3, "title": "L'état d'esprit Kaizen",
        "points": [("Tout processus peut s'améliorer", "Tout processus peut"),
                   ("Les problèmes servent à apprendre, pas à blâmer", "Les problèmes sont"),
                   ("La créativité avant le capital", "la créativité avant le capital")],
        "example": "« On l'a toujours retourné » est exactement la phrase que le Kaizen remet en question.",
        "example_cue": "On l'a toujours",
        "script": "Tout part d'une conviction. Tout processus peut s'améliorer, même un bon. Les problèmes "
                  "sont des occasions d'apprendre, pas des raisons de blâmer quelqu'un. Allez voir avant de "
                  "décider. Et utilisez la créativité avant le capital. Un marquage au ruban bat souvent "
                  "une nouvelle machine. On l'a toujours fait comme ça, c'est exactement la phrase que le "
                  "Kaizen remet en question. Quand l'avez-vous entendue pour la dernière fois sur votre "
                  "ligne ?",
    },
    {
        "key": "p04", "num": 4, "title": "Types de Kaizen",
        "points": [("Kaizen quotidien : de quelques minutes à quelques jours", "Le Kaizen quotidien"),
                   ("Kaizen ponctuel : une perte précise", "Le Kaizen ponctuel"),
                   ("Événement Kaizen : trois à cinq jours", "Un événement Kaizen"),
                   ("Kaizen système : le flux de bout en bout", "Le Kaizen système")],
        "example": "Le double retournement : un Kaizen ponctuel, porté par l'équipe de Suresh elle-même.",
        "example_cue": "Le double retournement",
        "script": "Le Kaizen existe en plusieurs tailles. Le Kaizen quotidien est petit et local, comme "
                  "rapprocher un outil. Le Kaizen ponctuel vise une perte précise, en quelques heures ou "
                  "quelques jours. Un événement Kaizen réunit une équipe transverse pendant trois à cinq "
                  "jours. Le Kaizen système corrige le flux entre les services, sur plusieurs semaines. Le "
                  "double retournement était un Kaizen ponctuel, porté par l'équipe de Suresh elle-même. "
                  "Quelle taille convient à votre plus gros problème ?",
    },
    {
        "key": "p05", "num": 5, "title": "Le Kaizen fonctionne avec le PDCA",
        "points": [("Plan : observer, définir, trouver la cause", "Plan veut dire"),
                   ("Do : un essai petit et sûr", "Do veut dire"),
                   ("Check : comparer à la référence", "Check veut dire"),
                   ("Act : standardiser, ou apprendre et recommencer", "Act veut dire")],
        "example": "Le SDCA maintient le standard. Le PDCA l'améliore.",
        "example_cue": "Son jumeau",
        "script": "Chaque Kaizen suit le PDCA. Plan veut dire observer, définir l'écart, et trouver la "
                  "cause. Do veut dire un essai petit et sûr. Check veut dire comparer le résultat à votre "
                  "référence et à votre cible. Act veut dire le standardiser, ou apprendre et réessayer. "
                  "Son jumeau est le SDCA, qui tient le standard stable. Les équipes fortes passent de l'un "
                  "à l'autre. Sans le PDCA, une idée n'est qu'un changement non testé. Par où commencer ?",
    },
    {
        "key": "p06", "num": 6, "title": "Le voir au Gemba",
        "points": [("Observer le travail tel qu'il est vraiment", "Observez le travail"),
                   ("Compter marches, gestes, retournements", "Comptez les marches"),
                   ("Demander ce qui rend le travail difficile", "Demandez aux opérateurs")],
        "example": "Retourner face en bas pour monter le pied, face en haut pour tester. Deux levages d'un "
                   "moniteur de 6 kg.",
        "example_cue": "L'équipe de Suresh l'a vu",
        "script": "Au Gemba, bien sûr. Observez le travail tel qu'il est vraiment, pas tel que le SOP le "
                  "décrit. Comptez les marches, les gestes, les recherches et les levages. Demandez aux "
                  "opérateurs ce qui rend leur travail difficile. L'équipe de Suresh l'a vu tout de suite. "
                  "Chaque moniteur passait face en bas pour monter le pied, puis de nouveau face en haut "
                  "pour le test. Deux levages d'un moniteur de six kilos, à chaque fois. Que noteriez-vous "
                  "?",
    },
    {
        "key": "p07", "num": 7, "title": "Définir le problème",
        "points": [("Le symptôme, puis les faits", "Commencez par le symptôme"),
                   ("Mesurer la perte", "Mesurez la perte"),
                   ("Une cible avec une échéance", "Fixez une cible")],
        "example": "Cycle de 38 s contre un TAKT de 35 s. 2 retournements par unité. 15 dalles rayées pour "
                   "1 000.",
        "example_cue": "Les faits de Suresh",
        "script": "Commencez par le symptôme. La ligne ratait son objectif horaire. Puis rassemblez les "
                  "faits. Mesurez la perte, et séparez les faits des opinions. Les faits de Suresh étaient "
                  "clairs. Le temps de cycle était de trente-huit secondes, contre un TAKT de trente-cinq. "
                  "Chaque retournement risquait une rayure, et quinze dalles sur mille étaient rayées. "
                  "Fixez une cible avec une échéance, et laissez la solution de côté. Que viseriez-vous ?",
    },
    {
        "key": "p08", "num": 8, "title": "Trouver des idées",
        "points": [("Demander d'abord aux opérateurs", "Demandez d'abord aux opérateurs"),
                   ("Utiliser ECRS", "Utilisez ECRS"),
                   ("Regarder d'autres lignes", "Regardez d'autres lignes")],
        "example": "Leela, une opératrice : « Pourquoi ne pas monter le pied pendant que le moniteur est "
                   "encore dans son plateau ? »",
        "example_cue": "Leela, une opératrice",
        "script": "Trouvez maintenant des idées, et beaucoup. Demandez d'abord aux opérateurs. Qu'est-ce "
                  "qui rend ce travail difficile ? Qu'est-ce qui supprimerait une étape ? Utilisez ECRS, "
                  "éliminer, combiner, réordonner et simplifier. Regardez d'autres lignes, et d'autres "
                  "secteurs aussi. Leela, une opératrice de l'équipe de nuit, a eu la meilleure idée. "
                  "Pourquoi ne pas monter le pied pendant que le moniteur est encore face en bas, dans son "
                  "plateau ? Pourquoi personne ne le lui avait-il demandé avant ?",
    },
    {
        "key": "p09", "num": 9, "title": "Choisir l'idée",
        "points": [("La sécurité et la qualité sont des filtres", "La sécurité et la qualité"),
                   ("Noter impact, facilité, coût, rapidité", "Puis notez"),
                   ("Elle doit corriger une cause vérifiée", "Et l'idée doit")],
        "example": "L'idée de Leela : forte sur l'impact, la facilité et le coût. Elle a gagné.",
        "example_cue": "L'idée de Leela",
        "script": "Choisissez avec une grille de notation simple. La sécurité et la qualité sont des "
                  "filtres. Si une idée échoue, elle est éliminée, quelle que soit sa note. Puis notez "
                  "l'impact, la facilité, le coût et la rapidité, avec des pondérations convenues. Et "
                  "l'idée doit traiter une cause que vous avez vérifiée. Elle doit être assez simple pour "
                  "que tout le monde la suive. L'idée de Leela a eu une note élevée sur l'impact, la "
                  "facilité et le coût. Elle a gagné facilement. Comment l'essayer ?",
    },
    {
        "key": "p10", "num": 10, "title": "L'essayer en petit",
        "points": [("Une hypothèse et un périmètre", "Écrivez une hypothèse"),
                   ("Mêmes mesures que la référence", "Mesurez-la de la même façon"),
                   ("Observer les personnes, pas seulement les chiffres", "Observez les opérateurs")],
        "example": "Un poste, une équipe : étapes réordonnées et une mousse dans le plateau. Coût : presque "
                   "rien.",
        "example_cue": "L'essai de Suresh",
        "script": "D'abord petit et sûr. Écrivez une hypothèse. Si nous montons le pied dans le plateau, "
                  "les deux retournements disparaissent. Fixez le périmètre, un poste et une équipe. "
                  "Mesurez-la de la même façon que la référence. Observez les opérateurs, pas seulement les "
                  "chiffres. L'essai de Suresh a eu lieu sur un poste, pendant une équipe. Il utilisait des "
                  "étapes réordonnées et une mousse dans le plateau. Il n'a presque rien coûté. Que "
                  "s'est-il passé ?",
    },
    {
        "key": "p11", "num": 11, "title": "Vérifier les résultats",
        "points": [("Temps de cycle : de 38 s à 33 s", "Le temps de cycle est tombé"),
                   ("Retournements par unité : de 2 à 0", "Les deux retournements"),
                   ("Rayures : de 15 à 3 pour 1 000", "Les rayures sont tombées"),
                   ("Rien d'autre ne s'est dégradé", "rien d'autre ne s'est dégradé")],
        "example": "Règle de l'équilibre : la cible s'améliore, et la sécurité, la qualité et la livraison "
                   "n'en souffrent pas.",
        "example_cue": "C'est la règle de l'équilibre",
        "script": "Le temps de cycle est tombé à trente-trois secondes, désormais sous le TAKT. Les deux "
                  "retournements ont disparu. Les rayures sont tombées de quinze à trois pour mille. Et "
                  "l'équipe a vérifié que rien d'autre ne s'est dégradé. Les résultats de test, la sécurité "
                  "et le poste suivant ont tenu. Les opérateurs ont dit que leur dos sentait la différence "
                  "dès le déjeuner. C'est la règle de l'équilibre. Améliorer un chiffre en en abîmant un "
                  "autre, ce n'est pas du Kaizen. Mais comment savoir que ça va durer ?",
    },
    {
        "key": "p12", "num": 12, "title": "Mesurer honnêtement",
        "points": [("Mêmes définitions, avant et après", "Utilisez les mêmes définitions"),
                   ("Compter la bonne production, pas la brute", "Comptez la bonne production"),
                   ("Revérifier à 30, 60, 90 jours", "revérifiez")],
        "example": "Jour 30 : toujours 33 s. Jour 90 : toujours 33 s, et 3 rayures pour 1 000.",
        "example_cue": "Suresh a vérifié",
        "script": "Mesurez honnêtement. Utilisez les mêmes définitions avant et après. Comptez la bonne "
                  "production, pas la production brute. Montrez le changement réel, pas seulement un "
                  "pourcentage. Et vérifiez qu'autre chose, comme un mix de modèles plus facile, n'en est "
                  "pas la cause. Puis revérifiez à trente, soixante et quatre-vingt-dix jours. Suresh a "
                  "vérifié au jour trente, puis au jour quatre-vingt-dix. Toujours trente-trois secondes. "
                  "Qu'est-ce qui le verrouille ?",
    },
    {
        "key": "p13", "num": 13, "title": "Standardiser le gain",
        "points": [("Mettre à jour le SOP et le travail standard", "Mettez à jour le SOP"),
                   ("Former tout le monde, retirer l'ancienne façon", "Formez chaque opérateur"),
                   ("Nommer un responsable et auditer", "Nommez un responsable")],
        "example": "Les anciennes instructions de retournement ont été retirées de chaque poste la même "
                   "semaine.",
        "example_cue": "Suresh a retiré",
        "script": "Un Kaizen n'est pas terminé tant qu'il n'est pas le standard. Mettez à jour le SOP et le "
                  "travail standard. Formez chaque opérateur, et confirmez qu'il a compris. Retirez "
                  "l'ancienne méthode, pour que personne n'y revienne. Nommez un responsable, et auditez. "
                  "Suresh a retiré les anciennes instructions de retournement de chaque poste, la même "
                  "semaine. La nouvelle méthode est devenue la base. Et la base, c'est là que commence le "
                  "Kaizen suivant. Comment garder les idées qui arrivent ?",
    },
    {
        "key": "p14", "num": 14, "title": "En faire une habitude",
        "points": [("Un tableau d'idées visible", "Un tableau d'idées visible"),
                   ("Des réponses rapides à chaque idée", "Répondez à chaque idée"),
                   ("Reconnaître les personnes", "Reconnaissez")],
        "example": "L'équipe de Suresh : 40 idées en 3 mois, 27 testées, 19 standardisées.",
        "example_cue": "En trois mois",
        "script": "Faites du Kaizen une habitude quotidienne. Un tableau d'idées visible aide les gens à "
                  "voir que leurs idées comptent. Répondez à chaque idée en moins d'une semaine, même quand "
                  "la réponse est non. Reconnaissez les personnes, pas seulement les économies. Et revoyez "
                  "chaque semaine les idées en cours. En trois mois, l'équipe de Suresh a enregistré "
                  "quarante idées. Elle en a testé vingt-sept, et standardisé dix-neuf. Que se passerait-il "
                  "sur votre ligne ?",
    },
    {
        "key": "p15", "num": 15, "title": "Commencer demain",
        "points": [("Choisir un problème récurrent", "Choisissez un problème récurrent"),
                   ("Observer dix cycles, parler à l'équipe", "Observez dix cycles"),
                   ("Tester la plus petite solution sûre", "testez la plus petite solution sûre")],
        "example": "Kaizen = petites améliorations × répétition disciplinée × sens des responsabilités.",
        "example_cue": "De petites améliorations",
        "script": "Voici comment commencer demain. Choisissez un problème récurrent sur votre ligne. "
                  "Observez dix cycles, et mesurez la perte. Parlez aux personnes qui font le travail, et "
                  "fixez une cible mesurable. Puis testez la plus petite solution sûre possible. Si elle "
                  "marche, standardisez-la. De petites améliorations, répétées avec discipline, par des "
                  "personnes qui s'en sentent responsables. C'est ainsi que des lignes ordinaires "
                  "deviennent excellentes. À qui demanderez-vous en premier ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Changer pour le meilleur", "icon": "chartUp", "with": 0},
        {"label": "Petits pas", "icon": "sequence", "with": 1},
        {"label": "Par l'équipe", "icon": "person", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 2, "icon": "weight", "label": "retournements de chaque moniteur",
                 "unit": "chaque unité, chaque équipe", "with": "example"}},
    "p02": {"type": "icons", "items": [
        {"label": "Continu", "icon": "sequence", "with": 0},
        {"label": "Basé sur le Gemba", "icon": "walk", "with": 1},
        {"label": "Peu coûteux, données", "icon": "scale", "with": 2},
        {"label": "Nouveau standard", "icon": "clipboard", "tone": "good", "with": 3}]},
    "p03": {"type": "versus", "items": [
        {"label": "« On a toujours fait comme ça »", "sub": "Accepter la perte", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "« Tout processus peut s'améliorer »", "sub": "Kaizen", "icon": "check", "tone": "good", "with": 0}]},
    "p04": {"type": "ladder", "top": "LE PLUS GRAND", "bottom": "LE PLUS PETIT", "items": [
        {"label": "Kaizen système", "sub": "Semaines", "icon": "stack", "with": 3},
        {"label": "Événement Kaizen", "sub": "3–5 jours", "icon": "calendar", "with": 2},
        {"label": "Kaizen ponctuel", "sub": "Heures à jours", "icon": "pin", "with": 1},
        {"label": "Kaizen quotidien", "sub": "Minutes", "icon": "hand", "with": 0}]},
    "p05": {"type": "flow", "items": [
        {"label": "Plan", "icon": "clipboard", "with": 0},
        {"label": "Do", "icon": "wrench", "with": 1},
        {"label": "Check", "icon": "search", "with": 2},
        {"label": "Act", "icon": "check", "tone": "good", "with": 3}]},
    "p06": {"type": "flow", "items": [
        {"label": "Face en bas : monter le pied", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Face en haut : tester", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Deux levages de 6 kg", "icon": "warning", "tone": "bad", "with": "example"}]},
    "p07": {"type": "bars", "label": "TAKT", "value": 35, "suffix": " s", "with": "example", "items": [
        {"label": "Temps de cycle", "value": 38, "tone": "bad", "with": "example"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Demander aux opérateurs", "icon": "person", "with": 0},
        {"label": "ECRS", "icon": "key", "with": 1},
        {"label": "Autres lignes", "icon": "search", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Retourner deux fois", "sub": "Aujourd'hui", "icon": "weight", "tone": "bad", "with": "example"},
            {"label": "Monter le pied dans le plateau", "sub": "L'idée de Leela", "icon": "check", "tone": "good", "with": "example"}]}},
    "p09": {"type": "icons", "with": "example", "items": [
        {"label": "Bras robotisé", "sub": "Note 2,4", "icon": "gear", "with": "example"},
        {"label": "Aide au levage", "sub": "Note 3,6", "icon": "weight", "with": "example"},
        {"label": "L'idée de Leela", "sub": "Note 4,7 sur 5", "icon": "check", "tone": "good", "with": "example"}]},
    "p10": {"type": "doc", "items": [
        {"label": "Hypothèse : les deux retournements disparaissent", "icon": "key", "with": 0},
        {"label": "Périmètre : un poste, une équipe", "icon": "pin", "with": 0},
        {"label": "Mêmes mesures que la référence", "icon": "scale", "with": 1},
        {"label": "Mousse + nouvelle séquence", "icon": "shape", "with": "example"}]},
    "p11": {"type": "compare", "before": {"label": "Avant", "value": 15}, "after": {"label": "Essai", "value": 3},
            "unit": "dalles rayées pour 1 000 moniteurs", "note": "Cycle 38 s → 33 s · retournements 2 → 0", "with": 2},
    "p12": {"type": "timeline", "items": [
        {"label": "Référence", "sub": "Avant", "icon": "clipboard", "with": 0},
        {"label": "Toujours 33 s", "sub": "Jour 30", "icon": "check", "with": "example"},
        {"label": "Toujours 33 s", "sub": "Jour 90", "icon": "check", "tone": "good", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Mettre à jour le SOP", "icon": "clipboard", "with": 0},
        {"label": "Former, retirer l'ancienne façon", "icon": "person", "with": 1},
        {"label": "Responsable et audit", "icon": "search", "tone": "good", "with": 2}]},
    "p14": {"type": "bars", "label": "", "note": "L'équipe de Suresh, trois premiers mois", "with": "example", "items": [
        {"label": "Idées", "value": 40, "with": "example"},
        {"label": "Testées", "value": 27, "with": "example"},
        {"label": "Standardisées", "value": 19, "tone": "good", "with": "example"}]},
    "p15": {"type": "steps", "items": [
        {"label": "Un problème récurrent", "with": 0},
        {"label": "Dix cycles, parler à l'équipe", "with": 1},
        {"label": "La plus petite solution sûre", "with": 2},
        {"label": "Standardiser", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Quel est le meilleur énoncé de problème pour un Kaizen ?",
        "options": ["« Il nous faut un bras robotisé sur la ligne de moniteurs »",
                    "« Le temps de cycle est de 38 s contre un TAKT de 35 s, avec 2 retournements par unité ; "
                    "atteindre 35 s en 4 semaines »",
                    "« Les opérateurs sont trop lents »"],
        "correct": 1,
        "explanation": "Un bon énoncé contient l'écart mesuré, la perte observée et une cible avec une échéance, "
                       "sans nommer de solution ni blâmer les personnes.",
        "q_script": "Vérification rapide. Lequel de ces énoncés est le meilleur énoncé de problème pour un "
                    "Kaizen ? Prenez quelques secondes.",
        "a_script": "C'est le deuxième. Il contient l'écart mesuré, la perte observée, et une cible avec une "
                    "échéance. Les autres sont une solution et un reproche.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un essai réduit le temps de cycle de 4 secondes, mais les opérateurs signalent des "
                    "douleurs à l'épaule. Et maintenant ?",
        "options": ["Le standardiser : la cible s'est améliorée",
                    "Le considérer comme pas encore réussi : adapter la méthode et retester",
                    "Faire tourner les opérateurs chaque heure et le garder"],
        "correct": 1,
        "explanation": "La règle de l'équilibre : un Kaizen ne réussit que si la sécurité, la qualité et les "
                       "personnes n'en souffrent pas. Une douleur veut dire que la méthode doit changer avant de "
                       "devenir le standard.",
        "q_script": "Encore une, et cette fois c'est un scénario. Un essai réduit le temps de cycle de quatre "
                    "secondes. Mais les opérateurs signalent des douleurs à l'épaule. Que doit faire l'équipe "
                    "? Réfléchissez.",
        "a_script": "Ce n'est pas encore une réussite. Adaptez la méthode et retestez. Un Kaizen ne compte "
                    "que si la sécurité et les personnes ne paient pas le gain.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
