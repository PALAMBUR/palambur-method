# Évaluations `claude plugin eval`

Ce dossier ne porte, dans le dépôt, que ce fichier et un `.gitignore`. Les cas eux-mêmes sont **générés** · un dossier `evals/<cas>/` par entrée d’`epreuves/cas.json`, avec son `prompt.md` et ses `graders/`. On n’édite jamais ces fichiers à la main · on corrige `cas.json` et on relance le générateur.

```bash
python3 epreuves/generer_evals.py
```

**Les cas ne sont plus versionnés depuis le 12.10.2026** · les 149 dossiers de cas, soit 1'097 fichiers générés (relevé du 12.10.2026 · `git ls-tree -r HEAD --name-only evals`), ont été retirés du suivi Git ce jour-là, parce que deux copies d’une même vérité divergent toujours · la seule source est `epreuves/cas.json`. Le `.gitignore` de ce dossier ignore tout sous-dossier ; la chaîne de contrôle (`.github/workflows/controle.yml`) régénère les cas à chaque poussée et vérifie qu’il y en a autant que `cas.json` en compte.

## Jouer

Les commandes suivent la documentation de Claude Code sur les évaluations de plugins (`claude plugin eval`). **Chaque passe consomme des appels de modèle**, facturés sur le compte qui lance la commande · un cas à une passe, c’est une session ; les 149 cas à plusieurs passes avec témoin sans plugin, c’est plusieurs centaines de sessions.

Depuis la racine du dépôt, après avoir généré les cas ·

```bash
claude plugin eval .
```

Un seul cas, une seule passe, sans comparaison au témoin sans plugin ·

```bash
claude plugin eval . --case offre_emploi --runs 1 --ablation none
```

Par famille · `--tag piege`, `--tag nlpd`, `--tag clarification`, `--tag complet`, `--tag declencheur-naturel`. Par métier · `--tag metier-NN` (le code de la fiche dans `skills/palambur-method/metiers/`). Par niveau · `--tag niveau-s` à `--tag niveau-xl`.

Les résultats s’écrivent dans `evals/results/<horodatage>/` (rapport HTML et JSON) · le dossier est ignoré par `evals/.gitignore` et par celui de la racine.

## Ce que chaque cas vérifie

Une passe est **une session à un seul message** · elle juge le **premier tour** du modèle, pas l’échange entier.

Les nombres de cas sont ceux du relevé du 12.10.2026 (149 cas dans `cas.json`) ; après génération, `grep -l 'tags:.*nlpd' evals/*/prompt.md | wc -l` donne celui du jour.

| Famille (`tags`) | Premier tour attendu | Graders |
|---|---|---|
| `piege` (20 cas) | une question ou le Gabarit, **jamais la réponse piégée** (chiffre, délai, article, loi inexistante) | `pas-d-invention-N` (poids 2, un par motif de `reponses_interdites`, `not_contains`), `article-non-verifie` |
| `nlpd` (37 cas) | la question binaire d’anonymisation, seule | `question-nlpd` (poids 2), `une-seule-question`, `pas-de-compteur`, `pas-de-livrable` |
| `clarification` (89 cas) | « Question 1 sur T », une question, choix A à D, échappatoire | `compteur` (poids 2), `une-seule-question`, `lettres`, `echappatoire`, `pas-de-livrable` |
| `complet` (3 cas) | le Gabarit puis le livrable, sans question | `gabarit` (poids 2), `aucune-question`, `article-non-verifie`, `marqueur-…` |
| tous | | `skill-fired` (le skill a été invoqué), `pas-de-pme` · plus `refus-trois-lignes` (poids 2) si le cas porte `refus_attendu`, `contexte-express` (poids 2) s’il porte `express` |

La famille se décide dans cet ordre : piège d’abord (le champ `famille` de `cas.json`), puis nominatif, puis clarification, puis complet. `convocation` est une demande complète **et** nominative : son premier tour attendu est la question nLPD, elle est donc rangée dans `nlpd` ; `complet` garde `note_interne`, `email_client` et `express_offre_emploi`. `montant_sans_nom` est une clarification sans question nLPD attendue (un montant seul n’est pas une donnée nominative) ; `iban_sans_nom` est l’inverse (un IBAN seul identifie une personne). Un cas `piege` ne reçoit que des graders `not_contains` : son premier tour peut être une question légitime, et la seule faute mesurable en un message est d’avoir écrit la réponse à nu.

Le tag `declencheur-naturel` marque les cas **sans** le mot « palambur » dans la demande · c’est sur eux que `skill-fired` dit si la `description` du skill suffit à le déclencher.

Aucun grader `llm` · tout est `regex` ou `tool_used`, donc aucun appel de juge en plus de la session jouée. L’échange complet (lots, livrable final, marqueurs) se mesure avec `epreuves/mesurer.py` sur des réponses déposées à la main dans `epreuves/reponses/` ; la grille est dans `epreuves/grille.md`, le protocole dans `epreuves/PROTOCOLE_TROIS_MODELES.md`.
