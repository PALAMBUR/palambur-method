# Annuaires et marketplaces · où soumettre le skill

Relevé du 11.10.2026. **Rien n’a été soumis** : chaque action ci-dessous est **« à exécuter après le go de Victor »**. Chaque annuaire porte son URL, ses conditions lues sur place, la procédure et le texte de soumission prêt (français, puis anglais en orthographe britannique).

## Vue d’ensemble

| Annuaire | État au 11.10.2026 | Condition bloquante | Geste |
|---|---|---|---|
| **Skills Directory** | **déjà listé**, note A 100/100 | aucune | rien ; re-scan automatique |
| **skills.sh** (Vercel) | **déjà présent** (`skills.sh/palambur/palambur-method/palambur-method`, HTTP 200) | aucune, indexation par télémétrie de `npx skills add` | rien |
| **SkillsMP** | indexation automatique quotidienne de GitHub ; présence du skill **non confirmée** (page de recherche rendue côté client, illisible à nos outils) | le dépôt doit porter le sujet GitHub **`claude-skills`** ou **`claude-code-skill`** ; il porte `claude-skill` (sans s), qui ne correspond pas | ajouter un sujet GitHub (Victor ou agent dépôt) |
| **mdskills.ai** | non listé (`mdskills.ai/search?q=palambur` → HTTP 404) | formulaire derrière connexion ; « Every listing reviewed » | soumettre via `/submit` |
| **Annuaire Anthropic** (claude.ai/directory) | non soumis | **forfait payant** Claude (Pro, Max, Team, Enterprise) ; compte GitHub relié à claude.ai ; dépôt public ; fichier `LICENSE` (présent depuis le 11.10) | soumettre un **bundle** via `claude.ai/directory/manage` |
| **Annuaire de plugins OpenAI** (ChatGPT et Codex) | non soumis | **vérification d’identité** individuelle ou d’entreprise du compte OpenAI ; droit « Apps Management write » | créer un plugin « Skills only » via `platform.openai.com/plugins` |
| **awesome-claude-skills** (travisvn, 15,4 k étoiles) | non listé | **≥ 10 étoiles GitHub**, sinon la PR est fermée automatiquement ; le dépôt en a **2** ; **PR rédigée sans assistance IA (fermeture sinon)** | attendre 10 étoiles, puis PR **écrite à la main par Victor** |
| **awesome-claude-skills** (karanb192, 544 étoiles, MIT) | non listé | commits dans les 6 derniers mois (oui, 24.09) ; ligne < 150 caractères | PR d’une ligne de table |
| **awesome-claude-skills** (ComposioHQ, 76,9 k étoiles) | non listé | la PR **ajoute une copie du dossier du skill** dans leur dépôt | décision : accepter une copie hors source ou s’abstenir |
| **awesome-codex-skills** (ComposioHQ, redirige vers `composio-community/awesome-codex-skills`, 16,9 k étoiles) | non listé | idem, dossier avec `SKILL.md` | même décision |
| **awesome-claude-code** (hesreallyhim, 55,4 k étoiles) | non listé | `CONTRIBUTING.md` (lu le 11.10.2026) : « Do not open a PR. Just fill out the form. » ; ≥ 14 jours depuis le premier commit et développement actif, ou ≥ 100 étoiles, sinon fermeture automatique ; le fichier ne liste pas de catégories, les skills n’y sont pas nommés | issue, faible chance |
| **awesome-codex-cli** (milisp, 120 étoiles, CC0) | non listé | issue seulement, section Agent Skills | issue |
| **awesome-claude-code-and-skills** (GetBindu, 199 étoiles) | non listé | non lu en détail | à relire avant de soumettre |

Les comptes d’étoiles sont ceux affichés le 11.10.2026 ; ils vieillissent.

---

## 1 · Skills Directory · déjà fait

- URL : `https://www.skillsdirectory.com/skills/palambur-palambur-method` (HTTP 200 le 11.10.2026).
- Lu sur la fiche : **Grade A, 100/100**, ajouté et scanné le 06.09.2026, commande affichée `npx -y skills add PALAMBUR/palambur-method --skill palambur-method --agent claude-code`. Soumission d’autres skills : `https://app.skillsdirectory.com/submit` (connexion GitHub, Google ou e-mail) ; retrait sous 72 h sur demande.
- **Geste** : aucun. À surveiller à chaque version (le scan relit GitHub).

## 2 · skills.sh (Vercel) · déjà présent

- URL : `https://skills.sh/palambur/palambur-method/palambur-method` (HTTP 200 ; l’URL avec `PALAMBUR` en majuscules **redirige** (308, puis 200) vers `www.skills.sh/palambur/palambur-method/palambur-method`).
- FAQ (`https://skills.sh/docs/faq`, 11.10.2026) : l’annuaire se remplit **automatiquement** par la télémétrie de la commande `npx skills add owner/repo` ; pas de formulaire.
- **Geste** : aucun. Chaque installation par `npx skills add PALAMBUR/palambur-method` fait monter le compteur.

## 3 · SkillsMP

- URL : `https://skillsmp.com` ; FAQ `https://skillsmp.com/docs/faq` (11.10.2026).
- Conditions lues : indexation **automatique quotidienne** des dépôts GitHub qui portent un `SKILL.md` avec frontmatter **et** le sujet GitHub **`claude-skills`** ou **`claude-code-skill`**. La soumission manuelle est annoncée « coming soon ».
- État du dépôt (`gh repo view`, 11.10.2026) : sujets `claude-code, claude-skill, conformite, ia, intelligence-artificielle, nlpd, prompt-engineering, rgpd, skill, suisse`, plus le sujet en trois lettres que la règle maison interdit (plan, point 2). **Aucun des deux sujets attendus.**
- **Geste (après go)** : ajouter un sujet. Commande, depuis la racine du dépôt (action distante, à exécuter par Victor ou l’agent dépôt) :

```bash
gh repo edit PALAMBUR/palambur-method --add-topic claude-skills
```

Puis vérifier le lendemain sur `https://skillsmp.com/search?q=palambur`.

## 4 · mdskills.ai

- URL : `https://www.mdskills.ai` (HTTP 200) ; soumission `https://www.mdskills.ai/submit` (formulaire derrière connexion, contenu non lisible le 11.10.2026) ; spécification acceptée `https://www.mdskills.ai/specs/skill-md`.
- Conditions lues sur la page d’accueil : plus de 4’000 fiches, et la mention **« Every listing reviewed »**. Les champs exacts du formulaire ne sont pas connus : **non confirmé**.
- **Geste (après go)** : se connecter, ouvrir `/submit`, donner l’URL du dépôt et le texte ci-dessous.

## 5 · Annuaire Anthropic (claude.ai/directory)

- URLs : annuaire `https://claude.ai/directory` (HTTP 403 sans connexion) ; portail de soumission `https://claude.ai/directory/manage` (HTTP 403 sans connexion) ; documentation `https://claude.com/docs/directory/publish`, `https://claude.com/docs/plugins/submit`, liste de contrôle `https://claude.com/docs/plugins/pre-submission-checklist` (toutes HTTP 200 le 11.10.2026).
- Conditions lues : **« Anyone on a paid Claude plan can submit »** (Pro, Max, Team, Enterprise ; pas Free) ; compte GitHub **relié** dans claude.ai ; dépôt **public** avant mise en ligne ; **« Skills aren’t a submission type on their own. Put them in a bundle. »** ; le marketplace officiel `claude-plugins-official` **ne prend pas** de soumissions par le portail ; une seule fiche atteint claude.ai, Cowork et Claude Code (installation `<nom>@synced`) ; 10 soumissions par 24 h ; **relecture humaine** de la première version ; options d’auto-publication ensuite.
- Liste de contrôle, points qui **bloquent** : `README.md` d’au moins 40 mots dans le dossier du plugin (le README de la racine fait 3’099 mots au relevé du 11.10.2026 à 22 h 10, un autre agent l’écrit encore : **à relever le jour du commit**) ; **fichier `LICENSE` ou champ `license` dans `plugin.json`** (les deux sont présents depuis le 11.10.2026 : conforme) ; nom non ASCII (le nom `palambur` passe) ; **aucun lien symbolique commité** pour une entrée chargée ; aucun `.DS_Store` ; frontmatter YAML valide avec une `description` texte. Points **« Held for a reviewer »** (soumission possible, un relecteur Anthropic lit la version avant mise en ligne) : fichier non image de plus de 256 Kio, plus de 512 fichiers, fichier binaire autre qu’image ou police. Points en **avertissement** : nom hors motif minuscules et traits d’union, `description`, `author`, `version` renseignés (oui : 1.0.0).
- Pré-requis interne : la `description` du skill doit rester **sous 1’024 caractères** (938 au relevé du 11.10.2026 à 22 h 10, voir `CONFORMITE_STANDARD.md`).
- **Geste (après go, par Victor, connecté avec un forfait payant)** : `claude.ai/directory/manage` › nouvelle soumission › bundle depuis le dépôt GitHub `PALAMBUR/palambur-method`. Avant : lancer la liste de contrôle en local.

```bash
claude plugin validate --strict .
```

## 6 · Annuaire de plugins OpenAI (ChatGPT et Codex)

- URLs : portail `https://platform.openai.com/plugins` (HTTP 403 sans connexion) ; procédure `https://developers.openai.com/plugins/deploy/submission` et `https://developers.openai.com/plugins/guides/submit-claude-plugin` (HTTP 200 le 11.10.2026).
- Conditions lues : le portail accepte un **plugin Claude tel quel** : archive ZIP avec `.claude-plugin/plugin.json` (description non vide) et `skills/<nom>/SKILL.md` ; il le convertit en `.codex-plugin/plugin.json`. Type **« Skills only »** : pas de MCP ni d’URL légales à fournir. Compte OpenAI avec le droit **Apps Management write** et **vérification d’identité** (individuelle ou d’entreprise) : « Complete individual or business verification … to publish under your name ». Champs : nom et sous-titre ≤ 30 caractères, description longue ≤ 4’000, icône carrée ≥ 48 px. Relecture par e-mail, **sans délai annoncé, aucun frais mentionné**. Non pris en charge pour un plugin skills-only : hooks, `userConfig`, `marketplace.json`.
- Le dépôt `github.com/openai/skills` est **déprécié** et renvoie vers `github.com/openai/plugins`, dont la page affiche « Only collaborators can create PRs » (lu le 11.10.2026) : pas une porte.
- **Geste (après go, par Victor)** : vérification d’identité OpenAI, puis `platform.openai.com/plugins` › Create plugin › Skills only › téléverser le ZIP du dépôt (racine avec `.claude-plugin/` et `skills/`). Fabriquer le ZIP depuis la racine du dépôt :

```bash
zip -r palambur-plugin.zip .claude-plugin skills LICENSE README.md
```

## 7 · Listes « awesome » sur GitHub

Toutes vérifiées HTTP 200 le 11.10.2026.

| Liste | URL | Règles lues | Texte à fournir |
|---|---|---|---|
| travisvn/awesome-claude-skills | `https://github.com/travisvn/awesome-claude-skills` | `CONTRIBUTING.md` : format `- **[Nom](lien)** - description`, **un seul ajout par PR**, **≥ 10 étoiles sinon fermeture automatique**, et **« the PR not be explicitly generated / submitted with AI-assistance »** (« PRs will be closed without comment if the submitter has failed to acknowledge this »), ton non promotionnel | ligne EN ci-dessous, **quand le dépôt aura 10 étoiles**, PR **rédigée et ouverte à la main par Victor**, pas par un agent |
| karanb192/awesome-claude-skills | `https://github.com/karanb192/awesome-claude-skills` | ligne de table `\| [skill-name](url) \| tâche \|`, < 150 caractères, commits dans les 6 mois, titre de PR « Add [skill-name] to [category] » | ligne de table EN ci-dessous |
| ComposioHQ/awesome-claude-skills | `https://github.com/ComposioHQ/awesome-claude-skills` | la PR **ajoute un dossier** du skill dans leur dépôt + une ligne README `- [Skill Name](./skill-name/) - One-sentence description.`, pas d’emoji | **décision** : une copie du skill vivrait hors du dépôt source |
| composio-community/awesome-codex-skills (ex ComposioHQ, redirection 301) | `https://github.com/composio-community/awesome-codex-skills` | dossier avec `SKILL.md`, pas de README dans le dossier | même décision |
| hesreallyhim/awesome-claude-code | `https://github.com/hesreallyhim/awesome-claude-code/blob/main/CONTRIBUTING.md` | « ALL RECOMMENDATIONS MUST BE MADE USING THE WEB UI ISSUE FORM TEMPLATE », « Do not open a PR. Just fill out the form. » ; ≥ 14 jours depuis le premier commit et actif, ou ≥ 100 étoiles ; catégories non listées dans le fichier | issue EN, chance faible |
| milisp/awesome-codex-cli | `https://github.com/milisp/awesome-codex-cli` | issue seulement, section Agent Skills | issue EN |
| GetBindu/awesome-claude-code-and-skills | `https://github.com/GetBindu/awesome-claude-code-and-skills` | règles non lues en détail | relire avant |

Les listes dont le format est une **ligne avec un tiret** (`- **[Nom]…** - …`) imposent ce tiret : c’est la syntaxe de la liste d’accueil, pas la nôtre ; on la respecte chez eux.

---

## 8 · Textes de soumission prêts

Sans sigle interdit, sans tiret long. Le séparateur est « · ». À adapter à la longueur demandée par chaque formulaire.

### Français · court (≤ 150 caractères)

> Méthode Palambur · pose 4 questions ciblées avant tout livrable métier, protège les données (nLPD) et n’invente ni chiffre ni article de loi.

### Français · moyen (≤ 300 caractères)

> Méthode Palambur · un skill qui clarifie une demande métier sous-spécifiée avant de produire : lot de quatre questions au plus, une par message, défaut prudent signalé. Anonymisation par défaut (nLPD), aucun chiffre ni article de loi inventé. Pensé pour les entreprises de Suisse romande. Licence MIT.

### Français · long (annuaire Anthropic, mdskills, ≤ 1’000 caractères)

> **Méthode Palambur** transforme une demande en une ou deux phrases (« fais une offre d’emploi pour un peintre à 80 % ») en un livrable qu’on peut envoyer en confiance. Le skill évalue d’abord ce qui manque, pose au plus quatre questions, une par message, avec des choix lettrés et un défaut prudent, puis rend deux choses : le Gabarit Palambur rempli (le prompt réutilisable) et le livrable final.
>
> Trois garde-fous : protection des données par défaut (anonymisation et mention nLPD, question binaire posée en premier), aucune donnée inventée (les manques deviennent des marqueurs [À COMPLÉTER] ou [À VÉRIFIER]), aucun numéro d’article de loi sans source. Un mode relecture passe au crible un texte déjà écrit sans poser de question.
>
> Pensé pour les entreprises de Suisse romande (CO, LTr, LEg, nLPD), en français suisse romand, vouvoiement. Licence MIT. Dépôt : github.com/PALAMBUR/palambur-method · Site : palambur.ch

### English · short (≤ 150 characters)

> Palambur Method · asks up to four targeted questions before any business deliverable, protects personal data by default and never invents figures or legal references.

### English · medium (≤ 300 characters)

> Palambur Method · a skill that clarifies an under-specified business request before producing anything: at most four questions, one per message, with a safe default. Anonymisation by default (Swiss data protection act), no invented figures or legal articles. Built for businesses in French-speaking Switzerland. MIT licence.

### English · long (OpenAI plugin directory, ≤ 4,000 characters; also fits mdskills)

> **Palambur Method** turns a one-line request ("write a job ad for a painter at 80 %") into a deliverable you can send with confidence. The skill first assesses what is missing, then asks at most four questions, one per message, each with lettered choices and a flagged safe default. It then returns two things: the completed Palambur Template (the reusable prompt) and the final deliverable.
>
> Three safeguards: data protection by default (anonymisation and a Swiss data protection notice, with a yes/no question asked first), no invented data (gaps become visible [TO COMPLETE] or [TO VERIFY] markers), and no legal article number without a source. A review mode checks an existing text against six filters without asking any question.
>
> Built for businesses in French-speaking Switzerland (Swiss Code of Obligations, Labour Act, Gender Equality Act, data protection act), written in Swiss French with formal address. Works with Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and any host that follows the open Agent Skills standard. MIT licence. Repository: github.com/PALAMBUR/palambur-method · Website: palambur.ch

### Lignes pour les listes « awesome » (format imposé par chaque liste)

travisvn (quand ≥ 10 étoiles ; cette ligne est une proposition, la PR elle-même doit être **rédigée et ouverte par Victor sans assistance IA**, c’est la règle de la liste) :

```text
- **[Palambur Method](https://github.com/PALAMBUR/palambur-method)** - Clarifies an under-specified business request with at most four questions before producing, anonymises personal data by default (Swiss law) and never invents figures or legal references. Swiss French.
```

karanb192 (ligne de table, < 150 caractères) :

```text
| [palambur-method](https://github.com/PALAMBUR/palambur-method) | Asks four targeted questions before a business deliverable, protects data, invents nothing |
```

ComposioHQ (ligne README, si Victor accepte la copie du dossier) :

```text
- [Palambur Method](./palambur-method/) - Asks up to four targeted questions before any business deliverable, protects personal data by default and never invents a figure or a legal article. Inspired by the Palambur consulting method (Switzerland).
```

Issue (hesreallyhim, milisp), corps proposé :

```text
Name: palambur-method
Repository: https://github.com/PALAMBUR/palambur-method
Category: Agent Skills
Description: A SKILL.md that clarifies an under-specified business request with at most four questions (one per message, safe defaults) before producing, anonymises personal data by default under Swiss law, and never invents figures or legal references. Includes a review mode for existing texts. Swiss French, MIT licence, follows the Agent Skills standard.
```

---

## 9 · Ordre proposé et décisions pour Victor

1. **Sans décision** : rien à faire pour Skills Directory et skills.sh, ils suivent GitHub.
2. **Un sujet GitHub** (`claude-skills`) débloque SkillsMP ; c’est le geste le moins cher. À faire avec le retrait du sujet interdit (plan, point 2).
3. **Annuaire Anthropic** : accessible dès que la `description` du skill repasse sous 1’024 caractères et que la version 1.0.0 est poussée. Demande le compte claude.ai de Victor (forfait payant). **À décider : soumettre, oui ou non.**
4. **Annuaire OpenAI** : demande la **vérification d’identité** de Victor. Même décision que le point 17 du plan (GPT public), puisque les GPT personnalisés sont en retrait et que le plugin est la voie officielle.
5. **mdskills.ai** : une connexion et un formulaire, faible coût, relecture humaine. **À décider.**
6. **Listes awesome** : karanb192 tout de suite (PR d’une ligne) ; travisvn à 10 étoiles, **PR manuelle de Victor sans assistance IA** (règle de la liste) ; ComposioHQ **seulement si** Victor accepte qu’une copie du skill vive dans un dépôt tiers (contraire à « une seule source », mais 76’900 étoiles de visibilité). **À décider.**

Aucune de ces actions n’a été lancée le 11.10.2026.

---

## 10 · Rejouer la note de sécurité à chaque version

Plan du 11.10.2026, point 90. Le README affiche le badge Skills Directory (image servie par leur API, elle change toute seule quand le scan change). Ce que l’image ne dit pas, c’est **quand** le dernier scan a eu lieu ni **quelle version** il a lue. La note vaut pour l’état scanné, pas pour le dépôt d’aujourd’hui · une version qui ajoute un script, un workflow ou un fichier d’agents peut la faire bouger.

### La procédure, à chaque étiquette `vX.Y.Z`

1. **Après la poussée de l’étiquette**, attendre le re-scan. La fiche lue le 11.10.2026 dit que le scan relit GitHub de lui-même ; la cadence et l’existence d’un déclenchement manuel ne sont pas connues `[À VÉRIFIER : fréquence du re-scan et bouton de re-scan sur la fiche]`.
2. **Ouvrir la fiche** `https://www.skillsdirectory.com/skills/palambur-palambur-method` et lire trois choses · la note (lettre), le score (sur 100), la date du scan affichée.
3. **Reporter une ligne** dans la table ci-dessous · version, date du scan, note et score, date de la lecture, fonction de la personne qui a lu.
4. **Dater le badge dans le README** · à côté de l’image, en clair, « scan du jj.mm.aaaa » (le README est tenu par la session qui en a la charge ; cette section ne l’édite pas).
5. **Si la note baisse**, la release ne se publie pas tant que la cause n’est pas nommée dans `CHANGELOG.md` (section « Modifié » ou « Corrigé » de la version). Une baisse non expliquée est un défaut, pas un détail d’annuaire.
6. **Si la note ne bouge pas** mais que la date du scan est antérieure à l’étiquette, la ligne le dit (« scan antérieur à la version ») · un A lu sur l’ancienne version ne vaut rien pour la nouvelle.

### Historique des scans

| Version lue par le scan | Date du scan | Note · score | Lecture faite le | Par (fonction) |
|---|---|---|---|---|
| sans numéro (état du 24.09.2026, avant 1.0.0) | 06.09.2026 (date d’ajout et de scan affichée sur la fiche) | A · 100/100 | 11.10.2026 | agent de la session Évaluation et qualité |
| 1.0.0 | `[À COMPLÉTER]` | `[À COMPLÉTER]` | `[À COMPLÉTER]` | `[À COMPLÉTER]` |

Les autres annuaires qui notent (mdskills.ai relit chaque fiche à la main, SkillsMP indexe sans noter au 11.10.2026) entrent dans cette table le jour où le skill y est listé.

Marqueurs ouverts de cette section · `[À VÉRIFIER]` (cadence et déclenchement du re-scan) · `[À COMPLÉTER]` (la ligne 1.0.0, après la première étiquette poussée).
