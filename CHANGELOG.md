# Journal des versions

Ce fichier suit le format [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), adapté à la typographie Palambur (le séparateur est « · », jamais un tiret). Les versions suivent [Semantic Versioning](https://semver.org/lang/fr/).

Une version = une étiquette Git `vX.Y.Z`, une release GitHub et le même numéro dans `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` et ce journal. La chaîne de contrôle `outils/controle.py` **refuse** si les trois numéros divergent.

## [1.0.0] · 2026-10-11

Première version numérotée. Le skill existait depuis le 12 juillet 2026 sans numéro, sans licence affichée et en trois copies qui dérivaient (dépôt, skill installé localement, adaptations pour les autres IA). Cette version pose les **fondations** décrites dans le plan en 30 points du 11 octobre 2026.

État au 11.10.2026 : préparé en local. La publication (étiquette, release) attend le go de Victor Semblanet.

### Ajouté

- `LICENSE` · le texte complet de la licence MIT, titulaire « Palambur · Victor Semblanet ». Le README l’annonçait depuis le début, GitHub ne l’affichait pas.
- `CHANGELOG.md` · ce journal.
- `README.md` en **deux langues**, français puis anglais, ouvert par un exemple avant/après (la demande brute, les quatre questions, le livrable).
- `outils/generer_adaptations.py` · fabrique les deux prompts d’adaptation (complet et court) depuis `SKILL.md`, ses fichiers de référence et la table des hôtes d’`adaptations/README.md`, avec une empreinte des sources en tête de chaque fichier. Supprime la dérive constatée entre le skill (24.09) et les adaptations (12.07), et la double liste des hôtes (le chapeau citait encore des produits retirés).
- `outils/regle_typo.py` · la règle typographique maison (zéro tiret de ponctuation, apostrophe courbe, montants suisses exempts), copie datée d’une règle qui fait foi dans l’atelier Palambur, avec l’empreinte sha256 de sa source. Permet à `controle.py` de tourner sur un clone sans l’atelier.
- `outils/controle.py` · la chaîne de contrôle du dépôt : règle embarquée à jour sur sa source (quand l’atelier est à côté), typographie maison, zéro « PME », JSON valides, numéro de version unique, adaptations à jour, frontmatter et taille de `SKILL.md`, liens relatifs. Code de retour 0 ou 1, mode `--epreuve` qui casse chaque garde sur témoin fabriqué, option `--racine` pour contrôler une copie.
- `outils/installer_local.sh` · pose le skill du dépôt dans `~/.claude/skills/` (à blanc par défaut, `--ecrire` pour écrire). Le dépôt devient la **seule source** ; la copie locale n’est plus éditée à la main. Refuse si la cible est un lien symbolique (c’est le cas sur la machine de Palambur au 11.10.2026 : le lien vise un clone périmé) et nomme les deux voies de sortie.
- `epreuves/` · vingt cas (`cas.json`), la grille de notation (`grille.md`) et `mesurer.py` qui note une réponse contre la grille. **Les 20 cas n’ont pas encore été joués : dépense modèle non autorisée.**
- `evals/` · les mêmes vingt cas au format `claude plugin eval` (un dossier par cas, graders générés par `epreuves/generer_evals.py`). **Pas encore joués, pour la même raison** ; `evals/results/` est ignoré par git.
- Les commandes `gh` et `git` prêtes à copier pour retirer le sujet `pme`, corriger la description du profil, commiter, pousser et créer la release sont dans une feuille de l’atelier Palambur, **hors du dépôt** (`COMMANDES_GITHUB_SKILL_A_VALIDER_2026-10-11.md`) : elle porte des chemins de machine et des décisions qui ne regardent pas un clone public. À exécuter par Victor Semblanet.
- En préparation (autres sessions, même version) : `CONTRIBUTING.md`, `portabilite/` (installation sur Codex, ChatGPT, Gemini, Mistral, Infomaniak), `diffusion/`, `skills/palambur-method/gabarits/` (un fichier par livrable fréquent), `skills/palambur-method/metiers/` (un fichier par métier), `exemples/`.

### Modifié

- `.claude-plugin/plugin.json` et `marketplace.json` · version `1.0.0`, description sans tiret de ponctuation, mots-clés élargis (`gabarit-palambur`, `agent-skill`, `skill-md`, `leg`, `protection-des-donnees`, `suisse-romande`).
- `adaptations/methode-palambur-prompt.md` et `adaptations/methode-palambur-prompt-court.md` · désormais **générés** par `outils/generer_adaptations.py`, plus édités à la main. Le compteur « Question 1 sur 4 » et le lot de quatre au plus sont conservés ; la liste des hôtes du chapeau vient de la table d’`adaptations/README.md` (relevé du 11.10.2026), qui remplace celle du 12.07.

## [0.1.0] · 2026-07-12

Version initiale, publiée sans numéro de version visible (le `0.1.0` figurait dans `plugin.json` seulement). Les évolutions suivantes ont été poussées **sans changer le numéro** ; elles sont datées ici pour mémoire.

### Ajouté · 2026-07-12

- Le skill `palambur-method` · `SKILL.md` (déclenchement et déroulé en Étapes 0 à 3), `methode-palambur.md` (le Gabarit en 5 + 4 blocs, les 4 niveaux, les champs DONNÉES, le ton), `protection-donnees.md` (anonymisation, marqueurs, mentions nLPD, outils souverains).
- `.claude-plugin/plugin.json` et `marketplace.json` pour l’installation comme plugin Claude Code.
- Les adaptations pour les autres IA (`adaptations/`) · un prompt complet pour GPT personnalisé, Agent Mistral, Infomaniak et Projet Claude, un prompt court pour Gemini Gem et les Instructions personnalisées ChatGPT, avec un guide par plateforme.

### Modifié · 2026-08-04

- Alignement du skill sur le socle canonique de la Méthode Palambur · « Deux noms, deux objets » (la Méthode et le Gabarit), le compteur « Question 1 sur 4 », le lot anticipé de quatre questions posées une par message.

### Modifié · 2026-09-24

- Badge de sécurité Skills Directory (note A) dans le README.
- Remplace le mot « PME » par « entreprises » dans le README, le plugin, le skill et les adaptations, selon la règle maison.

[1.0.0]: https://github.com/PALAMBUR/palambur-method/compare/775304d...v1.0.0
[0.1.0]: https://github.com/PALAMBUR/palambur-method/commits/775304d
