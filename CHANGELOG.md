# Journal des versions

Ce fichier suit le format [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), adapté à la typographie Palambur (le séparateur est « · », jamais un tiret). Les versions suivent [Semantic Versioning](https://semver.org/lang/fr/).

Une version = une étiquette Git `vX.Y.Z`, une release GitHub et le même numéro dans `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` et ce journal. La chaîne de contrôle `outils/controle.py` **refuse** si les trois numéros divergent.

Chaque version porte une **Note de qualité** à forme fixe, cinq champs dans cet ordre · Cas joués · Verts · Rouges · Date · Instrument. « Non joué » est une valeur honnête ; un nombre sans date n’en est pas une. Les cas sont ceux d’`epreuves/cas.json`, l’instrument est `epreuves/mesurer.py` (ou `claude plugin eval`, nommé alors). La note ne recopie jamais un chiffre d’une version précédente.

## [1.0.0] · 2026-10-12

Première version numérotée, étiquetée et publiée le 12.10.2026 sur le go du fondateur. Le skill existait depuis le 12 juillet 2026 sans numéro, sans licence affichée et en trois copies qui dérivaient (dépôt, skill installé localement, adaptations pour les autres IA). Cette version pose les **fondations** décrites dans le plan en 30 points du 11 octobre 2026, puis les paquets F à M du plan en 100 points (le même jour au soir) et l’expérience Apertus (nuit du 11 au 12).

### Ajouté

- `LICENSE` · le texte complet de la licence MIT, titulaire « Palambur · Victor Semblanet ». Le README l’annonçait depuis le début, GitHub ne l’affichait pas.
- `CHANGELOG.md` · ce journal.
- `README.md` en **deux langues**, français puis anglais, ouvert par un exemple avant/après (la demande brute, les quatre questions, le livrable).
- `outils/generer_adaptations.py` · fabrique les deux prompts d’adaptation (complet et court) depuis `SKILL.md`, ses fichiers de référence et la table des hôtes d’`adaptations/README.md`, avec une empreinte des sources en tête de chaque fichier. Supprime la dérive constatée entre le skill (24.09) et les adaptations (12.07), et la double liste des hôtes (le chapeau citait encore des produits retirés).
- `outils/regle_typo.py` · la règle typographique maison (zéro tiret de ponctuation, apostrophe courbe, montants suisses exempts), copie datée d’une règle qui fait foi dans l’atelier Palambur, avec l’empreinte sha256 de sa source. Permet à `controle.py` de tourner sur un clone sans l’atelier.
- `outils/controle.py` · la chaîne de contrôle du dépôt : règle embarquée à jour sur sa source (quand l’atelier est à côté), typographie maison, zéro « PME », JSON valides, numéro de version unique, adaptations à jour, frontmatter et taille de `SKILL.md`, liens relatifs. Code de retour 0 ou 1, mode `--epreuve` qui casse chaque garde sur témoin fabriqué, option `--racine` pour contrôler une copie.
- `outils/installer_local.sh` · pose le skill du dépôt dans `~/.claude/skills/` (à blanc par défaut, `--ecrire` pour écrire). Le dépôt devient la **seule source** ; la copie locale n’est plus éditée à la main. Refuse si la cible est un lien symbolique (c’est le cas sur la machine de Palambur au 11.10.2026 : le lien vise un clone périmé) et nomme les deux voies de sortie.
- `epreuves/` · vingt cas (`cas.json`), la grille de notation (`grille.md`) et `mesurer.py` qui note une réponse contre la grille. Vingt cas au matin du 11.10, 149 au soir (entrée suivante) ; joués sur Apertus la nuit du 11 au 12.10.2026, voir la Note de qualité.
- `evals/` · les mêmes vingt cas au format `claude plugin eval` (un dossier par cas, graders générés par `epreuves/generer_evals.py`). **Pas encore joués avec `claude plugin eval`** (la dépense sur Claude n’a pas été autorisée ; Apertus l’a été, voir `epreuves/`) ; `evals/results/` est ignoré par git.
- Les commandes `gh` et `git` prêtes à copier pour retirer le sujet `pme`, corriger la description du profil, commiter, pousser et créer la release sont dans une feuille de l’atelier Palambur, **hors du dépôt** (`COMMANDES_GITHUB_SKILL_A_VALIDER_2026-10-11.md`) : elle porte des chemins de machine et des décisions qui ne regardent pas un clone public. Exécutées le 12.10.2026 sur son go.
- Livrés par les autres sessions du 11.10.2026, même version : `CONTRIBUTING.md`, `portabilite/` (installation sur Codex, ChatGPT, Gemini, Mistral, Infomaniak), `diffusion/`, `skills/palambur-method/gabarits/` (un fichier par livrable fréquent), `skills/palambur-method/metiers/` (un fichier par métier).

- `epreuves/cas.json` · passe de vingt-et-un à **149 cas en trois familles** (relevé du 11.10.2026, `python3 epreuves/mesurer.py --compter` fait foi) · `livrable` (25, dont `express_offre_emploi` et `refus_donnees_sensibles`), `metier` (104 · quatre tâches réelles par fiche de `skills/palambur-method/metiers/`, chacune vérifiée présente dans la fiche), `piege` (20 demandes qui poussent à inventer · loi inexistante, CCT fictive, montant à deviner, article précis).
- `epreuves/mesurer.py` · garde `G13_REPONSE_INVENTEE` (la réponse piégée n’est jamais écrite à nu ; `[À` dans les 60 caractères la permet), trois témoins T25 à T27 ; option `--compter`.
- `epreuves/mesurer.py` · garde `G12_DONNEE_SENSIBLE_RECOPIEE` et détecteur de formes sensibles (IBAN, AVS, courriel, téléphone, plaque), témoins T20 à T24.
- `epreuves/mesurer.py` · gardes `G16_JARGON`, `G17_CONTEXTE_ABSENT`, `G18_EXPRESS_NON_DIT`, `G19_REFUS_*` (jargon, ligne « Contexte retenu · », mode express, refus en trois lignes), témoins T40 à T49 ; champs de cas `express` et `refus_attendu`, graders `contexte-express` et `refus-trois-lignes` dans `evals/`.
- `epreuves/generer_evals.py` · famille `piege` (graders `pas-d-invention-N`, `not_contains`), étiquette `metier-NN` par cas métier.
- `epreuves/PROTOCOLE_LECTURE_HUMAINE.md` · vingt cas, trois lecteurs romands, à l’aveugle, grille à six critères · **non joué**.
- `epreuves/PROTOCOLE_TROIS_MODELES.md` · dix cas rejoués sur Claude, GPT et Mistral avec les adaptations · Claude, GPT et Mistral **non joués** ; un quatrième hôte, Apertus, joué les 11 et 12.10 (entrée suivante).
- `epreuves/BETA_LECTEURS.md` · grille de retour et message d’invitation pour cinq bêta-lecteurs romands · personnes non choisies.
- `.github/workflows/controle.yml` · à chaque poussée et pull request, sans secret ni appel de modèle · `controle.py`, les deux `--epreuve`, les evals régénérées et comparées, le mot interdit cherché à nu.
- `mesures/temps_gagne.csv` · la table vide (en-tête seul) du protocole de mesure du temps gagné.
- `outils/controle.py` · garde `taille_corps` (2'800 mots hors frontmatter pour `SKILL.md`).
- `.github/ISSUE_TEMPLATE/04_nouvelle_langue.md` · modèle de ticket « Nouvelle langue », avec la case du locuteur natif.
- `CONTRIBUTING.md` · la règle du locuteur natif, en français et en anglais.
- `portabilite/ANNUAIRES.md` · la procédure pour rejouer la note de sécurité Skills Directory à chaque version, et son historique daté.
- `exemples/` · dix exemples complets, un par gabarit (demande brute, questions, Gabarit rempli, livrable) · n’est plus « en préparation ».
- `pedagogie/` · le manifeste, la FAQ, le glossaire, la fiche imprimable, le cours de 20 minutes, l’atelier de 45 minutes et la première lettre trimestrielle.
- `README.de.md` et `README.it.md` · le README en allemand et en italien, **relecture native à faire** (règle du locuteur natif, `CONTRIBUTING.md`).
- `CODE_OF_CONDUCT.md` · le code de conduite du dépôt.
- `DIX_COMMANDEMENTS.md` · la Méthode en dix règles courtes.
- `VEILLE_JURIDIQUE.md` · comment les références de droit suisse du skill sont relues et datées.
- `GOUVERNANCE.md` · qui décide quoi dans le dépôt, et comment une version sort.
- `diffusion/partenaires/` · kits et textes pour fiduciaires, écoles, associations, presse, podcasts, communautés, ambassadeurs, Infomaniak et l’annuaire Claude.
- `diffusion/produit/` · les cadrages produit · passerelle Chaptal, Jacquard, marques, mesure du temps gagné, parrainage, autorisation de témoignage.
- `epreuves/jouer_apertus.py` · joue les cas contre Apertus (Infomaniak AI Services) · clé lue dans le trousseau macOS, jamais dans un fichier · utilisateur simulé pressé · compteur de dépense `reponses/DEPENSE.csv` avec plafond (`--plafond`, 4.00 CHF) · trois bras `sans`, `complet`, `court`.
- `epreuves/EXPERIENCE_APERTUS_2026-10-11.md` et `epreuves/RESULTATS_APERTUS_2026-10-11.md` · le plan et les résultats de l’expérience (budget 5 CHF posé par le fondateur, 2.8991 CHF dépensés) · 149 cas joués avec le prompt complet, dix avec chaque autre bras · **1 vert sur 149** en bras complet.
- `epreuves/reponses/` · les transcriptions des trois bras (`apertus-sans`, `apertus-complet`, `apertus-court`), le journal de dépense, et la première passe archivée (`_passe1_2026-10-11_instrument_v1/`, instrument défectueux, jamais supprimée).
- `epreuves/mesurer.py` · garde `G20_AUCUNE_CLARIFICATION` (zéro question posée alors que le cas en attend deux ou plus · trou vu sur Apertus, qui livrait l’offre d’emploi sans une question), témoins T05b et T07b · 39 témoins.

### Modifié

- `.claude-plugin/plugin.json` et `marketplace.json` · version `1.0.0`, description sans tiret de ponctuation, mots-clés élargis (`gabarit-palambur`, `agent-skill`, `skill-md`, `leg`, `protection-des-donnees`, `suisse-romande`).
- `adaptations/methode-palambur-prompt.md` et `adaptations/methode-palambur-prompt-court.md` · désormais **générés** par `outils/generer_adaptations.py`, plus édités à la main. Le compteur « Question 1 sur 4 » et le lot de quatre au plus sont conservés ; la liste des hôtes du chapeau vient de la table d’`adaptations/README.md` (relevé du 11.10.2026), qui remplace celle du 12.07.

### Modifié · 12.10.2026, après l’expérience Apertus

- `outils/generer_adaptations.py` et les deux prompts d’`adaptations/` · le prompt complet ne portait ni la ligne « Contexte retenu · » ni la règle zéro jargon, que la grille mesurait pourtant (`G17`, `G16`) · ajoutés aux deux prompts, redites coupées (7'940 / 8'000 et 1'492 / 1'500 caractères), deux témoins d’épreuve de plus (27).
- `epreuves/mesurer.py` · la question nLPD groupée au Gabarit comptait « absente » · elle compte « groupée ».
- `epreuves/grille.md` · ligne `G20_AUCUNE_CLARIFICATION`.
- `outils/controle.py` et `.github/workflows/controle.yml` · les transcriptions de modèles (`epreuves/reponses/`) sont tues et comptées par la typographie et le mot interdit · pièces à conviction, on ne les corrige pas.
- `README.md`, `epreuves/README.md`, `epreuves/PROTOCOLE_TROIS_MODELES.md` · « non joué » devient « joué sur Apertus, non joué sur Claude, GPT et Mistral ».

### Note de qualité

Cas joués : 149 (bras `complet`, prompt d’adaptation sur Apertus · 10 de plus en bras `sans` et 10 en bras `court`) · Verts : 1 · Rouges : 148 · Date : 2026-10-12 · Instrument : `epreuves/mesurer.py` (39 témoins), transcriptions dans `epreuves/reponses/apertus-complet/`. Le skill natif sur Claude n’a pas été joué (dépense non autorisée) ; cette note mesure le prompt collé sur un autre modèle, pas le skill. Détail dans `epreuves/RESULTATS_APERTUS_2026-10-11.md`.

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
