# Installer la Méthode Palambur, hôte par hôte

Relevé du 11.10.2026. Chaque affirmation sur une plateforme porte sa **source officielle** et sa date de consultation. Ce qui n’a pas pu être lu sur une page officielle est écrit **« non confirmé »**. Le dossier du skill est `skills/palambur-method/` ; le dépôt est `https://github.com/PALAMBUR/palambur-method`.

**Une commande par bloc.** Copiez un bloc, collez-le, attendez le résultat, passez au suivant.

Deux familles d’hôtes :

| Famille | Ce qu’on installe | Hôtes |
|---|---|---|
| **Skill natif** (standard Agent Skills, fichier `SKILL.md`) | le dossier `skills/palambur-method/` tel quel | Claude Code, Codex CLI, Codex dans ChatGPT, ChatGPT (app de bureau), Cursor, Gemini CLI et Antigravity, GitHub Copilot, Gemini (app), Mistral Vibe, claude.ai (skill personnalisé) |
| **Prompt collé** (une seule boîte d’instructions) | un des deux prompts de `adaptations/` | Projet Claude.ai, Mistral Vibe Work (champ d’instructions), Infomaniak Euria et AI Tools |

Le GPT personnalisé de ChatGPT n’est plus une cible recommandée : OpenAI annonce son retrait (§ 3).

---

## 1 · Claude Code

Source : `https://code.claude.com/docs/en/skills` et `https://code.claude.com/docs/en/plugins/publish` (consultées le 11.10.2026).

Claude Code lit trois emplacements : le skill **personnel** `~/.claude/skills/<nom>/SKILL.md`, le skill **de projet** `.claude/skills/<nom>/SKILL.md`, et le skill **de plugin** `<plugin>/skills/<nom>/SKILL.md`. La documentation précise qu’une entrée `<nom>` peut être **un lien symbolique** vers un dossier situé ailleurs sur le disque (hors plugins). Les skills se rechargent **sans redémarrer** Claude Code.

### 1a · Par le marketplace du dépôt (recommandé)

Le dépôt porte son propre marketplace (`.claude-plugin/marketplace.json`, nom `palambur`) et son plugin (`.claude-plugin/plugin.json`, nom `palambur`). L’identifiant d’installation est donc `palambur@palambur`.

Dans Claude Code, ajoutez le marketplace :

```bash
/plugin marketplace add PALAMBUR/palambur-method
```

Puis installez le plugin :

```bash
/plugin install palambur@palambur
```

Depuis la version 2.1.275, la documentation donne aussi la forme en un geste :

```bash
/plugin install palambur --marketplace PALAMBUR/palambur-method
```

En ligne de commande (si `claude` est sur votre `PATH`), l’équivalent est `claude plugin marketplace add PALAMBUR/palambur-method` puis `claude plugin install palambur@palambur`. Si `which claude` ne rend rien, passez par les commandes `/plugin` dans la conversation : elles font la même chose.

**Vérifier que le skill est chargé** : ouvrez le menu des plugins,

```bash
/plugin
```

puis l’onglet **Installed**, et Entrée sur `palambur` pour voir son état et ses composants. En ligne de commande (shell), les équivalents documentés sont `claude plugin list` et `claude plugin details palambur` (source `code.claude.com/docs/en/plugins/cli-reference`, sections « plugin list » et « plugin details », 11.10.2026). Puis la liste des skills visibles par Claude :

```bash
/skills
```

**Limites connues** (source `code.claude.com/docs/en/skills`, 11.10.2026) : la description et le champ `when_to_use` sont **tronqués ensemble à 1’536 caractères** dans la liste que voit Claude ; `compatibility` est limité à 500 caractères ; la documentation recommande de garder `SKILL.md` **sous 500 lignes**. Une nouvelle version du plugin **doit incrémenter `version`** dans `plugin.json`, sinon les utilisateurs gardent l’ancienne copie (source `code.claude.com/docs/en/plugins/publish`).

### 1b · Par copie ou lien manuel dans `~/.claude/skills/`

Clonez le dépôt une seule fois, à l’endroit de votre choix :

```bash
git clone https://github.com/PALAMBUR/palambur-method.git ~/palambur-method
```

Créez le dossier des skills personnels s’il n’existe pas :

```bash
mkdir -p ~/.claude/skills
```

Puis **liez** le skill (une seule source, mise à jour par `git pull`) :

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.claude/skills/palambur-method
```

Si vous préférez une **copie** indépendante (elle ne suivra pas les mises à jour) :

```bash
cp -R ~/palambur-method/skills/palambur-method ~/.claude/skills/palambur-method
```

**Vérifier** que le fichier est bien là :

```bash
ls -la ~/.claude/skills/palambur-method
```

Vous devez voir `SKILL.md`, ses fichiers de référence (`methode-palambur.md`, `protection-donnees.md`, `references-juridiques.md`, `relecture.md`, `profil-entreprise.md`) et les dossiers `gabarits/` et `metiers/` (contenu de la version 1.0.0, 12.10.2026). Puis, dans Claude Code :

```bash
/skills
```

et, pour un diagnostic du frontmatter et de la description :

```bash
/skill-doctor
```

Si le skill n’apparaît pas :

```bash
/reload-skills
```

**Mettre à jour** un skill lié :

```bash
git -C ~/palambur-method pull
```

**Une vérité, le dépôt** : la seule source du skill est `skills/palambur-method/` dans le dépôt ; tout emplacement d’hôte est un lien ou une copie datée qui se met à jour depuis lui, jamais un fichier qu’on corrige sur place. Si vous avez cloné le dépôt deux fois, gardez un seul clone et faites pointer le lien vers lui : deux clones finissent toujours par diverger.

### 1c · Skill personnalisé sur claude.ai (sans Claude Code)

Source : `https://support.claude.com/en/articles/12512180-using-skills-in-claude` (11.10.2026). Dans claude.ai : **Customize › Skills** (`https://claude.ai/customize/skills`, 403 sans connexion) › **+** › **Create skill** › **Upload a skill**, en déposant une archive ZIP du dossier `palambur-method/`. Conditions lues : forfaits Free, Pro, Max, Team, Enterprise ; l’exécution de code doit être activée ; **le nom du dossier doit être égal au `name`** du frontmatter. Hors Claude Code, seuls les champs `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` sont acceptés dans le frontmatter (source `code.claude.com/docs/en/skills`).

Fabriquer l’archive depuis la racine du dépôt (macOS ; `--keepParent` garde le dossier `palambur-method/` à la racine du ZIP, comme claude.ai l’exige ; `--norsrc` évite les fichiers `._*` que macOS ajoute sinon) :

```bash
ditto -c -k --keepParent --norsrc skills/palambur-method palambur-method.zip
```

---

## 2 · Codex CLI et Codex dans l’IDE (OpenAI)

Source : `https://developers.openai.com/codex/skills` (redirigée vers `https://learn.chatgpt.com/docs/build-skills`, consultée le 11.10.2026). Codex **« builds on the open agent skills standard »**.

**Emplacements lus par Codex** (liste de la page officielle) : `$CWD/.agents/skills`, les dossiers `.agents/skills` de chaque répertoire parent **jusqu’à la racine du dépôt Git**, `$HOME/.agents/skills` (personnel), `/etc/codex/skills` (machine), et les skills système fournis. **Les chemins `.codex/skills/` et `$CODEX_HOME/skills/` ne figurent pas** sur cette page : ils sont **non confirmés** au 11.10.2026 (des articles de blog les citent, la page officielle ne les nomme pas).

La page dit explicitement : **« Codex supports symlinked skill folders and follows the symlink target when scanning these locations. »** On peut donc lier au lieu de copier.

### 2a · Skill personnel (toutes vos sessions Codex)

Clonez le dépôt si ce n’est pas déjà fait :

```bash
git clone https://github.com/PALAMBUR/palambur-method.git ~/palambur-method
```

Créez le dossier personnel :

```bash
mkdir -p ~/.agents/skills
```

Liez le skill :

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.agents/skills/palambur-method
```

### 2b · Skill de dépôt (dans un projet)

Dans le dépôt `palambur-method` lui-même, le dossier `.agents/skills/palambur-method/` est prévu : voir son `README.md`. Depuis la racine du dépôt :

```bash
ln -s ../../skills/palambur-method .agents/skills/palambur-method
```

### 2c · Vérifier

Dans une session Codex, ouvrez le sélecteur de skills (la page `build-skills` écrit : « In Codex CLI or the IDE extension, run `/skills` or type `$` to mention a skill. ») :

```bash
/skills
```

Les skills activés apparaissent aussi dans la liste des commandes `/` (source `https://learn.chatgpt.com/codex/reference/slash-commands`, 11.10.2026). Si un skill ajouté n’apparaît pas, la page `build-skills` dit : « Codex detects newly installed skills automatically; if one doesn’t appear, restart Codex. »

**Limites connues** (page `build-skills`, 11.10.2026) : la liste des skills injectée au modèle est plafonnée à **2 % du contexte ou 8’000 caractères** ; `SKILL.md` **doit** contenir `name` et `description` ; un fichier optionnel `agents/openai.yaml` porte les métadonnées d’interface (invocation implicite autorisée ou non, outils requis). Pour désactiver un skill sans le supprimer : section `[[skills.config]]` avec `path` et `enabled = false` dans `~/.codex/config.toml`.

**Chargement éprouvé le 12.10.2026** avec Codex CLI (`codex-cli 0.162.0-alpha.17.2`, binaire embarqué dans l’application ChatGPT de bureau) : skill lié par lien symbolique dans `.agents/skills/palambur-method` d’un dossier de travail, puis `codex exec --skip-git-repo-check -s read-only --ephemeral` (entrée standard fermée, sinon Codex attend sur stdin). Codex a lu `SKILL.md` et ses fichiers de référence depuis `.agents/skills/`, puis a rendu un **premier tour conforme** (« Question 1 sur 4 », choix lettrés, échappatoire, aucune question nLPD puisque aucune donnée). Un seul tour : `codex exec` n’est pas interactif, l’échange entier reste à jouer dans l’IDE ou le CLI interactif. Le protocole des épreuves est décrit dans [`../../epreuves/README.md`](../../epreuves/README.md). Installation officielle du CLI (source `https://learn.chatgpt.com/codex/cli`, 11.10.2026 ; la page donne la forme `curl … | sh`, découpée ici pour lire le script avant de l’exécuter). Téléchargez le script :

```bash
curl -fsSL https://chatgpt.com/codex/install.sh -o install.sh
```

Lisez-le, puis exécutez-le :

```bash
sh install.sh
```

puis connexion par **« Sign in with ChatGPT »** au premier lancement de `codex`. Les forfaits donnant droit à Codex ne sont pas énumérés sur cette page : **non confirmé**.

---

## 3 · ChatGPT natif (sans Codex)

Source officielle lue : `https://learn.chatgpt.com/docs/build-skills` (11.10.2026), section des surfaces. Elle distingue :

- **Application ChatGPT de bureau** : « Standalone skills are available in the ChatGPT desktop app, Codex CLI, and IDE extension. » Les skills autonomes (un dossier `SKILL.md`) s’ajoutent depuis la barre latérale **« Skills »** et s’invoquent avec **`@`**.
- **ChatGPT web et mobile** : « Skills bundled in plugins are also available in Chat and Work across ChatGPT on the web, desktop, and mobile. » Les skills autonomes **ne sont pas listés** pour le web et le mobile (inférence : la page ne les y nomme pas, elle n’écrit pas « only »).

L’article d’aide officiel **« Skills in ChatGPT »** (`https://help.openai.com/en/articles/20001066-skills-in-chatgpt`) **n’était pas accessible à nos outils le 11.10.2026 (HTTP 403)**. Son extrait, lu par un moteur de recherche, indique que les skills personnels sont disponibles pour **ChatGPT Business, Enterprise, Healthcare et Edu**, désactivés par défaut pour Enterprise et Edu jusqu’au 23.07.2026. **Rien n’a pu être lu sur Free, Plus ou Pro : non confirmé.** Les articles de blog qui annoncent une ouverture plus large sont des **sources secondaires**.

**Procédure** (application de bureau, d’après la page `build-skills`) : préparez le dossier `skills/palambur-method/` (ou le ZIP du § 1c), ouvrez **Skills** dans la barre latérale, ajoutez le dossier, puis dans une conversation tapez `@palambur-method`. **Non éprouvé** au 12.10.2026.

**Chemin plugin pour le web** : OpenAI déclare que **« ChatGPT and Codex share one universal plugin directory »** (`https://learn.chatgpt.com/codex/skills-and-plugins`, 11.10.2026). La soumission d’un plugin « Skills only » demande une **vérification d’identité** du compte éditeur ; elle relève du mainteneur du dépôt, pas de l’utilisateur.

**À ne plus faire** : OpenAI retire les **GPT personnalisés** (`https://learn.chatgpt.com/codex/migrate-custom-gpts`, 11.10.2026 : « At retirement, custom GPTs stop running and leave the GPT directory », sans date publiée) et propose **« My GPTs › Migrate to plugin »**, qui transforme les instructions en skill. C’est pourquoi ce guide ne liste plus le GPT personnalisé parmi les cibles : si vous en avez un, migrez-le.

---

## 4 · Cursor

Source : `https://cursor.com/docs/context/skills` (11.10.2026). Cursor suit le standard Agent Skills.

**Emplacements** : projet `.agents/skills/` ou `.cursor/skills/` ; utilisateur `~/.agents/skills/` ou `~/.cursor/skills/` ; **compatibilité** avec `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/`. Donc le lien posé au § 2a (`~/.agents/skills/palambur-method`) **suffit aussi pour Cursor**, et un skill déjà dans `~/.claude/skills/` est vu.

Si vous n’avez fait ni l’un ni l’autre :

```bash
mkdir -p ~/.cursor/skills
```

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.cursor/skills/palambur-method
```

**Vérifier** : barre latérale **Customize › Skills** (le skill apparaît avec le mode « Agent Decides »), ou tapez `/` suivi du nom du skill dans le chat. **Limites** : `name` en minuscules **doit être égal au nom du dossier**, `description` obligatoire ; champs propres à Cursor `disable-model-invocation` et `paths` ; la page ne décrit l’import depuis GitHub que via un plugin `.cursor-plugin/marketplace.json` ; les **Cloud Agents** ne synchronisent que `~/.cursor/skills/`. **Non éprouvé** au 12.10.2026.

---

## 5 · Gemini CLI et Antigravity (Google)

Source : `https://geminicli.com/docs/cli/skills/` (11.10.2026). La page avertit : **« Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026 »** ; l’annonce officielle (`https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli`, 11.10.2026) précise que les comptes entreprise ne changent pas et qu’Antigravity CLI **conserve les Agent Skills**.

**Gemini CLI** · emplacements : utilisateur `~/.gemini/skills/` (alias accepté `~/.agents/skills/`), espace de travail `.gemini/skills/` ou `.agents/skills/`. Le lien du § 2a suffit donc. Sinon, **en session**, la commande documentée « `/skills link <path> [--scope user|workspace]`: Links skills from a local directory. » :

```bash
/skills link ~/palambur-method/skills/palambur-method
```

ou, dans le shell, installer depuis Git (forme documentée : « gemini skills install https://github.com/user/repo.git --consent ») :

```bash
gemini skills install https://github.com/PALAMBUR/palambur-method.git --consent
```

**Vérifier**, dans la session (« `/skills list [all] [nodesc]`: Shows discovered skills. ») :

```bash
/skills list
```

Après un ajout à la main :

```bash
/skills reload
```

**Limite** : à l’activation d’un skill, la page dit « You will see a confirmation prompt in the UI detailing the skill’s name, purpose » et l’exécution suit « Upon your approval ». **Non éprouvé** au 12.10.2026.

**Antigravity** (`https://antigravity.google/docs/skills`, 11.10.2026) : espace de travail `<racine>/.agents/skills/`, global `~/.gemini/config/skills/` (Antigravity 2.0 et IDE), CLI `~/.gemini/antigravity-cli/skills/`, ancien `~/.gemini/antigravity/skills/`. `description` obligatoire, `name` facultatif (le dossier fait foi). Chaque skill devient une commande `/`. Pour le global :

```bash
mkdir -p ~/.gemini/config/skills
```

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.gemini/config/skills/palambur-method
```

---

## 6 · GitHub Copilot

**Confirmé par la documentation officielle** : `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills` et `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills` (11.10.2026). « Skill files must be named SKILL.md » ; `name` et `description` obligatoires, `license` et `allowed-tools` facultatifs.

**Emplacements** : projet `.github/skills`, `.claude/skills`, `.agents/skills` ; personnel `~/.copilot/skills`, `~/.agents/skills`. Le lien du § 2a suffit. Sinon :

```bash
mkdir -p ~/.copilot/skills
```

```bash
ln -s ~/palambur-method/skills/palambur-method ~/.copilot/skills/palambur-method
```

**Vérifier**, dans Copilot CLI :

```bash
/skills reload
```

```bash
/skills info palambur-method
```

La documentation annonce aussi `gh skill` pour chercher, installer, mettre à jour et publier des skills. Surfaces : agent cloud, revue de code, Copilot CLI, application Copilot, mode agent dans VS Code et JetBrains. **Non éprouvé** au 12.10.2026.

---

## 7 · Gemini (application) · remplace le Gem

Source : `https://support.google.com/gemini/answer/17094296` (création et téléversement) et `https://support.google.com/gemini/answer/18560919` (transition des Gems), lues le 11.10.2026 ; ces deux pages répondent **404 à une requête HEAD** (`curl -I`) et **200 à une requête GET**, elles se lisent au navigateur. Google **retire les Gems** : « November 2026: Personal Google accounts. », « March 2027: Workspace business, enterprise, and non-profit accounts. », « June 2027: Workspace education accounts. » ; les Gems existants sont **recréés automatiquement en skills**.

**Le geste n’est donc plus « créer un Gem »**, mais **téléverser le skill** : barre latérale **Settings › Skills › Upload**, puis choisir le fichier `SKILL.md`, ou un dossier ou un `.zip` **dont `SKILL.md` est à la racine**, puis **Create**. Conditions lues sur la page 17094296 : `name` en minuscules avec traits d’union, « The total size of all uploaded files must not exceed 100 MB. », fichiers de référence en texte brut (le `.docx` n’est pas accepté), les scripts ne peuvent pas appeler l’extérieur, « Be 18 or over. », « For now, this feature isn’t available if you sign in with a work or school Google Account. », « Have Keep Activity on. ». Invocation : `/` puis le skill (bientôt `@`). Sur la page 18560919 (transition des Gems) : « You can create as many skills as you want, but only 100 can be active at a time. » et le **partage** avec d’autres personnes est annoncé « in the coming weeks », donc **pas disponible au 11.10.2026**. Disponibilité : « We’re gradually making skills available in Gemini chats, starting with personal Google Accounts. » ; **non confirmé** pour un compte donné tant qu’il n’a pas été essayé.

Le ZIP se fabrique comme au § 1c. **Non éprouvé** au 12.10.2026.

---

## 8 · Mistral Vibe (ex Le Chat) · remplace « l’Agent »

Sources : `https://help.mistral.ai/en/articles/682992-le-chat-is-now-vibe` (article daté du 12.08.2026), `https://docs.mistral.ai/vibe/overview` et `https://docs.mistral.ai/getting-started/quickstarts/vibe-work/create-first-skill` (11.10.2026). La page `vibe/overview` écrit : **« If you relied on Agents, use Skills instead »** (invocation avec `@`) ; la page `create-first-skill` écrit que les skills **« follow the open Agent Skills standard »**.

**Procédure** (Vibe Work) : `chat.mistral.ai` › onglet **Work** › **Context › Skills** › **New Skill** › Titre, Description, contenu du `SKILL.md` › **Create Skill**. Invocation `/palambur-method` ou `@`. Partage : **privé ou l’espace de travail entier**, pas de lien public. Les forfaits concernés ne sont pas nommés : **non confirmé**.

**Vibe CLI** (`https://github.com/mistralai/mistral-vibe`, 11.10.2026) lit `.agents/skills/`, `.vibe/skills/`, `~/.vibe/skills/`, `~/.agents/skills/` : le lien du § 2a suffit.

Le prompt complet d’`adaptations/` reste utilisable comme contenu du skill ou comme instructions.

---

## 9 · Projet Claude.ai, Infomaniak · le prompt collé

Les textes à coller sont **dans `adaptations/`** à la racine du dépôt et ne sont pas recopiés ici (une copie vieillit sans le dire) : `methode-palambur-prompt.md` (complet) et `methode-palambur-prompt-court.md` (court), avec le guide par plateforme dans [`adaptations/README.md`](../../adaptations/README.md).

| Plateforme | Où coller | Source officielle (11.10.2026) | État |
|---|---|---|---|
| **Projet Claude.ai** | Instructions du projet, prompt complet | `https://support.claude.com/en/articles/12512180-using-skills-in-claude` | fonctionne ; le skill natif (§ 1c) est préférable |
| **Infomaniak Euria** (kSuite) | **Projets › Nouveau projet › Instructions**, documents en glisser-déposer | `https://www.infomaniak.com/fr/support/faq/2907` et `/faq/1369` | hébergement **exclusivement en Suisse** ; gratuit avec kSuite Free (2 projets, 5 conversations par projet) ; **aucune notion de skill ni d’agent** sur la page Euria ; pas de partage de projet lu |
| **Infomaniak AI Tools / AI Services** (API) | system prompt de l’assistant, Manager › « Modifier l’assistant conversationnel actuel » › « Nouveau » (FAQ 2177) | `https://www.infomaniak.com/fr/support/faq/2177` (réglage) · `https://www.infomaniak.com/fr/hebergement/ai-services` (offre) | la page de l’offre écrit « API compatible OpenAI » et « nos data centers en Suisse » ; prompt complet |

Pour ces trois hôtes, la méthode **est** l’assistant : elle s’applique à chaque demande, sans mot déclencheur. Le GPT personnalisé de ChatGPT, qui recevait le même prompt, est classé « à ne plus faire » au § 3.

---

## 10 · Récapitulatif · un lien suffit pour cinq hôtes

Le dossier `~/.agents/skills/` est lu par **Codex, Cursor, Gemini CLI, GitHub Copilot et Mistral Vibe CLI** (sources respectives ci-dessus). Après le § 2a, ces cinq hôtes voient le skill. Claude Code lit `~/.claude/skills/` (§ 1b). Antigravity lit `~/.gemini/config/skills/` (§ 5).

**Ce guide a été éprouvé sur Claude Code et, le 12.10.2026, sur Codex** (§ 2 : skill lu depuis `.agents/skills/`, premier tour conforme, un seul tour en mode `codex exec`). Les autres hôtes n’ont pas été éprouvés ; leurs commandes sont celles des pages officielles citées, relues le 11.10.2026. Prochaine relecture des sources prévue au **11.11.2026**.
