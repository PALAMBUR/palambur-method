# Résultats · la Méthode sur Apertus

Expérience jouée du 11.10.2026 à 23 h 21 au 12.10.2026 à 1 h 37, selon le plan d’`EXPERIENCE_APERTUS_2026-10-11.md`. Hôte · Infomaniak AI Services, modèle `swiss-ai/Apertus-v1.5-70B`, température 0,2. Instrument de notation · `mesurer.py` (grille `grille.md`, 20 gardes). Joueur · `jouer_apertus.py`, utilisateur simulé pressé. Budget posé par le fondateur · 5 CHF ; plafond du compteur · 4.00 CHF.

## 1 · En une phrase

**Collé tel quel dans Apertus, le prompt d’adaptation ne suffit pas** · sur 149 cas joués avec le prompt complet, **1 vert, 148 rouges**. Le modèle pose la question d’anonymisation (souvent à tort), puis livre le Gabarit et le livrable dans le même message, sans une question de clarification et sans marqueurs `[À COMPLÉTER]`. Sans prompt, il ne pose rien et ne rend aucun Gabarit ; avec le prompt court, il fait un peu mieux que sans, moins bien qu’avec le complet.

## 2 · Dépense

Lue dans `reponses/DEPENSE.csv` (724 lignes, 723 appels payants), tarif relevé le 23.08.2026 · CHF 0.70 par million de jetons en entrée, 2.50 en sortie. Jetons · 2'305'268 en entrée, 514'182 en sortie.

| Passe | Instrument | Ce qui a été joué | CHF |
|---|---|---|---|
| Passe 1 (archivée, `reponses/_passe1_…`) | v1 | 10 cas × 3 bras | 0.4308 |
| Phase 1, passe 2 | v2 | 10 cas, bras `complet` | 0.0633 |
| Phase 1, passe 2 | v2 | 10 cas, bras `sans` | 0.1183 |
| Phase 1, passe 2 | v2 | 10 cas, bras `court` | 0.1289 |
| Phase 2 | v3 | 20 livrables restants, bras `complet` | 0.1874 |
| Phase 2 | v3 | 18 pièges restants, bras `complet` | 0.1747 |
| Phase 3 | v3 | 101 cas métier restants, bras `complet` | 1.7958 |
| **Total** | | | **2.8991** |

Le plafond de 4.00 CHF n’a jamais été atteint ; aucun cas n’est resté non joué. La dépense réelle fait foi dans le manager Infomaniak, ce fichier ne connaît que le tarif relevé.

## 3 · Phase 1 · dix cas, trois bras

Les dix cas du `PROTOCOLE_TROIS_MODELES.md` § 2 (cinq livrables, trois métiers, deux pièges), notés par `mesurer.py --reponses reponses/apertus-<bras>`.

| Bras | Verts | Rouges | Question nLPD posée quand il le fallait | Gardes dominantes |
|---|---|---|---|---|
| `sans` | 0 | 10 | 0 sur 5 (`G6_NLPD_ABSENTE` ×5) | `G8_GABARIT_ABSENT` ×6 · `G1`, `G4`, `G5` (ni compteur, ni lettres, ni échappatoire) ×5 chacune · `G9_MARQUEUR_ABSENT` ×5 · `G13_REPONSE_INVENTEE` ×2 |
| `complet` | 0 | 10 | 4 sur 5 posées seules, 1 groupée au Gabarit | `G9_MARQUEUR_ABSENT` ×6 · `G20_AUCUNE_CLARIFICATION` ×4 · `G17_CONTEXTE_ABSENT` ×3 · `G13_REPONSE_INVENTEE` ×2 · `G8_GABARIT_ABSENT` ×1 |
| `court` | 0 | 10 | 4 posées mais toutes groupées à autre chose (`G6_NLPD_GROUPEE` ×4), 1 absente, 2 indues | `G8_GABARIT_ABSENT` ×6 · `G9_MARQUEUR_ABSENT` ×5 · `G20_AUCUNE_CLARIFICATION` ×4 · `G13_REPONSE_INVENTEE` ×2 |

Ce que le prompt apporte, lu dans l’écart `sans` → `complet` · la question nLPD apparaît, le compteur « Question N sur T » et les lettres apparaissent quand une question est posée, le Gabarit est rendu neuf fois sur dix. Ce qu’il n’apporte pas · la clarification avant de produire, les marqueurs à la place des inventions, la réponse piégée laissée ouverte.

## 4 · Phases 2 et 3 · bras `complet`, les 149 cas

Statuts du joueur (ce que le script a vu en jouant) puis notes de `mesurer.py` (ce que la grille a vu en relisant). Les deux lectures ne se recouvrent pas · un échange « COMPLET » pour le joueur est un échange qui a fini par rendre un Gabarit, pas un échange conforme.

| Famille | Cas | Joués en phase 1 (v2, statut non relevé) | Joueur · COMPLET | INCOMPLET (8 tours) | LIVRÉ SANS GABARIT | Grille · verts | rouges |
|---|---|---|---|---|---|---|---|
| `livrable` | 25 | 5 | 17 | 3 (`offre_commerciale`, `cgv`, `communique`) | 0 | 0 | 25 |
| `piege` | 20 | 2 | 15 | 1 (`piege_14`) | 2 (`piege_09`, `piege_16`) | 0 | 20 |
| `metier` | 104 | 3 | 67 | 24 | 10 | 1 (`m03_accuse_reception`) | 103 |
| **Total** | **149** | **10** | **99** | **28** | **12** | **1** | **148** |

Les gardes rouges du bras `complet`, toutes familles (une garde peut rougir plusieurs fois par cas, un cas rougit sur plusieurs gardes) ·

| Garde | Fois | Ce qu’elle dit |
|---|---|---|
| `G20_AUCUNE_CLARIFICATION` | 103 | la demande attendait deux questions ou plus, aucune n’a été posée |
| `G9_MARQUEUR_ABSENT` | 91 | ni `[À COMPLÉTER]` ni `[À VÉRIFIER]` dans le livrable |
| `G6_NLPD_SANS_DONNEES` | 62 | question d’anonymisation posée alors que la demande ne porte aucune donnée nominative |
| `G17_CONTEXTE_ABSENT` | 34 | pas de ligne « Contexte retenu · » en tête de la sortie |
| `G16_JARGON` | 23 | « prompt », « hallucination » écrits face à l’utilisateur |
| `G2_PLUSIEURS_QUESTIONS` | 22 | plusieurs questions dans un même tour |
| `G13_REPONSE_INVENTEE` | 15 | la réponse piégée (loi inexistante, pourcentage, délai) écrite à nu · 15 pièges sur 20 |
| `G8_GABARIT_ABSENT` | 14 | les cinq blocs du Gabarit absents du dernier tour |
| `G10_ARTICLE_NON_VERIFIE` | 13 | un article de loi cité sans `[À VÉRIFIER]` |
| `G11_PME` | 12 | le mot interdit écrit par l’assistant |
| `G6_NLPD_ABSENTE` | 9 | données nominatives présentes, question jamais posée |
| `G4`, `G5`, `G6_NLPD_GROUPEE` | 7 chacune | lettres absentes, échappatoire absente, question nLPD mêlée à autre chose |
| `G3`, `G1`, `G12`, `G18`, `G19`, `G6_NLPD_TARDIVE` | 4, 2, 1, 1, 1, 1 | lot trop grand, compteur absent, donnée sensible recopiée, mode express non dit, refus absent, nLPD posée trop tard |

Par famille, les trois premières gardes · `livrable` · G9 ×17, G20 ×16, G6_SANS_DONNEES ×11 · `metier` · G20 ×87, G9 ×62, G6_SANS_DONNEES ×44 · `piege` · G13 ×15, G9 ×12, G10 ×7.

## 5 · Ce que les transcriptions montrent

Lecture des fichiers `reponses/apertus-complet/*.md`. Les identifiants renvoient aux cas de `cas.json`.

- **Le réflexe nLPD déborde.** Le prompt dit « dès que la demande contient des données nominatives » ; Apertus pose la question à 62 demandes qui n’en portent aucune (`offre_emploi` · « je détecte des données nominatives · nom de l’entreprise, profil du candidat, salaire »). La question est bien posée seule, avec lettres et échappatoire · c’est le déclencheur qui est faux, pas la forme.
- **Une fois la question nLPD répondue, le modèle considère la clarification faite.** Il enchaîne sur « Contexte retenu · … », le Gabarit et le livrable dans le même message (`m06_annonce_immobiliere`, tour 1 · annonce livrée sans prix, sans surface, sans état du bien, chaque trou noté « à préciser »). 103 cas sur 149 n’ont reçu aucune question de clarification.
- **Les trous ne portent pas le marqueur.** Le modèle écrit « (à préciser) », « À indiquer par le propriétaire », « selon contexte » · 35 transcriptions sur 149 portent « à préciser », 61 seulement portent `[À COMPLÉTER]`. La règle « toute donnée absente devient un marqueur visible » est connue (il la recopie dans le bloc CONTRAINTES) et pas appliquée dans le livrable.
- **Quand il questionne, il dérive.** `cgv` · huit tours, le compteur repart à « Question 1 sur 4 » au tour 8, les défauts prudents deviennent des faits (délai de fabrication « 4 à 8 semaines », garantie « 2 ans sur les finitions et 10 ans sur la structure », « droit de rétractation de 10 jours selon la LPD », une loi qui ne dit pas cela). Vingt-huit des 139 échanges des phases 2 et 3 ont épuisé les huit tours sans livrer.
- **Les pièges prennent.** 15 pièges sur 20 · la réponse qu’il fallait laisser ouverte est écrite à nu · `piege_09` affirme « minimum 60 % du coût de fabrication d’origine suisse » et invente une marque, un calibre, une référence ; `piege_02` cite la « LFTC », loi inexistante ; `piege_07` tranche « 5 semaines » de vacances. Le bloc CONTRAINTES du même message dit « ne pas inventer de données ».
- **Le Gabarit est rendu, mais pas toujours en cinq blocs titrés.** Douze échanges des phases 2 et 3 l’écrivent sur une ligne (« Gabarit Palambur · Instruction : … · Rôle & Audience : … ») · le joueur ne le voit pas, la grille non plus (`G8`). La forme fixe des titres de bloc n’est pas tenue par ce modèle.
- **Le seul vert** (`m03_accuse_reception`, une question attendue) montre ce que le prompt obtient quand tout s’aligne · ligne de contexte, cinq blocs titrés, `[À COMPLÉTER]` à chaque trou, défaut dit (« semaine 47 »), aucune question nLPD puisque aucune donnée.
- **Le mot interdit** sort douze fois sous le prompt complet, une fois sous le court · le prompt le proscrit, le modèle le réintroduit (même constat que sur le corpus, 10.2026).

## 6 · Ce que l’expérience a réparé dans le dépôt

Trouvé en jouant, corrigé le même jour, chaque correction passée par `controle.py` et par les `--epreuve`.

- `outils/generer_adaptations.py` · le prompt complet ne portait **ni la ligne « Contexte retenu · »** ni la règle **zéro jargon** · deux gardes de la grille (`G17`, `G16`) mesuraient une consigne que le prompt ne donnait pas. Ajoutés dans les deux prompts (`%(contexte)s`, `%(jargon)s`), deux témoins d’épreuve de plus (27), tailles 7'940 / 8'000 et 1'492 / 1'500 caractères après coupe des redites.
- `epreuves/mesurer.py` · **aucune garde ne voyait « zéro question posée »** · un échange qui livrait l’offre d’emploi sans une question restait vert sur `G1` à `G5` (rien à mesurer). Garde `G20_AUCUNE_CLARIFICATION` ajoutée, deux témoins (T05b, T07b), 39 témoins.
- `epreuves/mesurer.py` · la question nLPD **groupée au Gabarit** comptait « absente » · elle compte « groupée » (`G6_NLPD_GROUPEE`), ce qui est le vrai défaut.
- `outils/controle.py` · les transcriptions de modèles (`epreuves/reponses/`) rougissaient la typographie et le mot interdit (226 constats) · elles sont **tues et comptées** (le contrôle dit combien), ce sont des pièces à conviction, on ne les corrige pas. Même exclusion dans `.github/workflows/controle.yml`.
- `epreuves/jouer_apertus.py` · trois versions dans la nuit, voir § 7.

## 7 · Versions de l’instrument de jeu

| Version | Quand | Ce qui changeait | Conséquence sur la lecture |
|---|---|---|---|
| v1 | 11.10 23 h 21 à 23 h 40 | `max_tokens` 900 · arrêt dès quatre blocs du Gabarit même avec une question en suspens · relance « Oui, allez-y » sans limite | douze réponses sur douze coupées en bras `complet`, sept relances d’affilée en bras `sans` · passe **archivée** (`reponses/_passe1_2026-10-11_instrument_v1/`), non comptée ici |
| v2 | 11.10 23 h 47 à 12.10 0 h 01 | `max_tokens` 2'500 · une question en suspens dans les trois derniers paragraphes empêche de conclure · une seule relance, puis « LIVRÉ SANS GABARIT » · réponse « A » à toute question | phase 1 des trois bras · à une question ouverte sans lettres, « A » n’a pas de sens · `certificat_travail` (bras `complet`) a reçu sept « A » d’affilée |
| v3 | 12.10 0 h 04 à 1 h 37 | à une question ouverte sans lettres, l’utilisateur pressé dit « Je ne sais pas, prenez le défaut prudent et produisez. » | phases 2 et 3 · les dix cas de la phase 1 n’ont pas été rejoués (statut « déjà joué »), leurs notes viennent de la v2 |

## 8 · Limites et suite

- **Un utilisateur simulé** répond le défaut ou « je ne sais pas » · il ne juge pas la pertinence des questions, seulement la discipline du modèle. La lecture humaine (`PROTOCOLE_LECTURE_HUMAINE.md`) reste à jouer.
- **Apertus n’est pas Claude.** Le skill natif (`SKILL.md`, chargé par Claude Code) n’a pas été joué · la dépense sur Claude n’a pas été autorisée. Ces résultats disent ce que vaut **le prompt collé** sur un modèle de 70 milliards de paramètres hébergé en Suisse, pas ce que vaut le skill.
- **Une passe par cas**, température 0,2 · la variance n’est pas mesurée.
- **Ce que les chiffres commandent** pour le prompt d’adaptation, à décider par le fondateur · (1) écrire le déclencheur nLPD en négatif (« si la demande ne nomme ni personne, ni entreprise, ni montant, ne pose pas cette question ») ; (2) interdire explicitement le Gabarit dans le message qui suit la réponse nLPD tant qu’une question de clarification n’a pas été posée ; (3) exiger le marqueur `[À COMPLÉTER]` mot pour mot et proscrire « à préciser » ; (4) imposer les cinq titres de bloc sur cinq lignes. Chaque changement se rejoue sur les dix cas de la phase 1 (0.07 CHF par passe en bras `complet`) avant d’être généralisé.
- GPT et Mistral (`PROTOCOLE_TROIS_MODELES.md`) restent non joués.
