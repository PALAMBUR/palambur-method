# Version entreprise du skill · note de cadrage (point 29)

**Brouillon · 11.10.2026 · session Skills et Prompt Ingénierie.** Rien n’est vendu, rien n’est construit. Cette note situe l’offre, dit ce qu’elle contient, ce qu’elle exige de Palambur, et comment elle se livre. **Le prix n’est pas écrit ici** : il se décide dans la grille tarifaire, qui fait foi.

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

## Ce qui exige Victor

1. Le **prix** et sa structure (unique, récurrent, ou option de la formation).
2. L’**hébergement** de la version client (dépôt privé ou dossier remis).
3. Le **préalable formation** (obligatoire ou recommandé).
4. Le **nom** de l’offre dans `offres.ts`, qui fait foi pour les noms : cette note dit « version entreprise », le nom commercial reste à poser.

## Ce que cette note ne fait pas

Elle ne chiffre rien, ne fixe aucun délai ferme, et ne présume pas qu’un client existe. Le premier client qui la demande écrira la version définitive de cette note, pas l’inverse (même règle que l’offre d’entrée de la grille : on n’invente pas un produit avant sa demande).
