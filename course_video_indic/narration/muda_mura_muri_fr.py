"""muda_mura_muri in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh muda_mura_muri_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "mm_fr"
NAME = "muda_mura_muri_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Next Inspection": "nexte inspékchone",
    "Poka Yoke": "Poka Yoké",
    "TIMWOODS": "timme-oudz",
    "Heijunka": "Héïdjounka",
    "Gemba": "Guemba",
    "CCTV": "cé cé té vé",
    "SMED": "smède",
    "TAKT": "takte",
    "Muda": "Mouda",
    "Mura": "Moura",
    "Muri": "Mouri",
    "TPM": "té pé emme",
    "WIP": "double vé i pé",
    "3M": "trois emme",
    "5S": "cinq esse",
    "M": "emme",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Dix-huit heures. L'équipe finit dans une heure, et la ligne de Sanjay a quarante caméras "
    "de retard. Tout le monde se précipite. Les erreurs s'accumulent au test. Demain, ça "
    "recommence. Ça vous dit quelque chose ? Dans cette leçon, vous allez découvrir les 3M du "
    "Lean : Muda, Mura et Muri. Vous verrez comment le gaspillage, l'irrégularité et la "
    "surcharge s'alimentent les uns les autres. Et nous suivrons Sanjay, superviseur de ligne "
    "sur une ligne de caméras CCTV, qui casse ce cercle."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Muda, c'est le gaspillage, Mura, l'irrégularité, et Muri, "
    "la surcharge. Ils s'alimentent les uns les autres, alors améliorez-les ensemble. Et "
    "l'objectif est un flux stable, pas des gens qui travaillent plus vite. Voici votre "
    "action pour cette semaine. Suivez un produit le long de votre ligne, et repérez un "
    "exemple de chaque M. Bravo d'avoir terminé cette leçon. Ensuite, vous découvrirez Next "
    "Inspection, pour protéger le processus qui suit le vôtre."
)

# One story thread: Sanjay's CCTV camera assembly line. Big work-order releases,
# WIP waves before test, walking for parts, end-of-shift rush and overtime.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Découvrez les 3M",
        "points": [("Muda : le gaspillage — aucune valeur pour le client", "Muda, c'est le gaspillage"),
                   ("Mura : l'irrégularité — la charge monte et descend", "Mura, c'est l'irrégularité"),
                   ("Muri : la surcharge — au-delà de la capacité sûre", "Muri, c'est la surcharge")],
        "example": "La ligne de Sanjay, en une heure : les opérateurs attendent les kits (Muda), la "
                   "production fait des bonds (Mura), puis tout le monde se précipite (Muri).",
        "example_cue": "Sur la ligne de Sanjay",
        "script": "Voici l'idée centrale. Le Lean cherche trois ennemis d'un bon flux. Muda, c'est le "
                  "gaspillage, un travail qui n'apporte aucune valeur à votre client. Mura, c'est "
                  "l'irrégularité, une charge qui monte et descend. Muri, c'est la surcharge, demander aux "
                  "personnes ou aux machines plus qu'elles ne peuvent donner en sécurité. Sur la ligne de "
                  "Sanjay, on voit les trois en une heure. Les opérateurs attendent les kits, la production "
                  "fait des bonds, puis tout le monde se précipite. Alors, lequel attaquer en premier ?",
    },
    {
        "key": "p02", "num": 2, "title": "Comment les 3M sont liés",
        "points": [("On ne peut pas les corriger un par un", "Vous ne pouvez pas les corriger"),
                   ("Mura crée Muri, Muri crée Muda", "Mura crée souvent"),
                   ("Ne chassez que le gaspillage et il revient", "Si vous ne chassez")],
        "example": "Le gros lot du lundi (Mura) → opérateurs et testeur débordés (Muri) → défauts, "
                   "retouches, heures supplémentaires (Muda).",
        "example_cue": "Le planificateur de Sanjay a lancé",
        "script": "Voici la surprise. Vous ne pouvez pas les corriger un par un. Mura crée souvent Muri, et "
                  "Muri crée Muda. Le planificateur de Sanjay a lancé un énorme lot le lundi matin. Ça, "
                  "c'est Mura. Pour rattraper, les opérateurs se sont dépêchés et le testeur ne s'est "
                  "jamais arrêté. Ça, c'est Muri. Puis sont venus les défauts, les retouches et les heures "
                  "supplémentaires. Ça, c'est Muda. Si vous ne chassez que le gaspillage, il revient "
                  "aussitôt. Regardons donc chacun de près, en commençant par le gaspillage.",
    },
    {
        "key": "p03", "num": 3, "title": "Muda : le test de la valeur",
        "points": [("Est-ce que cela transforme le produit dont le client a besoin ?", "Cette étape transforme-t-elle"),
                   ("Est-ce bien fait du premier coup ?", "Est-ce bien fait"),
                   ("Le client paierait-il pour cela ?", "Le client paierait-il volontiers"),
                   ("Sinon — remettez-le en question", "Si la réponse est non")],
        "example": "Monter l'objectif ajoute de la valeur. Marcher pour chercher des étiquettes, attendre un "
                   "kit et tester deux fois, non.",
        "example_cue": "Sur la ligne de Sanjay, monter",
        "script": "Comment repérer le gaspillage ? Utilisez un test simple de la valeur. Cette étape "
                  "transforme-t-elle le produit d'une façon dont votre client a besoin ? Est-ce bien fait "
                  "du premier coup ? Le client paierait-il volontiers pour cela ? Si la réponse est non, "
                  "remettez-le en question. Sur la ligne de Sanjay, monter l'objectif ajoute de la valeur. "
                  "Marcher pour chercher des étiquettes, non. Pas plus qu'attendre un kit, ou tester une "
                  "caméra deux fois. Mais pouvez-vous supprimer chaque étape qui échoue au test ?",
    },
    {
        "key": "p04", "num": 4, "title": "Nécessaire ou pur gaspillage",
        "points": [("Type 1 : nécessaire aujourd'hui — simplifiez-le", "Certaines étapes n'ajoutent aucune valeur"),
                   ("Type 2 : pur gaspillage — supprimez-le", "Le type deux est du pur gaspillage"),
                   ("N'appelez jamais une personne un gaspillage", "N'appelez jamais une personne un gaspillage")],
        "example": "Type 1 : un contrôle de sécurité obligatoire. Type 2 : saisir le même numéro de série "
                   "dans deux systèmes.",
        "example_cue": "Un contrôle de sécurité obligatoire",
        "script": "Pas toujours. Certaines étapes n'ajoutent aucune valeur, mais vous en avez encore besoin "
                  "aujourd'hui. Un contrôle de sécurité obligatoire en est une. C'est du gaspillage de type "
                  "un. Simplifiez-le, ou repensez le processus pour qu'il ne soit plus nécessaire. Le type "
                  "deux est du pur gaspillage, comme saisir le même numéro de série dans deux systèmes. "
                  "Supprimez-le. Et voici une règle à respecter. N'appelez jamais une personne un "
                  "gaspillage. Le gaspillage vit dans le processus. Votre travail est de rendre le travail "
                  "plus facile et plus sûr. Alors, à quoi ressemble le gaspillage ?",
    },
    {
        "key": "p05", "num": 5, "title": "Les 8 gaspillages : TIMWOODS",
        "points": [("Transport · Stocks · Mouvements · Attente", "Transport, stocks"),
                   ("Surproduction · Surtraitement", "Surproduction et surtraitement"),
                   ("Défauts · Compétences inutilisées", "Défauts, et compétences inutilisées"),
                   ("Tournée des gaspillages : suivre un produit", "Sanjay a fait une tournée des gaspillages")],
        "example": "La tournée de Sanjay : 3 attentes de kits en 2 heures, de longues marches pour les "
                   "étiquettes, un mur de WIP avant le test.",
        "example_cue": "Trois attentes de kits",
        "script": "Retenez les huit gaspillages avec un mot, TIMWOODS. Transport, stocks, mouvements et "
                  "attente. Surproduction et surtraitement. Défauts, et compétences inutilisées. Sanjay a "
                  "fait une tournée des gaspillages. Il a suivi une caméra de la préparation des kits "
                  "jusqu'à l'emballage, et a noté ce qu'il voyait. Trois attentes de kits en deux heures. "
                  "De longues marches pour les étiquettes. Et un mur de WIP devant le test. Lequel de ces "
                  "huit trouveriez-vous en premier sur votre ligne ?",
    },
    {
        "key": "p06", "num": 6, "title": "Mura : l'irrégularité",
        "points": [("De gros lots, puis plus rien", "De gros lots arrivent"),
                   ("La matière arrive par à-coups", "La matière arrive par à-coups"),
                   ("Même travail, méthodes différentes", "Deux opérateurs font"),
                   ("Les moyennes cachent les pics et les creux", "La moyenne paraît correcte")],
        "example": "Le tableau horaire de Sanjay : 60, puis 105, puis 70. La moyenne paraît correcte ; la "
                   "ligne, non.",
        "example_cue": "Regardez le tableau horaire de Sanjay",
        "script": "Passons au Mura. C'est l'irrégularité de la demande, de la charge de travail ou du flux. "
                  "De gros lots arrivent, puis plus rien. La matière arrive par à-coups. Deux opérateurs "
                  "font le même travail de façons différentes. Regardez le tableau horaire de Sanjay. "
                  "Soixante, puis cent cinq, puis soixante-dix. La moyenne paraît correcte. Mais votre "
                  "ligne ne vit pas dans les moyennes. Elle vit dans ces pics et ces creux. Et les pics "
                  "mettent quelqu'un sous pression. Qui paie, à votre avis ?",
    },
    {
        "key": "p07", "num": 7, "title": "Muri : la surcharge",
        "points": [("Personnes : levages, gestes, alarmes, formation insuffisante", "Pour les personnes, ce sont des levages lourds"),
                   ("Machines : au-delà de la charge nominale, maintenance sautée", "Pour les machines, c'est tourner"),
                   ("Mène à la fatigue, aux erreurs, aux pannes", "Le Muri mène à la fatigue")],
        "example": "Une opératrice lève le bras au-dessus de l'épaule 120 fois par heure ; le testeur tourne "
                   "pendant chaque pause.",
        "example_cue": "Une des opératrices de Sanjay",
        "script": "Ce sont les personnes et les machines qui paient. C'est le Muri, la surcharge. Pour les "
                  "personnes, ce sont des levages lourds, des gestes difficiles, trop d'alarmes, ou trop "
                  "peu de formation. Pour les machines, c'est tourner au-delà de leur charge nominale, et "
                  "sauter la maintenance pour sortir la production. Une des opératrices de Sanjay lève le "
                  "bras au-dessus de l'épaule cent vingt fois par heure. Et le testeur tourne sans arrêt "
                  "pendant chaque pause. Le Muri mène à la fatigue, aux erreurs et aux pannes. Alors, "
                  "comment les trois se combinent-ils ?",
    },
    {
        "key": "p08", "num": 8, "title": "Quand les trois se percutent",
        "points": [("4 heures de demande en un seul lancement", "Quatre heures de demande"),
                   ("Postes en avance — le WIP s'accumule", "Les premiers postes ont pris de l'avance"),
                   ("Le test devient le goulot", "Le test est devenu le goulot"),
                   ("Heures supplémentaires, précipitation, défauts, retouches", "Les superviseurs ont ajouté du monde")],
        "example": "Ça ressemblait à une « capacité de test trop faible ». En réalité : lancement irrégulier "
                   "(Mura) + précipitation (Muri) + retouches (Muda).",
        "example_cue": "Ça ressemblait à un problème de capacité de test",
        "script": "Voici ce qui s'est passé lundi. Quatre heures de demande sont arrivées en un seul "
                  "lancement. Les premiers postes ont pris de l'avance, et le WIP s'est accumulé. Le test "
                  "est devenu le goulot. Les superviseurs ont ajouté du monde et des heures "
                  "supplémentaires. Les opérateurs se sont dépêchés, les défauts ont augmenté, et les "
                  "retouches ont chargé le test encore plus. Ça ressemblait à un problème de capacité de "
                  "test. Mais vous voyez les trois M dans cette histoire. Alors, comment les trouver sur "
                  "votre propre ligne ?",
    },
    {
        "key": "p09", "num": 9, "title": "Trouver les 3M au Gemba",
        "points": [("Observer avant de changer quoi que ce soit", "observez avant de changer"),
                   ("Noter temps, attentes, marches, WIP, retouches", "Notez les temps de cycle"),
                   ("Demander aux opérateurs ce qui est difficile", "Puis demandez aux opérateurs"),
                   ("Vérifier les données avant de choisir une solution", "Puis vérifiez les données")],
        "example": "Sanjay a étiqueté chaque constat Muda, Mura ou Muri. Une attente de kit de 20 minutes a "
                   "reçu deux étiquettes : gaspillage et irrégularité.",
        "example_cue": "Sanjay a étiqueté chaque constat",
        "script": "Allez au Gemba, et observez avant de changer quoi que ce soit. Choisissez une famille de "
                  "produits, et suivez-la. Notez les temps de cycle, les attentes, les marches, le WIP et "
                  "les retouches. Puis demandez aux opérateurs ce qui rend le travail difficile, irrégulier "
                  "ou dangereux. En général, ils le savent. Sanjay a étiqueté chaque constat Muda, Mura ou "
                  "Muri. Certains ont reçu deux étiquettes. Une attente de kit de vingt minutes est à la "
                  "fois du gaspillage et de l'irrégularité. Puis vérifiez les données avant de choisir une "
                  "solution.",
    },
    {
        "key": "p10", "num": 10, "title": "Outils pour supprimer le Muda",
        "points": [("5S : moins de recherches et de marches", "Les 5S réduisent"),
                   ("Travail standard : la meilleure méthode, la plus sûre", "Le travail standard fixe"),
                   ("Poka Yoke : arrêter les erreurs à la source", "Le Poka Yoke arrête les erreurs"),
                   ("SMED et TPM : changements de série, fiabilité", "Le SMED réduit"),
                   ("Analyse des causes racines : pas de défauts répétés", "L'analyse des causes racines arrête"),
                   ("N'automatisez pas un gaspillage", "N'automatisez pas un gaspillage")],
        "example": "Étiquettes et vis déplacées sur des racks à chaque poste : la marche est passée de 40 m "
                   "à 8 m.",
        "example_cue": "Sanjay a déplacé les étiquettes",
        "script": "Commençons à supprimer le gaspillage. Les 5S réduisent les recherches et les marches. Le "
                  "travail standard fixe la meilleure méthode, la plus sûre. Le Poka Yoke arrête les "
                  "erreurs à la source. Le SMED réduit le temps de changement de série, et la TPM garde les "
                  "machines fiables. L'analyse des causes racines arrête les défauts répétés. Sanjay a "
                  "déplacé les étiquettes et les vis sur des racks à chaque poste. La marche est passée de "
                  "quarante mètres à huit. Un avertissement, quand même. N'automatisez pas un gaspillage. "
                  "Vous ne feriez que l'accélérer.",
    },
    {
        "key": "p11", "num": 11, "title": "Outils pour lisser le Mura",
        "points": [("Heijunka : lisser le volume et le mix", "Le Heijunka lisse"),
                   ("Le TAKT relie votre rythme à la demande", "Le temps TAKT relie"),
                   ("Lancer à chaque pitch, pas par vagues", "lance donc maintenant le travail"),
                   ("Tirer et couloirs premier entré, premier sorti", "Les signaux de tirage")],
        "example": "TAKT = 27 000 s ÷ 450 caméras = une caméra toutes les 60 secondes.",
        "example_cue": "L'équipe de Sanjay dispose",
        "script": "Ensuite, lissez le flux. Le Heijunka lisse à la fois le volume et le mix. Le temps TAKT "
                  "relie votre rythme à la demande du client. L'équipe de Sanjay dispose de vingt-sept "
                  "mille secondes de temps de travail. Le client a besoin de quatre cent cinquante caméras. "
                  "Cela fait une caméra toutes les soixante secondes. Il lance donc maintenant le travail à "
                  "chaque pitch, pas par vagues. Les signaux de tirage et les couloirs premier entré, "
                  "premier sorti le gardent régulier. Le TAKT est un rythme, pas un fouet. Alors, comment "
                  "protéger vos équipes ?",
    },
    {
        "key": "p12", "num": 12, "title": "Outils pour soulager le Muri",
        "points": [("Équilibrer chaque poste au TAKT", "Équilibrez chaque poste"),
                   ("Gestes et levages dans une zone sûre", "Gardez les gestes"),
                   ("Des gabarits là où les mains tiennent les pièces", "Ajoutez des gabarits"),
                   ("Respecter les limites des machines et la maintenance", "Respectez les limites des machines")],
        "example": "Un gabarit tient maintenant la caméra pendant le vissage ; le bac haut est descendu à "
                   "portée de main.",
        "example_cue": "Sanjay a ajouté un gabarit",
        "script": "Concevez le travail pour qu'il convienne aux personnes et aux machines. Équilibrez "
                  "chaque poste au TAKT, avec des temps de cycle réels. Gardez les gestes et les levages "
                  "dans une zone sûre. Ajoutez des gabarits et des montages là où les mains tiennent des "
                  "pièces. Respectez les limites des machines, et ne sautez jamais la maintenance pour "
                  "protéger la production. Sanjay a ajouté un gabarit qui tient la caméra pendant le "
                  "vissage. Le bac haut est descendu à portée de main. Ne planifiez jamais pour cent pour "
                  "cent d'utilisation. Alors, comment tout assembler ?",
    },
    {
        "key": "p13", "num": 13, "title": "Une méthode 3M en 8 étapes",
        "points": [("Définir, puis observer au Gemba", "Définissez le problème"),
                   ("Classer selon les trois M", "Classez ce que vous voyez"),
                   ("Mesurer une référence, trouver les causes racines", "Mesurez une référence"),
                   ("Tester de petits changements avec le PDCA", "Testez de petits changements"),
                   ("Standardiser, continuer à auditer", "Quand un changement marche")],
        "example": "La référence de Sanjay : production horaire très irrégulière, 2,5 heures supplémentaires "
                   "par jour.",
        "example_cue": "La référence de Sanjay était claire",
        "script": "Utilisez une méthode simple en huit étapes. Définissez le problème, puis observez au "
                  "Gemba. Classez ce que vous voyez selon les trois M. Mesurez une référence, puis trouvez "
                  "les causes racines. Testez de petits changements en planifiant, faisant, vérifiant et "
                  "agissant. Quand un changement marche, faites-en le nouveau standard, et continuez à "
                  "l'auditer. La référence de Sanjay était claire. La production horaire faisait de grands "
                  "bonds, et les heures supplémentaires atteignaient deux heures et demie par jour. Voyons "
                  "maintenant ses résultats.",
    },
    {
        "key": "p14", "num": 14, "title": "Cas pratique : ligne CCTV",
        "points": [("Des lancements petits et réguliers + couloir premier entré, premier sorti", "Des lancements petits et réguliers"),
                   ("Pièces et étiquettes au point d'utilisation", "Les pièces et les étiquettes"),
                   ("Lancement aligné sur la capacité de test", "Un travail lancé selon"),
                   ("Tableau horaire, problèmes remontés tôt", "Et un tableau horaire")],
        "example": "Après 6 semaines : écarts horaires presque disparus, heures supplémentaires proches de "
                   "zéro, rendement au premier passage jusqu'à 98 %.",
        "example_cue": "Après six semaines",
        "script": "Voici ce que Sanjay a changé. Des lancements petits et réguliers, avec un couloir "
                  "premier entré, premier sorti avant le test. Les pièces et les étiquettes au point "
                  "d'utilisation. Un travail lancé selon la capacité de test. Et un tableau horaire, pour "
                  "que les problèmes remontent tôt, pas à dix-huit heures. Après six semaines, les écarts "
                  "horaires avaient presque disparu. Les heures supplémentaires étaient proches de zéro. Le "
                  "rendement au premier passage est monté à quatre-vingt-dix-huit pour cent. Remarquez "
                  "qu'il n'a demandé à personne de travailler plus vite. Alors, comment prouver que ça dure "
                  "?",
    },
    {
        "key": "p15", "num": 15, "title": "KPI et pérennité",
        "points": [("Flux : délai, WIP", "Pour le flux"),
                   ("Mura : amplitude de la production horaire", "Pour le Mura"),
                   ("Qualité : FPY, retouches", "Pour la qualité"),
                   ("Muri : heures supplémentaires, risque ergonomique", "Pour le Muri")],
        "example": "Plus d'unités par heure, mais moins de qualité et plus d'heures supplémentaires ? Vous "
                   "n'avez fait que déplacer la perte.",
        "example_cue": "Si les unités par heure",
        "script": "Mesurez les trois M, pas seulement la production. Pour le flux, suivez le délai et le "
                  "WIP. Pour le Mura, suivez l'amplitude de la production horaire, pas seulement la "
                  "moyenne. Pour la qualité, suivez le rendement au premier passage et les retouches. Pour "
                  "le Muri, surveillez les heures supplémentaires et les risques ergonomiques. Et ne "
                  "poursuivez jamais un seul chiffre. Si les unités par heure montent, mais que la qualité "
                  "baisse et que les heures supplémentaires grimpent, vous n'avez fait que déplacer la "
                  "perte. Continuez à le revoir au Gemba, chaque semaine.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Muda", "sub": "Gaspillage : attendre les kits", "icon": "trash", "tone": "bad"},
        {"label": "Mura", "sub": "Irrégularité : la production fait des bonds", "icon": "wave", "tone": "bad"},
        {"label": "Muri", "sub": "Surcharge : tout le monde se précipite", "icon": "weight", "tone": "bad"}]},
    "p02": {"type": "flow", "items": [
        {"label": "Mura", "sub": "Un énorme lot le lundi", "icon": "wave", "tone": "bad", "with": 1},
        {"label": "Muri", "sub": "Précipitation ; le testeur ne s'arrête jamais", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Muda", "sub": "Défauts, retouches, heures supplémentaires", "icon": "trash", "tone": "bad", "with": "example"}]},
    "p03": {"type": "versus", "items": [
        {"label": "Marcher pour les étiquettes", "sub": "Aucune valeur (ni attendre, ni tester deux fois)", "icon": "walk", "with": "example"},
        {"label": "Monter l'objectif", "sub": "Ajoute de la valeur", "icon": "camera", "with": "example"}]},
    "p04": {"type": "icons", "items": [
        {"label": "Type 1 : simplifier", "sub": "Un contrôle de sécurité obligatoire", "icon": "shield"},
        {"label": "Type 2 : supprimer", "sub": "Un numéro de série saisi deux fois", "icon": "cross", "tone": "bad"},
        {"label": "Les personnes ne sont jamais du gaspillage", "sub": "Le gaspillage vit dans le processus", "icon": "person", "tone": "good"}]},
    "p05": {"type": "steps", "items": [
        {"label": "Transport", "sub": "T", "with": 0}, {"label": "Stocks", "sub": "I", "with": 0},
        {"label": "Mouvements", "sub": "M", "with": 0}, {"label": "Attente", "sub": "W", "with": 0},
        {"label": "Surproduction", "sub": "O", "with": 1}, {"label": "Surtraitement", "sub": "O", "with": 1},
        {"label": "Défauts", "sub": "D", "with": 2}, {"label": "Compétences inutilisées", "sub": "S", "with": 2}]},
    "p06": {"type": "bars", "label": "Moyenne", "note": "paraît correcte, cache les écarts", "unit": "Tableau horaire de Sanjay : caméras par heure", "items": [
        {"label": "Heure 1", "value": 60, "with": "example"},
        {"label": "Heure 2", "value": 105, "tone": "bad", "with": "example"},
        {"label": "Heure 3", "value": 70, "with": "example"}]},
    "p07": {"type": "icons", "items": [
        {"label": "Personnes", "sub": "Levages, gestes, alarmes", "icon": "person", "tone": "bad", "with": 0},
        {"label": "Machines", "sub": "Au-delà de la charge nominale", "icon": "gear", "tone": "bad", "with": 1}],
        "then": {"type": "stat", "value": 120, "icon": "hand", "label": "gestes au-dessus de l'épaule",
                 "unit": "par heure, pour une opératrice", "with": "example"}},
    "p08": {"type": "flow", "items": [
        {"label": "4 heures de demande d'un coup", "icon": "wave", "tone": "bad"},
        {"label": "Le WIP s'accumule", "icon": "stack", "tone": "bad"},
        {"label": "Le test devient le goulot", "icon": "test", "tone": "bad"},
        {"label": "Heures supplémentaires, précipitation, retouches", "icon": "clock", "tone": "bad"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Observer d'abord", "icon": "search"}, {"label": "Le noter", "icon": "clipboard"},
        {"label": "Demander aux opérateurs", "icon": "person"}, {"label": "Vérifier les données", "icon": "chartUp"}]},
    "p10": {"type": "icons", "items": [
        {"label": "5S", "icon": "tray", "with": 0}, {"label": "Travail standard", "icon": "clipboard", "with": 1},
        {"label": "Poka Yoke", "icon": "key", "with": 2}, {"label": "SMED + TPM", "icon": "wrench", "with": 3},
        {"label": "Cause racine", "icon": "search", "with": 4}],
        "then": {"type": "compare", "before": {"label": "Avant", "value": 40}, "after": {"label": "Après", "value": 8},
                 "suffix": " m", "unit": "marche par caméra", "note": "80 % de marche en moins", "with": "example"}},
    "p11": {"type": "icons", "items": [
        {"label": "Heijunka", "sub": "Lisser le volume et le mix", "icon": "sequence", "with": 0},
        {"label": "TAKT", "sub": "Rythme fixé par la demande", "icon": "clock", "with": 1}],
        "then": {"type": "stat", "value": 60, "suffix": " s", "icon": "camera", "label": "une caméra toutes les 60 secondes",
                 "unit": "27 000 s de temps de travail ÷ 450 caméras", "with": "example"}},
    "p12": {"type": "icons", "items": [
        {"label": "Équilibrer au TAKT", "icon": "scale"}, {"label": "Zone de gestes sûre", "icon": "person"},
        {"label": "Gabarits et montages", "icon": "wrench"}, {"label": "Limites des machines", "icon": "gear"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Les mains tiennent la caméra", "sub": "Bac haut au-dessus de l'épaule", "icon": "hand"},
            {"label": "Un gabarit la tient", "sub": "Bac à portée de main", "icon": "wrench"}]}},
    "p13": {"type": "steps", "items": [
        {"label": "Définir", "with": 0}, {"label": "Observer", "with": 0}, {"label": "Classer 3M", "with": 1},
        {"label": "Mesurer", "with": 2}, {"label": "Trouver les causes", "with": 2}, {"label": "Tester (PDCA)", "with": 3},
        {"label": "Standardiser", "with": 4}, {"label": "Auditer", "with": 4}]},
    "p14": {"type": "flow", "items": [
        {"label": "Lancements petits et réguliers", "icon": "sequence", "tone": "good"},
        {"label": "Pièces au point d'utilisation", "icon": "tray", "tone": "good"},
        {"label": "Lancement = capacité de test", "icon": "test", "tone": "good"},
        {"label": "Tableau horaire", "icon": "chartUp", "tone": "good"}],
        "then": {"type": "stat", "value": 98, "suffix": "%", "icon": "check", "label": "rendement au premier passage après 6 semaines",
                 "unit": "Heures supplémentaires proches de zéro. Personne n'a travaillé plus vite.", "with": "example"}},
    "p15": {"type": "icons", "items": [
        {"label": "Flux", "sub": "Délai, WIP", "icon": "clock"},
        {"label": "Mura", "sub": "Amplitude horaire", "icon": "wave"},
        {"label": "Qualité", "sub": "FPY, retouches", "icon": "check"},
        {"label": "Muri", "sub": "Heures supplémentaires, ergonomie", "icon": "weight"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "La production horaire d'une ligne affiche 60, 105, 70, 110. Quel M cela montre-t-il le "
                    "plus clairement ?",
        "options": ["Muda — gaspillage", "Mura — irrégularité", "Muri — surcharge"],
        "correct": 1,
        "explanation": "Une production qui fait des bonds d'heure en heure, c'est le Mura : l'irrégularité de la "
                       "charge et du flux. Laissé tel quel, il crée en général du Muri (précipitation) puis du "
                       "Muda (défauts, heures supplémentaires).",
        "q_script": "Vérification rapide. La production horaire d'une ligne ne cesse de faire des bonds, "
                    "entre soixante et cent dix. Quel M cela montre-t-il le plus clairement ? Prenez quelques "
                    "secondes.",
        "a_script": "C'est le Mura, l'irrégularité. La charge fait des bonds d'heure en heure. Laissé tel "
                    "quel, il crée en général de la précipitation, puis du gaspillage.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un superviseur atteint le plan quotidien en ajoutant deux heures supplémentaires chaque "
                    "jour. Que doit faire l'équipe EN PREMIER ?",
        "options": ["Demander aux opérateurs de travailler plus vite", "Ajouter encore des heures supplémentaires pour créer un tampon",
                    "Observer le flux et trouver le Mura et le Muri derrière le manque",
                    "Acheter un autre testeur"],
        "correct": 2,
        "explanation": "Les heures supplémentaires cachent le problème. Allez au Gemba et trouvez l'irrégularité "
                       "et la surcharge qui causent la perte, puis lissez et rééquilibrez. Accélérer, ajouter "
                       "des tampons ou de nouvelles machines ne fait que déplacer la perte.",
        "q_script": "Encore une, et cette fois c'est un scénario. Un superviseur atteint le plan chaque jour "
                    "en ajoutant deux heures supplémentaires. Que doit faire l'équipe en premier ? "
                    "Réfléchissez.",
        "a_script": "Allez d'abord observer le flux. Trouvez l'irrégularité et la surcharge derrière le "
                    "manque, puis lissez et rééquilibrez. Les heures supplémentaires ne font que cacher le "
                    "problème.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
