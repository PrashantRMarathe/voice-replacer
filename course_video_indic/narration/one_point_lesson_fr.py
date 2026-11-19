"""one_point_lesson in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh one_point_lesson_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "op_fr"
NAME = "one_point_lesson_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "One Point Lesson": "ouane poïnnte lèsseune",
    "Poka Yoke": "Poka Yoké",
    "Kaizen": "Kaïzène",
    "Gemba": "Guemba",
    "OPL": "o pé elle",
    "SOP": "esse o pé",
    "PCB": "pé cé bé",
    "AOI": "a o i",
    "ESD": "eu esse dé",
    "TPM": "té pé emme",
    "5S": "cinq esse",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Équipe de nuit. Un nouvel opérateur monte un connecteur à l'envers, et le fissure. "
    "L'équipe de jour connaissait l'astuce. Personne ne l'avait partagée. Ça vous dit quelque "
    "chose ? Dans cette leçon, vous allez découvrir la One Point Lesson. C'est une façon "
    "visuelle, sur une seule page, d'enseigner bien une seule chose, directement au poste de "
    "travail. Nous suivrons Ravi, superviseur d'équipe sur une ligne d'enregistreurs vidéo, "
    "qui crée ses premières."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Un sujet, un point clair, et un visuel fort. Enseignez-la "
    "au Gemba, et confirmez-la en observant le travail. Et maîtrisez-la, pour qu'elle "
    "corresponde toujours au standard en vigueur. Voici votre action pour cette semaine. "
    "Choisissez une erreur qui se répète, et rédigez un brouillon de One Point Lesson pour "
    "elle. Bravo d'avoir terminé cette leçon. Ensuite, vous découvrirez le Poka Yoke, le "
    "détrompage."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce qu'est une One Point Lesson",
        "points": [("Une chose, sur une page", "enseigne une seule chose sur une"),
                   ("Courte : apprise en quelques minutes", "Elle est courte"),
                   ("Visuelle : bons et mauvais exemples", "Elle est visuelle"),
                   ("Enseignée sur le lieu de travail", "elle est enseignée directement sur le lieu de travail")],
        "example": "La première OPL de Ravi, l'insertion du connecteur : la bonne prise, la mauvaise prise, "
                   "et le clic à écouter.",
        "example_cue": "La première de Ravi",
        "script": "Voici l'idée centrale. Une One Point Lesson, ou OPL, enseigne une seule chose sur une "
                  "seule page. Elle est courte, donc vous l'apprenez en quelques minutes. Elle est "
                  "visuelle, avec des photos et des exemples clairs de bon et de mauvais. Et elle est "
                  "enseignée directement sur le lieu de travail. La première de Ravi portait sur "
                  "l'insertion du connecteur. Une photo de la bonne prise, une de la mauvaise prise, et le "
                  "clic à écouter. Selon vous, que ne doit-elle jamais remplacer ?",
    },
    {
        "key": "p02", "num": 2, "title": "Ce qu'une OPL n'est pas",
        "points": [("Ne remplace jamais votre SOP", "Une OPL ne remplace jamais votre SOP"),
                   ("Pas un gros sujet tassé sur une page", "Elle ne tasse pas non plus"),
                   ("Renforce un point critique", "elle renforce un point critique")],
        "example": "La leçon sur le connecteur de Ravi est placée à côté du SOP et désigne l'étape exacte "
                   "qu'elle soutient.",
        "example_cue": "La leçon sur le connecteur de Ravi",
        "script": "Une OPL ne remplace jamais votre SOP. Ce n'est pas une instruction de travail, une "
                  "spécification complète, ni une certification. Elle ne tasse pas non plus un gros sujet "
                  "sur une page surchargée. Au contraire, elle renforce un point critique, pour que les "
                  "gens le retiennent. La leçon sur le connecteur de Ravi est placée juste à côté du SOP. "
                  "Elle désigne l'étape exacte qu'elle soutient. Le standard reste donc la référence, et "
                  "l'OPL le fait tenir. Pourquoi cela vaut-il l'effort ?",
    },
    {
        "key": "p03", "num": 3, "title": "Pourquoi les OPL sont rentables",
        "points": [("Ferme les écarts de compétence entre équipes", "Les OPL ferment les écarts de compétence"),
                   ("Les nouveaux apprennent plus vite", "Les nouveaux apprennent plus vite"),
                   ("Les leçons des défauts partagées vite", "Les leçons des défauts"),
                   ("Les opérateurs expérimentés deviennent formateurs", "vos opérateurs expérimentés")],
        "example": "L'équipe de nuit fissurait 14 connecteurs par semaine ; l'équipe de jour, 2. Même SOP, "
                   "savoir-faire différent.",
        "example_cue": "L'équipe de nuit de Ravi fissurait",
        "script": "Les OPL ferment les écarts de compétence entre les personnes et les équipes. L'équipe de "
                  "nuit de Ravi fissurait quatorze connecteurs par semaine. L'équipe de jour en fissurait "
                  "deux. Même SOP, mais savoir-faire différent. Une One Point Lesson diffuse ce "
                  "savoir-faire en quelques minutes. Les nouveaux apprennent plus vite. Les leçons des "
                  "défauts et des pannes sont partagées vite. Et vos opérateurs expérimentés deviennent "
                  "formateurs, ce qui crée une vraie appropriation. Le gain se voit en qualité, en sécurité "
                  "et en coût. Alors, quels types pouvez-vous faire ?",
    },
    {
        "key": "p04", "num": 4, "title": "Types d'OPL",
        "points": [("Connaissance de base, par ex. la manipulation ESD", "Une leçon de connaissance de base"),
                   ("Problème : défaut, cause et correction", "Une leçon problème"),
                   ("Amélioration : une meilleure méthode issue d'un Kaizen", "Une leçon amélioration"),
                   ("Sécurité · Qualité · Maintenance", "Il y a ensuite les leçons sécurité")],
        "example": "La leçon de Ravi sur le connecteur fissuré est de type problème.",
        "example_cue": "La leçon de Ravi sur le connecteur fissuré",
        "script": "Il existe six types courants. Une leçon de connaissance de base enseigne ce que tout le "
                  "monde doit savoir, comme la manipulation ESD. Une leçon problème explique un défaut, sa "
                  "cause et sa correction. Une leçon amélioration partage une meilleure méthode issue d'un "
                  "Kaizen. Il y a ensuite les leçons sécurité, qualité et maintenance. La leçon de Ravi sur "
                  "le connecteur fissuré est de type problème. Les noms peuvent varier sur votre site. La "
                  "règle, non. Un point clair. Alors, quand en faire une ?",
    },
    {
        "key": "p05", "num": 5, "title": "Quand en créer une",
        "points": [("Un défaut répété vient d'être résolu", "Un défaut répété vient"),
                   ("Nouveau produit, nouvelle machine ou nouveau gabarit", "Un nouveau produit"),
                   ("Une étape toujours mal comprise", "Une étape du SOP"),
                   ("Un presque-accident ou l'astuce d'un expert", "Un presque-accident")],
        "example": "Le déclencheur de Ravi : la cause des connecteurs fissurés était trouvée — la correction "
                   "devait maintenant atteindre chaque équipe.",
        "example_cue": "Pour Ravi, le déclencheur",
        "script": "Faites-en une quand un petit savoir peut changer un comportement. Un défaut répété vient "
                  "d'être résolu. Un nouveau produit, une nouvelle machine ou un nouveau gabarit arrive. "
                  "Une étape du SOP reste mal comprise. Un presque-accident révèle un écart. Ou une "
                  "personne expérimentée connaît une astuce que personne d'autre ne connaît. Pour Ravi, le "
                  "déclencheur était clair. La cause des connecteurs fissurés avait été trouvée. Maintenant "
                  "la correction devait atteindre chaque équipe. Que met-on sur la page ?",
    },
    {
        "key": "p06", "num": 6, "title": "La structure d'une bonne OPL",
        "points": [("Numéro, titre, révision, date", "Commencez par un numéro"),
                   ("Pourquoi c'est important + le seul point clé", "Puis dites pourquoi c'est important"),
                   ("Visuels, étapes, mise en garde", "Ajoutez les visuels"),
                   ("Responsable, approbation, enregistrement de formation", "Terminez par le responsable")],
        "example": "La page doit se comprendre d'un coup d'œil — votre opérateur le plus récent pourrait-il "
                   "la lire en une minute ?",
        "example_cue": "La page doit se comprendre",
        "script": "Chaque OPL suit la même mise en page, pour que les gens sachent où regarder. Commencez "
                  "par un numéro, un titre court, la révision et la date. Puis dites pourquoi c'est "
                  "important, et énoncez le seul point clé. Ajoutez les visuels et les étapes simples. "
                  "Incluez une mise en garde là où il y a un risque. Terminez par le responsable, "
                  "l'approbation et l'enregistrement de formation. La page doit se comprendre d'un coup "
                  "d'œil. Votre opérateur le plus récent pourrait-il lire la vôtre en une minute ?",
    },
    {
        "key": "p07", "num": 7, "title": "Comment la préparer",
        "points": [("Définir un objectif d'apprentissage", "définir un objectif d'apprentissage"),
                   ("Aller au Gemba, vérifier le standard", "Puis allez au Gemba"),
                   ("Mots simples, vraies photos, bon contre mauvais", "Ensuite, mettez-la"),
                   ("Vérifier, puis approuver", "Puis faites vérifier")],
        "example": "Ravi a photographié le vrai connecteur, au vrai poste.",
        "example_cue": "Ravi a photographié",
        "script": "Commencez par définir un objectif d'apprentissage. Puis allez au Gemba, et observez le "
                  "vrai travail. Vérifiez le standard approuvé et la cause racine. Ensuite, mettez-la dans "
                  "les mots simples qu'utilisent vos opérateurs. Ajoutez de vraies photos, des flèches et "
                  "des exemples bons et mauvais. Rédigez-la sur le modèle standard. Puis faites vérifier et "
                  "approuver par la qualité ou l'ingénierie. Ravi a photographié le vrai connecteur, au "
                  "vrai poste. Alors, comment rendre les visuels efficaces ?",
    },
    {
        "key": "p08", "num": 8, "title": "Communication visuelle",
        "points": [("Vraies photos, flèches sur l'endroit exact", "Utilisez de vraies photos"),
                   ("Bon et mauvais côte à côte", "Mettez le bon et le mauvais"),
                   ("Grand texte, beaucoup d'espace", "Utilisez un grand texte"),
                   ("Ne jamais utiliser la couleur comme seul signal", "n'utilisez jamais la couleur")],
        "example": "L'OPL de Ravi montre une coche, une croix, et les mots bon et pas bon.",
        "example_cue": "Ravi a ajouté une coche",
        "script": "Les visuels sont le cœur d'une OPL. Votre apprenant doit comprendre le point avant de "
                  "lire une seule phrase. Utilisez de vraies photos, avec des flèches et des cercles sur "
                  "l'endroit exact. Mettez le bon et le mauvais côte à côte. Utilisez un grand texte et "
                  "beaucoup d'espace. Évitez les longs paragraphes et le jargon. Et n'utilisez jamais la "
                  "couleur comme seul signal. Ravi a ajouté une coche, une croix, et les mots bon et pas "
                  "bon. Alors, comment l'enseigner vraiment ?",
    },
    {
        "key": "p09", "num": 9, "title": "Enseigner au Gemba",
        "points": [("Expliquer pourquoi c'est important", "Expliquez pourquoi c'est important"),
                   ("Montrer, démontrer, comparer", "Montrez la vraie pièce"),
                   ("Poser des questions, laisser essayer", "Posez des questions courtes"),
                   ("Une signature seule ne prouve rien", "Une signature seule")],
        "example": "Ravi enseigne chaque leçon en 5 minutes en début d'équipe, puis observe chaque opérateur "
                   "la faire.",
        "example_cue": "Ravi enseigne chaque leçon",
        "script": "Enseignez-la là où se fait le travail. Expliquez pourquoi c'est important, en termes de "
                  "qualité ou de sécurité. Montrez la vraie pièce. Démontrez lentement, puis comparez le "
                  "bon et le mauvais. Posez des questions courtes pour vérifier la compréhension. Laissez "
                  "l'apprenant essayer, et corrigez les erreurs sur le moment. Ravi enseigne chaque leçon "
                  "en cinq minutes en début d'équipe. Puis il observe chaque opérateur la faire. Une "
                  "signature seule ne prouve rien. Où d'autre les OPL peuvent-elles aider ?",
    },
    {
        "key": "p10", "num": 10, "title": "Les OPL pour l'assemblage final et la qualité",
        "points": [("Cartes : fausse alerte AOI ou vrai défaut", "Sur les cartes"),
                   ("Assemblage : séquence de vissage, verrouillage des connecteurs", "À l'assemblage"),
                   ("Test : contrôle de la version du firmware", "Au test"),
                   ("Emballage : contrôles d'étiquette et d'accessoires", "À l'emballage")],
        "example": "Éviter le mauvais PCB : où lire le numéro de la carte, comment vérifier le modèle, que "
                   "faire en cas d'écart.",
        "example_cue": "La leçon suivante de Ravi",
        "script": "Presque chaque processus a un bon sujet d'OPL. Sur les cartes, apprenez à distinguer une "
                  "fausse alerte AOI d'un vrai défaut. À l'assemblage, enseignez la séquence de vissage et "
                  "le verrouillage des connecteurs. Au test, enseignez le contrôle de la version du "
                  "firmware. À l'emballage, enseignez les contrôles d'étiquette et d'accessoires. La leçon "
                  "suivante de Ravi portait sur le mauvais PCB. Où lire le numéro de la carte, comment "
                  "vérifier le modèle, et que faire en cas d'écart. Quel sujet vous aiderait le plus ?",
    },
    {
        "key": "p11", "num": 11, "title": "Les OPL et les autres outils Lean",
        "points": [("Après un Kaizen : la nouvelle méthode", "Après un Kaizen"),
                   ("Après un Poka Yoke : ce que veut dire son alarme", "Après l'installation d'un Poka Yoke"),
                   ("Standards 5S et entretien des machines", "Elle enseigne les standards 5S"),
                   ("Les leçons de l'analyse des causes racines", "Elle partage les leçons")],
        "example": "Nouveau gabarit → une OPL sur la façon de le charger, et ce que veut dire le voyant "
                   "rouge.",
        "example_cue": "L'équipe de Ravi a installé",
        "script": "Les OPL aident les autres outils Lean à fonctionner sur le terrain. Après un Kaizen, une "
                  "OPL enseigne la nouvelle méthode. Après l'installation d'un Poka Yoke, elle explique "
                  "comment fonctionne le dispositif, et ce que veut dire son alarme. Elle enseigne les "
                  "standards 5S, et l'entretien de base des machines pour la TPM. Elle partage les leçons "
                  "de l'analyse des causes racines. L'équipe de Ravi a installé un nouveau gabarit. Son OPL "
                  "enseignait comment le charger, et ce que veut dire le voyant rouge. Mais comment garder "
                  "les OPL justes ?",
    },
    {
        "key": "p12", "num": 12, "title": "Maîtrise et révisions",
        "points": [("Numéro, responsable, approbateur", "Donnez-lui un numéro unique"),
                   ("Liée au SOP qu'elle soutient", "Liez-la au SOP"),
                   ("Revue à chaque changement", "Revoyez-la chaque fois"),
                   ("Anciennes copies retirées de la ligne", "Et retirez les anciennes copies")],
        "example": "Quand le fournisseur du connecteur a changé, Ravi a révisé la leçon et retiré chaque "
                   "ancienne copie.",
        "example_cue": "Quand le fournisseur du connecteur de Ravi",
        "script": "Une OPL est un document maîtrisé, même si elle est courte. Donnez-lui un numéro unique, "
                  "un responsable et un approbateur. Liez-la au SOP qu'elle soutient. Revoyez-la chaque "
                  "fois que le produit, le processus ou le standard change. Et retirez les anciennes copies "
                  "de la ligne. Quand le fournisseur du connecteur de Ravi a changé, il a révisé la leçon, "
                  "et retiré chaque ancienne copie. Voici la règle d'or. Une OPL ne doit jamais contredire "
                  "votre standard en vigueur. Alors, est-ce que ça a marché ?",
    },
    {
        "key": "p13", "num": 13, "title": "Mesurer l'efficacité",
        "points": [("Le résultat, c'est un comportement changé", "Un comportement changé est"),
                   ("Vérifier les connaissances par des questions", "Vérifiez donc les connaissances"),
                   ("Observer la méthode quelques jours après", "Puis observez la méthode"),
                   ("Suivre le défaut ciblé", "Et suivez le défaut")],
        "example": "Équipe de nuit : 14 connecteurs fissurés par semaine → 1 par semaine, six semaines après "
                   "la leçon.",
        "example_cue": "L'équipe de nuit de Ravi fissurait",
        "script": "Voici le vrai test. Terminer une formation n'est pas le résultat. Un comportement changé "
                  "est le résultat. Vérifiez donc les connaissances avec quelques questions. Puis observez "
                  "la méthode au Gemba, quelques jours après. Et suivez le défaut que vous visiez. L'équipe "
                  "de nuit de Ravi fissurait quatorze connecteurs par semaine. Six semaines après la leçon, "
                  "elle en fissurait un. Si un problème continue, ne vous contentez pas de reformer. "
                  "Regardez aussi le standard et le processus. Quelles erreurs faut-il éviter ?",
    },
    {
        "key": "p14", "num": 14, "title": "Erreurs fréquentes",
        "points": [("Trop de contenu → divisez", "Trop de contenu"),
                   ("Que du texte → ajoutez de vraies photos", "Que du texte"),
                   ("Que des signatures → démontrez et observez", "Que des signatures"),
                   ("Ancienne version au mur → maîtrise des révisions", "Une ancienne version")],
        "example": "Le premier brouillon de Ravi couvrait quatre sujets. Il l'a divisé en quatre leçons.",
        "example_cue": "Le premier brouillon de Ravi",
        "script": "Attention à quelques erreurs classiques. Trop de contenu sur une page ? Divisez-le. Que "
                  "du texte ? Ajoutez de vraies photos. Que des signatures ? Démontrez, questionnez et "
                  "observez. Une ancienne version au mur ? Utilisez la maîtrise des révisions. Pas de "
                  "vérification ? Suivez le défaut. Et n'utilisez jamais une OPL pour blâmer quelqu'un. Le "
                  "premier brouillon de Ravi couvrait quatre sujets. Il l'a divisé en quatre leçons. Prêt à "
                  "déployer les vôtres ?",
    },
    {
        "key": "p15", "num": 15, "title": "Feuille de route et check-list du rédacteur",
        "points": [("Planifier le modèle, la numérotation, l'approbation", "Planifiez votre modèle"),
                   ("Piloter sur les plus gros défauts ou risques", "Faites un pilote avec quelques leçons"),
                   ("Former les formateurs, utiliser au Gemba", "Formez les superviseurs"),
                   ("Mesurer l'effet, construire une bibliothèque", "Mesurez l'effet")],
        "example": "Avant la diffusion, demandez : est-elle juste ? Le point est-il évident ?",
        "example_cue": "Avant de diffuser une leçon",
        "script": "Déployez-la par phases simples. Planifiez votre modèle, la numérotation et le circuit "
                  "d'approbation. Faites un pilote avec quelques leçons sur vos plus gros défauts ou "
                  "risques de sécurité. Formez les superviseurs et les opérateurs expérimentés à les "
                  "enseigner. Puis utilisez-les aux réunions d'équipe et au Gemba. Mesurez l'effet, et "
                  "construisez une bibliothèque maîtrisée. Avant de diffuser une leçon, demandez-vous. "
                  "Est-elle juste ? Le point est-il évident ? Enseignez bien un point, et gardez-le à jour.",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Une chose", "icon": "check"}, {"label": "Quelques minutes pour apprendre", "icon": "clock"},
        {"label": "Visuelle", "icon": "camera"}, {"label": "Sur le lieu de travail", "icon": "wrench"}]},
    "p02": {"type": "versus", "items": [
        {"label": "Remplacer le SOP", "sub": "ou tasser un gros sujet", "icon": "cross", "with": 0},
        {"label": "À côté du SOP", "sub": "Désigne l'étape exacte", "icon": "clipboard", "with": 2}]},
    "p03": {"type": "compare", "before": {"label": "Équipe de nuit", "value": 14}, "after": {"label": "Équipe de jour", "value": 2},
            "unit": "connecteurs fissurés par semaine", "note": "Même SOP, savoir-faire différent", "with": "example"},
    "p04": {"type": "icons", "items": [
        {"label": "Connaissance de base", "icon": "chip", "with": 0}, {"label": "Problème", "icon": "warning", "with": 1},
        {"label": "Amélioration", "icon": "chartUp", "with": 2}, {"label": "Sécurité", "icon": "shield", "with": 3},
        {"label": "Qualité", "icon": "check", "with": 3}, {"label": "Maintenance", "icon": "wrench", "with": 3}]},
    "p05": {"type": "icons", "items": [
        {"label": "Défaut répété résolu", "icon": "check"}, {"label": "Nouveau produit ou gabarit", "icon": "box"},
        {"label": "Étape mal comprise", "icon": "search"}, {"label": "Presque-accident, ou astuce", "icon": "warning"}]},
    "p06": {"type": "doc", "items": [
        {"label": "OPL-012 · Insertion du connecteur · Rev B", "icon": "label", "with": 0},
        {"label": "Point clé : poussez jusqu'au clic", "icon": "key", "with": 1},
        {"label": "", "icon": "goodbad", "with": 2},
        {"label": "Attention : ne forcez jamais", "icon": "warning", "with": 2},
        {"label": "Responsable · approuvée · formés", "icon": "person", "with": 3}]},
    "p07": {"type": "flow", "items": [
        {"label": "Un objectif d'apprentissage", "icon": "search"},
        {"label": "Allez au Gemba", "sub": "Vérifiez le standard", "icon": "walk"},
        {"label": "Mots simples, vraies photos", "icon": "camera"},
        {"label": "Vérifier, puis approuver", "icon": "check", "tone": "good"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Vraies photos, flèches", "icon": "camera", "with": 0},
        {"label": "Bon et mauvais côte à côte", "icon": "shape", "with": 1},
        {"label": "Grand texte, espace", "icon": "label", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Couleur seule", "sub": "Tout le monde ne la voit pas", "icon": "warning"},
            {"label": "Coche, croix + mots", "sub": "Bon / pas bon", "icon": "check"}]}},
    "p09": {"type": "flow", "items": [
        {"label": "Expliquer pourquoi c'est important", "icon": "person"},
        {"label": "Montrer, démontrer, comparer", "icon": "camera"},
        {"label": "Questionner, puis laisser essayer", "icon": "hand"},
        {"label": "Une signature ne prouve rien", "icon": "cross", "tone": "bad"}]},
    "p10": {"type": "flow", "items": [
        {"label": "Cartes", "sub": "Fausse alerte AOI ou vrai défaut", "icon": "chip"},
        {"label": "Assemblage", "sub": "Séquence de vissage, verrouillage des connecteurs", "icon": "screw"},
        {"label": "Test", "sub": "Contrôle de version du firmware", "icon": "test"},
        {"label": "Emballage", "sub": "Étiquette et accessoires", "icon": "label"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Kaizen", "icon": "chartUp"}, {"label": "Poka Yoke", "icon": "key"},
        {"label": "5S + TPM", "icon": "tray"}, {"label": "Cause racine", "icon": "search"}]},
    "p12": {"type": "flow", "items": [
        {"label": "Numéro, responsable, approbateur", "icon": "label"},
        {"label": "Liée à son SOP", "icon": "clipboard"},
        {"label": "Revue à chaque changement", "icon": "sequence"},
        {"label": "Anciennes copies retirées", "icon": "trash", "tone": "good"}]},
    "p13": {"type": "icons", "items": [
        {"label": "Comportement changé", "icon": "person", "with": 0},
        {"label": "Quelques questions", "icon": "search", "with": 1},
        {"label": "Observer, quelques jours après", "icon": "clock", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Avant", "value": 14}, "after": {"label": "6 semaines après", "value": 1},
                 "unit": "connecteurs fissurés par semaine, équipe de nuit", "note": "La leçon a changé le comportement", "with": "example"}},
    "p14": {"type": "icons", "items": [
        {"label": "Trop ?", "sub": "Divisez-le", "icon": "stack"},
        {"label": "Que du texte ?", "sub": "Ajoutez de vraies photos", "icon": "camera"},
        {"label": "Que des signatures ?", "sub": "Observez le travail", "icon": "hand"},
        {"label": "Ancienne version ?", "sub": "Maîtrise des révisions", "icon": "sequence"}]},
    "p15": {"type": "steps", "items": [
        {"label": "Modèle + numérotation", "with": 0}, {"label": "Pilote sur les gros défauts", "with": 1},
        {"label": "Former les formateurs", "with": 2}, {"label": "Utiliser au Gemba", "with": 2},
        {"label": "Mesurer l'effet", "with": 3}, {"label": "Construire une bibliothèque", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Un brouillon d'OPL couvre l'insertion du connecteur, le couple de vissage, les contrôles "
                    "d'étiquette et l'ESD sur une page. Quel est le problème ?",
        "options": ["Il faut plus de texte", "Il y a trop de points — divisez-la en plusieurs OPL",
                    "Elle devrait être seulement en couleur"],
        "correct": 1,
        "explanation": "Une OPL enseigne UN point. Quatre sujets sur une page diluent le message — faites plutôt "
                       "quatre OPL ciblées.",
        "q_script": "Vérification rapide. Un brouillon de leçon couvre l'insertion du connecteur, le couple "
                    "de vissage, les contrôles d'étiquette et l'ESD, le tout sur une page. Quel est le "
                    "problème ? Prenez quelques secondes.",
        "a_script": "Il y a trop de points. Une One Point Lesson enseigne une seule chose. Divisez-la en "
                    "quatre leçons ciblées.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Tout le monde a signé l'OPL il y a deux semaines, mais le même défaut est revenu. Que "
                    "doit faire le superviseur EN PREMIER ?",
        "options": ["Faire signer tout le monde à nouveau", "Observer le travail et vérifier le standard, la méthode et la leçon",
                    "Blâmer les opérateurs qui ont signé", "Retirer l'OPL de la ligne"],
        "correct": 1,
        "explanation": "Les signatures ne prouvent pas l'apprentissage. Allez observer : la méthode est-elle "
                       "suivie, le standard est-il juste, l'OPL est-elle claire ? Puis corrigez la cause.",
        "q_script": "Encore une, et cette fois c'est un scénario. Tout le monde a signé la leçon il y a deux "
                    "semaines, mais le même défaut est revenu. Que doit faire le superviseur en premier ? "
                    "Réfléchissez.",
        "a_script": "Allez observer le travail. Vérifiez la méthode, le standard et la leçon elle-même. Une "
                    "signature ne prouve pas l'apprentissage, alors trouvez la vraie cause.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
