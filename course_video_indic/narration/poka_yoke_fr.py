"""poka_yoke in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh poka_yoke_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "pk_fr"
NAME = "poka_yoke_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Shigeo Shingo": "Chiguéo Chinngo",
    "Poka Yokes": "Poka Yoké",
    "Poka Yoke": "Poka Yoké",
    "Pareto": "Paréto",
    "QRQC": "ku erre ku cé",
    "FMEA": "effe emme eu a",
    "NVR": "enne vé erre",
    "MES": "emme eu esse",
    "SOP": "esse o pé",
    "PPM": "pé pé emme",
    "SMT": "esse emme té",
    "BOM": "bé o emme",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Dix-huit enregistreurs vidéo sont partis avec une vis manquante. L'opératrice était "
    "compétente, et attentive. Elle était simplement humaine. Ça vous dit quelque chose ? "
    "Dans cette leçon, vous allez découvrir le Poka Yoke, ou détrompage. Vous verrez comment "
    "concevoir un processus où la mauvaise action est impossible, ou détectée immédiatement. "
    "Nous suivrons Divya, ingénieure procédés sur une ligne d'assemblage de NVR, qui retire "
    "la mémoire de la qualité."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Les erreurs sont prévisibles, alors éliminez-les dès la "
    "conception. Préférez la prévention à la détection, et la détection à l'alerte. Et testez "
    "chaque dispositif avec de mauvais échantillons, pour savoir qu'il fonctionne toujours. "
    "Voici votre action pour cette semaine. Trouvez sur votre ligne un contrôle qui repose "
    "sur la mémoire, et esquissez un Poka Yoke pour lui. Bravo d'avoir terminé cette leçon. "
    "Ensuite, vous découvrirez le QRQC, le contrôle qualité à réponse rapide."
)

# Each page: title, 2-5 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est le Poka Yoke",
        "points": [("En japonais : à l'épreuve des erreurs", "Le Poka Yoke est un terme japonais"),
                   ("Ne comptez pas sur la mémoire", "Ne comptez pas sur"),
                   ("Mauvaise action impossible, ou vue immédiatement", "Concevez le processus")],
        "example": "Divya a remplacé un autocollant « vérifier l'orientation » par un connecteur détrompé. "
                   "Un autocollant avertit. Un détrompeur empêche.",
        "example_cue": "La ligne de Divya avait un autocollant",
        "script": "Voici l'idée centrale. Le Poka Yoke est un terme japonais qui veut dire à l'épreuve des "
                  "erreurs. Ne comptez pas sur quelqu'un qui doit se souvenir de bien faire. Concevez le "
                  "processus pour que la mauvaise action ne puisse pas arriver, ou se voie immédiatement. "
                  "La ligne de Divya avait un autocollant qui disait : vérifiez l'orientation du "
                  "connecteur. Elle l'a remplacé par un connecteur détrompé qui ne rentre que dans un sens. "
                  "Un autocollant avertit. Un détrompeur empêche. Alors, d'où vient cette idée ?",
    },
    {
        "key": "p02", "num": 2, "title": "Erreur ou défaut",
        "points": [("Du système de production Toyota", "Le Poka Yoke est né"),
                   ("Erreur : la mauvaise action", "L'erreur est la mauvaise action"),
                   ("Défaut : le mauvais produit qui en résulte", "Le défaut est le mauvais produit"),
                   ("Arrêtez l'erreur avant qu'elle devienne un défaut", "Vous arrêtez l'erreur")],
        "example": "L'inspection en fin de ligne trouve les problèmes une fois la main-d'œuvre et les pièces "
                   "dépensées.",
        "example_cue": "L'inspection en fin de ligne trouve",
        "script": "Le Poka Yoke est né dans le système de production Toyota, grâce à l'ingénieur Shigeo "
                  "Shingo. Son idée clé était simple. Une erreur et un défaut sont différents. L'erreur est "
                  "la mauvaise action, comme inverser un connecteur. Le défaut est le mauvais produit qui "
                  "en résulte. Vous arrêtez l'erreur avant qu'elle devienne un défaut. L'inspection en fin "
                  "de ligne trouve les problèmes une fois la main-d'œuvre et les pièces dépensées. Pourquoi "
                  "attendre si longtemps ?",
    },
    {
        "key": "p03", "num": 3, "title": "La hiérarchie des contrôles",
        "points": [("1 Éliminer : pions de centrage asymétriques", "Le mieux, éliminer"),
                   ("2 Empêcher : verrouillage par code-barres", "Ensuite, empêcher"),
                   ("3 Détecter et arrêter : capteur de vis manquante", "Puis détecter et arrêter"),
                   ("4 Avertir : une alarme", "Plus faible encore"),
                   ("5 Inspecter plus tard — le plus faible", "Le plus faible, inspecter plus tard")],
        "example": "Choisissez les contrôles selon leur fiabilité à arrêter les erreurs — pas selon leur "
                   "facilité d'installation.",
        "example_cue": "Choisissez les contrôles selon leur fiabilité",
        "script": "Tous les contrôles ne se valent pas. Voici l'ordre de force. Le mieux, éliminer le "
                  "risque d'erreur, avec des pions de centrage asymétriques. Ensuite, empêcher la mauvaise "
                  "action, comme un verrouillage par code-barres. Puis détecter et arrêter, comme un "
                  "capteur qui repère une vis manquante. Plus faible encore, une alarme d'avertissement. Le "
                  "plus faible, inspecter plus tard. Choisissez les contrôles selon leur fiabilité à "
                  "arrêter les erreurs, pas selon leur facilité d'installation. À quel niveau sont vos "
                  "contrôles aujourd'hui ?",
    },
    {
        "key": "p04", "num": 4, "title": "Règles d'ingénierie",
        "points": [("Un signal positif de conformité, pas « pas d'alarme »", "D'abord, cherchez"),
                   ("Sécurité intrinsèque en cas de perte d'alimentation ou de capteur", "Deuxièmement, le contrôle doit se mettre en sécurité"),
                   ("Contournement : rare, enregistré, limité dans le temps", "Troisièmement, rendez tout contournement"),
                   ("Testez-le avec de mauvaises conditions", "Quatrièmement, n'affirmez jamais")],
        "example": "Divya a débranché le câble du capteur pendant un essai. Le gabarit est resté verrouillé.",
        "example_cue": "Divya a débranché le câble du capteur",
        "script": "Suivez quatre règles d'ingénierie. D'abord, cherchez un signal positif de conformité, "
                  "pas seulement l'absence d'alarme. Deuxièmement, le contrôle doit se mettre en sécurité. "
                  "Si l'alimentation ou un capteur est perdu, il s'arrête. Troisièmement, rendez tout "
                  "contournement rare, enregistré et limité dans le temps. Quatrièmement, n'affirmez jamais "
                  "qu'il fonctionne avant de l'avoir testé avec de mauvaises conditions. Divya a débranché "
                  "le câble du capteur pendant un essai. Le gabarit est resté verrouillé. Alors, quels "
                  "types de Poka Yoke existent ?",
    },
    {
        "key": "p05", "num": 5, "title": "Trois méthodes",
        "points": [("Contact : forme, taille, position", "La méthode par contact"),
                   ("Valeur fixe : le bon nombre", "La méthode à valeur fixe"),
                   ("Étapes de mouvement : la bonne séquence", "La méthode par étapes")],
        "example": "Problème d'orientation → contact. Pièce manquante → valeur fixe. Scanner, programmer, "
                   "tester, étiqueter dans l'ordre → étapes de mouvement.",
        "example_cue": "Un problème d'orientation",
        "script": "Il existe trois méthodes classiques. La méthode par contact utilise la forme, la taille "
                  "ou la position pour distinguer le bon du mauvais. Un nid asymétrique en est un exemple. "
                  "La méthode à valeur fixe vérifie le nombre, comme un compteur qui exige les six vis. La "
                  "méthode par étapes vérifie la séquence. Scanner, programmer, tester, puis étiqueter, "
                  "dans cet ordre. Chacune peut empêcher ou détecter. Un problème d'orientation ? Utilisez "
                  "le contact. Une pièce manquante ? Utilisez la valeur fixe.",
    },
    {
        "key": "p06", "num": 6, "title": "L'erreur humaine est prévisible",
        "points": [("Les erreurs humaines sont prévisibles", "Les erreurs humaines sont prévisibles"),
                   ("Oubli, mauvaise pièce, inversion, désordre", "Les gens sautent des étapes"),
                   ("Demandez ce qui l'a rendu possible, pas qui", "Alors demandez ce qui a rendu")],
        "example": "Mauvais firmware → noms de recettes similaires → modèle choisi à la main → scan MES non "
                   "relié au programmateur.",
        "example_cue": "Divya a remonté le mauvais firmware",
        "script": "Les erreurs humaines sont prévisibles, alors traitez-les comme des risques du système. "
                  "Les gens sautent des étapes, prennent la mauvaise pièce, inversent des choses, ou font "
                  "les étapes dans le désordre. Ils saisissent le mauvais réglage, ou confondent les "
                  "étiquettes. Alors demandez ce qui a rendu l'erreur possible, pas qui l'a faite. Divya a "
                  "remonté le mauvais firmware jusqu'à des recettes aux noms similaires. Le modèle était "
                  "choisi à la main. Le scan MES n'était pas relié au programmateur. Voyez-vous déjà la "
                  "solution ?",
    },
    {
        "key": "p07", "num": 7, "title": "Une méthode de conception en 8 étapes",
        "points": [("Définir, observer, mesurer, trouver la cause", "Définissez le défaut"),
                   ("Choisir l'idée robuste la plus simple", "Choisissez l'idée robuste"),
                   ("Prototyper et tester avec de mauvaises pièces", "Construisez un prototype"),
                   ("Mettre à jour le SOP, former, surveiller", "Puis mettez à jour le SOP")],
        "example": "Convenez du succès avant d'installer : mauvaises pièces rejetées, bonnes pièces "
                   "acceptées, cadence tenue.",
        "example_cue": "Avant d'installer quoi que ce soit",
        "script": "Formez une équipe transverse, et travaillez en huit étapes. Définissez le défaut. "
                  "Observez l'opération réelle, et trouvez où l'erreur se produit. Mesurez la situation de "
                  "départ, et trouvez la cause. Choisissez l'idée robuste la plus simple. Construisez un "
                  "prototype, et testez-le avec de bonnes et de mauvaises pièces. Puis mettez à jour le "
                  "SOP, formez, et continuez à surveiller. Avant d'installer quoi que ce soit, convenez de "
                  "ce qu'est le succès. Mauvaises pièces rejetées, bonnes pièces acceptées, et votre "
                  "cadence tient toujours.",
    },
    {
        "key": "p08", "num": 8, "title": "Applications en assemblage",
        "points": [("Signal de couple relié à l'ordre de fabrication", "Elle a relié le signal de couple"),
                   ("Le gabarit ne se libère que si chaque vis est bonne", "Le gabarit ne se libère"),
                   ("Connecteurs détrompés, capteur de joint", "Elle a aussi ajouté")],
        "example": "Vis manquantes : 18 sur 10 000 → 1 sur 10 000, environ 94 % de moins.",
        "example_cue": "Les vis manquantes sont passées",
        "script": "Allons maintenant sur la ligne d'assemblage de Divya. Les vis manquantes étaient le gros "
                  "problème. Elle a relié le signal de couple de la visseuse à l'ordre de fabrication. Le "
                  "gabarit ne se libère que lorsque chaque vis a un bon résultat. Un plateau magnétique ne "
                  "pouvait pas le prouver. Les vis manquantes sont passées de dix-huit sur dix mille à une. "
                  "C'est environ quatre-vingt-quatorze pour cent de moins. Elle a aussi ajouté des "
                  "connecteurs détrompés, et un capteur de joint avant la fermeture. Et les cartes à "
                  "l'intérieur ?",
    },
    {
        "key": "p09", "num": 9, "title": "Applications en SMT et en test",
        "points": [("Chaque bobine scannée contre la BOM", "Alors scannez chaque bobine"),
                   ("Version du programme vérifiée avant le démarrage", "Vérifiez la version du programme"),
                   ("Numéro de série lié au modèle, au firmware et à l'enregistrement de réussite", "Au test, liez chaque"),
                   ("Une coupure réseau ne doit jamais donner « réussi »", "Et assurez-vous qu'une coupure réseau")],
        "example": "Le testeur de Divya ne peut pas imprimer d'étiquette sans enregistrement de réussite "
                   "pour ce numéro de série.",
        "example_cue": "Le testeur de Divya ne peut pas imprimer",
        "script": "Sur la ligne de cartes, de mauvais réglages peuvent produire des milliers de défauts "
                  "très vite. Alors scannez chaque bobine contre la nomenclature. Vérifiez la version du "
                  "programme avant le démarrage de la machine. Au test, liez chaque numéro de série à son "
                  "modèle, son firmware et son enregistrement de réussite. Le testeur de Divya ne peut pas "
                  "imprimer d'étiquette sans cet enregistrement. Et assurez-vous qu'une coupure réseau ne "
                  "puisse jamais créer une fausse réussite. Avez-vous testé le vôtre de cette façon ?",
    },
    {
        "key": "p10", "num": 10, "title": "Emballage et expédition",
        "points": [("Scan du numéro de série + correspondance avec l'étiquette du carton", "Alors scannez le numéro de série"),
                   ("Accessoires comptés avant la fermeture", "comptez les accessoires"),
                   ("Les contrôles de poids ont des angles morts", "Les contrôles de poids aident"),
                   ("Les codes-barres peuvent être contournés", "un code-barres n'est pas automatiquement")],
        "example": "Un mauvais adaptateur pesait autant que le bon — un plateau de kit profilé l'a détecté.",
        "example_cue": "Divya a trouvé un mauvais adaptateur",
        "script": "Un produit parfait peut encore devenir une réclamation à l'emballage. Alors scannez le "
                  "numéro de série, vérifiez l'étiquette du carton, et comptez les accessoires avant la "
                  "fermeture de la boîte. Les contrôles de poids aident, mais ils ont des angles morts. "
                  "Divya a trouvé un mauvais adaptateur qui pesait autant que le bon. Un plateau de kit "
                  "profilé l'a détecté à la place. Et rappelez-vous, un code-barres n'est pas "
                  "automatiquement à l'épreuve des erreurs. Les étiquettes en double et les forçages "
                  "manuels peuvent le contourner. Alors, chaque solution doit-elle coûter cher ?",
    },
    {
        "key": "p11", "num": 11, "title": "Peu coûteux et sûr",
        "points": [("Simple : pions, guides, contacts, plateaux", "Des pions, des guides, des fins de course"),
                   ("Ne jamais créer de point de pincement", "Un dispositif ne doit jamais"),
                   ("Les capteurs qualité ne sont pas des systèmes de sécurité", "un simple capteur qualité"),
                   ("Prévoir nettoyage et étalonnage", "Prévoyez aussi son nettoyage")],
        "example": "Le meilleur dispositif de Divya a coûté ₹1 200 : deux pions qui empêchent de monter le "
                   "panneau arrière à l'envers.",
        "example_cue": "Le meilleur dispositif de Divya a coûté",
        "script": "Pas du tout. Beaucoup des meilleurs Poka Yokes sont simples. Des pions, des guides, des "
                  "fins de course, des plateaux de comptage et des calibres passe, ne passe pas. Le "
                  "meilleur dispositif de Divya a coûté mille deux cents roupies. Deux pions qui empêchent "
                  "de monter le panneau arrière à l'envers. Mais gardez la sécurité en premier. Un "
                  "dispositif ne doit jamais créer de point de pincement. Et un simple capteur qualité "
                  "n'est pas un système de sécurité. Prévoyez aussi son nettoyage et son étalonnage. Alors, "
                  "comment le faire durer ?",
    },
    {
        "key": "p12", "num": 12, "title": "FMEA, plan de contrôle et audits",
        "points": [("FMEA : lien avec le mode de défaillance", "Dans le FMEA"),
                   ("Plan de contrôle : méthode et réaction", "Dans le plan de contrôle"),
                   ("Travail standard : signal de conformité, qui réarme", "Dans le travail standard"),
                   ("Auditer avec un mauvais échantillon connu", "Présentez-lui un mauvais échantillon connu")],
        "example": "Divya présente à chaque dispositif un mauvais échantillon connu, à chaque équipe.",
        "example_cue": "Divya le fait à chaque équipe",
        "script": "Intégrez chaque dispositif à votre système qualité. Dans le FMEA, reliez-le au mode de "
                  "défaillance qu'il maîtrise. Dans le plan de contrôle, écrivez la méthode et la réaction. "
                  "Dans le travail standard, montrez à quoi ressemble une conformité, et qui peut réarmer "
                  "le dispositif. Puis auditez-le. Ne vérifiez pas seulement que le dispositif existe. "
                  "Présentez-lui un mauvais échantillon connu, et confirmez qu'il le rejette. Divya le fait "
                  "à chaque équipe. Comment mesurer le bénéfice ?",
    },
    {
        "key": "p13", "num": 13, "title": "KPI et économies",
        "points": [("PPM de défauts et fuites en baisse", "Le PPM de défauts"),
                   ("Rendement au premier passage en hausse", "Le rendement au premier passage doit monter"),
                   ("Surveillez les faux rejets", "Et surveillez les faux rejets")],
        "example": "60 000 unités/mois, défauts réduits de 0,8 % à 0,2 % ≈ ₹65 000 économisées par mois, "
                   "moins le coût de fonctionnement.",
        "example_cue": "La ligne de Divya produit",
        "script": "Mesurez le résultat, et la santé de votre dispositif. Le PPM de défauts et les fuites "
                  "chez le client doivent baisser. Le rendement au premier passage doit monter. Et "
                  "surveillez les faux rejets. Un capteur qui rejette sans cesse de bonnes unités pousse "
                  "les gens à le contourner. La ligne de Divya produit soixante mille unités par mois. "
                  "Faire passer les défauts de presque un pour cent au quart de cela économise environ "
                  "soixante-cinq mille roupies par mois. Retirez ensuite votre coût de fonctionnement.",
    },
    {
        "key": "p14", "num": 14, "title": "Feuille de route sur 90 jours",
        "points": [("Semaines 1–2 : principaux modes de défaillance + situation de départ", "Pendant les deux premières semaines"),
                   ("Semaines 3–4 : options de conception, logique validée", "Pendant les deux semaines suivantes"),
                   ("Mois 2 : pilote sur un poste", "Le deuxième mois"),
                   ("Mois 3 : documenter, former, dupliquer", "Le dernier mois")],
        "example": "Testez chaque mauvaise condition connue pendant le pilote.",
        "example_cue": "testez chaque mauvaise condition",
        "script": "Voici un plan simple sur quatre-vingt-dix jours. Pendant les deux premières semaines, "
                  "choisissez vos principaux modes de défaillance grâce au Pareto et au FMEA, et fixez une "
                  "situation de départ. Pendant les deux semaines suivantes, concevez les options et "
                  "validez la logique. Le deuxième mois, faites un pilote sur un poste, et testez chaque "
                  "mauvaise condition connue. Le dernier mois, mettez à jour les documents, formez les "
                  "gens, puis dupliquez sur d'autres lignes. Qui est responsable de chaque partie ?",
    },
    {
        "key": "p15", "num": 15, "title": "Liste de vérification avant mise en service",
        "points": [("Mode de défaillance clair, avec une situation de départ", "Le mode de défaillance est-il clair"),
                   ("Sécurité et ergonomie revues", "La sécurité et l'ergonomie"),
                   ("Mauvais échantillons testés sur chaque modèle", "L'a-t-on testé"),
                   ("Perte d'alimentation, mode hors ligne, contournement gérés", "Gère-t-il la perte d'alimentation")],
        "example": "La production est responsable du poste. L'ingénierie le conçoit. La qualité le met à "
                   "l'épreuve.",
        "example_cue": "La production est responsable du poste",
        "script": "La production est responsable du poste. L'ingénierie le conçoit, et la qualité le met à "
                  "l'épreuve. Avant de mettre en service un dispositif, passez une dernière liste de "
                  "vérification. Le mode de défaillance est-il clair, avec une situation de départ ? La "
                  "sécurité et l'ergonomie ont-elles été revues ? L'a-t-on testé avec de mauvais "
                  "échantillons sur chaque modèle ? Gère-t-il la perte d'alimentation, le mode hors ligne "
                  "et le contournement ? Le meilleur Poka Yoke rend la bonne action naturelle, et la "
                  "mauvaise impossible.",
    },
]

# The picture beside each page's boxes (same layouts and icons as English, French
# labels). Items appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "versus", "items": [
        {"label": "Un autocollant avertit", "sub": "« Vérifier l'orientation »", "icon": "sticker", "with": "example"},
        {"label": "Un détrompeur empêche", "sub": "Ne rentre que dans un sens", "icon": "key", "with": "example"}]},
    "p02": {"type": "flow", "stop": {"after": 0, "label": "STOP ICI", "with": 3}, "items": [
        {"label": "Erreur", "sub": "La mauvaise action", "icon": "hand", "tone": "bad", "with": 1},
        {"label": "Défaut", "sub": "Le mauvais produit", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Trouvé en fin de ligne", "sub": "Main-d'œuvre et pièces déjà dépensées", "icon": "search", "tone": "bad", "with": "example"}]},
    "p03": {"type": "ladder", "items": [
        {"label": "Éliminer", "icon": "pin"}, {"label": "Empêcher", "icon": "barcode"},
        {"label": "Détecter et arrêter", "icon": "sensor"}, {"label": "Avertir", "icon": "warning"},
        {"label": "Inspecter plus tard", "icon": "search"}]},
    "p04": {"type": "icons", "items": [
        {"label": "Signal positif", "icon": "check"}, {"label": "Sécurité intrinsèque", "icon": "power"},
        {"label": "Contournement enregistré", "icon": "lock"}, {"label": "Tester les mauvais cas", "icon": "test"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Contact", "sub": "Forme, taille, position", "icon": "shape"},
        {"label": "Valeur fixe", "sub": "Le bon nombre", "icon": "count"},
        {"label": "Étapes de mouvement", "sub": "Le bon ordre", "icon": "sequence"}]},
    "p06": {"type": "flow", "items": [
        {"label": "Noms de recettes similaires", "icon": "sticker", "tone": "bad", "with": 2},
        {"label": "Modèle choisi à la main", "icon": "hand", "tone": "bad", "with": 2},
        {"label": "Mauvais firmware", "icon": "chip", "tone": "bad", "with": 2},
        {"label": "Solution : relier le scan MES", "sub": "au programmateur", "icon": "barcode", "tone": "good", "with": "example"}]},
    "p07": {"type": "steps", "items": [
        {"label": "Définir", "with": 0}, {"label": "Observer", "with": 0},
        {"label": "Mesurer", "with": 0}, {"label": "Trouver la cause", "with": 0},
        {"label": "Choisir une idée", "with": 1}, {"label": "Prototyper", "with": 2},
        {"label": "La mettre à l'épreuve", "with": 2}, {"label": "Standardiser", "with": 3}]},
    "p08": {"type": "assembly", "label": "La ligne NVR de Divya : le gabarit compte chaque vis",
            "then": {"type": "compare", "before": {"label": "Avant", "value": 18}, "after": {"label": "Après", "value": 1},
                     "unit": "vis manquantes pour 10 000 unités", "note": "environ 94 % de moins"}},
    "p09": {"type": "flow", "stop": {"after": 2, "label": "PAS DE RÉUSSITE, PAS D'ÉTIQUETTE", "with": "example"}, "items": [
        {"label": "Bobine scannée contre la BOM", "icon": "barcode", "with": 0},
        {"label": "Version du programme vérifiée", "icon": "chip", "with": 1},
        {"label": "Enregistrement de réussite par numéro de série", "icon": "test", "with": 2},
        {"label": "L'étiquette s'imprime", "icon": "label", "tone": "good", "with": "example"}]},
    "p10": {"type": "versus", "items": [
        {"label": "Contrôle de poids", "sub": "Mauvais adaptateur, même poids", "icon": "scale", "with": "example"},
        {"label": "Plateau de kit profilé", "sub": "Le mauvais adaptateur ne rentre pas", "icon": "tray", "with": "example"}]},
    "p11": {"type": "stat", "value": 1200, "prefix": "₹", "icon": "pin", "label": "Deux pions de centrage",
            "unit": "Plus aucun panneau arrière monté à l'envers"},
    "p12": {"type": "flow", "items": [
        {"label": "FMEA", "sub": "Le mode de défaillance", "icon": "clipboard"},
        {"label": "Plan de contrôle", "sub": "Méthode et réaction", "icon": "shield"},
        {"label": "Travail standard", "sub": "Signal de conformité, qui réarme", "icon": "person"},
        {"label": "Audit", "sub": "Un mauvais échantillon connu", "icon": "test", "tone": "good"}]},
    "p13": {"type": "compare", "before": {"label": "Avant", "value": 0.8}, "after": {"label": "Après", "value": 0.2},
            "suffix": "%", "decimals": 1, "unit": "taux de défauts, 60 000 unités par mois", "note": "≈ ₹65 000 économisées par mois"},
    "p14": {"type": "timeline", "items": [
        {"label": "Modes de défaillance + situation de départ", "sub": "W1–2", "span": 2, "icon": "search"},
        {"label": "Options de conception, logique validée", "sub": "W3–4", "span": 2, "icon": "gear"},
        {"label": "Pilote sur un poste", "sub": "Mois 2", "span": 4, "icon": "test"},
        {"label": "Documenter, former, dupliquer", "sub": "Mois 3", "span": 4, "icon": "clipboard"}]},
    "p15": {"type": "icons", "items": [
        {"label": "Production", "sub": "Responsable du poste", "icon": "person", "with": "example"},
        {"label": "Ingénierie", "sub": "Le conçoit", "icon": "gear", "with": "example"},
        {"label": "Qualité", "sub": "Le met à l'épreuve", "icon": "shield", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un gabarit ne se libère pas avant d'avoir compté les six vis. Quelle méthode de Poka "
                    "Yoke est-ce ?",
        "options": ["Méthode par contact", "Méthode à valeur fixe", "Méthode par étapes"],
        "correct": 1,
        "explanation": "Il confirme le bon nombre, c'est donc la méthode à valeur fixe. Le contact vérifie la "
                       "forme ou la position ; les étapes vérifient la séquence.",
        "q_script": "Vérification rapide. Un gabarit ne se libère pas avant d'avoir compté les six vis. "
                    "Quelle méthode de Poka Yoke est-ce ? Prenez quelques secondes.",
        "a_script": "C'est la méthode à valeur fixe. Elle confirme le bon nombre. Le contact vérifie la "
                    "forme, et les étapes vérifient la séquence.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un nouveau capteur de joint rejette tant de bonnes unités que les opérateurs commencent "
                    "à le contourner. Que doit faire l'équipe EN PREMIER ?",
        "options": ["Retirer le capteur", "Sanctionner les opérateurs",
                    "Maîtriser le contournement et corriger les faux rejets avec des échantillons vérifiés",
                    "Ajouter un panneau de rappel"],
        "correct": 2,
        "explanation": "Les faux rejets incitent au contournement. Verrouillez le contournement, puis améliorez "
                       "le positionnement, l'éclairage ou les seuils avec des échantillons bons et mauvais "
                       "connus, et suivez le taux de faux rejets.",
        "q_script": "Encore une, et cette fois c'est un scénario. Un nouveau capteur de joint rejette tant de "
                    "bonnes unités que les opérateurs commencent à le contourner. Que doit faire l'équipe en "
                    "premier ? Réfléchissez.",
        "a_script": "Maîtrisez le contournement, puis corrigez les faux rejets. Améliorez le réglage du "
                    "capteur, avec des échantillons bons et mauvais connus. Les faux rejets poussent les gens "
                    "à contourner un dispositif.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
