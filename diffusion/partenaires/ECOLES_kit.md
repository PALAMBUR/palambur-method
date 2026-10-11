# Écoles · kit « matériel de cours » (point 67)

**Brouillon · rien n’est envoyé · go Victor.** Préparé le 11.10.2026. Aucune école contactée. Les organisations sont celles vérifiées dans `../RELAIS_ROMANDS.md` (relevé du 11.10.2026, non recopié) ; **aucune personne n’est nommée**, seulement des fonctions.

## L’idée

Une haute école de gestion ou une école de commerce cherche des objets pédagogiques **réels** pour enseigner l’IA générative : pas un exercice inventé, un dépôt public, versionné, avec ses épreuves et sa chaîne de contrôle, qu’un étudiant peut lire, critiquer et améliorer par une contribution. La Méthode Palambur en est un. Le kit ci-dessous donne à un enseignant **tout ce qu’il faut pour une séance de 90 minutes**, sans rien demander à Palambur, et sans que Palambur vende quoi que ce soit en classe.

## Le kit · ce qu’il contient et où c’est

| Pièce | Rôle dans le cours | Où (dans le dépôt) | État au 11.10.2026 |
|---|---|---|---|
| **Le manifeste** « Pourquoi questionner avant de produire » | lecture préalable, 1 page, FR puis EN | `pedagogie/MANIFESTE.md` | **en préparation** (paquet 4, point 57) · ce kit le cite, il ne l’écrit pas |
| **L’exemple avant/après** du peintre à 80 % | la démonstration d’ouverture | `README.md`, section « Avant / après, en 30 secondes » | posé |
| **Dix exemples complets** (demande brute → questions → deux blocs) | corpus d’analyse | `exemples/` | **en préparation** (paquet 4, point 58) |
| **Les vingt cas d’épreuve** et la grille de notation | matière de l’exercice, barème | `epreuves/cas.json`, `epreuves/grille.md` | posés, **non joués** (dépense modèle non autorisée) |
| **Les gabarits** (offre d’emploi, devis, relance, contrat de travail, certificat…) | ce que les étudiants font produire | `skills/palambur-method/gabarits/` | 10 fichiers posés |
| **Le skill lui-même** et le guide d’installation | pour que chaque étudiant l’ait sur son poste | `skills/palambur-method/`, `portabilite/INSTALLATION.md` | posés |
| **Le prompt à coller** pour un étudiant sans Claude Code | même séance, sur un Projet Claude.ai, un GPT ou Euria | `adaptations/methode-palambur-prompt.md` | généré |
| **Le lien « sans rien installer »** | la voie la plus courte | Projet Claude.ai partagé (`PROJET_CLAUDE_AI.md`) | **à créer par Victor** |

## La séance de 90 minutes · déroulé pour l’enseignant

**Objectif** : à la fin, l’étudiant sait dire **pourquoi** un modèle de langage invente, **comment** une méthode de clarification l’en empêche, et il a **mesuré** la différence sur un cas.

| Minute | Séquence | Matériel |
|---|---|---|
| 0 à 10 | **La panne.** Chacun colle « fais une offre d’emploi pour un peintre à 80 % » dans l’assistant de son choix, sans méthode. Lister au tableau tout ce que le modèle a décidé seul (canton, contrat, date, avantages, convention collective). | aucun |
| 10 à 25 | **Le pourquoi.** Lecture du manifeste. Discussion : une invention plausible se voit-elle à la relecture ? Qui signe le document ? | `pedagogie/MANIFESTE.md` |
| 25 à 40 | **La méthode.** La même demande avec le skill ou le prompt collé : quatre questions, une par message, compteur, lettres, défaut prudent ; puis deux blocs. Comparer avec le tableau de la minute 10. | `README.md`, skill ou `adaptations/` |
| 40 à 70 | **L’exercice.** Par binôme : tirer un cas de `epreuves/cas.json`, le jouer **avec** et **sans** la méthode, noter les deux réponses avec `epreuves/grille.md`. Un binôme sur quatre tire un cas **piégé** (loi inexistante, montant à deviner). | `epreuves/` |
| 70 à 85 | **Restitution.** Chaque binôme donne ses deux notes et la ligne de la grille qui a fait la différence. Ce qu’on attend : les marqueurs `[À COMPLÉTER]` et `[À VÉRIFIER]` lus comme une **qualité**, pas comme un manque. | tableau |
| 85 à 90 | **La suite.** Comment on contribue (un gabarit pour un livrable qu’on écrit souvent, `CONTRIBUTING.md`) ; le dépôt comme objet versionné. | `CONTRIBUTING.md` |

**Variante travail de semestre** : un groupe écrit un gabarit pour un livrable d’un métier de `skills/palambur-method/metiers/` (26 métiers), le soumet comme contribution, et documente ce que le skill a changé sur cinq demandes réelles anonymisées. La contribution fusionnée vaut mention dans le README (règle du programme `AMBASSADEURS_programme.md`).

## L’exercice noté · consigne prête à distribuer

> **Consigne.** Vous recevez une demande d’entreprise en une phrase. Produisez le document deux fois : d’abord directement, puis avec la Méthode Palambur (skill ou prompt). Rendez : (1) les deux documents ; (2) la liste de **tout ce que la première version a décidé seule** ; (3) votre notation des deux versions avec la grille fournie ; (4) un paragraphe : si vous deviez signer ce document, laquelle des deux versions signeriez-vous, et pourquoi.
>
> **Règle absolue** : aucune donnée réelle de personne ou d’entreprise dans vos copies. Si votre cas en contient, anonymisez avant de coller (la méthode vous le propose ; un outil en ligne gratuit, Jomini, le fait aussi, dans le navigateur, sans compte : palambur.ch/outils/).
>
> **Barème** : la grille d’`epreuves/grille.md` fait foi. La note récompense ce que vous avez **vu**, pas la longueur du document.

## Les contacts institutionnels · fonctions, pas de personnes

Les écoles ci-dessous ont été vérifiées le 11.10.2026 dans `../RELAIS_ROMANDS.md` (titres de page relevés là). Les noms de personnes se relèvent sur le site de l’école **le jour de l’envoi**.

| École | Fonction à viser | Pourquoi cette porte |
|---|---|---|
| **HEG Arc** (Neuchâtel, HES-SO) | responsable de la formation continue ; responsable du CAS « IA appliquée en entreprise » | terrain de Palambur ; un CAS existant où le cas d’étude entre tel quel |
| **HEG Genève** (HES-SO) | responsable de la formation continue ; responsable du CAS « Intelligence artificielle au service de la transformation digitale » | CAS existant, journée certifiante IA |
| **HEIG-VD** | doyen ou responsable du département Économie et Services ; responsable des formations continues | même domaine HES-SO ; offre IA `[À VÉRIFIER sur leur catalogue]` |
| **HES-SO, domaine Économie et Services** (coordination) | responsable de domaine | une seule porte pour les trois écoles ci-dessus, si elle existe pour la formation continue `[À VÉRIFIER]` |
| **Écoles de commerce et de culture générale** (cantons romands) | doyen ou responsable de filière « maturité professionnelle commerciale » ; coordinateur informatique ou numérique | les élèves rédigent déjà offres, courriers, devis en cours de pratique ; **aucune école nommée tant qu’elle n’est pas vérifiée** `[À COMPLÉTER : une école par canton, vérifiée le jour de l’envoi]` |
| **Centre Patronal · Romandie Formation** | responsable des programmes | formation supérieure et continue, déjà dans `RELAIS_ROMANDS.md` |

## Le message d’approche

Le message est celui de `../RELAIS_ROMANDS.md`, section « Le message d’approche », avec ses trois variables ; il **n’est pas recopié**. Pour une école, les variables prennent ces valeurs :

- `[le livrable]` → « des offres d’emploi, des courriers et des devis dans leurs travaux pratiques »
- `[ce qu’on propose]` → « un cas d’étude ouvert (dépôt public, licence MIT) et une séance de 90 minutes prête à donner, avec ses épreuves et sa grille »
- paragraphe ajouté avant la salutation : « Le matériel est libre : vous pouvez le donner sans nous, et un étudiant peut l’améliorer par une contribution versionnée. »

## Ce qui exige Victor

- Le **go d’envoi**, école par école ; Neuchâtel d’abord (HEG Arc), comme dans `RELAIS_ROMANDS.md`.
- La **création du Projet Claude.ai** (le lien « sans rien installer » que l’enseignant donne aux étudiants).
- Si une école veut une **intervention en personne** : la date et le cadre (gratuit en séance ; tout prolongement payant passe par la grille tarifaire, jamais par ce kit).

## Dépendances vers d’autres paquets

- `pedagogie/MANIFESTE.md` et `exemples/` (paquet 4, points 57 et 58) : ce kit les cite comme « en préparation » ; le jour où ils sont posés, remplacer la mention d’état dans la table.

## Marqueurs laissés dans ce fichier

- `[À VÉRIFIER sur leur catalogue]` · offre IA de la HEIG-VD.
- `[À VÉRIFIER]` · existence d’une porte unique « formation continue » au niveau du domaine HES-SO.
- `[À COMPLÉTER : une école par canton, vérifiée le jour de l’envoi]` · écoles de commerce.
