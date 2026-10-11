# Protocole · dix cas rejoués sur trois modèles

Plan du 11.10.2026, point 52. Le skill est écrit pour Claude et porté vers les autres IA par les deux prompts d’`adaptations/`. Rien ne dit aujourd’hui que la promesse (« fluide », « sûr ») tient hors de Claude. Ce protocole le mesure avec **la même grille**, `grille.md`, et **le même instrument**, `mesurer.py`. **Claude, GPT et Mistral n’ont pas été joués** · toute passe est une dépense de modèle, et le budget n’est pas posé pour ces trois hôtes. Un quatrième hôte, **Apertus** (Infomaniak), a été joué les 11 et 12.10.2026 avec un budget de 5 CHF posé par le fondateur · plan dans `EXPERIENCE_APERTUS_2026-10-11.md`, résultats dans `RESULTATS_APERTUS_2026-10-11.md`.

## 1 · Les trois hôtes

| Hôte | Comment le skill y entre | Fichier source |
|---|---|---|
| Claude (Claude Code ou claude.ai) | le skill natif, `skills/palambur-method/` installé comme plugin ou skill | `SKILL.md` et ses fichiers de référence |
| GPT (GPT personnalisé ou Instructions) | le prompt complet collé dans les instructions | `adaptations/methode-palambur-prompt.md` |
| Mistral (Agent) | le même prompt complet | `adaptations/methode-palambur-prompt.md` |

Les prompts d’adaptation sont **générés** depuis le skill (`outils/generer_adaptations.py`) et portent l’empreinte de leurs sources en tête · on note cette empreinte dans le relevé, c’est elle qui dit quelle version du skill a été jouée. Le modèle exact (nom et date de version affichés par l’hôte) est noté aussi · « GPT » ou « Mistral » sans version ne veut rien dire six mois plus tard.

## 2 · Les dix cas

Cinq livrables courants, trois cas métier, deux pièges · tirés de `cas.json`.

| N° | `id` | Ce que le cas éprouve |
|---|---|---|
| 1 | `offre_emploi` | la clarification à quatre questions, compteur et lettres |
| 2 | `relance_facture` | la question nLPD d’abord, seule, puis le lot du gabarit |
| 3 | `certificat_travail` | XL nominatif, validation humaine |
| 4 | `note_interne` | demande complète · zéro question |
| 5 | `refus_candidat` | niveau S, une question au plus |
| 6 | `m06_annonce_immobiliere` | prix et surface non inventés, pas de superlatif |
| 7 | `m16_relance_documents` | niveau S nominatif, ton |
| 8 | `m22_reponse_contestation` | nominatif, montant, pas de qualification juridique |
| 9 | `piege_02_loi_inexistante_lftc` | une loi qui n’existe pas |
| 10 | `piege_07_vacances_minimales` | un minimum légal à deviner |

## 3 · La passe

Pour chaque hôte, chaque cas, **une fois** (une seule passe par cas et par hôte · le but est de voir si la méthode passe, pas de mesurer une variance) ·

1. Nouvelle conversation. Coller la `demande` du cas, mot pour mot.
2. Répondre aux questions comme un utilisateur pressé · la lettre du défaut quand il y en a un, sinon A ; « conserver » n’est jamais répondu à la question nLPD.
3. Aller jusqu’au livrable. S’arrêter au dixième message de l’assistant si le livrable n’est pas venu (statut INCOMPLET).
4. Recopier l’échange dans `reponses/<hote>/<id>.md` au format décrit en tête de `mesurer.py` (`## Demande`, `## Assistant · tour N`, `## Utilisateur · tour N`).

Puis, par hôte ·

```bash
python3 epreuves/mesurer.py --reponses epreuves/reponses/claude
```

```bash
python3 epreuves/mesurer.py --reponses epreuves/reponses/gpt
```

```bash
python3 epreuves/mesurer.py --reponses epreuves/reponses/mistral
```

Le dossier `reponses/` n’est pas versionné tant que personne n’a joué ; s’il le devient, les trois sous-dossiers portent chacun un fichier `RELEVE.md` avec l’hôte, le modèle, la date, l’empreinte des adaptations et la personne (fonction) qui a joué.

## 4 · Ce qu’on lit

Trois tableaux de dix lignes, un par hôte, et une synthèse ·

| Hôte | Cas joués | Verts | Rouges | Incomplets | Gardes rouges les plus fréquentes |
|---|---|---|---|---|---|
| Claude | | | | | |
| GPT | | | | | |
| Mistral | | | | | |

Lecture ·

- une garde qui rougit **sur les trois hôtes** est un défaut du skill ou de la grille ;
- une garde qui rougit **sur GPT et Mistral seulement** est un défaut du prompt d’adaptation (ou une limite de l’hôte, à nommer) ;
- la ligne « Incomplets » dit si l’hôte tient dix messages de clarification sans décrocher.

Le résultat va dans la **note de qualité** du `CHANGELOG.md` de la version jouée (forme fixe · cas joués, verts, rouges, date, hôte), et dans `epreuves/resultats/TROIS_MODELES_AAAA-MM-JJ.md`.

## 5 · Le budget

Trente conversations de dix messages au plus. Le coût dépend des tarifs des trois hôtes à la date de la passe et de la longueur des échanges · **il n’est pas chiffré ici** (aucun chiffre sans date ni source). Avant de jouer ·

- `[À DÉCIDER]` · le plafond en francs pour la passe, posé par Victor Semblanet ;
- `[À DÉCIDER]` · les comptes utilisés (un compte d’essai par hôte, jamais un compte client) ;
- `[À COMPLÉTER]` · le relevé de la dépense réelle, après la passe, dans `RELEVE.md`.

Sans go, ce protocole reste ce qu’il est · un protocole.
