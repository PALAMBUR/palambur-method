# Contribuer · Contributing

Français d’abord, English below.

---

## Français

Merci de votre intérêt. Ce dépôt porte **la Méthode Palambur** sous forme de skill : une discipline de clarification avant production, un Gabarit en cinq blocs, des garde-fous suisses et l’interdiction d’inventer. Toute contribution qui renforce l’un de ces quatre points est bienvenue. Toute contribution qui les affaiblit sera discutée avant d’être refusée.

### Trois façons de contribuer

1. **Signaler un défaut** · le skill a posé une mauvaise question, a inventé une donnée, a oublié le compteur, a cité une loi qu’il n’aurait pas dû citer. Ouvrez un ticket avec le modèle « Défaut ».
2. **Proposer un gabarit de livrable** · un fichier dans `skills/palambur-method/gabarits/` pour un livrable fréquent (offre d’emploi, devis, certificat de travail, note interne…) : ses champs DONNÉES, ses garde-fous, un exemple rempli. C’est la contribution la plus utile et la plus simple. Modèle « Nouveau gabarit ».
3. **Corriger une référence juridique** · une loi mal nommée, une base légale périmée, une convention collective citée sans source. Modèle « Correction juridique ».

Les tickets marqués **« bonne première contribution »** sont réservés aux gabarits : une personne qui écrit un gabarit sait de quoi elle parle, et c’est tout ce qu’il faut.

### Prérequis

- **Pour utiliser le skill** : aucun. Un hôte qui lit le standard `SKILL.md` suffit (voir [`docs/portabilite/INSTALLATION.md`](docs/portabilite/INSTALLATION.md)).
- **Pour contribuer et lancer les contrôles** : Claude Code à jour (les commandes `/plugin`, `/skills` et `/skill-doctor` servent à vérifier le chargement) et **Python 3.9 ou plus** pour les scripts d’`outils/` et d’`epreuves/`, sans bibliothèque à installer.

### Avant d’ouvrir une pull request

- **Un gabarit ne touche ni `SKILL.md` ni les adaptations** : il se pose dans `gabarits/` et la chaîne de contrôle le vérifie. Les adaptations ne suivent pas toutes seules, voir la règle de régénération ci-dessous.
- **Règle de régénération** · toute modification dans `skills/palambur-method/` (`SKILL.md`, `methode-palambur.md`, `protection-donnees.md`, et aussi la table des hôtes d’`adaptations/README.md`) exige deux commandes, dans cet ordre : `python3 outils/generer_adaptations.py --ecrire`, qui refabrique les deux prompts d’`adaptations/`, puis `python3 outils/controle.py`. Sans la première, le contrôle `adaptations` refuse : l’empreinte déclarée en tête des prompts ne correspond plus aux sources. Ne modifiez jamais les deux prompts à la main.
- **Lancez la chaîne de contrôle** : `python3 outils/controle.py`. Elle refuse si la typographie, le numéro de version, les liens ou les adaptations ne sont pas conformes. Un refus n’est pas une sanction, c’est une indication.
- **Un gabarit = un fichier**, nommé par le livrable, en français suisse romand, vouvoiement, sans superlatif.

### La règle typographique maison, en trois lignes

1. **Aucun tiret de ponctuation** · ni cadratin, ni demi-cadratin, ni trait d’union entre deux mots. Le séparateur est le point médian « · ». Le trait d’union d’un mot composé (garde-fou) et la puce de liste restent.
2. **L’apostrophe est courbe** (’) dans la langue : l’outil, n’est. Elle reste droite seulement entre deux chiffres : 4'820 CHF.
3. **Le sigle français des petites et moyennes entreprises n’existe pas ici** · on écrit « entreprises ». Le contrôle le refuse.

### La règle juridique, en une ligne

**Jamais un numéro d’article de loi sans `[À VÉRIFIER]`.** On nomme le texte (CO, LTr, LEg, nLPD, LCD), on ne cite pas un numéro d’article que personne n’a vérifié à la date de la contribution. Une convention collective n’est jamais citée sans sa source. Si vous êtes certain d’un article, écrivez-le quand même avec le marqueur : la vérification appartient à la personne qui relit, pas à la personne qui écrit.

### La règle du locuteur natif, en une ligne

**Aucune langue n’entre dans le skill sans la relecture d’un locuteur natif de cette langue qui exerce l’un des métiers visés.** Une traduction automatique est un brouillon, pas une contribution. La pull request nomme la **fonction** du relecteur (jamais son nom), la date de sa relecture et les fichiers relus ; le modèle de ticket « Nouvelle langue » porte cette case, et une pull request qui ne la coche pas attend. La règle vaut pour l’anglais aussi, même si le README est déjà bilingue · l’anglais du skill est relu comme les autres.

### Ce que nous ne prenons pas

- Des gabarits qui inventent des valeurs par défaut là où la Méthode exige un marqueur.
- Des références à des outils d’IA qui envoient des données hors de Suisse présentées comme « souverains ».
- Des contributions qui ajoutent de la publicité pour Palambur dans les livrables : le skill est gratuit et il le reste, sans message commercial dans ce qu’il produit.

**Code de conduite et traductions** · le [code de conduite](CODE_OF_CONDUCT.md) s’applique à tout échange dans ce dépôt ; toute traduction (`README`, adaptations, gabarits) est relue par un locuteur natif de la langue cible avant d’être fusionnée, et porte en tête la mention « relecture native à faire » tant qu’elle ne l’a pas été.

### Gouvernance

**Ce que seul le mainteneur décide.** Le dépôt est tenu par Palambur, qui en est le mainteneur. Trois choses lui reviennent et ne se décident pas dans une pull request : le **numéro de version**, **ce qui entre dans le skill** (un gabarit, une fiche métier, une règle de `SKILL.md`) et **les textes de loi nommés** dans `references-juridiques.md`. Tout le reste se discute dans les tickets, et une pull request conforme aux règles ci-dessus est relue dans les dix jours ouvrables.

**Comment une version sort.** Une version est une entrée du [`CHANGELOG.md`](CHANGELOG.md) avec sa **note de qualité** (cas joués, verts, rouges, date, instrument ; « non joué » est une valeur honnête), le même numéro dans `.claude-plugin/plugin.json` et `.claude-plugin/marketplace.json`, une étiquette Git `vX.Y.Z`, une release GitHub et une **CI verte** (`outils/controle.py`). La règle du numéro : le **premier chiffre** change quand le format du skill ou la Méthode elle-même change de façon incompatible ; le **deuxième chiffre** compte les itérations de travail depuis la naissance du skill le 12.07.2026 (la version 1.6.0 est la sixième itération) ; le **troisième chiffre** est une correction sans contenu nouveau (une faute, un lien, une typographie). Une nouvelle version incrémente toujours `version` dans `plugin.json`, sinon les utilisateurs gardent l’ancienne copie.

### Licence

En contribuant, vous acceptez que votre contribution soit publiée sous la licence MIT du dépôt.

---

## English

Thank you for your interest. This repository holds **the Palambur Method** as a skill: a discipline of clarification before production, a five block template, Swiss legal safeguards and a ban on inventing data. Any contribution that strengthens one of these four points is welcome. Any contribution that weakens them will be discussed before it is declined.

### Three ways to contribute

1. **Report a defect** · the skill asked the wrong question, invented a value, forgot the counter, or cited a law it should not have cited. Open an issue with the "Defect" template.
2. **Propose a deliverable template** · a file in `skills/palambur-method/gabarits/` for a frequent deliverable (job advert, quote, employment certificate, internal memo…): its DATA fields, its safeguards, one completed example. This is the most useful and the simplest contribution. "New template" issue.
3. **Correct a legal reference** · a misnamed law, an outdated legal basis, a collective agreement cited without a source. "Legal correction" issue.

Issues labelled **"good first contribution"** are reserved for templates: someone who writes a template knows the subject, and that is all it takes.

### Prerequisites

- **To use the skill**: none. Any host that reads the `SKILL.md` standard is enough (see [`docs/portabilite/INSTALLATION.md`](docs/portabilite/INSTALLATION.md), in French).
- **To contribute and run the checks**: an up to date Claude Code (the `/plugin`, `/skills` and `/skill-doctor` commands verify loading) and **Python 3.9 or later** for the scripts in `outils/` and `epreuves/`, with no library to install.

### Before opening a pull request

- **A template touches neither `SKILL.md` nor the adaptations**: it goes in `gabarits/` and the control chain checks it. The adaptations do not follow on their own, see the regeneration rule below.
- **Regeneration rule** · any change inside `skills/palambur-method/` (`SKILL.md`, `methode-palambur.md`, `protection-donnees.md`, and also the host table in `adaptations/README.md`) requires two commands, in this order: `python3 outils/generer_adaptations.py --ecrire`, which rebuilds the two prompts in `adaptations/`, then `python3 outils/controle.py`. Without the first one, the `adaptations` check refuses: the fingerprint declared at the top of the prompts no longer matches the sources. Never edit the two prompts by hand.
- **Run the control chain**: `python3 outils/controle.py`. It refuses when typography, version number, links or adaptations are not compliant. A refusal is not a sanction, it is a pointer.
- **One template = one file**, named after the deliverable, in Swiss French, formal address, no superlatives.

### The house typography rule, in three lines

1. **No punctuation dash** · no em dash, no en dash, no hyphen between two words. The separator is the middle dot "·". Hyphens inside compound words and list bullets stay.
2. **Apostrophes are curly** (’) in prose: l’outil, n’est. They stay straight only between two digits: 4'820 CHF.
3. **The French acronym for small and medium sized businesses is banned** · we write "entreprises" in French and "businesses" or "organisations" in English. The control chain refuses it.

### The legal rule, in one line

**Never a numbered article of law without `[À VÉRIFIER]`** (to be checked). Name the text (CO, LTr, LEg, nLPD, LCD), never quote an article number nobody has verified at the date of the contribution. A collective agreement is never cited without its source. If you are sure of an article, write it anyway with the marker: verification belongs to the reviewer, not to the writer.

### The native speaker rule, in one line

**No language enters the skill without a review by a native speaker of that language who works in one of the target professions.** A machine translation is a draft, not a contribution. The pull request names the reviewer’s **role** (never their name), the date of the review and the files reviewed; the "New language" issue template carries this checkbox, and a pull request that leaves it unticked waits. The rule applies to English too, even though the README is already bilingual · the skill’s English is reviewed like any other language.

### What we do not accept

- Templates that invent default values where the Method requires a marker.
- References to AI tools that send data outside Switzerland presented as "sovereign".
- Contributions that add advertising for Palambur inside deliverables: the skill is free and stays free, with no commercial message in what it produces.

**Code of conduct and translations** · the [code of conduct](CODE_OF_CONDUCT.md) applies to every exchange in this repository; every translation (`README`, adaptations, templates) is proofread by a native speaker of the target language before it is merged, and carries the note “relecture native à faire” at the top until that is done.

### Governance

**What only the maintainer decides.** The repository is maintained by Palambur. Three things belong to the maintainer and are not decided in a pull request: the **version number**, **what enters the skill** (a template, a trade sheet, a rule in `SKILL.md`) and **the legal texts named** in `references-juridiques.md`. Everything else is discussed in issues, and a pull request that follows the rules above is reviewed within ten working days.

**How a version is released.** A version is an entry in [`CHANGELOG.md`](CHANGELOG.md) with its **quality note** (cases played, green, red, date, instrument; “not played” is an honest value), the same number in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, a Git tag `vX.Y.Z`, a GitHub release and a **green CI** (`outils/controle.py`). The numbering rule: the **first digit** changes when the skill format or the Method itself changes incompatibly; the **second digit** counts the working iterations since the skill was born on 12.07.2026 (version 1.6.0 is the sixth iteration); the **third digit** is a correction with no new content (a typo, a link, typography). A new version always increments `version` in `plugin.json`, otherwise users keep the old copy.

### Licence

By contributing, you agree that your contribution is published under the repository’s MIT licence.
