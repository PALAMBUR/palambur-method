# Journal des versions

Ce fichier suit le format [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), adapté à la typographie Palambur (le séparateur est « · », jamais un tiret). Les versions suivent [Semantic Versioning](https://semver.org/lang/fr/).

Une version = une étiquette Git `vX.Y.Z`, une release GitHub et le même numéro dans `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` et ce journal. La chaîne de contrôle `outils/controle.py` **refuse** si les trois numéros divergent.

Depuis le 13.10.2026, les entrées s’écrivent en anglais · les entrées antérieures restent en français. · From 13.10.2026 the entries are written in English; earlier entries stay in French.

Chaque version porte une **Note de qualité** à forme fixe, cinq champs dans cet ordre · Cas joués · Verts · Rouges · Date · Instrument. « Non joué » est une valeur honnête ; un nombre sans date n’en est pas une. Les cas sont ceux d’`epreuves/cas.json`, l’instrument est `epreuves/mesurer.py` (ou `claude plugin eval`, nommé alors). La note ne recopie jamais un chiffre d’une version précédente.

## [Unreleased]

### Changed

- **English becomes the first language** (maintainer’s decision, 13.10.2026 · Switzerland has three national languages, English is the common language of GitHub readers). `README.md` is now the English version, French lives in `README.fr.md`; the language bar of the four READMEs follows the order English · Français · Deutsch · Italiano. The content of the READMEs does not change. The GitHub repository description and its social preview image (a GitHub setting, outside the repo) are in English since the same day.
- **The storefront in English, the engine in French.** Everything a visitor reads before installing is now English first · the bilingual files (`CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, the pull request template, the four issue templates, `docs/pedagogie/FAQ.md`) put English before French; `docs/portabilite/INSTALLATION.md` is translated, the French guide moves to `INSTALLATION.fr.md`; `CITATION.cff`, the issue menu, the descriptions in `plugin.json` and `marketplace.json` are in English. The skill itself (`skills/palambur-method/`, templates, trade sheets, test cases, grid) stays in French · it produces French-language documents and its published measurements were made on that text; the English README says so. From this entry on, this changelog is written in English; earlier entries stay in French.

## [1.6.0] · 2026-10-12

**Le dépôt s’adresse désormais à ses utilisateurs**, plus à l’atelier qui le fabrique. Un audit du 12.10.2026, mené contre les conventions des dépôts à plusieurs dizaines de milliers d’étoiles, a trouvé un cœur solide (exemples, journal, chaîne de contrôle, résultats négatifs publiés) enveloppé dans des fichiers écrits pour l’auteur : voix d’atelier dans 37 fichiers, chemins d’un disque privé dans les 26 fiches métier lues par l’IA, démarrage rapide après 110 lignes, dossiers de diffusion et de gouvernance interne. Cette version refait l’enveloppe sans toucher au fond de la Méthode.

**Pourquoi 1.6.0 et pas 1.0.1.** Le deuxième chiffre compte les **itérations de travail** depuis la naissance du skill le 12.07.2026 : 04.08.2026 (socle canonique), 24.09.2026 (« entreprises »), 11.10.2026 (fondations, plans en 30 et 100 points), 12.10.2026 (1.0.0 et l’expérience Apertus), 12.10.2026 (prompt réécrit et Codex), 12.10.2026 (cette refonte). Six itérations, dont cinq avaient été poussées sous le même numéro ; ce journal les date, le numéro les compte désormais. La règle complète est dans `CONTRIBUTING.md`, section Gouvernance.

### Ajouté

- `README.en.md` · le README en anglais, même structure que le français. Les quatre langues portent une **barre de langues** en tête, quatre badges (CI, licence, version, Skills Directory), une section **« Essayer en deux minutes »** (Claude Code en deux commandes, boîte d’instructions par copier-coller, hôtes `.agents/skills` par lien symbolique), « Vérifier que le skill est chargé », un sommaire, les prérequis, et la section « Citer ».
- `docs/demo-quatre-questions.svg` · une illustration schématique de l’échange (demande, quatre questions, Gabarit, Livrable, Journal de confiance), 1200 × 630, aucune donnée réelle · c’est un dessin, pas une capture.
- `SECURITY.md` (FR puis EN) · ce que le skill fait et ne fait pas chez l’utilisateur, comment signaler, versions prises en charge. Le signalement privé GitHub (« Report a vulnerability ») est activé sur le dépôt depuis le 12.10.2026.
- `CITATION.cff` · métadonnées de citation (Citation File Format 1.2.0), auteur « Palambur » comme entité.
- `.github/PULL_REQUEST_TEMPLATE.md` (FR puis EN) · huit cases qui reprennent les règles de `CONTRIBUTING.md`. `.github/ISSUE_TEMPLATE/config.yml` · tickets vides fermés, renvoi vers les Discussions du dépôt et le site de la Méthode.
- `CONTRIBUTING.md` · prérequis (Claude Code à jour ; Python 3.9 ou plus pour `outils/` seulement), **règle de régénération** (`python3 outils/generer_adaptations.py --ecrire` puis `python3 outils/controle.py` après toute retouche du skill), et deux paragraphes **Gouvernance** qui remplacent l’ancien `GOUVERNANCE.md` : ce que le mainteneur décide seul, comment une version sort, la règle du numéro.
- `docs/pedagogie/FAQ.md` · deux entrées : « Qu’est-ce que `profil-entreprise.md` ? » et « Que veulent dire skill, plugin, marketplace, `CLAUDE.md` ? ». `docs/pedagogie/GLOSSAIRE.md` · section « Les mots de l’outil ».
- `skills/palambur-method/protection-donnees.md` · **Jomini défini en une ligne** à sa première section (outil gratuit d’anonymisation de Palambur, sans compte, dans le navigateur) ; le README dit que c’est la seule mention d’un outil Palambur dans le skill, et pourquoi.
- `outils/metiers/verifier.py` · **contrôle 9** : aucune trace de chemin d’atelier dans les fiches métier (il rougit à 111 traces sur les anciennes fiches, 0 après régénération).
- `epreuves/reponses/codex-natif/` · première **épreuve réelle du skill natif sur Codex** (CLI, 12.10.2026) · le skill est lu depuis `.agents/skills/` par lien symbolique et le premier tour est conforme (« Question 1 sur 4 », lettres, échappatoire, défaut marqué, aucune question nLPD puisque aucune donnée) · un seul tour, `codex exec` n’est pas interactif · relevé dans `RELEVE.md`.
- Dépôt GitHub (réglages, pas des fichiers) · page d’accueil `https://palambur.ch/methode/`, Discussions ouvertes, sujets `claude-code`, `claude-code-skill`, `codex`, `prompt-engineering`, `nlpd`, `rgpd`, `suisse` ajoutés.

### Modifié

- `README.md` · réécrit pour l’utilisateur, en français seul (l’anglais vit dans `README.en.md`). La **démo** suit la sortie réelle du skill : trois lignes d’ouverture, niveau de sensibilité, « Question 1 sur 4 · le lieu et le cadre », ligne « Contexte retenu · … », blocs « Gabarit Palambur » et « Livrable », « Journal de confiance ». La mesure publiée est **recadrée** : 1 vert sur 149, mesuré sur Apertus avec le prompt d’adaptation complet, pas le skill natif ; le skill natif sur Claude n’a pas encore été mesuré. `profil-entreprise.md` est documenté. Le « GPT personnalisé » n’est plus une cible recommandée. La promesse de gratuité ne renvoie plus à un fichier de cadrage.
- `README.de.md`, `README.it.md` · alignés sur le nouveau français (« vingt cas » devient 149 ; chemins `docs/`) · relecture native toujours attendue.
- `docs/exemples/*.md` · les dix déroulés montrent les pièces que le skill rend vraiment (ouverture, niveau de sensibilité, « Contexte retenu », titres de blocs, Journal de confiance), avec un compte honnête de réponses, défauts et marqueurs ; liens corrigés après le déplacement.
- Les **26 fiches métier**, `metiers/README.md`, `metiers/MARCHES.md`, `gabarits/README.md`, `references-juridiques.md` · plus aucun chemin ni nom de fichier de l’atelier (`outil_chaptal.html`, `0600_…`, `prompts.jsonl`, fichiers mémoire) ; les fiches sont régénérées par `outils/metiers/generer.py`, le contenu métier est intact à l’octet. Formule autoportante : « corpus Palambur, relevé du 09.10.2026 », « nomenclature suisse des professions, Office fédéral de la statistique ».
- `docs/portabilite/INSTALLATION.md`, `docs/portabilite/CONFORMITE_STANDARD.md`, `docs/VEILLE_JURIDIQUE.md`, `outils/installer_local.sh`, `.agents/skills/palambur-method/README.md`, `adaptations/README.md`, `skills/palambur-method/agents/openai.yaml` · **voix d’atelier retirée** (relevés de poste, « go », « point N du plan », sessions, chemins de machine, renvois vers des fichiers hors dépôt) ; les relevés datés utiles restent.
- `CODE_OF_CONDUCT.md` · le contact est le formulaire de palambur.ch ; la section « reste à décider » disparaît.
- `.github/workflows/controle.yml` · les cas `evals/` sont **générés puis comptés** contre `epreuves/cas.json` (un dossier par cas, chacun avec son `prompt.md`) au lieu d’être comparés à un dossier commité ; le `grep` du mot interdit exclut `evals/`. `epreuves/generer_evals.py` ne réécrit plus `evals/.gitignore` s’il existe.
- `outils/controle.py` · les témoins de l’épreuve suivent les fichiers dans `docs/`.
- `outils/generer_adaptations.py` et `adaptations/methode-palambur-prompt.md` · quatre règles tirées de l’expérience Apertus (déclencheur nLPD en négatif, Gabarit interdit sans clarification, marqueur écrit mot pour mot et formules « à préciser » interdites, cinq titres de bloc sur cinq lignes) ; gloses coupées pour tenir sous 8'000 caractères. Rejoué sur Apertus (dix cas, 0.0780 CHF) · **10 rouges sur 10, aucun gain**, détail dans `epreuves/RESULTATS_APERTUS_2026-10-11.md` § 9. L’empreinte des adaptations couvre désormais le générateur lui-même.
- `epreuves/jouer_apertus.py` · bras `complet-v2` (même prompt, autre dossier de réponses) ; `epreuves/reponses/apertus-complet-v2/`.

### Déplacé

- `exemples/`, `pedagogie/`, `portabilite/`, `VEILLE_JURIDIQUE.md`, `DIX_COMMANDEMENTS.md` descendent dans **`docs/`**. La racine ne porte plus que les README, le journal, les règles de contribution, de conduite et de sécurité, la citation et la licence.

### Retiré

Ces fichiers servaient l’atelier Palambur (diffusion, gouvernance interne, protocoles de mesure non engagés) et non les utilisateurs ; ils vivent désormais hors du dépôt. Rien n’est perdu, rien n’est publié à leur place.

- `diffusion/` (22 fichiers · kits partenaires, cadrages produit, calendrier éditorial), `GOUVERNANCE.md` (remplacé par la section Gouvernance de `CONTRIBUTING.md`), `mesures/` (3 fichiers) et `outils/mesure.py`, `portabilite/ANNUAIRES.md`, `portabilite/VEILLE_PLATEFORMES.md`, `portabilite/METADONNEES_HOTES.md`, `pedagogie/LETTRE_TRIMESTRIELLE_N1.md`, `pedagogie/ATELIER_45_MIN.md`, `pedagogie/COURS_20_MIN.md`, `pedagogie/FICHE_IMPRIMABLE.md`, `epreuves/BETA_LECTEURS.md`, `epreuves/PROTOCOLE_LECTURE_HUMAINE.md`.
- `evals/` · les **1'097 fichiers générés** quittent le suivi Git ; `evals/README.md` dit comment les régénérer et les jouer.

### Note de qualité

Cas joués : 10 (bras `complet-v2`, prompt d’adaptation réécrit, sur Apertus) · Verts : 0 · Rouges : 10 · Date : 2026-10-12 · Instrument : `epreuves/mesurer.py`. En plus, un cas joué sur Codex avec le skill natif (premier tour conforme, un seul tour, relevé dans `epreuves/reponses/codex-natif/RELEVE.md`), hors instrument. Les 149 cas de 1.0.0 n’ont pas été rejoués ; le skill natif sur Claude n’a pas été joué. Cette version change l’enveloppe du dépôt et la forme des exemples, pas les consignes de `SKILL.md` ni de `methode-palambur.md` ; le prompt d’adaptation est celui mesuré ci-dessus.

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
- Réglages du dépôt GitHub le 12.10.2026 : le sujet `pme` retiré, description réécrite, étiquette `v1.0.0` et release créées.
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
