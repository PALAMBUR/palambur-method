# Exemples complets · dix cas, un par gabarit

Dix déroulés de bout en bout, écrits le 11.10.2026 à partir des dix fiches de [`../skills/palambur-method/gabarits/`](../skills/palambur-method/gabarits/). Chacun montre, dans l’ordre où l’utilisateur les voit :

1. **la demande brute**, telle qu’on la tape en une ou deux phrases ;
2. **la question d’anonymisation** (Étape 0) quand la demande porte des noms ou des montants ;
3. **les questions**, une par message, avec le compteur « Question N sur T », les choix lettrés, le défaut prudent et l’échappatoire ;
4. **le Gabarit Palambur rempli**, le prompt réutilisable en cinq blocs (neuf pour les livrables sensibles) ;
5. **le livrable**, prêt à relire ;
6. **ce qui n’a pas été inventé**, la liste des trous laissés visibles.

Toutes les données sont **fictives**. L’entreprise s’appelle « Exemple SA », les personnes sont désignées par leur fonction ou par les pseudonymes de la Méthode (« Client X », « Collaborateur·trice A »). Aucun montant, aucune date et aucune référence de ces exemples ne décrit une entreprise réelle.

| Fichier | Livrable | Niveau | Étape 0 jouée |
|---|---|---|---|
| [`01-offre-emploi.md`](01-offre-emploi.md) | Offre d’emploi à publier | L | non |
| [`02-relance-facture.md`](02-relance-facture.md) | Relance de paiement | M | oui |
| [`03-devis.md`](03-devis.md) | Devis chiffré | L | oui |
| [`04-contrat-travail.md`](04-contrat-travail.md) | Contrat individuel de travail | XL | oui |
| [`05-certificat-travail.md`](05-certificat-travail.md) | Certificat de travail | XL | oui |
| [`06-avertissement.md`](06-avertissement.md) | Avertissement écrit | L | oui |
| [`07-courrier-refus-candidat.md`](07-courrier-refus-candidat.md) | Réponse négative à une candidature | S | oui |
| [`08-offre-commerciale.md`](08-offre-commerciale.md) | Offre commerciale | L | oui |
| [`09-note-interne.md`](09-note-interne.md) | Note interne | M | non |
| [`10-compte-rendu.md`](10-compte-rendu.md) | Compte rendu de séance | M | oui |

## Comment lire ces exemples

- Les réponses de l’utilisateur sont **choisies pour l’exemple** et écrites en clair après chaque question. Dans la vraie vie, l’utilisateur répond par une lettre ou en texte libre.
- Un livrable de niveau **XL** (contrat, certificat) est **raccourci** ici : il montre la structure et les marqueurs, pas les trois pages. Le gabarit dit la longueur réelle attendue.
- Les textes de loi sont **nommés**, jamais cités par article : partout où un numéro, un délai ou un taux manquerait, le livrable porte `[À VÉRIFIER : …]`. C’est la règle de [`../skills/palambur-method/references-juridiques.md`](../skills/palambur-method/references-juridiques.md), et c’est ce que ces exemples veulent montrer.
- Les marqueurs `[À COMPLÉTER]`, `[À VÉRIFIER]`, `[À ARBITRER]` et `[À CONFIRMER]` sont **la démonstration**, pas des oublis : ce qui n’a pas été dit n’a pas été inventé.

## Contrôle

Depuis la racine du dépôt :

```bash
python3 outils/regle_typo.py exemples/*.md
```

Chaque fichier doit rendre « propre ». Le contrôle complet du dépôt, `python3 outils/controle.py`, couvre aussi ce dossier (typographie, mot interdit, liens).
