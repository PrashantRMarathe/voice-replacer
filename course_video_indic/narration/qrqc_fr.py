"""qrqc in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh qrqc_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "qr_fr"
NAME = "qrqc_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Root Cause Analysis": "route côze analyse",
    "QRQC": "ku erre ku cé",
    "FMEA": "effe emme eu a",
    "5W2H": "cinq double vé deux ache",
    "MES": "emme eu esse",
    "SKU": "esse ka u",
    "SOP": "esse o pé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Dix heures. Des caméras commencent à échouer au test de mise au point. Quelqu'un "
    "réinitialise le testeur, et la ligne continue. À midi, une équipe entière de caméras "
    "suspectes part vers l'entrepôt. Ça vous dit quelque chose ? Dans cette leçon, vous allez "
    "découvrir le QRQC, le contrôle qualité à réponse rapide. Vous verrez comment réagir en "
    "quelques minutes, protéger votre client, et trouver quand même la vraie cause. Nous "
    "suivrons Farhan, responsable qualité dans une usine de caméras."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Réagissez vite, mais avec des preuves. Confinez d'abord, "
    "et réconciliez chaque unité suspecte. Et ne clôturez un problème que quand la solution "
    "est prouvée en production réelle. Voici votre action pour cette semaine. Écrivez les "
    "trente premières minutes de votre plan de réaction pour un défaut critique. Bravo "
    "d'avoir terminé cette leçon. Ensuite, vous approfondirez le Root Cause Analysis."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le QRQC",
        "points": [("Le détecter et le rendre visible", "Vous le détectez"),
                   ("Le confiner pour protéger le client", "Vous le confinez"),
                   ("Trouver la cause avec des faits, prouver la solution", "Puis vous trouvez la cause"),
                   ("La vitesse ne remplace jamais la preuve", "La vitesse compte")],
        "example": "Ligne 4 : le QRQC commence par isoler l'ordre de fabrication — pas par réinitialiser le "
                   "testeur.",
        "example_cue": "Sur la ligne quatre de Farhan",
        "script": "Voici l'idée centrale. QRQC veut dire contrôle qualité à réponse rapide. C'est une façon "
                  "disciplinée de réagir à un problème. Vous le détectez et le rendez visible. Vous le "
                  "confinez, pour protéger votre client. Puis vous trouvez la cause avec des faits, et "
                  "prouvez que la solution marche. La vitesse compte, mais elle ne remplace jamais la "
                  "preuve. Sur la ligne quatre de Farhan, le QRQC commence par isoler l'ordre de "
                  "fabrication. Pas par réinitialiser le testeur. Alors, qu'y a-t-il derrière cette "
                  "approche ?",
    },
    {
        "key": "p02", "num": 2, "title": "Principes clés",
        "points": [("Lieu réel, pièces réelles", "Allez au lieu réel"),
                   ("Faits vérifiés, jamais de reproche", "Utilisez des faits vérifiés"),
                   ("Réagir tout de suite à un risque client ou sécurité", "Réagissez tout de suite"),
                   ("Confinement ≠ solution définitive", "Et séparez le confinement temporaire")],
        "example": "La réunion de Farhan commence avec la caméra défaillante sur la table, à côté de ses "
                   "enregistrements.",
        "example_cue": "La réunion de Farhan commence",
        "script": "Le QRQC est né dans la qualité des fournisseurs automobiles. Il repose sur quelques "
                  "principes. Allez au lieu réel, et regardez les pièces réelles. Utilisez des faits "
                  "vérifiés, jamais des opinions ou des reproches. Réagissez tout de suite à tout risque "
                  "client ou sécurité. Et séparez le confinement temporaire de la solution définitive. La "
                  "réunion de Farhan commence avec la caméra défaillante sur la table, à côté de ses "
                  "enregistrements. Que mettriez-vous sur votre table ?",
    },
    {
        "key": "p03", "num": 3, "title": "Trois niveaux d'escalade",
        "points": [("Niveau 1 : la ligne ou l'équipe réagit", "Au niveau un"),
                   ("Niveau 2 : une équipe transverse", "Au niveau deux"),
                   ("Niveau 3 : la direction de l'usine, le client", "Au niveau trois"),
                   ("Escalader tout de suite : sécurité, fuite répétée", "Escaladez tout de suite")],
        "example": "Votre site fixe les délais d'escalade, selon le risque.",
        "example_cue": "Votre site fixe les délais",
        "script": "Un bon système QRQC a trois niveaux. Au niveau un, la ligne ou l'équipe détecte le "
                  "problème, arrête ou isole, et enregistre les preuves. Au niveau deux, une équipe "
                  "transverse enquête et agit. Au niveau trois, la direction de l'usine ajoute des moyens, "
                  "ou parle au client. Escaladez tout de suite pour la sécurité, ou une fuite répétée. "
                  "Votre site fixe les délais, selon le risque. Alors, que se passe-t-il dans les premières "
                  "minutes ?",
    },
    {
        "key": "p04", "num": 4, "title": "Les 30 premières minutes",
        "points": [("0–5 min : détecter, trouver poste et lot, isoler", "Dans les cinq premières minutes"),
                   ("Puis : prévenir le chef et la qualité, garder des échantillons", "Ensuite, prévenez le chef d'équipe"),
                   ("Puis : trouver le dernier point bon connu", "Puis trouvez le dernier point bon"),
                   ("À 30 min : quarantaine, enregistrement, attribution", "À trente minutes")],
        "example": "Ne redémarrez jamais un processus critique sur un accord oral.",
        "example_cue": "ne redémarrez jamais un processus critique",
        "script": "La première demi-heure donne le ton. Dans les cinq premières minutes, détectez, trouvez "
                  "le poste et le lot, et arrêtez ou isolez le flux. Ensuite, prévenez le chef d'équipe et "
                  "la qualité, et gardez des échantillons défaillants et bons. Puis trouvez le dernier "
                  "point bon connu. À trente minutes, mettez le stock suspect en quarantaine, et "
                  "enregistrez les quantités et les responsables. Et ne redémarrez jamais un processus "
                  "critique sur un accord oral. Quel serait votre premier appel ?",
    },
    {
        "key": "p05", "num": 5, "title": "5W2H : définir le problème",
        "points": [("Quoi, où, quand, qui", "Ce qui a échoué, où"),
                   ("Comment détecté, combien", "comment il a été détecté"),
                   ("Rejets confirmés face à la population suspecte", "Séparez les rejets confirmés")],
        "example": "Ligne 4 : 24 caméras sur 800 ont échoué à la mise au point entre 10 h et midi, juste "
                   "après un changement de gabarit d'objectif.",
        "example_cue": "Sur la ligne quatre, vingt-quatre",
        "script": "Un énoncé précis vous évite de poursuivre la mauvaise piste. Utilisez le 5W2H. Ce qui a "
                  "échoué, où, quand, qui l'a vu, comment il a été détecté, et combien. Séparez les rejets "
                  "confirmés de la population suspecte. Voici l'énoncé de Farhan. Sur la ligne quatre, "
                  "vingt-quatre caméras sur huit cents ont échoué à la mise au point ce matin-là. Cela a "
                  "commencé juste après un changement de gabarit d'objectif. Remarquez comme cela indique "
                  "déjà une piste. Mais d'abord, que faire des unités suspectes ?",
    },
    {
        "key": "p06", "num": 6, "title": "Confinement et réconciliation",
        "points": [("Trouver le périmètre suspect", "Trouvez le périmètre suspect"),
                   ("Le bloquer : physiquement et dans le système", "Bloquez ce stock"),
                   ("Trier selon le risque", "Triez-le selon le risque"),
                   ("Réconcilier chaque unité", "Puis réconciliez chaque unité")],
        "example": "2 000 caméras suspectes : triées bonnes + défaillantes + en attente doivent faire le "
                   "compte exact. Aucune unité ne peut disparaître.",
        "example_cue": "Farhan avait deux mille",
        "script": "Le confinement est une barrière, pas un remède. Trouvez le périmètre suspect par numéro "
                  "de série, ordre de fabrication et équipe. Bloquez ce stock, physiquement et dans le "
                  "système. Triez-le selon le risque. Puis réconciliez chaque unité. Farhan avait deux "
                  "mille caméras suspectes. La plupart ont été triées bonnes, certaines ont échoué, et le "
                  "reste attendait encore. Les chiffres doivent faire le compte exact. Aucune unité ne peut "
                  "simplement disparaître. Alors, où l'équipe suit-elle tout cela ?",
    },
    {
        "key": "p07", "num": 7, "title": "Le tableau QRQC et la réunion",
        "points": [("Risque, confinement, cause, action, responsable, date", "Chaque problème montre"),
                   ("Rouge ouvert · orange en vérification · vert prouvé", "Utilisez le rouge pour ouvert"),
                   ("Apporter les vraies pièces et les courbes de tendance", "Apportez les vraies pièces"),
                   ("Rien de « fait » sans preuve", "méfiez-vous du théâtre des réunions")],
        "example": "La réunion de 15 minutes de Farhan : nouveaux problèmes, puis confinement, puis actions "
                   "et escalades.",
        "example_cue": "Farhan anime une réunion de quinze",
        "script": "Le tableau QRQC est votre centre de pilotage. Chaque problème montre son risque, son "
                  "confinement, sa cause, son action, son responsable et son échéance. Utilisez le rouge "
                  "pour ouvert, l'orange pour en vérification, et le vert seulement pour une clôture "
                  "prouvée. Farhan anime une réunion de quinze minutes au tableau à chaque équipe. D'abord "
                  "les nouveaux problèmes, puis le confinement, puis les actions et les escalades. Apportez "
                  "les vraies pièces et les courbes de tendance. Et méfiez-vous du théâtre des réunions. Y "
                  "a-t-il quelque chose marqué fait sans preuve ?",
    },
    {
        "key": "p08", "num": 8, "title": "La cause racine avec des preuves",
        "points": [("Cinq pourquoi = une hypothèse, pas une preuve", "Une chaîne de cinq pourquoi"),
                   ("Reproduire la défaillance en sécurité", "Reproduisez la défaillance"),
                   ("Brainstormer sur les 6M", "Faites un brainstorming des causes sur"),
                   ("S'est produit · s'est échappé · le système l'a permis", "Cherchez trois causes")],
        "example": "Une arête de poisson seule ne suffit pas : chaque idée concurrente doit être testée.",
        "example_cue": "Puis testez les idées concurrentes",
        "script": "Trouvez maintenant la cause racine, avec des preuves. Une chaîne de cinq pourquoi est "
                  "une hypothèse, pas une preuve. Reproduisez la défaillance en sécurité si vous le pouvez. "
                  "Faites un brainstorming des causes sur la main-d'œuvre, la machine, la méthode, la "
                  "matière, la mesure et le milieu. Puis testez les idées concurrentes. Cherchez trois "
                  "causes. Pourquoi c'est arrivé, pourquoi ça s'est échappé, et ce qui, dans le système, a "
                  "permis les deux. Voyez-vous pourquoi une arête de poisson seule ne suffit pas ?",
    },
    {
        "key": "p09", "num": 9, "title": "Action corrective et maîtrise des changements",
        "points": [("Corriger comment c'est arrivé et comment ça s'est échappé", "Traitez les deux"),
                   ("Des contrôles techniques plutôt que des rappels", "Préférez des contrôles techniques"),
                   ("Vérifier temps de cycle, sécurité, faux rejets", "Vérifiez l'effet"),
                   ("Mettre à jour le FMEA, le SOP, la formation", "Puis mettez à jour le FMEA")],
        "example": "Un « vérifiez le gabarit » oral est devenu un scan : chaque gabarit lié à sa recette "
                   "approuvée.",
        "example_cue": "Sur la ligne de Farhan",
        "script": "Corrigez maintenant chaque cause vérifiée. Traitez les deux, comment c'est arrivé, et "
                  "comment ça s'est échappé. Préférez des contrôles techniques, comme des gabarits "
                  "détrompés et des verrouillages par scan, plutôt que des rappels. Vérifiez l'effet sur le "
                  "temps de cycle, la sécurité et les faux rejets. Puis mettez à jour le FMEA, le SOP et la "
                  "formation. Sur la ligne de Farhan, une consigne orale de vérifier le gabarit est devenue "
                  "un scan. Chaque gabarit est maintenant lié à sa recette approuvée. Alors, quand "
                  "pouvez-vous clôturer ?",
    },
    {
        "key": "p10", "num": 10, "title": "Critères de clôture",
        "points": [("Installé ≠ prouvé", "Installer une solution"),
                   ("Mise à l'épreuve : pièces bonnes, mauvaises, limites", "mettez-la à l'épreuve avec des pièces bonnes connues"),
                   ("Sur plusieurs équipes, modèles, changements de série", "Vérifiez-la sur plusieurs équipes"),
                   ("Chaque unité suspecte tranchée, puis signature", "Assurez-vous que chaque unité suspecte")],
        "example": "La règle de Farhan : dix jours de production sans répétition avant que le tableau passe "
                   "au vert.",
        "example_cue": "Farhan attend dix",
        "script": "Voici le piège. Installer une solution n'est pas la même chose que la prouver. Pour "
                  "clôturer, mettez-la à l'épreuve avec des pièces bonnes connues, mauvaises connues et "
                  "limites. Vérifiez-la sur plusieurs équipes, modèles et changements de série. Suivez la "
                  "répétition et le rendement pendant une période fixée. Assurez-vous que chaque unité "
                  "suspecte a une décision. Puis la qualité et le responsable signent. Farhan attend dix "
                  "jours de production sans répétition. Alors seulement le tableau passe au vert. Comment "
                  "mesurer tout cela ?",
    },
    {
        "key": "p11", "num": 11, "title": "KPI du QRQC",
        "points": [("Temps de réaction : détection → confinement", "Le temps de réaction va"),
                   ("% de couverture du confinement", "La couverture du confinement est"),
                   ("Rendement au premier passage et taux de défauts", "Suivez le rendement au premier passage"),
                   ("Clôture des actions à temps", "mesurez la clôture à temps")],
        "example": "95 % des unités suspectes trouvées = pas fini : 5 % sont encore dehors.",
        "example_cue": "Si vous avez trouvé",
        "script": "Utilisez un ensemble équilibré de mesures. Le temps de réaction va de la détection au "
                  "premier confinement efficace. La couverture du confinement est la part des unités "
                  "suspectes que vous avez retrouvées. Suivez le rendement au premier passage et le taux de "
                  "défauts. Et mesurez la clôture à temps des actions. En voici une subtile. Si vous avez "
                  "trouvé quatre-vingt-quinze pour cent des unités suspectes, vous n'avez pas fini. Cinq "
                  "pour cent sont encore dehors. Prêt pour le cas de Farhan ?",
    },
    {
        "key": "p12", "num": 12, "title": "Cas pratique : défaut de mise au point",
        "points": [("24 sur 800 échouent à la mise au point contre < 0,5 % normalement", "Après le changement de série"),
                   ("Bloquer l'ordre de fabrication + la production depuis le dernier bon réglage", "Farhan a bloqué l'ordre de fabrication"),
                   ("Comparer gabarit, recette, tendance de mise au point", "L'équipe a comparé"),
                   ("Tester l'hypothèse de la recette", "Leur hypothèse était")],
        "example": "La mauvaise recette de mise au point a reproduit la défaillance sur des échantillons "
                   "contrôlés. Alors seulement on l'a appelée la cause.",
        "example_cue": "Ils l'ont donc testée",
        "script": "Voici l'histoire complète. Après le changement de série, vingt-quatre caméras sur huit "
                  "cents ont échoué à la mise au point. Le taux normal était sous un demi pour cent. Farhan "
                  "a bloqué l'ordre de fabrication, et tout ce qui avait été produit depuis le dernier bon "
                  "réglage. L'équipe a comparé les enregistrements des gabarits, les versions de recette et "
                  "les tendances de mise au point. Leur hypothèse était la mauvaise recette de mise au "
                  "point. Ils l'ont donc testée sur des échantillons contrôlés, et elle a reproduit la "
                  "défaillance. Alors seulement ils l'ont appelée la cause. Votre équipe aurait-elle "
                  "attendu ?",
    },
    {
        "key": "p13", "num": 13, "title": "Cas pratique : étiquette non conforme",
        "points": [("Étiquette du carton ≠ appareil à l'intérieur", "Un carton d'enregistreur vidéo"),
                   ("Bloquer la palette, vérifier chaque numéro de série", "L'équipe a bloqué la palette"),
                   ("Tracer les scans et les impressions", "Puis ils ont tracé"),
                   ("Imposer la correspondance série-SKU, enregistrer les contournements", "La solution a donc imposé")],
        "example": "Cause racine : la correspondance MES avait été coupée pendant une panne d'imprimante, et "
                   "personne ne l'avait noté.",
        "example_cue": "La correspondance MES avait été",
        "script": "Voici un deuxième cas, à l'emballage. Un carton d'enregistreur vidéo affichait le "
                  "mauvais SKU. Le produit à l'intérieur fonctionnait parfaitement. Mais le client aurait "
                  "quand même reçu le mauvais article. L'équipe a bloqué la palette, et a vérifié chaque "
                  "numéro de série avec son étiquette. Puis ils ont tracé les scans et les impressions. La "
                  "correspondance MES avait été coupée pendant une panne d'imprimante. Personne ne l'avait "
                  "noté. La solution a donc imposé une correspondance série-SKU avant l'impression, et "
                  "enregistré chaque contournement. Auriez-vous cherché là ?",
    },
    {
        "key": "p14", "num": 14, "title": "Déploiement sur 90 jours",
        "points": [("Piloter d'abord une zone à haut risque", "Commencez par une zone pilote"),
                   ("Jours 1–30 : déclencheurs, niveaux, tableau", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : former les responsables, animer les réunions", "Pendant les trente suivants"),
                   ("Jours 61–90 : auditer, relier au FMEA, étendre", "Pendant les trente derniers")],
        "example": "Déployez le QRQC comme un système d'exploitation, pas comme un formulaire isolé.",
        "example_cue": "déployez le QRQC comme un système d'exploitation",
        "script": "Maintenant, déployez le QRQC comme un système d'exploitation, pas comme un formulaire "
                  "isolé. Commencez par une zone pilote à haut risque, et stabilisez-y la méthode. Pendant "
                  "les trente premiers jours, fixez les déclencheurs, les niveaux et le tableau. Pendant "
                  "les trente suivants, formez vos chefs de ligne et animez les réunions. Pendant les "
                  "trente derniers, auditez les actions, reliez-les au FMEA, et étendez à d'autres lignes. "
                  "Qui est responsable de quoi ?",
    },
    {
        "key": "p15", "num": 15, "title": "Le dossier du problème et les rôles",
        "points": [("Le directeur d'usine parraine", "Le directeur d'usine le parraine"),
                   ("La qualité est responsable de la méthode", "La qualité est responsable de la méthode"),
                   ("La production est responsable de la réaction", "La production est responsable"),
                   ("L'ingénierie est responsable des solutions techniques", "Et l'ingénierie est responsable"),
                   ("Un dossier par problème", "Tenez un dossier")],
        "example": "Le test : quelqu'un pourrait-il reconstituer tout l'événement à partir de votre seul "
                   "dossier ?",
        "example_cue": "Quelqu'un pourrait-il reconstituer",
        "script": "Le directeur d'usine le parraine. La qualité est responsable de la méthode. La "
                  "production est responsable de la réaction immédiate. Et l'ingénierie est responsable des "
                  "solutions techniques. Tenez un dossier par problème. Il contient le problème, les photos "
                  "et la fenêtre suspecte. Il contient le confinement et la réconciliation, les causes, les "
                  "actions et la preuve. Voici le test. Quelqu'un pourrait-il reconstituer tout l'événement "
                  "à partir de votre seul dossier ? Réagissez vite, mais clôturez toujours avec des "
                  "preuves.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Détecter, rendre visible", "icon": "sensor", "with": 0},
        {"label": "Confiner : protéger le client", "icon": "lock", "with": 1},
        {"label": "Cause avec des faits, solution prouvée", "icon": "search", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Réinitialiser le testeur", "sub": "et continuer", "icon": "power"},
            {"label": "Isoler l'ordre de fabrication", "sub": "Le QRQC commence ici", "icon": "lock"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Lieu réel, pièces réelles", "icon": "walk"}, {"label": "Des faits, jamais de reproche", "icon": "search"},
        {"label": "Réagir tout de suite", "icon": "warning"}, {"label": "Le confinement n'est pas la solution", "icon": "lock"}]},
    "p03": {"type": "flow", "items": [
        {"label": "Niveau 1 : ligne ou équipe", "sub": "Arrêter, isoler, enregistrer", "icon": "person", "with": 0},
        {"label": "Niveau 2 : équipe transverse", "sub": "Enquêter et agir", "icon": "gear", "with": 1},
        {"label": "Niveau 3 : direction de l'usine", "sub": "Moyens, le client", "icon": "shield", "with": 2}]},
    "p04": {"type": "timeline", "items": [
        {"label": "Détecter, trouver poste et lot, isoler", "sub": "0–5", "span": 5, "icon": "sensor"},
        {"label": "Prévenir le chef et la qualité, garder des échantillons", "sub": "Ensuite", "span": 8, "icon": "person"},
        {"label": "Trouver le dernier point bon connu", "sub": "Puis", "span": 7, "icon": "search"},
        {"label": "Quarantaine, enregistrement, attribution", "sub": "À 30", "span": 10, "icon": "lock"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Quoi, où, quand, qui", "icon": "search", "with": 0},
        {"label": "Comment détecté, combien", "icon": "count", "with": 1},
        {"label": "Rejets face aux suspects", "icon": "stack", "with": 2}],
        "then": {"type": "stat", "value": 24, "suffix": " / 800", "icon": "camera", "label": "caméras ont échoué à la mise au point",
                 "unit": "De 10 h à midi, juste après un changement de gabarit d'objectif", "with": "example"}},
    "p06": {"type": "icons", "items": [
        {"label": "Trouver le périmètre", "icon": "search"}, {"label": "Le bloquer", "icon": "lock"},
        {"label": "Trier selon le risque", "icon": "test"}, {"label": "Réconcilier", "icon": "count"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "2 000 caméras suspectes", "icon": "stack", "with": "example"},
            {"label": "Bonnes + défaillantes + en attente", "icon": "count", "with": "example"},
            {"label": "= 2 000 : aucune ne manque", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Ouvert", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "En vérification", "icon": "clock", "with": 1},
        {"label": "Prouvé", "sub": "Alors seulement : vert", "icon": "check", "tone": "good", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Nouveaux problèmes", "icon": "warning", "with": "example"},
            {"label": "Confinement", "icon": "lock", "with": "example"},
            {"label": "Actions, escalades", "icon": "sequence", "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Main-d'œuvre", "icon": "person", "with": 2}, {"label": "Machine", "icon": "gear", "with": 2},
        {"label": "Méthode", "icon": "clipboard", "with": 2}, {"label": "Matière", "icon": "box", "with": 2},
        {"label": "Mesure", "icon": "scale", "with": 2}, {"label": "Milieu", "icon": "wave", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "S'est produit + s'est échappé", "icon": "search"}, {"label": "Contrôles techniques", "icon": "key"},
        {"label": "Temps de cycle, sécurité", "icon": "clock"}, {"label": "FMEA, SOP, formation", "icon": "clipboard"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "« Vérifiez le gabarit »", "sub": "Un rappel oral", "icon": "person"},
            {"label": "Scan du gabarit", "sub": "Lié à sa recette approuvée", "icon": "barcode"}]}},
    "p10": {"type": "icons", "items": [
        {"label": "Installé n'est pas prouvé", "icon": "cross", "tone": "bad"}, {"label": "Le mettre à l'épreuve", "icon": "test"},
        {"label": "Sur équipes, modèles", "icon": "sequence"}, {"label": "Chaque unité tranchée", "icon": "check"}],
        "then": {"type": "stat", "value": 10, "suffix": " jours", "icon": "calendar", "label": "de production sans répétition",
                 "unit": "avant que le tableau passe au vert", "with": "example"}},
    "p11": {"type": "icons", "items": [
        {"label": "Temps de réaction", "icon": "clock"}, {"label": "Couverture du confinement", "icon": "count"},
        {"label": "Rendement, taux de défauts", "icon": "chartUp"}, {"label": "Clôture à temps", "icon": "calendar"}],
        "then": {"type": "stat", "value": 5, "suffix": "%", "icon": "warning", "label": "des unités suspectes encore dehors",
                 "unit": "En trouver 95 % n'est pas fini", "with": "example"}},
    "p12": {"type": "flow", "items": [
        {"label": "24 sur 800 échouent à la mise au point", "sub": "Normal : moins de 0,5 %", "icon": "camera", "tone": "bad", "with": 0},
        {"label": "Bloquer depuis le dernier bon réglage", "icon": "lock", "with": 1},
        {"label": "Comparer gabarit, recette, tendance", "icon": "search", "with": 2},
        {"label": "La mauvaise recette l'a reproduite", "sub": "Alors seulement : la cause", "icon": "test", "tone": "good", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Étiquette du carton ≠ appareil", "icon": "label", "tone": "bad", "with": 0},
        {"label": "Bloquer la palette, vérifier les numéros de série", "icon": "lock", "with": 1},
        {"label": "Correspondance MES coupée", "sub": "Pendant une panne d'imprimante, non notée", "icon": "warning", "tone": "bad", "with": "example"},
        {"label": "Correspondance série-SKU imposée", "sub": "Chaque contournement enregistré", "icon": "barcode", "tone": "good", "with": 3}]},
    "p14": {"type": "timeline", "items": [
        {"label": "Déclencheurs, niveaux, tableau", "sub": "Jours 1–30", "icon": "clipboard", "with": 1},
        {"label": "Former les responsables, animer les réunions", "sub": "31–60", "icon": "person", "with": 2},
        {"label": "Auditer, relier au FMEA, étendre", "sub": "61–90", "icon": "chartUp", "with": 3}]},
    "p15": {"type": "icons", "items": [
        {"label": "Directeur d'usine", "sub": "Parraine", "icon": "person"}, {"label": "Qualité", "sub": "La méthode", "icon": "shield"},
        {"label": "Production", "sub": "La réaction", "icon": "wrench"}, {"label": "Ingénierie", "sub": "Les solutions", "icon": "gear"},
        {"label": "Un dossier", "sub": "Chaque problème", "icon": "clipboard"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "1 900 des 2 000 unités suspectes ont été retrouvées et triées. Le confinement est-il "
                    "terminé ?",
        "options": ["Oui — 95 %, c'est suffisant", "Non — 100 unités suspectes ne sont toujours pas retrouvées",
                    "Oui, si la solution est installée"],
        "correct": 1,
        "explanation": "Une couverture de confinement de 95 % veut dire que 5 % de la population suspecte est "
                       "encore dehors. Le confinement n'est terminé que quand chaque unité est retrouvée.",
        "q_script": "Vérification rapide. Mille neuf cents des deux mille unités suspectes ont été retrouvées "
                    "et triées. Le confinement est-il terminé ? Prenez quelques secondes.",
        "a_script": "Non. Cent unités suspectes ne sont toujours pas retrouvées. Le confinement n'est terminé "
                    "que quand chaque unité est retrouvée.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Les échecs de mise au point bondissent au test juste après un changement de gabarit. On "
                    "réinitialise le testeur et il passe. Que faut-il faire EN PREMIER ?",
        "options": ["Continuer — le testeur passe", "Isoler les unités depuis le dernier bon réglage et enregistrer les preuves",
                    "Remettre l'ancien gabarit sans rien dire", "Attendre la réunion de fin de journée"],
        "correct": 1,
        "explanation": "Protégez d'abord le client : bloquez tout depuis le dernier réglage vérifié, gardez "
                       "échantillons et enregistrements, puis enquêtez. Réinitialiser le testeur cache "
                       "l'anomalie.",
        "q_script": "Encore une, et cette fois c'est un scénario. Les échecs de mise au point bondissent "
                    "juste après un changement de gabarit. Quelqu'un réinitialise le testeur, et il passe. "
                    "Que faut-il faire en premier ? Réfléchissez.",
        "a_script": "Isolez chaque unité depuis le dernier bon réglage, et enregistrez les preuves. Puis "
                    "enquêtez. Réinitialiser le testeur ne fait que cacher le problème.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
