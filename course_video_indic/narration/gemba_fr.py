"""gemba in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh gemba_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "gb_fr"
NAME = "gemba_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Genbutsu": "Guène-boutsou",
    "Genjitsu": "Guène-djitsou",
    "Hancho": "Hanntcho",
    "Gemba": "Guemba",
    "PPE": "pé pé eu",
    "ESD": "eu esse dé",
    "3G": "trois gé",
    "G": "gé",
    "A": "a",
    "B": "bé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Le tableau de bord disait que l'équipe B était négligente. Deux fois plus d'écouteurs "
    "échouaient au test audio que dans l'équipe A. Le plan était simple. Reformer l'équipe B. "
    "Personne n'avait regardé un seul écouteur défaillant. Ça vous dit quelque chose ? Dans "
    "cette leçon, vous allez découvrir le Gemba, et les 3G qui l'accompagnent. Vous verrez "
    "comment aller au lieu réel, examiner la chose réelle, et vérifier les faits réels. Nous "
    "suivrons Manoj, superviseur de production sur une ligne d'écouteurs sans fil."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Allez au lieu réel, et observez de vrais cycles avant de "
    "décider. Prenez la chose réelle en main, et comparez-la à une bonne. Et vérifiez les "
    "faits réels, avec des comptages, des temps et un dénominateur. Voici votre action pour "
    "cette semaine. Prenez un problème récurrent, et faites une visite 3G de trente minutes. "
    "Bravo d'avoir terminé cette leçon. Ensuite, vous découvrirez le Hancho, le leadership "
    "sur le terrain."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Aller voir",
        "points": [("Gemba : le lieu réel", "Gemba veut dire"),
                   ("Genbutsu : la chose réelle", "Genbutsu veut dire"),
                   ("Genjitsu : les faits réels", "Genjitsu veut dire")],
        "example": "La règle de Manoj : aucune décision sur l'équipe B avant d'avoir tenu un écouteur "
                   "défaillant en main.",
        "example_cue": "Manoj s'est fixé une règle",
        "script": "Le Lean a une habitude simple. Allez voir, avant de décider. Elle tient en trois mots "
                  "japonais, souvent appelés les 3G. Gemba veut dire le lieu réel, là où le travail se "
                  "fait. Genbutsu veut dire la chose réelle, comme la pièce défaillante. Genjitsu veut dire "
                  "les faits réels. Manoj s'est fixé une règle. Aucune décision sur l'équipe B, avant "
                  "d'avoir tenu un écouteur défaillant en main. Pourquoi est-ce important ?",
    },
    {
        "key": "p02", "num": 2, "title": "Pourquoi les rapports ne suffisent pas",
        "points": [("Les tableaux de bord montrent des symptômes", "Les tableaux de bord montrent"),
                   ("Les rapports cachent le contexte", "Les rapports cachent"),
                   ("Les faits arrêtent les reproches", "Et les faits arrêtent")],
        "example": "Le tableau de bord montrait les défaillances de l'équipe B. Il ne montrait pas pourquoi.",
        "example_cue": "Le tableau de bord de Manoj",
        "script": "Parce que les rapports ne racontent qu'une partie de l'histoire. Les tableaux de bord "
                  "montrent des symptômes, pas des causes. Les rapports cachent la séquence, les "
                  "contournements et le contexte. Une pièce, un gabarit ou un poste de travail montre "
                  "souvent des preuves qu'aucun tableur ne peut montrer. Et les faits arrêtent les "
                  "reproches, et l'argent gaspillé dans la mauvaise solution. Le tableau de bord de Manoj "
                  "montrait que l'équipe B échouait plus. Il ne pouvait pas montrer pourquoi. Alors, par où "
                  "commencer ?",
    },
    {
        "key": "p03", "num": 3, "title": "Les 3G en une vue",
        "points": [("Où cela s'est-il produit ?", "Gemba demande"),
                   ("Qu'est-ce qui a été touché exactement ?", "Genbutsu demande"),
                   ("Que s'est-il réellement passé ?", "Genjitsu demande")],
        "example": "Ligne 2 · test audio · écouteur gauche · 22 sur 1 100 dans l'équipe B",
        "example_cue": "Pour Manoj",
        "script": "Voyez chaque G comme une question. Gemba demande, où cela s'est-il produit ? La ligne, "
                  "le poste, l'étape. Genbutsu demande, qu'est-ce qui a été touché exactement ? L'unité, la "
                  "pièce, l'outil. Genjitsu demande, que s'est-il réellement passé ? Des temps, des "
                  "comptages et des mesures. Pour Manoj, c'était la ligne deux, le test audio, et "
                  "l'écouteur gauche. Vingt-deux défaillances sur mille cent, dans l'équipe B. Alors allons "
                  "au lieu réel.",
    },
    {
        "key": "p04", "num": 4, "title": "Gemba : le lieu réel",
        "points": [("Avoir une question claire", "Partez d'une question claire"),
                   ("Prévenir le responsable de zone, porter les PPE", "Prévenez le responsable de zone"),
                   ("Observer plusieurs cycles complets", "Observez plusieurs"),
                   ("Comparer au standard", "Comparez ce que vous voyez")],
        "example": "La question de Manoj : qu'est-ce qui est différent au test audio dans l'équipe B ?",
        "example_cue": "La question de Manoj",
        "script": "Partez d'une question claire, et d'un processus cible. Prévenez le responsable de zone "
                  "de votre venue, et suivez les règles PPE et ESD. Observez plusieurs cycles complets, "
                  "sans intervenir. Comparez ce que vous voyez avec le travail standard approuvé. Puis "
                  "posez des questions neutres, et notez tout écart avec son heure et son lieu. La question "
                  "de Manoj était courte. Qu'est-ce qui est différent au test audio dans l'équipe B ? "
                  "Comment devez-vous vous comporter sur place ?",
    },
    {
        "key": "p05", "num": 5, "title": "Le savoir-vivre au Gemba",
        "points": [("Pas une inspection surprise", "n'est pas une inspection surprise"),
                   ("Écouter avant de suggérer", "Écoutez avant"),
                   ("Ne jamais juger sur un seul cycle", "ne jugez jamais")],
        "example": "Manoj est resté une heure complète avec l'équipe B, et a demandé : « Qu'est-ce qui rend "
                   "ce travail difficile ? »",
        "example_cue": "Manoj est resté une heure complète avec l'équipe B",
        "script": "Une visite au Gemba n'est pas une inspection surprise, ni une chasse au coupable. "
                  "Écoutez avant de suggérer quoi que ce soit. N'interrompez pas un travail critique. Et ne "
                  "jugez jamais sur un seul cycle, car un seul cycle peut vous tromper. Manoj est resté une "
                  "heure complète avec l'équipe B. Il a posé une question. Qu'est-ce qui rend ce travail "
                  "difficile pour vous ? Les réponses l'ont surpris. Mais que devez-vous tenir en main ?",
    },
    {
        "key": "p06", "num": 6, "title": "Genbutsu : la chose réelle",
        "points": [("L'unité défaillante, la pièce, l'outil", "Cela veut dire l'unité défaillante"),
                   ("Noter modèle, lot, heure, poste", "Notez le modèle"),
                   ("Comparer le mauvais au bon", "Comparez une mauvaise unité")],
        "example": "Écouteurs gauches défaillants : soudure terne et granuleuse sur le fil du haut-parleur. "
                   "Les bons : brillante et lisse.",
        "example_cue": "Manoj a comparé",
        "script": "Prenez la chose réelle en main. Cela veut dire l'unité défaillante, le composant, le "
                  "gabarit ou l'outil. Notez le modèle, le lot, l'heure et le poste avant d'y toucher. "
                  "Inspectez-la sans modifier la preuve. Comparez une mauvaise unité avec une bonne, côte à "
                  "côte, sous la même lumière. Manoj a comparé des écouteurs gauches défaillants avec des "
                  "bons. Les soudures défaillantes paraissaient ternes et granuleuses. Qu'est-ce qui "
                  "pourrait causer cela ?",
    },
    {
        "key": "p07", "num": 7, "title": "La sécurité d'abord",
        "points": [("Ne jamais contourner un interverrouillage", "Ne contournez jamais"),
                   ("Consigner avant d'ouvrir un équipement", "Consignez d'abord"),
                   ("Manipulation ESD pour l'électronique", "manipulez l'électronique")],
        "example": "Manoj a demandé au technicien de refroidir et de consigner le fer avant de le vérifier.",
        "example_cue": "Manoj a demandé",
        "script": "Une règle passe avant la curiosité. Ne contournez jamais un interverrouillage, et "
                  "n'ouvrez jamais un équipement sous tension, juste pour voir la chose réelle. Consignez "
                  "d'abord, et laissez faire une personne qualifiée. Manipulez l'électronique avec une "
                  "protection ESD, sinon vous créerez de nouveaux défauts pendant votre enquête. Manoj a "
                  "demandé au technicien de refroidir et de consigner la station de soudage avant de la "
                  "vérifier. Une preuve sûre est une bonne preuve. Et maintenant, les faits ?",
    },
    {
        "key": "p08", "num": 8, "title": "Genjitsu : les faits réels",
        "points": [("Des faits, pas des opinions", "Remplacez les opinions"),
                   ("Des comptages avec un dénominateur", "Utilisez des comptages"),
                   ("Un signal n'est pas une preuve", "est un signal")],
        "example": "Équipe B : 22 sur 1 100 (2,0 %). Équipe A : 9 sur 1 050 (0,9 %).",
        "example_cue": "L'équipe B a eu",
        "script": "Remplacez les opinions par des faits. Le test est lent, c'est une opinion. Le temps de "
                  "test médian est passé de quarante-six à soixante et une secondes, c'est un fait. "
                  "Utilisez des comptages avec un dénominateur, et des horodatages fiables. L'équipe B a eu "
                  "vingt-deux défaillances sur mille cent. L'équipe A en a eu neuf sur environ mille. Cette "
                  "différence est un signal pour enquêter. Mais prouve-t-elle que l'équipe B en est la "
                  "cause ?",
    },
    {
        "key": "p09", "num": 9, "title": "Une enquête reliée",
        "points": [("Définir et confiner d'abord", "Définissez le problème"),
                   ("Lieu, chose, faits, ensemble", "allez au lieu réel"),
                   ("Tester les causes avant de corriger", "Puis testez")],
        "example": "Manoj a d'abord bloqué les écouteurs suspects de l'équipe B.",
        "example_cue": "Manoj a d'abord bloqué",
        "script": "Non. Utilisez donc les 3G comme une seule enquête reliée, pas comme trois cases à "
                  "cocher. Définissez le problème en chiffres, et protégez d'abord votre client. Puis allez "
                  "au lieu réel, inspectez la chose, et rassemblez les faits, ensemble. Puis testez les "
                  "causes possibles, avant de changer quoi que ce soit durablement. Manoj a d'abord bloqué "
                  "tous les écouteurs suspects de l'équipe B. Puis il est retourné au poste. Que lui a "
                  "montré le lieu réel ?",
    },
    {
        "key": "p10", "num": 10, "title": "Ce que le lieu a montré",
        "points": [("Mêmes personnes, même méthode", "suivait la même méthode"),
                   ("Une panne de fer différente", "la panne du fer"),
                   ("Changée le lundi soir", "changée le lundi")],
        "example": "Le fer de l'équipe B avait une panne plus petite venant du magasin de pièces. Pas la "
                   "panne standard.",
        "example_cue": "Elle venait",
        "script": "Au début, rien ne semblait anormal. L'équipe B suivait la même méthode que l'équipe A, "
                  "étape par étape. Puis Manoj a regardé de près la panne du fer. Elle était plus petite "
                  "que celle du poste de l'équipe A. Elle avait été changée le lundi soir. Elle venait du "
                  "magasin de pièces, et ce n'était pas la panne standard. Une panne plus petite "
                  "pourrait-elle faire une soudure plus faible ? Comment le sauriez-vous ?",
    },
    {
        "key": "p11", "num": 11, "title": "Ce que les faits ont montré",
        "points": [("Défaillances par poste et par heure", "Manoj a cartographié"),
                   ("Commencées juste après le changement de panne", "ont commencé l'équipe"),
                   ("Un essai contrôlé l'a confirmé", "Puis un essai contrôlé")],
        "example": "Essai : panne standard 1 défaillance sur 300. Panne plus petite : 7 sur 300.",
        "example_cue": "Avec la panne standard",
        "script": "Manoj a cartographié chaque défaillance par poste, heure et lot. Elles ont commencé "
                  "l'équipe qui a suivi le changement de panne, et seulement sur ce poste. Puis un essai "
                  "contrôlé, approuvé par l'ingénierie, a testé les deux pannes. Avec la panne standard, un "
                  "écouteur sur trois cents a échoué. Avec la panne plus petite, sept ont échoué. La panne "
                  "plus petite ne pouvait pas apporter assez de chaleur dans la soudure. L'équipe B "
                  "était-elle négligente, finalement ?",
    },
    {
        "key": "p12", "num": 12, "title": "Les 3G alimentent la cause racine",
        "points": [("Chaque pourquoi appuyé sur une preuve", "Chaque pourquoi"),
                   ("Ne jamais s'arrêter à « erreur de l'opérateur »", "Ne vous arrêtez jamais"),
                   ("Demander ce qui a rendu l'erreur possible", "Demandez quelle condition")],
        "example": "Cause racine : le magasin de pièces stockait la mauvaise panne, et le standard ne la "
                   "nommait pas.",
        "example_cue": "Le dernier pourquoi de Manoj",
        "script": "Non. Les 3G donnent de vraies preuves à vos outils de cause racine. Avec les cinq "
                  "pourquoi, chaque pourquoi doit s'appuyer sur quelque chose que vous avez vu ou mesuré. "
                  "Ne vous arrêtez jamais à l'erreur de l'opérateur, ou à plus de formation. Demandez "
                  "quelle condition du processus a rendu l'erreur possible. Le dernier pourquoi de Manoj "
                  "était clair. Le magasin de pièces stockait la mauvaise panne, et le standard ne nommait "
                  "pas le type de panne. Alors, qu'a-t-il changé ?",
    },
    {
        "key": "p13", "num": 13, "title": "Corriger et vérifier",
        "points": [("La bonne panne, nommée dans le standard", "nommait maintenant le type de panne"),
                   ("Contrôle de la panne à chaque début d'équipe", "un contrôle de la panne"),
                   ("Vérifié sur cinq équipes", "a vérifié le résultat")],
        "example": "Équipe B : de 20 à 8 pour 1 000, au niveau de l'équipe A.",
        "example_cue": "Les défaillances de l'équipe B",
        "script": "La solution était simple. Le standard nommait maintenant le type de panne, et le magasin "
                  "de pièces ne stockait que la bonne. Un contrôle de la panne a rejoint la routine de "
                  "début d'équipe. Puis il a vérifié le résultat sur cinq équipes complètes, pas sur une "
                  "bonne heure. Les défaillances de l'équipe B sont passées de vingt pour mille à huit, au "
                  "niveau de l'équipe A. Et l'équipe B n'a jamais eu besoin d'être reformée. Comment en "
                  "faire une habitude quotidienne ?",
    },
    {
        "key": "p14", "num": 14, "title": "La tournée Gemba de 30 minutes",
        "points": [("Objectif et sécurité d'abord", "passez en revue la sécurité"),
                   ("Observer, puis vérifier la chose et les données", "observez le processus"),
                   ("Convenir du confinement et d'un responsable", "convenez du confinement")],
        "example": "La question de Manoj à chaque arrêt : « Quel est le standard, et que se passe-t-il "
                   "vraiment ? »",
        "example_cue": "La question préférée de Manoj",
        "script": "Faites-en un travail standard. Dans une tournée de trente minutes, passez en revue la "
                  "sécurité, l'écart et votre objectif. Puis observez le processus au point de travail "
                  "pendant dix minutes. Inspectez l'élément touché, et vérifiez les données clés. Demandez "
                  "à l'équipe les causes, convenez du confinement, et nommez un responsable avec une date. "
                  "La question préférée de Manoj est simple. Quel est le standard, et que se passe-t-il "
                  "vraiment ? Que demanderiez-vous ?",
    },
    {
        "key": "p15", "num": 15, "title": "Erreurs à éviter",
        "points": [("Piloter depuis le tableau de bord", "Piloter seulement"),
                   ("Prendre un échantillon pour la vérité", "Prendre un seul échantillon"),
                   ("Clôturer après une formation", "Clôturer un problème")],
        "example": "Manoj passe maintenant les 30 premières minutes de chaque équipe au Gemba.",
        "example_cue": "Manoj passe maintenant",
        "script": "Attention à quelques erreurs fréquentes. Piloter seulement depuis le tableau de bord. "
                  "S'appuyer sur des entretiens, sans tenir la pièce. Prendre un seul échantillon pour la "
                  "vérité. Changer des réglages pendant l'enquête, et détruire les preuves. Clôturer un "
                  "problème après une formation, sans vérifier qu'il s'est arrêté. Manoj passe maintenant "
                  "les trente premières minutes de chaque équipe au Gemba. Pourriez-vous faire de même ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Gemba", "sub": "Lieu réel", "icon": "walk", "with": 0},
        {"label": "Genbutsu", "sub": "Chose réelle", "icon": "wave", "with": 1},
        {"label": "Genjitsu", "sub": "Faits réels", "icon": "search", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Tableau de bord", "sub": "Montre des symptômes", "icon": "chartUp", "with": 0},
        {"label": "Le lieu réel", "sub": "Montre des causes", "icon": "walk", "tone": "good", "with": 2}]},
    "p03": {"type": "flow", "items": [
        {"label": "Où ?", "sub": "Ligne 2, test audio", "icon": "pin", "with": 0},
        {"label": "Quoi ?", "sub": "Écouteur gauche", "icon": "wave", "with": 1},
        {"label": "Que s'est-il passé ?", "sub": "22 sur 1 100", "icon": "count", "with": 2}]},
    "p04": {"type": "steps", "items": [
        {"label": "Question claire", "with": 0}, {"label": "Responsable, PPE, ESD", "with": 1},
        {"label": "Observer des cycles complets", "with": 2}, {"label": "Comparer au standard", "with": 3}]},
    "p05": {"type": "versus", "items": [
        {"label": "Inspection surprise", "sub": "Chercher un coupable", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Visite respectueuse", "sub": "« Qu'est-ce qui rend ça difficile ? »", "icon": "person", "tone": "good", "with": "example"}]},
    "p06": {"type": "versus", "items": [
        {"label": "Écouteur défaillant", "sub": "Soudure terne, granuleuse", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "Bon écouteur", "sub": "Soudure brillante, lisse", "icon": "check", "tone": "good", "with": "example"}]},
    "p07": {"type": "icons", "items": [
        {"label": "Aucun interverrouillage contourné", "icon": "lock", "with": 0},
        {"label": "Consignation d'abord", "icon": "key", "with": 1},
        {"label": "Protection ESD", "icon": "shield", "tone": "good", "with": 2}]},
    "p08": {"type": "bars", "label": "", "note": "Défaillances pour 1 000 écouteurs : un signal, pas une preuve", "with": "example", "items": [
        {"label": "Équipe A", "value": 9, "with": "example"},
        {"label": "Équipe B", "value": 20, "tone": "bad", "with": "example"}]},
    "p09": {"type": "steps", "items": [
        {"label": "Définir et confiner", "with": 0},
        {"label": "Lieu", "with": 1}, {"label": "Chose", "with": 1}, {"label": "Faits", "with": 1},
        {"label": "Tester les causes", "with": 2}]},
    "p10": {"type": "versus", "items": [
        {"label": "Panne de l'équipe B", "sub": "Plus petite, venant du magasin de pièces", "icon": "wrench", "tone": "bad", "with": 1},
        {"label": "Panne standard", "sub": "Équipe A", "icon": "check", "tone": "good", "with": 1}]},
    "p11": {"type": "bars", "label": "", "note": "Essai contrôlé : défaillances sur 300 écouteurs", "with": "example", "items": [
        {"label": "Panne standard", "value": 1, "tone": "good", "with": "example"},
        {"label": "Panne plus petite", "value": 7, "tone": "bad", "with": "example"}]},
    "p12": {"type": "steps", "items": [
        {"label": "Soudures faibles", "with": 0},
        {"label": "Panne plus petite, trop peu de chaleur", "with": 0},
        {"label": "Mauvaise panne au magasin de pièces", "with": "example"},
        {"label": "Type de panne absent du standard", "with": "example"}]},
    "p13": {"type": "compare", "before": {"label": "Avant", "value": 20}, "after": {"label": "Après", "value": 8},
            "unit": "défaillances pour 1 000 écouteurs, équipe B", "note": "Au niveau de l'équipe A, vérifié sur 5 équipes", "with": "example"},
    "p14": {"type": "timeline", "items": [
        {"label": "Sécurité, écart, objectif", "sub": "0–5", "icon": "shield", "with": 0, "span": 5},
        {"label": "Observer", "sub": "5–15", "icon": "walk", "with": 1, "span": 10},
        {"label": "Chose et données", "sub": "15–22", "icon": "search", "with": 1, "span": 7},
        {"label": "Causes, responsable", "sub": "22–30", "icon": "person", "tone": "good", "with": 2, "span": 8}]},
    "p15": {"type": "icons", "items": [
        {"label": "Tableau de bord seul", "icon": "chartUp", "tone": "bad", "with": 0},
        {"label": "Un seul échantillon", "icon": "count", "tone": "bad", "with": 1},
        {"label": "Clôturé après formation", "icon": "clipboard", "tone": "bad", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Quelle phrase est un fait réel (Genjitsu) ?",
        "options": ["« L'équipe B est toujours négligente. »",
                    "« C'est le fournisseur qui l'a causé. »",
                    "« 18 des 24 défaillances viennent du lot B. »"],
        "correct": 2,
        "explanation": "Un fait a des comptages, un dénominateur et un périmètre vérifiable. Les autres sont des "
                       "opinions, et l'accusation du fournisseur n'est pas prouvée.",
        "q_script": "Vérification rapide. Laquelle de ces phrases est un fait réel ? Prenez quelques "
                    "secondes.",
        "a_script": "C'est la dernière. Elle a un comptage, un dénominateur et un périmètre vérifiable. Les "
                    "deux autres ne sont que des opinions.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Le tableau de bord montre une équipe avec deux fois plus de défauts. Le responsable veut "
                    "la reformer. Que faire en premier ?",
        "options": ["La reformer aujourd'hui : les données sont claires",
                    "Aller au poste, tenir les unités défaillantes, et vérifier les faits",
                    "Échanger les opérateurs des deux équipes"],
        "correct": 1,
        "explanation": "Une différence entre équipes est un signal, pas une preuve. Allez voir : le lieu réel, "
                       "la chose réelle et les faits réels, avant de décider d'une solution.",
        "q_script": "Encore une, et cette fois c'est un scénario. Le tableau de bord montre une équipe avec "
                    "deux fois plus de défauts. Le responsable veut la reformer. Que faut-il faire en premier "
                    "? Réfléchissez.",
        "a_script": "Allez voir. Visitez le poste, prenez les unités défaillantes en main, et vérifiez les "
                    "faits. Une différence entre équipes est un signal, pas une preuve.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
