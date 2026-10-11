# Épreuves · vingt-et-une demandes qui mettent le skill à l’épreuve

Le README promet « fluide » (une question à la fois, un compteur, quatre questions au plus) et « sûr » (la question nLPD d’abord, aucun article de loi inventé). Ce dossier existe pour que ces deux mots soient **mesurés** et non espérés (plan du 11.10.2026, points 6 et 7).

## Ce qu’il y a ici

| Fichier | Rôle |
|---|---|
| `cas.json` | les **vingt-et-une demandes types**, une par livrable courant plus un témoin « montant sans nom » · c’est la source, tout le reste en découle |
| `grille.md` | la **grille de notation** · chaque garde, son code, ce qui la rend verte ou rouge |
| `mesurer.py` | l’instrument · lit `cas.json` et `reponses/<id>.md`, rend un tableau et un code de retour · `--epreuve` casse chaque garde sur témoin fabriqué |
| `generer_evals.py` | fabrique `../evals/` (le format de `claude plugin eval`) depuis `cas.json` · relançable, idempotent |
| `reponses/` | **à déposer** · une réponse par cas, au format décrit dans `mesurer.py` · absent du dépôt tant que personne n’a joué les cas |

## Un cas, champ par champ

| Champ | Sens |
|---|---|
| `id` | le nom du fichier de réponse attendu (`reponses/<id>.md`) et du dossier `evals/<id>/` |
| `livrable` | ce que l’utilisateur veut obtenir |
| `niveau` | S, M, L ou XL · recopié de `../skills/palambur-method/gabarits/README.md`, qui fait foi pour le niveau d’un livrable · S = 0 à 1 question, jamais de lot |
| `demande` | la phrase telle qu’un utilisateur la taperait · apostrophes droites comprises, c’est son texte, pas le nôtre |
| `declencheur_explicite` | `true` si la demande contient le mot « palambur » · la moitié des cas n’en porte pas, pour éprouver le déclenchement sur la nature de la demande |
| `donnees_nominatives` | la demande porte des noms de personnes ou d’entreprises, et les montants ou contrats qui leur sont rattachés · un montant seul n’en est pas une (cas `montant_sans_nom`) |
| `question_nlpd_attendue` | égal à `donnees_nominatives` · la question binaire d’anonymisation doit venir en premier, seule, sans compteur |
| `nb_questions_attendu` | taille du **premier lot** de clarification, question nLPD exclue · `0` pour une demande complète (trois cas : `note_interne`, `email_client`, `convocation` ; le dernier est aussi nominatif, donc il attend la question nLPD et rien d’autre) · pour la relance, le lot du gabarit `relance-facture.md` fait foi (4) |
| `lots_max` | nombre de lots que le skill peut enchaîner avant de produire · `0` pour une demande complète |
| `marqueurs_attendus` | ce qui doit apparaître dans le livrable (`[À COMPLÉTER]`, `[À VÉRIFIER]`) |
| `pieges` | ce qu’un modèle livré à lui-même écrit souvent et que le skill doit **ne pas** écrire · lecture à l’œil, pas mesurée par le script |

Les noms sont fictifs et le disent (« Menuiserie Exemple SA », « Mme Anne Témoin »). Aucun n’est prélevé dans un dossier client.

## Jouer les vingt-et-un cas

1. Ouvrir une session avec le skill chargé, coller la `demande` d’un cas, répondre aux questions comme un utilisateur pressé (choisir une lettre), aller jusqu’au livrable.
2. Recopier l’échange dans `reponses/<id>.md` au format `## Assistant · tour N` / `## Utilisateur · tour N` (l’en-tête de `mesurer.py` le décrit).
3. Lancer la mesure.

```bash
python3 epreuves/mesurer.py
```

Le tableau donne, par cas · le statut (VERT, ROUGE, INCOMPLET), le nombre de questions mesuré contre attendu, l’état de la question nLPD, et **chaque garde rouge avec sa raison**. Code de retour · 0 tout vert, 1 au moins un rouge, 3 rien à mesurer.

Avant de croire un vert, faire rougir l’instrument ·

```bash
python3 epreuves/mesurer.py --epreuve
```

Dix-neuf témoins fabriqués en mémoire ; chacun doit déclencher **sa** garde et aucune autre (CLAUDE.md § 4 du dossier Palambur). Un témoin vérifie que le filtre qui tait les faux positifs (titre d’article du document, renvoi interne, numéro suivi de `[À VÉRIFIER]`) **dit combien** il en a tu. Deux témoins (T18, T19) rejouent des faux rouges trouvés par un relecteur le 11.10.2026 et doivent rester verts : une question nLPD close par « ? » et un livrable dont l’accroche finit par « ? ».

## Le format `claude plugin eval`

Claude Code sait rejouer des cas depuis `evals/<cas>/prompt.md` avec des `graders/`. `generer_evals.py` écrit ce dossier depuis `cas.json`, un dossier par cas, graders `regex` et `tool_used` seulement (aucun grader `llm`, qui coûterait un appel de juge par cas et par passe).

```bash
python3 epreuves/generer_evals.py
```

Limite à connaître · une passe `plugin eval` est **une session à un seul message**. Elle mesure donc le **premier tour** (la question nLPD, ou la première question avec compteur et lettres, ou le Gabarit complet pour une demande complète), pas l’échange entier. L’échange entier se mesure avec `mesurer.py`. Les deux instruments lisent la même source, `cas.json`.

## Ce que ces épreuves ne couvrent pas

- le **mode relecture** (Étape 4 du skill) · aucun des vingt-et-un cas ne joint un texte à relire ; à ajouter quand `relecture.md` aura servi,
- la **qualité du fond** du livrable (les `pieges`) · lecture humaine, par construction,
- le déclenchement **sans** le mot « palambur » · `plugin eval` le mesure (grader `skill-fired`), `mesurer.py` ne le voit pas, puisqu’on lui donne la réponse.

Si un chiffre dérive, c’est le skill qu’on corrige, pas la grille.
