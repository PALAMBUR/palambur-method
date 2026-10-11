# Emplacement Codex du skill `palambur-method`

Codex (OpenAI) lit les skills d’un dépôt dans **`.agents/skills/`**, en remontant jusqu’à la racine Git (source : `https://developers.openai.com/codex/skills`, consultée le 11.10.2026). Cursor, Gemini CLI, GitHub Copilot et Mistral Vibe CLI lisent le même dossier.

**La source du skill est unique** : `skills/palambur-method/`, à la racine du dépôt. Elle n’est **pas dupliquée** ici. Deux copies d’un même fichier finissent toujours par diverger, et celle qui diverge en silence est celle qu’on ne relit pas (le skill installé localement a déjà pris deux commits de retard sur GitHub, relevé du 11.10.2026).

## Lier plutôt que copier

La documentation Codex dit : **« Codex supports symlinked skill folders and follows the symlink target when scanning these locations. »** Depuis la racine du dépôt, remplacez ce dossier par un lien vers la source :

```bash
rm -r .agents/skills/palambur-method
```

```bash
ln -s ../../skills/palambur-method .agents/skills/palambur-method
```

Le lien est **relatif**, il survit à un déplacement du dépôt. Pour vérifier qu’il pointe bien :

```bash
ls -la .agents/skills/palambur-method/
```

Vous devez voir `SKILL.md` et ses fichiers de référence.

## Si le lien n’est pas possible

Sur un système qui ne suit pas les liens symboliques, copiez le dossier ; la copie devra être **refaite à chaque version** :

```bash
cp -R skills/palambur-method/. .agents/skills/palambur-method/
```

## Pourquoi ce dossier ne contient qu’un README

Au 11.10.2026, `which codex` était vide sur la machine de relevé. **Le 12.10.2026, le chargement par Codex a été éprouvé** avec le binaire embarqué dans l’application ChatGPT : le skill, lié par ce même type de lien dans `.agents/skills/` d’un dossier de travail, a été lu et le premier tour était conforme (`../../../epreuves/reponses/codex-natif/`). Le lien n’est pas commité tant que Victor n’a pas tranché : un lien symbolique dans Git fonctionne sous macOS et Linux mais pas toujours sous Windows, et la liste de contrôle d’Anthropic refuse les liens symboliques commités pour les entrées chargées par un plugin (source : `https://claude.com/docs/plugins/pre-submission-checklist`, 11.10.2026 ; ce dossier n’est pas chargé par le plugin Claude, mais la règle mérite d’être lue avant de commiter).

## Métadonnées propres à Codex · `agents/openai.yaml`

La page officielle `https://learn.chatgpt.com/docs/build-skills` (lue le 11.10.2026) décrit un fichier **facultatif** `agents/openai.yaml` dans le dossier du skill, annoté « Optional: appearance and dependencies. » : nom affiché, description courte, invite par défaut, et la règle `allow_implicit_invocation` (« When `false`, Codex won't implicitly invoke the skill based on user prompt. »). C’est le **seul** fichier de métadonnées à part documenté par l’un des quatre hôtes relevés (Codex, Cursor, Gemini CLI, Copilot) ; les trois autres lisent le frontmatter de `SKILL.md` et des fichiers joints libres. Le relevé complet, avec les extraits de chaque page et le contenu proposé pour ce fichier, est dans `portabilite/METADONNEES_HOTES.md`. **Au 11.10.2026, le fichier n’est pas posé** : il vit dans `skills/palambur-method/agents/`, avec la source, jamais ici.

Guide complet par hôte : `portabilite/INSTALLATION.md`.
