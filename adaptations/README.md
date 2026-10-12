# Adaptations · le prompt à coller, pour les hôtes sans skill

Le skill `palambur-method` (dossier `skills/`) est **natif Claude Code** : Claude charge le corps du skill et ses fichiers de référence **à la demande** (divulgation progressive). Depuis que `SKILL.md` est un standard ouvert, la plupart des hôtes lisent ce même dossier (Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe CLI) ou l’acceptent par téléversement (Gemini application, Mistral Vibe Work, claude.ai) : pour eux, **rien à coller**, voir [`../docs/portabilite/INSTALLATION.md`](../docs/portabilite/INSTALLATION.md).

Restent les hôtes qui n’offrent qu’une **boîte d’instructions système**, avec une limite de taille. Ces adaptations condensent la méthode en **un prompt autonome**, en deux tailles :

| Fichier | Pour |
|---|---|
| [`methode-palambur-prompt.md`](methode-palambur-prompt.md) | Version **complète** (limite 8'000 caractères) · Projet Claude.ai, Infomaniak AI Tools, Euria Projets, GPT personnalisé |
| [`methode-palambur-prompt-court.md`](methode-palambur-prompt-court.md) | Version **courte** (limite 1'500 caractères) · champs d’instructions bornés (Instructions personnalisées ChatGPT, et tout champ court quand il existe) |

La taille exacte du bloc à coller est écrite en tête de chaque fichier, au moment de sa génération. Elle n’est pas recopiée ici : un chiffre recopié vieillit sans le dire.

> Différence clé avec le skill : sur ces hôtes, l’assistant **EST** la méthode (elle s’applique à chaque demande). Il n’y a pas de mot déclencheur « palambur ».

## Où coller le prompt, hôte par hôte

État relevé le **11.10.2026** sur les pages officielles de chaque hôte (citées, avec leur date, dans le guide d’installation ; pas recopiées ici). Trois fiches de la version précédente de ce fichier étaient périmées : le Gem Google, l’Agent Mistral et le GPT personnalisé.

| Hôte | Quelle version | Où | État au 11.10.2026 |
|---|---|---|---|
| Claude · Projet (claude.ai) | complète | Instructions du projet | fonctionne ; le skill natif téléversé (§ 1c du guide) est préférable |
| Infomaniak · Euria (kSuite) | complète | Projets › Nouveau projet › Instructions | hébergé **exclusivement en Suisse** ; aucune notion de skill sur la page Euria ; gratuit avec kSuite Free (2 projets) |
| Infomaniak · AI Tools (API) | complète | Manager › Modifier l’assistant › system prompt | API compatible OpenAI, centres de données suisses |
| ChatGPT · GPT personnalisé | complète | Explorer les GPT › Créer › Configurer › Instructions | **en retrait annoncé** par OpenAI, date non publiée ; migration vers plugin proposée · **non confirmé au 11.10.2026** pour la date |
| ChatGPT · Instructions personnalisées | courte | Réglages › Personnalisation | champ court ; les skills natifs ChatGPT dépendent du forfait, **non confirmé au 11.10.2026** pour Free, Plus, Pro |
| Google · Gemini (application) | aucune · téléverser `SKILL.md` | Settings › Skills › Upload | les **Gems sont retirés** dès novembre 2026 (comptes personnels) ; le skill remplace le prompt collé · déploiement progressif, **non confirmé au 11.10.2026** pour un compte donné tant qu’il n’a pas été essayé |
| Mistral · Vibe Work (ex Le Chat) | aucune · créer un skill | Context › Skills › New Skill | les **Agents sont remplacés par des Skills** ; le prompt complet peut servir de contenu de skill · forfaits **non confirmés au 11.10.2026** |
| Claude Code, Codex, Cursor, Copilot, Gemini CLI, Vibe CLI | aucune | le dossier `skills/palambur-method/` lui-même | voir le [README principal](../README.md) et le guide |

## Maintenance · ces fichiers sont générés

**Ne pas éditer ces deux fichiers à la main.** Ils sont fabriqués par [`../outils/generer_adaptations.py`](../outils/generer_adaptations.py) depuis `SKILL.md`, `methode-palambur.md`, `protection-donnees.md` **et la table des hôtes ci-dessus** (c’est elle qui écrit le chapeau de chaque fichier : quel hôte reçoit quelle version). La première ligne de chaque fichier porte la date de génération et l’empreinte des quatre sources ; `outils/controle.py` refuse si l’empreinte ne correspond plus.

À blanc, pour voir les tailles et le diff :

```bash
python3 outils/generer_adaptations.py
```

En écriture, pour régénérer les deux fichiers :

```bash
python3 outils/generer_adaptations.py --ecrire
```

Pourquoi : les versions précédentes, retouchées à la main, dataient du 12.07.2026 alors que le skill avait changé le 04.08 et le 24.09. Le générateur supprime cette dérive. La table ci-dessus est la **seule** liste des hôtes du dépôt (le générateur la lit, il n’en porte pas de copie) : elle se relit sur les pages officielles, prochaine relecture prévue le **11.11.2026**. Toute modification de ce fichier change l’empreinte des sources : relancez le générateur en écriture, sinon `outils/controle.py` refuse. Une ligne « complète » ou « courte » ajoutée, retirée ou renommée change les deux fichiers générés.
