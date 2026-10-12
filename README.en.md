# Palambur Method · the `palambur-method` skill

[Français](README.md) · English · [Deutsch](README.de.md) · [Italiano](README.it.md)

[![Control](https://github.com/PALAMBUR/palambur-method/actions/workflows/controle.yml/badge.svg)](https://github.com/PALAMBUR/palambur-method/actions/workflows/controle.yml) [![MIT licence](https://img.shields.io/badge/licence-MIT-blue)](LICENSE) [![Version](https://img.shields.io/github/v/release/PALAMBUR/palambur-method)](https://github.com/PALAMBUR/palambur-method/releases) [![Security: A · Skills Directory](https://www.skillsdirectory.com/api/skills/palambur-palambur-method/badge)](https://www.skillsdirectory.com/skills/palambur-palambur-method)

**A skill that asks the right questions before it writes.** You ask an AI for a working document (a job advert, a quote, a payment reminder, a contract, an internal memo). Instead of guessing what is missing and making up the rest, the skill asks you at most four short questions, one at a time, then delivers a document you can actually send. Designed for businesses in French-speaking Switzerland, usable anywhere. Free, MIT licence.

---

<a id="try"></a>
## Try it in two minutes

**Claude Code** · two commands in the conversation, then one request.

```
/plugin marketplace add PALAMBUR/palambur-method
```

```
/plugin install palambur@palambur
```

Then type: `palambur method: write a job advert for a painter at 80 %`

**In your browser** (Claude.ai, ChatGPT, Infomaniak’s Euria, Mistral…) · open [`adaptations/methode-palambur-prompt.md`](adaptations/methode-palambur-prompt.md), copy **the block below the rule**, paste it into the instructions of your project or assistant. Nothing to install. For an instructions box with a tight size limit, take the [short prompt](adaptations/methode-palambur-prompt-court.md). Both prompts are in French; the questions and the deliverable follow the language of your request.

**Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe** · a single symbolic link from the `skills/palambur-method/` folder into `~/.agents/skills/` serves all five hosts. The commands, host by host, are in [`docs/portabilite/INSTALLATION.md`](docs/portabilite/INSTALLATION.md) (in French).

**Check that the skill is loaded** · in Claude Code, `/plugin` then the **Installed** tab; or, on any host, ask “palambur method: what is your first question?” and expect a reply that starts with “Question 1 of N”.

---

## Contents

- [Try it in two minutes](#try)
- [Before and after, in 30 seconds](#before-after)
- [What it is](#what-it-is)
- [Triggering · three doors](#triggering)
- [Installation](#installation)
- [Repository layout](#layout)
- [Measures and test cases](#measures)
- [Commitments](#commitments)
- [Contributing](#contributing) · [Citing](#citing) · [Licence](#licence)

---

<a id="before-after"></a>
## Before and after, in 30 seconds

![The four questions, then the Template and the Deliverable](docs/demo-quatre-questions.svg)

**What you type:**

> palambur method: write a job advert for a painter at 80 %

**What the skill replies.** On its first trigger, three opening lines, the sensitivity level, then the first question, all in the same message:

> **Palambur Method.** I will first ask you a few questions, one at a time, so that I invent nothing on your behalf.
> You answer with a letter or in free text; if you skip, a cautious default applies and stays visible.
> You will then receive two blocks to copy: the reusable **Palambur Template**, then the **Deliverable**.
>
> Sensitivity level · ordinary (no name, no amount)
>
> **Question 1 of 4 · the place and the setting**
>
> Where is the position, and in what setting?
>
> A. a single workplace, canton to be named
> B. several sites or regular travel
> C. partial remote work possible, share to be specified
> D. Other / I don’t know · default if you don’t say

Then, **one question per message**, always with a counter, lettered choices, a flagged cautious default and an escape hatch:

> **Question 2 of 4 · the duties** · A. I will provide them · B. propose the usual duties of the trade, I will correct · default if you don’t say · C. the position is new, the duties are not settled yet · D. Other / I don’t know

> **Question 3 of 4 · the profile** · A. a required qualification (CFC, federal diploma, master craftsman) · B. CFC or recognised equivalent experience · default if you don’t say · C. no qualification required, in-house training provided · D. Other / I don’t know

> **Question 4 of 4 · what the company offers** · A. nothing beyond the contractual and collective framework · default if you don’t say · B. benefits to be named · C. benefits to be named and a published gross salary range · D. Other / I don’t know

Answers kept for the example: A (canton of Vaud, workshop in Yverdon-les-Bains), B, A (Swiss federal certificate, CFC, in building painting), B (13th month’s salary and continuing education). If you choose “I don’t know”, the field stays `[TO BE COMPLETED]` in the document.

**What you receive.** First **one line of context**, stating what was kept:

> Context kept · job advert · building painter at 80 % · canton of Vaud · factual tone · data: none · 4 answers, 0 defaults, 10 markers

Then the **completed Palambur Template**, the reusable prompt (excerpt):

```
Palambur Template

INSTRUCTION
Write a complete job advert for a building painter position at 80 %, to be
published on [TO BE COMPLETED: channels]. Goal: attract qualified applicants
by stating the real work, the place, the hours and the setting, without
promising anything the management has not validated.

ROLE AND AUDIENCE
You are the recruiter at Exemple SA, a building painting company in the
canton of Vaud, trained in the Code of Obligations, the Gender Equality Act,
the Labour Act and the Data Protection Act. You write for a tradesperson who
reads the advert on a phone.

DATA
• Job title: building painter (m/f/d)
• Workplace and canton: workshop in Yverdon-les-Bains, sites across the
  canton of Vaud
• Rate · contract type · start date: 80 % · open-ended · to be agreed
• Required profile: CFC in building painting
• Benefits validated by management: 13th month · continuing education
• Applicable collective labour agreement, if known: [TO BE COMPLETED]

CONSTRAINTS
No discriminatory criterion (Gender Equality Act, Code of Obligations),
gender-neutral wording (m/f/d). No invented salary, no invented holiday
entitlement. No legal article quoted: if a collective agreement applies,
name it and write [TO BE VERIFIED: applicable agreement].

FORMAT
Six sections: title and hook · the company · your duties · your profile ·
what we offer · how to apply. 400 to 600 words. Formal address, French of
French-speaking Switzerland. Data processing notice at the end of the advert.
```

Then the **Deliverable** (excerpt):

> **Building painter, CFC (m/f/d) · 80 % · Yverdon-les-Bains**
>
> Do you take pride in careful work and renovation projects? Exemple SA is looking for a building painter at 80 %, start date to be agreed.
>
> **Your duties** [TO BE VALIDATED: proposed list, to be corrected by management] · surface preparation, interior painting of flats and offices, wall coverings, finishing, on-site advice to clients.
>
> **Your profile** · required: CFC in building painting · desirable: [TO BE COMPLETED: years of experience], driving licence [TO BE COMPLETED: category].
>
> **What we offer** · 13th month’s salary · continuing education paid for.
>
> **How to apply** · send your file to [TO BE COMPLETED: recipient’s function] via [TO BE COMPLETED: channel].
>
> *Your application data is processed by Exemple SA using [TO BE COMPLETED: tool], hosted in [TO BE COMPLETED: country], and kept for [TO BE COMPLETED: duration].*

And, to close, the **Trust log**, five lines stating what was protected, marked and refused:

```
Trust log
· Sensitivity level · ordinary (no person named)
· Data · none
· Markers placed · [TO BE COMPLETED] ×7 · [TO BE VERIFIED] ×2 (applicable agreement, job posting notice) · [TO BE VALIDATED] ×1 (duties)
· Refused assumptions · no salary figure; no collective agreement named from memory; no data hosting location asserted
· Human review · required before publication (HR deliverable)
```

Whatever was not said has not been invented: it stays marked. If your request contains **client names or amounts**, the skill first asks, in one question on its own, whether it should anonymise them (anonymising is the default). The full exchange is in [`docs/exemples/01-offre-emploi.md`](docs/exemples/01-offre-emploi.md); nine other walkthroughs, one per template, are in [`docs/exemples/`](docs/exemples/) (in French).

---

<a id="what-it-is"></a>
## What it is

**Two names, two objects.** *The Palambur Method* is the whole: the discipline of clarifying first, the Swiss legal guardrails, the refusal to invent. *The Palambur Template* is its tool: the **5 ordered blocks** of a prompt, Instruction · Role and audience · Data · Constraints · Format, plus 4 extension blocks for high-stakes deliverables (contracts, charters, internal policies).

The skill turns an **under-specified** business request into a **quality deliverable** by filling the missing context *before* producing anything. Internally it anticipates a batch of at most four decisive questions (place and setting, duties, profile, benefits…), but asks **only one per message**, with a counter (“Question 1 of 4”), a flagged cautious default and an escape hatch (“Other / I don’t know”). Then it delivers:

1. the **completed Palambur Template**, ready to copy, paste and reuse;
2. the written **Deliverable**, with the Swiss guardrails (Gender Equality Act, Data Protection Act, Code of Obligations, Labour Act, data sovereignty), closed by a Trust log.

**Three commitments.**

- **Smooth** · few questions, well targeted, four per batch at most. If everything is already provided, it produces straight away.
- **Safe** · data protection by default (anonymisation, data protection notice), no invented data, no legal article number written without a `[TO BE VERIFIED]` marker.
- **Silent** · this skill sends nothing, anywhere. No telemetry, no Palambur server, no account. It is plain text files that your AI reads.

**A company profile, so you never answer twice.** The skill reads a `profil-entreprise.md` file placed at the **root of your working folder**: canton, collective agreement, tone, signature, language. Its completed fields count as answers, and the questions it settles are no longer asked. The model to copy is in the skill: [`skills/palambur-method/profil-entreprise.md`](skills/palambur-method/profil-entreprise.md).

**And a review mode.** You attach a text you have already written (a dismissal letter, a quote) and ask for a review: no questions, a table “Finding · Risk · Proposed correction”, then the corrected version. The review fixes form, law and data; it does not rewrite the substance ([`relecture.md`](skills/palambur-method/relecture.md)).

<a id="triggering"></a>
## Triggering · three doors

One is enough.

1. **The word** · your message contains **“palambur”**, **“méthode palambur”** or **“palambur method”**.
2. **The nature of the request** · a working document asked for in one or two sentences (job advert, quote, reminder, contract, internal memo…), a Swiss business context, names or amounts to protect, or a text attached for review.
3. **The “always on” option** · write **“Méthode Palambur toujours active”** in the conversation or in your `CLAUDE.md`, and the skill applies to everything the AI writes, until “Méthode Palambur désactivée”.

Once triggered: if decisive elements are missing, it **clarifies**; if everything is provided, it produces directly; if a text is attached for review, it reviews without asking anything.

The skill’s own files are written in **French**. The questions and the deliverable follow the language of your request.

---

<a id="installation"></a>
## Installation

### Prerequisites

- **To use the skill** · a host that reads the `SKILL.md` format (an up-to-date Claude Code, Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe) or any AI with an instructions box. Nothing else.
- **For the repository tools** (control chain, test cases, generators) · Python 3.9 or newer. Optional: you do not need it to use the skill.

### Claude Code · plugin

In Claude Code, add this repository as a marketplace:

```
/plugin marketplace add PALAMBUR/palambur-method
```

Then install the plugin:

```
/plugin install palambur@palambur
```

Updates arrive with each **new version** of the plugin; `/plugin` then **Installed** shows the one you have.

### Local copy · `outils/installer_local.sh`

If you prefer a copy in `~/.claude/skills/` without the marketplace, clone the repository and run the script. Dry run by default, it shows what it would do:

```bash
bash outils/installer_local.sh
```

With `--ecrire`, it actually writes the copy:

```bash
bash outils/installer_local.sh --ecrire
```

The script **refuses** if the target is already a symbolic link, so as not to write into another clone through the link.

### Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe · `.agents/skills`

The `SKILL.md` format is an **open standard**. A single symbolic link from `skills/palambur-method/` into `~/.agents/skills/` serves five hosts: **Codex** (which follows symbolic links and also reads `.agents/skills/` inside a project), **Cursor**, **GitHub Copilot**, **Gemini CLI** and **Mistral Vibe CLI** (each vendor’s official documentation, read on 11.10.2026). The Gemini app and Mistral Vibe Work accept the skill by upload. The step-by-step guide, host by host, with its dated sources, is in [`docs/portabilite/INSTALLATION.md`](docs/portabilite/INSTALLATION.md); the skill’s conformity to the standard is recorded in [`docs/portabilite/CONFORMITE_STANDARD.md`](docs/portabilite/CONFORMITE_STANDARD.md) (both in French).

### Instructions boxes · Claude.ai Project, Euria, other assistants

For hosts that only offer a **system instructions box**, the [`adaptations/`](adaptations/) folder provides the method condensed into a standalone prompt, **generated from the skill itself** at each version: a [full version](adaptations/methode-palambur-prompt.md) under 8'000 characters and a [short version](adaptations/methode-palambur-prompt-court.md) under 1'500 characters. On these hosts the assistant *is* the method: it applies to every request, with no trigger word. The table “which host, which version, where to paste” is in [`adaptations/README.md`](adaptations/README.md).

**One truth, the repository.** The skill has a single source: `skills/palambur-method/` in this repository. What the hosts read (`~/.claude/skills/`, `~/.agents/skills/`, an installed plugin, a pasted prompt) is **a link or a dated copy**, updated with `git pull` or a new plugin version, **never by editing the files in place**: a fix made in a copy is lost at the next update, and nobody reviews it.

---

<a id="layout"></a>
## Repository layout

```
palambur-method/
├── README.md · README.en.md · README.de.md · README.it.md   # this file, in four languages
├── CHANGELOG.md · CONTRIBUTING.md · CODE_OF_CONDUCT.md      # versions, contributions, conduct
├── SECURITY.md · CITATION.cff · LICENSE                     # reporting, citation, MIT
├── .claude-plugin/          # plugin.json and marketplace.json · the Claude Code plugin
├── .github/                 # issue templates, PR template, workflows/controle.yml (CI)
├── .agents/skills/palambur-method/   # Codex and .agents hosts location · a README, the link is made on your side
├── skills/palambur-method/  # THE SKILL · the single source
│   ├── SKILL.md             # when to trigger, steps 0 to 4, the shape of the questions
│   ├── methode-palambur.md  # the Template (5 + 4 blocks), the 4 levels, the tone, three walkthroughs
│   ├── protection-donnees.md   # sensitivity levels, anonymisation, trust log
│   ├── relecture.md         # the review mode · six screens, output table
│   ├── references-juridiques.md   # the legal texts the skill may name, what it never invents
│   ├── profil-entreprise.md # the company profile model read at the root of the working folder
│   ├── gabarits/            # one file per frequent deliverable (questions, DATA fields, pitfalls)
│   ├── metiers/             # one file per trade (vocabulary, named legal texts, pitfalls)
│   └── agents/openai.yaml   # optional metadata read by Codex
├── adaptations/             # the generated system prompts · full (under 8'000 characters) and short
├── docs/
│   ├── exemples/            # ten complete walkthroughs, one per template, fictional data
│   ├── pedagogie/           # MANIFESTE.md, FAQ.md, GLOSSAIRE.md
│   ├── portabilite/         # INSTALLATION.md (host by host), CONFORMITE_STANDARD.md
│   ├── VEILLE_JURIDIQUE.md  # what feeds the table of legal references
│   └── DIX_COMMANDEMENTS.md # data protection in ten lines
├── epreuves/                # 149 cases (cas.json), grille.md, mesurer.py, generer_evals.py,
│                            # jouer_apertus.py, results and protocol, reponses/ (transcripts)
├── evals/                   # README only · the “claude plugin eval” cases are regenerated
└── outils/                  # controle.py, generer_adaptations.py, installer_local.sh, regle_typo.py, metiers/
```

The `gabarits/` and `metiers/` folders grow with each version; the [changelog](CHANGELOG.md) says what is in place, with a quality note per version. The [ten commandments](docs/DIX_COMMANDEMENTS.md) hold data protection on one page; the [FAQ](docs/pedagogie/FAQ.md), the [manifesto](docs/pedagogie/MANIFESTE.md) and the [glossary](docs/pedagogie/GLOSSAIRE.md) answer the recurring questions. The documentation outside this README is in French; the [German](README.de.md) and [Italian](README.it.md) READMEs await a **native review**.

---

<a id="measures"></a>
## Measures and test cases

**The control chain** checks the repository before every publication: typography rule, forbidden word, valid JSON, a single version number across three files, adaptations up to date with their sources, `SKILL.md` frontmatter and size, relative links. It runs on any clone and in the CI (`.github/workflows/controle.yml`), with no secret and no model call:

```bash
python3 outils/controle.py
```

The control **breaks itself** on fabricated witnesses, to prove it is looking:

```bash
python3 outils/controle.py --epreuve
```

**The skill’s test cases** (is it smooth, is it safe?) are in [`epreuves/`](epreuves/): **149 cases** in three families (deliverables, trade tasks, traps that push the model to invent · as of 11.10.2026, `python3 epreuves/mesurer.py --compter` is authoritative), a [marking grid](epreuves/grille.md) with twenty guards, and `mesurer.py`, which marks a reply against the grid and can break itself too (`--epreuve`). The same cases in `claude plugin eval` format are **regenerated** from `epreuves/cas.json` with `python3 epreuves/generer_evals.py`; they are no longer versioned, and [`evals/README.md`](evals/README.md) says how to run them.

**The published measure.** Measured on 12.10.2026 on Apertus (Infomaniak) with the **full adaptation prompt**, not the native skill: **1 green out of 149**. The model asks the anonymisation question, then delivers the Template and the deliverable in the same message, without clarifying and without markers. Details, red guards per family and exact spend are in [`epreuves/RESULTATS_APERTUS_2026-10-11.md`](epreuves/RESULTATS_APERTUS_2026-10-11.md) (in French). **The native skill on Claude has not been measured yet**; the [changelog](CHANGELOG.md) will carry its quality note the day it has been.

---

<a id="commitments"></a>
## Commitments

- **The base skill is free and will stay free.** MIT licence: you may use, copy and modify it, including commercially. **The base skill is this whole repository**: the method, the templates, the trade files, the test cases, and every version to come. Palambur sells **service around it** (a version pre-configured for one company, an assisted installation); nothing that is here becomes paid.
- **It sends nothing, anywhere.** No telemetry, no network calls, no account. Your requests stay between you and the AI you chose.
- **No advertising inside the skill.** Deliverables carry no Palambur mention. The skill names **one single Palambur tool, Jomini** (free anonymisation in the browser, no account), because it serves data protection; that is the only mention. What follows is the other exception, and it lives here, not in the skill.

The skill is the door, [Chaptal](https://palambur.ch) is the house: **782 ready-to-use prompts per trade**, built on the Palambur Template, on palambur.ch (as of 11.10.2026).

---

<a id="contributing"></a>
## Contributing

A missing template, a legal correction, a new language: [`CONTRIBUTING.md`](CONTRIBUTING.md) says how to propose one, what the control chain requires and the **native speaker rule** for translations. The [code of conduct](CODE_OF_CONDUCT.md) applies to every exchange; a vulnerability, or a behaviour of the skill that exposes data, is reported as described in [`SECURITY.md`](SECURITY.md), not in a public issue.

<a id="citing"></a>
## Citing

To cite the Palambur Method in a paper, a course or an article, the **citation metadata** is in [`CITATION.cff`](CITATION.cff); GitHub offers its APA and BibTeX forms from the repository page.

<a id="licence"></a>
## Licence

[MIT](LICENSE) · Palambur · Victor Semblanet · 2026
