# Page `palambur.ch/methode/` · proposition de contenu (point 21)

**Brouillon · 11.10.2026 · session Skills et Prompt Ingénierie.** Rien n’est publié. La page appartient à la session **Site internet** : ce fichier propose le texte, il ne touche ni `src/vues/Methode.astro` ni `src/data/contenu-methode*.ts`. Les marqueurs `[À VÉRIFIER]` et `[À DÉCIDER]` sont volontaires et signalés ici : ils doivent disparaître avant la mise en ligne.

## Ce qui existe déjà (relevé du 11.10.2026)

La page `https://www.palambur.ch/methode/` **existe et répond 200** dans les cinq langues du site (`contenu-methode.ts`, `-en-US`, `-de-CH`, `-it-CH`, `-es`). Elle porte déjà : le constat, la discipline (A · B · C), le Gabarit en cinq blocs, les quatre garde-fous, les trois portes (Apprendre · Exécuter · Copier), une section `#depot` qui renvoie vers `github.com/PALAMBUR/palambur-method`, et un appel final vers la formation et l’audit.

**Ce qui lui manque pour remplir le point 21 du plan** : l’exemple avant/après vivant, la commande d’installation, les liens vers les autres hôtes, la promesse (gratuit, sans télémétrie). La proposition ci-dessous **complète la section `#depot`** et ajoute **une section « L’exemple »** entre « La discipline » et « Le Gabarit ». Le reste de la page ne bouge pas.

## Titre et accroche (inchangés, pour mémoire)

- **Titre** (déjà en ligne) : « Cadrer l’IA **avant** de produire ».
- **Accroche** (déjà en ligne) : « Une IA qui hallucine, c’est une IA qui n’a pas reçu un cadre assez serré. »

Aucun changement proposé sur le hero : le titre est bon, il porte déjà la Méthode.

## Nouvelle section · « L’exemple » (à insérer après « La discipline »)

**Étiquette** : L’exemple

**Titre H2** : Trente secondes, **une demande**, quatre questions

**Lead** : Voici ce que la Méthode change sur une demande ordinaire. À gauche, ce qu’on tape d’habitude. À droite, ce que l’outil fait avant d’écrire la première ligne.

### Colonne « Avant » (la demande brute)

> « fais une offre d’emploi pour un peintre à 80 % »

**Sous la demande** : Un modèle répond tout de suite. Il choisit lui-même le canton, le type de contrat, la date d’entrée, les avantages, et parfois une convention collective. **Tout est plausible, rien n’est vérifié.**

### Colonne « Après » (les quatre questions, une par message, avec compteur)

**Question 1 sur 4** · Dans quel canton le poste est-il basé ?
A. Neuchâtel · B. Vaud · C. Genève · D. Autre / je ne sais pas (défaut prudent : « Suisse romande », sans canton nommé)

Les trois questions suivantes ont la même forme : des choix lettrés, et la dernière lettre est toujours l’échappatoire « Autre / je ne sais pas », qui laisse un crochet `[À COMPLÉTER]` dans le livrable plutôt qu’une valeur inventée.

**Question 2 sur 4** · Quelles sont les trois à cinq missions principales ? (défaut : missions types d’un peintre en bâtiment, marquées à relire)

**Question 3 sur 4** · Quel profil cherchez-vous ? CFC exigé, expérience minimale, permis de conduire ? (défaut : CFC ou équivalent, permis non exigé)

**Question 4 sur 4** · Quels avantages peut-on annoncer ? 13e salaire, LPP au-delà du minimum, formation, horaires ? (défaut : aucun avantage annoncé plutôt qu’un avantage inventé)

**Sous les questions** : Le canton change le salaire de référence et la convention applicable. Les missions changent le texte. Le profil change le filtre. Les avantages changent le taux de réponse. **Aucune de ces quatre réponses ne peut être devinée.**

### Extrait du livrable (après les réponses)

> **Peintre en bâtiment CFC · 80 % · [Canton] · entrée [date ou « à convenir »]**
>
> Vous préparez les supports, appliquez les peintures et les enduits, et assurez les finitions sur des chantiers de rénovation. Vous travaillez en équipe de deux à quatre personnes, sous la responsabilité d’un chef d’équipe.
>
> **Profil** · CFC de peintre ou titre jugé équivalent · trois ans d’expérience en rénovation · permis de conduire [À COMPLÉTER : exigé ou souhaité].
>
> **Ce que nous offrons** · [À COMPLÉTER : avantages confirmés par l’employeur, aucun n’est annoncé par défaut].
>
> Poste ouvert à toutes et à tous. Vos données sont traitées en Suisse, conformément à la nLPD.

**Note sous l’extrait** : Les crochets ne sont pas un oubli. **C’est ce qui manque, écrit manquant**, pour que la relecture le voie. Aucune convention collective n’est citée tant qu’elle n’est pas confirmée.

**Rendu proposé** : deux colonnes au bureau, empilées au téléphone, dans la base claire des pubs d’outils (fond `#F8FAFC` quadrillé, barre rouge, logo marine). Les quatre questions en cartes numérotées, le compteur en petites capitales. La session Site tranche la forme.

## Section `#depot` complétée · « Installer la Méthode »

Le texte actuel (« La Méthode est publiée, donc vérifiable », `p1`, `p2`, trois principes) **reste**. S’ajoute, sous le bouton « Voir le dépôt sur GitHub », un bloc d’installation en quatre lignes.

**Sous-titre** : Installer, **gratuitement**

**Paragraphe** : Le skill est publié sous licence MIT. Il est **gratuit**, il ne demande **aucun compte** Palambur, et il **n’envoie rien à Palambur** : aucune télémétrie, aucune donnée de vos demandes ne quitte votre outil pour venir chez nous. Ce que vous tapez reste entre vous et l’IA que vous avez choisie.

**Dans Claude Code** (deux blocs de code, une commande par bloc, dans l’ordre) :

```bash
/plugin marketplace add PALAMBUR/palambur-method
```

```bash
/plugin install palambur@palambur
```

L’identifiant `palambur@palambur` est celui que fixent `.claude-plugin/marketplace.json` et `plugin.json` (voir `portabilite/INSTALLATION.md`, § 1a). La **forme en ligne de commande (shell)**, hors conversation, est `claude plugin marketplace add PALAMBUR/palambur-method` puis `claude plugin install palambur@palambur` ; elle n’est pas montrée sur la page, parce que le public visé passe par la conversation et que `claude` n’est pas sur le `PATH` de toutes les machines (ce n’est pas le cas sur celle qui écrit ce brouillon). `[À VÉRIFIER par la session Site]` · rejouer les deux commandes `/plugin` sur une installation propre avant la mise en ligne.

**Ligne « Autres environnements »** (alignée sur la table de `portabilite/INSTALLATION.md`, relevé du 11.10.2026) : Le même skill se charge **tel quel** dans Codex, Cursor, Gemini CLI, GitHub Copilot et Mistral Vibe CLI (un seul dossier `~/.agents/skills/` suffit pour les cinq), ainsi que dans l’application Gemini et Mistral Vibe par téléversement du fichier `SKILL.md`. Pour un GPT personnalisé, un Projet Claude.ai ou Euria d’Infomaniak, qui n’offrent qu’une boîte d’instructions, la Méthode est fournie **en prompt à coller**, en version complète et en version courte. **Le guide par hôte** : `github.com/PALAMBUR/palambur-method/blob/main/portabilite/INSTALLATION.md`.

**Ligne de retenue** (petite, sous le bloc) : Le skill applique la Méthode. Il ne remplace ni une relecture humaine, ni un avis juridique.

## Ponts vers Chaptal et la formation (déjà présents, à resserrer)

Les trois portes existent. Deux phrases à ajuster pour que le pont soit explicite :

- **Porte « Copier »** (Chaptal) · texte actuel : « La bibliothèque de prompts métier, déjà écrits au Gabarit, garde-fous compris. C’est Chaptal. » **Ajout proposé** : « Le skill montre la Méthode sur une demande ; Chaptal la déploie **métier par métier**, sur [nombre relevé le jour de la mise en ligne] pistes déjà cadrées. » Le nombre se lit dans `prompts.jsonl` ce jour-là, jamais recopié d’ici (règle § 1 de `CLAUDE.md`). Lien actuel `#chaptal` à remplacer par `/chaptal/` ou `/trouver-la-bonne-demande/` (les deux répondent 200 le 11.10.2026) `[À DÉCIDER par la session Site : une seule adresse canonique]`.
- **Porte « Apprendre »** (formation) · texte actuel correct. **Ajout proposé** d’une phrase : « Le skill est gratuit ; **apprendre à le faire tenir dans une équipe**, c’est l’objet de la formation. » Lien `/formation-ia/` inchangé.

Aucun prix sur la page, ni pour la formation, ni pour Chaptal : le site ne publie pas de prix (règle du 04.08.2026, reconfirmée le 02.09.2026).

## Les cinq langues

La page existe en fr-CH, de-CH, it-CH, en-US et es, plus les trois variantes de marché (fr-FR, de-DE, it-IT) qui reprennent le contenu de leur langue mère. **Tout ce qui précède est à traduire par la session Site, règle : uniformité des langues** · la nouvelle section et le bloc d’installation apparaissent **dans chaque variante le même jour**, mise en page et fonction comprises, pas seulement le texte (arbitrage de Victor du 15.09.2026). L’exemple du peintre reste suisse dans toutes les langues ; seule la mention nLPD s’adapte au marché (fr-FR : RGPD) comme le fait déjà `contenu-methode-en-US.ts` pour son public `[À VÉRIFIER : comment la page anglaise traite aujourd’hui la mention nLPD]`.

## Ce qui exige Victor

1. **Go de publication** · le push sur `main` déploie le site (règle du 23.09.2026).
2. **Adresse canonique de Chaptal** sur la porte « Copier ».
3. **Validation de l’exemple** · le peintre à 80 % est l’exemple de référence du skill depuis le 12.07 ; le garder sur la page le rend reconnaissable d’un support à l’autre (README, posts, vidéo).

## Ce que cette proposition ne fait pas

Elle ne modifie pas le hero, le constat, les garde-fous ni l’appel final. Elle n’ajoute aucune capture d’écran : si la session Site veut un GIF de la clarification, il se tourne sur le skill de la version 1.0.0, pas sur la copie locale du 04.08 (en retard de trois mots interdits par la règle maison, corrigés sur GitHub le 24.09 · relevé du plan du 11.10.2026).
