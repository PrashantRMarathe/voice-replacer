"""design_thinking in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh design_thinking_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "dt_fr"
NAME = "design_thinking_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Elimination of Waste": "éliminéïchone ov ouéïste",
    "Design Thinking": "dizaïne sinking",
    "Poka Yoke": "Poka Yoké",
    "SCAMPER": "scampeur",
    "Kaizen": "Kaïzène",
    "Gemba": "Guemba",
    "TAKT": "takte",
    "A3": "a trois",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "La ligne d'emballage manquait sans cesse son objectif. De mauvaises étiquettes passaient "
    "sans cesse. La première idée a été une imprimante plus rapide, pour beaucoup d'argent. "
    "Personne n'avait demandé aux emballeurs. Ça vous dit quelque chose ? Dans cette leçon, "
    "vous allez découvrir le Design Thinking. Vous verrez comment comprendre les personnes "
    "qui font le travail, résoudre le bon problème, et tester des idées à petit prix. Nous "
    "suivrons Pooja, ingénieure amélioration dans une usine de dispositifs médicaux."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Partez des personnes qui font le travail, et observez "
    "avant de décider. Définissez le besoin sans y cacher une solution. Et testez en petit, "
    "en mesurant les résultats et si les gens l'utilisent vraiment. Voici votre action pour "
    "cette semaine. Observez dix cycles d'un travail pénible, et parlez à trois personnes qui "
    "le font. Bravo d'avoir terminé cette leçon. Ensuite, vous découvrirez Elimination of "
    "Waste."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le Design Thinking",
        "points": [("Partir des personnes du processus", "part des personnes"),
                   ("Comprendre, définir, imaginer", "Vous faites preuve d'empathie"),
                   ("Prototyper et tester, puis recommencer", "Puis vous prototypez")],
        "example": "Le poste d'emballage de Pooja : pompes à perfusion, étiquettes, et des emballeurs à qui "
                   "personne n'avait demandé.",
        "example_cue": "Le défi de Pooja",
        "script": "Le Design Thinking est une façon de résoudre les problèmes qui part des personnes du "
                  "processus. Celles qui font le travail, le soutiennent, ou le reçoivent. Vous faites "
                  "preuve d'empathie, en observant le travail réel. Vous définissez le vrai besoin, et "
                  "imaginez de nombreuses options. Puis vous prototypez quelque chose de petit, vous le "
                  "testez, et vous apprenez. Et vous recommencez. Le défi de Pooja était le poste "
                  "d'emballage des pompes à perfusion. Alors, comment cela s'articule-t-il avec le Lean ?",
    },
    {
        "key": "p02", "num": 2, "title": "Design Thinking et Lean",
        "points": [("Ne remplace pas les outils Lean", "Il ne remplace pas l'A3"),
                   ("Trouve d'abord le bon problème", "Il vous aide à trouver"),
                   ("Les gens adoptent ce qu'ils aident à concevoir", "les gens adoptent")],
        "example": "La nouvelle méthode d'emballage de l'an dernier a duré deux semaines. Les emballeurs "
                   "sont revenus à l'ancienne façon.",
        "example_cue": "L'an dernier",
        "script": "Il ne remplace pas l'A3, le Kaizen ou le Poka Yoke. Il vous aide à trouver le bon "
                  "problème avant d'en choisir un. Le Lean élimine le gaspillage. Le Design Thinking "
                  "s'assure que le changement convient à de vraies personnes et à un vrai travail. Et voici "
                  "le bonus. Les gens adoptent ce qu'ils ont aidé à concevoir. L'an dernier, une nouvelle "
                  "méthode d'emballage a duré deux semaines. Puis les emballeurs sont revenus discrètement "
                  "à l'ancienne façon. Pourquoi, à votre avis ?",
    },
    {
        "key": "p03", "num": 3, "title": "Principes de travail",
        "points": [("Observer sans supposer", "Observez sans supposer"),
                   ("Séparer les faits des opinions", "Séparez les faits"),
                   ("Prototyper en petit avant les grands changements", "Essayez les idées en petit"),
                   ("Mesurer les résultats et l'adhésion", "Mesurez les deux")],
        "example": "La règle de Pooja : « Montrez-moi » avant « dites-moi ».",
        "example_cue": "La règle de Pooja",
        "script": "Quelques principes vous gardent honnête. Observez sans supposer que vous connaissez déjà "
                  "la réponse. Séparez les faits des opinions, et des solutions proposées. Traitez les "
                  "opérateurs et les équipes support comme vos utilisateurs. Essayez les idées en petit, "
                  "avant de changer tout le processus. Mesurez les deux, les résultats et l'adhésion réelle "
                  "des gens au changement. La règle de Pooja était simple. Montrez-moi, avant dites-moi. "
                  "Lequel de ces principes sautez-vous le plus souvent ?",
    },
    {
        "key": "p04", "num": 4, "title": "Ce qu'il évite",
        "points": [("Automatiser un processus défaillant", "Automatiser un processus défaillant"),
                   ("Ne corriger que le symptôme visible", "Ne corriger que"),
                   ("Des solutions que les gens ne peuvent pas suivre", "Imposer une solution"),
                   ("Dépenser beaucoup avant de tester", "Dépenser beaucoup")],
        "example": "L'imprimante plus rapide : une grosse dépense, sur un problème que personne n'avait "
                   "vérifié.",
        "example_cue": "L'imprimante plus rapide",
        "script": "Pourquoi s'en donner la peine ? Parce que cela évite des erreurs coûteuses. Automatiser "
                  "un processus défaillant que vous ne comprenez pas vraiment. Ne corriger que le symptôme "
                  "visible. Imposer une solution que les gens ne peuvent pas suivre pendant une équipe "
                  "chargée. Et dépenser beaucoup, avant de tester une seule hypothèse. L'imprimante plus "
                  "rapide en était l'exemple parfait. Une grosse dépense, sur un problème que personne "
                  "n'avait vérifié. Alors, quelles étapes allez-vous suivre ?",
    },
    {
        "key": "p05", "num": 5, "title": "Cinq étapes, une boucle",
        "points": [("Empathie · Définir · Imaginer", "L'empathie demande"),
                   ("Prototyper · Tester", "Le prototype demande"),
                   ("Désirable, faisable, viable", "Une bonne réponse est"),
                   ("Avancez avec des preuves, pas des réunions", "Passez à l'étape suivante")],
        "example": "La porte de Pooja : pas d'idées avant des observations réelles et une référence.",
        "example_cue": "Pooja a fixé une porte",
        "script": "Il y a cinq étapes, et vous pouvez revenir en arrière. L'empathie demande ce que vivent "
                  "les utilisateurs. La définition demande quel problème compte le plus. L'idéation demande "
                  "ce qui pourrait le résoudre. Le prototype demande comment cela pourrait marcher. Le test "
                  "demande si cela crée de la valeur. Une bonne réponse est désirable, faisable et viable. "
                  "Passez à l'étape suivante avec des preuves, pas parce qu'une réunion est finie. Pooja a "
                  "fixé une porte. Pas d'idées sans observations. Prêt à observer ?",
    },
    {
        "key": "p06", "num": 6, "title": "L'empathie au Gemba",
        "points": [("Observer sur plusieurs équipes", "Observez plusieurs cycles"),
                   ("Interroger après avoir observé", "Puis posez des questions ouvertes"),
                   ("Suivre un poste de bout en bout", "Suivez une personne"),
                   ("Carte d'empathie : dit, pense, fait, ressent", "Une carte d'empathie")],
        "example": "Pooja a observé dix cycles par équipe, puis a parlé avec cinq emballeurs.",
        "example_cue": "Pooja a observé",
        "script": "L'empathie commence au Gemba. Observez plusieurs cycles, en équipes normales et "
                  "chargées. Puis posez des questions ouvertes, après avoir vu le travail. Suivez une "
                  "personne pendant tout le travail, pour voir les passages de relais. Une carte d'empathie "
                  "vous aide à tout trier. Que disent-ils, pensent-ils, font-ils et ressentent-ils ? Pooja "
                  "a observé dix cycles par équipe. Puis elle a parlé avec cinq emballeurs. Que croyez-vous "
                  "qu'elle ait vu ?",
    },
    {
        "key": "p07", "num": 7, "title": "Ce que Pooja a vu",
        "points": [("Marcher pour chercher les étiquettes", "emballeurs marchaient"),
                   ("Deux étiquettes semblables côte à côte", "Deux étiquettes qui se ressemblaient"),
                   ("Attendre l'imprimante", "l'imprimante faisait parfois")],
        "example": "« Je ne suis pas lent. Je cherche. » Un emballeur, de l'équipe de nuit.",
        "example_cue": "Un emballeur l'a dit",
        "script": "Pas des emballeurs lents. Les emballeurs marchaient jusqu'à un rack partagé pour chaque "
                  "étiquette. Deux étiquettes qui se ressemblaient presque étaient côte à côte. Et "
                  "l'imprimante faisait parfois des pauses, alors ils attendaient. Un emballeur l'a dit "
                  "parfaitement. Je ne suis pas lent. Je cherche. Vous remarquez ce qui manque ? Personne "
                  "n'a accusé personne. Ce sont des faits sur le travail, pas sur les personnes. Comment en "
                  "feriez-vous un problème qui vaut d'être résolu ?",
    },
    {
        "key": "p08", "num": 8, "title": "Définir le besoin",
        "points": [("Utilisateur · besoin · constat", "utilisateur, un besoin"),
                   ("Pas de solution dans l'énoncé", "Il ne nomme pas"),
                   ("Une référence mesurable", "Ajoutez une référence")],
        "example": "Les emballeurs ont besoin de la bonne étiquette à portée de main, car les étiquettes "
                   "semblables et la marche causent des erreurs. Aujourd'hui : 52 s contre un TAKT de 45 s, "
                   "12 erreurs pour 1 000.",
        "example_cue": "Pooja a écrit",
        "script": "Définissez maintenant le besoin. Un bon énoncé nomme un utilisateur, un besoin et un "
                  "constat. Il ne nomme pas la solution. Pooja a écrit une phrase. Les emballeurs ont "
                  "besoin de la bonne étiquette juste à portée de main, car les étiquettes semblables et la "
                  "marche causent des erreurs. Ajoutez une référence. Le poste prenait cinquante-deux "
                  "secondes, contre un TAKT de quarante-cinq. Et douze pompes sur mille avaient une erreur "
                  "d'étiquette. Voyez-vous l'imprimante quelque part dans cet énoncé ?",
    },
    {
        "key": "p09", "num": 9, "title": "Imaginer : ouvrir large d'abord",
        "points": [("Écrire les idées avant d'en discuter", "Écrire les idées en silence"),
                   ("Demander « Comment pourrions-nous… ? »", "Comment pourrions-nous"),
                   ("SCAMPER et le prisme des gaspillages", "Essayez SCAMPER")],
        "example": "L'équipe de Pooja : 23 idées en 30 minutes, venant des emballeurs, de la qualité et du "
                   "magasin.",
        "example_cue": "L'équipe de Pooja",
        "script": "Ouvrez maintenant large, avant de choisir. Écrire les idées en silence veut dire que "
                  "chacun écrit ses idées seul, avant que le groupe en parle. Ainsi, ce n'est pas la voix "
                  "la plus forte qui gagne. Posez des questions comment pourrions-nous, pour transformer "
                  "les limites en occasions. Essayez SCAMPER, ou passez en revue les huit gaspillages. "
                  "L'équipe de Pooja a écrit vingt-trois idées en trente minutes. Les emballeurs, la "
                  "qualité et le magasin ont tous participé. Comment n'en choisir qu'une ?",
    },
    {
        "key": "p10", "num": 10, "title": "Choisir avec une grille de notation",
        "points": [("Pondérez chaque critère", "Pondérez chaque critère"),
                   ("Notez chaque concept, additionnez les notes", "Notez chaque concept"),
                   ("La sécurité et la qualité sont des filtres", "la sécurité et la qualité")],
        "example": "Emplacements d'étiquettes + contrôle par scan : 4,15. Nouvelle imprimante au poste : "
                   "4,10.",
        "example_cue": "Les deux premières",
        "script": "Utilisez une grille de notation simple. Pondérez chaque critère, comme la qualité, "
                  "l'adhésion des utilisateurs, l'impact, la faisabilité et le coût. Notez chaque concept, "
                  "de un à cinq. Multipliez et additionnez. Mais la sécurité et la qualité ne sont pas que "
                  "des notes. Ce sont des filtres. Si une idée en échoue un, elle est éliminée. Les deux "
                  "premières étaient proches. Des emplacements d'étiquettes par modèle avec contrôle par "
                  "scan, et une nouvelle imprimante au poste. Les emplacements l'ont emporté, de justesse. "
                  "Que testeriez-vous en premier ?",
    },
    {
        "key": "p11", "num": 11, "title": "Prototyper petit et pas cher",
        "points": [("Papier, carton ou ruban d'abord", "Commencez par du papier"),
                   ("Un poste avant la ligne", "Essayez un poste"),
                   ("Des heures, pas des mois", "se mesure en heures")],
        "example": "Des emplacements d'étiquettes en carton, un par modèle, scotchés à côté de l'emballeur.",
        "example_cue": "Le premier prototype de Pooja",
        "script": "Rendez l'idée réelle, au plus bas coût possible. Commencez par du papier, du carton ou "
                  "du ruban au sol. Essayez un poste avant toute la ligne. Un bon prototype se mesure en "
                  "heures, pas en mois. Le premier prototype de Pooja était en carton. Un emplacement "
                  "d'étiquette par modèle, scotché juste à côté de l'emballeur, avec le scanner à portée de "
                  "main. Il n'a presque rien coûté. Mais comment saurait-elle s'il marchait ?",
    },
    {
        "key": "p12", "num": 12, "title": "Planifier le test",
        "points": [("Une hypothèse claire", "Écrivez une hypothèse"),
                   ("Périmètre, mesures et comparaison", "Fixez le périmètre"),
                   ("Une règle de décision convenue à l'avance", "Convenez d'une règle de décision")],
        "example": "Hypothèse : les emplacements + le contrôle par scan ramènent le temps de cycle sous le "
                   "TAKT et réduisent les erreurs d'étiquette d'au moins 75 %.",
        "example_cue": "L'hypothèse de Pooja",
        "script": "Planifiez le test avant de le commencer. Écrivez une hypothèse. Si nous changeons ceci, "
                  "nous attendons cela. Fixez le périmètre, les mesures, et la base de comparaison. "
                  "Convenez d'une règle de décision à l'avance. Adopter, adapter ou arrêter. L'hypothèse de "
                  "Pooja était claire. Les emplacements et un contrôle par scan ramèneraient le temps de "
                  "cycle sous le TAKT. Et les erreurs d'étiquette baisseraient d'au moins trois quarts. Que "
                  "s'est-il passé, à votre avis ?",
    },
    {
        "key": "p13", "num": 13, "title": "Les résultats",
        "points": [("Temps de cycle : de 52 s à 44 s", "Le temps de cycle est passé"),
                   ("Bonnes pompes par équipe : de 500 à 610", "Les bonnes pompes par équipe"),
                   ("Erreurs d'étiquette : de 12 à 2 pour 1 000", "Les erreurs d'étiquette sont passées"),
                   ("Marche : de 4 m à 1,2 m", "La marche a diminué")],
        "example": "18 emballeurs sur 20 ont utilisé la nouvelle méthode : 90 % d'adhésion.",
        "example_cue": "Dix-huit sur vingt",
        "script": "L'essai a marché, presque entièrement. Le temps de cycle est passé de cinquante-deux à "
                  "quarante-quatre secondes. C'est maintenant sous le TAKT. Les bonnes pompes par équipe "
                  "sont passées de cinq cents à six cent dix. Les erreurs d'étiquette sont passées de douze "
                  "à deux pour mille. La marche a diminué de plus de moitié. Et dix-huit sur vingt "
                  "emballeurs ont utilisé la nouvelle méthode. C'est quatre-vingt-dix pour cent. Alors, "
                  "Pooja doit-elle la généraliser dès demain ?",
    },
    {
        "key": "p14", "num": 14, "title": "Adapter avant de généraliser",
        "points": [("Pas 100 % d'adhésion ? Cherchez pourquoi", "Deux emballeurs"),
                   ("Simplifier l'étape difficile, retester", "a simplifié cette étape"),
                   ("Vérifier que d'autres facteurs n'en sont pas la cause", "Et vérifiez que")],
        "example": "Les deux emballeurs étaient gauchers. Les emplacements étaient à droite. Inversez la "
                   "disposition.",
        "example_cue": "Il s'est avéré",
        "script": "Pas encore. Deux emballeurs n'ont pas suivi la méthode. Alors elle leur a demandé "
                  "pourquoi. Il s'est avéré qu'ils travaillaient de la main gauche, et que les emplacements "
                  "étaient à droite. Elle a simplifié cette étape, avec une disposition en miroir, et a "
                  "retesté. Et vérifiez que d'autres facteurs n'ont pas causé le gain, comme un mix de "
                  "modèles plus facile ou du personnel en plus. Alors seulement vous standardisez. Comment "
                  "mesureriez-vous le succès ?",
    },
    {
        "key": "p15", "num": 15, "title": "Mesurer, standardiser, démarrer",
        "points": [("Résultat, processus, adhésion, équilibre", "Mesurez le résultat"),
                   ("Standardiser, former, revoir à 30/60/90", "Puis standardisez"),
                   ("Commencer demain : 10 cycles, 3 personnes", "Commencez demain")],
        "example": "La revue de Pooja à 90 jours : erreurs maintenues à 2 pour 1 000, adhésion à 100 %.",
        "example_cue": "À quatre-vingt-dix jours",
        "script": "Mesurez le résultat, le processus, l'adhésion et l'équilibre. Autre chose s'est-il "
                  "dégradé, comme la sécurité ou le coût ? Puis standardisez, formez chaque équipe, et "
                  "faites une revue à trente, soixante et quatre-vingt-dix jours. À quatre-vingt-dix jours, "
                  "les erreurs de Pooja tenaient à deux pour mille, et chaque emballeur utilisait la "
                  "méthode. Commencez demain. Observez dix cycles d'un travail pénible, parlez à trois "
                  "personnes, et écrivez un besoin.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "steps", "items": [
        {"label": "Empathie", "with": 1}, {"label": "Définir", "with": 1},
        {"label": "Imaginer", "with": 1}, {"label": "Prototyper", "with": 2},
        {"label": "Tester", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Les outils Lean restent", "icon": "wrench", "with": 0},
        {"label": "D'abord le bon problème", "icon": "search", "with": 1},
        {"label": "Porté par les utilisateurs", "icon": "hand", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Méthode imposée", "sub": "Disparue en deux semaines", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Méthode co-conçue", "sub": "Les gens la gardent", "icon": "check", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Observer", "icon": "search", "with": 0},
        {"label": "D'abord les faits", "icon": "clipboard", "with": 1},
        {"label": "Petits essais", "icon": "shape", "with": 2},
        {"label": "Adhésion", "icon": "person", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Automatiser le désordre", "icon": "gear", "tone": "bad", "with": 0},
        {"label": "Seulement le symptôme", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Impossible à suivre", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Grosse dépense, sans test", "icon": "trash", "tone": "bad", "with": 3}]},
    "p05": {"type": "steps", "items": [
        {"label": "Empathie", "with": 0}, {"label": "Définir", "with": 0},
        {"label": "Imaginer", "with": 0}, {"label": "Prototyper", "with": 1},
        {"label": "Tester", "with": 1}],
        "then": {"type": "icons", "with": 2, "items": [
            {"label": "Désirable", "sub": "Les utilisateurs en ont besoin", "icon": "person", "with": 2},
            {"label": "Faisable", "sub": "Nous pouvons le faire", "icon": "wrench", "with": 2},
            {"label": "Viable", "sub": "Vaut son coût", "icon": "scale", "tone": "good", "with": 2}]}},
    "p06": {"type": "icons", "items": [
        {"label": "Observer", "icon": "search", "with": 0},
        {"label": "Interroger", "icon": "person", "with": 1},
        {"label": "Suivre", "icon": "walk", "with": 2},
        {"label": "Dit · pense · fait · ressent", "icon": "clipboard", "with": 3}]},
    "p07": {"type": "flow", "items": [
        {"label": "Marcher jusqu'au rack", "icon": "walk", "tone": "bad", "with": 0},
        {"label": "Étiquettes semblables", "icon": "label", "tone": "bad", "with": 1},
        {"label": "Attendre l'imprimante", "icon": "clock", "tone": "bad", "with": 2}]},
    "p08": {"type": "doc", "items": [
        {"label": "Utilisateur : les emballeurs", "icon": "person", "with": 0},
        {"label": "Besoin : la bonne étiquette à portée de main", "icon": "label", "with": "example"},
        {"label": "Constat : étiquettes semblables et marche", "icon": "search", "with": "example"},
        {"label": "Référence : 52 s contre 45 s, 12 pour 1 000", "icon": "chartUp", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Idées en silence", "icon": "clipboard", "with": 0},
        {"label": "Comment pourrions-nous… ?", "icon": "key", "with": 1},
        {"label": "SCAMPER, 8 gaspillages", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 23, "icon": "key", "label": "idées en 30 minutes",
                 "unit": "emballeurs, qualité et magasin", "with": "example"}},
    "p10": {"type": "versus", "items": [
        {"label": "Nouvelle imprimante", "sub": "Note 4,10 sur 5", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "Emplacements d'étiquettes + contrôle par scan", "sub": "Note 4,15 sur 5", "icon": "check", "tone": "good", "with": "example"}]},
    "p11": {"type": "ladder", "top": "LE MOINS CHER", "bottom": "LE PLUS GROS", "items": [
        {"label": "Papier, carton, ruban", "icon": "shape", "with": 0},
        {"label": "Pilote sur un poste", "icon": "pin", "with": 1},
        {"label": "Essai en ligne", "icon": "sequence", "with": 1}],
        "then": {"type": "stat", "value": 1, "suffix": " emplacement par modèle", "icon": "label", "label": "en carton, scotché près de l'emballeur",
                 "unit": "scanner à portée de main", "with": "example"}},
    "p12": {"type": "flow", "items": [
        {"label": "Hypothèse", "icon": "key", "with": 0},
        {"label": "Périmètre et mesures", "icon": "clipboard", "with": 1},
        {"label": "Adopter · adapter · arrêter", "icon": "scale", "tone": "good", "with": 2}]},
    "p13": {"type": "compare", "before": {"label": "Avant", "value": 12}, "after": {"label": "Essai", "value": 2},
            "unit": "erreurs d'étiquette pour 1 000 pompes", "note": "Cycle 52 s → 44 s · 500 → 610 bonnes pompes", "with": 2,
            "then": {"type": "stat", "value": 90, "suffix": "%", "icon": "person", "label": "adhésion",
                     "unit": "18 emballeurs sur 20", "with": "example"}},
    "p14": {"type": "flow", "items": [
        {"label": "Demandez pourquoi", "icon": "person", "with": 0},
        {"label": "Disposition en miroir", "icon": "shape", "with": 1},
        {"label": "Vérifiez le mix de modèles", "icon": "search", "with": 2},
        {"label": "Puis standardisez", "icon": "check", "tone": "good", "with": 2}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Standardiser, former", "sub": "Jour 0", "icon": "clipboard", "with": 1},
        {"label": "Revue", "sub": "30 · 60", "icon": "search", "with": 1},
        {"label": "Erreurs maintenues à 2", "sub": "90 jours", "icon": "check", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Quel est le meilleur énoncé de défi en Design Thinking ?",
        "options": ["Il nous faut une imprimante d'étiquettes plus rapide à l'emballage",
                    "Les emballeurs ont besoin de la bonne étiquette à portée de main, car les étiquettes "
                    "semblables et la marche causent des erreurs",
                    "Les emballeurs doivent faire plus attention aux étiquettes"],
        "correct": 1,
        "explanation": "Il nomme l'utilisateur, le besoin et le constat, sans choisir de solution ni accuser "
                       "personne. Les autres sont une solution et un reproche.",
        "q_script": "Vérification rapide. Lequel de ces énoncés est le meilleur énoncé de défi ? Prenez "
                    "quelques secondes.",
        "a_script": "C'est le deuxième. Il nomme l'utilisateur, le besoin et le constat. Le premier est déjà "
                    "une solution, et le dernier n'est qu'un reproche.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un pilote réduit le temps de cycle, mais seuls 6 opérateurs sur 10 utilisent la nouvelle "
                    "méthode. Et ensuite ?",
        "options": ["Le généraliser : les chiffres se sont améliorés",
                    "Demander aux quatre autres pourquoi, simplifier, et retester",
                    "Le rendre obligatoire et auditer chaque jour"],
        "correct": 1,
        "explanation": "Une faible adhésion est aussi une preuve. Trouvez ce qui rend la méthode difficile pour "
                       "ces utilisateurs, améliorez-la, et retestez avant de standardiser.",
        "q_script": "Encore une, et cette fois c'est un scénario. Un pilote réduit le temps de cycle. Mais "
                    "seuls six opérateurs sur dix utilisent la nouvelle méthode. Que doit faire l'équipe ? "
                    "Réfléchissez.",
        "a_script": "Demandez aux quatre autres pourquoi, simplifiez la partie difficile, et retestez. Une "
                    "faible adhésion est aussi une preuve, alors traitez-la comme n'importe quel autre "
                    "résultat.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
