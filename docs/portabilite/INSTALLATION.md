# Installing the Palambur Method, host by host

English · [Français](INSTALLATION.fr.md)

Survey of 11.10.2026. Every statement about a platform carries its **official source** and the date it was consulted. Whatever could not be read on an official page is written **“not confirmed”**. The skill folder is `skills/palambur-method/`; the repository is `https://github.com/PALAMBUR/palambur-method`.

**One command per block.** Copy a block, paste it, wait for the result, move on to the next one.

Two families of hosts:

| Family | What you install | Hosts |
|---|---|---|
| **Native skill** (Agent Skills standard, `SKILL.md` file) | the `skills/palambur-method/` folder as is | Claude Code, Codex CLI, Codex in ChatGPT, ChatGPT (desktop app), Cursor, Gemini CLI and Antigravity, GitHub Copilot, Gemini (app), Mistral Vibe, claude.ai (custom skill) |
| **Pasted prompt** (a single instructions box) | one of the two prompts in `adaptations/` | Claude.ai Project, Mistral Vibe Work (instructions field), Infomaniak Euria and AI Tools |

ChatGPT’s custom GPT is no longer a recommended target: OpenAI has announced its retirement (§ 3).

---

## 1 · Claude Code

Source: `https://code.claude.com/docs/en/skills` and `https://code.claude.com/docs/en/plugins/publish` (consulted on 11.10.2026).

Claude Code reads three locations: the **personal** skill `~/.claude/skills/<name>/SKILL.md`, the **project** skill `.claude/skills/<name>/SKILL.md`, and the **plugin** skill `<plugin>/skills/<name>/SKILL.md`. The documentation states that a `<name>` entry may be **a symbolic link** to a folder located elsewhere on the disk (except for plugins). Skills reload **without restarting** Claude Code.

### 1a · Through the repository’s marketplace (recommended)

The repository carries its own marketplace (`.claude-plugin/marketplace.json`, name `palambur`) and its plugin (`.claude-plugin/plugin.json`, name `palambur`). The installation identifier is therefore `palambur@palambur`.

In Claude Code, add the marketplace:

```bash
/plugin marketplace add PALAMBUR/palambur-method
```

Then install the plugin:

```bash
/plugin install palambur@palambur
```

Since version 2.1.275, the documentation also gives the one-step form:

```bash
/plugin install palambur --marketplace PALAMBUR/palambur-method
```

On the command line (if `claude` is on your `PATH`), the equivalent is `claude plugin marketplace add PALAMBUR/palambur-method` then `claude plugin install palambur@palambur`. If `which claude` returns nothing, use the `/plugin` commands in the conversation: they do the same thing.

**Check that the skill is loaded**: open the plugins menu,

```bash
/plugin
```

then the **Installed** tab, and Enter on `palambur` to see its state and its components. On the command line (shell), the documented equivalents are `claude plugin list` and `claude plugin details palambur` (source `code.claude.com/docs/en/plugins/cli-reference`, sections “plugin list” and “plugin details”, 11.10.2026). Then the list of skills visible to Claude:

```bash
/skills
```

**Known limits** (source `code.claude.com/docs/en/skills`, 11.10.2026): the description and the `when_to_use` field are **truncated together at 1’536 characters** in the list Claude sees; `compatibility` is limited to 500 characters; the documentation recommends keeping `SKILL.md` **under 500 lines**. A new version of the plugin **must increment `version`** in `plugin.json`, otherwise users keep the old copy (source `code.claude.com/docs/en/plugins/publish`).

### 1b · By manual copy or link into `~/.claude/skills/`

Clone the repository once, wherever you like:

```bash
git clone https://github.com/PALAMBUR/palambur-method.git ~/palambur-method
```

Create the personal skills folder if it does not exist:

```bash
mkdir -p ~/.claude/skills
```

Then **link** the skill (a single source, updated with `git pull`):

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.claude/skills/palambur-method
```

If you prefer an independent **copy** (it will not follow updates):

```bash
cp -R ~/palambur-method/skills/palambur-method ~/.claude/skills/palambur-method
```

**Check** that the file is there:

```bash
ls -la ~/.claude/skills/palambur-method
```

You should see `SKILL.md`, its reference files (`methode-palambur.md`, `protection-donnees.md`, `references-juridiques.md`, `relecture.md`, `profil-entreprise.md`) and the `gabarits/` and `metiers/` folders (contents of version 1.0.0, 12.10.2026). Then, in Claude Code:

```bash
/skills
```

and, for a diagnosis of the frontmatter and the description:

```bash
/skill-doctor
```

If the skill does not appear:

```bash
/reload-skills
```

**Update** a linked skill:

```bash
git -C ~/palambur-method pull
```

**One truth, the repository**: the only source of the skill is `skills/palambur-method/` in the repository; every host location is a link or a dated copy that updates from it, never a file you fix in place. If you have cloned the repository twice, keep a single clone and point the link at it: two clones always end up diverging.

### 1c · Custom skill on claude.ai (without Claude Code)

Source: `https://support.claude.com/en/articles/12512180-using-skills-in-claude` (11.10.2026). In claude.ai: **Customize › Skills** (`https://claude.ai/customize/skills`, 403 when not signed in) › **+** › **Create skill** › **Upload a skill**, dropping a ZIP archive of the `palambur-method/` folder. Conditions read: Free, Pro, Max, Team, Enterprise plans; code execution must be enabled; **the folder name must equal the `name`** of the frontmatter. Outside Claude Code, only the fields `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` are accepted in the frontmatter (source `code.claude.com/docs/en/skills`).

Build the archive from the repository root (macOS; `--keepParent` keeps the `palambur-method/` folder at the root of the ZIP, as claude.ai requires; `--norsrc` avoids the `._*` files macOS would otherwise add):

```bash
ditto -c -k --keepParent --norsrc skills/palambur-method palambur-method.zip
```

---

## 2 · Codex CLI and Codex in the IDE (OpenAI)

Source: `https://developers.openai.com/codex/skills` (redirected to `https://learn.chatgpt.com/docs/build-skills`, consulted on 11.10.2026). Codex **“builds on the open agent skills standard”**.

**Locations read by Codex** (list from the official page): `$CWD/.agents/skills`, the `.agents/skills` folders of each parent directory **up to the root of the Git repository**, `$HOME/.agents/skills` (personal), `/etc/codex/skills` (machine), and the bundled system skills. **The paths `.codex/skills/` and `$CODEX_HOME/skills/` do not appear** on this page: they are **not confirmed** as of 11.10.2026 (blog posts cite them, the official page does not name them).

The page says explicitly: **“Codex supports symlinked skill folders and follows the symlink target when scanning these locations.”** You can therefore link instead of copying.

### 2a · Personal skill (all your Codex sessions)

Clone the repository if you have not done so already:

```bash
git clone https://github.com/PALAMBUR/palambur-method.git ~/palambur-method
```

Create the personal folder:

```bash
mkdir -p ~/.agents/skills
```

Link the skill:

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.agents/skills/palambur-method
```

### 2b · Repository skill (inside a project)

In the `palambur-method` repository itself, the `.agents/skills/palambur-method/` folder is provided for this: see its `README.md`. From the repository root:

```bash
ln -s ../../skills/palambur-method .agents/skills/palambur-method
```

### 2c · Check

In a Codex session, open the skills picker (the `build-skills` page writes: “In Codex CLI or the IDE extension, run `/skills` or type `$` to mention a skill.”):

```bash
/skills
```

Enabled skills also appear in the list of `/` commands (source `https://learn.chatgpt.com/codex/reference/slash-commands`, 11.10.2026). If an added skill does not appear, the `build-skills` page says: “Codex detects newly installed skills automatically; if one doesn’t appear, restart Codex.”

**Known limits** (`build-skills` page, 11.10.2026): the list of skills injected into the model is capped at **2 % of the context or 8’000 characters**; `SKILL.md` **must** contain `name` and `description`; an optional `agents/openai.yaml` file carries the interface metadata (implicit invocation allowed or not, required tools). To disable a skill without deleting it: a `[[skills.config]]` section with `path` and `enabled = false` in `~/.codex/config.toml`.

**Loading tested on 12.10.2026** with Codex CLI (`codex-cli 0.162.0-alpha.17.2`, binary bundled in the ChatGPT desktop application): skill linked by symbolic link in `.agents/skills/palambur-method` of a working folder, then `codex exec --skip-git-repo-check -s read-only --ephemeral` (standard input closed, otherwise Codex waits on stdin). Codex read `SKILL.md` and its reference files from `.agents/skills/`, then produced a **compliant first turn** (“Question 1 sur 4”, lettered choices, escape hatch, no Data Protection Act question since there was no data). A single turn: `codex exec` is not interactive, the whole exchange remains to be played in the IDE or the interactive CLI. The test protocol is described in [`../../epreuves/README.md`](../../epreuves/README.md). Official installation of the CLI (source `https://learn.chatgpt.com/codex/cli`, 11.10.2026; the page gives the form `curl … | sh`, split here so you can read the script before running it). Download the script:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh -o install.sh
```

Read it, then run it:

```bash
sh install.sh
```

then sign in with **“Sign in with ChatGPT”** on the first launch of `codex`. The plans that give access to Codex are not listed on this page: **not confirmed**.

---

## 3 · Native ChatGPT (without Codex)

Official source read: `https://learn.chatgpt.com/docs/build-skills` (11.10.2026), surfaces section. It distinguishes:

- **ChatGPT desktop application**: “Standalone skills are available in the ChatGPT desktop app, Codex CLI, and IDE extension.” Standalone skills (a `SKILL.md` folder) are added from the **“Skills”** sidebar and invoked with **`@`**.
- **ChatGPT web and mobile**: “Skills bundled in plugins are also available in Chat and Work across ChatGPT on the web, desktop, and mobile.” Standalone skills **are not listed** for web and mobile (inference: the page does not name them there, it does not write “only”).

The official help article **“Skills in ChatGPT”** (`https://help.openai.com/en/articles/20001066-skills-in-chatgpt`) **was not accessible to our tools on 11.10.2026 (HTTP 403)**. Its excerpt, read through a search engine, indicates that personal skills are available for **ChatGPT Business, Enterprise, Healthcare and Edu**, disabled by default for Enterprise and Edu until 23.07.2026. **Nothing could be read about Free, Plus or Pro: not confirmed.** Blog posts announcing a wider opening are **secondary sources**.

**Procedure** (desktop application, according to the `build-skills` page): prepare the `skills/palambur-method/` folder (or the ZIP from § 1c), open **Skills** in the sidebar, add the folder, then in a conversation type `@palambur-method`. **Not tested** as of 12.10.2026.

**Plugin path for the web**: OpenAI states that **“ChatGPT and Codex share one universal plugin directory”** (`https://learn.chatgpt.com/codex/skills-and-plugins`, 11.10.2026). Submitting a “Skills only” plugin requires an **identity verification** of the publisher account; it is the repository maintainer’s business, not the user’s.

**What to stop doing**: OpenAI is retiring **custom GPTs** (`https://learn.chatgpt.com/codex/migrate-custom-gpts`, 11.10.2026: “At retirement, custom GPTs stop running and leave the GPT directory”, no published date) and offers **“My GPTs › Migrate to plugin”**, which turns the instructions into a skill. This is why this guide no longer lists the custom GPT among the targets: if you have one, migrate it.

---

## 4 · Cursor

Source: `https://cursor.com/docs/context/skills` (11.10.2026). Cursor follows the Agent Skills standard.

**Locations**: project `.agents/skills/` or `.cursor/skills/`; user `~/.agents/skills/` or `~/.cursor/skills/`; **compatibility** with `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/`. So the link set up in § 2a (`~/.agents/skills/palambur-method`) **is also enough for Cursor**, and a skill already in `~/.claude/skills/` is seen.

If you have done neither:

```bash
mkdir -p ~/.cursor/skills
```

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.cursor/skills/palambur-method
```

**Check**: **Customize › Skills** sidebar (the skill appears with the “Agent Decides” mode), or type `/` followed by the skill name in the chat. **Limits**: lowercase `name` **must equal the folder name**, `description` required; Cursor-specific fields `disable-model-invocation` and `paths`; the page only describes import from GitHub through a `.cursor-plugin/marketplace.json` plugin; **Cloud Agents** only synchronise `~/.cursor/skills/`. **Not tested** as of 12.10.2026.

---

## 5 · Gemini CLI and Antigravity (Google)

Source: `https://geminicli.com/docs/cli/skills/` (11.10.2026). The page warns: **“Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026”**; the official announcement (`https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli`, 11.10.2026) states that enterprise accounts do not change and that Antigravity CLI **keeps Agent Skills**.

**Gemini CLI** · locations: user `~/.gemini/skills/` (accepted alias `~/.agents/skills/`), workspace `.gemini/skills/` or `.agents/skills/`. The link from § 2a is therefore enough. Otherwise, **in a session**, the documented command “`/skills link <path> [--scope user|workspace]`: Links skills from a local directory.”:

```bash
/skills link ~/palambur-method/skills/palambur-method
```

or, in the shell, install from Git (documented form: “gemini skills install https://github.com/user/repo.git --consent”):

```bash
gemini skills install https://github.com/PALAMBUR/palambur-method.git --consent
```

**Check**, in the session (“`/skills list [all] [nodesc]`: Shows discovered skills.”):

```bash
/skills list
```

After a manual addition:

```bash
/skills reload
```

**Limit**: when a skill is activated, the page says “You will see a confirmation prompt in the UI detailing the skill’s name, purpose” and execution follows “Upon your approval”. **Not tested** as of 12.10.2026.

**Antigravity** (`https://antigravity.google/docs/skills`, 11.10.2026): workspace `<root>/.agents/skills/`, global `~/.gemini/config/skills/` (Antigravity 2.0 and IDE), CLI `~/.gemini/antigravity-cli/skills/`, legacy `~/.gemini/antigravity/skills/`. `description` required, `name` optional (the folder is authoritative). Each skill becomes a `/` command. For the global location:

```bash
mkdir -p ~/.gemini/config/skills
```

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.gemini/config/skills/palambur-method
```

---

## 6 · GitHub Copilot

**Confirmed by the official documentation**: `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills` and `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills` (11.10.2026). “Skill files must be named SKILL.md”; `name` and `description` required, `license` and `allowed-tools` optional.

**Locations**: project `.github/skills`, `.claude/skills`, `.agents/skills`; personal `~/.copilot/skills`, `~/.agents/skills`. The link from § 2a is enough. Otherwise:

```bash
mkdir -p ~/.copilot/skills
```

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.copilot/skills/palambur-method
```

**Check**, in Copilot CLI:

```bash
/skills reload
```

```bash
/skills info palambur-method
```

The documentation also announces `gh skill` to search for, install, update and publish skills. Surfaces: cloud agent, code review, Copilot CLI, Copilot application, agent mode in VS Code and JetBrains. **Not tested** as of 12.10.2026.

---

## 7 · Gemini (app) · replaces the Gem

Source: `https://support.google.com/gemini/answer/17094296` (creation and upload) and `https://support.google.com/gemini/answer/18560919` (Gems transition), read on 11.10.2026; both pages answer **404 to a HEAD request** (`curl -I`) and **200 to a GET request**, they are read in a browser. Google is **retiring Gems**: “November 2026: Personal Google accounts.”, “March 2027: Workspace business, enterprise, and non-profit accounts.”, “June 2027: Workspace education accounts.”; existing Gems are **automatically recreated as skills**.

**The step is therefore no longer “create a Gem”**, but **upload the skill**: **Settings › Skills › Upload** sidebar, then choose the `SKILL.md` file, or a folder or a `.zip` **with `SKILL.md` at its root**, then **Create**. Conditions read on page 17094296: lowercase `name` with hyphens, “The total size of all uploaded files must not exceed 100 MB.”, reference files in plain text (`.docx` is not accepted), scripts cannot call outside, “Be 18 or over.”, “For now, this feature isn’t available if you sign in with a work or school Google Account.”, “Have Keep Activity on.”. Invocation: `/` then the skill (soon `@`). On page 18560919 (Gems transition): “You can create as many skills as you want, but only 100 can be active at a time.” and **sharing** with other people is announced “in the coming weeks”, so **not available as of 11.10.2026**. Availability: “We’re gradually making skills available in Gemini chats, starting with personal Google Accounts.”; **not confirmed** for a given account until it has been tried.

The ZIP is built as in § 1c. **Not tested** as of 12.10.2026.

---

## 8 · Mistral Vibe (formerly Le Chat) · replaces the “Agent”

Sources: `https://help.mistral.ai/en/articles/682992-le-chat-is-now-vibe` (article dated 12.08.2026), `https://docs.mistral.ai/vibe/overview` and `https://docs.mistral.ai/getting-started/quickstarts/vibe-work/create-first-skill` (11.10.2026). The `vibe/overview` page writes: **“If you relied on Agents, use Skills instead”** (invocation with `@`); the `create-first-skill` page writes that skills **“follow the open Agent Skills standard”**.

**Procedure** (Vibe Work): `chat.mistral.ai` › **Work** tab › **Context › Skills** › **New Skill** › Title, Description, contents of `SKILL.md` › **Create Skill**. Invocation `/palambur-method` or `@`. Sharing: **private or the whole workspace**, no public link. The plans concerned are not named: **not confirmed**.

**Vibe CLI** (`https://github.com/mistralai/mistral-vibe`, 11.10.2026) reads `.agents/skills/`, `.vibe/skills/`, `~/.vibe/skills/`, `~/.agents/skills/`: the link from § 2a is enough.

The full prompt from `adaptations/` remains usable as the skill’s content or as instructions.

---

## 9 · Claude.ai Project, Infomaniak · the pasted prompt

The texts to paste are **in `adaptations/`** at the repository root and are not copied here (a copy ages without saying so): `methode-palambur-prompt.md` (full) and `methode-palambur-prompt-court.md` (short), with the per-platform guide in [`adaptations/README.md`](../../adaptations/README.md).

| Platform | Where to paste | Official source (11.10.2026) | Status |
|---|---|---|---|
| **Claude.ai Project** | Project instructions, full prompt | `https://support.claude.com/en/articles/12512180-using-skills-in-claude` | works; the native skill (§ 1c) is preferable |
| **Infomaniak Euria** (kSuite) | **Projets › Nouveau projet › Instructions** (Projects › New project › Instructions), documents by drag and drop | `https://www.infomaniak.com/fr/support/faq/2907` and `/faq/1369` | hosting **exclusively in Switzerland**; free with kSuite Free (2 projects, 5 conversations per project); **no notion of skill or agent** on the Euria page; no project sharing read |
| **Infomaniak AI Tools / AI Services** (API) | system prompt of the assistant, Manager › “Modifier l’assistant conversationnel actuel” (Edit the current conversational assistant) › “Nouveau” (New) (FAQ 2177) | `https://www.infomaniak.com/fr/support/faq/2177` (setting) · `https://www.infomaniak.com/fr/hebergement/ai-services` (offer) | the offer page writes “API compatible OpenAI” (OpenAI-compatible API) and “nos data centers en Suisse” (our data centres in Switzerland); full prompt |

For these three hosts, the method **is** the assistant: it applies to every request, with no trigger word. ChatGPT’s custom GPT, which received the same prompt, is classed as “what to stop doing” in § 3.

---

## 10 · Summary · one link is enough for five hosts

The `~/.agents/skills/` folder is read by **Codex, Cursor, Gemini CLI, GitHub Copilot and Mistral Vibe CLI** (respective sources above). After § 2a, these five hosts see the skill. Claude Code reads `~/.claude/skills/` (§ 1b). Antigravity reads `~/.gemini/config/skills/` (§ 5).

**This guide has been tested on Claude Code and, on 12.10.2026, on Codex** (§ 2: skill read from `.agents/skills/`, compliant first turn, a single turn in `codex exec` mode). The other hosts have not been tested; their commands are those of the official pages cited, re-read on 11.10.2026. Next review of the sources is planned for **11.11.2026**.
