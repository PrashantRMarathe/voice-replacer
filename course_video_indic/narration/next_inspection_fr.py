"""next_inspection in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh next_inspection_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ni_fr"
NAME = "next_inspection_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "One Point Lesson": "ouane poïnnte lèsseune",
    "Next Inspection": "nexte inspékchone",
    "Poka Yoke": "Poka Yoké",
    "Pareto": "Paréto",
    "Jidoka": "Djidoka",
    "Andon": "Anndone",
    "FMEA": "effe emme eu a",
    "CTQ": "cé té ku",
    "SOP": "esse o pé",
    "SMT": "esse emme té",
    "PCB": "pé cé bé",
    "MSA": "emme esse a",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Un connecteur mal enfiché, au poste trois. Personne ne l'a remarqué. Il a traversé "
    "quatre postes de plus, le test final et l'emballage. Puis un client a ouvert le carton. "
    "Ça vous dit quelque chose ? Dans cette leçon, vous allez découvrir Next Inspection. Vous "
    "verrez comment chaque processus peut protéger le suivant, et attraper les défauts là où "
    "ils naissent. Nous suivrons Anita, ingénieure qualité sur une ligne de caméras de "
    "sécurité, qui fait exactement cela."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Ne faites pas, ne transmettez pas et n'acceptez pas de "
    "défaut. Contrôlez les points critiques au plus tôt, et réagissez vite. Et continuez à "
    "remonter vos contrôles vers l'amont, vers la prévention. Voici votre action pour cette "
    "semaine. Choisissez un passage de relais sur votre ligne, et notez ce dont le processus "
    "suivant a besoin. Bravo d'avoir terminé cette leçon. Ensuite, vous découvrirez la One "
    "Point Lesson."
)

# One story thread: Anita's security-camera line. Assembly -> firmware -> test ->
# packing. Loose connectors and wrong labels were escaping downstream.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est Next Inspection",
        "points": [("Chaque processus protège le suivant", "chaque processus protège"),
                   ("Confirmer les points critiques avant de transmettre", "Avant de transmettre le travail"),
                   ("Ne pas faire de défaut", "Ne faites pas de défaut"),
                   ("Ne pas transmettre de défaut", "Ne transmettez pas de défaut"),
                   ("Ne pas accepter de défaut", "N'acceptez pas de défaut")],
        "example": "Le poste boîtier d'Anita vérifie maintenant d'abord le verrouillage du connecteur.",
        "example_cue": "Sur la ligne d'Anita",
        "script": "Voici l'idée centrale. Next Inspection veut dire que chaque processus protège le "
                  "suivant. Avant de transmettre le travail, vous confirmez les points critiques. Et le "
                  "poste qui reçoit n'accepte pas un défaut en silence. Il le renvoie aussitôt. Trois "
                  "règles résument tout. Ne faites pas de défaut. Ne transmettez pas de défaut. N'acceptez "
                  "pas de défaut. Sur la ligne d'Anita, le poste boîtier vérifie maintenant d'abord le "
                  "verrouillage du connecteur. Alors, pourquoi est-ce si important ?",
    },
    {
        "key": "p02", "num": 2, "title": "Pourquoi l'attraper tôt",
        "points": [("Les défauts coûtent plus cher à chaque étape", "Un défaut coûte plus cher"),
                   ("Détection précoce = retour rapide", "La détection précoce donne aussi"),
                   ("Plus d'inspection ≠ qualité", "Plus d'inspection ne")],
        "example": "Connecteur mal enfiché : quelques secondes à corriger à l'assemblage → ouvrir, réparer, "
                   "retester après le test → un retour chez le client.",
        "example_cue": "À l'assemblage, un connecteur mal enfiché",
        "script": "Un défaut coûte plus cher à chaque étape qu'il traverse. À l'assemblage, un connecteur "
                  "mal enfiché se corrige en quelques secondes. Après le test, il faut ouvrir le boîtier, "
                  "réparer et retester. Chez le client, c'est un retour, et un coup porté à votre "
                  "réputation. La détection précoce donne aussi un retour rapide. La cause est encore "
                  "fraîche, donc facile à trouver. Mais attention. Plus d'inspection ne crée pas la "
                  "qualité. Alors, où placer les contrôles ?",
    },
    {
        "key": "p03", "num": 3, "title": "Trois niveaux d'inspection",
        "points": [("À la source : vérifier d'abord la condition", "L'inspection à la source vérifie"),
                   ("Autocontrôle : vérifier votre propre travail", "L'autocontrôle veut dire"),
                   ("Processus suivant : vérifier avant d'accepter", "L'inspection par le processus suivant veut dire")],
        "example": "La ligne d'Anita : un capteur vérifie l'orientation, l'assembleur confirme le "
                   "verrouillage, le testeur confirme le modèle.",
        "example_cue": "Sur la ligne d'Anita",
        "script": "Il y a trois niveaux. L'inspection à la source vérifie la condition qui pourrait créer "
                  "le défaut, avant qu'il n'arrive. L'autocontrôle veut dire que vous vérifiez votre propre "
                  "travail, là où vous l'avez fait. L'inspection par le processus suivant veut dire que le "
                  "poste qui reçoit vérifie avant d'accepter. Sur la ligne d'Anita, un capteur vérifie "
                  "l'orientation. L'assembleur confirme le verrouillage. Et le testeur confirme le modèle. "
                  "Quel niveau est le plus fort ? Le plus proche de la source.",
    },
    {
        "key": "p04", "num": 4, "title": "Le processus suivant est mon client",
        "points": [("Le processus suivant est votre client", "Le processus suivant est votre client"),
                   ("Bon produit, quantité, qualité, étiquette, délai", "Il lui faut le bon produit"),
                   ("Ne jamais transmettre sciemment une unité anormale", "Ne transmettez jamais sciemment"),
                   ("Signalez-le par l'Andon", "Signalez-le plutôt par l'Andon")],
        "example": "Les assembleurs d'Anita ont demandé à l'équipe firmware : de quoi avez-vous besoin de "
                   "notre part ?",
        "example_cue": "Les assembleurs d'Anita ont simplement demandé",
        "script": "Voyez chaque passage de relais comme une vente. Le processus suivant est votre client. "
                  "Il lui faut le bon produit, la bonne quantité et la bonne qualité, et la bonne étiquette "
                  "au bon moment. Alors suivez le SOP, et confirmez vos points critiques. Ne transmettez "
                  "jamais sciemment une unité anormale. Signalez-le plutôt par l'Andon. Les assembleurs "
                  "d'Anita ont simplement demandé à l'équipe firmware, de quoi avez-vous besoin de notre "
                  "part ? Avez-vous déjà posé cette question à votre processus suivant ?",
    },
    {
        "key": "p05", "num": 5, "title": "Les responsables le rendent réel",
        "points": [("Les responsables soutiennent quiconque arrête pour la qualité", "Les responsables doivent soutenir"),
                   ("Réagir vite quand on les appelle", "Ils doivent réagir"),
                   ("Enregistrer les défauts pour apprendre, jamais pour blâmer", "Et les défauts doivent être enregistrés")],
        "example": "Une opératrice a arrêté la ligne d'Anita pour une lentille fêlée — son responsable l'a "
                   "remerciée devant l'équipe.",
        "example_cue": "Quand une opératrice a arrêté",
        "script": "Voici ce qui fait réussir ou échouer Next Inspection. Vos responsables. Si les gens sont "
                  "poussés à continuer malgré un problème, les contrôles deviennent des cases à cocher. Les "
                  "responsables doivent soutenir quiconque arrête pour la qualité. Ils doivent réagir vite "
                  "quand on les appelle. Et les défauts doivent être enregistrés pour apprendre, jamais "
                  "pour blâmer. Quand une opératrice a arrêté la ligne d'Anita pour une lentille fêlée, son "
                  "responsable l'a remerciée devant l'équipe. Que se passerait-il sur votre ligne ?",
    },
    {
        "key": "p06", "num": 6, "title": "Choisir quoi inspecter",
        "points": [("Choisir les contrôles selon le risque", "Alors choisissez selon le risque"),
                   ("CTQ client : fonction, sécurité, ajustement", "Commencez par ce que votre client"),
                   ("FMEA et fuites répétées", "Puis regardez votre FMEA"),
                   ("Où une mauvaise pièce ou étiquette peut-elle se glisser ?", "Demandez où une mauvaise pièce")],
        "example": "Anita en a choisi quatre : verrouillage du connecteur, version du firmware, joint du "
                   "boîtier et étiquette.",
        "example_cue": "Anita en a choisi quatre",
        "script": "Vous ne pouvez pas tout vérifier avec le même soin. Alors choisissez selon le risque. "
                  "Commencez par ce que votre client ressent, comme la fonction, la sécurité et "
                  "l'ajustement. Ce sont vos points CTQ. Puis regardez votre FMEA, et les défauts qui "
                  "continuent de s'échapper. Demandez où une mauvaise pièce, un mauvais réglage ou une "
                  "mauvaise étiquette pourraient se glisser. Anita en a choisi quatre : verrouillage du "
                  "connecteur, version du firmware, joint du boîtier et étiquette. Pour les risques élevés, "
                  "préférez la prévention à un contrôle visuel. Alors, comment construire une bonne porte ?",
    },
    {
        "key": "p07", "num": 7, "title": "Concevoir une porte d'inspection",
        "points": [("Définir le bon et le mauvais, avec des échantillons", "D'abord, définissez à quoi"),
                   ("Choisir la méthode", "Puis choisissez la méthode"),
                   ("Fixer la fréquence de contrôle", "Fixez la fréquence de contrôle"),
                   ("Décider la réaction à l'avance", "Et décidez la réaction")],
        "example": "La porte du joint d'Anita : des échantillons limites sur l'établi et un bac rouge pour "
                   "les rejets.",
        "example_cue": "La porte du joint d'Anita",
        "script": "Une bonne porte est rapide, claire et difficile à contourner. D'abord, définissez à quoi "
                  "ressemblent le bon et le mauvais, avec des échantillons limites quand c'est possible. "
                  "Puis choisissez la méthode, une jauge, un capteur, un scan ou un contrôle visuel. Fixez "
                  "la fréquence de contrôle. Et décidez la réaction avant qu'un défaut n'apparaisse. La "
                  "porte du joint d'Anita a des échantillons sur l'établi, et un bac rouge pour les rejets. "
                  "Alors, que se passe-t-il quand la porte trouve quelque chose ?",
    },
    {
        "key": "p08", "num": 8, "title": "Le plan de réaction",
        "points": [("Arrêter ou signaler par l'Andon", "Arrêtez ou signalez par l'Andon"),
                   ("Identifier le défaut, le modèle, le numéro de série", "Identifiez le défaut"),
                   ("Confiner jusqu'à la dernière bonne unité", "Confinez chaque unité"),
                   ("Corriger, vérifier, prévenir", "Corrigez le processus")],
        "example": "Mauvais firmware au test : chaque unité depuis le dernier bon contrôle a été bloquée.",
        "example_cue": "Quand le testeur d'Anita a trouvé",
        "script": "Vous réagissez, vite et dans l'ordre. Arrêtez ou signalez par l'Andon. Identifiez le "
                  "défaut, le modèle et le numéro de série. Confinez chaque unité jusqu'à la dernière bonne "
                  "connue. Corrigez le processus, et vérifiez la première bonne unité avant de redémarrer. "
                  "Puis trouvez la cause racine, et empêchez son retour. Quand le testeur d'Anita a trouvé "
                  "un mauvais firmware, chaque unité depuis le dernier bon contrôle a été bloquée. Un plan "
                  "vague, c'est du retard et des stocks mélangés.",
    },
    {
        "key": "p09", "num": 9, "title": "Les outils Lean qui aident",
        "points": [("Le Poka Yoke arrête la mauvaise pièce ou la mauvaise étape", "Le Poka Yoke empêche"),
                   ("Jidoka et Andon arrêtent et appellent à l'aide", "Jidoka et Andon"),
                   ("Le travail standard rend le bon et le mauvais évidents", "Le travail standard et les standards visuels"),
                   ("Le FMEA définit les risques, les audits vérifient les contrôles", "Votre FMEA définit")],
        "example": "Anita a remplacé un contrôle visuel d'étiquette par une correspondance au scan — la "
                   "mauvaise étiquette ne peut plus s'imprimer.",
        "example_cue": "Anita a remplacé un contrôle visuel",
        "script": "Next Inspection fonctionne mieux avec d'autres outils Lean. Le Poka Yoke empêche même la "
                  "mauvaise pièce ou la mauvaise étape de se produire. Jidoka et Andon arrêtent la ligne et "
                  "appellent à l'aide. Le travail standard et les standards visuels rendent le bon et le "
                  "mauvais évidents. Votre FMEA définit les risques, et les audits vérifient que les "
                  "contrôles sont vraiment appliqués. Anita a remplacé un contrôle visuel d'étiquette par "
                  "une correspondance au scan. Maintenant, la mauvaise étiquette ne peut tout simplement "
                  "plus s'imprimer. Où cela pourrait-il marcher ailleurs ?",
    },
    {
        "key": "p10", "num": 10, "title": "Exemples en électronique",
        "points": [("SMT : inspection optique, chargeurs vérifiés", "En SMT"),
                   ("Assemblage : code-barres du PCB, compteur de vis", "À l'assemblage"),
                   ("Firmware : verrouillage de version", "Au firmware"),
                   ("Emballage : contrôle de poids et scans", "À l'emballage")],
        "example": "Chaque contrôle se place juste après l'étape qu'il protège. L'inspection finale est le "
                   "dernier filet de sécurité.",
        "example_cue": "Chaque contrôle se place juste après",
        "script": "Parcourons la ligne. En SMT, l'inspection optique automatique vérifie les cartes, et les "
                  "chargeurs sont vérifiés. À l'assemblage, un code-barres confirme le bon PCB, et un "
                  "compteur confirme chaque vis. Au firmware, un verrouillage vérifie la version avant la "
                  "libération. À l'emballage, un contrôle de poids et des scans attrapent un accessoire "
                  "manquant. Remarquez la logique. Chaque contrôle se place juste après l'étape qu'il "
                  "protège. Et l'inspection finale ? C'est votre dernier filet de sécurité, pas votre "
                  "système qualité.",
    },
    {
        "key": "p11", "num": 11, "title": "La qualité à la source",
        "points": [("L'amont fabrique au standard", "L'amont fabrique au standard"),
                   ("L'aval n'accepte que du bon", "L'aval n'accepte"),
                   ("Les problèmes retournent au poste qui les a créés", "Tout problème retourne directement"),
                   ("Attention au piège de l'inspection", "attention au piège de l'inspection")],
        "example": "La ligne d'Anita avait autrefois un contrôleur après chaque poste. Elle en a affecté "
                   "trois à des projets de prévention.",
        "example_cue": "La ligne d'Anita fonctionnait autrefois",
        "script": "Next Inspection soutient la qualité à la source. L'amont fabrique au standard. L'aval "
                  "n'accepte que du bon. Tout problème retourne directement au poste qui l'a créé, et la "
                  "cause est corrigée. Maintenant, attention au piège de l'inspection. Ajouter un "
                  "contrôleur après chaque poste coûte cher, et cache des processus faibles. La ligne "
                  "d'Anita fonctionnait autrefois ainsi. Elle a plutôt affecté trois contrôleurs à des "
                  "projets de prévention. Pouvez-vous faire confiance aux contrôles qui restent ?",
    },
    {
        "key": "p12", "num": 12, "title": "Pouvez-vous faire confiance au contrôle ?",
        "points": [("Les fausses acceptations laissent passer des défauts", "Une fausse acceptation"),
                   ("Les faux rejets poussent au contournement", "Un faux rejet"),
                   ("Définitions claires, photos, échantillons limites", "Alors définissez clairement les défauts"),
                   ("Former les contrôleurs", "Formez les personnes qui contrôlent"),
                   ("Étalonner les jauges, faire une MSA", "Étalonnez les jauges"),
                   ("Maîtriser l'éclairage et la distance de vue", "Maîtrisez l'éclairage")],
        "example": "Les deux contrôleurs d'Anita n'étaient pas d'accord sur un joint sur cinq. De meilleurs "
                   "échantillons l'ont corrigé.",
        "example_cue": "Les deux contrôleurs d'Anita",
        "script": "Un contrôle n'est utile que si vous pouvez lui faire confiance. Une fausse acceptation "
                  "laisse passer un défaut. Un faux rejet crée des retouches inutiles, et les gens "
                  "commencent à contourner le contrôle. Alors définissez clairement les défauts, avec des "
                  "photos et des échantillons limites. Formez les personnes qui contrôlent. Étalonnez les "
                  "jauges, et faites une étude de mesure, appelée MSA. Maîtrisez l'éclairage et la distance "
                  "de vue. Les deux contrôleurs d'Anita n'étaient pas d'accord sur un joint sur cinq. De "
                  "meilleurs échantillons l'ont corrigé. Alors, comment mesurer le succès ?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI pour Next Inspection",
        "points": [("Rendement au premier passage en hausse", "Le rendement au premier passage doit monter"),
                   ("Taux de fuite en baisse", "Le taux de fuite doit baisser"),
                   ("Retouches, défauts répétés, temps de réaction", "Surveillez votre taux de retouche"),
                   ("Fausses alertes suivies", "Et suivez les fausses alertes")],
        "example": "Le rendement monte pendant que l'effort d'inspection baisse = vous gagnez.",
        "example_cue": "Si le rendement monte",
        "script": "Suivez un ensemble équilibré de chiffres. Le rendement au premier passage doit monter. "
                  "Le taux de fuite doit baisser. Ce sont les défauts trouvés en aval qui auraient dû être "
                  "attrapés plus tôt. Surveillez votre taux de retouche et les défauts répétés. Mesurez le "
                  "temps de réaction de la détection, du signal au confinement. Et suivez les fausses "
                  "alertes, pour savoir que vos contrôles sont fiables. Si le rendement monte pendant que "
                  "l'effort d'inspection baisse, vous gagnez. Prêt à voir les résultats d'Anita ?",
    },
    {
        "key": "p14", "num": 14, "title": "Cas pratique : ligne de caméras",
        "points": [("Contrôles de passage de relais sur 4 points à risque", "Elle a placé des contrôles"),
                   ("Plan de réaction affiché à chaque porte", "Chaque porte a reçu"),
                   ("Les contrôles de joint et d'étiquette sont devenus des verrouillages", "Les contrôles de joint et d'étiquette"),
                   ("Revue hebdomadaire des fuites avec la source", "Et chaque semaine")],
        "example": "Après 8 semaines : fuites de 18 à 3 par semaine, retouches réduites de plus de moitié, "
                   "rendement au premier passage de 98,5 %.",
        "example_cue": "Après huit semaines",
        "script": "Voici ce qu'a fait Anita. Elle a placé des contrôles de passage de relais sur quatre "
                  "points à risque. Chaque porte a reçu un plan de réaction affiché. Les contrôles de joint "
                  "et d'étiquette sont devenus des verrouillages. Et chaque semaine, elle a revu chaque "
                  "fuite avec le poste qui l'avait créée. Après huit semaines, les fuites sont passées de "
                  "dix-huit par semaine à trois. Les retouches ont baissé de plus de moitié. Le rendement "
                  "au premier passage est monté à quatre-vingt-dix-huit et demi pour cent. Comment le "
                  "déploieriez-vous ?",
    },
    {
        "key": "p15", "num": 15, "title": "Feuille de route et check-list quotidienne",
        "points": [("Choisir par risque et Pareto, cartographier le flux", "Choisissez un produit selon le risque et un Pareto"),
                   ("Concevoir des contrôles avec des plans de réaction", "Concevez les contrôles"),
                   ("Piloter une ligne, comparer avant / après", "Faites un pilote sur une ligne"),
                   ("Standardiser SOP, FMEA, formation", "Puis standardisez le SOP")],
        "example": "Questions quotidiennes : les critères sont-ils visibles ? Vos opérateurs savent-ils "
                   "expliquer le plan de réaction ?",
        "example_cue": "Chaque jour, posez des questions simples",
        "script": "Déployez-le étape par étape. Choisissez un produit selon le risque et un Pareto. "
                  "Cartographiez le flux, et listez les points critiques. Concevez les contrôles à la "
                  "source, les autocontrôles et ceux du processus suivant, avec des plans de réaction. "
                  "Faites un pilote sur une ligne, et comparez avant et après. Puis standardisez le SOP, le "
                  "FMEA et la formation. Chaque jour, posez des questions simples. Les critères sont-ils "
                  "visibles ? Vos opérateurs savent-ils expliquer le plan de réaction ? Protégez le "
                  "processus suivant, à chaque fois.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Ne faites pas", "sub": "de défaut", "icon": "wrench", "with": 2},
        {"label": "Ne transmettez pas", "sub": "de défaut", "icon": "lock", "with": 3},
        {"label": "N'acceptez pas", "sub": "de défaut", "icon": "shield", "with": 4}]},
    "p02": {"type": "flow", "items": [
        {"label": "À l'assemblage", "sub": "Quelques secondes à corriger", "icon": "wrench", "tone": "good", "with": "example"},
        {"label": "Après le test", "sub": "Ouvrir, réparer, retester", "icon": "test", "with": "example"},
        {"label": "Chez le client", "sub": "Un retour, et un coup à votre réputation", "icon": "box", "tone": "bad", "with": "example"}]},
    "p03": {"type": "ladder", "top": "LE PLUS FORT : LE PLUS PRÈS DE LA SOURCE", "bottom": "DERNIÈRE LIGNE DE DÉFENSE", "items": [
        {"label": "Source", "icon": "sensor"}, {"label": "Autocontrôle", "icon": "hand"},
        {"label": "Processus suivant", "icon": "search"}]},
    "p04": {"type": "flow", "items": [
        {"label": "Votre poste", "sub": "Suivre le SOP", "icon": "wrench", "with": 0},
        {"label": "Vérifier les points critiques", "sub": "Produit, quantité, étiquette, délai", "icon": "check", "with": 1},
        {"label": "Processus suivant", "sub": "Votre client", "icon": "person", "tone": "good", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Soutenir l'arrêt", "icon": "shield"}, {"label": "Réagir vite", "icon": "clock"},
        {"label": "Apprendre, jamais blâmer", "icon": "person", "tone": "good"}]},
    "p06": {"type": "icons", "items": [
        {"label": "CTQ client", "sub": "Fonction, sécurité, ajustement", "icon": "person", "with": 1},
        {"label": "FMEA + fuites", "sub": "Ce qui continue de s'échapper", "icon": "clipboard", "with": 2},
        {"label": "Points où ça se glisse", "sub": "Mauvaise pièce, réglage, étiquette", "icon": "label", "with": 3}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Verrouillage du connecteur", "icon": "lock", "with": "example"},
            {"label": "Version du firmware", "icon": "chip", "with": "example"},
            {"label": "Joint du boîtier", "icon": "shield", "with": "example"},
            {"label": "Étiquette", "icon": "label", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Échantillons bons et mauvais", "icon": "shape"}, {"label": "La méthode", "icon": "sensor"},
        {"label": "La fréquence", "icon": "clock"}, {"label": "La réaction", "icon": "warning"}]},
    "p08": {"type": "flow", "items": [
        {"label": "Arrêter : Andon", "icon": "warning", "tone": "bad"},
        {"label": "Identifier", "sub": "Défaut, modèle, numéro de série", "icon": "search"},
        {"label": "Confiner", "sub": "Jusqu'à la dernière bonne unité", "icon": "lock"},
        {"label": "Corriger, vérifier, prévenir", "icon": "check", "tone": "good"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Poka Yoke", "icon": "key"}, {"label": "Jidoka + Andon", "icon": "warning"},
        {"label": "Travail standard", "icon": "clipboard"}, {"label": "FMEA + audits", "icon": "shield"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Contrôle visuel d'étiquette", "sub": "Facile à rater", "icon": "search"},
            {"label": "Correspondance au scan", "sub": "La mauvaise étiquette ne peut pas s'imprimer", "icon": "barcode"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "SMT", "sub": "Inspection optique, chargeurs vérifiés", "icon": "chip"},
        {"label": "Assemblage", "sub": "Code-barres du PCB, compteur de vis", "icon": "barcode"},
        {"label": "Firmware", "sub": "Verrouillage de version", "icon": "lock"},
        {"label": "Emballage", "sub": "Contrôle de poids et scans", "icon": "scale"}]},
    "p11": {"type": "flow", "items": [
        {"label": "L'amont fabrique au standard", "icon": "wrench", "with": 0},
        {"label": "L'aval n'accepte que du bon", "icon": "check", "with": 1},
        {"label": "Les problèmes retournent à la source", "icon": "sequence", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Un contrôleur après chaque poste", "sub": "Coûteux ; cache des processus faibles", "icon": "person"},
            {"label": "3 affectés à la prévention", "sub": "La qualité à la source", "icon": "shield"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Fausse acceptation", "icon": "cross", "tone": "bad"}, {"label": "Faux rejet", "icon": "warning", "tone": "bad"},
        {"label": "Définitions claires", "icon": "clipboard"}, {"label": "Contrôleurs formés", "icon": "person"},
        {"label": "Étalonner, MSA", "icon": "gear"}, {"label": "Éclairage", "icon": "sensor"}],
        "then": {"type": "stat", "value": 5, "prefix": "1 / ", "icon": "search", "label": "joints sur lesquels les deux contrôleurs n'étaient pas d'accord",
                 "unit": "De meilleurs échantillons limites l'ont corrigé", "with": "example"}},
    "p13": {"type": "icons", "items": [
        {"label": "Rendement au premier passage", "sub": "En hausse", "icon": "chartUp", "tone": "good"},
        {"label": "Taux de fuite", "sub": "En baisse", "icon": "chartDown", "tone": "good"},
        {"label": "Retouches, temps de réaction", "icon": "clock"},
        {"label": "Fausses alertes", "icon": "warning"}]},
    "p14": {"type": "flow", "items": [
        {"label": "Contrôles sur 4 points à risque", "icon": "search", "tone": "good"},
        {"label": "Plan de réaction à chaque porte", "icon": "clipboard", "tone": "good"},
        {"label": "Verrouillages joint + étiquette", "icon": "lock", "tone": "good"},
        {"label": "Revue hebdomadaire des fuites", "icon": "calendar", "tone": "good"}],
        "then": {"type": "compare", "before": {"label": "Avant", "value": 18}, "after": {"label": "Après 8 semaines", "value": 3},
                 "unit": "fuites par semaine", "note": "Rendement au premier passage de 98,5 %", "with": "example"}},
    "p15": {"type": "steps", "items": [
        {"label": "Choisir par risque", "with": 0}, {"label": "Cartographier le flux", "with": 0},
        {"label": "Concevoir les contrôles", "with": 1}, {"label": "Pilote sur une ligne", "with": 2},
        {"label": "Standardiser", "with": 3}, {"label": "Demander chaque jour", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un capteur empêche la mauvaise orientation du connecteur avant le montage de la pièce. "
                    "Quel niveau d'inspection est-ce ?",
        "options": ["Inspection à la source", "Autocontrôle", "Inspection par le processus suivant"],
        "correct": 0,
        "explanation": "Il vérifie la condition qui créerait le défaut, avant qu'il n'arrive. C'est l'inspection "
                       "à la source — le niveau le plus fort.",
        "q_script": "Vérification rapide. Un capteur empêche la mauvaise orientation du connecteur avant même "
                    "le montage de la pièce. Quel niveau d'inspection est-ce ? Prenez quelques secondes.",
        "a_script": "C'est l'inspection à la source. Elle vérifie la condition avant que le défaut ne puisse "
                    "arriver. C'est le niveau le plus fort.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Le test trouve sans cesse le même connecteur mal enfiché venant de l'assemblage, alors "
                    "un responsable ajoute un contrôleur après l'assemblage. Quelle est la meilleure option ?",
        "options": ["Ajouter un deuxième contrôleur par sécurité", "Garder le contrôleur et corriger aussi la cause à l'assemblage",
                    "Supprimer tous les contrôles pour économiser", "Demander au test d'arrêter de le signaler"],
        "correct": 1,
        "explanation": "Un contrôleur supplémentaire peut contenir le risque pour l'instant, mais un défaut "
                       "répété veut dire qu'il faut corriger le processus à la source — puis le contrôle "
                       "temporaire peut être retiré.",
        "q_script": "Encore une, et cette fois c'est un scénario. Le test trouve sans cesse le même "
                    "connecteur mal enfiché venant de l'assemblage. Un responsable ajoute un contrôleur après "
                    "l'assemblage. Quelle est la meilleure option ? Réfléchissez.",
        "a_script": "Gardez le contrôle pour l'instant, mais corrigez la cause à l'assemblage. Un défaut "
                    "répété veut dire que le processus doit s'améliorer à la source. Ensuite, le contrôle "
                    "supplémentaire peut partir.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
