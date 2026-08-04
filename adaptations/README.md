# Adaptations multi-IA de la Méthode Palambur

Le skill `palambur-method` (dossier `skills/`) est **natif Claude Code** : Claude charge le corps du skill et ses fichiers de référence **à la demande** (divulgation progressive). Les autres plateformes n'ont pas ce mécanisme : elles offrent une **seule boîte d'instructions système**, avec des limites de taille.

Ces adaptations condensent donc la méthode en **un prompt autonome**, décliné en deux tailles :

| Fichier | Pour |
|---|---|
| [`methode-palambur-prompt.md`](methode-palambur-prompt.md) | Version **complète** (7 258 car.) · GPT personnalisé, Agent Mistral, AI Tools Infomaniak, Projet Claude |
| [`methode-palambur-prompt-court.md`](methode-palambur-prompt-court.md) | Version **courte** (1 481 car.) · Gemini Gem, Instructions personnalisées ChatGPT |

> Différence clé avec le skill Claude : sur ces plateformes, l'assistant **EST** la méthode (elle s'applique à chaque demande). Il n'y a pas de mot-déclencheur « palambur ».

## Où coller le prompt, plateforme par plateforme

### ChatGPT · GPT personnalisé (recommandé)
1. ChatGPT → **Explorer les GPT** → **Créer** → onglet **Configurer**.
2. Nom : `Méthode Palambur`. Coller la **version complète** dans le champ **Instructions** (limite ~8 000 car.).
3. Enregistrer (privé, lien, ou public).

### ChatGPT · Instructions personnalisées (global, sans créer de GPT)
Réglages → **Personnalisation** → **Instructions personnalisées** → coller la **version courte** (limite 1 500 car.) dans « Comment ChatGPT doit-il répondre ? ». S'applique à toutes vos conversations.

### Google Gemini · Gem (nécessite Gemini Advanced)
1. gemini.google.com → **Explorer les Gems** → **Nouveau Gem**.
2. Nom : `Méthode Palambur`. Coller la **version courte** dans les instructions (Google conseille 500 à 2 000 car.).
3. Tester dans l'aperçu à droite, puis **Enregistrer**.

### Mistral · Agent (Le Chat)
1. Le Chat → créer un **Agent** : nom, description, **system prompt**.
2. Coller la **version complète** dans le system prompt. Possibilité d'attacher des documents de référence.

### Infomaniak · souverain (recommandé pour les données sensibles)
- **AI Tools / AI Services** (API compatible OpenAI, modèles open source hébergés en Suisse) : définir le **system prompt** avec la **version complète**.
- **Euria** (assistant souverain, kSuite/kChat) : créer une conversation orientée avec la **version courte** comme prompt de configuration.
- Intérêt : hébergement 100 % suisse, cohérent avec le garde-fou anti-Shadow AI de la méthode.

### Claude
- **Projet Claude** (claude.ai) : coller la **version complète** dans les instructions du projet.
- **Claude Code** : ne pas utiliser ces fichiers, installer le skill natif (voir le [README principal](../README.md)), plus complet grâce à la divulgation progressive.

## Maintenance

La **source canonique** de la méthode est le socle Palambur ; dans ce dépôt, le skill Claude Code (`skills/palambur-method/`) en est la mise en œuvre de référence. Ces prompts en sont une **photographie condensée** : après une évolution du skill, les régénérer pour éviter la dérive.
