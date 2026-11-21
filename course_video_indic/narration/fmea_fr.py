"""fmea in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh fmea_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "fm_fr"
NAME = "fmea_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Gemba": "Guemba",
    "FMEA": "effe emme eu a",
    "RPN": "erre pé enne",
    "SOP": "esse o pé",
    "5G": "cinq gé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Six unités radio extérieures sont revenues du terrain, pleines d'eau. Sur deux, le joint "
    "manquait. Sur quatre, il était tordu. Toutes avaient passé l'inspection finale. Ça vous "
    "dit quelque chose ? Dans cette leçon, vous allez découvrir le FMEA, l'analyse des modes "
    "de défaillance et de leurs effets. Vous verrez comment trouver les risques avant qu'ils "
    "n'atteignent un client, et traiter les plus gros en premier. Nous suivrons Asha, "
    "ingénieure qualité dans une usine de télécommunications."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Construisez une chaîne claire, de l'effet au mode de "
    "défaillance puis à une cause que vous pouvez maîtriser. Notez avec des preuves, et ne "
    "laissez jamais le chiffre remplacer le jugement. Et préférez la prévention, puis prouvez "
    "qu'elle marche avant de renoter. Voici votre action pour cette semaine. Choisissez une "
    "étape critique, et écrivez sa chaîne de défaillance avec votre équipe. Bravo d'avoir "
    "terminé cette leçon. Ensuite, vous découvrirez le Gemba, le lieu réel."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le FMEA",
        "points": [("Comment cela pourrait-il échouer, et pourquoi ?", "Il demande comment"),
                   ("Quel serait l'effet ?", "quel serait l'effet"),
                   ("Agir avant que cela atteigne le client", "Puis vous agissez")],
        "example": "La cible d'Asha : le joint du boîtier d'une petite cellule 5G extérieure.",
        "example_cue": "La cible d'Asha",
        "script": "Le FMEA est une méthode d'équipe pour réfléchir avant que la défaillance n'arrive. Il "
                  "demande comment un produit ou un processus pourrait échouer, et pourquoi. Il demande "
                  "quel serait l'effet, et quels contrôles vous avez aujourd'hui. Puis vous agissez, avant "
                  "que la défaillance n'atteigne votre client. C'est la qualité intégrée, pas l'inspection. "
                  "La cible d'Asha était le joint du boîtier d'une petite cellule 5G extérieure. Alors, de "
                  "quels mots avez-vous besoin ?",
    },
    {
        "key": "p02", "num": 2, "title": "Les mots clés",
        "points": [("Mode de défaillance : comment ça échoue", "Un mode de défaillance"),
                   ("Effet : ce que subit le client", "L'effet"),
                   ("Cause : pourquoi cela pourrait arriver", "La cause"),
                   ("Contrôle et action", "Un contrôle")],
        "example": "Mode : joint tordu. Effet : eau à l'intérieur. Cause : pas de contrôle de mise en place.",
        "example_cue": "Pour Asha",
        "script": "Retenez cinq mots. Un mode de défaillance, c'est la façon dont l'exigence échoue. "
                  "L'effet, c'est ce qui arrive au processus suivant, ou au client. La cause, c'est "
                  "pourquoi cela pourrait arriver. Un contrôle empêche la cause, ou détecte la défaillance. "
                  "Et une action réduit le risque. Pour Asha, le mode était un joint tordu. L'effet était "
                  "de l'eau à l'intérieur. Devinez-vous la cause ?",
    },
    {
        "key": "p03", "num": 3, "title": "Types de FMEA",
        "points": [("FMEA système et conception", "Les analyses système et conception"),
                   ("FMEA processus : les étapes de fabrication", "Un FMEA processus"),
                   ("Des limites claires de début et de fin", "Fixez des limites claires")],
        "example": "Le périmètre d'Asha : de la prise du joint au boîtier scellé et testé.",
        "example_cue": "Le périmètre d'Asha",
        "script": "Il en existe plusieurs types. Les analyses système et conception, le FMEA système et le "
                  "FMEA conception, regardent le produit et la façon dont ses pièces fonctionnent ensemble. "
                  "L'analyse machine regarde l'équipement. Un FMEA processus regarde vos étapes de "
                  "fabrication, et c'est celui qu'utilisent la plupart des équipes Lean. Fixez des limites "
                  "claires, pour que le travail reste gérable. Le périmètre d'Asha allait de la prise du "
                  "joint, au boîtier scellé et testé. Quand faut-il en construire un ?",
    },
    {
        "key": "p04", "num": 4, "title": "Quand commencer ou mettre à jour",
        "points": [("Nouveau produit ou nouveau processus", "un nouveau produit"),
                   ("Tout changement : matière, outil, implantation", "tout changement"),
                   ("Après une réclamation ou une fuite", "après une réclamation")],
        "example": "Asha a mis le sien à jour le jour où les six radios mouillées sont revenues.",
        "example_cue": "Asha a mis le sien à jour",
        "script": "Commencez-en un pour un nouveau produit ou un nouveau processus. Mettez-le à jour après "
                  "tout changement. Cela inclut la matière, l'équipement, le logiciel, l'outillage, "
                  "l'implantation ou la méthode. Et mettez-le à jour après une réclamation, ou dès que vous "
                  "apprenez qu'un contrôle ne fonctionne pas. Un FMEA vieux de deux ans décrit une usine "
                  "qui n'existe plus. Asha a mis le sien à jour le jour où les radios mouillées sont "
                  "revenues. Qui le construit ?",
    },
    {
        "key": "p05", "num": 5, "title": "L'équipe et les données d'entrée",
        "points": [("Une équipe transverse", "Faites venir la production"),
                   ("Des opérateurs expérimentés", "Incluez des opérateurs expérimentés"),
                   ("Diagramme de flux, données, instructions de travail", "Apportez aussi les données"),
                   ("Allez au Gemba avant de noter", "allez au Gemba")],
        "example": "Au Gemba, Asha a vu deux tailles de joint partager un même bac.",
        "example_cue": "Au Gemba",
        "script": "Faites venir la production, l'ingénierie, la qualité, la maintenance et le test. Incluez "
                  "des opérateurs expérimentés qui connaissent le travail réel. Apportez aussi les données. "
                  "Un flux du processus, des données de défauts, les instructions de travail et les retours "
                  "d'expérience. Puis allez au Gemba avant de noter quoi que ce soit. Comparez la méthode "
                  "écrite avec ce qui se passe vraiment. Au Gemba, Asha a vu deux tailles de joint partager "
                  "un même bac. Que noteriez-vous ?",
    },
    {
        "key": "p06", "num": 6, "title": "Les sept étapes",
        "points": [("Planifier, structure, fonction", "Planifiez le périmètre"),
                   ("Analyse des défaillances", "analysez les défaillances"),
                   ("Analyse des risques", "notez le risque"),
                   ("Optimiser et documenter", "passez à l'action")],
        "example": "L'équipe d'Asha : une exigence et une chaîne de défaillance à la fois.",
        "example_cue": "L'équipe d'Asha",
        "script": "La méthode a sept étapes. Planifiez le périmètre, cartographiez la structure, et écrivez "
                  "ce que chaque étape doit accomplir. Puis analysez les défaillances, et notez le risque. "
                  "Enfin, passez à l'action, et documentez ce qui a changé. Une règle simple garde les "
                  "réunions raisonnables. L'équipe d'Asha a travaillé une exigence et une chaîne de "
                  "défaillance à la fois. Alors, à quoi ressemble une bonne exigence ?",
    },
    {
        "key": "p07", "num": 7, "title": "Écrire des fonctions claires",
        "points": [("Un verbe d'action plus une exigence", "un verbe, plus"),
                   ("Mesurable, pas vague", "mesurable")],
        "example": "Faible : « Mettre le joint. » Fort : « Placer le bon joint entièrement dans la gorge, "
                   "sans torsion ni dommage. »",
        "example_cue": "Comparez ces deux formulations",
        "script": "Écrivez chaque fonction comme un verbe, plus une exigence que vous pouvez vérifier. "
                  "Rendez-la mesurable, pas vague. Assembler correctement ne dit rien à personne. Comparez "
                  "ces deux formulations. Mettre le joint. Ou, placer le bon joint entièrement dans la "
                  "gorge, sans torsion ni dommage. La deuxième vous dit exactement comment elle peut "
                  "échouer. Manquant, mauvaise taille, mal en place, ou tordu. Pouvez-vous réécrire ainsi "
                  "une de vos propres étapes ?",
    },
    {
        "key": "p08", "num": 8, "title": "La chaîne de défaillance",
        "points": [("Effet : entrée d'eau, panne sur le terrain", "L'effet est"),
                   ("Mode : joint manquant ou tordu", "Le mode de défaillance est"),
                   ("Cause : quelque chose que vous pouvez maîtriser", "La cause doit")],
        "example": "Cause : deux tailles de joint dans un bac, et aucun contrôle de mise en place.",
        "example_cue": "Les causes d'Asha étaient",
        "script": "Reliez maintenant la chaîne. L'effet est une entrée d'eau, et une radio en panne sur un "
                  "poteau. Le mode de défaillance est un joint manquant, ou tordu. La cause doit être "
                  "quelque chose que vous pouvez vraiment maîtriser. N'écrivez jamais négligence ou erreur "
                  "humaine. Les causes d'Asha étaient précises. Deux tailles de joint partageaient un bac. "
                  "Et rien ne vérifiait que le joint était bien en place. Vous pouvez maintenant concevoir "
                  "une solution. Mais quel risque passe en premier ?",
    },
    {
        "key": "p09", "num": 9, "title": "Gravité, occurrence, détection",
        "points": [("Gravité : à quel point l'effet est grave", "La gravité note"),
                   ("Occurrence : à quelle fréquence la cause arrive", "L'occurrence note"),
                   ("Détection : probabilité de l'attraper", "La détection note"),
                   ("Chaque note a besoin d'une preuve", "Appuyez chaque note")],
        "example": "Risque du joint : gravité 8, occurrence 5, détection 6.",
        "example_cue": "L'équipe d'Asha a noté",
        "script": "Vous notez trois choses, en général de un à dix. La gravité note à quel point l'effet "
                  "est grave. L'occurrence note à quelle fréquence la cause arrive, avec la prévention "
                  "d'aujourd'hui. La détection note la probabilité de l'attraper avant qu'il ne s'échappe. "
                  "Ici, dix veut dire que vous ne l'attraperez probablement pas. Appuyez chaque note sur "
                  "des données, pas sur des impressions. L'équipe d'Asha a noté le joint huit, cinq et six. "
                  "Qu'est-ce que cela donne ?",
    },
    {
        "key": "p10", "num": 10, "title": "Indice de priorité du risque",
        "points": [("RPN = gravité × occurrence × détection", "L'indice de priorité du risque"),
                   ("8 × 5 × 6 = 240", "Cela fait deux cent"),
                   ("Un guide, pas un verdict", "Mais traitez-le")],
        "example": "RPN du joint : 240, le plus élevé de la feuille d'Asha.",
        "example_cue": "C'était le chiffre le plus élevé",
        "script": "L'indice de priorité du risque multiplie les trois notes. Pour le joint, huit fois cinq "
                  "fois six. Cela fait deux cent quarante. C'était le chiffre le plus élevé de la feuille "
                  "d'Asha. Mais traitez-le comme un guide, pas comme un verdict. Des notes différentes "
                  "peuvent donner le même RPN. Et les équipes peuvent être tentées d'ajuster les notes pour "
                  "passer sous une limite. Alors, que faut-il regarder aussi ?",
    },
    {
        "key": "p11", "num": 11, "title": "La gravité d'abord",
        "points": [("Une gravité élevée demande une action de toute façon", "une gravité élevée"),
                   ("Priorité d'action haute, moyenne, basse", "Beaucoup d'équipes utilisent maintenant"),
                   ("Demandez : la prévention ou la détection est-elle faible ?", "Et demandez toujours")],
        "example": "Un risque sécurité avec un RPN de 90 peut compter plus qu'un risque esthétique à 200.",
        "example_cue": "Un risque sécurité",
        "script": "Regardez d'abord la gravité. Une gravité élevée demande une action, même quand son RPN "
                  "semble modéré. Beaucoup d'équipes utilisent maintenant la priorité d'action, notée "
                  "haute, moyenne ou basse. Haute veut dire agir, ou expliquer formellement pourquoi vous "
                  "ne pouvez pas. Et demandez toujours quel contrôle est faible, la prévention ou la "
                  "détection. Un risque sécurité noté quatre-vingt-dix peut compter plus qu'un risque "
                  "esthétique noté deux cents. Êtes-vous d'accord ?",
    },
    {
        "key": "p12", "num": 12, "title": "Prévention ou détection",
        "points": [("Prévention : empêcher la cause d'arriver", "Les contrôles de prévention"),
                   ("Détection : l'attraper avant la libération", "Les contrôles de détection"),
                   ("L'automatique bat le jugement humain", "l'automatique bat")],
        "example": "Le seul contrôle d'Asha : une inspection visuelle finale. De la détection, et faible.",
        "example_cue": "Le seul contrôle d'Asha",
        "script": "Sachez quel type de contrôle vous avez. Les contrôles de prévention empêchent la cause "
                  "d'arriver, comme une pièce détrompée ou un verrouillage de recette. Les contrôles de "
                  "détection attrapent la défaillance avant la libération, comme un capteur ou un test. "
                  "Demandez si chacun vérifie chaque unité, et s'il peut être contourné. Et l'automatique "
                  "bat le jugement humain, presque à chaque fois. Le seul contrôle d'Asha était une "
                  "inspection visuelle finale. De la détection, et faible. Qu'ajouteriez-vous ?",
    },
    {
        "key": "p13", "num": 13, "title": "Choisir des actions fortes",
        "points": [("Éliminer la cause", "D'abord, éliminez"),
                   ("L'empêcher : verrou, détrompeur, interverrouillage", "Ensuite, empêchez-la"),
                   ("Améliorer la détection", "Puis améliorez la détection"),
                   ("Formation et check-lists en dernier", "La formation et les check-lists")],
        "example": "Les actions d'Asha : un joint par plateau détrompé, un gabarit de gorge, un capteur de "
                   "présence et un test d'étanchéité.",
        "example_cue": "Asha a choisi",
        "script": "Certaines actions sont plus fortes que d'autres. D'abord, éliminez la cause par la "
                  "conception, si vous le pouvez. Ensuite, empêchez-la, avec un verrou, un détrompeur ou un "
                  "interverrouillage. Puis réduisez la variation. Puis améliorez la détection avec un "
                  "contrôle automatique. La formation et les check-lists viennent en dernier, quand rien de "
                  "plus fort n'est possible. Asha a choisi un plateau détrompé avec une seule taille de "
                  "joint, un gabarit de gorge, un capteur de présence, et un test d'étanchéité. Est-ce que "
                  "ça a marché ?",
    },
    {
        "key": "p14", "num": 14, "title": "Vérifier, puis renoter",
        "points": [("Le prouver en conditions réelles", "Prouvez d'abord qu'il fonctionne"),
                   ("La gravité reste à 8 : même effet", "La gravité est restée"),
                   ("Occurrence 5 → 2, détection 6 → 2", "L'occurrence est tombée"),
                   ("RPN 240 → 32", "Le RPN est tombé")],
        "example": "La preuve d'abord : le capteur a attrapé chaque mauvais échantillon lors d'un essai de "
                   "500 unités.",
        "example_cue": "La preuve d'Asha",
        "script": "Ne renotez jamais simplement parce que vous avez acheté un capteur. Prouvez d'abord "
                  "qu'il fonctionne en conditions réelles. La preuve d'Asha est venue d'un essai de cinq "
                  "cents unités. Le capteur a attrapé chaque mauvais échantillon. La gravité est restée à "
                  "huit, car de l'eau à l'intérieur reste tout aussi grave. L'occurrence est tombée à deux, "
                  "et la détection est tombée à deux. Le RPN est tombé de deux cent quarante à trente-deux. "
                  "Le travail est-il terminé ?",
    },
    {
        "key": "p15", "num": 15, "title": "Le garder vivant",
        "points": [("Mettre à jour le plan de contrôle, le SOP, la formation", "Mettez à jour le plan de contrôle, le SOP"),
                   ("Revoir les risques élevés chaque semaine", "Revoyez les risques élevés ouverts"),
                   ("Dupliquer les leçons sur des produits similaires", "Dupliquez ce que vous avez appris")],
        "example": "L'équipe d'Asha a dupliqué le plateau détrompé sur deux autres unités extérieures.",
        "example_cue": "L'équipe d'Asha a dupliqué",
        "script": "Pas tout à fait. Un FMEA est un document vivant, pas un formulaire à classer. Mettez à "
                  "jour le plan de contrôle, le SOP, la formation et les audits. Revoyez les risques élevés "
                  "ouverts chaque semaine, et toute la feuille après chaque réclamation. Dupliquez ce que "
                  "vous avez appris sur des produits similaires. L'équipe d'Asha a dupliqué le plateau "
                  "détrompé sur deux autres unités extérieures. Et aucune radio mouillée n'est revenue "
                  "depuis. Où commencerez-vous le vôtre ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Comment cela pourrait-il échouer ?", "icon": "search", "with": 0},
        {"label": "Quel est l'effet ?", "icon": "warning", "with": 1},
        {"label": "Agir d'abord", "icon": "shield", "tone": "good", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Mode de défaillance", "sub": "Comment ça échoue", "icon": "cross", "with": 0},
        {"label": "Effet", "sub": "Ce que ça provoque", "icon": "warning", "with": 1},
        {"label": "Cause", "sub": "Pourquoi ça arrive", "icon": "search", "with": 2},
        {"label": "Contrôle, action", "sub": "Ce qui l'arrête", "icon": "shield", "tone": "good", "with": 3}]},
    "p03": {"type": "icons", "items": [
        {"label": "Système", "icon": "stack", "with": 0},
        {"label": "Conception", "icon": "shape", "with": 0},
        {"label": "Processus", "icon": "sequence", "tone": "good", "with": 1},
        {"label": "Limites", "icon": "pin", "with": 2}]},
    "p04": {"type": "icons", "items": [
        {"label": "Nouveau produit ou processus", "icon": "box", "with": 0},
        {"label": "Tout changement", "icon": "gear", "with": 1},
        {"label": "Réclamation ou fuite", "icon": "warning", "tone": "bad", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Transverse", "icon": "person", "with": 0},
        {"label": "Opérateurs", "icon": "hand", "with": 1},
        {"label": "Données et flux", "icon": "clipboard", "with": 2},
        {"label": "Le Gemba d'abord", "icon": "walk", "tone": "good", "with": 3}]},
    "p06": {"type": "steps", "items": [
        {"label": "Planifier", "with": 0}, {"label": "Structure", "with": 0},
        {"label": "Fonction", "with": 0}, {"label": "Défaillance", "with": 1},
        {"label": "Risque", "with": 2}, {"label": "Optimiser", "with": 3},
        {"label": "Documenter", "with": 3}]},
    "p07": {"type": "versus", "items": [
        {"label": "« Mettre le joint »", "sub": "Vague", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "« Bon joint, bien en place, sans torsion »", "sub": "Mesurable", "icon": "check", "tone": "good", "with": "example"}]},
    "p08": {"type": "flow", "items": [
        {"label": "Effet", "sub": "Entrée d'eau", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Mode de défaillance", "sub": "Manquant ou tordu", "icon": "cross", "tone": "bad", "with": 1},
        {"label": "Cause", "sub": "Bac mélangé, pas de contrôle de mise en place", "icon": "search", "with": "example"}]},
    "p09": {"type": "bars", "label": "", "note": "Gravité · Occurrence · Détection, de 1 à 10", "with": "example", "items": [
        {"label": "Grav.", "value": 8, "tone": "bad", "with": "example"},
        {"label": "Occ.", "value": 5, "with": "example"},
        {"label": "Dét.", "value": 6, "with": "example"}]},
    "p10": {"type": "stat", "value": 240, "icon": "warning", "label": "RPN du joint",
            "unit": "8 × 5 × 6", "with": 1},
    "p11": {"type": "ladder", "top": "HAUTE", "bottom": "BASSE", "items": [
        {"label": "Agir, ou justifier pourquoi pas", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Revoir et améliorer", "icon": "search", "with": 1},
        {"label": "Maintenir et surveiller", "icon": "check", "tone": "good", "with": 1}]},
    "p12": {"type": "versus", "items": [
        {"label": "Détection", "sub": "Inspection visuelle finale", "icon": "search", "with": 1},
        {"label": "Prévention", "sub": "Empêcher la cause", "icon": "key", "tone": "good", "with": 0}]},
    "p13": {"type": "ladder", "top": "LE PLUS FORT", "bottom": "LE PLUS FAIBLE", "items": [
        {"label": "Éliminer par la conception", "icon": "shape", "with": 0},
        {"label": "Empêcher : détrompeur, verrou", "icon": "key", "with": 1},
        {"label": "Détecter automatiquement", "icon": "sensor", "with": 2},
        {"label": "Former, check-list", "icon": "clipboard", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Avant", "value": 240}, "after": {"label": "Après", "value": 32},
            "unit": "RPN du joint", "note": "Occurrence 5 → 2 · Détection 6 → 2", "with": 3},
    "p15": {"type": "flow", "items": [
        {"label": "Plan de contrôle, SOP", "icon": "clipboard", "with": 0},
        {"label": "Revue hebdomadaire des risques", "icon": "calendar", "with": 1},
        {"label": "Dupliquer sur des unités similaires", "icon": "sequence", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Quelle est une cause utile pour un FMEA ?",
        "options": ["La négligence de l'opérateur",
                    "Deux tailles de joint partagent un bac au poste",
                    "De l'eau entre dans la radio"],
        "correct": 1,
        "explanation": "Une cause utile est une condition précise que vous pouvez maîtriser. La négligence est "
                       "un reproche, et l'eau à l'intérieur est l'effet.",
        "q_script": "Vérification rapide. Laquelle de ces propositions est une cause utile, pour un FMEA ? "
                    "Prenez quelques secondes.",
        "a_script": "C'est la deuxième. C'est une condition précise que vous pouvez maîtriser. La négligence "
                    "n'est qu'un reproche, et l'eau à l'intérieur est l'effet.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Après l'ajout d'un capteur et d'un test d'étanchéité, l'équipe veut baisser la gravité "
                    "de 8 à 4. Est-ce correct ?",
        "options": ["Oui : le risque est plus faible maintenant",
                    "Non : la gravité ne change que si l'effet change",
                    "Oui, si le RPN reste sous 100"],
        "correct": 1,
        "explanation": "La gravité note l'effet. De l'eau dans une radio est tout aussi grave qu'avant. Les "
                       "nouveaux contrôles baissent l'occurrence et la détection, pas la gravité.",
        "q_script": "Encore une, et cette fois c'est un scénario. Après l'ajout d'un capteur et d'un test "
                    "d'étanchéité, l'équipe veut baisser la gravité de huit à quatre. Est-ce correct ? "
                    "Réfléchissez.",
        "a_script": "Non. La gravité note l'effet, et de l'eau à l'intérieur est tout aussi grave qu'avant. "
                    "Les nouveaux contrôles baissent plutôt l'occurrence et la détection.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
