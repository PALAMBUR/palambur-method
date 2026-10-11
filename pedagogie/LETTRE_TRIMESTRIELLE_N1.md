# Lettre trimestrielle « La Méthode » · numéro 1 · gabarit

**Gabarit du premier numéro.** Trois rubriques fixes, dans cet ordre : ce qui a changé, un cas, une règle de droit. Six cents mots au plus, lue en quatre minutes. L’envoi revient à Victor ; ce fichier donne le texte prêt à relire, avec les trous marqués et listés en fin de fichier. Aucun prix, aucune adresse, aucun nom de personne.

---

**Objet : La Méthode · n° 1 · [À DÉCIDER : mois et année]**

Madame, Monsieur,

Vous avez installé le skill « Méthode Palambur », ou vous vous êtes inscrit pour en suivre les versions. Cette lettre paraît quatre fois par an. Elle dit ce qui a changé dans le skill, raconte un cas, et rappelle une règle de droit en une phrase. Elle ne vend rien.

## Ce qui a changé

**Version [À COMPLÉTER : numéro de version, lue dans CHANGELOG.md]**, publiée le [À COMPLÉTER : date, lue dans CHANGELOG.md].

- **Dix exemples complets** dans `exemples/` : une demande par gabarit (offre d’emploi, relance, devis, contrat, certificat, avertissement, refus de candidat, offre commerciale, note interne, compte rendu), avec les questions posées, le Gabarit rempli et le livrable, sur des données fictives.
- **Un dossier `pedagogie/`** : le manifeste « Pourquoi questionner avant de produire », une foire aux questions, un glossaire des textes de loi que le skill nomme, la fiche imprimable « Le Gabarit Palambur », et les scripts d’un cours en vingt minutes.
- **Le `README` en allemand et en italien**, en attente de relecture par un locuteur natif ; si vous lisez l’une de ces langues, votre relecture est bienvenue.
- [À COMPLÉTER : les autres changements du trimestre, lus dans CHANGELOG.md, deux au plus]

Le détail est dans le [journal des versions](https://github.com/PALAMBUR/palambur-method/blob/main/CHANGELOG.md). Une copie installée se met à jour par `git pull` ou par la nouvelle version du plugin, jamais en éditant les fichiers sur place.

## Un cas

Une fiduciaire de Suisse romande (fictive, comme tous les cas de cette lettre) demande : « [prénom] quitte la fiduciaire fin novembre, comptable depuis 2021, prépare son certificat ».

Sans la Méthode, l’IA rend un certificat complet en dix secondes : des tâches plausibles, une appréciation élogieuse, une formule de départ « d’un commun accord ». Rien de tout cela n’a été dit.

Avec la Méthode, le skill demande d’abord s’il doit anonymiser le nom (il le fait par défaut), puis pose trois questions : le type de certificat, la qualité du travail, le comportement. L’utilisateur répond « très bonne ; a repris seul·e le portefeuille de bouclements d’une collègue partie en 2024 ». Le certificat porte cette seule réalisation, laisse les tâches en `[À COMPLÉTER : reprendre le cahier des charges]`, ne mentionne pas les circonstances du départ, et ajoute une note interne : à soumettre à la personne, puis au supérieur, avant signature.

Ce qui a été gagné ne se voit pas dans le texte : c’est l’éloge non étayé qui n’y est pas, et la formule « d’un commun accord » que personne n’avait demandée. L’exemple complet est dans `exemples/05-certificat-travail.md`.

## Une règle de droit

**Le certificat de travail est dû à la demande de la personne, et il doit être à la fois véridique et bienveillant** ; c’est le Code des obligations qui le dit `[À VÉRIFIER : base légale]`. Un certificat qui tait une insuffisance établie manque à la vérité ; un certificat qui glisse une formule codée (« s’est efforcé·e de ») manque à la bienveillance. Le skill refuse les deux et laisse la vérification de l’article à la personne qui relit.

## La suite

Le prochain atelier de quarante-cinq minutes a lieu le [À DÉCIDER : date] ; l’invitation suit. Pour signaler un défaut ou proposer un gabarit : [les tickets du dépôt](https://github.com/PALAMBUR/palambur-method/issues).

Avec nos salutations les meilleures,

[Fonction] · Palambur

*Vous recevez cette lettre parce que vous l’avez demandée. Un lien de désinscription figure sous chaque numéro. Vos données sont traitées en Suisse, conformément à la nLPD.*

---

## Ce qui reste à faire avant envoi

- `[À DÉCIDER : mois et année]` · le premier numéro n’a pas de date ; le plan fixe le rythme trimestriel, pas le point de départ.
- `[À COMPLÉTER : numéro de version]`, `[À COMPLÉTER : date]` · à lire dans `CHANGELOG.md` au moment de l’envoi, jamais recopiés d’ici.
- `[À COMPLÉTER : autres changements du trimestre]` · deux au plus, lus dans `CHANGELOG.md`.
- `[À DÉCIDER : date]` du prochain atelier · même décision que `pedagogie/ATELIER_45_MIN.md`.
- `[À DÉCIDER : outil d’envoi]` · l’outil doit poser le lien de désinscription et traiter les adresses en Suisse ; signaler toute dépendance non suisse.
- `[À VÉRIFIER : base légale]` · la règle de droit est nommée, pas numérotée ; une relecture juridique avant envoi.
- Relecture typographique : `python3 outils/regle_typo.py pedagogie/LETTRE_TRIMESTRIELLE_N1.md`.
