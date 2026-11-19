"""jidoka in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh jidoka_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "jd_fr"
NAME = "jidoka_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Sakichi Toyoda": "Sakitchi Toyoda",
    "Poka Yoke": "Poka Yoké",
    "Jidoka": "Djidoka",
    "Kaizen": "Kaïzène",
    "Andon": "Anndone",
    "PFMEA": "pé effe emme eu a",
    "SOP": "esse o pé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Le doseur a parfaitement tourné toute la nuit. Sauf que sa buse était à moitié bouchée. "
    "Au matin, cent quarante moniteurs patient avaient un joint trop fin. Ça vous dit quelque "
    "chose ? Dans cette leçon, vous allez découvrir le Jidoka, l'automatisation à visage "
    "humain. Vous verrez comment faire en sorte qu'un processus repère un problème, s'arrête "
    "de lui-même, et appelle à l'aide, avant que les défauts s'accumulent. Nous suivrons "
    "Anjali, ingénieure procédés sur une ligne de moniteurs patient."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Définissez d'abord le normal, pour que le processus sache "
    "à quoi ressemble l'anormal. Détectez, arrêtez et confinez à la source, et ne transmettez "
    "jamais un défaut. Et traitez chaque arrêt comme une leçon, en corrigeant la cause racine "
    "pour qu'il ne se répète pas. Voici votre action pour cette semaine. Choisissez un "
    "processus automatique, et notez ce qui devrait le faire s'arrêter. Bravo d'avoir terminé "
    "cette leçon. Ensuite, vous découvrirez le Kaizen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le Jidoka",
        "points": [("Détecter une anomalie", "détecte une condition anormale"),
                   ("Arrêter ou confiner", "arrête ou confine"),
                   ("Corriger, puis prévenir", "Puis les personnes corrigent")],
        "example": "Le doseur d'Anjali scelle le cadre avant de chaque moniteur patient.",
        "example_cue": "Le défi d'Anjali",
        "script": "On appelle souvent le Jidoka l'automatisation à visage humain. Il désigne un processus "
                  "qui détecte une condition anormale de lui-même. Il arrête ou confine le travail, pour "
                  "qu'aucun défaut n'avance. Puis les personnes corrigent, et empêchent que cela se "
                  "reproduise. Le défi d'Anjali était un doseur de colle. Il scelle le cadre avant de "
                  "chaque moniteur patient. Alors, qu'est-ce qui change quand vous ajoutez le Jidoka ?",
    },
    {
        "key": "p02", "num": 2, "title": "Sans et avec le Jidoka",
        "points": [("Les défauts voyagent ou sont attrapés à la source", "Sans Jidoka, un défaut"),
                   ("Hésitation ou règles d'arrêt claires", "les gens hésitent"),
                   ("Inspection ou qualité intégrée", "la qualité dépend")],
        "example": "Sans lui : 140 joints trop fins, trouvés au test d'étanchéité le lendemain matin.",
        "example_cue": "Sans lui",
        "script": "Sans Jidoka, un défaut peut traverser de nombreux postes avant que quelqu'un le voie. "
                  "Les gens hésitent à arrêter, parce que personne ne leur a dit qu'ils pouvaient. Le tri "
                  "devient une routine, et la qualité dépend de l'inspection finale. Avec le Jidoka, il est "
                  "attrapé près de la source. Les règles d'arrêt sont claires, et la qualité est intégrée "
                  "au processus. Sans lui, Anjali a trouvé cent quarante joints trop fins le lendemain "
                  "matin. Où cette idée est-elle née ?",
    },
    {
        "key": "p03", "num": 3, "title": "D'où il vient",
        "points": [("Le métier à tisser automatique de Sakichi Toyoda", "Il remonte au métier de Sakichi Toyoda"),
                   ("Il s'arrêtait quand un fil cassait", "s'arrêtait de lui-même"),
                   ("Un des deux piliers du TPS", "deux piliers")],
        "example": "Le juste-à-temps déplace bien la matière. Le Jidoka garantit qu'il ne déplace pas bien "
                   "les défauts.",
        "example_cue": "Voici le lien",
        "script": "Il remonte au métier de Sakichi Toyoda. L'astuce n'était pas la vitesse. Le métier "
                  "s'arrêtait de lui-même chaque fois qu'un fil cassait, au lieu de tisser du mauvais "
                  "tissu. Cette idée est devenue un des deux piliers du système de production Toyota. Voici "
                  "le lien. Le juste-à-temps déplace la matière efficacement. Le Jidoka garantit que vous "
                  "ne déplacez pas les défauts efficacement. Cela veut-il dire moins de personnes ?",
    },
    {
        "key": "p04", "num": 4, "title": "Les personnes comptent toujours",
        "points": [("Les machines surveillent, les personnes réfléchissent", "Les machines surveillent"),
                   ("Une personne peut s'occuper de plusieurs machines", "une personne peut"),
                   ("Jugement, réparation, amélioration", "au jugement")],
        "example": "L'opératrice d'Anjali fixait le cordon toute l'équipe. Elle tient maintenant deux "
                   "postes.",
        "example_cue": "L'opératrice d'Anjali",
        "script": "Non. Le Jidoka ne supprime pas les personnes. Les machines surveillent, et les personnes "
                  "réfléchissent. Comme la machine signale quand elle a besoin d'aide, une personne peut "
                  "s'occuper de plusieurs machines. Son temps va au jugement, à la réparation, aux "
                  "standards et à l'amélioration. L'opératrice d'Anjali fixait le cordon de colle toute "
                  "l'équipe. Elle tient maintenant deux postes, et résout des problèmes. Comment fonctionne "
                  "le cycle ?",
    },
    {
        "key": "p05", "num": 5, "title": "Étape 1 : détecter",
        "points": [("Définir d'abord le normal", "définir le normal"),
                   ("Puis détecter l'écart", "détectez quand"),
                   ("Capteurs, contrôles, tests, surveillance", "Capteurs, vision")],
        "example": "Cordon normal : de 2,0 à 2,4 mm de large, sans trou.",
        "example_cue": "Pour Anjali",
        "script": "Le cycle a quatre étapes. Détecter, arrêter, corriger et prévenir. La détection demande "
                  "d'abord une chose. Vous devez définir le normal. Vous ne pouvez pas détecter l'anormal "
                  "tant que vous ne savez pas à quoi ressemble le bon. Puis vous détectez quand le "
                  "processus s'en écarte. Capteurs, vision, tests, surveillance du couple et contrôles "
                  "opérateur peuvent tous le faire. Pour Anjali, le normal était un cordon de deux à deux "
                  "virgule quatre millimètres de large, sans trou. Et ensuite ?",
    },
    {
        "key": "p06", "num": 6, "title": "Étapes 2 à 4 : arrêter, corriger, prévenir",
        "points": [("Arrêter ou confiner selon le risque", "Arrêtez ou confinez"),
                   ("Corriger : rétablir le standard", "Corriger veut dire"),
                   ("Prévenir : supprimer la cause racine", "Prévenir veut dire")],
        "example": "Corriger n'est pas prévenir. Une buse nettoyée peut se reboucher.",
        "example_cue": "Retenez ceci",
        "script": "Arrêtez ou confinez, d'une façon adaptée au risque. Cela peut être un arrêt machine, un "
                  "verrouillage de poste, une unité bloquée, ou une transaction bloquée. Corriger veut dire "
                  "rétablir le standard approuvé, et retrouver le produit touché. Prévenir veut dire "
                  "supprimer la cause racine, et mettre à jour le standard. Retenez ceci. Corriger n'est "
                  "pas prévenir. Une buse nettoyée peut se reboucher demain. Alors, en quoi est-ce "
                  "différent de l'automatisation ?",
    },
    {
        "key": "p07", "num": 7, "title": "Jidoka ou simple automatisation",
        "points": [("L'automatisation fait le travail", "La simple automatisation"),
                   ("Le Jidoka juge aussi le travail", "Le Jidoka ajoute"),
                   ("Des machines rapides font des défauts rapides", "une machine rapide")],
        "example": "Le doseur d'Anjali : entièrement automatique, mais aveugle. Il a dosé toute la nuit.",
        "example_cue": "Le doseur d'Anjali",
        "script": "La simple automatisation fait le travail. Le Jidoka ajoute un jugement sur le travail. "
                  "Une machine normale continue de tourner, sauf si quelque chose se bloque physiquement. "
                  "Une machine avec Jidoka s'arrête quand elle voit une anomalie définie, et appelle une "
                  "personne. Et voici le danger. Une machine rapide fait des défauts rapidement. Le doseur "
                  "d'Anjali était entièrement automatique, mais aveugle. Il a dosé des cordons trop fins "
                  "toute la nuit. Quels principes doivent vous guider ?",
    },
    {
        "key": "p08", "num": 8, "title": "Principes clés",
        "points": [("Aucun défaut transmis", "Aucun défaut transmis"),
                   ("Aucune anomalie cachée", "Aucune anomalie cachée"),
                   ("Aucune répétition acceptée sans action", "Aucun problème répété")],
        "example": "Trois questions : quel est le normal ? Comment détecter un écart ? Que se passe-t-il "
                   "ensuite ?",
        "example_cue": "Posez trois questions",
        "script": "Retenez trois règles courtes. Aucun défaut transmis. Aucune anomalie cachée. Aucun "
                  "problème répété accepté sans action. Utilisez ensemble la détection machine et le "
                  "jugement humain. Et ne redémarrez jamais sans avoir appris quelque chose. Chaque arrêt "
                  "doit laisser le processus un peu plus solide. Posez trois questions sur n'importe quel "
                  "processus. Quel est le normal ? Comment détecterons-nous un écart ? Et que se passe-t-il "
                  "exactement après la détection ? Savez-vous y répondre pour votre ligne ?",
    },
    {
        "key": "p09", "num": 9, "title": "Andon",
        "points": [("Vert : normal", "Vert veut dire"),
                   ("Jaune : besoin d'aide", "Jaune veut dire"),
                   ("Rouge : arrêter, confiner, escalader", "Rouge veut dire")],
        "example": "La règle d'Anjali : le chef d'équipe répond à un jaune en moins de deux minutes.",
        "example_cue": "Sur la ligne d'Anjali",
        "script": "L'Andon rend les problèmes visibles, avec des lumières, des sons ou des écrans. Vert "
                  "veut dire normal, donc on continue au standard. Jaune veut dire qu'il faut de l'aide, et "
                  "un responsable arrive vite. Rouge veut dire une anomalie critique. Arrêtez en sécurité, "
                  "confinez, et escaladez. Puis retrouvez la dernière bonne unité connue. Sur la ligne "
                  "d'Anjali, le chef d'équipe répond à tout jaune en moins de deux minutes. À quelle "
                  "vitesse l'aide arrive-t-elle sur votre ligne ?",
    },
    {
        "key": "p10", "num": 10, "title": "Une culture de l'Andon",
        "points": [("Un appel est une information utile", "Un véritable appel Andon"),
                   ("Ne jamais sanctionner un arrêt", "Ne sanctionnez jamais"),
                   ("Les appels peuvent d'abord augmenter", "les appels augmentent souvent")],
        "example": "Les appels Andon ont doublé le premier mois, puis ont été divisés par deux au troisième.",
        "example_cue": "Sur la ligne d'Anjali",
        "script": "L'Andon ne marche que si les gens lui font confiance. Un véritable appel Andon est une "
                  "information utile, pas une gêne. Ne sanctionnez jamais un arrêt, sinon les gens "
                  "cacheront les problèmes pour protéger la production. Et attendez-vous à une surprise. "
                  "Quand les problèmes deviennent visibles, les appels augmentent souvent au début. Sur la "
                  "ligne d'Anjali, les appels Andon ont doublé le premier mois. Au troisième mois, ils "
                  "avaient été divisés par deux, parce que les causes étaient corrigées. Votre équipe "
                  "appellerait-elle ?",
    },
    {
        "key": "p11", "num": 11, "title": "Les contrôles les plus forts d'abord",
        "points": [("Éliminer, ou empêcher par la conception", "D'abord, éliminez"),
                   ("Détecter et arrêter immédiatement", "Ensuite, détectez"),
                   ("Avertissements et inspection en dernier", "Les avertissements viennent")],
        "example": "Un bon Poka Yoke : simple, près de la source, difficile à contourner, facile à tester.",
        "example_cue": "Un bon Poka Yoke",
        "script": "Utilisez le contrôle le plus fort possible. D'abord, éliminez le risque d'erreur, ou "
                  "empêchez-le par la conception. Ensuite, détectez l'erreur et arrêtez immédiatement. Les "
                  "avertissements viennent après, et l'inspection en aval seulement comme défense "
                  "supplémentaire. Un bon Poka Yoke est simple, près de la source, et difficile à "
                  "contourner. Et il est facile à tester à chaque équipe. Alors, qu'a construit Anjali ?",
    },
    {
        "key": "p12", "num": 12, "title": "Le poste Jidoka d'Anjali",
        "points": [("Un capteur mesure chaque cordon", "mesure chaque cordon"),
                   ("Hors limites : le doseur s'arrête", "le doseur s'arrête"),
                   ("Andon, et blocage jusqu'à la dernière bonne unité", "L'Andon appelle")],
        "example": "Premier vrai arrêt : un moniteur touché, pas 140.",
        "example_cue": "Son premier vrai arrêt",
        "script": "Elle a ajouté un capteur de vision qui mesure chaque cordon, juste après le dosage. Si "
                  "la largeur sort des limites, le doseur s'arrête, et l'unité est bloquée. L'Andon appelle "
                  "le chef d'équipe. Tout ce qui a été fait depuis la dernière bonne unité est vérifié. Son "
                  "premier vrai arrêt est arrivé deux semaines plus tard. Un moniteur a été touché, pas "
                  "cent quarante. Mais pourquoi la buse s'était-elle bouchée ?",
    },
    {
        "key": "p13", "num": 13, "title": "La cause racine après l'arrêt",
        "points": [("L'arrêt révèle ; l'analyse améliore", "L'arrêt révèle"),
                   ("Demander pourquoi, avec des preuves", "Pourquoi la buse s'est-elle bouchée"),
                   ("Corriger, puis standardiser", "Elle a donc ajouté")],
        "example": "La colle polymérisait dans la buse pendant les pauses. Pas d'étape de purge dans le "
                   "standard.",
        "example_cue": "La colle polymérisait",
        "script": "L'arrêt révèle un problème. L'analyse de la cause racine le transforme en amélioration. "
                  "Pourquoi la buse s'est-elle bouchée ? La colle polymérisait à l'intérieur pendant les "
                  "pauses. Pourquoi ? Il n'y avait pas d'étape de purge après une pause. Pourquoi ? Le "
                  "standard ne couvrait jamais les pauses. Elle a donc ajouté une purge automatique après "
                  "toute pause, et une surveillance de pression. Le PFMEA et le SOP ont aussi été mis à "
                  "jour. Comment mesureriez-vous le succès ?",
    },
    {
        "key": "p14", "num": 14, "title": "Mesurer les bonnes choses",
        "points": [("Rendement au premier passage et fuites", "Surveillez le rendement au premier passage"),
                   ("Temps de réponse Andon", "Le temps de réponse Andon"),
                   ("Anomalies répétées", "les anomalies répétées")],
        "example": "Rendement au premier passage : 97,5 % → 99,0 %. Fuites : zéro en 90 jours.",
        "example_cue": "Les résultats d'Anjali",
        "script": "Mesurez la réaction et la répétition, pas seulement le nombre d'arrêts. Surveillez le "
                  "rendement au premier passage, et les fuites vers le client. Suivez le temps de réponse "
                  "Andon, de l'appel à l'arrivée de l'aide. Et surveillez les anomalies répétées. Elles "
                  "doivent baisser avec le temps. Les résultats d'Anjali étaient clairs. Le rendement au "
                  "premier passage a gagné un point et demi, à quatre-vingt-dix-neuf pour cent. Pas un seul "
                  "joint n'a échappé en quatre-vingt-dix jours. Qui fait que tout cela marche ?",
    },
    {
        "key": "p15", "num": 15, "title": "Rôles et feuille de route",
        "points": [("Les opérateurs détectent, appellent et arrêtent", "Les opérateurs détectent"),
                   ("Les responsables réagissent et rétablissent", "Les responsables réagissent"),
                   ("Un déploiement en 30-60-90 jours", "Déployez-le")],
        "example": "Jours 0–30 : définir l'anormal. 31–60 : détecter et former. 61–90 : corriger les "
                   "principales répétitions.",
        "example_cue": "Pendant les trente premiers jours",
        "script": "Chacun a un rôle. Les opérateurs détectent, appellent, arrêtent et donnent des faits. "
                  "Les responsables réagissent vite, et rétablissent le standard. La maintenance garde les "
                  "capteurs et les interverrouillages en état, et la direction protège le droit d'arrêter. "
                  "Déployez-le en quatre-vingt-dix jours. Pendant les trente premiers jours, définissez "
                  "l'anormal et choisissez un pilote. Puis construisez la détection et formez. Enfin, "
                  "corrigez les principales causes répétées. Par où commencerez-vous ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Détecter", "icon": "sensor", "with": 0},
        {"label": "Arrêter", "icon": "lock", "with": 1},
        {"label": "Corriger", "icon": "wrench", "with": 2},
        {"label": "Prévenir", "icon": "shield", "tone": "good", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Sans Jidoka", "sub": "Les défauts voyagent, trouvés tard", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Avec Jidoka", "sub": "Attrapé à la source", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 140, "icon": "warning", "label": "joints trop fins au matin",
                 "unit": "trouvés au test d'étanchéité", "with": "example"}},
    "p03": {"type": "timeline", "items": [
        {"label": "Le métier s'arrête si un fil casse", "sub": "Début des années 1900", "icon": "gear", "with": 0},
        {"label": "Pilier du TPS", "sub": "TPS", "icon": "stack", "with": 2},
        {"label": "Aucun défaut transmis", "sub": "Aujourd'hui", "icon": "shield", "tone": "good", "with": "example"}]},
    "p04": {"type": "versus", "items": [
        {"label": "Surveiller une machine", "sub": "Toute l'équipe", "icon": "search", "tone": "bad", "with": 0},
        {"label": "Deux postes tenus", "sub": "Et des problèmes résolus", "icon": "person", "tone": "good", "with": "example"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Définir le normal", "icon": "clipboard", "with": 0},
        {"label": "Détecter la dérive", "icon": "sensor", "with": 1},
        {"label": "Tests, surveillance", "icon": "test", "with": 2}],
        "then": {"type": "stat", "value": 2.0, "decimals": 1, "suffix": "–2.4 mm", "icon": "pin", "label": "largeur normale du cordon",
                 "unit": "sans trou", "with": "example"}},
    "p06": {"type": "steps", "items": [
        {"label": "Arrêter ou confiner", "with": 0},
        {"label": "Corriger", "with": 1},
        {"label": "Prévenir", "with": 2}]},
    "p07": {"type": "versus", "items": [
        {"label": "Simple automatisation", "sub": "A dosé toute la nuit", "icon": "gear", "tone": "bad", "with": 0},
        {"label": "Jidoka", "sub": "S'arrête et appelle", "icon": "sensor", "tone": "good", "with": 1}]},
    "p08": {"type": "icons", "items": [
        {"label": "Aucun défaut transmis", "icon": "lock", "with": 0},
        {"label": "Aucune anomalie cachée", "icon": "search", "with": 1},
        {"label": "Aucune répétition sans action", "icon": "key", "tone": "good", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Vert : normal", "sub": "Restez au standard", "icon": "check", "tone": "good", "with": 0},
        {"label": "Jaune : aide", "sub": "Un responsable arrive vite", "icon": "person", "with": 1},
        {"label": "Rouge : arrêt", "sub": "Confiner, escalader", "icon": "warning", "tone": "bad", "with": 2}]},
    "p10": {"type": "bars", "label": "", "note": "Appels Andon par semaine", "with": 2, "items": [
        {"label": "Avant", "value": 10, "with": 2},
        {"label": "Mois 1", "value": 20, "with": "example"},
        {"label": "Mois 3", "value": 10, "tone": "good", "with": "example"}]},
    "p11": {"type": "ladder", "top": "LE PLUS FORT", "bottom": "LE PLUS FAIBLE", "items": [
        {"label": "Éliminer ou empêcher", "icon": "shape", "with": 0},
        {"label": "Détecter et arrêter", "icon": "sensor", "with": 1},
        {"label": "Avertir", "icon": "warning", "with": 2},
        {"label": "Inspecter plus tard", "icon": "search", "with": 2}]},
    "p12": {"type": "flow", "items": [
        {"label": "Le capteur vérifie chaque cordon", "icon": "sensor", "with": 0},
        {"label": "Le doseur s'arrête", "icon": "lock", "with": 1},
        {"label": "Andon, blocage jusqu'à la dernière bonne", "icon": "warning", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Avant", "value": 140}, "after": {"label": "Avec Jidoka", "value": 1},
                 "unit": "moniteurs touchés par problème de buse", "with": "example"}},
    "p13": {"type": "steps", "items": [
        {"label": "Buse bouchée", "with": 1},
        {"label": "Colle polymérisée pendant les pauses", "with": "example"},
        {"label": "Pas d'étape de purge", "with": "example"},
        {"label": "Purge automatique + surveillance de pression", "with": 2}]},
    "p14": {"type": "compare", "before": {"label": "Avant", "value": 97.5}, "after": {"label": "Après", "value": 99.0},
            "decimals": 1, "suffix": "%", "unit": "rendement au premier passage", "note": "Zéro fuite en 90 jours", "with": "example"},
    "p15": {"type": "timeline", "items": [
        {"label": "Définir l'anormal, pilote", "sub": "Jours 0–30", "icon": "clipboard", "with": 2},
        {"label": "Détecter, former", "sub": "31–60", "icon": "sensor", "with": 2},
        {"label": "Corriger les principales répétitions", "sub": "61–90", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Qu'est-ce qui distingue le Jidoka de l'automatisation ordinaire ?",
        "options": ["Il va plus vite",
                    "Il détecte une anomalie définie, s'arrête, et appelle une personne",
                    "Il n'a besoin de personne"],
        "correct": 1,
        "explanation": "L'automatisation fait le travail ; le Jidoka le juge aussi. Il s'arrête sur une anomalie "
                       "définie et appelle à l'aide humaine, pour que les défauts ne se multiplient pas.",
        "q_script": "Vérification rapide. Qu'est-ce qui distingue le Jidoka de l'automatisation ordinaire ? "
                    "Prenez quelques secondes.",
        "a_script": "C'est le deuxième. Il détecte une anomalie définie, s'arrête de lui-même, et appelle une "
                    "personne. Ainsi les défauts ne se multiplient pas.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Une opératrice voit un joint anormal, mais la ligne est en retard sur l'objectif. Que "
                    "doit-elle faire ?",
        "options": ["Continuer et le signaler en fin d'équipe",
                    "Appeler l'Andon et bloquer l'unité, comme le disent les règles d'arrêt",
                    "Le corriger elle-même discrètement et continuer"],
        "correct": 1,
        "explanation": "Aucun défaut transmis, aucune anomalie cachée. Appeler l'Andon et bloquer l'unité "
                       "protège le client, même quand la production est en retard.",
        "q_script": "Encore une, et cette fois c'est un scénario. Une opératrice voit un joint anormal, mais "
                    "la ligne est en retard sur l'objectif. Que doit-elle faire ? Réfléchissez.",
        "a_script": "Appeler l'Andon, et bloquer l'unité, exactement comme le disent les règles d'arrêt. "
                    "Aucun défaut transmis, et aucune anomalie cachée, même quand la production est en "
                    "retard.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
