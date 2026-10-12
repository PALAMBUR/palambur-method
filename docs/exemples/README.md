# Exemples complets · dix cas, un par gabarit

Dix déroulés de bout en bout, écrits le 11.10.2026 à partir des dix fiches de [`gabarits/`](../../skills/palambur-method/gabarits/) et alignés le 12.10.2026 sur la sortie réelle du skill. Chacun montre, dans l’ordre où l’utilisateur les voit à l’écran :

1. **l’ouverture** · au premier déclenchement, les trois lignes fixes (« Méthode Palambur. Je vais d’abord vous poser quelques questions… »), puis la ligne « Niveau de sensibilité · ordinaire / sensible / critique » ;
2. **la question binaire sur les données** (Étape 0) · seule, sans compteur, en premier, dès que la demande porte un nom ou un montant rattaché à quelqu’un ; au niveau critique, avec la phrase du pont vers Jomini ;
3. **les questions**, une par message · « Question N sur T · objet », une phrase, choix A à D, un défaut prudent marqué « défaut si vous ne précisez pas », et « Autre / je ne sais pas » en dernier ;
4. **la ligne « Contexte retenu »** puis le bloc **« Gabarit Palambur »** · livrable, destinataire, canton, ton, sort des données, et le compte honnête « N réponses, M défauts, K marqueurs » ; puis le Gabarit en cinq blocs (neuf pour les livrables sensibles), réutilisable ;
5. **le bloc « Livrable »** puis le **« Journal de confiance »** · le texte prêt à relire, fermé par cinq lignes au plus : niveau, données, marqueurs comptés, hypothèses refusées, relecture humaine.

Toutes les données sont **fictives**. L’entreprise s’appelle « Exemple SA », les personnes sont désignées par leur fonction ou par les pseudonymes de la Méthode (« Client X », « Collaborateur·trice A »). Aucun montant, aucune date et aucune référence de ces exemples ne décrit une entreprise réelle.

| Fichier | Livrable | Niveau | Sensibilité | Étape 0 jouée |
|---|---|---|---|---|
| [`01-offre-emploi.md`](01-offre-emploi.md) | Offre d’emploi à publier | L | ordinaire | non |
| [`02-relance-facture.md`](02-relance-facture.md) | Relance de paiement | M | sensible | oui |
| [`03-devis.md`](03-devis.md) | Devis chiffré | L | sensible | oui, noms conservés |
| [`04-contrat-travail.md`](04-contrat-travail.md) | Contrat individuel de travail | XL | critique | oui |
| [`05-certificat-travail.md`](05-certificat-travail.md) | Certificat de travail | XL | critique | oui |
| [`06-avertissement.md`](06-avertissement.md) | Avertissement écrit | L | critique | oui |
| [`07-courrier-refus-candidat.md`](07-courrier-refus-candidat.md) | Réponse négative à une candidature | S | sensible | oui, noms conservés |
| [`08-offre-commerciale.md`](08-offre-commerciale.md) | Offre commerciale | L | sensible | oui |
| [`09-note-interne.md`](09-note-interne.md) | Note interne | M | ordinaire | non |
| [`10-compte-rendu.md`](10-compte-rendu.md) | Compte rendu de séance | M | sensible | oui |

L’exemple 01 est aussi dessiné en une image : [`../demo-quatre-questions.svg`](../demo-quatre-questions.svg) · la demande, les quatre questions, les deux blocs et le journal.

## Comment lire ces exemples

- Les réponses de l’utilisateur sont **choisies pour l’exemple** et écrites en clair après chaque question. Dans la vraie vie, l’utilisateur répond par une lettre ou en texte libre.
- Les **compteurs** de la ligne de contexte sont ceux de l’exemple : « réponses » compte les questions auxquelles l’utilisateur a répondu, « défauts » les valeurs prudentes posées sans question, « marqueurs » les trous laissés visibles dans le livrable, chacun compté une fois. Le Journal de confiance les détaille.
- Un livrable de niveau **XL** (contrat, certificat) est **raccourci** ici : il montre la structure et les marqueurs, pas les trois pages. Le gabarit dit la longueur réelle attendue.
- Les textes de loi sont **nommés**, jamais cités par article : partout où un numéro, un délai ou un taux manquerait, le livrable porte `[À VÉRIFIER : …]`. C’est la règle de [`references-juridiques.md`](../../skills/palambur-method/references-juridiques.md), et c’est ce que ces exemples veulent montrer.
- Les marqueurs `[À COMPLÉTER]`, `[À VÉRIFIER]`, `[À VALIDER]`, `[À ARBITRER]`, `[À CONFIRMER]` et `[INFO MANQUANTE]` sont **la démonstration**, pas des oublis : ce qui n’a pas été dit n’a pas été inventé.
- La forme de chaque pièce est fixée dans le skill : l’ouverture et les questions dans [`SKILL.md`](../../skills/palambur-method/SKILL.md), le niveau de sensibilité et le Journal de confiance dans [`protection-donnees.md`](../../skills/palambur-method/protection-donnees.md), la ligne de contexte dans [`gabarits/offre-emploi.md`](../../skills/palambur-method/gabarits/offre-emploi.md), section 6.

## Contrôle

Depuis la racine du dépôt :

```bash
python3 outils/regle_typo.py docs/exemples/*.md
```

Chaque fichier doit rendre « propre ». Le contrôle complet du dépôt, `python3 outils/controle.py`, couvre aussi ce dossier (typographie, mot interdit, liens).
