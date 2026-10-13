# Méthode Palambur · skill `palambur-method`

[English](README.md) · Français · [Deutsch](README.de.md) · [Italiano](README.it.md)

[![Contrôle](https://github.com/PALAMBUR/palambur-method/actions/workflows/controle.yml/badge.svg)](https://github.com/PALAMBUR/palambur-method/actions/workflows/controle.yml) [![Licence MIT](https://img.shields.io/badge/licence-MIT-blue)](LICENSE) [![Version](https://img.shields.io/github/v/release/PALAMBUR/palambur-method)](https://github.com/PALAMBUR/palambur-method/releases) [![Security: A · Skills Directory](https://www.skillsdirectory.com/api/skills/palambur-palambur-method/badge)](https://www.skillsdirectory.com/skills/palambur-palambur-method)

**Un skill qui pose les bonnes questions avant d’écrire.** Vous demandez un document de travail à une IA (offre d’emploi, devis, relance, contrat, note interne). Au lieu de deviner ce qui manque et d’inventer le reste, le skill vous pose quatre questions courtes au plus, une à la fois, puis rend un document que vous pouvez envoyer. Pensé pour les entreprises de Suisse romande, utilisable partout. Gratuit, licence MIT.

---

<a id="essayer"></a>
## Essayer en deux minutes

**Claude Code** · deux commandes dans la conversation, puis une demande.

```
/plugin marketplace add PALAMBUR/palambur-method
```

```
/plugin install palambur@palambur
```

Puis tapez : `méthode palambur : fais une offre d’emploi pour un peintre à 80 %`

**Dans votre navigateur** (Claude.ai, ChatGPT, Euria d’Infomaniak, Mistral…) · ouvrez [`adaptations/methode-palambur-prompt.md`](adaptations/methode-palambur-prompt.md), copiez **le bloc sous le trait**, collez-le dans les instructions de votre projet ou de votre assistant. Rien à installer. Pour une boîte d’instructions limitée en taille, prenez le [prompt court](adaptations/methode-palambur-prompt-court.md).

**Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe** · un seul lien symbolique du dossier `skills/palambur-method/` dans `~/.agents/skills/` suffit aux cinq hôtes. Les commandes, hôte par hôte, sont dans [`docs/portabilite/INSTALLATION.md`](docs/portabilite/INSTALLATION.md).

**Vérifier que le skill est chargé** · dans Claude Code, `/plugin` puis l’onglet **Installed** ; ou, sur n’importe quel hôte, demandez « méthode palambur : quelle est ta première question ? » et attendez une réponse qui commence par « Question 1 sur N ».

---

## Sommaire

- [Essayer en deux minutes](#essayer)
- [Avant / après, en 30 secondes](#avant-apres)
- [Ce que c’est](#ce-que-c-est)
- [Déclenchement · trois portes](#declenchement)
- [Installation](#installation)
- [Structure du dépôt](#structure)
- [Mesures et épreuves](#mesures)
- [Engagements](#engagements)
- [Contribuer](#contribuer) · [Citer](#citer) · [Licence](#licence)

---

<a id="avant-apres"></a>
## Avant / après, en 30 secondes

![Les quatre questions, puis le Gabarit et le Livrable](docs/demo-quatre-questions.svg)

**Ce que vous écrivez :**

> méthode palambur : fais une offre d’emploi pour un peintre à 80 %

**Ce que le skill répond.** Au premier déclenchement, trois lignes d’ouverture, le niveau de sensibilité, puis la première question, dans le même message :

> **Méthode Palambur.** Je vais d’abord vous poser quelques questions, une à la fois, pour ne rien inventer à votre place.
> Vous répondez par une lettre ou en texte libre ; si vous passez, une valeur prudente s’applique et reste visible.
> Vous recevrez ensuite deux blocs à copier : le **Gabarit Palambur**, réutilisable, puis le **Livrable**.
>
> Niveau de sensibilité · ordinaire (aucun nom, aucun montant)
>
> **Question 1 sur 4 · le lieu et le cadre**
>
> Où se trouve le poste, et dans quel cadre ?
>
> A. un seul lieu de travail, canton à nommer
> B. plusieurs sites ou déplacements réguliers
> C. télétravail partiel possible, part à préciser
> D. Autre / je ne sais pas · défaut si vous ne précisez pas

Puis, **une question par message**, toujours avec un compteur, des choix lettrés, un défaut prudent signalé et une échappatoire :

> **Question 2 sur 4 · les missions** · A. je les fournis · B. proposez les missions courantes du métier, je corrige · défaut si vous ne précisez pas · C. le poste est nouveau, les missions ne sont pas encore arrêtées · D. Autre / je ne sais pas

> **Question 3 sur 4 · le profil** · A. un titre exigé (CFC, brevet, maîtrise) · B. CFC ou expérience équivalente reconnue · défaut si vous ne précisez pas · C. aucun titre exigé, formation interne assurée · D. Autre / je ne sais pas

> **Question 4 sur 4 · ce que l’entreprise offre** · A. rien au-delà du cadre contractuel et conventionnel · défaut si vous ne précisez pas · B. des avantages à nommer · C. des avantages à nommer et une fourchette salariale brute publiée · D. Autre / je ne sais pas

Réponses retenues pour l’exemple : A (canton de Vaud, atelier à Yverdon-les-Bains), B, A (CFC de peintre en bâtiment), B (13e salaire et formation continue). Si vous choisissez « je ne sais pas », le champ reste `[À COMPLÉTER]` dans le document.

**Ce que vous recevez.** D’abord **une ligne de contexte**, qui dit ce qui a été retenu :

> Contexte retenu · offre d’emploi · peintre en bâtiment à 80 % · canton de Vaud · ton factuel · données : aucune · 4 réponses, 0 défaut, 10 marqueurs

Puis le **Gabarit Palambur rempli**, le prompt réutilisable (extrait) :

```
Gabarit Palambur

INSTRUCTION
Rédigez une offre d’emploi complète pour un poste de peintre en bâtiment à
80 %, destinée à être publiée sur [À COMPLÉTER : canaux]. Objectif : obtenir
des candidatures qualifiées en disant le travail réel, le lieu, l’horaire et
le cadre, sans rien promettre qui n’ait été validé par la direction.

RÔLE ET AUDIENCE
Vous êtes chargé·e de recrutement chez Exemple SA, entreprise de peinture en
bâtiment du canton de Vaud, formé·e au CO, à la LEg, à la LTr et à la nLPD.
Vous écrivez pour une personne du métier qui lit l’annonce sur son téléphone.

DONNÉES
• Intitulé du poste : peintre en bâtiment (h/f/d)
• Lieu de travail et canton : atelier d’Yverdon-les-Bains, chantiers dans le
  canton de Vaud
• Taux · type de contrat · date d’entrée : 80 % · durée indéterminée · à convenir
• Profil indispensable : CFC de peintre en bâtiment
• Avantages validés par la direction : 13e salaire · formation continue
• Convention collective applicable, si connue : [À COMPLÉTER]

CONTRAINTES
Aucun critère discriminatoire (LEg, CO), neutralité de genre (h/f/d). Aucun
salaire, aucune durée de vacances inventés. Aucun article de loi cité : si une
CCT s’applique, nommez-la et posez [À VÉRIFIER : CCT applicable].

FORMAT
Six sections : titre et accroche · l’entreprise · vos missions · votre profil ·
ce que nous offrons · postuler. 400 à 600 mots. Vouvoiement, français de
Suisse romande. Mention de traitement des données en fin d’annonce.
```

Puis le **Livrable** (extrait) :

> **Peintre en bâtiment CFC (h/f/d) · 80 % · Yverdon-les-Bains**
>
> Vous aimez le travail soigné et les chantiers de rénovation ? Exemple SA cherche un·e peintre en bâtiment à 80 %, entrée en fonction à convenir.
>
> **Vos missions** [À VALIDER : liste proposée, à corriger par la direction] · préparation des supports, peinture intérieure de logements et de bureaux, pose de revêtements muraux, finitions, conseil au client sur place.
>
> **Votre profil** · indispensable : CFC de peintre en bâtiment · souhaité : [À COMPLÉTER : années d’expérience], permis de conduire [À COMPLÉTER : catégorie].
>
> **Ce que nous offrons** · 13e salaire · formation continue prise en charge.
>
> **Postuler** · envoyez votre dossier à [À COMPLÉTER : fonction du destinataire] par [À COMPLÉTER : canal].
>
> *Vos données de candidature sont traitées par Exemple SA au moyen de [À COMPLÉTER : outil], hébergé [À COMPLÉTER : pays], et conservées [À COMPLÉTER : durée].*

Et, pour clore, le **Journal de confiance**, cinq lignes qui disent ce qui a été protégé, marqué et refusé :

```
Journal de confiance
· Niveau de sensibilité · ordinaire (aucune personne nommée)
· Données · aucune
· Marqueurs posés · [À COMPLÉTER] ×7 · [À VÉRIFIER] ×2 (CCT applicable, annonce du poste) · [À VALIDER] ×1 (missions)
· Hypothèses refusées · aucun salaire chiffré ; aucune CCT nommée de mémoire ; aucun lieu d’hébergement des données affirmé
· Relecture humaine · requise avant publication (livrable RH)
```

Ce qui n’a pas été dit n’a pas été inventé : il reste marqué. Si votre demande contient des **noms de clients ou des montants**, le skill demande d’abord, en une question seule, s’il doit les anonymiser (c’est le réglage par défaut). L’échange complet est dans [`docs/exemples/01-offre-emploi.md`](docs/exemples/01-offre-emploi.md) ; neuf autres déroulés, un par gabarit, sont dans [`docs/exemples/`](docs/exemples/).

---

<a id="ce-que-c-est"></a>
## Ce que c’est

**Deux noms, deux objets.** *La Méthode Palambur* est l’ensemble : la discipline de clarification, les garde-fous suisses, l’anti-invention. *Le Gabarit Palambur* en est l’outil : les **5 blocs** ordonnés d’un prompt, Instruction · Rôle et audience · Données · Contraintes · Format, plus 4 blocs d’extension pour les livrables à fort enjeu (contrat, charte, politique interne).

Le skill transforme une demande métier **sous-spécifiée** en **livrable de qualité**, en comblant le contexte manquant *avant* de produire. Il anticipe en interne un lot d’au plus quatre questions déterminantes (lieu et cadre, missions, profil, avantages…), mais n’en pose **qu’une par message**, avec un compteur (« Question 1 sur 4 »), un défaut prudent signalé et une échappatoire « Autre / je ne sais pas ». Puis il livre :

1. le **Gabarit Palambur rempli**, prêt à copier-coller et à réutiliser ;
2. le **Livrable** rédigé, avec les garde-fous suisses (LEg, nLPD, CO, LTr, souveraineté des données), fermé par un Journal de confiance.

**Trois promesses.**

- **Fluide** · peu de questions, bien ciblées, quatre par lot au plus. Si tout est déjà fourni, il produit directement.
- **Sûr** · protection des données par défaut (anonymisation, mention nLPD), aucune donnée inventée, aucun numéro d’article de loi écrit sans la marque `[À VÉRIFIER]`.
- **Silencieux** · ce skill n’envoie rien, nulle part. Pas de télémétrie, pas de serveur Palambur, pas de compte. Ce sont des fichiers texte que votre IA lit.

**Un profil d’entreprise, pour ne pas répondre deux fois.** Le skill lit un fichier `profil-entreprise.md` placé à la **racine de votre dossier de travail** : canton, convention collective, ton, signature, langue. Ses champs remplis valent réponses, et les questions qu’il tranche ne vous sont plus posées. Le modèle à copier est dans le skill : [`skills/palambur-method/profil-entreprise.md`](skills/palambur-method/profil-entreprise.md).

**Et un mode relecture.** Vous joignez un texte déjà écrit (une lettre de licenciement, un devis) et demandez de le relire : aucune question, un tableau « Constat · Risque · Correction proposée », puis la version corrigée. La relecture corrige la forme, le droit et les données ; elle ne réécrit pas le fond ([`relecture.md`](skills/palambur-method/relecture.md)).

<a id="declenchement"></a>
## Déclenchement · trois portes

Une seule suffit.

1. **Le mot** · votre message contient **« palambur »**, **« méthode palambur »** ou **« palambur method »**.
2. **La nature de la demande** · un document de travail demandé en une ou deux phrases (offre d’emploi, devis, relance, contrat, note interne…), un contexte d’entreprise suisse, des noms ou des montants à protéger, ou un texte joint à relire.
3. **L’option « toujours actif »** · écrivez **« Méthode Palambur toujours active »** dans la conversation ou dans votre `CLAUDE.md`, et le skill s’applique à tout ce que l’IA rédige, jusqu’à « Méthode Palambur désactivée ».

Une fois déclenché : s’il manque des éléments déterminants, il **clarifie** ; si tout est fourni, il produit directement ; si un texte est joint pour relecture, il relit sans poser de question.

Les fichiers du skill sont écrits en **français**. Les questions et le livrable suivent la langue de votre demande.

---

<a id="installation"></a>
## Installation

### Prérequis

- **Pour utiliser le skill** · un hôte qui lit le format `SKILL.md` (Claude Code à jour, Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe) ou n’importe quelle IA dotée d’une boîte d’instructions. Rien d’autre.
- **Pour les outils du dépôt** (contrôle, épreuves, générateurs) · Python 3.9 ou plus récent. Facultatif : vous n’en avez pas besoin pour utiliser le skill.

### Claude Code · plugin

Dans Claude Code, ajoutez ce dépôt comme marketplace :

```
/plugin marketplace add PALAMBUR/palambur-method
```

Puis installez le plugin :

```
/plugin install palambur@palambur
```

Les mises à jour arrivent avec chaque **nouvelle version** du plugin ; `/plugin` puis **Installed** montre celle que vous avez.

### Copie locale · `outils/installer_local.sh`

Si vous préférez une copie dans `~/.claude/skills/` sans passer par le marketplace, clonez le dépôt puis lancez le script. À blanc par défaut, il montre ce qu’il ferait :

```bash
bash outils/installer_local.sh
```

Avec `--ecrire`, il pose réellement la copie :

```bash
bash outils/installer_local.sh --ecrire
```

Le script **refuse** si la cible est déjà un lien symbolique, pour ne pas écrire dans un autre clone à travers le lien.

### Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe · `.agents/skills`

Le format `SKILL.md` est un **standard ouvert**. Un seul lien symbolique du dossier `skills/palambur-method/` dans `~/.agents/skills/` suffit à cinq hôtes : **Codex** (qui suit les liens symboliques et lit aussi `.agents/skills/` dans un projet), **Cursor**, **GitHub Copilot**, **Gemini CLI** et **Mistral Vibe CLI** (documentation officielle de chaque éditeur, relevée le 11.10.2026). Gemini (application) et Mistral Vibe Work acceptent le skill par téléversement. Le guide pas à pas, hôte par hôte, avec ses sources datées, est dans [`docs/portabilite/INSTALLATION.md`](docs/portabilite/INSTALLATION.md) ; la conformité du skill au standard est relevée dans [`docs/portabilite/CONFORMITE_STANDARD.md`](docs/portabilite/CONFORMITE_STANDARD.md).

### Boîtes d’instructions · Projet Claude.ai, Euria, autres assistants

Pour les hôtes qui n’offrent qu’une **boîte d’instructions système**, le dossier [`adaptations/`](adaptations/) fournit la méthode condensée en un prompt autonome, **généré depuis le skill lui-même** à chaque version : une [version complète](adaptations/methode-palambur-prompt.md) sous 8'000 caractères et une [version courte](adaptations/methode-palambur-prompt-court.md) sous 1'500 caractères. Sur ces hôtes, l’assistant *est* la méthode : elle s’applique à chaque demande, sans mot déclencheur. Le tableau « quel hôte, quelle version, où coller » est dans [`adaptations/README.md`](adaptations/README.md).

**Une vérité, le dépôt.** Le skill n’a qu’une source : `skills/palambur-method/` dans ce dépôt. Ce que les hôtes lisent (`~/.claude/skills/`, `~/.agents/skills/`, un plugin installé, un prompt collé) est **un lien ou une copie datée**, qui se met à jour par `git pull` ou par une nouvelle version du plugin, **jamais en éditant les fichiers sur place** : une correction faite dans une copie est perdue à la mise à jour suivante, et personne ne la relit.

---

<a id="structure"></a>
## Structure du dépôt

```
palambur-method/
├── README.md · README.fr.md · README.de.md · README.it.md   # ce fichier, en quatre langues
├── CHANGELOG.md · CONTRIBUTING.md · CODE_OF_CONDUCT.md      # versions, contributions, conduite
├── SECURITY.md · CITATION.cff · LICENSE                     # signalement, citation, MIT
├── .claude-plugin/          # plugin.json et marketplace.json · le plugin Claude Code
├── .github/                 # modèles de tickets, modèle de PR, workflows/controle.yml (CI)
├── .agents/skills/palambur-method/   # emplacement Codex et hôtes .agents · un README, le lien se pose chez vous
├── skills/palambur-method/  # LE SKILL · la seule source
│   ├── SKILL.md             # quand se déclencher, les étapes 0 à 4, la forme des questions
│   ├── methode-palambur.md  # le Gabarit (5 + 4 blocs), les 4 niveaux, le ton, trois parcours
│   ├── protection-donnees.md   # niveaux de sensibilité, anonymisation, journal de confiance
│   ├── relecture.md         # le mode relecture · six cribles, tableau de sortie
│   ├── references-juridiques.md   # les textes que le skill peut nommer, ce qu’il n’invente jamais
│   ├── profil-entreprise.md # le modèle du profil d’entreprise lu à la racine du dossier de travail
│   ├── gabarits/            # un fichier par livrable fréquent (questions, champs DONNÉES, pièges)
│   ├── metiers/             # un fichier par métier (vocabulaire, textes de loi nommés, pièges)
│   └── agents/openai.yaml   # métadonnées facultatives lues par Codex
├── adaptations/             # les prompts système générés · complet (sous 8'000 caractères) et court
├── docs/
│   ├── exemples/            # dix déroulés complets, un par gabarit, données fictives
│   ├── pedagogie/           # MANIFESTE.md, FAQ.md, GLOSSAIRE.md
│   ├── portabilite/         # INSTALLATION.md (hôte par hôte), CONFORMITE_STANDARD.md
│   ├── VEILLE_JURIDIQUE.md  # ce qui alimente la table des références juridiques
│   └── DIX_COMMANDEMENTS.md # la protection des données en dix lignes
├── epreuves/                # 149 cas (cas.json), grille.md, mesurer.py, generer_evals.py,
│                            # jouer_apertus.py, résultats et protocole, reponses/ (transcriptions)
├── evals/                   # README seulement · les cas « claude plugin eval » se régénèrent
└── outils/                  # controle.py, generer_adaptations.py, installer_local.sh, regle_typo.py, metiers/
```

Les dossiers `gabarits/` et `metiers/` se complètent au fil des versions ; le [journal des versions](CHANGELOG.md) dit ce qui est posé, avec une note de qualité par version. Les [dix commandements](docs/DIX_COMMANDEMENTS.md) tiennent la protection des données en une page ; la [FAQ](docs/pedagogie/FAQ.md), le [manifeste](docs/pedagogie/MANIFESTE.md) et le [glossaire](docs/pedagogie/GLOSSAIRE.md) répondent aux questions qui reviennent. Les README en [allemand](README.de.md) et en [italien](README.it.md) attendent une **relecture native**.

---

<a id="mesures"></a>
## Mesures et épreuves

**La chaîne de contrôle** vérifie le dépôt avant chaque publication : règle typographique, mot interdit, JSON valides, numéro de version unique dans trois fichiers, adaptations à jour sur leurs sources, frontmatter et taille de `SKILL.md`, liens relatifs. Elle tourne sur n’importe quel clone et dans la CI (`.github/workflows/controle.yml`), sans secret ni appel de modèle :

```bash
python3 outils/controle.py
```

Le contrôle **se casse lui-même** sur des témoins fabriqués, pour prouver qu’il regarde :

```bash
python3 outils/controle.py --epreuve
```

**Les épreuves du skill** (est-il fluide, est-il sûr ?) sont dans [`epreuves/`](epreuves/) : **149 cas** en trois familles (livrables, tâches métier, pièges qui poussent à inventer · relevé du 11.10.2026, `python3 epreuves/mesurer.py --compter` fait foi), une [grille de notation](epreuves/grille.md) à vingt gardes, et `mesurer.py`, qui note une réponse contre la grille et sait lui aussi se casser (`--epreuve`). Les mêmes cas au format `claude plugin eval` se **régénèrent** depuis `epreuves/cas.json` avec `python3 epreuves/generer_evals.py` ; ils ne sont plus versionnés, [`evals/README.md`](evals/README.md) dit comment les lancer.

**La mesure publiée.** Mesuré le 12.10.2026 sur Apertus (Infomaniak) avec le **prompt d’adaptation complet**, pas le skill natif : **1 vert sur 149**. Le modèle pose la question d’anonymisation, puis livre le Gabarit et le livrable dans le même message, sans clarifier et sans marqueurs. Détail, gardes rouges par famille et dépense exacte dans [`epreuves/RESULTATS_APERTUS_2026-10-11.md`](epreuves/RESULTATS_APERTUS_2026-10-11.md). **Le skill natif sur Claude n’a pas encore été mesuré** ; le [journal des versions](CHANGELOG.md) portera sa note de qualité le jour où il l’aura été.

---

<a id="engagements"></a>
## Engagements

- **Le skill de base est gratuit et le restera.** Licence MIT : vous pouvez l’utiliser, le copier, le modifier, y compris dans un cadre commercial. **Le skill de base, c’est tout ce dépôt** : la méthode, les gabarits, les fiches métier, les épreuves, et chaque version qui suivra. Palambur vend du **service autour** (une version pré-réglée pour une entreprise, une installation accompagnée) ; rien de ce qui est ici ne devient payant.
- **Il n’envoie rien, nulle part.** Aucune télémétrie, aucun appel réseau, aucun compte. Vos demandes restent entre vous et l’IA que vous avez choisie.
- **Pas de publicité dans le skill.** Les livrables ne portent aucune mention Palambur. Le skill nomme **un seul outil Palambur, Jomini** (anonymisation gratuite dans le navigateur, sans compte), parce qu’il sert la protection des données ; c’est la seule mention. Ce qui suit est l’autre exception, et elle est ici, pas dans le skill.

Le skill est la porte, [Chaptal](https://palambur.ch) la maison : **782 pistes métier** au Gabarit Palambur, prêtes à l’emploi, sur palambur.ch (relevé du 11.10.2026).

---

<a id="contribuer"></a>
## Contribuer

Un gabarit manquant, une correction juridique, une nouvelle langue : [`CONTRIBUTING.md`](CONTRIBUTING.md) dit comment proposer, ce que la chaîne de contrôle exige et la **règle du locuteur natif** pour les traductions. Le [code de conduite](CODE_OF_CONDUCT.md) s’applique à tous les échanges ; une faille ou un comportement du skill qui expose des données se signale selon [`SECURITY.md`](SECURITY.md), pas dans un ticket public.

<a id="citer"></a>
## Citer

Pour citer la Méthode Palambur dans un travail, un cours ou un article, les **métadonnées de citation** sont dans [`CITATION.cff`](CITATION.cff) ; GitHub en propose la forme APA et BibTeX depuis la page du dépôt.

<a id="licence"></a>
## Licence

[MIT](LICENSE) · Palambur · Victor Semblanet · 2026
