# Conformité au standard Agent Skills · relevé du 11.10.2026

Référence : la spécification **Agent Skills** (`https://agentskills.io/specification`, consultée le 11.10.2026) et son dépôt de référence (`https://github.com/agentskills/agentskills`, validateur `skills-ref`). Fichier confronté : `skills/palambur-method/SKILL.md` **dans l’état du 11.10.2026 à 22 h 10** (174 lignes, un autre agent le réécrit en parallèle : un premier relevé à 21 h 30 donnait 169 lignes et une description de 1’103 caractères, corrigée depuis ; les mesures sont à rejouer avant publication, la commande est donnée en fin de document).

Ce rapport **ne modifie pas `SKILL.md`**. Il dit ce qui doit changer.

## Table de conformité

| Exigence (spécification) | Mesure | État | À faire |
|---|---|---|---|
| Fichier `SKILL.md` à la racine du dossier du skill | présent, `skills/palambur-method/SKILL.md` | **conforme** | rien |
| Frontmatter YAML ouvert par `---` en ligne 1 | ligne 1 = `---` | **conforme** | rien |
| `name` obligatoire, 1 à 64 caractères, minuscules, chiffres, traits d’union, sans trait d’union en tête, en queue ni doublé | `palambur-method`, 15 caractères, motif respecté | **conforme** | rien |
| `name` **égal au nom du dossier parent** | dossier `palambur-method` | **conforme** | rien |
| `description` obligatoire, non vide, **1 à 1’024 caractères** | **938 caractères** (relevé 22 h 10 ; 1’103 à 21 h 30) | **conforme** | ne plus dépasser 1’000 pour garder une marge ; rejouer la mesure avant chaque version |
| Champs facultatifs admis : `license`, `compatibility` (≤ 500), `metadata` (clés et valeurs texte), `allowed-tools` (expérimental) | présents : `license: MIT`, `metadata` (author, homepage, source) ; aucun champ hors liste | **conforme** | rien ; `compatibility` absent, c’est permis |
| Hors Claude Code (claude.ai, API), seuls `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` sont acceptés (source `code.claude.com/docs/en/skills`) | mêmes quatre champs | **conforme** | rien |
| Corps en Markdown, taille recommandée **moins de 5’000 jetons** | 2’522 mots, 15’530 caractères (22 h 10) ; estimation 3’800 à 4’450 jetons selon la règle (mots × 1,5 ou caractères ÷ 3,5) | **conforme, marge faible** (550 à 1’200 jetons) | ne plus allonger `SKILL.md` ; tout ajout va dans un fichier de référence |
| Claude Code recommande `SKILL.md` **sous 500 lignes** | 174 lignes (22 h 10) | **conforme** | rien |
| Fichiers de référence cités dans le corps **présents** | `methode-palambur.md`, `protection-donnees.md`, `references-juridiques.md`, `relecture.md` : les quatre existent | **conforme** (le 11.10 à 22 h 10 ; `references-juridiques.md` était absent à 20 h 30) | rien |
| Références **à un seul niveau de profondeur** depuis `SKILL.md` | tous à la racine du skill ; `gabarits/README.md` et `metiers/README.md` cités, un niveau | **conforme** | les dossiers `gabarits/` et `metiers/` existent dans le skill au relevé de 22 h 10 (posés par d’autres agents) ; le corps dit de poursuivre sans eux s’ils manquent |
| Dossiers recommandés `scripts/`, `references/`, `assets/` | aucun ; les fichiers de référence sont **à la racine** du skill | **recommandation non suivie** (ce n’est pas une exigence) | décision : déplacer les quatre `.md` dans `references/` et corriger les chemins dans `SKILL.md`, **ou** laisser tel quel. Si on déplace, `outils/generer_adaptations.py` et `outils/controle.py` lisent ces chemins et doivent suivre |
| Codex : `SKILL.md` **doit** contenir `name` et `description` ; liste des skills ≤ 2 % du contexte ou 8’000 caractères (source `learn.chatgpt.com/docs/build-skills`) | présents ; une description de 938 caractères consomme 12 % de ce budget à elle seule | **conforme** | ne pas rallonger |
| Claude Code : `description` + `when_to_use` **tronqués ensemble à 1’536 caractères** | 938, pas de `when_to_use` | **conforme** | rien |
| Gemini (app) : `name` en minuscules avec traits d’union, fichiers de référence en texte brut (source `support.google.com/gemini/answer/17094296`) | conforme ; cinq `.md` | **conforme** | rien |
| Cursor et claude.ai : `name` égal au nom du dossier | égal | **conforme** | rien |
| Validateur de référence `skills-ref validate` | **non exécuté** (Python 3.9, pas de `uv`, pas de PyYAML sur cette machine) | **à faire** | voir ci-dessous |
| Typographie maison (`audit_typo.py`) sur `SKILL.md` | « propre » au 11.10.2026 | **conforme** | rejouer après la réécriture |

**Bilan au relevé de 22 h 10** : **aucune non-conformité bloquante**. La `description`, non conforme à 21 h 30 (1’103 > 1’024), a été ramenée à 938 caractères par l’agent qui réécrit `SKILL.md`. Le reste est conforme ou relève d’une recommandation ; le point de vigilance est la **taille du corps**, qui a grossi de 1’100 caractères en quarante minutes.

## Ce que l’agent qui réécrit `SKILL.md` doit tenir

1. **Garder `description` sous 1’024 caractères**, idéalement sous 1’000 (938 aujourd’hui). La description sert au modèle pour **décider quand charger le skill**, pas pour le décrire exhaustivement.
2. **Ne plus allonger le corps** : la marge sous 5’000 jetons est de 550 à 1’200 jetons selon l’estimation, et elle a fondu pendant la session.
3. **Garder `name: palambur-method`** tel quel et ne pas renommer le dossier.
4. Si le choix tombe sur `references/`, **mettre à jour les quatre chemins** dans le corps et dans la table « Fichiers de référence », puis les outils de `outils/`.

## Rejouer la mesure

Depuis la racine du dépôt, un seul fichier à mesurer :

```bash
python3 -c "import re;t=open('skills/palambur-method/SKILL.md',encoding='utf-8').read();fm=t.split('---\n')[1];d=re.search(r'^description:\s*(.*)$',fm,re.M).group(1).strip();print('description',len(d),'caractères','OK' if len(d)<=1024 else 'TROP LONG')"
```

Validateur de référence (à installer une fois, dans un environnement Python ≥ 3.10) :

```bash
git clone https://github.com/agentskills/agentskills.git ~/agentskills
```

```bash
pip install -e ~/agentskills/skills-ref
```

```bash
skills-ref validate skills/palambur-method
```

Le dépôt de référence annonce ce validateur « à titre de démonstration » ; il reste l’arbitre le plus proche du texte de la spécification.

Côté Claude Code, le même contrôle pour le plugin complet (à la racine du dépôt, où `.claude-plugin/plugin.json` existe ; la condition « version 2.1.233 ou plus récente » de la documentation vaut pour valider un dossier **sans** manifeste, comme `~/.claude/skills`) :

```bash
claude plugin validate --strict .
```

Les deux validateurs **n’ont pas tourné le 11.10.2026** (`claude` hors `PATH`, Python 3.9). Leur sortie fera foi sur ce rapport.

## Sources

- Spécification Agent Skills : `https://agentskills.io/specification` (11.10.2026). Liste des hôtes compatibles : `https://agentskills.io/clients`.
- Dépôt de référence et validateur : `https://github.com/agentskills/agentskills` (11.10.2026).
- Claude Code, skills : `https://code.claude.com/docs/en/skills` (11.10.2026).
- Codex, skills : `https://developers.openai.com/codex/skills` → `https://learn.chatgpt.com/docs/build-skills` (11.10.2026).
- Cursor : `https://cursor.com/docs/context/skills` (11.10.2026).
- Gemini (app) : `https://support.google.com/gemini/answer/17094296` (11.10.2026).
