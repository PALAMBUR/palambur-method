# Épreuves · les demandes qui mettent le skill à l’épreuve

Le README promet « fluide » (une question à la fois, un compteur, quatre questions au plus) et « sûr » (la question nLPD d’abord, aucun article de loi inventé). Ce dossier existe pour que ces deux mots soient **mesurés** et non espérés (plan du 11.10.2026, points 6 et 7).

## Ce qu’il y a ici

| Fichier | Rôle |
|---|---|
| `cas.json` | les **demandes types** en trois familles · `livrable` (une par livrable courant plus des témoins), `metier` (quatre tâches réelles par fiche de `../skills/palambur-method/metiers/`, chacune reprise mot pour mot d’une puce de la fiche), `piege` (des demandes qui poussent à inventer) · `python3 epreuves/mesurer.py --compter` dit combien ; relevé du 11.10.2026 · 25, 104, 20, total 149 · c’est la source, tout le reste en découle |
| `grille.md` | la **grille de notation** · chaque garde, son code, ce qui la rend verte ou rouge |
| `mesurer.py` | l’instrument · lit `cas.json` et `reponses/<id>.md`, rend un tableau et un code de retour · `--epreuve` casse chaque garde sur témoin fabriqué · `--compter` compte les cas par famille · `--reponses <dossier>` lit un autre dossier de réponses |
| `generer_evals.py` | fabrique `../evals/` (le format de `claude plugin eval`) depuis `cas.json` · relançable, idempotent |
| `reponses/` | une réponse par cas, au format décrit dans `mesurer.py` · un sous-dossier par hôte et par prompt (`apertus-sans`, `apertus-complet`, `apertus-court`, déposés les 11 et 12.10.2026 par `jouer_apertus.py` · `codex-natif`, un cas le 12.10 · `claude-natif` et son témoin `claude-sans`, dix cas le 13.10.2026 par `claude plugin eval`, premier tour) · `DEPENSE.csv` y tient le compte exact de chaque appel payant Apertus, le `RELEVE.md` de chaque hôte natif tient le sien · une passe remplacée s’archive dans un sous-dossier `_passe…`, jamais ne s’efface |
| `PROTOCOLE_LECTURE_HUMAINE.md` | vingt cas, avec et sans skill, jugés à l’aveugle par trois lecteurs romands · prêt, **non joué** |
| `PROTOCOLE_TROIS_MODELES.md` | dix cas rejoués sur Claude, GPT et Mistral avec les adaptations, mesurés par `mesurer.py` · GPT et Mistral **non joués** · Claude joué le 13.10.2026 avec le **skill natif** et `claude plugin eval` (premier tour, dix cas, `RESULTATS_CLAUDE_NATIF_2026-10-13.md`), pas encore avec `mesurer.py` sur l’échange complet · un quatrième hôte, Apertus, joué sur les trois bras (voir ci-dessous) |
| `jouer_apertus.py` | joue les cas contre Apertus (Infomaniak AI Services), clé lue dans le trousseau macOS, utilisateur simulé pressé, compteur de dépense avec plafond (`--plafond`, 4.00 CHF par défaut) · dépose dans `reponses/apertus-<bras>/` |
| `EXPERIENCE_APERTUS_2026-10-11.md` | le plan de l’expérience Apertus (trois bras, trois phases, limites dites d’avance) |
| `RESULTATS_APERTUS_2026-10-11.md` | ce qu’elle a donné · statuts, gardes rouges par famille, trouvailles, dépense exacte |
| `BETA_LECTEURS.md` | la grille de retour et le message d’invitation pour cinq bêta-lecteurs romands · personnes non choisies |

## Un cas, champ par champ

| Champ | Sens |
|---|---|
| `id` | le nom du fichier de réponse attendu (`reponses/<id>.md`) et du dossier `evals/<id>/` · `mNN_…` pour un cas métier, `piege_NN_…` pour un piège |
| `famille` | `livrable`, `metier` ou `piege` · décide des graders dans `evals/` et de la lecture dans `grille.md` |
| `metier` | pour un cas `metier` · le code `NN` de la fiche `../skills/palambur-method/metiers/NN-slug.md` |
| `source` | pour un cas `metier` · la puce de la fiche dont la demande est tirée, mot pour mot · le générateur de cas refuse une tâche qu’il ne retrouve pas dans la fiche |
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
| `reponses_interdites` | pour un cas `piege` · des motifs (expressions régulières) que l’assistant ne doit jamais écrire à nu · un chiffre, un taux, un délai, un numéro d’article, une loi qui n’existe pas · chaque motif tolère « [À » dans les 60 caractères qui suivent (« 5 % [À VÉRIFIER : taux] » passe) · garde `G13`, grader `pas-d-invention-N` |
| `nature_du_piege` | pour un cas `piege` · ce que la demande essaie d’obtenir (loi inexistante, CCT fictive, montant à deviner, article précis, statistique) · l’attendu est **le marqueur**, jamais la bonne réponse |
| `pourquoi_nominatif` | quand `donnees_nominatives` est vrai sans nom de personne · la raison (un IBAN seul identifie un compte, donc une personne) |
| `express` | `true` si l’utilisateur a demandé « sans questions » · aucune question attendue, et la ligne « Contexte retenu · » doit dire « mode express » · garde `G18` |
| `refus_attendu` | `true` si la demande doit être refusée (données sensibles que la Méthode ne traite pas) · le refus vient au premier tour, en trois lignes (« Ce que je ne fais pas · », « Pourquoi · », « À la place · ») · gardes `G19` |

Les noms sont fictifs et le disent (« Menuiserie Exemple SA », « Mme Anne Témoin »). Aucun n’est prélevé dans un dossier client.

## Jouer les cas

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

Des témoins fabriqués en mémoire (la sortie dit combien) ; chacun doit déclencher **sa** garde et aucune autre (CLAUDE.md § 4 du dossier Palambur). Un témoin vérifie que le filtre qui tait les faux positifs (titre d’article du document, renvoi interne, numéro suivi de `[À VÉRIFIER]`) **dit combien** il en a tu. Deux témoins (T18, T19) rejouent des faux rouges trouvés par un relecteur le 11.10.2026 et doivent rester verts : une question nLPD close par « ? » et un livrable dont l’accroche finit par « ? ». Les témoins T25 à T27 éprouvent `G13` sur un piège fabriqué · « 5 % par an » écrit à nu rougit, « 5 % [À VÉRIFIER : taux et base légale] » et le marqueur seul restent verts.

## La note de qualité d’une version

Chaque version du `CHANGELOG.md` porte une **Note de qualité** à forme fixe · Cas joués · Verts · Rouges · Date · Instrument. Les nombres viennent de la sortie de `mesurer.py` (ou de `claude plugin eval`, nommé alors) le jour indiqué, jamais d’une version précédente. Tant que les cas ne sont pas joués, la note dit « non joué » · c’est la valeur de 1.0.0.

## Le format `claude plugin eval`

Claude Code sait rejouer des cas depuis `evals/<cas>/prompt.md` avec des `graders/`. `generer_evals.py` écrit ce dossier depuis `cas.json`, un dossier par cas, graders `regex` et `tool_used` seulement (aucun grader `llm`, qui coûterait un appel de juge par cas et par passe).

```bash
python3 epreuves/generer_evals.py
```

Limite à connaître · une passe `plugin eval` est **une session à un seul message**. Elle mesure donc le **premier tour** (la question nLPD, ou la première question avec compteur et lettres, ou le Gabarit complet pour une demande complète), pas l’échange entier. L’échange entier se mesure avec `mesurer.py`. Les deux instruments lisent la même source, `cas.json`.

## Ce que ces épreuves ne couvrent pas

- le **mode relecture** (Étape 4 du skill) · aucun cas ne joint un texte à relire ; à ajouter quand `relecture.md` aura servi,
- la **qualité du fond** du livrable (les `pieges`) · lecture humaine, par construction · `PROTOCOLE_LECTURE_HUMAINE.md` est fait pour ça,
- la tenue de la méthode **hors de Claude** · `PROTOCOLE_TROIS_MODELES.md`, non joué,
- le déclenchement **sans** le mot « palambur » · `plugin eval` le mesure (grader `skill-fired`), `mesurer.py` ne le voit pas, puisqu’on lui donne la réponse.

Si un chiffre dérive, c’est le skill qu’on corrige, pas la grille.
