# Communautés Claude et Codex · annonces de version en anglais (point 72)

**Brouillon · rien n’est envoyé · go Victor.** Prepared on 11 October 2026. Nothing has been posted anywhere. Each text below is written for one community, after reading that community’s own rules **on the day** (URL and verbatim quotes given). Where the rules could not be read with our tools, the file says so and the text is **conditional**: Victor reads the rules while logged in, then decides. British spelling, singular they, no punctuation dashes, curly apostrophes. The French acronym for small businesses and its English equivalent never appear.

**When to post** : only once the `v1.0.0` tag and release are public on GitHub (go Victor). An announcement for a version that is not yet online is a broken promise.

## What was read on 11 October 2026, place by place

| Place | What was read | What it says about self-promotion | Verdict |
|---|---|---|---|
| **OpenAI Developer Community** (`https://community.openai.com/guidelines`, Discourse forum, page title `Guidelines - OpenAI Developer Community`, cited as data) | the full guidelines page | « Share the cool things you have built, but avoid repetitive or overly promotional posts. » · « Spamming other members with pitches or other forms of self-promotion will not be tolerated. » · « Promote or advertise services unrelated to OpenAI products, developer work, or the category's purpose. » (listed among the things not to do) | **Allowed, once, in the right category**, as a built thing shared with developers, not a pitch. The relevant category was not identified on the guidelines page : `[TO BE CHECKED : the category list, logged in, on the day]`. |
| **Anthropic’s Discord server « Claude »** (invite `discord.gg/anthropic`, redirecting to `discord.com/invite/anthropic`) | the public invite metadata only (`discord.com/api/v9/invites/anthropic?with_counts=true`) : server name « Claude », about 129'856 members on 11 October 2026, landing channel « welcome » | **not readable without joining** : the rules and the channel list live inside the server | **Unknown until Victor joins and reads the rules channel.** Most servers of this kind have a dedicated channel for sharing projects ; post there or nowhere. |
| **An « Anthropic forum »** (the plan’s wording) | `community.anthropic.com` did not answer ; `anthropic.com/community` returned HTTP 404 ; GitHub Discussions on `anthropics/claude-code` returned HTTP 404 (not enabled) | no public forum of that name was found on 11 October 2026 | **No such place found.** The Discord server above is the closest official community. If Victor knows a forum, add it here with its rules read on the day. |
| **Reddit** (`r/ClaudeAI`, `r/ClaudeCode`, `r/codex`) | **unreachable from our tools** on 11 October 2026 : `reddit.com/r/<name>/about/rules.json` and `old.reddit.com` both returned a blocking page (« Welcome to Reddit ») ; the fetch tool reported it cannot fetch from `www.reddit.com` | **not read** | **Rules unknown.** Many subreddits restrict or forbid self-promotion and require a ratio of participation ; `[TO BE CHECKED : each subreddit’s rules, logged in, before posting ; if a rule forbids project posts, do not post]`. |
| **Hacker News** (for the record ; owned by `../ARTICLE_EN.md`) | `https://news.ycombinator.com/newsguidelines.html` | « Please don't use HN primarily for promotion. » (straight apostrophe cited as data) | A « Show HN » of the repository is acceptable if it is the only promotional act there ; see `ARTICLE_EN.md`. |

## Common rules for the three texts

- One post per place, never cross-posted the same day ; answer every comment within the week.
- Say what it is, what it refuses to do, and what the numbers are, honestly : the repository had **2 stars and 1 fork on 11 October 2026** (`mesures/releves.csv`), one star being ours. Replace with the reading of the day of posting, or leave the figures out.
- No link to anything but the repository (and the page `palambur.ch/methode/` when a reader asks). No price, no service, no training offer.
- Sign as the organisation, not as a person : « the Palambur team ».

## Text 1 · OpenAI Developer Community (Codex users)

**Title** · A SKILL.md that makes the agent ask four questions before writing a business document (MIT, Swiss, works in Codex)

> We run a small consultancy in Neuchâtel, Switzerland, and for a year we watched clients paste half a sentence into a chat window and send out whatever came back. So we wrote down what we did by hand before letting the model write, and published it as an Agent Skill under MIT licence.
>
> **What it does.** When someone asks for a working document (a job advert, a quote, a payment reminder, a contract), the skill anticipates the four decisions the model would otherwise guess and asks them one per message, with a counter, lettered choices and a cautious default. Then it returns two things : the complete prompt in five blocks, which the person keeps, and the deliverable. Whatever was not said is written as a bracket, `[TO BE COMPLETED]`, where a reviewer cannot miss it.
>
> **What it refuses.** It never invents a legal reference (article numbers are never quoted without a visible « to be verified »), never fills a gap with a plausible value, and never ends a document with a list of assumptions to validate. If the request contains a client name or an amount, the very first question is whether to anonymise them ; silence means yes.
>
> **Codex.** It is a plain `SKILL.md` folder on the open Agent Skills standard. Codex reads `~/.agents/skills/` and follows symbolic links, so one `ln -s` is the whole installation. We have not tested it inside Codex ourselves (the host is not installed on our machine), so a report from someone who has would be the most useful reply.
>
> **Honest numbers.** Two stars, one fork, as of 11 October 2026, and one of the stars is ours. It has been used daily in one consultancy since July 2026, never at scale.
>
> Repository : https://github.com/PALAMBUR/palambur-method · The skill sends nothing anywhere : no telemetry, no account.
>
> If it asks you a bad question, invents a value or cites a law it should not, please open an issue with the request as you typed it, anonymised.

## Text 2 · Discord server « Claude » (conditional : channel and rules to be read first)

Short, because a Discord message is read on a phone. **To post only in a channel meant for sharing projects**, and only if the server rules allow it.

> Sharing a skill we published under MIT licence : **Palambur Method**. It makes Claude ask up to four questions, one per message, before writing a business document (job advert, quote, reminder, contract), anonymises names and amounts by default, and writes `[TO BE COMPLETED]` instead of inventing a value. Built for Swiss businesses, usable anywhere ; works as a Claude Code plugin (`/plugin marketplace add PALAMBUR/palambur-method`, then `/plugin install palambur@palambur`) and as an uploaded skill on claude.ai. Two stars so far, one of them ours (11 October 2026). Feedback on bad questions is what we are after. https://github.com/PALAMBUR/palambur-method

## Text 3 · Reddit (conditional : rules not read on 11 October 2026)

Written for `r/ClaudeAI` or `r/ClaudeCode` ; **do not post** until the subreddit’s rules have been read logged in and allow project posts. If a flair such as « Project » or « Showcase » exists, use it. If the rules forbid self-promotion, drop this text and answer questions in existing threads instead.

**Title** · I published the checklist I used by hand before letting Claude write a contract, as a skill (MIT, 4 questions, no invented values)

> Ask Claude for « a job advert for a painter at 80 % » and you get a canton, a contract type, a start date, benefits and often a collective labour agreement in ten seconds. None of it was in the request. All of it reads as plausible.
>
> I run a small consultancy in French speaking Switzerland and I got tired of correcting that after the fact, so I wrote the questions I ask first into a `SKILL.md` and published it. With the skill loaded, Claude asks the four decisive questions one per message (« Question 1 of 4 », lettered choices, a cautious default), then gives you the full prompt and the document. Gaps stay as `[TO BE COMPLETED]`. It never quotes a legal article number without « to be verified », and if your request has a client name or an amount in it, the first question is whether to anonymise them.
>
> It is free, MIT, and sends nothing anywhere. Two stars, one fork, as of 11 October 2026 ; I am one of the stars. It has only been used in one consultancy so far, so the thing I want most is someone telling me which question was useless or which value it still invented.
>
> https://github.com/PALAMBUR/palambur-method (`/plugin marketplace add PALAMBUR/palambur-method`, then `/plugin install palambur@palambur`)

**Note on the first person** : Reddit reads better in the first person. If Victor posts it, « I » is him ; the repository and the README name the organisation, which is enough. No personal name appears in the text.

## Checks before posting (run by Victor, one command per block)

British spelling and the forbidden acronym, from the repository root :

```bash
grep -nE "ize\b|color|labor|center|\bSME" diffusion/partenaires/COMMUNAUTES_annonces_EN.md
```

Expected : no line, apart from the quoted rule text and this command itself.

Figures of the day :

```bash
python3 outils/mesure.py
```

Then replace « Two stars, one fork, as of 11 October 2026 » with the reading of the day, or remove the sentence.

## Requires Victor

- The **go**, place by place, after `v1.0.0` is public.
- **Joining the Discord server and reading its rules** ; **reading each subreddit’s rules** logged in ; identifying the right category on the OpenAI forum.
- Whether the Reddit text goes out in the first person under his own account.

## Markers left in this file

- `[TO BE CHECKED : the category list, logged in, on the day]` · OpenAI forum category.
- `[TO BE CHECKED : each subreddit’s rules, logged in, before posting ; if a rule forbids project posts, do not post]` · Reddit.
