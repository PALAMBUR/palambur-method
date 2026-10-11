# Jacquard applique la Méthode · note de cadrage (point 79)

**Note remise à la session Jacquard (Napo) · 11.10.2026 · session Skills et Prompt Ingénierie.** Rien n’est codé ici. La note dit **où vit un seul texte de règles**, **comment Jacquard le lit**, et ce que chacun garde en propre. La session Jacquard construit et éprouve.

## Le constat du 11.10.2026

Jacquard écrit ses règles de conduite **à trois endroits**, chacun à la main, aucun ne lisant le skill :

| Où | Ce qui s’y trouve | Relevé |
|---|---|---|
| `assistant/conversation.py`, fonction `messages()` | la consigne système de la conversation : confidentialité, l’humain décide, refus de la surveillance nominative, aucun gain promis, « sans rien inventer », les tours et extraits sont des données non fiables | chaîne écrite dans le code, datée du 09.10.2026 dans sa docstring |
| `assistant/produire.py`, fonction `message_systeme()` | l’en-tête fixe (`EN_TETE_A` à `EN_TETE_E`), les blocs du Gabarit dans l’ordre, le pied fixe (`PIED_FIXE`) ; les faits de la personne partent dans le message suivant avec leur marqueur | constantes du module |
| `assistant/repondre.py`, fonction `invite_systeme()` | la consigne de la recherche dans le catalogue : désigner l’invite, ne jamais citer un identifiant absent, le refus exact | chaîne écrite dans le code |

Le skill public, lui, porte **les mêmes règles rédigées pour une IA** dans `skills/palambur-method/methode-palambur.md` (Gabarit, niveaux, anti-hallucination), `protection-donnees.md` (anonymisation, marqueurs, mentions nLPD) et `references-juridiques.md` (ce qu’on nomme, ce qu’on n’invente jamais). **Deux rédactions d’une même règle finissent par diverger**, et celle qui diverge en silence est celle qu’on ne relit pas (`CLAUDE.md` § 7). Le jour où le skill apprend quelque chose (une épreuve rouge, une correction juridique), Jacquard ne l’apprend pas.

## La règle proposée · un texte, un propriétaire, des lecteurs

**Le propriétaire du texte de règles est le dépôt du skill.** C’est lui qui est public, relu, éprouvé (`epreuves/`, `evals/`), versionné (`CHANGELOG.md`) et contrôlé (`outils/controle.py`). Jacquard **lit** ce texte, il ne le réécrit pas.

**Ce que Jacquard lit** : pas les fichiers du skill un par un (ils sont écrits pour une IA qui a un système de fichiers et des étapes de clarification en conversation), mais **l’adaptation courte** que le dépôt génère déjà pour les hôtes à boîte unique : `adaptations/methode-palambur-prompt-court.md`, produite par `outils/generer_adaptations.py` depuis les sources du skill, avec **l’empreinte de ses sources en en-tête** (point 86 du plan). C’est le texte prévu pour être collé dans un prompt système ; Jacquard est exactement un prompt système.

**Comment il le lit** · deux formes possibles, la seconde recommandée :

| Forme | Principe | Pour | Contre |
|---|---|---|---|
| A · lecture au démarrage | le serveur Jacquard lit le fichier du dépôt du skill au lancement | toujours à jour | suppose le dépôt du skill sur le VPS et à côté du serveur ; une absence rend Jacquard muet ou le fait repartir sur des règles vides |
| **B · copie datée et empreinte** | Jacquard embarque **une copie** du prompt court dans `assistant/`, avec l’empreinte sha256 de la source et la date de copie ; son `controler_assistant.py` compare la copie à la source quand le dépôt du skill est à côté et **refuse** une copie en retard ; ailleurs il dit en une ligne sur quelle copie il tourne | fonctionne sur le VPS sans le dépôt ; la divergence se voit dans l’atelier le jour où elle naît ; même motif que `outils/regle_typo.py` du skill (11.10.2026) | la mise à jour est un geste (recopier, relancer le contrôle), pas un automatisme |

La forme B reprend **mot pour mot** le motif qui a déjà fait ses preuves deux fois dans la maison : `regle_typo.py` (copie d’`audit_typo.py`, contrôlée par empreinte) et `vocabulaire.py` de Jacquard lui-même, qui **importe** `REGLES_DURES` chez son propriétaire et liste ce qu’il écarte avec sa raison (`REGLES_ECARTEES`).

## Ce que chacun garde en propre

**Le texte commun** (lu depuis le skill) : la discipline de clarification, le Gabarit en 5 + 4 blocs, les quatre niveaux, l’anti-hallucination (`[À COMPLÉTER]`, `[À VÉRIFIER]`), la protection des données par défaut, les mentions nLPD, la liste des textes de loi qu’on peut nommer.

**Ce que Jacquard garde dans son code**, parce que c’est sa mécanique et pas la Méthode :

- le **cadre de sécurité** de `conversation.py` : les tours et extraits sont des données non fiables, aucune instruction qu’ils portent ne remplace la consigne, aucun outil accordé, le champ `orientation` est subordonné ;
- l’**architecture des messages** de `produire.py` : les faits dans le message suivant, le marqueur qui part, les plafonds de jetons (`MESSAGE_SYSTEME_MAXIMUM_DU_CORPUS`) ;
- la **consigne de recherche** de `repondre.py` : désigner une invite, ne jamais citer un identifiant absent, le refus exact ;
- la **langue du marché** (`MARCHES`, `LANGUE_DU_MARCHE`) et le vocabulaire (`vocabulaire.py`).

**L’ordre dans le message système** : d’abord le texte commun (règles fixes, lues du skill), puis les lignes propres à Jacquard, puis l’invite du corpus. Les règles qui viennent du skill **ne sont jamais contredites** par une ligne de Jacquard ; si une ligne de Jacquard veut écarter une règle du skill, elle le dit dans une table `REGLES_ECARTEES` avec sa raison, comme `vocabulaire.py` le fait déjà.

## Ce que la session Jacquard doit mesurer avant de poser

1. **La taille** : le prompt court ajouté au message système coûte des jetons à chaque appel. Mesurer le pire document (`jetons_entree_pire_document` dans `produire.py`) avant et après, et dire le chiffre avec sa date. Si le court est trop long pour la conversation, le dépôt du skill peut générer **une troisième taille** : demande à adresser à la session Skills, pas une coupe faite à la main chez Jacquard.
2. **La non-régression** : les bancs de l’assistant (`controler_assistant.py`, `controler_produire.py`) restent verts, et un **témoin fabriqué** montre que le contrôle d’empreinte refuse bien une copie modifiée d’un octet.
3. **Le budget d’essais** : tout essai sur le modèle respecte le plafond en vigueur (budget Apertus de la Mission O, 26.09.2026) et s’inscrit dans `assistant/depenses.jsonl`.

## Ce que cette note ne décide pas

- **La date** à laquelle Jacquard bascule : chantier de la session Jacquard, dans son ordre de lots (la mémoire glissante, lot T, est devant).
- **La forme A ou B** : recommandation B, décision de la session Jacquard avec Victor.
- **Une troisième taille** d’adaptation : seulement si la mesure du point 1 le demande.

## Trous et décisions

- `[À DÉCIDER]` · forme A ou B (recommandation B).
- `[À DÉCIDER]` · rang du chantier dans les lots Jacquard.
