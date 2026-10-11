# Gouvernance du dépôt · qui décide, qui tient, quand on s’arrête

Écrit le 11.10.2026 (plan d’actions en 100 points, points 98, 99 et 100). Ce fichier dit **qui répond de chaque axe** du plan, **ce que seul le fondateur décide**, **comment on suit le budget** par trimestre, et **à quoi on reconnaît que la version 1 est finie**. Il ne décrit pas la méthode elle-même (`skills/palambur-method/`) ni la façon de contribuer (`CONTRIBUTING.md`).

## 1 · Un responsable par axe

Le plan d’actions se lit par **axes** (A à M). Chaque axe a **un** responsable, désigné par sa fonction · une session de travail de l’atelier Palambur, ou le fondateur. Le responsable ne fait pas tout lui-même ; il **répond** de l’état de l’axe à la revue trimestrielle.

| Axe | Sujet | Responsable |
|---|---|---|
| A | Fondations du dépôt (licence, journal, README) | Session Skills et Prompt Ingénierie |
| B | Le skill lui-même (`SKILL.md`, fichiers de référence) | Session Skills et Prompt Ingénierie |
| C | Portabilité vers les autres hôtes (adaptations, installation) | Session Skills et Prompt Ingénierie |
| D | Viralité et visibilité · **sauf** le point 21 (page `palambur.ch/methode/`) | Session Skills et Prompt Ingénierie · point 21 : Session Site |
| E | Pont avec l’offre Palambur | Fondateur (décide) · Session Skills et Prompt Ingénierie (prépare) |
| F | Expérience de la personne | Session Skills et Prompt Ingénierie |
| G | Protection des données | Session Skills et Prompt Ingénierie |
| H | Évaluation et qualité | Session Skills et Prompt Ingénierie |
| I | Pédagogie et langues · **sauf** le point 61 (fiche imprimable au gabarit PDF maison) | Session Skills et Prompt Ingénierie · point 61 : Session Site (gabarit maison) |
| J | Distribution et partenariats | Session Site |
| K | Produit et modèle d’affaires · points 78 et 79 (ponts vers Chaptal et Jacquard) | Fondateur (décide) · points 78 et 79 : Sessions Chaptal et Jacquard |
| L | Technique (installation, conformité au standard, chaîne de contrôle, modèles de tickets) | Session Skills et Prompt Ingénierie |
| M | Gouvernance (marques, revue, budget, critère de fin) | Fondateur (décide) · Session Skills et Prompt Ingénierie (prépare) |

Règle de lecture · quand un point d’un axe exige un fichier qui appartient à un autre responsable, on **écrit la demande**, on ne touche pas au fichier. Les périmètres sont tenus dans l’atelier, hors de ce dépôt.

## 2 · Ce que seul le fondateur décide

Aucune session ne fait ces gestes sans son accord écrit, même si le travail est prêt :

- pousser sur la branche publique, poser une étiquette, publier une release ;
- soumettre à un annuaire, prendre contact avec un partenaire, un relais, un média ;
- fixer ou publier un prix, signer, payer, déposer une marque ;
- abandonner un point du plan, ou changer un critère de ce fichier.

## 3 · Budget par trimestre · le gabarit

Un tableau par trimestre, rempli à la revue trimestrielle. Les montants sont en francs suisses, les heures en heures de session. Les lignes qui n’ont rien à dire restent à zéro ; on ne les supprime pas, pour que les trimestres se comparent.

### Trimestre 4 · 2026 (du 01.10.2026 au 31.12.2026)

| Poste | Prévu | Réalisé | Écart | Source du chiffre réalisé |
|---|---|---|---|---|
| Heures de session (toutes sessions, ce dépôt) | [À COMPLÉTER] | [À COMPLÉTER] | [À COMPLÉTER] | journal des sessions de l’atelier |
| Essais de modèles (CHF, facturés par les fournisseurs) | [À COMPLÉTER] | [À COMPLÉTER] | [À COMPLÉTER] | factures des fournisseurs |
| Vidéo (CHF · tournage, montage, musique) | [À COMPLÉTER] | [À COMPLÉTER] | [À COMPLÉTER] | factures |
| Marque (CHF · taxes de l’IPI, conseil) | [À COMPLÉTER] | [À COMPLÉTER] | [À COMPLÉTER] | décompte de l’IPI (`diffusion/produit/MARQUES_IPI_note.md`) |
| Autres (CHF · nom de domaine, impression, divers) | [À COMPLÉTER] | [À COMPLÉTER] | [À COMPLÉTER] | factures |
| **Total CHF** | [À COMPLÉTER] | [À COMPLÉTER] | [À COMPLÉTER] | somme des lignes en francs |

Pour un nouveau trimestre · copier ce tableau sous un nouveau titre, **au-dessus** du précédent (le plus récent se lit d’abord). Le « Prévu » se fixe à la revue qui ouvre le trimestre, le « Réalisé » à celle qui le ferme. Un chiffre sans source ne s’écrit pas.

## 4 · Critère de fin de la version 1

La version 1 est **finie**, et on ouvre le bilan, quand les deux conditions sont réunies :

1. **mille installations attestées** du skill ;
2. **dix contributions externes fusionnées** (des demandes de fusion venues de personnes hors de l’atelier Palambur, acceptées dans la branche publique).

Alors, et seulement alors · un **bilan** écrit (ce qui a servi, ce qui n’a pas servi, ce que les contributions ont demandé), puis la **décision** du fondateur d’ouvrir une version 2, de prolonger la version 1, ou d’arrêter.

**Avant ce point, pas de refonte d’architecture** · ni du découpage des fichiers du skill, ni de la chaîne de contrôle, ni du format des adaptations. On corrige, on complète, on traduit ; on ne reconstruit pas. Une proposition de refonte reçue avant le critère est rangée, datée, et relue au bilan.

Ce que ce critère ne fixe pas encore · la **façon de compter une installation attestée**. Un clone ou une étoile sur GitHub n’est pas une installation ; une installation par le marketplace, un téléversement sur claude.ai ou un lien dans `~/.agents/skills/` ne remontent aucun compteur au dépôt. La mesure retenue est à décider (voir la fin de ce fichier).

## 5 · Revue trimestrielle

L’état des 100 points du plan est revu **une fois par trimestre**, à la date anniversaire du 11.10.2026 (prochaine : 11.01.2027). La table de revue vit **dans l’atelier, hors de ce dépôt**, en tête du plan d’actions ; elle dit ce qui est fait, en cours, abandonné, et à quelle date. Le budget du § 3 se remplit à la même séance. Les abandons sont une décision du fondateur (§ 2).

## Ce qui reste à décider

- `[À DÉCIDER]` · la définition et la source d’une **installation attestée** (compteur du marketplace, formulaire volontaire, retour par ticket, autre), pour que le critère du § 4 soit mesurable.
- `[À COMPLÉTER]` · les six lignes « Prévu » du trimestre 4 · 2026, à la première revue.
