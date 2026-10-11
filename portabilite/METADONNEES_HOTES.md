# Métadonnées propres à chaque hôte · relevé (point 87)

**Relevé du 11.10.2026 · session Skills et Prompt Ingénierie.** Question : quels fichiers, en plus de `SKILL.md`, chacun des hôtes accepte-t-il dans le dossier d’un skill, et lesquels méritent d’être posés dans `skills/palambur-method/` ? Règle : **un fichier n’est posé que s’il est documenté sur une page officielle lue ce jour** ; sinon il est écrit « non confirmé ». Chaque fait porte son URL et un extrait **mot pour mot** de la page.

## Table

| Hôte | Page officielle (lue le 11.10.2026) | Fichier ou champ accepté en plus de `SKILL.md` | Extrait exact | État pour ce skill |
|---|---|---|---|---|
| **Codex** (OpenAI) | `https://learn.chatgpt.com/docs/build-skills` | `agents/openai.yaml`, facultatif : section `interface` (nom affiché, description courte, icônes, couleur, `default_prompt`), section `policy` (`allow_implicit_invocation`, vrai par défaut), section `dependencies` (outils requis) | « A skill is a directory with a `SKILL.md` file plus optional scripts and references. » · le dossier `agents/openai.yaml` est annoté « Optional: appearance and dependencies. » · « When `false`, Codex won't implicitly invoke the skill based on user prompt. » | **documenté · à poser** (contenu proposé ci-dessous) |
| **Cursor** | `https://cursor.com/docs/context/skills` | aucun fichier de métadonnées ; des champs de frontmatter propres : `paths`, `disable-model-invocation`, `icon`, `color`, `metadata` ; dossiers facultatifs `scripts/`, `references/`, `assets/` | « Skills can also include optional directories for scripts, references, and assets: » · `name` : « Must match the parent folder name. » · `disable-model-invocation` : « When `true`, the skill is only included when explicitly invoked via `/skill-name`. » · `metadata` : « Arbitrary key-value mapping for additional metadata. » | **rien à poser** · le frontmatter actuel (`name`, `description`, `license`, `metadata`) est accepté tel quel ; `disable-model-invocation` resterait faux, le skill veut être invoqué par le modèle (porte 2) |
| **Gemini CLI** (Google) | `https://geminicli.com/docs/cli/skills/` | aucun fichier de métadonnées nommé ; fichiers joints libres | « Include scripts, templates, or example data alongside instructions so the agent has everything it needs. » · « Only skill metadata (name and description) is loaded initially. » | **rien à poser** · aucun champ propre documenté sur cette page |
| **GitHub Copilot** | `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills` et `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills` | aucun fichier de métadonnées ; champs `name`, `description` (obligatoires), `license`, `allowed-tools` (facultatifs) ; fichiers joints libres | « Skill files must be named `SKILL.md`. » · « Optionally, add scripts, examples or other resources to your skill's directory. » · « Copilot automatically discovers all of the files in the skill's directory » | **rien à poser** · `license: MIT` est déjà dans le frontmatter ; `allowed-tools` ne s’applique pas, le skill n’exécute rien |

**Lecture d’ensemble** : sur les quatre hôtes, **un seul** (Codex) documente un fichier de métadonnées à part. Les trois autres lisent le frontmatter de `SKILL.md` et des fichiers joints libres. Le skill n’a donc qu’**un** fichier à ajouter, et il est facultatif.

## Le fichier `agents/openai.yaml` · contenu proposé

Le fichier se pose dans `skills/palambur-method/agents/openai.yaml` (ce dossier appartient au paquet 1 ; la pose lui est demandée dans le rapport, elle n’est pas faite ici). Les noms de champs ci-dessous sont ceux que la page `build-skills` nomme (`interface`, `policy`, `dependencies`) ; les sous-champs d’`interface` sont décrits par la page comme un nom affiché, une description courte, des icônes, une couleur et un `default_prompt`, **sans que les clés exactes aient pu être recopiées mot pour mot** : avant la pose, le paquet 1 relit la page et aligne les clés sur l’exemple qu’elle donne.

```yaml
interface:
  display_name: "Méthode Palambur"
  short_description: "Pose les bonnes questions avant d’écrire un document de travail."
  default_prompt: "méthode palambur : "
policy:
  allow_implicit_invocation: true
```

Pourquoi ces valeurs :

- `allow_implicit_invocation: true` est la valeur par défaut ; elle est écrite pour dire que **la porte 2 du skill est voulue** (déclenchement sur la nature de la demande, sans mot).
- `default_prompt` donne l’amorce « méthode palambur : » pour que la personne n’ait qu’à écrire sa demande derrière (porte 1).
- **Pas de section `dependencies`** : le skill n’exige aucun outil, aucun serveur MCP, aucun réseau.
- **Pas d’icône ni de couleur** : la charte Palambur vit chez le site et sa Fabrique ; poser une couleur en dur ici serait une copie de plus (`CLAUDE.md` § 8). À ajouter le jour où la Fabrique sait produire ce fichier.

## Ce qui est non confirmé

- **Les clés exactes** des sous-champs d’`interface` dans `agents/openai.yaml` : décrites, pas recopiées. Relire la page avant la pose.
- **ChatGPT application de bureau** : la même page dit que les skills autonomes y sont disponibles ; si le fichier `agents/openai.yaml` y règle aussi l’affichage, la page le laisse entendre (« configure UI metadata ») sans que la phrase complète ait été recopiée : non confirmé.
- **Antigravity, Mistral Vibe, Gemini application** : hors du périmètre du point 87, non relevés ici ; voir `INSTALLATION.md`.

## Prochaine relecture

Avec la veille des plateformes, le **11.11.2026** (`VEILLE_PLATEFORMES.md`). Si une page citée change, la ligne de la table change avec sa nouvelle date.
