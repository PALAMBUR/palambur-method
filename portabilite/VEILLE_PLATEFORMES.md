# Veille · les skills chez les plateformes d’IA

État au **11.10.2026**. Socle du point 94 (suivi mensuel). Chaque ligne porte sa source ; **« officiel »** = page de l’éditeur lue ce jour ; **« source secondaire »** = blog ou presse, à ne pas citer comme fait ; **« non confirmé »** = aucune page officielle lue.

Le fichier a **trois parties** : le **journal mensuel** (une ligne par mois, ce qui a bougé), la **table d’état** (ce qui existe chez chaque plateforme, réécrite à chaque relevé), et la **procédure** (les pages à relire, la commande de relevé, ce qui reste non confirmé). Le journal ne se réécrit jamais : on ajoute une ligne. La table, elle, dit toujours l’état du dernier relevé.

## Journal mensuel · une ligne par mois

Relevé le **11 de chaque mois** (ou le premier jour ouvré qui suit). La ligne dit ce qui a changé depuis le relevé précédent, pour **les plateformes et pour le dépôt**, et renvoie à la table ou au fichier modifié. Une ligne sans changement s’écrit « rien n’a bougé », datée : c’est aussi une mesure.

| Relevé du | Ce qui a bougé | Conséquence pour le dépôt | Qui a relevé |
|---|---|---|---|
| **11.10.2026** | Premier relevé : 13 lignes de la table posées depuis les pages officielles ; Gemini retire les Gems (novembre 2026), Mistral remplace les Agents par des Skills, OpenAI annonce le retrait des GPT personnalisés sans date ; standard Agent Skills à 46 hôtes ; Infomaniak Euria sans notion de skill. Dépôt : 2 étoiles, 1 fork (`mesures/releves.csv`). | `adaptations/README.md` réécrit (trois fiches périmées retirées) ; `INSTALLATION.md` hôte par hôte ; `ANNUAIRES.md` ; point 17 du plan réorienté vers le plugin OpenAI ; projet Claude.ai et Euria restent les deux hôtes à prompt collé (`diffusion/partenaires/`). | session Skills et Prompt Ingénierie |
| 11.11.2026 | `[À RELEVER]` | | |

## Table

| Plateforme | Ce qui existe au 11.10.2026 | Emplacement ou geste | Forfaits | Source | Nature |
|---|---|---|---|---|---|
| **Standard Agent Skills** | spécification ouverte (`SKILL.md` + frontmatter `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`) ; liste de **46 hôtes** compatibles (relevé du 11.10.2026) dont Claude Code, Claude, ChatGPT et Codex, Cursor, GitHub Copilot, VS Code, Gemini CLI, Mistral Vibe CLI, Goose, OpenCode | `agentskills.io/specification` | sans objet | `https://agentskills.io/specification` · `https://agentskills.io/clients` | officiel |
| **Anthropic · Claude Code** | skills personnels, de projet, de plugin ; marketplaces Git ; `/skills`, `/skill-doctor`, `/reload-skills` ; liens symboliques acceptés ; validateur `claude plugin validate` | `~/.claude/skills/`, `.claude/skills/`, `<plugin>/skills/` | tous ceux qui ont Claude Code | `https://code.claude.com/docs/en/skills` · `https://code.claude.com/docs/en/plugins/publish` | officiel |
| **Anthropic · claude.ai et Cowork** | skills personnalisés par téléversement ZIP ; annuaire `claude.ai/directory` (403 sans connexion) ouvert aux soumissions (bundles) depuis un forfait payant ; une fiche sert claude.ai, Cowork et Claude Code | Customize › Skills › Upload ; `claude.ai/directory/manage` | Free à Enterprise pour l’usage ; **payant** pour soumettre | `https://support.claude.com/en/articles/12512180-using-skills-in-claude` · `https://claude.com/docs/directory/publish` | officiel |
| **OpenAI · Codex CLI et IDE** | skills autonomes, standard ouvert ; `.agents/skills` en cascade jusqu’à la racine Git ; `$HOME/.agents/skills` ; `/etc/codex/skills` ; **liens symboliques suivis** ; `$` pour invoquer ; `agents/openai.yaml` facultatif ; plugins avec marketplace `$REPO_ROOT/.agents/plugins/marketplace.json` et `codex plugin marketplace add` (page `plugins/build/plugins`) | voir colonne précédente ; `.codex/skills` et `$CODEX_HOME/skills` **absents de la page** | « Sign in with ChatGPT », forfaits non énumérés | `https://developers.openai.com/codex/skills` (→ `learn.chatgpt.com/docs/build-skills`) · `https://learn.chatgpt.com/codex/cli` · `https://developers.openai.com/plugins/build/plugins` | officiel ; forfaits **non confirmés** |
| **OpenAI · ChatGPT** | app de bureau : skills autonomes via barre latérale « Skills », invocation `@` ; web et mobile : « Skills bundled in plugins are also available in Chat and Work across ChatGPT on the web, desktop, and mobile. », les skills autonomes n’y sont pas listés (inférence, la page n’écrit pas « only ») ; un annuaire de plugins commun à ChatGPT et Codex ; soumission via `platform.openai.com/plugins` avec vérification d’identité | Skills (app de bureau) ; `@nom` | article d’aide (extrait moteur, page HTTP 403 pour nous) : Business, Enterprise, Healthcare, Edu ; **Free, Plus, Pro non confirmés** | `https://learn.chatgpt.com/docs/build-skills` · `https://learn.chatgpt.com/codex/skills-and-plugins` · `https://help.openai.com/en/articles/20001066-skills-in-chatgpt` | officiel pour les surfaces ; **extrait** pour les forfaits ; blogs (gigazine, bleepingcomputer) = source secondaire |
| **OpenAI · GPT personnalisés** | **en retrait** : « At retirement, custom GPTs stop running and leave the GPT directory », date non publiée ; « My GPTs › Migrate to plugin » transforme les instructions en skill | sans objet | sans objet | `https://learn.chatgpt.com/codex/migrate-custom-gpts` | officiel ; **date non confirmée** |
| **Google · Gemini CLI** | skills ; `~/.gemini/skills/` (alias `~/.agents/skills/`) ; en session `/skills list`, `/skills link <path>`, `/skills reload` ; dans le shell `gemini skills install <git> --consent` ; à l’activation « You will see a confirmation prompt in the UI » ; **remplacé par Antigravity CLI le 18.06.2026 pour les particuliers**, entreprises inchangées | voir colonne précédente | gratuit et Google One → Antigravity ; entreprise → Gemini CLI | `https://geminicli.com/docs/cli/skills/` · `https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli` | officiel |
| **Google · Antigravity** | skills, `name` facultatif, chaque skill devient une commande `/` ; `agy plugin install` | `.agents/skills/`, `~/.gemini/config/skills/`, `~/.gemini/antigravity-cli/skills/` | non lu | `https://antigravity.google/docs/skills` | officiel ; forfaits **non confirmés** |
| **Google · Gemini (app)** | **Gems retirés** : novembre 2026 (comptes personnels), mars 2027 (Workspace entreprise), juin 2027 (éducation), migration automatique ; skills par téléversement de `SKILL.md`, dossier ou ZIP ; 100 Mo (page 17094296) ; « only 100 can be active at a time » et partage annoncé « in the coming weeks », donc **pas disponible** (page 18560919) ; 18 ans, compte personnel seulement ; déploiement progressif | Settings › Skills › Upload ; `/nom` puis `@nom` | personnel ; Workspace **non pris en charge** pour l’instant | `https://support.google.com/gemini/answer/17094296` · `https://support.google.com/gemini/answer/18560919` (toutes deux **404 en HEAD, 200 en GET**, lisibles au navigateur) · `https://gemini.google/overview/gems/` | officiel |
| **Mistral · Vibe (ex Le Chat)** | renommé Vibe le 12.08.2026 ; **« If you relied on Agents, use Skills instead »** (page `vibe/overview`) ; Chat et Work fusionnés « Since September 22 » (la page ne donne pas l’année) ; Vibe Work : Context › Skills › New Skill, standard ouvert, partage privé ou espace de travail, pas de lien public ; Vibe CLI lit `.agents/skills/`, `.vibe/skills/`, `~/.vibe/skills/`, `~/.agents/skills/` | voir colonne précédente ; `/nom` ou `@` | non nommés | `https://help.mistral.ai/en/articles/682992-le-chat-is-now-vibe` · `https://docs.mistral.ai/vibe/overview` · `https://docs.mistral.ai/getting-started/quickstarts/vibe-work/create-first-skill` · `https://github.com/mistralai/mistral-vibe` | officiel ; forfaits **non confirmés** |
| **Cursor** | skills, standard ouvert ; projet `.agents/skills/` et `.cursor/skills/` ; utilisateur `~/.agents/skills/` et `~/.cursor/skills/` ; compatibilité `.claude/skills/` et `.codex/skills/` ; champs propres `disable-model-invocation`, `paths` ; la page ne décrit l’import GitHub que via un plugin | Customize › Skills | tous | `https://cursor.com/docs/context/skills` | officiel |
| **GitHub Copilot** | skills `SKILL.md` ; `.github/skills`, `.claude/skills`, `.agents/skills`, `~/.copilot/skills`, `~/.agents/skills` ; `/skills reload`, `/skills info` ; `gh skill` ; agent cloud, revue de code, CLI, VS Code, JetBrains | voir colonne précédente | non lu | `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills` · `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills` | officiel |
| **Infomaniak · Euria** | assistant kSuite hébergé **exclusivement en Suisse** ; **Projets** avec Instructions et documents ; **aucune notion de skill ni d’agent** sur la page (grep « skill », « agent » : 0) ; pas de partage de projet lu | Projets › Nouveau projet › Instructions | kSuite Free : 2 projets, 5 conversations par projet | `https://www.infomaniak.com/fr/support/faq/1369` · `https://www.infomaniak.com/fr/support/faq/2907` | officiel |
| **Infomaniak · AI Tools / AI Services** | page de l’offre : « API compatible OpenAI », « nos data centers en Suisse » ; FAQ 2177 : system prompt de l’assistant dans le Manager | Manager › Modifier l’assistant › Nouveau | selon produit | `https://www.infomaniak.com/fr/hebergement/ai-services` · `https://www.infomaniak.com/fr/support/faq/2177` | officiel |

## Ce que cela change pour Palambur

- **Un lien dans `~/.agents/skills/`** suffit à cinq hôtes (Codex, Cursor, Gemini CLI, Copilot, Vibe CLI). Le dépôt n’a rien à dupliquer.
- **Trois fiches de `adaptations/README.md` sont périmées** : « Gemini · Gem » (retrait en novembre), « Mistral · Agent (Le Chat) » (remplacé par Vibe Skills), « ChatGPT · GPT personnalisé » (retrait annoncé). Le prompt collé reste utile pour Projet Claude.ai et Infomaniak.
- **Le point 17 du plan** (GPT public) rejoint la voie plugin OpenAI : vérification d’identité de Victor, puis plugin « Skills only ».
- **Le point 16** (ChatGPT natif) dépend du forfait : l’article officiel n’a pas pu être lu, la liste Business, Enterprise, Healthcare, Edu vient d’un extrait. À vérifier **sur le compte de Victor** avant d’annoncer quoi que ce soit.

## Ce qui reste non confirmé au 11.10.2026

| Point | Pourquoi |
|---|---|
| Forfaits ChatGPT ouvrant les skills (Free, Plus, Pro) | article d’aide officiel en HTTP 403 pour nos outils ; seul un extrait moteur a été lu |
| Date de retrait des GPT personnalisés | page officielle sans date |
| Chemins `.codex/skills/` et `$CODEX_HOME/skills/` | absents de la page officielle Codex ; cités par des blogs seulement |
| Forfaits Codex, Antigravity, Mistral Vibe, Copilot | pages lues sans énumération de forfaits |
| Disponibilité des skills Gemini (app) pour le compte Palambur | « gradually rolling out », pas essayé |
| Présence du skill sur SkillsMP | page de recherche rendue côté client, illisible à nos outils ; sujet GitHub requis absent |
| Chargement réel par Cursor, Gemini, Copilot, Vibe | aucun de ces hôtes n’est installé sur la machine · **Codex éprouvé le 12.10.2026** avec le binaire embarqué dans ChatGPT.app (`INSTALLATION.md` § 2, `../epreuves/reponses/codex-natif/`) |

## La procédure mensuelle · ce qu’on relit, dans l’ordre

Chaque relevé suit ces étapes, puis ajoute **une ligne** au journal. Une page qui ne répond plus se remplace par la page officielle qui la remplace, jamais par un blog.

### 1 · Les pages à relire (une par ligne de la table)

| Plateforme | Pages (lues le 11.10.2026) | Ce qu’on cherche |
|---|---|---|
| Standard Agent Skills | `https://agentskills.io/specification` · `https://agentskills.io/clients` | champs du frontmatter ; nombre d’hôtes (46 au 11.10.2026) |
| Anthropic · Claude Code | `https://code.claude.com/docs/en/skills` · `https://code.claude.com/docs/en/plugins/publish` | emplacements, limites (500 lignes, 1'536 caractères), règle de version |
| Anthropic · claude.ai, Cowork, annuaire | `https://support.claude.com/en/articles/12512180-using-skills-in-claude` · `https://claude.com/docs/directory/publish` | téléversement ZIP, forfaits, soumission à l’annuaire ; **et le partage d’un Projet** (`diffusion/partenaires/PROJET_CLAUDE_AI.md`) |
| OpenAI · Codex | `https://developers.openai.com/codex/skills` · `https://learn.chatgpt.com/codex/cli` · `https://developers.openai.com/plugins/build/plugins` | emplacements, `agents/openai.yaml`, marketplace de plugins |
| OpenAI · ChatGPT | `https://learn.chatgpt.com/docs/build-skills` · `https://learn.chatgpt.com/codex/skills-and-plugins` · `https://help.openai.com/en/articles/20001066-skills-in-chatgpt` (403 le 11.10.2026 ; si toujours fermée, lire depuis le compte ChatGPT de Victor) | surfaces, forfaits Free, Plus, Pro |
| OpenAI · GPT personnalisés | `https://learn.chatgpt.com/codex/migrate-custom-gpts` | la date de retrait, toujours absente le 11.10.2026 |
| Google · Gemini CLI et Antigravity | `https://geminicli.com/docs/cli/skills/` · `https://antigravity.google/docs/skills` | emplacements, commandes `/skills` |
| Google · Gemini (app) | `https://support.google.com/gemini/answer/17094296` · `https://support.google.com/gemini/answer/18560919` (404 en HEAD, 200 en GET : lire au navigateur) | **partage des skills** ouvert ? disponibilité pour le compte Palambur |
| Mistral · Vibe | `https://docs.mistral.ai/vibe/overview` · `https://docs.mistral.ai/getting-started/quickstarts/vibe-work/create-first-skill` · `https://github.com/mistralai/mistral-vibe` | **lien public** de skill ? forfaits |
| Cursor | `https://cursor.com/docs/context/skills` | emplacements, import GitHub |
| GitHub Copilot | `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills` · `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills` | emplacements, `gh skill` |
| Infomaniak · Euria et AI Services | `https://www.infomaniak.com/fr/euria` · `https://www.infomaniak.com/fr/support/faq/1369` · `https://www.infomaniak.com/fr/support/faq/2907` · `https://www.infomaniak.com/fr/hebergement/ai-services` · `https://www.infomaniak.com/fr/support/faq/2177` | apparition d’une notion de skill ou de partage de projet ; suite de `diffusion/partenaires/INFOMANIAK_demande.md` |
| Annuaires | `https://skillsmp.com` · `https://mdskills.ai` · la liste travisvn (seuil de 10 étoiles) · `https://www.skillsdirectory.com/skills/palambur-palambur-method` | présence du skill après les gestes d’`ANNUAIRES.md` ; note de sécurité à rejouer |
| Communautés | règles de `https://community.openai.com/guidelines`, du serveur Discord « Claude », des subreddits visés (illisibles pour nos outils le 11.10.2026) | changement des règles d’auto-promotion avant tout post (`diffusion/partenaires/COMMUNAUTES_annonces_EN.md`) |

### 2 · La commande de relevé des pages

Depuis la racine du dépôt, une seule commande : elle lit chaque URL de ce fichier et imprime le code HTTP. Un code autre que 200 ou 30x se note dans le journal et la ligne de la table se revérifie au navigateur (les deux pages Google répondent 404 en HEAD par construction).

```bash
grep -oE 'https://[^` )|]+' portabilite/VEILLE_PLATEFORMES.md | sort -u | while read u; do printf '%s  %s\n' "$(curl -sIL --max-time 20 -o /dev/null -w '%{http_code}' "$u")" "$u"; done
```

### 3 · La commande de relevé du dépôt

Étoiles, forks, vues, clones du jour, une ligne dans `mesures/releves.csv` (lecture seule sur GitHub) :

```bash
python3 outils/mesure.py
```

### 4 · Ce qu’on fait de ce qui a bougé

1. Mettre à jour la ligne concernée de la **table d’état** (colonne « Ce qui existe au … », date du relevé).
2. Si un hôte à prompt collé change : relire la table des hôtes d’`adaptations/README.md`, puis `python3 outils/generer_adaptations.py --ecrire`.
3. Si un emplacement ou une commande change : corriger `INSTALLATION.md`, section de l’hôte.
4. Si un annuaire s’ouvre ou un seuil est atteint : `ANNUAIRES.md`, et un geste de Victor.
5. Si le Projet Claude.ai partagé existe : vérifier que ses instructions sont celles du prompt régénéré.
6. Ajouter **la ligne du mois** au journal, puis `python3 outils/controle.py`.

### 5 · Ce qu’il reste à vérifier au prochain relevé (11.11.2026)

1. Rouvrir l’article d’aide ChatGPT (403 le 11.10) ; sinon le lire depuis le compte de Victor.
2. Google : le **partage** des skills Gemini est-il ouvert (point 19 du plan) ?
3. Mistral Vibe : un **lien public** de skill existe-t-il (idem point 19) ?
4. SkillsMP et mdskills : le skill y est-il, après les gestes d’`ANNUAIRES.md` ?
5. Étoiles GitHub : le seuil de 10 ouvre la liste travisvn.
6. Reddit : les règles des subreddits visés, lues connecté (`COMMUNAUTES_annonces_EN.md`).
