"""hancho in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh hancho_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "hc_fr"
NAME = "hancho_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Ishikawa": "Ichikawa",
    "Hancho": "Hanntcho",
    "Gemba": "Guemba",
    "TAKT": "takte",
    "SOP": "esse o pé",
    "LED": "led",
    "TV": "té vé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Le mois dernier, la ligne a produit vingt TV de moins par heure, pendant toute une "
    "équipe. Personne ne l'a remarqué avant le rapport du lendemain matin. À ce moment-là, la "
    "perte appartenait au passé. Ça vous dit quelque chose ? Dans cette leçon, vous allez "
    "découvrir le Hancho, le leadership directement sur le terrain. Vous verrez comment un "
    "chef d'équipe repère un écart dès la première heure, et le corrige avant la fin de "
    "l'équipe. Nous suivrons Sunita, nouvelle Hancho sur une ligne de TV LED."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Dirigez depuis le Gemba, en comparant le standard à ce "
    "qui se passe vraiment. Rendez chaque écart visible, chaque heure, et réagissez dans la "
    "même équipe. Et faites grandir vos équipes, pour que la ligne ne dépende pas de vous. "
    "Voici votre action pour cette semaine. Écrivez votre propre travail standard de "
    "responsable, pour une équipe. Bravo d'avoir terminé cette leçon. Ensuite, vous "
    "découvrirez le diagramme d'Ishikawa."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est un Hancho",
        "points": [("En japonais : chef d'équipe", "veut dire en japonais"),
                   ("Un système de leadership, pas un outil", "Ce n'est pas un outil"),
                   ("Dirige là où la valeur est créée", "qui dirige là même")],
        "example": "Sunita : douze opérateurs, une ligne de TV LED, les résultats de chaque équipe.",
        "example_cue": "Sunita dirige douze opérateurs sur une ligne d'écrans LED",
        "script": "Hancho veut dire en japonais chef d'équipe, ou responsable de premier niveau. Ce n'est "
                  "pas un outil que l'on remplit. C'est un système de leadership, construit autour d'une "
                  "personne qui dirige là même où la valeur est créée. Près des opérateurs, près du "
                  "processus, et près des problèmes. Sunita dirige douze opérateurs sur une ligne d'écrans "
                  "LED. Elle répond des résultats de chaque équipe, et de chaque TV. Alors, comment pense "
                  "un Hancho ?",
    },
    {
        "key": "p02", "num": 2, "title": "L'état d'esprit du Hancho",
        "points": [("Quel est le standard ? Quel est le réel ?", "Quel est le standard"),
                   ("Où est l'écart, et pourquoi ?", "Où est l'écart"),
                   ("Agir maintenant, puis empêcher que ça se répète", "Que faisons-nous tout de suite")],
        "example": "Sunita garde ces questions sur une carte dans sa poche.",
        "example_cue": "Sunita garde",
        "script": "Un Hancho pose les mêmes questions, à chaque fois. Quel est le standard ? Que se "
                  "passe-t-il vraiment ? Où est l'écart, et qu'est-ce qui l'a causé ? Que faisons-nous tout "
                  "de suite, et que faut-il changer pour que ça ne se répète jamais ? Remarquez qu'aucune "
                  "ne contient de reproche. Seulement le standard, le réel, l'écart et l'action. Sunita "
                  "garde ces questions sur une petite carte dans sa poche. Pourquoi une ligne a-t-elle "
                  "besoin de ce rôle ?",
    },
    {
        "key": "p03", "num": 3, "title": "Pourquoi les lignes ont besoin d'un Hancho",
        "points": [("Les petits écarts grandissent quand les responsables sont loin", "Quand les responsables sont loin"),
                   ("Réaction plus rapide, responsabilité claire", "Un Hancho veut dire"),
                   ("Kaizen quotidien, pas seulement des projets", "Et l'amélioration se fait")],
        "example": "Le mois dernier : un écart de 20 TV par heure, trouvé le lendemain matin.",
        "example_cue": "Souvenez-vous de l'écart",
        "script": "Quand les responsables sont loin du processus, les petits écarts grandissent. Un gabarit "
                  "desserré devient un arrêt. Quelques défauts deviennent une réclamation client. Un Hancho "
                  "veut dire une réaction plus rapide, et une responsabilité claire dans chaque équipe. Les "
                  "standards sont suivis, parce que quelqu'un vérifie. Et l'amélioration se fait chaque "
                  "jour, pas seulement dans des projets spéciaux. Souvenez-vous de l'écart du mois dernier, "
                  "trouvé le lendemain matin. De quoi un Hancho est-il exactement responsable ?",
    },
    {
        "key": "p04", "num": 4, "title": "Ce dont un Hancho est responsable",
        "points": [("Sécurité et qualité", "La sécurité d'abord"),
                   ("Livraison et coût", "La livraison veut dire"),
                   ("Les personnes et le processus", "Et les personnes")],
        "example": "La règle de Sunita : le résoudre, appeler le support, ou escalader. Savoir lequel.",
        "example_cue": "Sunita a appris",
        "script": "Un Hancho est responsable de six domaines. La sécurité d'abord, puis la qualité, en "
                  "protégeant le standard et en confinant les défauts. La livraison veut dire suivre le "
                  "plan face au réel, chaque heure. Le coût veut dire réduire le rebut, les retouches et "
                  "les arrêts. Et les personnes, et le processus, par la formation, le travail standard et "
                  "une ligne prête. Sunita a appris une chose de plus. Savoir quand le résoudre, quand "
                  "appeler le support, et quand escalader. Comment commence sa journée ?",
    },
    {
        "key": "p05", "num": 5, "title": "Avant le début de l'équipe",
        "points": [("Vérification de préparation avant l'équipe", "D'abord, la préparation"),
                   ("Un court briefing d'équipe", "Puis un court briefing"),
                   ("Contrôles de démarrage et de première pièce", "Puis les contrôles de démarrage")],
        "example": "Le briefing du jour : un changement de modèle vers la TV de 43 pouces à 10 heures.",
        "example_cue": "Le briefing du jour",
        "script": "La journée de Sunita commence avant celle de la ligne. D'abord, la préparation. Les "
                  "personnes, les matières, les machines, les outils et les documents sont-ils prêts ? Puis "
                  "un court briefing. La cible, les alertes qualité, les points de sécurité, et ce que "
                  "l'équipe précédente a appris. Puis les contrôles de démarrage, y compris la première "
                  "pièce. Le briefing du jour avait un point important. Un changement de modèle vers la TV "
                  "de quarante-trois pouces à dix heures. Que se passe-t-il une fois la ligne lancée ?",
    },
    {
        "key": "p06", "num": 6, "title": "Pendant et après l'équipe",
        "points": [("Plan face au réel chaque heure", "Chaque heure"),
                   ("Réagir à chaque anomalie", "Elle réagit"),
                   ("Accompagner au poste", "Elle accompagne"),
                   ("Une passation factuelle", "À la fin")],
        "example": "Note de passation : problèmes ouverts, WIP, état qualité, actions et responsables.",
        "example_cue": "Sa passation",
        "script": "Chaque heure, elle compare le plan au réel. Production, rendement au premier passage, "
                  "arrêts et en-cours. Elle réagit à chaque anomalie, et l'enregistre. Elle accompagne les "
                  "opérateurs au poste, pas en salle de réunion. À la fin, elle passe le relais à l'équipe "
                  "suivante avec des faits, pas des souvenirs. Sa passation couvre les problèmes ouverts, "
                  "l'état qualité, les actions et les responsables. Où passe-t-elle la plupart de son temps "
                  "?",
    },
    {
        "key": "p07", "num": 7, "title": "Diriger au Gemba",
        "points": [("Observer le processus et le produit réels", "Elle observe"),
                   ("Parler avec l'opérateur", "Elle parle"),
                   ("Poser des questions, pas seulement donner des réponses", "Elle pose des questions")],
        "example": "« Que devrait-il se passer ? Que se passe-t-il vraiment ? Qu'est-ce qui a changé ? »",
        "example_cue": "Ses trois préférées",
        "script": "Au Gemba, pas à un bureau. Elle observe le processus réel et le produit réel. Elle parle "
                  "avec l'opérateur qui fait le travail. Elle compare la méthode réelle au standard. Et "
                  "elle pose des questions qui font réfléchir, au lieu de donner toutes les réponses. Ses "
                  "trois préférées sont simples. Que devrait-il se passer ? Que se passe-t-il vraiment ? Et "
                  "qu'est-ce qui a changé ? Laquelle poseriez-vous en premier ?",
    },
    {
        "key": "p08", "num": 8, "title": "Travail standard du responsable",
        "points": [("Des contrôles par fréquence", "liste ses contrôles"),
                   ("Séquence, temps de cycle, points qualité", "Elle vérifie"),
                   ("Le dernier SOP à chaque poste", "Et le dernier SOP")],
        "example": "La liste de Sunita : début d'équipe, chaque heure, chaque changement de modèle, fin "
                   "d'équipe.",
        "example_cue": "Sa liste couvre",
        "script": "Un Hancho a besoin lui aussi d'un travail standard. Le travail standard du responsable "
                  "liste ses contrôles, selon leur fréquence. Elle vérifie la séquence de travail, le temps "
                  "de cycle face au TAKT, et les points qualité. Elle vérifie que les outils et les "
                  "gabarits sont bons. Et le dernier SOP doit être à chaque poste, et compris. Sa liste "
                  "couvre le début d'équipe, chaque heure, chaque changement de modèle, et la fin. Que "
                  "contiendrait la vôtre ?",
    },
    {
        "key": "p09", "num": 9, "title": "Management visuel",
        "points": [("Plan face au réel, chaque heure", "Le plan face au réel"),
                   ("Qualité, arrêts, actions ouvertes", "Le rendement au premier passage"),
                   ("Voir, réagir, enregistrer, suivre", "Chaque chiffre en rouge")],
        "example": "10 h à 11 h : plan 120 TV, réel 98. Rouge.",
        "example_cue": "À onze heures",
        "script": "Rendez la ligne lisible d'un coup d'œil. Le plan face au réel, chaque heure. Le "
                  "rendement au premier passage, les principaux défauts, les causes d'arrêt, et les actions "
                  "ouvertes avec leurs responsables. Mais un tableau n'est pas une décoration. Chaque "
                  "chiffre en rouge doit déclencher une réaction. Voyez-le, réagissez, enregistrez-le, et "
                  "suivez. À onze heures, le tableau de Sunita est passé au rouge. Plan, cent vingt TV. "
                  "Réel, quatre-vingt-dix-huit. Que doit-elle faire en premier ?",
    },
    {
        "key": "p10", "num": 10, "title": "Réaction aux anomalies",
        "points": [("Détecter, confiner, appeler", "Détectez l'écart"),
                   ("Corriger et confirmer", "Corrigez le processus"),
                   ("Prévenir et partager", "Puis prévenez-le")],
        "example": "Niveau 1 : l'équipe le corrige. Niveau 2 : appeler le support. Niveau 3 : escalader à la "
                   "direction.",
        "example_cue": "Il y a trois niveaux",
        "script": "Suivez une réaction claire. Détectez l'écart, confinez-le pour protéger le client, et "
                  "appelez le bon support. Corrigez le processus, et confirmez que la production est de "
                  "nouveau bonne. Puis prévenez-le, et partagez ce que vous avez appris. Il y a trois "
                  "niveaux. Niveau un, l'équipe le corrige. Niveau deux, appelez la qualité, l'ingénierie "
                  "ou la maintenance. Niveau trois, risque sécurité ou client, escaladez tout de suite. "
                  "Quel était le niveau de Sunita ?",
    },
    {
        "key": "p11", "num": 11, "title": "L'heure rouge de Sunita",
        "points": [("Production : 98 contre 120 par heure", "La production était tombée"),
                   ("Rendement au premier passage : de 98,5 % à 95,8 %", "Le rendement au premier passage"),
                   ("Le travail s'accumule avant le test", "Et le travail s'accumulait")],
        "example": "Cela a commencé juste après le changement de modèle de 10 heures.",
        "example_cue": "Tout a commencé",
        "script": "Voici ce qu'elle a vu. La production était tombée à quatre-vingt-dix-huit TV par heure, "
                  "contre un plan de cent vingt. Le rendement au premier passage avait baissé de près de "
                  "trois points. Et le travail s'accumulait devant le poste de test. Trois chiffres, tous "
                  "dans le mauvais sens. Tout a commencé juste après le changement de modèle de dix heures. "
                  "Iriez-vous d'abord au poste de test ?",
    },
    {
        "key": "p12", "num": 12, "title": "Confiner, puis aller voir",
        "points": [("Bloquer les TV suspectes", "elle a bloqué"),
                   ("Trouver le poste goulot", "a trouvé le goulot"),
                   ("Comparer la méthode au standard", "a comparé la méthode")],
        "example": "Poste 6 : sur le nouveau modèle, le câble de dalle prenait un autre chemin, et les "
                   "opérateurs le pliaient à la main.",
        "example_cue": "Au poste six",
        "script": "Pas encore. D'abord, elle a bloqué chaque TV suspecte depuis dix heures. Client protégé. "
                  "Puis elle a parcouru la ligne, et a trouvé le goulot avant le test. Elle a comparé la "
                  "méthode au standard, à chaque poste. Au poste six, le câble de dalle du nouveau modèle "
                  "prenait un autre chemin. Le gabarit guidait toujours l'ancien chemin. Les opérateurs "
                  "pliaient donc le câble à la main, et certains n'étaient pas bien enfichés. Était-ce du "
                  "niveau un ?",
    },
    {
        "key": "p13", "num": 13, "title": "Appeler, corriger, confirmer",
        "points": [("Niveau 2 : appeler l'ingénierie", "Elle a appelé l'ingénierie"),
                   ("Corriger le gabarit, mettre à jour le SOP", "a ajusté le guide de câble"),
                   ("Confirmer sur plusieurs cycles", "l'a confirmé")],
        "example": "À 1 h de l'après-midi : 120 TV par heure, rendement au premier passage de 98,6 %.",
        "example_cue": "À une heure",
        "script": "C'était du niveau deux. Elle a appelé l'ingénierie, avec des faits, des photos et les "
                  "unités défaillantes. L'ingénierie a ajusté le guide de câble pour le nouveau modèle, et "
                  "le SOP a été mis à jour. Sunita l'a confirmé sur plusieurs cycles, pas seulement sur une "
                  "bonne TV. À une heure, la ligne était revenue à cent vingt par heure. Le rendement au "
                  "premier passage était de quatre-vingt-dix-huit virgule six. Qui s'est assuré que chaque "
                  "équipe le sache ?",
    },
    {
        "key": "p14", "num": 14, "title": "Faire grandir les personnes",
        "points": [("Expliquer, montrer, pratiquer, vérifier", "Expliquez, démontrez"),
                   ("Certifier les compétences critiques", "Certifiez les compétences critiques"),
                   ("Former en polyvalence pour se remplacer", "Formez en polyvalence")],
        "example": "Sunita a formé deux opérateurs au nouveau cheminement du câble avant l'équipe de nuit.",
        "example_cue": "Sunita a formé",
        "script": "Un Hancho développe des compétences, pas de la dépendance. Utilisez un rythme de "
                  "formation simple. Expliquez, démontrez, laissez-les pratiquer, puis vérifiez. Certifiez "
                  "les compétences critiques avant que quiconque travaille seul. Formez en polyvalence, "
                  "pour qu'une absence ne puisse pas arrêter la ligne. Et apprenez-leur à résoudre des "
                  "problèmes, pas seulement le travail. Sunita a formé deux opérateurs au nouveau "
                  "cheminement du câble, avant le début de l'équipe de nuit. Votre ligne pourrait-elle "
                  "tourner sans vous ?",
    },
    {
        "key": "p15", "num": 15, "title": "Le mesurer, puis démarrer",
        "points": [("KPI chaque heure, chaque jour, chaque semaine", "Revoyez la production"),
                   ("Auditer pour accompagner, pas pour blâmer", "Auditez pour accompagner"),
                   ("Un plan sur 30 jours", "Voici un plan sur trente jours")],
        "example": "Semaine 1 rôles · semaine 2 tableau horaire · semaine 3 compétences · semaine 4 audit et "
                   "revue.",
        "example_cue": "Voici un plan sur trente jours",
        "script": "Mesurez les résultats et la discipline. Revoyez la production et les arrêts chaque "
                  "heure, la qualité chaque jour, et les compétences et le Kaizen chaque semaine. Un "
                  "chiffre vert sans discipline ne durera pas. Auditez pour accompagner votre équipe, pas "
                  "pour prendre les gens en faute. Voici un plan sur trente jours. Semaine une, définissez "
                  "les rôles et le travail standard du responsable. Semaine deux, lancez le tableau "
                  "horaire. Semaine trois, compétences et accompagnement. Semaine quatre, audit et revue. "
                  "Par quelle semaine commencerez-vous ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Chef d'équipe", "sub": "班長", "icon": "person", "with": 0},
        {"label": "Un système", "icon": "gear", "with": 1},
        {"label": "Au Gemba", "icon": "walk", "tone": "good", "with": 2}]},
    "p02": {"type": "steps", "items": [
        {"label": "Standard ?", "with": 0}, {"label": "Réel ?", "with": 0},
        {"label": "Écart et cause ?", "with": 1}, {"label": "Agir et prévenir", "with": 2}]},
    "p03": {"type": "versus", "items": [
        {"label": "Responsable éloigné", "sub": "Écart trouvé le lendemain matin", "icon": "clock", "tone": "bad", "with": 0},
        {"label": "Hancho sur la ligne", "sub": "Écart trouvé dans l'heure", "icon": "person", "tone": "good", "with": 1}]},
    "p04": {"type": "icons", "items": [
        {"label": "Sécurité", "icon": "shield", "with": 0},
        {"label": "Qualité", "icon": "check", "with": 0},
        {"label": "Livraison", "icon": "calendar", "with": 1},
        {"label": "Coût", "icon": "scale", "with": 1},
        {"label": "Personnes", "icon": "person", "with": 2},
        {"label": "Processus", "icon": "clipboard", "with": 2}]},
    "p05": {"type": "flow", "items": [
        {"label": "Préparation", "sub": "Personnes, matières, outils", "icon": "clipboard", "with": 0},
        {"label": "Briefing", "sub": "Cible, alertes, retours d'expérience", "icon": "person", "with": 1},
        {"label": "Contrôles de démarrage", "sub": "Première pièce", "icon": "check", "tone": "good", "with": 2}]},
    "p06": {"type": "timeline", "items": [
        {"label": "Plan face au réel", "sub": "Chaque heure", "icon": "clock", "with": 0},
        {"label": "Réagir, accompagner", "sub": "Toute l'équipe", "icon": "hand", "with": 1},
        {"label": "Passation", "sub": "Fin d'équipe", "icon": "clipboard", "tone": "good", "with": 3}]},
    "p07": {"type": "icons", "items": [
        {"label": "Observer", "icon": "search", "with": 0},
        {"label": "Parler", "icon": "person", "with": 1},
        {"label": "Demander, ne pas ordonner", "icon": "key", "tone": "good", "with": 2}]},
    "p08": {"type": "doc", "items": [
        {"label": "Début d'équipe : préparation", "icon": "calendar", "with": "example"},
        {"label": "Chaque heure : plan face au réel", "icon": "clock", "with": "example"},
        {"label": "Changement de modèle : première pièce", "icon": "check", "with": "example"},
        {"label": "Fin d'équipe : passation", "icon": "clipboard", "with": "example"}]},
    "p09": {"type": "bars", "label": "", "note": "10 h – 11 h : plan face au réel", "with": "example", "items": [
        {"label": "Plan", "value": 120, "tone": "good", "with": "example"},
        {"label": "Réel", "value": 98, "tone": "bad", "with": "example"}]},
    "p10": {"type": "ladder", "top": "NIVEAU 3", "bottom": "NIVEAU 1", "items": [
        {"label": "Risque sécurité ou client : escaladez tout de suite", "icon": "warning", "tone": "bad", "with": "example"},
        {"label": "Appelez les fonctions support", "icon": "person", "with": "example"},
        {"label": "L'équipe rétablit le standard", "icon": "hand", "tone": "good", "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "98 contre 120 par heure", "icon": "chartDown", "tone": "bad", "with": 0},
        {"label": "FPY 98.5% → 95.8%", "icon": "test", "tone": "bad", "with": 1},
        {"label": "WIP avant le test", "icon": "stack", "tone": "bad", "with": 2}]},
    "p12": {"type": "flow", "items": [
        {"label": "Bloquer les TV suspectes", "icon": "lock", "with": 0},
        {"label": "Trouver le goulot", "icon": "search", "with": 1},
        {"label": "Poste 6 : chemin du câble modifié", "icon": "wrench", "tone": "bad", "with": "example"}]},
    "p13": {"type": "compare", "before": {"label": "11 h", "value": 98}, "after": {"label": "1 h de l'après-midi", "value": 120},
            "unit": "TV par heure", "note": "Rendement au premier passage revenu à 98,6 %", "with": "example"},
    "p14": {"type": "steps", "items": [
        {"label": "Expliquer", "with": 0}, {"label": "Démontrer", "with": 0},
        {"label": "Pratiquer", "with": 0}, {"label": "Vérifier", "with": 1}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Rôles, travail standard du responsable", "sub": "Semaine 1", "icon": "clipboard", "with": 2},
        {"label": "Tableau horaire", "sub": "Semaine 2", "icon": "chartUp", "with": 2},
        {"label": "Compétences, accompagnement", "sub": "Semaine 3", "icon": "person", "with": 2},
        {"label": "Audit, revue", "sub": "Semaine 4", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Le travail d'un Hancho consiste surtout à…",
        "options": ["Remplir le rapport d'équipe en fin de journée",
                    "Diriger au Gemba : tenir le standard, réagir aux écarts, faire grandir les personnes",
                    "Faire lui-même le poste le plus difficile, à chaque équipe"],
        "correct": 1,
        "explanation": "Un Hancho dirige là où la valeur est créée : il protège le standard, réagit vite aux "
                       "anomalies et développe les compétences de l'équipe. Les rapports et le remplacement aux "
                       "postes ne sont pas le cœur du rôle.",
        "q_script": "Vérification rapide. Quel est le travail principal d'un Hancho ? Prenez quelques "
                    "secondes.",
        "a_script": "C'est le deuxième. Diriger au Gemba. Tenir le standard, réagir aux écarts, et faire "
                    "grandir vos équipes.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Le tableau horaire passe au rouge et les unités suspectes peuvent présenter un risque "
                    "sécurité. Quel niveau de réaction ?",
        "options": ["Niveau 1 : l'équipe corrige discrètement",
                    "Niveau 2 : appeler la maintenance quand elle est libre",
                    "Niveau 3 : confiner et escalader immédiatement à la direction"],
        "correct": 2,
        "explanation": "Un risque sécurité ou client, c'est le niveau 3 : confinez les unités et escaladez "
                       "immédiatement. N'attendez pas de voir si l'équipe peut s'en charger.",
        "q_script": "Encore une, et cette fois c'est un scénario. Le tableau horaire passe au rouge, et les "
                    "unités suspectes peuvent présenter un risque sécurité. Quel est le niveau de réaction ? "
                    "Réfléchissez.",
        "a_script": "C'est le niveau trois. Confinez les unités, et escaladez immédiatement à la direction. "
                    "Un risque sécurité n'attend jamais.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
