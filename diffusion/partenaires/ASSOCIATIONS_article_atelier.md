# Associations patronales · article de bulletin et déroulé d’atelier (point 69)

**Brouillon · rien n’est envoyé · go Victor.** Préparé le 11.10.2026. Complète `../RELAIS_ROMANDS.md` (19 organisations vérifiées, message d’approche, ordre proposé), qui **n’est pas réécrit** : ce fichier ajoute ce que ce relais demandait, un **article de 600 mots** pour un bulletin de membres et un **déroulé d’atelier d’une heure**, tous deux adaptables par deux variables : `[Association]` et `[le livrable]`.

Aucune personne nommée. Aucun prix. Le nombre de mots de l’article est mesuré en fin de fichier.

---

## L’article · « Quatre questions avant d’écrire »

*Chapeau* · Vos membres demandent de plus en plus à une IA de rédiger leurs documents. Elle écrit vite, bien, et invente ce qu’on ne lui a pas dit. Une méthode publiée en Suisse romande l’oblige à demander d’abord.

Vos membres rédigent chaque semaine [le livrable]. De plus en plus souvent, ils le demandent à une IA en une phrase et envoient ce qui revient. Le texte est propre, le ton est juste, et quelque chose cloche : un canton qui n’est pas le bon, une convention collective jamais nommée, un délai de paiement sorti de nulle part. Rien de tout cela n’était dans la demande ; tout paraît plausible. Une invention plausible ne se voit pas à la relecture.

**Pourquoi l’IA invente**

Un modèle de langage ne cherche pas la vérité, il prédit le mot suivant. Devant une information manquante, il ne s’arrête pas : il prédit le contenu du trou. Demandez « une offre d’emploi pour un peintre à 80 % » et vous obtenez en dix secondes un canton, un contrat, une date d’entrée et des avantages, aucun vérifié.

**Inverser l’ordre**

Une entreprise de conseil neuchâteloise, Palambur, a publié sous licence MIT une méthode qui inverse l’ordre habituel : l’IA clarifie d’abord, puis produit une seule fois, au lieu de produire d’abord et de corriger dix fois. Concrètement, avant d’écrire, l’assistant anticipe les quatre décisions qu’il aurait sinon prises à votre place et vous les pose, une par message, avec un compteur (« Question 1 sur 4 »), des réponses par lettre et un défaut prudent si vous ne savez pas.

Quatre réponses, trente secondes. Puis deux textes reviennent : le prompt complet, réutilisable, et le document. Ce qui n’a pas été dit n’a pas été inventé : il reste écrit « à compléter », entre crochets, là où un relecteur ne peut pas le manquer.

**La règle qui passe avant les autres**

La plupart des demandes réelles contiennent des données personnelles : le nom d’un client, un montant, une adresse. Avant toute question sur le ton ou le délai, la méthode en pose une seule : elle a repéré un nom et un montant, elle les anonymise par défaut, souhaitez-vous les noms réels ? Le silence vaut anonymisation. Le numéro de facture et les coordonnées bancaires ne sont jamais envoyés au modèle : ils deviennent des cases à remplir à la main, hors de l’outil.

En Suisse, exposer les données d’un client dans une IA publique engage la responsabilité de la direction.

**Trois refus**

La méthode refuse trois choses : inventer une référence légale (les lois sont nommées, CO, LTr, LEg, nLPD, et les numéros d’articles portent toujours « à vérifier »), combler un trou par une valeur plausible, et terminer un document par une liste d’hypothèses à valider, ce réflexe qui ressemble à de la rigueur et qui est la faute qu’elle veut supprimer.

**Ce que cela change pour vous**

La méthode est gratuite, publique et vérifiable ligne à ligne sur GitHub (github.com/PALAMBUR/palambur-method). Elle s’installe dans Claude Code en deux commandes, se charge dans les assistants qui lisent le standard ouvert des skills, et se colle dans ceux qui n’offrent qu’une boîte d’instructions, dont Euria d’Infomaniak, hébergé en Suisse. Elle n’envoie rien à personne : pas de compte, pas de serveur, pas de télémétrie.

[Association] propose à ses membres un atelier d’une heure, « quatre questions avant d’écrire », sur [le livrable]. On vient avec une vraie demande ; on repart avec la méthode installée et un premier document. Sans frais, sans démarche commerciale en séance.

Clarifier avant de produire n’est pas une invention : tout professionnel soigneux le fait. Ce qui est nouveau, c’est de l’avoir écrit pour qu’une machine le fasse aussi, et de l’avoir publié pour que chacun lise ce que l’assistant fait d’une demande avant de lui en confier une.

---

## Adapter l’article à l’association

| Association (vérifiée dans `RELAIS_ROMANDS.md`) | `[le livrable]` proposé | Publication visée |
|---|---|---|
| CNCI | la relance de facture | magazine *Repères* |
| CVCI | l’offre d’emploi | publication aux membres |
| FER Genève, FER Neuchâtel | l’offre d’emploi | lettre aux membres |
| FPV et Centre Patronal | le certificat de travail | relais vers les associations professionnelles membres |
| CCIG, CCIF, CCI Valais, CCIJ | la relance de facture | programme d’événements et lettre |
| FIDUCIAIRE SUISSE, sections romandes | la relance de facture | atelier de section (voir aussi `FIDUCIAIRES_kit.md`) |

Le chapeau, le titre et le dernier paragraphe peuvent être coupés par la rédaction ; le paragraphe « La règle qui passe avant les autres » **ne se coupe pas** : c’est la raison d’être de la méthode.

## Le déroulé d’atelier · une heure, pour les membres

**Titre** · « Quatre questions avant d’écrire » · **Public** · dirigeants, cadres, administratifs des entreprises membres, 8 à 20 personnes · **Prérequis** · un ordinateur portable, un accès à un assistant d’IA (celui qu’on utilise déjà), une demande réelle **anonymisée avant de venir** (consigne envoyée avec l’invitation) · **Animation** · une personne de Palambur, présentée par sa fonction · **Coût pour l’association et ses membres** · aucun · **Démarche commerciale en séance** · aucune ; la seule mention est le dépôt public.

| Minute | Séquence | Ce qu’on montre ou fait |
|---|---|---|
| 0 à 5 | Accueil par [Association]. | une phrase sur pourquoi ce sujet maintenant |
| 5 à 15 | **La panne.** « Fais [le livrable] » collé en direct, sans méthode. Au tableau : tout ce que le modèle a décidé seul. | projecteur, un assistant quelconque |
| 15 à 25 | **La méthode.** Même demande avec le skill : la question d’anonymisation en premier si la demande porte un nom ; puis les quatre questions ; puis les deux blocs. Comparer avec le tableau. | `README.md`, section avant/après |
| 25 à 45 | **Pratique.** Chacun sur sa demande, avec le lien du Projet partagé (sans rien installer) ou le prompt collé dans son outil. Les animateurs passent dans les rangs. | `PROJET_CLAUDE_AI.md`, `adaptations/` |
| 45 à 55 | **Relecture croisée.** Par deux : l’un lit le document de l’autre et cherche ce qui a été inventé ; la grille d’`epreuves/grille.md` sert de liste. | `epreuves/grille.md` imprimée |
| 55 à 60 | **Installation et suite.** Deux commandes pour Claude Code ; le guide hôte par hôte pour les autres ; où poser une question (un ticket sur le dépôt). | `portabilite/INSTALLATION.md` |

**Ce qu’on emporte** : la méthode installée ou le lien ; un premier document ; la grille de relecture ; l’adresse du dépôt. **Ce qu’on ne distribue pas** : un prix, une offre, une carte de visite glissée dans les documents.

**Le texte d’invitation** (pour le bulletin ou le courriel de l’association, 80 mots) :

> **Atelier · Quatre questions avant d’écrire** · [date, lieu, à compléter par l’association]
> Vous demandez à une IA de rédiger [le livrable] ? Elle invente ce que vous ne lui dites pas. En une heure, installez une méthode gratuite et publiée qui l’oblige à demander d’abord, et repartez avec un premier document relu. Apportez un ordinateur et une demande réelle, **sans nom ni montant**. Gratuit pour les membres de [Association], sans démarche commerciale.

## Ce qui exige Victor

- Le **go**, association par association, dans l’ordre de `RELAIS_ROMANDS.md` (Neuchâtel d’abord).
- La **signature de l’article** : le nom de l’entreprise seul, ou une fonction ; jamais ce fichier qui décide.
- Le lien du Projet partagé (`PROJET_CLAUDE_AI.md`) avant le premier atelier.

## Mesure du nombre de mots de l’article

Compter les mots entre les deux traits horizontaux (chapeau compris), depuis la racine du dépôt :

```bash
awk '/^---$/{n++; next} n==1' diffusion/partenaires/ASSOCIATIONS_article_atelier.md | wc -w
```

Relevé du 11.10.2026 : voir le rapport de la session (le chiffre n’est pas recopié ici ; la commande fait foi). Cible : 600 mots, tolérance 550 à 650.

## Marqueurs laissés dans ce fichier

- `[Association]`, `[le livrable]`, `[date, lieu, à compléter par l’association]` · variables d’adaptation, remplies par l’association ou le jour de l’envoi.
