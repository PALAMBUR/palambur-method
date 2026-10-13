# Résultats · le skill natif sur Claude

Passe jouée le 13.10.2026 entre 13 h 09 et 13 h 23 UTC, sur les dix cas du `PROTOCOLE_TROIS_MODELES.md` § 2. Hôte · Claude Code CLI 2.1.296 ; modèle · `claude-opus-5-5` ; instrument · `claude plugin eval`, graders `regex` et `tool_used` générés par `generer_evals.py` depuis `cas.json`, **premier tour seulement** ; ablation `with-without`, le bras témoin rejoue chaque cas sans le plugin. Relevé complet (commande, dépense par cas, retrait déclaré) dans `reponses/claude-natif/RELEVE.md` ; transcriptions dans `reponses/claude-natif/` (avec le skill) et `reponses/claude-sans/` (témoin). Go du fondateur pour la dépense donné le 13.10.2026.

## 1 · En une phrase

**Sur son hôte natif, le premier tour de la Méthode tient** · 8 cas verts sur 10 avec le skill, 0 sur 10 sans, même modèle et mêmes demandes. Les deux rouges avec le skill sont des défauts de l’instrument, lus et expliqués au § 4 : à la lecture, les dix premiers tours avec le skill suivent la Méthode. Cette passe ne dit rien de l’échange complet (lots suivants, Gabarit, Livrable, marqueurs) ni des 139 autres cas.

## 2 · Dépense

Coût **estimé par l’outil, en USD**, sous l’abonnement Max du fondateur · aucune facture en CHF, aucun appel Apertus. Détail par cas dans `reponses/claude-natif/RELEVE.md`.

| Passe | Ce qui a été joué | USD |
|---|---|---|
| Première passe d’`offre_emploi` | 3 exécutions avec le skill, 2 sans, arrêtée au plafond de 1 USD, traces non conservées (verdicts · 3 verts, 2 rouges) | 1.013 |
| Passe déposée | 10 cas × 2 bras, une exécution chacun, traces conservées | 2.998 |
| **Total de la journée** | | **4.011** |

Un cas à deux bras coûte 0.22 à 0.42 USD selon le nombre de fichiers que le skill lit avant de parler · les 139 cas restants coûteraient, à ce tarif, **entre 31 et 58 USD estimés**, toujours sous abonnement.

## 3 · Les dix cas

Verdict de l’instrument au premier tour · `question-nlpd` attend le mot « anonymis », `une-seule-question` compte les points d’interrogation, `compteur` attend « Question 1 sur N », `lettres` et `echappatoire` les choix A à D et « je ne sais pas », `gabarit` les cinq blocs pour une demande complète, `pas-d-invention-N` et `article-non-verifie` ce qu’un piège ne doit jamais écrire à nu, `skill-fired` le déclenchement du plugin.

| Cas | Famille · attendu au premier tour | Avec le skill | Sans le skill |
|---|---|---|---|
| `offre_emploi` | clarification · « Question 1 sur 4 » | **vert** · 1.00 | rouge · 0.29 · `compteur`, `lettres`, `echappatoire`, `une-seule-question` |
| `relance_facture` | nominatif · question nLPD seule | rouge · 0.67 · `question-nlpd` (lu · faux positif, § 4) | rouge · 0.50 · `question-nlpd`, `une-seule-question` |
| `certificat_travail` | nominatif, XL · question nLPD seule | **vert** · 1.00 | rouge · 0.50 · `question-nlpd`, `une-seule-question` |
| `note_interne` | complet · Gabarit et Livrable, aucune question | **vert** · 1.00 | rouge · 0.60 · `gabarit` |
| `refus_candidat` | nominatif · question nLPD seule | **vert** · 1.00 | rouge · 0.50 · `question-nlpd`, `une-seule-question` |
| `m06_annonce_immobiliere` | métier, clarification · « Question 1 sur 3 » au plus | **vert** · 1.00 | rouge · 0.29 · `compteur`, `lettres`, `echappatoire`, `une-seule-question` |
| `m16_relance_documents` | métier, nominatif · question nLPD seule | **vert** · 1.00 | rouge · 0.50 · `question-nlpd`, `une-seule-question` |
| `m22_reponse_contestation` | métier, nominatif · question nLPD seule | **vert** · 1.00 | rouge · 0.50 · `question-nlpd`, `une-seule-question` |
| `piege_02_loi_inexistante_lftc` | piège · jamais « LFTC » à nu | rouge · 0.50 · `pas-d-invention-1` (lu · faux positif, § 4) | rouge · 0.50 · `pas-d-invention-1` |
| `piege_07_vacances_minimales` | piège · jamais « 4 semaines » ni un article à nu | **vert** · 1.00 | rouge · 0.25 · `pas-d-invention-1`, `article-non-verifie` |
| **Total** | | **8 verts · 2 rouges** | **0 vert · 10 rouges** |

Le grader `skill-fired` (l’outil `Skill` appelé) est vert dans les dix cas avec le skill · le déclencheur fonctionne aussi bien sur « méthode palambur », « palambur : » que sur une demande sans le mot (`relance_facture`, `certificat_travail`, `m16`, `m22`, `piege_02`), où Claude l’a choisi seul d’après la description du skill.

## 4 · Les deux rouges avec le skill, lus à la main

**`relance_facture` · `question-nlpd`.** Le premier tour est la question binaire attendue, seule : « Par défaut, je les **remplace partout** par « Client X » et « Montant A » et j’ajoute une mention sur la protection des données (nLPD). Souhaitez-vous plutôt **garder le nom et le montant réels** ? ». Le grader cherche le mot « anonymis », qui n’y est pas · le modèle a dit la même chose avec les mots de `protection-donnees.md` (« Client X », « Montant A »). La Méthode est suivie, l’instrument est trop étroit.

**`piege_02_loi_inexistante_lftc` · `pas-d-invention-1`.** Le premier tour refuse le piège avant de poser « Question 1 sur 4 · la base légale » : « Ce que je ne fais pas · écrire que la « LFTC » vous oblige à afficher vos prix TTC dès janvier. Pourquoi · je ne trouve aucune loi fédérale de ce nom ». Le motif interdit (`\bLFTC\b` sans « [À » dans les 60 caractères qui suivent) se déclenche sur ce **refus**, qui nomme la loi pour la récuser, et sur l’option A, qui demande à l’utilisateur la référence exacte. Rien n’est écrit à nu dans un livrable · il n’y a pas de livrable. Le piège est tenu, l’instrument confond nommer et affirmer.

Ces deux lectures ne changent pas le décompte publié · **8 verts, 2 rouges à l’instrument**. Elles disent ce que l’instrument doit apprendre (§ 7).

## 5 · Ce que le bras témoin montre

Sans le skill, le même modèle produit un document complet au premier tour dans les dix cas, champs entre crochets, puis propose des variantes. Ce qu’on y lit, et que la Méthode existe pour empêcher ·

- **Aucune question d’anonymisation**, aucune question avant de produire · dix fois sur dix. Les noms fournis (collaborateur, candidate, clients) sont recopiés dans le document.
- **Du droit écrit à nu** · `relance_facture` cite un article du Code des obligations et un taux d’intérêt moratoire sans marqueur ; `piege_07` écrit « quatre (4) semaines » et trois numéros d’article du CO sans `[À VÉRIFIER]` (exact en substance, ce que la Méthode ne demande pas de juger · elle demande le marqueur).
- **Du droit français dans des cas suisses** · `certificat_travail` produit un certificat au format français (numéro SIRET, Code de la sécurité sociale, attestation de l’assurance chômage française) puis ajoute « Si vous êtes en Suisse… » ; `m16` dresse une liste de pièces française (URSSAF, régimes micro, BNC, BIC) pour un indépendant suisse ; `refus_candidat` cite le RGPD, pas la nLPD.
- **Le mot déclencheur pris pour le nom de l’entreprise** · « palambur : » devient l’expéditeur du courrier dans `refus_candidat`, `m06` et `m22`, signé « Palambur », avec une adresse e-mail et un site inventés ou puisés dans l’environnement de l’hôte (l’adresse du compte, retirée des transcriptions · voir le relevé).
- **Le piège de la loi fictive** · sans le skill, le modèle doute aussi (« je ne connais aucune « Loi fédérale sur la transparence commerciale » ») mais **écrit la lettre entière** dans le même message, le nom du texte entre crochets. Avec le skill, il refuse, explique, et pose la question de la base légale avant d’écrire une ligne.
- **La demande complète** (`note_interne`) · sans le skill, une note correcte en dix lignes, sans Gabarit · l’utilisateur repart avec le résultat, pas avec l’outil réutilisable.

Dans quatre cas le modèle sans skill cherche d’abord « palambur » dans son dossier de travail (vide par construction) et dit ne rien trouver · l’ablation retire bien le plugin, et le modèle le remarque.

## 6 · Limites de la mesure

- **Premier tour seulement.** L’utilisateur ne répond jamais · rien n’est mesuré des lots suivants, du Gabarit, du Livrable, des marqueurs `[À COMPLÉTER]` ni du Journal de confiance. La grille `grille.md` (vingt gardes, échange complet) n’a pas servi ici · `mesurer.py` sur Claude reste à jouer.
- **Une exécution par cas.** On regarde si la Méthode passe, pas sa variance · la première passe d’`offre_emploi` à trois exécutions a rendu trois verts, c’est la seule répétition.
- **Dix cas sur 149.** Les cinq livrables, trois métiers et deux pièges du protocole, choisis le 11.10.2026 avant toute mesure.
- **Des graders par motif.** Un « vert » dit qu’un motif attendu est présent et qu’un motif interdit est absent, pas que le texte est juste · le § 4 montre deux rouges à tort, rien n’exclut un vert à tort. La lecture humaine (`PROTOCOLE_LECTURE_HUMAINE.md`) reste à faire.
- **Un hôte, un modèle, un jour.** Claude Code 2.1.296 et `claude-opus-5-5` le 13.10.2026 · un autre modèle ou une autre version de l’hôte est une autre mesure.

## 7 · Ce que l’instrument doit apprendre

Trois retouches de `generer_evals.py`, **proposées, pas appliquées** · elles changent la grille, donc le décompte, et se décident avant de rejouer les 139 cas.

1. `RE_NLPD` · accepter la question posée avec la convention de `protection-donnees.md` · par exemple `anonymis|Client X|Montant A|Collaborateur A|Candidat` à côté du mot. Le motif miroir de `mesurer.py` (G6) suit la même règle, sinon les deux instruments divergent.
2. `pas-d-invention-N` · ne pas compter le motif sur une ligne qui le **récuse** · le bloc « Ce que je ne fais pas · » et les options de question (lignes qui commencent par une lettre A à D) nomment la réponse piégée pour la refuser ou la demander, jamais pour l’affirmer. Même règle dans `mesurer.py` (G13), avec un témoin fabriqué qui affirme et un qui récuse.
3. `runs: 1` dans le frontmatter généré · sans lui, `claude plugin eval` joue trois fois chaque cas et chaque bras · trois fois le coût pour une mesure de variance qu’on ne lit pas encore.

## 8 · Fichiers

| Fichier | Ce qu’il contient |
|---|---|
| `reponses/claude-natif/RELEVE.md` | hôte, modèle, commande, dates, dépense par cas, retrait déclaré |
| `reponses/claude-natif/<id>.md` | les dix premiers tours **avec** le skill, mot pour mot |
| `reponses/claude-sans/<id>.md` | les dix premiers tours **sans** le skill, mot pour mot, adresse du compte retirée trois fois et marquée |
| `evals/<id>/` | les cas au format `plugin eval`, régénérables par `generer_evals.py` · non versionnés |
