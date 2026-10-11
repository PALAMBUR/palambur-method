# Parrainage GitHub · note de décision (point 82)

**Note · 11.10.2026 · session Skills et Prompt Ingénierie · décision Victor.** La question : faut-il poser un bouton « Sponsor » (GitHub Sponsors, fichier `.github/FUNDING.yml`) sur le dépôt public du skill ? **Rien n’est posé** ; par défaut, le dépôt n’a pas de bouton de don.

## Ce qu’est le bouton

GitHub affiche un bouton « Sponsor » en tête d’un dépôt quand celui-ci porte un fichier `.github/FUNDING.yml` listant un ou plusieurs comptes de financement (GitHub Sponsors du propriétaire, ou des plateformes tierces). Les conditions d’ouverture d’un compte GitHub Sponsors pour une entreprise individuelle suisse, les frais retenus et la fiscalité des sommes reçues **n’ont pas été relevés sur une page officielle le 11.10.2026** : ils s’écrivent ici seulement avec leur URL et leur date, le jour où quelqu’un les lit (`[À VÉRIFIER]`).

## Pour

- **Un signal d’ouverture** : un bouton de don dit « ce projet est fait pour durer et accepte de l’aide », ce que les projets ouverts bien tenus affichent souvent.
- **Un canal sans friction** pour une personne qui veut dire merci sans acheter une prestation.
- **Aucun coût de mise en place** : un fichier de quelques lignes.

## Contre

- **La promesse publique** du README est « gratuit et le restera ». Un bouton de don à côté brouille la phrase : on lit « gratuit, mais… ». Le skill est la **porte** vers Chaptal, la formation et la version entreprise ; c’est là que Palambur gagne sa vie, pas dans les dons.
- **La posture** : Palambur est une entreprise de conseil qui vend des prestations à des entreprises. Un bouton de don est la posture d’un projet communautaire ou d’un développeur indépendant ; ce n’est pas celle d’un fournisseur qu’une direction d’entreprise mandate.
- **La comptabilité et la fiscalité** : chaque don est un revenu de l’entreprise individuelle, à comptabiliser, à déclarer, éventuellement soumis à la TVA selon les seuils `[À VÉRIFIER]`. Pour des montants probablement petits, c’est un travail administratif disproportionné.
- **Un deuxième rail d’argent** : le paiement Palambur passe par Stripe, chantier clos le 24.09.2026, un seul rail et un seul porte-monnaie. GitHub Sponsors en ouvrirait un second, hors de ce rail, avec ses propres relevés.
- **Le retour en arrière coûte** : retirer un bouton de don posé se remarque plus que ne jamais l’avoir mis.

## Recommandation

**Pas de bouton de don, pas de `FUNDING.yml`, dans la version 1.0.0 ni après, tant que le critère de fin de la v1 n’est pas atteint** (point 100 du plan : mille installations attestées et dix contributions externes fusionnées). Ce jour-là, la question se repose avec les chiffres en main, et la réponse peut rester non.

**Ce qu’on fait à la place**, et qui tient la même promesse d’ouverture :

- la section **« Engagements »** du README dit déjà gratuit, sans télémétrie, sans publicité ;
- **`CONTRIBUTING.md`** dit comment aider : un gabarit, une correction juridique, une langue ;
- la **mention Chaptal** sous les engagements est la seule porte commerciale, et elle est nommée comme telle.

Si une personne demande spontanément comment soutenir le projet, la réponse est : **une étoile sur le dépôt, un gabarit contribué, ou une recommandation à une entreprise qui a besoin de la formation.**

## Ce qui exige Victor

1. Confirmer ou renverser la recommandation.
2. S’il la renverse : lire les conditions GitHub Sponsors pour une entreprise individuelle suisse sur la page officielle, avec date et URL, puis en parler au comptable avant de poser le fichier.

## Trous et décisions

- `[À DÉCIDER]` · la décision elle-même (recommandation : non).
- `[À VÉRIFIER]` · conditions, frais et fiscalité GitHub Sponsors, seulement si la décision est oui.
