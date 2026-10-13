# Relevé · Claude · skill natif

- Hôte · Claude Code CLI 2.1.296, lancé par `npx -y @anthropic-ai/claude-code` (aucun binaire `claude` sur le poste), compte Max du fondateur connecté le 13.10.2026 par `auth login`
- Modèle · `claude-opus-5-5`, celui que `claude plugin eval` choisit par défaut, lu dans le champ `model` de chaque trace
- Skill · le dépôt lui-même, résolu comme plugin depuis `.` (`.claude-plugin/plugin.json`, version 1.6.0) · l’ablation `with-without` rejoue chaque cas une seconde fois **sans** le plugin, même modèle, même demande · ce second bras est déposé dans `../claude-sans/`
- Instrument · `claude plugin eval . --case <id> --no-publish --trust-plugin --keep-temp --max-cost-usd 1 --json … --output-dir …` · graders `regex` et `tool_used` générés par `epreuves/generer_evals.py` depuis `cas.json`, **premier tour seulement** (`last_message`) · `runs: 1` posé à la main dans le frontmatter des dix `evals/<id>/prompt.md`, le générateur ne l’écrit pas encore (sans lui, trois passes par cas et par bras)
- Joué le 13.10.2026 entre 13 h 09 et 13 h 23 UTC · **un seul tour**, l’utilisateur ne répond pas · le jeu s’arrête au premier message de l’assistant et les graders ne lisent que lui
- Dépense · coût **estimé par l’outil, en USD**, sous abonnement Max (aucune facture en CHF, aucun appel Apertus) · 10 cas × 2 bras · **2.998 USD**, détail ci-dessous · plus **1.013 USD** d’une première passe d’`offre_emploi` à trois exécutions par bras, arrêtée au plafond de 1 USD, traces non conservées, verdicts identiques (3 verts avec le skill, 2 rouges sans) · remplacée par la passe à une exécution déposée ici · cumul de la journée **4.011 USD**
- Ce que Claude a lu avec le skill · l’outil `Skill` (déclenchement), puis `SKILL.md`, `methode-palambur.md`, `protection-donnees.md`, le gabarit du livrable et les fiches métier selon le cas · 5 à 9 tours d’outils avant le premier message · sans le skill · aucun fichier dans six cas ; dans quatre cas une recherche `Grep` ou `Glob` de « palambur » dans un dossier de travail vide, puis un livrable
- Résultat du premier tour · **8 cas verts sur 10 avec le skill, 0 sur 10 sans** · les deux rouges avec le skill (`relance_facture`, `piege_02_loi_inexistante_lftc`) sont lus à la main et expliqués dans `epreuves/RESULTATS_CLAUDE_NATIF_2026-10-13.md` · ce sont des défauts de l’instrument, pas de la Méthode
- Retrait déclaré · dans `../claude-sans/`, trois transcriptions (`refus_candidat`, `m06_annonce_immobiliere`, `m22_reponse_contestation`) portaient l’**adresse e-mail du compte** qui a lancé l’épreuve, écrite par le modèle comme coordonnée de l’expéditeur · elle est remplacée par `[ADRESSE E-MAIL DU COMPTE RETIRÉE]`, une fois dans chaque fichier · rien d’autre n’est touché dans les vingt transcriptions, fautes de typographie et mots interdits compris

## Dépense par cas

Lue dans les fichiers `--json` de chaque passe (`costUsd`), un cas par ligne · les tours comptent les messages de l’assistant, appels d’outils compris.

| Cas | Début (UTC) | Tours avec | Tours sans | USD avec | USD sans | USD total |
|---|---|---|---|---|---|---|
| `offre_emploi` | 2026-10-13 13:21 | 9 | 3 | 0.286 | 0.077 | 0.363 |
| `relance_facture` | 2026-10-13 13:12 | 5 | 1 | 0.159 | 0.062 | 0.220 |
| `certificat_travail` | 2026-10-13 13:13 | 5 | 1 | 0.160 | 0.069 | 0.229 |
| `note_interne` | 2026-10-13 13:13 | 8 | 2 | 0.301 | 0.060 | 0.361 |
| `refus_candidat` | 2026-10-13 13:14 | 5 | 1 | 0.165 | 0.055 | 0.220 |
| `m06_annonce_immobiliere` | 2026-10-13 13:15 | 9 | 1 | 0.307 | 0.060 | 0.367 |
| `m16_relance_documents` | 2026-10-13 13:15 | 5 | 2 | 0.160 | 0.068 | 0.228 |
| `m22_reponse_contestation` | 2026-10-13 13:16 | 5 | 3 | 0.166 | 0.071 | 0.237 |
| `piege_02_loi_inexistante_lftc` | 2026-10-13 13:16 | 7 | 1 | 0.289 | 0.066 | 0.355 |
| `piege_07_vacances_minimales` | 2026-10-13 13:17 | 7 | 1 | 0.360 | 0.058 | 0.417 |
| **Total** | | | | **2.353** | **0.646** | **2.998** |
