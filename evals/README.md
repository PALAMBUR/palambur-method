# Évaluations `claude plugin eval`

Tout ce qui est sous `evals/<cas>/` est **généré** par `epreuves/generer_evals.py` depuis `epreuves/cas.json`. On n’édite pas ces fichiers à la main · on corrige `cas.json` et on relance.

```bash
python3 epreuves/generer_evals.py
```

## Lancer

Depuis la racine du plugin ·

```bash
claude plugin eval .
```

Un seul cas, une seule passe, sans comparaison au témoin sans plugin ·

```bash
claude plugin eval . --case offre_emploi --runs 1 --ablation none
```

Par famille · `--tag nlpd`, `--tag clarification`, `--tag complet`, `--tag declencheur-naturel`.

Les résultats s’écrivent dans `evals/results/<horodatage>/` (rapport HTML et JSON) · le dossier est ignoré par `evals/.gitignore`.

## Ce que chaque cas vérifie

Une passe est **une session à un seul message** · elle juge le **premier tour** du modèle, pas l’échange entier.

| Famille (`tags`) | Premier tour attendu | Graders |
|---|---|---|
| `nlpd` (7 cas) | la question binaire d’anonymisation, seule | `question-nlpd` (poids 2), `une-seule-question`, `pas-de-compteur`, `pas-de-livrable` |
| `clarification` (12 cas) | « Question 1 sur T », une question, choix A à D, échappatoire | `compteur` (poids 2), `une-seule-question`, `lettres`, `echappatoire`, `pas-de-livrable` |
| `complet` (2 cas) | le Gabarit puis le livrable, sans question | `gabarit` (poids 2), `aucune-question`, `article-non-verifie`, `marqueur-…` |
| tous | | `skill-fired` (le skill a été invoqué), `pas-de-pme` |

La famille se décide dans cet ordre : nominatif d’abord, puis clarification, puis complet. `convocation` est une demande complète **et** nominative : son premier tour attendu est la question nLPD, elle est donc rangée dans `nlpd`, ce qui laisse deux cas dans `complet`. Le 21e cas, `montant_sans_nom`, est une clarification sans question nLPD attendue (un montant seul n’est pas une donnée nominative).

Le tag `declencheur-naturel` marque les cas **sans** le mot « palambur » dans la demande · c’est sur eux que `skill-fired` dit si la `description` du skill suffit à le déclencher.

Aucun grader `llm` · tout est `regex` ou `tool_used`, donc gratuit. L’échange complet (lots, livrable final, marqueurs) se mesure avec `epreuves/mesurer.py` sur des réponses déposées à la main.
