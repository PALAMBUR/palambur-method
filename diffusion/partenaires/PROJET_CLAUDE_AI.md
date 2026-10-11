# Projet Claude.ai partageable · instructions et notice (point 65)

**Brouillon · rien n’est envoyé · go Victor.** Préparé le 11.10.2026 par la session Skills et Prompt Ingénierie. Aucun projet n’a été créé sur claude.ai, rien n’a été partagé. Ce fichier dit **quoi coller, où, et ce qu’il faut vérifier** ; la création et le partage sont des gestes de Victor, sur son compte.

## Pourquoi un Projet, alors qu’il existe un skill

Le skill natif (`skills/palambur-method/`, téléversé en ZIP selon `portabilite/INSTALLATION.md` § 1c) est la **voie préférée** sur claude.ai : il se charge à la demande et porte ses fichiers de référence. Un **Projet** sert à autre chose : il se **partage par un lien** à des personnes qui ne veulent rien installer (un client, un participant d’atelier, un lecteur d’article). Elles ouvrent le projet, posent leur demande, la méthode s’applique. C’est la porte la plus courte pour quelqu’un qui n’a jamais entendu le mot « skill ».

## Ce qui va dans le Projet

| Champ du Projet | Quoi | Source dans le dépôt |
|---|---|---|
| **Nom** | `Méthode Palambur · quatre questions avant d’écrire` | ce fichier |
| **Description** (une phrase) | voir ci-dessous | ce fichier |
| **Instructions** | le bloc **sous le trait** de `adaptations/methode-palambur-prompt.md` (version complète, 7'839 caractères au 11.10.2026, taille écrite en tête du fichier généré) | généré par `outils/generer_adaptations.py`, **jamais recopié ici** |
| **Connaissances** (fichiers joints) | `skills/palambur-method/methode-palambur.md`, `protection-donnees.md`, `references-juridiques.md`, `relecture.md`, et le dossier `gabarits/` (un fichier par livrable) | le skill lui-même |

**Pourquoi on ne recopie pas les instructions ici** : le prompt est généré depuis le skill et porte une empreinte de ses sources ; une copie dans ce fichier vieillirait sans le dire (c’est la dérive constatée entre le 12.07 et le 24.09.2026, voir `CHANGELOG.md`). Le jour de la création, Victor ouvre le fichier généré et copie le bloc sous le trait.

### Description à coller

> Vous demandez un document d’entreprise (offre d’emploi, devis, relance, contrat, note interne). Avant d’écrire, l’assistant pose au plus quatre questions, une par message, anonymise les noms et les montants par défaut, et n’invente ni chiffre ni article de loi. Méthode publiée sous licence MIT par Palambur, Neuchâtel · github.com/PALAMBUR/palambur-method

### Première ligne à ajouter en tête des instructions (propre au Projet)

Le prompt généré ne sait pas qu’il tourne dans un projet partagé. Victor ajoute **une ligne au-dessus** du bloc collé :

> Tu tournes dans un Projet Claude.ai partagé publiquement. Les personnes qui t’écrivent ne connaissent ni le skill ni le dépôt : ne mentionne jamais « SKILL.md », « adaptations » ou « empreinte ». Si on te demande qui a écrit la méthode, réponds « Palambur, Neuchâtel, licence MIT, github.com/PALAMBUR/palambur-method », rien de plus.

## La notice (texte pour la page d’accueil du projet ou le message qui accompagne le lien)

> **Méthode Palambur · quatre questions avant d’écrire**
>
> Ce projet applique une méthode publiée et gratuite. Écrivez votre demande comme vous la diriez à un collègue (« fais une relance pour une facture impayée »). L’assistant vous pose au plus quatre questions, une à la fois, avec des réponses par lettre et un défaut prudent si vous ne savez pas. Puis il rend deux textes : le prompt complet, que vous pouvez garder, et le document.
>
> **Vos données.** Si votre demande contient un nom de client, un montant ou une adresse, l’assistant propose d’abord de les anonymiser ; c’est le réglage par défaut. Ne collez pas de numéro de facture, d’IBAN ou de numéro AVS : ils deviennent des cases `[À COMPLÉTER]` que vous remplissez vous-même, hors de l’outil. Ce que vous écrivez ici est traité par Anthropic selon ses conditions, pas par Palambur : Palambur ne reçoit rien, ne voit rien, ne compte rien.
>
> **Ce que l’assistant refuse.** Inventer une valeur plausible, citer un numéro d’article de loi sans « à vérifier », finir un document par une liste d’hypothèses à valider.
>
> La méthode complète, ses fichiers et sa chaîne de contrôle sont publics : github.com/PALAMBUR/palambur-method. Pour l’installer dans votre propre outil (Claude Code, Codex, Cursor, Copilot, Gemini, Mistral, Euria), le guide est dans le dépôt, dossier `portabilite/`.

## Le geste de Victor, dans l’ordre

1. Sur claude.ai, créer un projet avec le nom et la description ci-dessus.
2. Ouvrir `adaptations/methode-palambur-prompt.md` **du dépôt à jour** (après `python3 outils/controle.py` CONFORME), copier le bloc sous le trait dans **Instructions**, et poser la ligne propre au Projet au-dessus.
3. Joindre les fichiers de connaissance listés plus haut.
4. Essayer **trois demandes** avant de partager : la relance avec nom et montant (la question d’anonymisation doit venir **en premier**), l’offre d’emploi du peintre (compteur « Question 1 sur 4 », lettres A à D), un texte joint à relire (aucune question, tableau Constat · Risque · Correction).
5. Régler le partage. **Qui peut voir le projet et selon quel forfait** n’a pas été lu sur une page officielle le 11.10.2026 : `[À VÉRIFIER sur claude.ai, dans les réglages de partage du projet, le jour de la création]`.
6. Noter le lien dans `diffusion/` et le donner aux relais (`RELAIS_ROMANDS.md`), aux fiduciaires (`FIDUCIAIRES_kit.md`) et aux écoles (`ECOLES_kit.md`) : c’est le lien « sans rien installer » de tous ces kits.

## Ce qu’il faut savoir avant de partager

- **Pas de télémétrie Palambur, mais pas de souveraineté non plus.** Les conversations d’un Projet Claude.ai sont traitées par Anthropic ; la promesse « rien ne quitte votre machine » du README vaut pour le skill lu par une IA locale ou par l’IA que l’utilisateur a choisie, pas pour ce projet. La notice le dit en clair. Pour une entreprise qui exige l’hébergement suisse, la voie est Euria d’Infomaniak (`INFOMANIAK_demande.md`, `portabilite/INSTALLATION.md` § 9).
- **Le projet vieillit.** À chaque version du skill, les instructions se recollent depuis le fichier régénéré ; la veille mensuelle (`portabilite/VEILLE_PLATEFORMES.md`) porte la ligne « Projet Claude.ai : instructions à jour ? ».
- **Aucun prix, aucune offre** dans le projet. La seule mention commerciale autorisée est celle du README (« le skill est la porte, Chaptal la maison »), et elle ne figure pas dans les instructions.

## Marqueurs laissés dans ce fichier

- `[À VÉRIFIER sur claude.ai, dans les réglages de partage du projet, le jour de la création]` · portée du partage (lien public, organisation, forfait requis).
- `[À DÉCIDER]` (hors texte) · Victor choisit si le projet est public ou réservé aux participants d’ateliers.
