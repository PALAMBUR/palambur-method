# Méthode Palambur · skill `palambur-method`

[![Security: A · Skills Directory](https://www.skillsdirectory.com/api/skills/palambur-palambur-method/badge)](https://www.skillsdirectory.com/skills/palambur-palambur-method)

**Un skill qui pose les bonnes questions avant d’écrire.** Vous demandez un document de travail à une IA (offre d’emploi, devis, relance, contrat, note interne). Au lieu de deviner ce qui manque et d’inventer le reste, le skill vous pose quatre questions courtes, puis rend un document que vous pouvez envoyer. Pensé pour les entreprises de Suisse romande, utilisable partout. Gratuit, licence MIT.

🇬🇧 [English version below](#english)

---

## Avant / après, en 30 secondes

**Ce que vous écrivez :**

> méthode palambur : fais une offre d’emploi pour un peintre à 80 %

**Ce que le skill répond** (une question par message, avec un compteur, des choix lettrés et un défaut prudent) :

> **Question 1 sur 4 · le canton**
>
> Dans quel canton se trouve le poste ?
>
> A. Vaud
> B. Genève
> C. Suisse romande, sans préciser · défaut si vous ne précisez pas
> D. Autre / je ne sais pas

Puis, sur le même modèle :

> **Question 2 sur 4 · les missions** · A. peinture intérieure et rénovation · B. façades et travaux extérieurs · C. les deux · D. Autre / je ne sais pas

> **Question 3 sur 4 · le profil** · A. CFC de peintre en bâtiment, 3 ans d’expérience · B. CFC exigé, débutant accepté · C. expérience sans CFC acceptée · D. Autre / je ne sais pas

> **Question 4 sur 4 · les avantages** · A. 13e salaire · B. 13e salaire et formation continue · C. aucun en particulier · D. Autre / je ne sais pas

Vous répondez par une lettre ou en texte libre. Si vous passez, le défaut s’applique ; si vous choisissez « je ne sais pas », le champ reste `[À COMPLÉTER]` dans le document.

**Ce que vous recevez**, en deux parties. D’abord le **Gabarit Palambur rempli**, le prompt réutilisable (extrait) :

```
INSTRUCTION
Rédigez une offre d’emploi pour un poste de peintre en bâtiment à 80 %, afin
d’attirer des candidatures qualifiées dans le canton de Vaud.

RÔLE ET AUDIENCE
Vous êtes chargé de recrutement dans une entreprise de Suisse romande, formé au
CO, à la LEg et à la nLPD. Vous écrivez pour des candidats du bâtiment.

DONNÉES
Taux 80 % · canton de Vaud · peinture intérieure et rénovation · CFC de peintre
en bâtiment, 3 ans d’expérience · 13e salaire et formation continue
Date d’entrée : [À COMPLÉTER] · Type de contrat : [À COMPLÉTER]

CONTRAINTES
Formulation neutre de genre (h/f/d). Aucun critère d’âge, d’origine ou d’état
civil. Si une information manque, écrivez [À COMPLÉTER], jamais une valeur
plausible.

FORMAT
Titre, accroche, missions, profil, avantages, modalités de candidature,
mention nLPD. 250 à 350 mots.
```

Puis le **livrable final** (extrait) :

> **Peintre en bâtiment CFC (h/f/d) · 80 % · canton de Vaud**
>
> Vous aimez le travail soigné et les chantiers de rénovation ? Notre entreprise [À COMPLÉTER] cherche un·e peintre en bâtiment à 80 %, entrée en fonction le [À COMPLÉTER].
>
> **Vos missions** · préparation des supports, peinture intérieure, rénovation d’appartements et de bureaux, finitions soignées, conseil aux clients sur place.
>
> **Votre profil** · CFC de peintre en bâtiment, trois ans d’expérience au minimum, autonomie et sens du détail.
>
> **Ce que nous offrons** · 13e salaire, formation continue prise en charge, équipe stable.
>
> *Vos données sont traitées en Suisse, conformément à la nLPD.*

Ce qui n’a pas été dit n’a pas été inventé : il reste marqué `[À COMPLÉTER]`. Si votre demande contient des noms de clients ou des montants, le skill demande d’abord s’il doit les anonymiser (c’est le réglage par défaut).

---

## Ce que c’est

**Deux noms, deux objets.** *La Méthode Palambur* est l’ensemble : la discipline de clarification, les garde-fous suisses, l’anti-hallucination. *Le Gabarit Palambur* en est l’outil : les **5 blocs** ordonnés d’un prompt, Instruction · Rôle et audience · Données · Contraintes · Format, plus 4 blocs d’extension pour les livrables à fort enjeu (contrat, charte, politique interne).

Le skill transforme une demande métier **sous-spécifiée** en **livrable de qualité**, en comblant le contexte manquant *avant* de produire. Il anticipe en interne un lot d’environ quatre questions déterminantes (canton, missions, profil, avantages…), mais n’en pose **qu’une par message**, avec un compteur (« Question 1 sur 4 »), un défaut prudent signalé et une échappatoire « autre / je ne sais pas ». Puis il livre :

1. le **Gabarit Palambur rempli**, prêt à copier-coller et à réutiliser ;
2. le **livrable final** rédigé, avec les garde-fous suisses (LEg, nLPD, CO/LTr, souveraineté des données).

**Trois promesses.**

- **Fluide** · peu de questions, bien ciblées, quatre par lot au plus. Si tout est déjà fourni, il produit directement.
- **Sûr** · protection des données par défaut (anonymisation, mention nLPD), aucune donnée inventée, aucun numéro d’article de loi écrit sans la marque `[À VÉRIFIER]`.
- **Silencieux** · ce skill n’envoie rien, nulle part. Pas de télémétrie, pas de serveur Palambur, pas de compte. Ce sont des fichiers texte que votre IA lit.

**Et un mode relecture.** Vous joignez un texte déjà écrit (une lettre de licenciement, un devis) et demandez de le relire : aucune question, un tableau « Constat · Risque · Correction proposée », puis la version corrigée. La relecture corrige la forme, le droit et les données ; elle ne réécrit pas le fond.

### Déclenchement · trois portes

Une seule suffit.

1. **Le mot** · votre message contient **« palambur »**, **« méthode palambur »** ou **« palambur method »**.
2. **La nature de la demande** · un document de travail demandé en une ou deux phrases (offre d’emploi, devis, relance, contrat, note interne…), un contexte d’entreprise suisse, des noms ou des montants à protéger, ou un texte joint à relire.
3. **L’option « toujours actif »** · écrivez **« Méthode Palambur toujours active »** dans la conversation ou dans votre `CLAUDE.md`, et le skill s’applique à tout ce que l’IA rédige, jusqu’à « Méthode Palambur désactivée ».

Une fois déclenché : s’il manque des éléments déterminants, il clarifie ; si tout est fourni, il produit directement.

Les fichiers du skill sont écrits en français. Les questions et le livrable suivent la langue de votre demande.

---

## Installation

### Claude Code (plugin)

Dans Claude Code, ajouter ce dépôt comme marketplace :

```
/plugin marketplace add PALAMBUR/palambur-method
```

Puis installer le plugin :

```
/plugin install palambur@palambur
```

Ou copier le dossier `skills/palambur-method/` dans `~/.claude/skills/`. Le script `outils/installer_local.sh` le fait pour vous (à blanc par défaut, `--ecrire` pour poser).

### Codex, Cursor, Copilot, Gemini, Mistral, ChatGPT, Infomaniak

Le format `SKILL.md` est un **standard ouvert**. Un seul lien symbolique du dossier `skills/palambur-method/` dans `~/.agents/skills/` suffit à cinq hôtes : **Codex** (OpenAI, qui suit les liens symboliques et lit aussi `.agents/skills/` dans un projet), **Cursor**, **GitHub Copilot**, **Gemini CLI** et **Mistral Vibe CLI** (documentation officielle de chaque éditeur, relevée le 11.10.2026). Gemini (application) et Mistral Vibe Work acceptent le skill par téléversement ; ChatGPT déploie des skills natifs selon l’abonnement. Pour les hôtes qui n’offrent qu’une boîte d’instructions (Projet Claude.ai, Euria d’Infomaniak), le dossier [`adaptations/`](adaptations/) fournit la méthode condensée en **un prompt système autonome**, en deux tailles, généré depuis le skill lui-même.

Le guide pas à pas, hôte par hôte, avec ses sources, est dans [`portabilite/INSTALLATION.md`](portabilite/INSTALLATION.md).

---

## Structure du dépôt

```
palambur-method/
├── .claude-plugin/
│   ├── plugin.json              # le plugin Claude Code (nom, version, mots-clés)
│   └── marketplace.json         # la marketplace qui le sert
├── skills/
│   └── palambur-method/
│       ├── SKILL.md             # quand se déclencher + le déroulé (Étapes 0 à 4)
│       ├── methode-palambur.md  # le Gabarit (5 + 4 blocs), les 4 niveaux, champs DONNÉES, ton
│       ├── protection-donnees.md  # anonymisation, marqueurs, mentions nLPD, outils souverains
│       ├── relecture.md         # le mode relecture (Étape 4) : six cribles, tableau de sortie
│       ├── references-juridiques.md # les textes que le skill peut nommer, ce qu’il n’invente jamais
│       ├── gabarits/            # un fichier de référence par livrable fréquent
│       └── metiers/             # un fichier par métier (tâches, lois, vocabulaire, pièges)
├── adaptations/                 # les prompts à coller (Projet Claude.ai, Euria, GPT) · générés
├── portabilite/                 # installer le skill hôte par hôte · veille des plateformes
├── epreuves/                    # vingt cas, la grille de notation, mesurer.py
├── evals/                       # les mêmes vingt cas au format « claude plugin eval »
├── diffusion/                   # ce qui sert à faire connaître le skill (hors du skill)
├── outils/                      # générateur d’adaptations, chaîne de contrôle, règle typographique, installation locale
├── CHANGELOG.md                 # le journal des versions
├── CONTRIBUTING.md              # comment proposer un gabarit ou une correction
├── LICENSE                      # MIT
└── README.md
```

Les dossiers `gabarits/`, `metiers/`, `portabilite/` et `diffusion/` se remplissent au fil des versions ; le [journal des versions](CHANGELOG.md) dit ce qui est posé et ce qui est en préparation.

### Vérifier avant de publier

La chaîne de contrôle (règle typographique à jour, typographie, zéro « PME », JSON, version, adaptations, frontmatter, taille, liens) :

```bash
python3 outils/controle.py
```

Le contrôle se casse lui-même sur des témoins fabriqués, pour prouver qu’il regarde :

```bash
python3 outils/controle.py --epreuve
```

`controle.py` tourne **sur n’importe quel clone** : la règle typographique qu’il applique est embarquée dans `outils/regle_typo.py`, copie datée d’une règle qui fait foi dans l’atelier Palambur, hors de ce dépôt. Quand l’atelier est à côté, le contrôle `regle` compare les deux et refuse une copie en retard ; ailleurs, il le dit en une ligne et ne rougit pas. Le reste de la chaîne de l’atelier (registre des invites, corpus Chaptal) suppose l’atelier et n’est pas dans ce dépôt.

Les **épreuves du skill** lui-même (est-il fluide, est-il sûr ?) sont dans [`epreuves/`](epreuves/) : vingt demandes, une grille de notation, `mesurer.py`. Le dossier [`evals/`](evals/) porte les mêmes vingt cas au format `claude plugin eval`. Au 11.10.2026, **les 20 cas n’ont pas encore été joués** : les jouer dépense des appels au modèle, et cette dépense n’a pas été autorisée.

---

## Engagements

- **Le skill de base est gratuit et le restera.** Licence MIT : vous pouvez l’utiliser, le copier, le modifier, y compris dans un cadre commercial.
- **Il n’envoie rien, nulle part.** Aucune télémétrie, aucun appel réseau, aucun compte. Vos demandes restent entre vous et l’IA que vous avez choisie.
- **Pas de publicité dans le skill.** Les livrables ne portent aucune mention Palambur. Ce qui suit est la seule exception, et elle est ici, pas dans le skill.

Le skill est la porte, [Chaptal](https://palambur.ch) la maison : 782 pistes métier au Gabarit Palambur, prêtes à l’emploi, sur palambur.ch (relevé du 11.10.2026).

## Licence

[MIT](LICENSE) · Palambur · Victor Semblanet · 2026

---
---

<a id="english"></a>

# Palambur Method · the `palambur-method` skill

**A skill that asks the right questions before it writes.** You ask an AI for a working document (a job advert, a quote, a payment reminder, a contract, an internal memo). Instead of guessing what is missing and making up the rest, the skill asks you four short questions, then delivers a document you can actually send. Designed for businesses in French-speaking Switzerland, usable anywhere. Free, MIT licence.

---

## Before and after, in 30 seconds

**What you type:**

> palambur method: write a job advert for a painter at 80%

**What the skill replies** (one question per message, with a counter, lettered choices and a cautious default):

> **Question 1 of 4 · the canton**
>
> Which canton is the position in?
>
> A. Vaud
> B. Geneva
> C. French-speaking Switzerland, unspecified · default if you don’t say
> D. Other / I don’t know

Then, on the same model:

> **Question 2 of 4 · the duties** · A. interior painting and renovation · B. façades and exterior work · C. both · D. Other / I don’t know

> **Question 3 of 4 · the profile** · A. Swiss federal certificate (CFC) in painting, 3 years’ experience · B. CFC required, beginners welcome · C. experience without a CFC accepted · D. Other / I don’t know

> **Question 4 of 4 · the benefits** · A. 13th month’s salary · B. 13th month and continuing education · C. none in particular · D. Other / I don’t know

You answer with a letter or in free text. If you skip, the default applies; if you choose “I don’t know”, the field stays `[TO BE COMPLETED]` in the document.

**What you receive**, in two parts. First, the **completed Palambur Template**, the reusable prompt (excerpt):

```
INSTRUCTION
Write a job advert for a building painter position at 80%, to attract
qualified applicants in the canton of Vaud.

ROLE AND AUDIENCE
You are a recruiter in a company in French-speaking Switzerland, trained in
the Swiss Code of Obligations, the Gender Equality Act and the Data Protection
Act. You write for applicants from the building trades.

DATA
80% · canton of Vaud · interior painting and renovation · CFC in painting,
3 years’ experience · 13th month and continuing education
Start date: [TO BE COMPLETED] · Contract type: [TO BE COMPLETED]

CONSTRAINTS
Gender-neutral wording. No criteria of age, origin or marital status. If a
piece of information is missing, write [TO BE COMPLETED], never a plausible
value.

FORMAT
Title, hook, duties, profile, benefits, how to apply, data protection notice.
250 to 350 words.
```

Then the **final deliverable** (excerpt):

> **Building painter, CFC (m/f/d) · 80% · canton of Vaud**
>
> Do you take pride in careful work and renovation projects? Our company [TO BE COMPLETED] is looking for a building painter at 80%, starting on [TO BE COMPLETED].
>
> **Your duties** · surface preparation, interior painting, renovation of flats and offices, careful finishing, on-site advice to clients.
>
> **Your profile** · CFC in painting, at least three years’ experience, autonomy and an eye for detail.
>
> **What we offer** · 13th month’s salary, continuing education paid for, a stable team.
>
> *Your data is processed in Switzerland, in accordance with the Swiss Data Protection Act.*

Whatever was not said has not been invented: it stays marked `[TO BE COMPLETED]`. If your request contains client names or amounts, the skill first asks whether it should anonymise them (anonymising is the default).

---

## What it is

**Two names, two objects.** *The Palambur Method* is the whole: the discipline of clarifying first, the Swiss legal guardrails, the refusal to invent. *The Palambur Template* is its tool: the **5 ordered blocks** of a prompt, Instruction · Role and audience · Data · Constraints · Format, plus 4 extension blocks for high-stakes deliverables (contracts, charters, internal policies).

The skill turns an **under-specified** business request into a **quality deliverable** by filling the missing context *before* producing anything. Internally it anticipates a batch of about four decisive questions (canton, duties, profile, benefits…), but asks **only one per message**, with a counter (“Question 1 of 4”), a cautious default and an escape hatch (“other / I don’t know”). Then it delivers:

1. the **completed Palambur Template**, ready to copy, paste and reuse;
2. the **final deliverable**, written with the Swiss guardrails (Gender Equality Act, Data Protection Act, Code of Obligations and Labour Act, data sovereignty).

**Three commitments.**

- **Smooth** · few questions, well targeted, four per batch at most. If everything is already provided, it produces straight away.
- **Safe** · data protection by default (anonymisation, data protection notice), no invented data, no legal article number written without a `[TO BE VERIFIED]` marker.
- **Silent** · this skill sends nothing, anywhere. No telemetry, no Palambur server, no account. It is plain text files that your AI reads.

**And a review mode.** You attach a text you have already written (a dismissal letter, a quote) and ask for a review: no questions, a table “Finding · Risk · Proposed correction”, then the corrected version. The review fixes form, law and data; it does not rewrite the substance.

### Triggering · three doors

One is enough.

1. **The word** · your message contains **“palambur”**, **“méthode palambur”** or **“palambur method”**.
2. **The nature of the request** · a working document asked for in one or two sentences (job advert, quote, reminder, contract, internal memo…), a Swiss business context, names or amounts to protect, or a text attached for review.
3. **The “always on” option** · write **“Méthode Palambur toujours active”** in the conversation or in your `CLAUDE.md`, and the skill applies to everything the AI writes, until “Méthode Palambur désactivée”.

Once triggered: if decisive elements are missing, it clarifies; if everything is provided, it produces directly.

The skill’s own files are written in French. The questions and the deliverable follow the language of your request.

---

## Installation

### Claude Code (plugin)

In Claude Code, add this repository as a marketplace:

```
/plugin marketplace add PALAMBUR/palambur-method
```

Then install the plugin:

```
/plugin install palambur@palambur
```

Or copy the `skills/palambur-method/` folder into `~/.claude/skills/`. The script `outils/installer_local.sh` does it for you (dry run by default, `--ecrire` to write).

### Codex, Cursor, Copilot, Gemini, Mistral, ChatGPT, Infomaniak

The `SKILL.md` format is an **open standard**. A single symbolic link from `skills/palambur-method/` into `~/.agents/skills/` serves five hosts: **Codex** (OpenAI, which follows symbolic links and also reads `.agents/skills/` inside a project), **Cursor**, **GitHub Copilot**, **Gemini CLI** and **Mistral Vibe CLI** (each vendor’s official documentation, read on 11.10.2026). The Gemini app and Mistral Vibe Work accept the skill by upload; ChatGPT is rolling out native skills depending on the subscription. For hosts that only offer an instructions box (a Claude.ai Project, Infomaniak’s Euria), the [`adaptations/`](adaptations/) folder provides the method condensed into **a standalone system prompt**, in two sizes, generated from the skill itself.

The step-by-step guide, host by host, with its sources, is in [`portabilite/INSTALLATION.md`](portabilite/INSTALLATION.md) (in French).

---

## Repository layout

See the tree in the French section above. In short: `skills/palambur-method/` is the skill (with `gabarits/` for deliverable templates and `metiers/` for trades), `adaptations/` holds the generated prompts for other AIs, `portabilite/` the installation guides, `epreuves/` twenty test cases with their marking grid (and `evals/` the same cases in `claude plugin eval` format; as of 11.10.2026 none has been run yet, since that would spend model calls that were not authorised), `outils/` the adaptation generator, the control chain, the embedded typography rule and the local installer. `CHANGELOG.md` says what is in place and what is still in preparation.

### Checking before publishing

The control chain (typography rule up to date, typography, no forbidden words, JSON, version, adaptations, frontmatter, size, links):

```bash
python3 outils/controle.py
```

The control breaks itself on fabricated witnesses, to prove it is looking:

```bash
python3 outils/controle.py --epreuve
```

`controle.py` runs **on any clone**: the typography rule it applies is embedded in `outils/regle_typo.py`, a dated copy of a rule whose source lives in the Palambur workshop, outside this repository. When the workshop sits next to the clone, the `regle` control compares both and refuses an outdated copy; elsewhere it says so in one line and stays green. The rest of the workshop chain (prompt registry, Chaptal corpus) assumes the workshop and is not in this repository.

---

## Commitments

- **The base skill is free and will stay free.** MIT licence: you may use, copy and modify it, including commercially.
- **It sends nothing, anywhere.** No telemetry, no network calls, no account. Your requests stay between you and the AI you chose.
- **No advertising inside the skill.** Deliverables carry no Palambur mention. What follows is the only exception, and it lives here, not in the skill.

The skill is the door, [Chaptal](https://palambur.ch) is the house: 782 ready-to-use prompts per trade, built on the Palambur Template, on palambur.ch (as of 11 October 2026).

## Licence

[MIT](LICENSE) · Palambur · Victor Semblanet · 2026
