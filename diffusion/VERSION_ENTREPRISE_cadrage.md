# Version entreprise du skill · note de cadrage (points 29, 76 et 77)

**Brouillon · 11.10.2026 · session Skills et Prompt Ingénierie · complété le soir du même jour (points 76 et 77).** Rien n’est vendu, rien n’est construit. Cette note situe l’offre, dit ce qu’elle contient, ce qu’elle exige de Palambur, et comment elle se livre. **Le prix n’est pas écrit ici** : il se décide dans la grille tarifaire, qui fait foi.

## Ce qui reste gratuit, quoi qu’il arrive

**Tout ce que le dépôt public contient, dans chaque version** : la méthode, les gabarits de livrables, les fiches métier, le mode relecture, les références juridiques, les épreuves, les adaptations pour les autres IA. La promesse du `README.md` (« gratuit et le restera ») **porte sur le dépôt entier**, pas sur un sous-ensemble ; aucune fiche, aucun gabarit, aucune mise à jour de droit du dépôt public ne passe derrière un paiement. Ce que les deux offres ci-dessous vendent, c’est **du service autour du skill** : le pré-réglage pour une entreprise, le temps d’une personne qui installe et vérifie, la tenue à jour d’une version client.

## En une phrase

**Le skill public montre la Méthode sur une demande ; la version entreprise la pré-règle pour un client** : sa charte, ses conventions collectives, son ton, ses signatures, ses livrables types, installée dans l’outil que le client utilise déjà (Claude Code ou Projet ChatGPT), et tenue à jour.

## Pourquoi cette offre existe

Le skill gratuit pose les bonnes questions, mais il **repart de zéro à chaque demande** : il demande le canton, la convention collective, le ton, la signature. Dans une entreprise, ces réponses sont **toujours les mêmes**. Une version pré-réglée les connaît d’avance, ne pose plus que les questions propres à la demande du jour, et rend un livrable déjà dans la voix du client. C’est le gain des « trois minutes de plus » (point 9 du plan) rapporté à une seule entreprise, livrable après livrable.

C’est aussi le **produit dérivé naturel de la formation** « Le Collaborateur, augmenté » : la formation apprend la Méthode, la version entreprise la fait tenir sans effort dans les habitudes de l’équipe.

## Ce qu’elle contient

| Pièce | Contenu | Source dans le dépôt public |
|---|---|---|
| **Le skill de base** | `SKILL.md`, `methode-palambur.md`, `protection-donnees.md`, à la version numérotée du jour | identique au public, jamais une copie divergente |
| **Le fichier d’entreprise** | charte rédactionnelle (ton, vouvoiement ou tutoiement interne, formules d’ouverture et de clôture), signatures et coordonnées, mentions légales de l’entreprise, canton et langue par défaut | nouveau · un fichier `entreprise.md` chargé en premier |
| **Les conventions collectives applicables** | nommées, avec leur source et leur date de vérification ; le skill les cite, il ne les invente jamais | nouveau · table `references-juridiques.md` restreinte au client |
| **Les gabarits de livrables du client** | les cinq à dix livrables que l’entreprise rédige le plus, au Gabarit, avec leurs champs DONNÉES pré-remplis quand ils sont constants | dérivés de `gabarits/` (point 9), adaptés |
| **Le ou les métiers** | le fichier métier correspondant (point 10), version complète | dérivé de `metiers/` et de Chaptal |
| **Le mode relecture** | passer au crible un document existant du client sans question (point 11) | identique au public |
| **Le jeu d’épreuves du client** | dix demandes réelles du client, anonymisées, avec le comportement attendu, rejoué avant chaque mise à jour | dérivé de `epreuves/` (point 6) |

Ce qu’elle **ne contient pas** : aucune donnée nominative de clients du client, aucun document confidentiel stocké dans le skill. Le fichier d’entreprise porte des règles, pas des dossiers.

## Ce qu’elle exige de Palambur

1. **Un atelier de cadrage** avec le client (une demi-journée) : relever la charte, les livrables fréquents, les conventions collectives applicables, les signatures. Sans cet atelier, on pré-règle à l’aveugle.
2. **La rédaction** du fichier d’entreprise et des gabarits, puis le jeu d’épreuves.
3. **La chaîne de contrôle** (point 30) jouée sur la version client : typographie, zéro mot interdit, épreuves vertes, et une étiquette de version propre au client.
4. **L’installation** chez le client, et la vérification sur un vrai cas en séance.
5. **La tenue à jour** : à chaque version mensuelle du skill public, la version client est rejouée sur ses épreuves et mise à jour. C’est ce qui justifie une part récurrente.

Deux points à trancher avant la première vente :

- **Où vit la version client** `[À DÉCIDER par Victor]` · un dépôt GitHub privé par client (traçable, versionné, Palambur garde la main), ou un dossier remis au client (simple, mais plus de mise à jour possible sans retour chez Palambur). La règle « mémoire sur trois nuages » (07.10.2026) penche pour le dépôt privé.
- **Ce que Palambur voit** · rien. La version entreprise, comme la publique, **n’envoie rien à Palambur**. La mesure d’usage, si le client la veut, se fait chez lui.

## Livraison

| Étape | Ce qui est livré | Délai indicatif |
|---|---|---|
| 1 | Compte rendu de l’atelier de cadrage, liste des livrables retenus | sous une semaine après l’atelier |
| 2 | Version client installée, jeu d’épreuves vert, démonstration sur un cas réel | `[À DÉCIDER : délai, selon le nombre de gabarits]` |
| 3 | Mise à jour mensuelle alignée sur la version publique | tant que la tenue à jour est souscrite |

**Installation** : Claude Code (`~/.claude/skills/` ou plugin depuis le dépôt privé) ou Projet ChatGPT (prompt complet régénéré par `outils/generer_adaptations.py` à partir de la version client). Le choix dépend de l’outil déjà en place chez le client, jamais l’inverse.

## Où elle se situe dans la grille (lecture du 11.10.2026, aucun chiffre inventé)

La grille `0300_STRATEGIE_COMMERCIALE/03.01_Strategie-Commerciale/03_GRILLE_TARIFAIRE_PALAMBUR.md` (MAJ 2026-09-24) range l’axe 1 en ascenseur : Audit Express, Audit Complet, **Le Collaborateur, augmenté** (quatre formats, support et gabarits, suivi 30 jours), Accélérateur Lean & IA, puis **Accompagnement mensuel** (veille, hotline, point mensuel).

La version entreprise s’y place **entre la formation et l’accompagnement mensuel** :

- une **part unique** (atelier, rédaction, installation), de la nature du Collaborateur augmenté, et qui peut en être une option ;
- une **part récurrente** (tenue à jour mensuelle), de la nature de l’accompagnement mensuel, et qui peut y être incluse.

Elle **ne crée pas un quatrième axe** : c’est une prestation de l’axe 1, et l’argument « référencement actif, remise sur le prochain service » de la grille s’y applique tel quel. Elle ne se vend pas sans que le client ait au moins suivi un format de la formation `[À DÉCIDER par Victor : préalable obligatoire ou simplement recommandé]`.

**Prix : [À DÉCIDER par Victor, grille `0300_STRATEGIE_COMMERCIALE/03.01_Strategie-Commerciale/03_GRILLE_TARIFAIRE_PALAMBUR.md` fait foi]**

Quand le prix est décidé, il s’écrit **dans la grille**, et cette note le cite par renvoi, jamais par recopie (règle § 1 et § 8 de `CLAUDE.md`). Le site ne l’affiche pas : « Prix sur demande. »

## « Méthode Palambur Pro » · le nom de travail de la version entreprise (point 76)

Le plan du 11.10.2026 nomme la version entreprise **« Méthode Palambur Pro »**. C’est un **nom de travail** : le nom commercial se pose dans `offres.ts` du site, qui fait foi pour les noms (`[À DÉCIDER par Victor]`). Ce que le nom recouvre, pour qu’on ne vende pas deux choses différentes sous le même mot :

| | Gratuit (dépôt public) | « Pro » (version entreprise) |
|---|---|---|
| **La méthode, le Gabarit, les règles** | tout, à jour | identiques, jamais une copie divergente |
| **Les gabarits de livrables** | les gabarits génériques de `gabarits/`, qui grandissent à chaque version | les cinq à dix livrables **du client**, pré-remplis de ses constantes (signatures, canton, conventions collectives, ton) |
| **Les fiches métier** | les fiches de `metiers/`, qui résument chaque métier | la fiche du métier du client **au complet**, dérivée du corpus Chaptal, avec ses tâches et ses pièges |
| **Les mises à jour de droit** | dans le dépôt, pour tous, à chaque version | **rejouées sur la version client** : quand une référence change dans le dépôt, la version client est contrôlée et mise à jour, et le client en est averti |
| **L’installation** | par la personne elle-même (`portabilite/INSTALLATION.md`) | par Palambur, chez le client, sur son outil |
| **Les épreuves** | les vingt cas publics | dix cas **du client**, anonymisés, rejoués avant chaque mise à jour |
| **Le prix** | aucun | **`[À DÉCIDER]`**, dans la grille |

Ce qui ne change pas d’une colonne à l’autre : le skill **n’envoie rien à Palambur**, dans les deux versions. « Pro » n’achète pas de la confidentialité en plus, elle est déjà totale ; il achète du **pré-réglage et de la tenue à jour**.

**Rattachement à la grille** : voir la section « Où elle se situe dans la grille » ci-dessus ; « Pro » est une prestation de l’axe 1, pas un axe nouveau. Quand le prix est décidé, il s’écrit dans `03_GRILLE_TARIFAIRE_PALAMBUR.md` et cette note le cite par renvoi.

## Installation accompagnée d’une heure (point 77)

Une prestation **plus petite que la version entreprise**, pour une personne ou une petite équipe qui veut le skill public, bien installé, sur son outil, et une première réussite en séance. Elle ne pré-règle rien : elle installe le dépôt public tel quel.

**Prérequis**, demandés avant de fixer l’heure :

- un outil déjà en place et un compte qui fonctionne (Claude Code, Codex, Cursor, Gemini CLI, Copilot, ou une IA à boîte d’instructions comme Euria ou un Projet Claude.ai) ;
- un ordinateur sur lequel la personne a le droit d’installer (pour les hôtes à fichiers) ;
- **une vraie demande** de la personne, choisie par elle avant la séance (une offre d’emploi à publier, une relance à envoyer), sans donnée nominative, ou avec l’accord de l’anonymiser en séance.

**Déroulé de l’heure** :

| Minutes | Ce qui se passe |
|---|---|
| 0 à 10 | ce qu’est la Méthode, en trois phrases, et la démonstration du `README.md` sur l’écran de la personne |
| 10 à 25 | installation sur **son** outil, en suivant `portabilite/INSTALLATION.md` hôte par hôte ; vérification que le skill est chargé (`/skills` ou équivalent) |
| 25 à 45 | **sa** demande, jouée de bout en bout : les questions, le Gabarit rempli, le livrable ; la personne tient le clavier |
| 45 à 55 | le mode relecture sur un texte qu’elle a déjà écrit ; comment déclencher (les trois portes) ; comment mettre à jour (`git pull` ou nouvelle version du plugin) |
| 55 à 60 | ce qu’elle fait seule demain ; où trouver de l’aide (le dépôt, `CONTRIBUTING.md`) ; ce que la formation ajouterait |

**Ce qui est remis** : rien à part le skill installé et son livrable ; un message après la séance avec les trois commandes utilisées et le lien du dépôt.

**Lien avec la formation** : l’heure est **la plus petite marche** de l’ascenseur de l’axe 1 ; elle précède « Le Collaborateur, augmenté » (qui apprend la Méthode à une équipe) et peut en être déduite si la personne s’y inscrit ensuite `[À DÉCIDER par Victor]`. Elle n’est pas un format de la formation, c’est une installation.

**Prix : [À DÉCIDER par Victor, dans la grille tarifaire]**. Aucun montant ici ni sur le site tant que la grille ne le porte pas.

## Ce qui exige Victor

1. Le **prix** et sa structure (unique, récurrent, ou option de la formation).
2. L’**hébergement** de la version client (dépôt privé ou dossier remis).
3. Le **préalable formation** (obligatoire ou recommandé).
4. Le **nom** de l’offre dans `offres.ts`, qui fait foi pour les noms : cette note dit « version entreprise », le plan dit « Méthode Palambur Pro », le nom commercial reste à poser.
5. Le **prix de l’installation accompagnée**, et si elle se déduit de la formation.

## Ce que cette note ne fait pas

Elle ne chiffre rien, ne fixe aucun délai ferme, et ne présume pas qu’un client existe. Le premier client qui la demande écrira la version définitive de cette note, pas l’inverse (même règle que l’offre d’entrée de la grille : on n’invente pas un produit avant sa demande).
