"""uniform_production in French, made from the Hindi lesson with tools/translate_lesson.py:
same pages, visuals and numbers. Voice: Microsoft French neural female voice (fr-FR-DeniseNeural).

  bash tools/build_hindi.sh uniform_production_fr --force     voice + level + sync
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402
import pronounce  # noqa: E402

ID = "up_fr"
NAME = "uniform_production_fr"
LANG = "fr"
VOICE = "fr-FR-DeniseNeural"   # female (user, 2 Nov 2026)

# English on screen/captions -> French script for the voice. Longest first.
SPOKEN = {
    "Heijunka": "Héïdjounka",
    "Kanban": "Kanne-banne",
    "Mura": "Moura",
    "Muri": "Mouri",
    "Muda": "Mouda",
    "TAKT": "takte",
    "EPEI": "eu pé eu i",
    "SMED": "smède",
    "WIP": "double vé i pé",
}


def say(text: str) -> str:
    for en in sorted(SPOKEN, key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9]){re.escape(en)}(?![A-Za-z0-9])", SPOKEN[en], text)
    return pronounce.fix(text, LANG)


INTRO_SCRIPT = (
    "Lundi, trois mille téléphones. Mardi, presque rien. Mercredi, le banc de test est noyé "
    "et la facture d'heures supplémentaires grimpe. Ça vous dit quelque chose ? Dans cette "
    "leçon, vous allez découvrir la production uniforme. Vous verrez comment lisser le volume "
    "et le mix, pour que votre ligne tourne à un rythme régulier qu'elle peut vraiment tenir. "
    "Nous suivrons Kavya, planificatrice de production dans une usine d'électronique, qui "
    "calme un planning très chaotique."
)
OUTRO_SCRIPT = (
    "Alors, trois choses à retenir. Lissez à la fois le volume et le mix, pour suivre la "
    "demande réelle. Vérifiez les goulots et les changements de série avant de faire "
    "confiance à un schéma. Et rendez le plan visible, avec des règles claires quand les "
    "choses changent. Voici votre action pour cette semaine. Trouvez un produit que vous "
    "fabriquez en gros lot, et esquissez un schéma plus petit qui se répète. Bravo d'avoir "
    "terminé cette leçon. Ensuite, vous allez cartographier toute votre chaîne de valeur."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Ce que veut dire la production uniforme",
        "points": [("Le lissage — Heijunka", "La production uniforme veut dire lisser"),
                   ("Lisser le volume et le mix", "Vous lissez à la fois"),
                   ("Un schéma de lancement régulier", "Les commandes irrégulières deviennent"),
                   ("Suivre la demande réelle, pas des quantités égales", "Mais lisser ne veut pas dire")],
        "example": "L'usine de Kavya fabrique des téléphones, des décodeurs et des appareils audio — en "
                   "petites séquences qui se répètent, pas tous les téléphones d'abord.",
        "example_cue": "L'usine de Kavya fabrique",
        "script": "Voici l'idée centrale. La production uniforme veut dire lisser. Le Lean appelle cela "
                  "Heijunka. Vous lissez à la fois le volume et le mix de ce que vous fabriquez, sur une "
                  "période fixée. Les commandes irrégulières deviennent un schéma de lancement régulier que "
                  "votre ligne peut vraiment tenir. Mais lisser ne veut pas dire fabriquer des quantités "
                  "égales de tout. Cela veut dire caler le mix et le rythme sur la demande réelle. L'usine "
                  "de Kavya fabrique des téléphones, des décodeurs et des appareils audio. Au lieu de tous "
                  "les téléphones d'abord, elle planifie de petites séquences qui se répètent. Pourquoi "
                  "est-ce important ?",
    },
    {
        "key": "p02", "num": 2, "title": "Pourquoi lisser compte",
        "points": [("La demande n'arrive jamais régulièrement", "La demande n'arrive presque jamais"),
                   ("Courir après les pics : heures supplémentaires, stock, qualité fragile", "Si vous courez après chaque pic"),
                   ("Le lissage lisse dans une fenêtre de planification", "Le lissage lisse vos lancements"),
                   ("Il faut encore un peu de tampon", "il vous faudra encore un peu de tampon")],
        "example": "Une grosse commande de téléphones est arrivée le lundi. Kavya l'a étalée sur la semaine, "
                   "comme la date de livraison le permettait.",
        "example_cue": "La semaine dernière, une grosse commande de téléphones",
        "script": "La demande n'arrive presque jamais régulièrement. Si vous courez après chaque pic, vous "
                  "avez des heures supplémentaires, des piles de produits finis, des fournisseurs "
                  "bousculés, et une qualité fragile. Le lissage lisse vos lancements dans une fenêtre de "
                  "planification convenue. Il n'efface pas les variations de la demande, et il vous faudra "
                  "encore un peu de tampon. La semaine dernière, une grosse commande de téléphones est "
                  "arrivée le lundi. Kavya ne l'a pas tout fabriquée ce jour-là. Elle l'a étalée sur la "
                  "semaine, parce que la date de livraison le permettait. Alors, qu'est-ce qui ne va pas "
                  "exactement quand le travail est irrégulier ?",
    },
    {
        "key": "p03", "num": 3, "title": "Mura, Muri et Muda",
        "points": [("Mura : l'irrégularité", "Mura, c'est l'irrégularité"),
                   ("Muri : la surcharge", "Muri, c'est la surcharge"),
                   ("Muda : le gaspillage", "Muda, c'est le gaspillage")],
        "example": "Le testeur traite ~2 000 unités par jour ; l'assemblage en a lancé plus de 3 000 au test "
                   "en un jour — une file s'est formée.",
        "example_cue": "Le testeur fonctionnel de Kavya",
        "script": "Le Lean nomme trois problèmes liés. Mura, c'est l'irrégularité. Muri, c'est la "
                  "surcharge. Muda, c'est le gaspillage. Voici comment ils se relient. Les lancements "
                  "irréguliers créent des pics. Les pics surchargent vos personnes et vos machines. Et la "
                  "surcharge engendre des défauts, de l'attente et du stock en plus. Le testeur fonctionnel "
                  "de Kavya traite environ deux mille unités par jour. Le mois dernier, l'assemblage en a "
                  "lancé plus de trois mille au test en un seul jour. L'assemblage a tenu son plan, mais "
                  "une file s'est formée au test. Voyez-vous cette chaîne sur votre propre ligne ?",
    },
    {
        "key": "p04", "num": 4, "title": "Lisser le volume",
        "points": [("Étaler la production sur un horizon", "Lisser le volume étale"),
                   ("Demande nette = demande + stock final − stock", "D'abord, calculez la demande nette"),
                   ("Diviser par les jours de production", "Puis divisez par les jours de production"),
                   ("Vérifier matières, rendement, disponibilité, effectif", "Vérifiez d'abord les matières")],
        "example": "30 000 unités de besoin net sur 5 jours = 6 000 bonnes unités par jour, régulièrement.",
        "example_cue": "Le besoin net de Kavya",
        "script": "Commencez par le volume. Lisser le volume étale votre production planifiée sur un "
                  "horizon raisonnable. D'abord, calculez la demande nette. C'est la demande client, plus "
                  "le stock final souhaité, moins le stock utilisable disponible. Puis divisez par les "
                  "jours de production disponibles. Le besoin net de Kavya cette semaine est de trente "
                  "mille unités, sur cinq jours. Cela fait six mille bonnes unités par jour, régulièrement. "
                  "Mais votre ligne peut-elle vraiment tenir cela ? Vérifiez d'abord les matières, le "
                  "rendement, la disponibilité et l'effectif.",
    },
    {
        "key": "p05", "num": 5, "title": "Lisser le mix",
        "points": [("De petits schémas répétés qui suivent la demande", "Lisser le mix répète"),
                   ("Le ratio vient de la demande", "C'est un ratio trois, deux, un"),
                   ("Vérifier changements de série, gabarits, pièces", "Vous devez vérifier les changements de série")],
        "example": "3 000 téléphones, 2 000 décodeurs, 1 000 audio → 3 : 2 : 1 → "
                   "Téléphone–Décodeur–Téléphone–Audio–Décodeur–Téléphone.",
        "example_cue": "Kavya a besoin de trois mille",
        "script": "Passons au mix. Lisser le mix répète vos produits en petits schémas qui suivent la "
                  "demande, au lieu d'un gros lot de chacun. Kavya a besoin de trois mille téléphones, deux "
                  "mille décodeurs, et mille appareils audio. C'est un ratio trois, deux, un. Un schéma de "
                  "six unités pourrait donc être téléphone, décodeur, téléphone, audio, décodeur, "
                  "téléphone. Mais voici le piège. Un joli schéma sur le papier n'est pas forcément "
                  "fabricable. Vous devez vérifier les changements de série, les gabarits et les pièces "
                  "d'abord. Alors, à quelle vitesse le schéma doit-il tourner ?",
    },
    {
        "key": "p06", "num": 6, "title": "Temps TAKT et pitch",
        "points": [("TAKT : le rythme exigé par le client", "Le TAKT est le rythme"),
                   ("Temps net ÷ bonnes unités nécessaires", "Divisez votre temps net disponible"),
                   ("Pitch : le temps pour lancer un lot", "Le pitch est le temps"),
                   ("TAKT moyen ≠ chaque modèle suit", "Un TAKT moyen ne")],
        "example": "Une unité toutes les 4,2 secondes → un pitch de 100 unités de 7 minutes.",
        "example_cue": "L'équipe de Kavya a besoin",
        "script": "C'est là qu'intervient le TAKT. Le TAKT est le rythme exigé par votre client. Divisez "
                  "votre temps net disponible par les bonnes unités nécessaires. Le lissage fixe ensuite "
                  "l'ordre concret des lancements à ce rythme. Le pitch est le temps pour lancer un lot, "
                  "souvent cent unités. L'équipe de Kavya a besoin d'une unité toutes les quatre virgule "
                  "deux secondes. Un pitch de cent unités fait donc sept minutes. Mais attention. Un TAKT "
                  "moyen ne prouve pas que chaque modèle peut suivre. Comment montrer le plan au terrain ?",
    },
    {
        "key": "p07", "num": 7, "title": "La boîte de lissage",
        "points": [("Un planning visuel", "C'est un planning visuel"),
                   ("Créneaux horaires en colonnes, produits en lignes", "Les créneaux horaires vont"),
                   ("Cartes : quoi lancer, combien", "Les cartes de chaque créneau"),
                   ("Créneaux manqués et manques visibles", "Les créneaux manqués")],
        "example": "Toutes les 30 minutes, le tableau de Kavya lance le lot suivant ; les kits sont préparés "
                   "dans cet ordre.",
        "example_cue": "Toutes les trente minutes",
        "script": "Avec une boîte de lissage. C'est un planning visuel. Les créneaux horaires vont en "
                  "colonnes, et les produits en lignes. Les cartes de chaque créneau montrent quoi lancer, "
                  "et combien. Toutes les trente minutes, le tableau de Kavya lance le lot suivant. Les "
                  "kits sont préparés dans cet ordre, pas par commodité. Les créneaux manqués et les "
                  "manques se voient d'un coup d'œil. Voici un test rapide pour votre ligne. Un opérateur "
                  "peut-il voir le prochain lancement, et qui appeler, sans rien demander à personne ?",
    },
    {
        "key": "p08", "num": 8, "title": "EPEI et changement de série",
        "points": [("Petits schémas = plus de changements de série", "Les petits schémas veulent dire"),
                   ("EPEI : chaque pièce à chaque intervalle", "L'EPEI mesure"),
                   ("SMED : réglage hors temps d'arrêt", "C'est pourquoi le SMED compte")],
        "example": "6 changements par jour : de 20 à 8 minutes = 72 minutes regagnées chaque jour.",
        "example_cue": "Les six changements quotidiens de Kavya",
        "script": "Les petits schémas veulent dire plus de changements de série. L'EPEI mesure à quelle "
                  "fréquence vous faites chaque pièce. Il veut dire chaque pièce à chaque intervalle. Kavya "
                  "fabrique chaque famille une fois par jour, donc son EPEI est d'un jour. Fabriquer "
                  "chacune deux fois par équipe répond plus vite, mais double les changements de série. "
                  "C'est pourquoi le SMED compte. Vous sortez le travail de réglage du temps d'arrêt. Les "
                  "six changements quotidiens de Kavya sont passés de vingt minutes à huit. Cela fait "
                  "soixante-douze minutes regagnées chaque jour. Où votre ligne perd-elle du temps ?",
    },
    {
        "key": "p09", "num": 9, "title": "Goulots et modèles mélangés",
        "points": [("Le lissage ne bat pas une limite de capacité", "Le lissage ne peut pas dépasser"),
                   ("Charger les postes avec le mix réel", "Vous devez charger chaque poste"),
                   ("Ne pas bloquer le modèle le plus lent", "Et si elle planifie")],
        "example": "40 % des unités demandent un test de 12 secondes = environ 340 tests/heure contre ~300 "
                   "pour un testeur. Ajoutez un deuxième testeur.",
        "example_cue": "Quarante pour cent des unités",
        "script": "Voici une dure vérité. Le lissage ne peut pas dépasser une vraie limite de capacité. "
                  "Vous devez charger chaque poste avec le mix réel, pas avec la moyenne. Kavya a vérifié "
                  "sa zone de test. Quarante pour cent des unités demandent un test de douze secondes. Cela "
                  "fait environ trois cent quarante tests par heure. Un testeur en fait environ trois "
                  "cents, avant même les pertes. Il lui faut donc un deuxième testeur, quelle que soit la "
                  "séquence. Et si elle planifie le modèle le plus lent en un seul long bloc, le testeur "
                  "est noyé. Connaissez-vous votre modèle le plus lent ?",
    },
    {
        "key": "p10", "num": 10, "title": "Kanban et maîtrise du WIP",
        "points": [("Kanban : quoi réapprovisionner, quand", "Les signaux Kanban disent"),
                   ("Contenants standard, couloirs premier entré, premier sorti", "Les contenants standard"),
                   ("Les limites de WIP arrêtent la surproduction", "Les limites de WIP arrêtent"),
                   ("Kits calés sur le pitch et le mix", "Calez votre rythme de kits")],
        "example": "Un kit de décodeur manquait — l'équipe l'a noté et a suivi la règle de replanification "
                   "approuvée.",
        "example_cue": "Mardi dernier",
        "script": "Un planning lissé a besoin de matières régulières. Les signaux Kanban disent au magasin "
                  "quoi réapprovisionner, et quand. Les contenants standard et les couloirs premier entré, "
                  "premier sorti évitent que la ligne manque de matière. Les limites de WIP arrêtent la "
                  "surproduction en amont. Calez votre rythme de kits sur le pitch et le mix. Mardi "
                  "dernier, un kit de décodeur manquait. L'équipe de Kavya n'a pas glissé discrètement une "
                  "autre pièce. Elle l'a noté, et a suivi la règle de replanification approuvée. Que ferait "
                  "votre équipe ?",
    },
    {
        "key": "p11", "num": 11, "title": "Gérer les changements de demande",
        "points": [("Une fenêtre proche gelée", "Il vous faut donc un horizon de planification"),
                   ("La replanification au poste crée le chaos", "Une replanification constante"),
                   ("Décider qui approuve les changements", "Décidez qui peut approuver")],
        "example": "500 appareils audio demandés plus tôt : Kavya a d'abord vérifié échéances, stock, pièces "
                   "et capacité de test.",
        "example_cue": "Un matin, un client",
        "script": "La demande changera quand même. Il vous faut donc un horizon de planification, et une "
                  "fenêtre proche gelée ou très encadrée. Une replanification constante au poste crée le "
                  "chaos. Décidez qui peut approuver un changement de séquence, et pourquoi. Un matin, un "
                  "client a demandé cinq cents appareils audio plus tôt. Kavya ne les a pas simplement fait "
                  "passer devant. Elle a d'abord vérifié les échéances, les produits finis, les composants "
                  "et la capacité de test. Puis elle a modifié les prochains créneaux de lancement. Qui "
                  "approuve les changements sur votre ligne ?",
    },
    {
        "key": "p12", "num": 12, "title": "KPI de lissage",
        "points": [("Suivre production et stabilité ensemble", "Suivez la production et la stabilité"),
                   ("Respect du planning", "Le respect du planning compare"),
                   ("Jours de WIP", "Les jours de WIP montrent"),
                   ("Plus FPY, arrêts, heures supplémentaires", "Ajoutez le rendement au premier passage")],
        "example": "95 % des unités planifiées faites. 12 000 unités de WIP = 2 jours de production.",
        "example_cue": "La ligne de Kavya a terminé",
        "script": "Comment savoir que le lissage marche ? Suivez la production et la stabilité ensemble. Le "
                  "respect du planning compare ce que vous avez terminé à ce que vous aviez prévu. La ligne "
                  "de Kavya a terminé quatre-vingt-quinze pour cent de ses unités planifiées. Les jours de "
                  "WIP montrent combien de temps le travail attend. Ses douze mille unités de WIP "
                  "représentent deux jours de production. Ajoutez le rendement au premier passage, les "
                  "arrêts et les heures supplémentaires. Sinon vous pourriez améliorer le respect du "
                  "planning et nuire discrètement à la qualité. Quels chiffres votre équipe revoit-elle "
                  "chaque jour ?",
    },
    {
        "key": "p13", "num": 13, "title": "Cas pratique : ligne partagée",
        "points": [("Mix 3 : 2 : 1, TAKT de 4,2 s", "Le mix est trois"),
                   ("Schéma de 60 unités : 30 · 20 · 10", "Elle essaie un schéma de soixante"),
                   ("Vérifier gamme, outillage, limites de test", "Mais d'abord, elle vérifie"),
                   ("Changements plus rapides, sans raccourcis", "Elle a accéléré les changements de série")],
        "example": "Un schéma environ toutes les quatre minutes en théorie — mais ses réglages étaient trop "
                   "lents pour ce rythme.",
        "example_cue": "En théorie, cela fait un schéma",
        "script": "Assemblons tout sur la ligne partagée de Kavya. Le mix est trois, deux, un. Le TAKT "
                  "moyen est de quatre virgule deux secondes. Elle essaie un schéma de soixante unités. "
                  "Trente téléphones, vingt décodeurs, et dix appareils audio. En théorie, cela fait un "
                  "schéma environ toutes les quatre minutes. Mais d'abord, elle vérifie la gamme, "
                  "l'outillage partagé, et les limites de test de chaque produit. Ses réglages se sont "
                  "révélés trop lents pour ce rythme. Alors, qu'a-t-elle fait ? Elle a accéléré les "
                  "changements de série, au lieu de forcer des raccourcis dangereux. Et vous ?",
    },
    {
        "key": "p14", "num": 14, "title": "Erreurs fréquentes",
        "points": [("Lisser sur le temps brut", "Lisser sur le temps brut"),
                   ("Des quantités égales pour un mix inégal", "Imposer des quantités égales"),
                   ("Plus de production que la ligne ne peut faire", "Planifier plus de bonne production"),
                   ("Sauter les contrôles de première pièce pour rattraper", "ne sautez jamais les contrôles de première pièce")],
        "example": "Testeurs firmware en panne pendant que le tableau demandait des décodeurs : plus de WIP "
                   "ne fait que déplacer le goulot. Escaladez.",
        "example_cue": "Un jour, le tableau de Kavya",
        "script": "Un plan peut paraître lissé sur le papier alors que le terrain reste chaotique. "
                  "Attention à ces erreurs. Lisser sur le temps brut, en ignorant les pauses et les pertes. "
                  "Imposer des quantités égales quand le mix de votre client ne l'est pas. Planifier plus "
                  "de bonne production que votre ligne ne peut vraiment en faire. Un jour, le tableau de "
                  "Kavya demandait des décodeurs, mais les testeurs firmware étaient en panne. Lancer plus "
                  "de travail n'aurait fait que déplacer le goulot. Elle a donc escaladé et mis le plan à "
                  "jour. Et ne sautez jamais les contrôles de première pièce pour rattraper.",
    },
    {
        "key": "p15", "num": 15, "title": "Feuille de route sur 90 jours",
        "points": [("Une famille, un horizon", "Commencez petit"),
                   ("Jours 1–30 : demande, mix, TAKT, réglages", "Pendant les trente premiers jours"),
                   ("Jours 31–60 : tableau pilote, kits, changements de série", "Pendant les trente suivants"),
                   ("Jours 61–90 : vérifier, standardiser, étendre", "Pendant les trente derniers")],
        "example": "La planification fixe les lancements, la production fabrique, l'ingénierie vérifie la "
                   "capacité, la qualité protège les contrôles, les matières gardent les kits prêts.",
        "example_cue": "La planification fixe les lancements",
        "script": "Commencez petit, avec une famille de produits et un horizon de planification. Pendant "
                  "les trente premiers jours, cartographiez la demande, le mix, le TAKT, les goulots et les "
                  "réglages. Pendant les trente suivants, faites un pilote de votre tableau de lissage, du "
                  "rythme des kits, et de changements plus rapides. Pendant les trente derniers, vérifiez "
                  "le rendement, le respect du planning et la livraison. Puis standardisez et étendez. "
                  "Donnez à chacun un rôle clair. La planification fixe les lancements, la production "
                  "fabrique, et l'ingénierie vérifie la capacité. La qualité protège les contrôles, et les "
                  "matières gardent les kits prêts. Qui porterait votre pilote ?",
    },
]

# The picture beside each page's boxes (same layout as the English lesson).
VISUALS = {
    "p01": {"type": "versus", "items": [
        {"label": "Tous les téléphones d'abord", "sub": "Puis les décodeurs, puis l'audio", "icon": "stack", "with": 1},
        {"label": "Petites séquences répétées", "sub": "Calées sur la demande réelle", "icon": "sequence", "with": "example"}]},
    "p02": {"type": "icons", "items": [
        {"label": "La demande est irrégulière", "icon": "wave"}, {"label": "Courir après les pics", "sub": "Heures supplémentaires, stock", "icon": "clock", "tone": "bad"},
        {"label": "Lisser les lancements", "icon": "sequence"}, {"label": "Un peu de tampon", "icon": "box"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Tout fabriquer le lundi", "sub": "Heures supplémentaires, test bousculé", "icon": "stack"},
            {"label": "Étalé sur la semaine", "sub": "La date de livraison le permettait", "icon": "calendar"}]}},
    "p03": {"type": "flow", "items": [
        {"label": "Mura", "sub": "Les lancements irréguliers créent des pics", "icon": "wave", "tone": "bad", "with": 0},
        {"label": "Muri", "sub": "Les pics surchargent personnes et machines", "icon": "weight", "tone": "bad", "with": 1},
        {"label": "Muda", "sub": "Défauts, attente, stock", "icon": "trash", "tone": "bad", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "Une file se forme au test", "unit": "unités en un jour", "with": "example", "items": [
            {"label": "Le testeur peut faire", "value": 2000, "tone": "good", "with": "example"},
            {"label": "Lancées", "value": 3200, "tone": "bad", "with": "example"}]}},
    "p04": {"type": "icons", "items": [
        {"label": "Un horizon raisonnable", "icon": "calendar"}, {"label": "Demande nette", "icon": "count"},
        {"label": "÷ jours de production", "icon": "sequence"}, {"label": "Vérifier que ça tient", "icon": "search"}],
        "then": {"type": "stat", "value": 6000, "icon": "chartUp", "label": "bonnes unités par jour, chaque jour",
                 "unit": "30 000 unités de besoin net ÷ 5 jours", "with": "example"}},
    "p05": {"type": "steps", "items": [
        {"label": "Téléphone", "sub": "P", "with": "example"}, {"label": "Décodeur", "sub": "B", "with": "example"},
        {"label": "Téléphone", "sub": "P", "with": "example"}, {"label": "Audio", "sub": "A", "with": "example"},
        {"label": "Décodeur", "sub": "B", "with": "example"}, {"label": "Téléphone", "sub": "P", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Le rythme du client", "icon": "clock", "with": 0},
        {"label": "Temps net ÷ bonnes unités", "icon": "count", "with": 1},
        {"label": "Pitch", "sub": "Temps pour lancer un lot", "icon": "box", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Une unité toutes les 4,2 s", "icon": "clock", "with": "example"},
            {"label": "× un lot de 100 unités", "icon": "box", "with": "example"},
            {"label": "= un pitch de 7 minutes", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "doc", "items": [
        {"label": "Boîte de lissage · ligne partagée", "icon": "calendar", "with": 0},
        {"label": "08:00  Téléphone · Décodeur · Téléphone", "icon": "sequence", "with": 1},
        {"label": "08:30  Audio · Décodeur · Téléphone", "icon": "sequence", "with": 1},
        {"label": "09:00  Lot suivant : kits prêts", "icon": "box", "with": 2},
        {"label": "Créneau manqué ? Visible tout de suite", "icon": "warning", "with": 3}]},
    "p08": {"type": "icons", "items": [
        {"label": "Plus de changements de série", "icon": "sequence", "with": 0},
        {"label": "EPEI", "sub": "Chaque pièce à chaque intervalle", "icon": "calendar", "with": 1},
        {"label": "SMED", "sub": "Réglage hors temps d'arrêt", "icon": "wrench", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Avant", "value": 20}, "after": {"label": "Après le SMED", "value": 8},
                 "suffix": " min", "unit": "par changement de série, six par jour", "note": "72 minutes regagnées chaque jour", "with": "example"}},
    "p09": {"type": "bars", "label": "Un testeur", "value": 300, "note": "insuffisant avant même les pertes : ajoutez un deuxième testeur", "unit": "tests par heure (40 % des unités demandent un test de 12 s)", "items": [
        {"label": "Tests nécessaires", "value": 343, "tone": "bad", "with": "example"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Signaux Kanban", "icon": "label"}, {"label": "Couloirs FIFO", "icon": "sequence"},
        {"label": "Limites de WIP", "icon": "stack"}, {"label": "Kits au rythme du pitch", "icon": "tray"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Une fenêtre gelée", "icon": "lock", "with": 0},
        {"label": "Replanification au poste", "sub": "Crée le chaos", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Qui approuve", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "500 audio demandés plus tôt", "icon": "box", "with": "example"},
            {"label": "Vérifier dates, stock, pièces, test", "icon": "search", "with": "example"},
            {"label": "Puis modifier les créneaux suivants", "icon": "sequence", "tone": "good", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Production + stabilité", "icon": "chartUp"}, {"label": "Respect du planning", "icon": "check"},
        {"label": "Jours de WIP", "icon": "clock"}, {"label": "FPY, arrêts, heures supplémentaires", "icon": "shield"}],
        "then": {"type": "stat", "value": 95, "suffix": "%", "icon": "check", "label": "des unités planifiées terminées",
                 "unit": "12 000 unités de WIP = 2 jours de production", "with": "example"}},
    "p13": {"type": "stat", "value": 4.2, "decimals": 1, "suffix": " s", "icon": "clock", "label": "TAKT moyen, mix 3 : 2 : 1",
            "unit": "téléphones : décodeurs : audio", "with": 0,
            "then": {"type": "bars", "label": "", "note": "Un schéma toutes les 4 minutes environ", "unit": "unités dans un schéma de 60 unités", "with": 1, "items": [
                {"label": "Téléphones", "value": 30, "with": 1}, {"label": "Décodeurs", "value": 20, "with": 1},
                {"label": "Audio", "value": 10, "with": 1}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Temps brut", "icon": "clock", "tone": "bad"}, {"label": "Quantités égales", "icon": "scale", "tone": "bad"},
        {"label": "Surplanification", "icon": "stack", "tone": "bad"}, {"label": "Sauter la première pièce", "icon": "warning", "tone": "bad"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Demande, mix, TAKT, réglages", "sub": "Jours 1–30", "icon": "clipboard", "with": 1},
        {"label": "Tableau pilote, kits, changements de série", "sub": "31–60", "icon": "calendar", "with": 2},
        {"label": "Vérifier, standardiser, étendre", "sub": "61–90", "icon": "chartUp", "with": 3}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Planification", "icon": "calendar", "with": "example"}, {"label": "Production", "icon": "wrench", "with": "example"},
            {"label": "Ingénierie", "icon": "gear", "with": "example"}, {"label": "Qualité", "icon": "shield", "with": "example"},
            {"label": "Matières", "icon": "box", "with": "example"}]}},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p06",
        "question": "Kavya a besoin de 3 000 téléphones, 2 000 décodeurs et 1 000 appareils audio. Quelle "
                    "séquence a un mix lissé ?",
        "options": ["Tous les téléphones, puis tous les décodeurs, puis tout l'audio", "Téléphone–Décodeur–Téléphone–Audio–Décodeur–Téléphone, répété",
                    "Un de chaque produit, à tour de rôle"],
        "correct": 1,
        "explanation": "Le schéma répété suit le ratio de demande 3 : 2 : 1. Les gros lots créent des pics ; les "
                       "quantités égales ignorent le mix réel.",
        "q_script": "Vérification rapide. Kavya a besoin de trois mille téléphones, deux mille décodeurs, et "
                    "mille appareils audio. Quelle séquence a un mix lissé ? Prenez quelques secondes.",
        "a_script": "Le schéma répété. Téléphone, décodeur, téléphone, audio, décodeur, téléphone. Il suit la "
                    "demande. Des quantités égales ignorent le mix réel.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Un client veut soudain 500 appareils audio plus tôt. Que doit faire Kavya EN PREMIER ?",
        "options": ["Les mettre dans le tout prochain créneau", "Vérifier les échéances, le stock, les pièces et la capacité de test, puis modifier les "
                                                                                                            "créneaux",
                    "Refuser — le planning est gelé", "Ajouter des heures supplémentaires et tout fabriquer aujourd'hui"],
        "correct": 1,
        "explanation": "Vérifiez d'abord l'impact, puis modifiez les prochains créneaux de lancement selon les "
                       "règles convenues. Passer devant à l'aveugle, ou refuser d'emblée, crée des problèmes.",
        "q_script": "Encore une, et cette fois c'est un scénario. Un client veut soudain cinq cents appareils "
                    "audio plus tôt. Que doit faire Kavya en premier ? Réfléchissez.",
        "a_script": "Vérifiez d'abord l'impact. Les échéances, les produits finis, les composants et la "
                    "capacité de test. Puis modifiez les prochains créneaux de lancement, selon les règles "
                    "convenues. Passer devant à l'aveugle, ou refuser d'emblée, crée des problèmes.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
