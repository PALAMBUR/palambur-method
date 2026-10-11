# A Swiss method to stop AI from inventing your contract

**Draft · 11 October 2026 · not published anywhere.** Target: Dev.to first, then Hacker News (as a link to the Dev.to post or to the repository). British spelling, no punctuation dashes, curly apostrophes, singular they. Word count checked at the end of the file. Markers in square brackets are deliberate and listed at the end; they must disappear before publication.

---

Ask a language model to write a job advert for a painter at 80 % and it will do so in ten seconds. It will also pick a canton, a contract type, a start date, a list of benefits and, quite often, a collective labour agreement. None of these were in your request. All of them will read as plausible. That is the problem: a plausible invention does not look like one when you proofread it.

This is not a bug you can patch. A language model is a prediction engine, as Lee Boonstra puts it in Google’s white paper *Prompt Engineering* (September 2024, p. 6), and a prediction engine does not stop at a gap. It predicts the content of the gap. In a small Swiss company, where the person who writes the contract often signs it too, that is a liability.

We run a small consultancy in Neuchâtel. For a year we watched clients paste half a sentence into a chat window and send out whatever came back. So we wrote down what we did by hand before letting the model write, and turned it into a skill any agent can load: the Palambur Method, on GitHub under MIT licence.

## What it does

The method inverts the usual order: the agent clarifies first, then produces once, instead of producing first and correcting ten times.

Here is the same request, before and after.

**Before**

> fais une offre d’emploi pour un peintre à 80 %

The model answers immediately. Canton, contract, start date, benefits, collective agreement: all chosen by the model, none verified.

**After**

The skill anticipates the four decisions that would otherwise be guessed and asks them one per message, with a counter, so the person knows when it ends:

- *Question 1 of 4* · Which canton is the position based in? A. Neuchâtel · B. Vaud · C. Geneva · D. Other / I do not know (cautious default: French speaking Switzerland, no canton named)
- *Question 2 of 4* · What are the three to five main tasks?
- *Question 3 of 4* · Which profile: certified apprenticeship required, minimum experience, driving licence?
- *Question 4 of 4* · Which benefits can be stated? (default: none stated, rather than one invented)

Then it writes and returns two things: the complete prompt in five blocks, which the person keeps, and the deliverable:

> Painter, certified · 80 % · [Canton] · start date to be agreed
> Profile: certified painter or equivalent · three years in renovation · driving licence [TO BE COMPLETED: required or preferred]
> What we offer: [TO BE COMPLETED: benefits confirmed by the employer, none stated by default]
> Open to all. Your data is processed in Switzerland, in accordance with the Swiss Data Protection Act.

The brackets are the point. What is missing is written as missing, where a reviewer cannot miss it. No collective agreement is cited until it is confirmed. The wording is gender neutral because Swiss equality law applies in the constraints, not at proofreading time.

## The rule that comes before all the others

The example above has no personal data in it. Most real requests do.

> write a reminder for the unpaid invoice of Menuiserie Exemple SA, CHF 4'820, overdue since 15 June

Before any question about tone or deadline, the skill asks one thing, in a single message: it has detected a client name and an amount. By default it anonymises them everywhere (Client X, Amount A) and adds a data protection notice. Does the person want the real names instead?

Silence means anonymise. There is no hybrid: never a real name in the prompt and a pseudonym in the letter. The invoice number and the bank account are not questions either. They are fields, delivered as brackets and filled in by hand, so the model never sees them.

We made this the first gate because in Switzerland exposing client data is a liability for the managing director personally, and because the people most likely to paste a client file into a public chat have the least time to think about it. Protection by default costs one question.

## What it refuses to do

Three refusals are built in.

It never invents a legal reference. Laws are named (Code of Obligations, Labour Act, Equality Act, Data Protection Act). Article numbers are never quoted without a visible *to be verified* marker, because verification belongs to the reviewer, not to the writer.

It never fills a gap with a plausible value. A missing fact becomes a bracket. This sounds trivial. It is the largest quality change we have seen: brackets get read, plausible sentences do not.

It never ends a deliverable with a list of assumptions to validate. That pattern looks like diligence. It is the exact failure the method exists to remove.

## Honest numbers

The repository has two stars at the time of writing, and one of them is ours. One fork. Eighteen page views in fourteen days, three of them unique. The clone count is in the hundreds, almost entirely directory crawlers. We are not going to pretend otherwise. It has been used daily in one consultancy and by a handful of clients since July 2026, never at scale, and the counter promise (four questions, one per message) is only now being measured on a replayable test set.

What we can say is narrower. Clarifying before producing is not ours; every careful professional does it. What is ours is writing it down as a loadable skill, with Swiss legal safeguards and data protection as the default, and publishing it so that anyone can read what the agent does with a request before trusting it with one.

## Install it

The skill follows the open `SKILL.md` convention, so the same files load in several agents.

In Claude Code, two commands, one at a time:

```bash
/plugin marketplace add PALAMBUR/palambur-method
```

```bash
/plugin install palambur@palambur
```

Codex, Cursor, Gemini CLI, GitHub Copilot and Mistral Vibe CLI all read `~/.agents/skills/`, so one symbolic link serves the five. The Gemini app and Mistral Vibe take `SKILL.md` as an upload. A custom GPT, a Claude.ai project or Infomaniak’s Euria, which offer a single instructions box, get the method as a prompt to paste, in a full and a short version. The guide per host is `portabilite/INSTALLATION.md`.

It is free, needs no account with us and sends us nothing: no telemetry, no copy of your requests. What you type stays between you and the model you chose.

Repository: https://github.com/PALAMBUR/palambur-method

## What we would like from you

If you write business documents in another jurisdiction, the most valuable contribution is a template for one deliverable you write often: its data fields, its safeguards, one completed example. Templates are labelled as good first contributions on purpose.

If the skill asks a bad question, invents a value or cites a law it should not, open an issue with the request as you typed it, anonymised. We would rather fix one real failure than add ten features.

And if it asks you something you had not thought about, that is the method working. Tell us what the question was.

---

## Checks to run before publication

- Word count of the article body (between the two horizontal rules): between 800 and 1200 words.
- British spelling: `grep -n "ize\b\|color\|labor\|center"` must return nothing in the body. The French acronym for small businesses must not appear.
- Hosts paragraph: aligned on the table of `portabilite/INSTALLATION.md` (reading of 11 October 2026). Re-read that table on the day of publication; it changes with the platforms.
- Google white paper: Lee Boonstra, *Prompt Engineering*, Google, September 2024, p. 6 and 7 (the same citation as the live page `palambur.ch/methode/`; a copy is held in `0600_RESSOURCES/06.01_IA_Prompting/`). No public link is given in the body: the Kaggle address returned HTTP 404 on 11 October 2026, so a link must be found and checked before publication.
- The star, fork, view and clone figures are the 11 October 2026 reading from `outils/mesure.py` and must be replaced by the reading of the day of publication, or the paragraph rewritten.
- The French brackets in the painter example (`[TO BE COMPLETED]`) are translated for the reader; the skill itself writes `[À COMPLÉTER]`.

**Requires Victor** · the go to publish, the Dev.to account, and whether Hacker News gets the Dev.to link or the repository link.
