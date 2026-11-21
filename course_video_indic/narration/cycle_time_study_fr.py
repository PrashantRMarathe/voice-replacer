"""cycle_time_study in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh cycle_time_study_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "ct_fr"
NAME = "cycle_time_study_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Cycle Time Study": "saïkeul taïme steudi",
    "Design Thinking": "dizaïne sinking",
    "Gemba": "Guemba",
    "TAKT": "takte",
    "ECRS": "eu cé erre esse",
    "UPH": "u pé ache",
    "FPY": "effe pé i grec",
    "SOP": "esse o pé",
    "ESD": "eu esse dé",
    "A": "a",
    "C": "cé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Le rapport disait que chaque poste était plus rapide que vingt-quatre secondes. "
    "Pourtant, la ligne de moniteurs ratait son objectif horaire, équipe après équipe. Alors, "
    "les chiffres de qui étaient faux ? Ça vous dit quelque chose ? Dans cette leçon, vous "
    "allez découvrir le Cycle Time Study. Vous verrez comment chronométrer correctement un "
    "poste, trouver le vrai goulot, et le corriger sans pousser les gens à aller plus vite. "
    "Nous suivrons Imran, ingénieur procédés sur une ligne d'assemblage de moniteurs."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Définissez d'abord la limite, sinon vos chiffres ne "
    "seront pas comparables. Regardez la dispersion, pas seulement la moyenne. Et corrigez la "
    "méthode au goulot, jamais en sautant des contrôles qualité. Voici votre action pour "
    "cette semaine. Chronométrez dix cycles sur un poste, et comparez le plus long au TAKT. "
    "Bravo d'avoir terminé cette leçon. Ensuite, vous découvrirez le Design Thinking."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le temps de cycle",
        "points": [("Le temps entre deux unités terminées", "le temps entre"),
                   ("À une limite définie", "à une limite que vous définissez"),
                   ("Dans des conditions précisées", "dans des conditions que vous précisez")],
        "example": "Le rapport disait que le poste C prenait 21 secondes. Le chronomètre d'Imran disait 28.",
        "example_cue": "Le rapport disait",
        "script": "Commençons par une définition claire. Le temps de cycle est le temps entre une unité "
                  "terminée et la suivante. On le mesure à une limite que vous définissez, dans des "
                  "conditions que vous précisez. Ça paraît simple, non ? Voici pourquoi ça ne l'est pas. Le "
                  "rapport disait que le poste de test d'écran prenait vingt et une secondes. Imran s'y est "
                  "tenu avec un chronomètre, et a mesuré vingt-huit. Les deux chiffres étaient honnêtes. "
                  "Alors, comment peuvent-ils être vrais tous les deux ?",
    },
    {
        "key": "p02", "num": 2, "title": "Les limites comptent",
        "points": [("Temps manuel : le travail à la main", "Le temps manuel est"),
                   ("Temps machine : test, dépose, polymérisation", "Le temps machine est"),
                   ("Cycle du poste : l'intervalle réel de répétition", "Le cycle du poste"),
                   ("Même limite, sinon pas de comparaison", "Si deux équipes")],
        "example": "Les 21 secondes venaient de vieux temps standard. Les 28 secondes étaient le vrai "
                   "intervalle d'une unité à l'autre.",
        "example_cue": "Le rapport utilisait",
        "script": "Parce qu'ils mesuraient des choses différentes. Le temps manuel est le travail à la "
                  "main, comme visser et connecter. Le temps machine est automatique, comme un test ou une "
                  "polymérisation. Le cycle du poste est l'intervalle réel de répétition, avec les "
                  "chevauchements. Vous ne pouvez pas simplement les additionner. Le rapport utilisait de "
                  "vieux temps standard, sans reprises ni attentes. Imran a mesuré d'un moniteur terminé au "
                  "suivant. Si deux équipes utilisent des limites différentes, leurs chiffres ne sont pas "
                  "comparables. Alors, quel chiffre compte pour votre client ?",
    },
    {
        "key": "p03", "num": 3, "title": "Temps de cycle face au TAKT, délai, UPH",
        "points": [("Temps de cycle : à quelle fréquence vous en terminez un", "Le temps de cycle demande"),
                   ("TAKT : le rythme exigé par la demande", "Le TAKT demande"),
                   ("Délai : de la commande à la fin, attentes comprises", "Le délai est"),
                   ("UPH : bonnes unités par heure", "L'UPH compte")],
        "example": "La ligne d'Imran : TAKT de 24 secondes, il lui faut donc 150 moniteurs par heure.",
        "example_cue": "Sur la ligne d'Imran",
        "script": "Quatre mesures se ressemblent, mais répondent à des questions différentes. Le temps de "
                  "cycle demande, à quelle fréquence en terminez-vous un ? Le TAKT demande, quel rythme la "
                  "demande exige-t-elle ? Le délai est tout le parcours, de la commande à la fin, attentes "
                  "comprises. Il peut se compter en jours, même quand votre cycle se compte en secondes. "
                  "L'UPH compte les bonnes unités par heure. Sur la ligne d'Imran, le TAKT est de "
                  "vingt-quatre secondes. Cela fait cent cinquante moniteurs par heure. Lesquelles "
                  "suivez-vous ?",
    },
    {
        "key": "p04", "num": 4, "title": "Comparer au TAKT",
        "points": [("Au-dessus du TAKT : manque de capacité", "Si le temps de cycle est au-dessus"),
                   ("Égal au TAKT : aucune marge", "S'il est égal"),
                   ("En dessous du TAKT : de la marge, ne surproduisez pas", "S'il est en dessous")],
        "example": "Le poste C à 28 secondes est 4 secondes au-dessus d'un TAKT de 24 secondes.",
        "example_cue": "Le poste de test d'écran d'Imran",
        "script": "Comparez maintenant votre cycle au TAKT. Si le temps de cycle est au-dessus du TAKT, ce "
                  "poste ne peut pas suivre. Vous manquez de capacité. S'il est égal, vous n'avez aucune "
                  "place pour le moindre accroc ou arrêt. S'il est en dessous, vous avez de la marge. Mais "
                  "ne l'utilisez pas pour surproduire. Le poste de test d'écran d'Imran était à vingt-huit "
                  "secondes. C'est quatre secondes au-dessus du TAKT, à chaque cycle. Alors, comment mener "
                  "une étude fiable ?",
    },
    {
        "key": "p05", "num": 5, "title": "Préparer l'étude",
        "points": [("Un objectif et un poste clairs", "Choisissez le poste"),
                   ("Notez les conditions", "Notez les conditions"),
                   ("Seulement les cycles normaux, retards consignés", "Séparez le démarrage"),
                   ("Expliquez-le à l'opérateur", "Et dites à l'opérateur")],
        "example": "L'objectif d'Imran : mesurer l'intervalle de répétition du poste C pour vérifier sa "
                   "capacité face au TAKT.",
        "example_cue": "L'objectif d'Imran tenait",
        "script": "Une bonne étude commence par un objectif. Choisissez le poste, peut-être un goulot "
                  "supposé, ou un poste qui varie beaucoup. Notez les conditions. C'est-à-dire le modèle, "
                  "l'opérateur, l'équipe et les outils. Séparez le démarrage, les changements de série et "
                  "les retouches des cycles normaux. Et dites à l'opérateur pourquoi vous êtes là. Vous "
                  "étudiez le processus, vous ne le jugez pas. L'objectif d'Imran tenait en une phrase. "
                  "Vérifier le poste C face au TAKT. Prêt à décomposer le travail ?",
    },
    {
        "key": "p06", "num": 6, "title": "Décomposer les éléments",
        "points": [("Découpez le travail en éléments visibles", "Découpez le travail"),
                   ("Un début et une fin clairs pour chacun", "Chaque élément a besoin"),
                   ("L'attente notée à part", "Notez l'attente à part"),
                   ("Ne supprimez jamais les contrôles qualité ou sécurité", "Ne supprimez jamais")],
        "example": "Poste C : charger 4 s, scanner l'étiquette 3 s, test d'écran 13 s, étiquette de série 4 "
                   "s, décharger 3 s, attente 1 s.",
        "example_cue": "Imran a découpé le poste C",
        "script": "Découpez le travail en petits éléments que vous pouvez vraiment voir. Chaque élément a "
                  "besoin d'un début et d'une fin clairs, pour ne rien compter deux fois. Notez l'attente à "
                  "part du temps de travail. Puis classez chaque étape en valeur ajoutée, nécessaire, ou "
                  "pur gaspillage. Ne supprimez jamais un contrôle qualité ou sécurité obligatoire. Imran a "
                  "découpé le poste C en six parties. Charger, scanner l'étiquette, le test d'écran, "
                  "l'étiquette de série, décharger, et un peu d'attente. Où regarderiez-vous en premier ?",
    },
    {
        "key": "p07", "num": 7, "title": "La feuille de chronométrage",
        "points": [("Chronométrez des cycles répétés, pas un seul", "Chronométrez de nombreux cycles"),
                   ("Moyenne : 28 s. Plage : de 26 à 32 s", "La moyenne était"),
                   ("Notez chaque cycle anormal", "Notez chaque cycle anormal")],
        "example": "Le cycle le plus long : 32 secondes, quand le scan de l'étiquette a échoué deux fois.",
        "example_cue": "Le cycle le plus long",
        "script": "Ne faites jamais confiance à un seul beau cycle. Chronométrez de nombreux cycles "
                  "d'affilée. Imran en a chronométré dix. La moyenne était de vingt-huit secondes. Mais la "
                  "dispersion allait de vingt-six jusqu'à trente-deux. Notez chaque cycle anormal, avec sa "
                  "raison, pas seulement le chiffre. Le cycle le plus long a eu lieu quand le scan de "
                  "l'étiquette a échoué deux fois. Une moyenne seule l'aurait caché. Que cache votre cycle "
                  "le plus long ?",
    },
    {
        "key": "p08", "num": 8, "title": "Calculer la capacité",
        "points": [("Production horaire = 3 600 ÷ temps de cycle", "La production horaire est"),
                   ("Poste C : environ 129 par heure", "À vingt-huit secondes"),
                   ("Postes nécessaires = contenu de travail ÷ TAKT", "Pour savoir combien")],
        "example": "La demande exige 150 par heure. Le poste C en fait environ 129. Voilà l'écart.",
        "example_cue": "La demande exige",
        "script": "Transformez maintenant le temps en capacité. La production horaire est le nombre de "
                  "secondes dans une heure, divisé par votre temps de cycle. À vingt-huit secondes, le "
                  "poste C fait environ cent vingt-neuf moniteurs par heure. La demande exige cent "
                  "cinquante. Voilà l'écart, en chiffres clairs. Pour savoir combien de postes il vous "
                  "faut, divisez le contenu de travail total par le TAKT, puis arrondissez au-dessus. "
                  "Précisez chaque hypothèse. Votre plan utilise-t-il le temps net, après les pauses ?",
    },
    {
        "key": "p09", "num": 9, "title": "La variation compte",
        "points": [("Les moyennes cachent les cycles longs", "les moyennes cachent"),
                   ("Tracez les cycles dans l'ordre chronologique", "Tracez vos cycles"),
                   ("Ne supprimez jamais les cycles longs pour faire joli", "Ne supprimez jamais"),
                   ("Indiquez la dispersion et le % au-dessus du TAKT", "Indiquez le temps typique")],
        "example": "Poste C : 3 cycles sur 10 ont duré 30 secondes ou plus.",
        "example_cue": "Au poste C",
        "script": "Voici un piège. Deux postes peuvent avoir la même moyenne, et se comporter très "
                  "différemment. Les moyennes cachent les cycles longs qui créent des files d'attente. "
                  "Alors tracez vos cycles dans l'ordre chronologique. Séparez-les par modèle et par équipe "
                  "avant de les regrouper. Ne supprimez jamais les cycles longs juste pour améliorer la "
                  "moyenne. Étudiez-les plutôt. Indiquez le temps typique, la dispersion, et la fréquence "
                  "des dépassements du TAKT. Au poste C, trois cycles sur dix ont duré trente secondes ou "
                  "plus. Ça vous dit quelque chose ?",
    },
    {
        "key": "p10", "num": 10, "title": "Trouver le goulot",
        "points": [("Le poste le plus lent fixe le rythme", "Le poste le plus lent"),
                   ("Cherchez une file avant, de l'attente après", "Cherchez une file"),
                   ("Corrigez d'abord la contrainte", "Corrigez d'abord la contrainte")],
        "example": "Postes A 19 s, B 22 s, C 28 s, D 21 s. Le poste C plafonne la ligne.",
        "example_cue": "Imran a chronométré les quatre",
        "script": "Alors, quel poste limite vraiment votre ligne ? Le poste le plus lent fixe généralement "
                  "le rythme. Cherchez une file qui se forme devant lui, et des gens qui attendent après. "
                  "Imran a chronométré les quatre postes. Pied et capot, montage de la carte, test d'écran "
                  "et emballage. Seul le test d'écran était au-dessus du TAKT. Corrigez d'abord la "
                  "contrainte. Accélérer n'importe quel autre poste ne fait qu'accumuler plus d'en-cours. "
                  "Alors, pourquoi le poste C était-il lent ?",
    },
    {
        "key": "p11", "num": 11, "title": "Pourquoi est-il lent ?",
        "points": [("Allez voir : le poste réel", "Imran est allé au Gemba"),
                   ("Méthode, conception, machine ou attente ?", "Un poste lent peut être"),
                   ("Vérifiez reprises, alarmes et horodatages", "Il a vérifié")],
        "example": "Des reprises de scan d'étiquette, et une étiquette de série posée au poste de test "
                   "lui-même.",
        "example_cue": "Il a trouvé deux choses",
        "script": "Imran est allé au Gemba, et a observé le poste réel. Un poste lent peut être un problème "
                  "de méthode, un problème de conception, une machine lente, ou simplement de l'attente. "
                  "Chacun demande une solution différente. Il a vérifié les reprises de scan, les codes "
                  "d'alarme et les horodatages de test. Il a trouvé deux choses. Les étiquettes étaient "
                  "posées de travers, donc le scanner ratait souvent. Et l'opérateur collait aussi "
                  "l'étiquette de série, là, pendant le cycle. Qu'essaieriez-vous ?",
    },
    {
        "key": "p12", "num": 12, "title": "Améliorer la méthode",
        "points": [("Éliminer, Combiner, Réordonner, Simplifier", "Pensez ECRS"),
                   ("D'abord des solutions simples et peu coûteuses", "Puis cherchez"),
                   ("Ne sautez jamais de tests pour gagner du temps", "Mais ne raccourcissez jamais un cycle")],
        "example": "Un guide d'étiquette redresse chaque étiquette. Le scanner lit du premier coup.",
        "example_cue": "Imran a ajouté",
        "script": "Corrigez la méthode avant de demander à qui que ce soit d'aller plus vite. Pensez ECRS. "
                  "Éliminer, combiner, réordonner et simplifier. Puis cherchez des solutions simples et peu "
                  "coûteuses, comme des guides, des distributeurs et des contrôles par code-barres. Mais ne "
                  "raccourcissez jamais un cycle en sautant un test, un contrôle de couple ou la protection "
                  "ESD. Ce n'est pas une amélioration. Imran a ajouté un petit guide d'étiquette. Chaque "
                  "étiquette est maintenant droite, et le scanner la lit du premier coup. Et l'étiquette de "
                  "série ?",
    },
    {
        "key": "p13", "num": 13, "title": "Rééquilibrer la ligne",
        "points": [("Déplacez du travail vers les postes qui ont du temps libre", "Déplacez du travail"),
                   ("Gardez séquence, compétences et contrôles", "Vérifiez la séquence"),
                   ("Pas de nouvelle marche ni de risque ergonomique", "Et assurez-vous")],
        "example": "Étiquette de série déplacée au poste A : A 23 s, C 23 s. Chaque poste est maintenant "
                   "sous le TAKT.",
        "example_cue": "Imran a déplacé l'étiquette de série",
        "script": "Ensuite, rééquilibrez la ligne. Déplacez du travail vers les postes qui ont du temps "
                  "libre, mais seulement si c'est sûr. Vérifiez la séquence, les outils, les compétences et "
                  "les contrôles au nouveau poste. Et assurez-vous de ne pas ajouter de marche, d'effort ou "
                  "de risque de défaut. Imran a déplacé l'étiquette de série au poste A. Le poste A est "
                  "passé à vingt-trois secondes. Le poste C est descendu à vingt-trois. Chaque poste est "
                  "maintenant sous le TAKT. Est-ce la fin de l'histoire ?",
    },
    {
        "key": "p14", "num": 14, "title": "Prouvez-le, puis standardisez",
        "points": [("Essai sur plusieurs équipes et modèles", "Menez l'essai"),
                   ("Comparez dispersion, FPY et production", "Comparez la dispersion"),
                   ("Mettez à jour le travail standard et formez", "mettez à jour le travail standard"),
                   ("Escaladez vite toute dérive", "Fixez un déclencheur")],
        "example": "Déclencheur : 3 cycles d'affilée au-dessus du TAKT, et le chef d'équipe vérifie le "
                   "poste.",
        "example_cue": "Le déclencheur d'Imran",
        "script": "Pas encore. Une matinée rapide ne prouve rien. Menez l'essai sur plusieurs équipes et "
                  "modèles. Comparez la dispersion, le rendement au premier passage et la production, pas "
                  "seulement la moyenne. Si la qualité tient, mettez à jour le travail standard et formez "
                  "chaque équipe. Fixez un déclencheur, pour attraper vite toute dérive. Le déclencheur "
                  "d'Imran était simple. Trois cycles d'affilée au-dessus du TAKT, et le chef d'équipe "
                  "vérifie le poste. Qui vérifierait le vôtre ?",
    },
    {
        "key": "p15", "num": 15, "title": "Votre plan sur 30 jours",
        "points": [("Semaine 1 : définir et mesurer la référence", "En semaine une"),
                   ("Semaine 2 : trouver le goulot", "En semaine deux"),
                   ("Semaine 3 : essayer une contre-mesure", "En semaine trois"),
                   ("Semaine 4 : vérifier, standardiser, former", "En semaine quatre")],
        "example": "La ligne d'Imran tient maintenant 150 moniteurs par heure, avec un rendement au premier "
                   "passage inchangé.",
        "example_cue": "La ligne d'Imran tient maintenant",
        "script": "Maintenant, à vous. Voici un plan simple sur trente jours. En semaine une, définissez la "
                  "limite d'un poste, et chronométrez au moins dix cycles. En semaine deux, trouvez le "
                  "goulot et ses causes. En semaine trois, essayez une contre-mesure. En semaine quatre, "
                  "vérifiez-la, mettez à jour le SOP, et formez. La ligne d'Imran tient maintenant ses cent "
                  "cinquante par heure, et le rendement au premier passage n'a pas bougé. Quel poste "
                  "chronométrerez-vous en premier ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "D'une unité à l'autre", "icon": "sequence", "with": 0},
        {"label": "Limite définie", "icon": "pin", "with": 1},
        {"label": "Conditions précisées", "icon": "clipboard", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "21 s", "sub": "Le rapport", "icon": "clipboard", "with": "example"},
            {"label": "28 s", "sub": "Le chronomètre d'Imran", "icon": "clock", "with": "example"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Manuel", "sub": "Le travail à la main", "icon": "hand", "with": 0},
        {"label": "Machine", "sub": "Test, dépose, polymérisation", "icon": "gear", "with": 1},
        {"label": "Cycle du poste", "sub": "Intervalle réel de répétition", "icon": "clock", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Vieux temps standard", "sub": "21 secondes", "icon": "clipboard", "with": "example"},
            {"label": "D'une unité à l'autre", "sub": "28 secondes", "icon": "sequence", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Temps de cycle", "sub": "À quelle fréquence vous terminez", "icon": "clock", "with": 0},
        {"label": "TAKT", "sub": "Rythme exigé par la demande", "icon": "wave", "with": 1},
        {"label": "Délai", "sub": "De la commande à la fin", "icon": "calendar", "with": 2},
        {"label": "UPH", "sub": "Bonnes unités par heure", "icon": "count", "with": 3}],
        "then": {"type": "stat", "value": 150, "icon": "count", "label": "moniteurs par heure nécessaires",
                 "unit": "TAKT de 24 secondes", "with": "example"}},
    "p04": {"type": "ladder", "top": "MANQUE DE CAPACITÉ", "bottom": "MARGE", "items": [
        {"label": "Au-dessus du TAKT", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Égal au TAKT", "icon": "scale", "with": 1},
        {"label": "En dessous du TAKT", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
            {"label": "Poste C", "value": 28, "tone": "bad", "with": "example"}]}},
    "p05": {"type": "flow", "items": [
        {"label": "Objectif et poste", "icon": "pin", "with": 0},
        {"label": "Conditions", "icon": "clipboard", "with": 1},
        {"label": "Seulement les cycles normaux", "icon": "clock", "with": 2},
        {"label": "Expliquer à l'opérateur", "icon": "person", "tone": "good", "with": 3}]},
    "p06": {"type": "bars", "label": "", "note": "Éléments du poste C : 28 s au total", "with": "example", "items": [
        {"label": "Charger", "value": 4, "with": "example"},
        {"label": "Scanner", "value": 3, "with": "example"},
        {"label": "Test", "value": 13, "with": "example"},
        {"label": "Étiquette de série", "value": 4, "with": "example"},
        {"label": "Décharger", "value": 3, "with": "example"},
        {"label": "Attente", "value": 1, "tone": "bad", "with": "example"}]},
    "p07": {"type": "bars", "label": "", "note": "Dix cycles chronométrés au poste C (secondes)", "items": [
        {"label": "Le plus rapide", "value": 26, "tone": "good", "with": 1},
        {"label": "Moyenne", "value": 28, "with": 1},
        {"label": "Le plus lent", "value": 32, "tone": "bad", "with": "example"}]},
    "p08": {"type": "compare", "before": {"label": "Poste C", "value": 129}, "after": {"label": "Demande", "value": 150},
            "unit": "moniteurs par heure", "note": "3,600 ÷ 28 ≈ 129", "with": 1},
    "p09": {"type": "icons", "items": [
        {"label": "Les moyennes cachent", "icon": "search", "tone": "bad", "with": 0},
        {"label": "Ordre chronologique", "icon": "chartUp", "with": 1},
        {"label": "Gardez les cycles longs", "icon": "lock", "with": 2},
        {"label": "Dispersion, % au-dessus du TAKT", "icon": "scale", "with": 3}],
        "then": {"type": "stat", "value": 3, "suffix": " / 10", "icon": "clock", "label": "cycles de 30 secondes ou plus",
                 "unit": "poste C", "with": "example"}},
    "p10": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
        {"label": "A", "value": 19, "with": "example"},
        {"label": "B", "value": 22, "with": "example"},
        {"label": "C", "value": 28, "tone": "bad", "with": "example"},
        {"label": "D", "value": 21, "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Méthode", "icon": "clipboard", "with": 1},
        {"label": "Conception", "icon": "shape", "with": 1},
        {"label": "Machine", "icon": "gear", "with": 1},
        {"label": "Attente", "icon": "clock", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Étiquettes de travers", "icon": "label", "tone": "bad", "with": "example"},
            {"label": "Reprises de scan", "icon": "barcode", "tone": "bad", "with": "example"},
            {"label": "Étiquette de série pendant le cycle", "icon": "sticker", "tone": "bad", "with": "example"}]}},
    "p12": {"type": "steps", "items": [
        {"label": "Éliminer", "with": 0}, {"label": "Combiner", "with": 0},
        {"label": "Réordonner", "with": 0}, {"label": "Simplifier", "with": 0}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Avant", "sub": "Étiquettes de travers, reprises de scan", "icon": "barcode", "tone": "bad", "with": "example"},
            {"label": "Guide d'étiquette", "sub": "Lu du premier coup", "icon": "check", "tone": "good", "with": "example"}]}},
    "p13": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
        {"label": "A", "value": 23, "with": "example"},
        {"label": "B", "value": 22, "with": "example"},
        {"label": "C", "value": 23, "tone": "good", "with": "example"},
        {"label": "D", "value": 21, "with": "example"}]},
    "p14": {"type": "flow", "items": [
        {"label": "Essai : équipes, modèles", "icon": "calendar", "with": 0},
        {"label": "Dispersion, FPY, production", "icon": "chartUp", "with": 1},
        {"label": "Travail standard, formation", "icon": "clipboard", "with": 2},
        {"label": "Déclencheur : 3 au-dessus du TAKT", "icon": "warning", "tone": "good", "with": "example"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Définir et mesurer la référence", "sub": "Semaine 1", "icon": "clock", "with": 0},
        {"label": "Goulot", "sub": "Semaine 2", "icon": "search", "with": 1},
        {"label": "Essai", "sub": "Semaine 3", "icon": "wrench", "with": 2},
        {"label": "Standardiser", "sub": "Semaine 4", "icon": "check", "tone": "good", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Le temps de cycle d'un poste est de 30 secondes. Quelle est sa production théorique par "
                    "heure ?",
        "options": ["90 unités", "120 unités", "180 unités"],
        "correct": 1,
        "explanation": "Production horaire = 3 600 ÷ temps de cycle = 3 600 ÷ 30 = 120 unités par heure, avant "
                       "toute perte.",
        "q_script": "Vérification rapide. Le temps de cycle d'un poste est de trente secondes. Quelle est sa "
                    "production théorique par heure ? Prenez quelques secondes.",
        "a_script": "C'est cent vingt. Divisez les secondes d'une heure par le temps de cycle, et "
                    "rappelez-vous, c'est avant toute perte.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Après un changement, le temps de cycle d'un poste passe de 28 à 22 secondes, mais le "
                    "rendement au premier passage baisse. Et maintenant ?",
        "options": ["Le standardiser : le poste est plus rapide",
                    "Suspendre le changement et trouver pourquoi la qualité a baissé",
                    "Ajouter un contrôleur final pour attraper les défauts"],
        "correct": 1,
        "explanation": "Un cycle plus rapide qui fait plus de défauts n'est pas une amélioration. Suspendez le "
                       "changement, trouvez pourquoi le rendement a baissé, et ne standardisez qu'une fois la "
                       "qualité revenue.",
        "q_script": "Encore une, et cette fois c'est un scénario. Après un changement, un poste gagne six "
                    "secondes. Mais le rendement au premier passage baisse. Que doit faire l'équipe ? "
                    "Réfléchissez.",
        "a_script": "Suspendez le changement, et trouvez pourquoi la qualité a baissé. Un cycle plus rapide "
                    "qui fait plus de défauts n'est pas du tout une amélioration.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
