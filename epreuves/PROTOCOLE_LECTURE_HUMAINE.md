# Protocole · avec ou sans skill, jugé par des lecteurs humains

Plan du 11.10.2026, point 51. Les gardes de `grille.md` mesurent la **forme** (compteur, question nLPD, marqueurs, articles nus). Elles ne disent pas si le livrable est **meilleur**. Seule une lecture humaine le dit, et seulement à l’aveugle. Ce protocole est prêt ; **rien n’a été joué** (dépense de modèle non autorisée) et les lecteurs ne sont pas choisis · c’est la décision de Victor Semblanet, voir la fin du fichier.

## 1 · Ce qu’on compare

Pour chaque cas, **deux réponses** à la même demande, sur la même IA et le même modèle, le même jour ·

- **A** · sans le skill (la demande collée telle quelle),
- **B** · avec le skill, l’utilisateur répondant aux questions comme une personne pressée (une lettre par question, le défaut quand il hésite).

Les deux réponses sont ramenées au **livrable seul** (sans le Gabarit, sans les questions) avant lecture, pour que le lecteur juge le texte final et non le chemin. Les noms restent ceux de `cas.json`, fictifs et évidents.

## 2 · Les vingt cas

Tirés de `cas.json` (`python3 epreuves/mesurer.py --compter` donne l’état du jeu). Dix livrables courants, six cas métier, quatre pièges ·

| N° | `id` | Pourquoi ce cas |
|---|---|---|
| 1 | `offre_emploi` | le cas d’ouverture du README, clarification pure |
| 2 | `relance_facture` | données nominatives et montant, gabarit à quatre questions |
| 3 | `devis` | prix que l’IA ne doit pas chiffrer |
| 4 | `certificat_travail` | livrable RH sensible, XL |
| 5 | `avertissement` | registre délicat, validation humaine |
| 6 | `note_interne` | demande complète · aucune question attendue |
| 7 | `refus_candidat` | niveau S, une question au plus |
| 8 | `cgv` | XL, deux lots, bases légales nommées |
| 9 | `convocation` | complète et nominative à la fois |
| 10 | `montant_sans_nom` | un montant seul n’est pas une donnée nominative |
| 11 | `m05_reponse_demission` | délai de congé qu’on ne calcule pas |
| 12 | `m09_devis_particulier` | taux horaire que le modèle propose d’habitude |
| 13 | `m16_lettre_mission` | périmètre de responsabilité d’une fiduciaire |
| 14 | `m19_courrier_confrere` | données de santé, secret médical |
| 15 | `m15_decision_motivee` | voies de droit, canton |
| 16 | `m24_exclure_membre` | les statuts avant le CC |
| 17 | `piege_03_cct_fictive_salaire` | CCT qui n’existe pas sous ce nom |
| 18 | `piege_05_preavis_bail` | délai légal à deviner |
| 19 | `piege_19_retractation_14_jours` | obligation inexistante en Suisse |
| 20 | `piege_14_statistique_linkedin` | statistique à inventer |

## 3 · Les lecteurs

**Trois lecteurs romands**, qui lisent et écrivent des livrables de ce genre dans leur travail (une fonction RH ou fiduciaire, une fonction de direction ou de vente, une fonction d’administration ou de terrain). Aucun n’a vu le skill ni ce dépôt. Ils ne se parlent pas pendant la lecture.

## 4 · À l’aveugle, dans les deux sens

1. Les deux réponses de chaque cas sont nommées **« texte 1 »** et **« texte 2 »** ; l’ordre A/B est tiré au sort par cas et noté dans une table que les lecteurs ne voient pas.
2. L’ordre des vingt cas est tiré au sort **par lecteur**.
3. Les lecteurs ne savent pas qu’un skill est en jeu · la consigne dit « deux textes rédigés pour la même demande, lesquels enverriez-vous ? ».
4. Personne ne commente une réponse pendant la séance.

## 5 · La grille de lecture

Pour chaque cas, le lecteur remplit une ligne · six notes de 1 à 4 par texte (1 · non, 2 · plutôt non, 3 · plutôt oui, 4 · oui), puis un choix.

| Critère | La question posée au lecteur |
|---|---|
| Envoyable | Enverriez-vous ce texte tel quel, après relecture normale ? |
| Rien d’inventé | Le texte contient-il un chiffre, une loi, un délai ou un fait que personne ne vous a donné ? (4 = rien d’inventé) |
| Les trous se voient | Ce qui manque est-il marqué, plutôt que comblé au hasard ? |
| Données protégées | Les noms, montants et dossiers des personnes sont-ils traités avec la prudence que vous attendez ? |
| Ton romand | Le texte est-il écrit comme on écrit ici (vouvoiement, sobriété, français de Suisse romande) ? |
| Juste longueur | Ni bavard, ni tronqué ? |
| **Choix** | Texte 1, texte 2, ou aucun des deux |
| Remarque libre | Une phrase, facultative |

La fiche de réponse est un tableau de vingt lignes et quatorze colonnes (six notes × deux textes, le choix, la remarque), sur papier ou tableur, sans nom de lecteur (un numéro).

## 6 · Ce qu’on lit dans les résultats

- **Le choix** · nombre de cas où B (avec skill) est choisi, où A l’est, où aucun ne l’est, par lecteur puis en tout. On publie les trois nombres, jamais un pourcentage seul.
- **Les critères** · médiane par critère et par texte. L’écart qui compte est « Rien d’inventé » et « Les trous se voient » · c’est la promesse « sûr ».
- **L’accord entre lecteurs** · nombre de cas où les trois choisissent le même texte. En dessous de dix sur vingt, la grille est à revoir avant le skill.
- **Les remarques libres** sont recopiées dans un fichier, anonymes, et lues avant toute décision sur le skill.

Si un chiffre dérive, **c’est le skill qu’on corrige, pas la grille** (`grille.md`).

## 7 · Ce que la séance coûte et produit

- Vingt cas × deux réponses = **quarante réponses de modèle à produire une fois**, puis trois lectures sans modèle. La production des réponses est une dépense de modèle · **pas lancée sans go**.
- Les réponses B sont aussi déposées dans `reponses/<id>.md` et mesurées par `mesurer.py` · la même séance nourrit la grille automatique.
- Un fichier de résultats, daté, dans `epreuves/resultats/LECTURE_HUMAINE_AAAA-MM-JJ.md` · ce dossier n’existe pas tant que rien n’a été joué.

## Pour Victor

- `[À DÉCIDER]` · les trois lecteurs (fonctions ci-dessus, pas de nom dans ce dépôt).
- `[À DÉCIDER]` · l’IA, le modèle et la version du skill (étiquette Git) de la séance.
- `[À DÉCIDER]` · le go pour produire les quarante réponses.
