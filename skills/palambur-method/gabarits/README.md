# Gabarits par livrable · bibliothèque du skill

Dix fiches de référence, une par livrable fréquent. Chacune dit **quelles questions valent la peine d’être posées**, quelles valeurs prennent un défaut prudent sans question, et quels champs DONNÉES remplir. Elles détaillent la table « champs DONNÉES par livrable » de `../methode-palambur.md` · elles ne la contredisent pas.

Chaque gabarit est **appuyé sur le corpus Palambur** des invites métier (relevé du 11.10.2026 · 782 invites fr-CH). Les références `PAL-…` citées en bas de chaque fiche existent dans ce corpus ; leurs champs et leurs contraintes ont été repris, pas réinventés.

## Règle d’usage

1. **À l’Étape 1** (évaluer), dès que le livrable est reconnu, le skill charge **un seul** gabarit : celui dont la section « Reconnaître » correspond à la demande. Il ne charge jamais les dix.
2. Si aucun gabarit ne correspond, le skill travaille avec la table générique de `methode-palambur.md`. Il n’invente pas un gabarit.
3. Le gabarit **ordonne le lot** de l’Étape 2 : les questions de la section 2 sont posées dans l’ordre, une par message, avec le compteur. Tout ce que la section 3 liste prend sa valeur par défaut **sans question**, et le défaut est **signalé** dans le livrable.
4. Une question du gabarit déjà répondue par la demande, ou couverte par un défaut prudent que l’utilisateur n’a pas de raison de changer, **se saute** ; le compteur annonce le nombre de questions restantes. Exemple : la relance « deuxième retard cette année » répond déjà à la question du degré.
4 bis. La **forme des choix appartient à `SKILL.md`** : lettres A, B, C (deux choix réels au minimum, trois au plus), défaut signalé sur sa lettre, et l’échappatoire « Autre / je ne sais pas » toujours en **dernière lettre** (D, ou C si la question n’a que deux choix réels). Les fiches la reprennent, elles ne la redéfinissent pas.
5. L’**Étape 0** (données nominatives) reste préalable et indépendante du gabarit. Chaque fiche rappelle seulement si ce livrable déclenche presque toujours la question d’anonymisation.
6. Le gabarit alimente la **partie 1** de la sortie (le Gabarit Palambur rempli, section 7 de la fiche) puis la **partie 2** (le livrable, section 6).

## Structure fixe des dix fiches

Les dix fichiers portent **les mêmes huit sections, dans le même ordre**, numérotées en titres de niveau 2. Un script qui compte les `## ` doit rendre 8 pour chaque fichier.

| N° | Section | Ce qu’elle contient |
|---|---|---|
| 1 | Reconnaître | Les mots de la demande qui désignent ce livrable · et ce avec quoi on le confond |
| 2 | Questions déterminantes | Au plus 4, ordonnées du plus structurant au plus accessoire · choix lettrés à la forme de `SKILL.md` (deux ou trois choix réels, puis « Autre / je ne sais pas » en dernière lettre, quatre lettres au plus) · défaut prudent · le pourquoi en une demi-ligne, à la forme « Pourquoi · parce que … » |
| 3 | Ce qui prend un défaut sans question | Liste « Libellé : défaut » · jamais une question de confort |
| 4 | Champs DONNÉES | Une ligne par exigence, à la forme « Libellé : [À COMPLÉTER] » · les consignes au modèle restent sans marqueur |
| 5 | Contraintes propres au livrable | Lois suisses **nommées** (CO, LTr, LEg, nLPD, LP, LCD, LTVA…), jamais un numéro d’article sans `[À VÉRIFIER]` · aucune CCT nommée sans source · anti-invention |
| 6 | Format attendu | Structure, longueur, ton · mention nLPD si le livrable sort de l’entreprise · validation humaine si RH ou juridique · la ligne « Contexte retenu » qui précède le Gabarit (forme dans `SKILL.md`, exemple dans `offre-emploi.md`) |
| 7 | Le Gabarit Palambur pré-rempli | Les 5 blocs (INSTRUCTION · RÔLE ET AUDIENCE · DONNÉES · CONTRAINTES · FORMAT) avec les marqueurs · les blocs d’extension pour L et XL |
| 8 | Pièges | Ce qu’un modèle invente d’habitude pour ce livrable |

Puis une ligne finale **« Appuyé sur PAL-… »** qui cite les invites sources.

## Conventions communes

- **Marqueurs** · `[À COMPLÉTER]` (l’utilisateur remplit), `[À VÉRIFIER : base légale]` (référence à confirmer au texte en vigueur), `[À VÉRIFIER : CCT applicable]`, `[À ARBITRER]` (décision humaine, souvent un montant ou un délai), `[À CONFIRMER]` (attribution floue dans des notes), `[INFO MANQUANTE]`.
- **Prix et montants** · l’IA met en forme, elle ne chiffre jamais. Un montant absent des DONNÉES devient `[À COMPLÉTER]`, jamais une estimation. Forme : `CHF 4'820.–`.
- **Dates** · jj.mm.aaaa. **Délais** · toujours rattachés à un événement daté.
- **Neutralité de genre** dans tout livrable RH · h/f/d ou formulation épicène.
- **Ton** · français suisse romand, vouvoiement, factuel, aucun superlatif.
- **Niveau** · S, M, L, XL au sens de `methode-palambur.md`. **Ce README est le propriétaire du niveau par livrable** (table ci-dessous) : `cas.json` et les exemples de `SKILL.md` s’alignent sur lui, pas l’inverse. Le niveau commande le nombre de lots et la présence des blocs d’extension, pas la longueur du texte. Règle unique du niveau **S** : **0 à 1 question, jamais de lot**.

## Les dix livrables

| Fichier | Livrable | Niveau | Lots | Étape 0 fréquente | Validation humaine | Appui corpus |
|---|---|---|---|---|---|---|
| `offre-emploi.md` | Offre d’emploi à publier | L | 1 | rare | RH avant publication | PAL-05-RH-01, PAL-14-IP-23, PAL-10-RE-07, PAL-05-RH-27 |
| `relance-facture.md` | Relance de paiement, du rappel à la mise en demeure | M (séquence : L) | 1 | presque toujours | direction avant mise en demeure | PAL-03-SC-05, PAL-09-AB-04, PAL-02-CV-22, PAL-14-IP-21, PAL-16-FI-18, PAL-19-SA-16, PAL-09-AB-21 |
| `devis.md` | Devis chiffré, particulier ou entreprise | L | 1 | souvent | prix validés par une personne nommée | PAL-09-AB-01, PAL-02-CV-05, PAL-03-SC-03, PAL-20-TL-05 |
| `contrat-travail.md` | Contrat individuel de travail | XL | 2 à 3 | toujours | juridique obligatoire avant signature | PAL-05-RH-04, PAL-05-RH-21 · voir aussi PAL-05-RH-24 |
| `certificat-travail.md` | Certificat de travail, complet ou simple | XL | 1 à 2 | toujours | RH + supérieur·e avant signature | PAL-05-RH-16, PAL-05-RH-24, PAL-05-RH-05 |
| `avertissement.md` | Avertissement écrit à un·e collaborateur·trice | L | 1 à 2 | toujours | RH ou juridique avant remise | PAL-05-RH-23, PAL-01-DS-10, PAL-05-RH-24 |
| `courrier-refus-candidat.md` | Réponse négative à une candidature | S | 0 à 1 question, jamais de lot | souvent | aucune, relecture RH conseillée | PAL-05-RH-26 · voir aussi PAL-15-AC-21, PAL-05-RH-01 |
| `offre-commerciale.md` | Offre argumentée de prestations ou de produits | L | 1 à 2 | souvent | direction sur le prix | PAL-14-IP-02, PAL-18-HO-05, PAL-02-CV-24, PAL-02-CV-06, PAL-02-CV-07 |
| `note-interne.md` | Note de service, communication à l’équipe | M | 1 | rare | direction si sujet sensible | PAL-10-RE-18, PAL-05-RH-07 · voir aussi PAL-05-RH-05 |
| `compte-rendu.md` | Compte rendu, PV, relevé de décisions | M (décisions engageantes : L) | 1 | presque toujours | rédacteur·trice + validation des décisions sensibles | PAL-01-DS-01, PAL-02-CV-09, PAL-08-CP-08, PAL-21-AR-18, PAL-16-FI-16, PAL-05-RH-11 |

## Ce qui n’est pas ici

- La **réponse à un appel d’offres public** (AIMP) n’a pas de gabarit : elle relève de PAL-02-CV-06 (XL, formalisme imposé). `offre-commerciale.md` dit quand renvoyer vers elle.
- La **communication interne sensible** (réorganisation, licenciement collectif) n’a pas de gabarit : PAL-05-RH-07 (XL, procédure légale avant toute communication). `note-interne.md` dit quand s’arrêter.
- Le **contrat d’apprentissage** n’a pas de gabarit : formulaire cantonal officiel, régime propre, PAL-05-RH-21. `contrat-travail.md` renvoie vers lui.
- La **lettre de licenciement** n’a pas de gabarit : PAL-05-RH-24 impose une vérification préalable (périodes de protection) que le skill ne peut pas tenir seul.

## Contrôle avant tout commit

Toutes les commandes se lancent **depuis la racine du dépôt** (`05.02_Skill_Methode_Palambur/`). La chaîne complète du dépôt, qui couvre la typographie et le mot interdit, est :

```bash
python3 outils/controle.py
```

Les quatre contrôles propres aux gabarits, un par bloc :

```bash
python3 outils/regle_typo.py skills/palambur-method/gabarits/*.md
```

```bash
grep -rnE "art\. ?[0-9]+" skills/palambur-method/gabarits/ | grep -vF "\`"
```

```bash
grep -c "^- autre" skills/palambur-method/gabarits/*.md
```

```bash
grep -c "^- Pourquoi · parce qu" skills/palambur-method/gabarits/*.md
```

Le premier doit rendre « CONFORME », le deuxième « propre » sur chaque fichier, le troisième rien (les contre-exemples entre accents graves sont écartés par le second filtre ; une ligne restante doit porter `[À VÉRIFIER]`), le quatrième 0 pour chaque fichier (l’échappatoire est une lettre, jamais une ligne à part), le cinquième, pour chaque fiche, autant de lignes que de questions (35 en tout au 11.10.2026 · chaque question porte son pourquoi).
