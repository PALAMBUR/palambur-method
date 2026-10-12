# Exemple 03 · Devis

Données fictives · « Exemple SA », entreprise de carrelage de Suisse romande qui n’existe pas ; « Client X » est un particulier fictif. Gabarit : [`devis.md`](../../skills/palambur-method/gabarits/devis.md) · niveau **L** · un lot · **Étape 0 déclenchée** (nom et adresse du client).

## 1 · La demande brute

> prépare le devis pour la salle de bain de [nom et adresse réels dans la demande], 12 m² de carrelage au sol, on a visité hier

## 2 · L’ouverture · le premier message

Premier déclenchement : les **trois lignes fixes**, la ligne de **niveau de sensibilité**, puis la question binaire sur les données, seule.

> **Méthode Palambur.** Je vais d’abord vous poser quelques questions, une à la fois, pour ne rien inventer à votre place.
> Vous répondez par une lettre ou en texte libre ; si vous passez, une valeur prudente s’applique et reste visible.
> Vous recevrez ensuite deux blocs à copier : le **Gabarit Palambur**, réutilisable, puis le **Livrable**.
>
> Niveau de sensibilité · sensible (particulier nommé, adresse).

## 3 · Étape 0 · données nominatives

> Je détecte des données nominatives (le nom du client et l’adresse du chantier). Par défaut je les **anonymise partout** (« Client X », adresse remplacée par « [adresse du chantier] ») et j’ajoute une mention nLPD. Souhaitez-vous plutôt les **conserver telles quelles** ?

*Réponse retenue pour l’exemple : « conserve, c’est pour lui envoyer ».* Les vrais noms restent donc **partout** ; dans cet exemple public, ils sont remplacés par « Client X » et « [adresse du chantier] » pour la seule raison que l’exemple est fictif.

## 4 · Les questions, une par message

Le gabarit donne quatre questions. La demande répond déjà à la deuxième (« Client X » est un particulier) : le compteur annonce trois.

**Question 1 sur 3 · l’origine des prix**

D’où viennent les prix ?

A. grille tarifaire ou chiffrage interne validé, que je colle
B. tarif horaire et quantités relevées sur place, que je donne
C. les prix ne sont pas encore fixés · défaut si vous ne précisez pas
D. Autre / je ne sais pas

*Réponse retenue : B · tarif horaire CHF [À COMPLÉTER], 12 m² relevés, fourniture du carrelage par le client.*

**Question 2 sur 3 · le périmètre**

Ce qui est compris, ce qui ne l’est pas ?

A. prestation ferme et complète, tout ce qui est compris est listé · défaut si vous ne précisez pas
B. prestation ferme, plus des options chiffrées à part
C. une partie en régie, ou estimation révisable après visite technique
D. Autre / je ne sais pas

*Réponse retenue : B · option : dépose de l’ancien carrelage.*

**Question 3 sur 3 · les conditions**

Validité, acompte, délais ?

A. conditions standard maison (validité 30 jours, acompte à préciser, paiement 30 jours net) · défaut si vous ne précisez pas
B. nos conditions générales, que je colle
C. conditions particulières, que je dicte
D. Autre / je ne sais pas

*Réponse retenue : A.*

## 5 · La production · la ligne de contexte

Un défaut posé sans question : le point de départ du délai de début des travaux (réception de l’acompte et livraison du carrelage), parce qu’un délai nu n’engage à rien.

> Contexte retenu · devis · Client X, particulier · Suisse romande · ton clair, contractuel · données : conservées · 3 réponses, 1 défaut, 25 marqueurs

## 6 · Le bloc « Gabarit Palambur »

```
Gabarit Palambur

INSTRUCTION
Rédigez un devis pour la pose de carrelage au sol d’une salle de bain (12 m²) destiné à Client X, particulier, à [adresse du chantier]. Objectif : un devis compris au premier passage, qui dit ce qui est compris, ce qui ne l’est pas et ce qui pourrait faire monter la facture.

RÔLE ET AUDIENCE
Vous êtes responsable des devis chez Exemple SA, entreprise de carrelage de Suisse romande. Vous savez qu’un devis est aussi un document contractuel : ce qui n’est pas écrit n’est pas dû. Vous écrivez pour un client qui ne connaît pas le métier et doit comprendre ce qu’il achète sans appeler.

DONNÉES
<donnees>
• Objet et lieu d’exécution : pose de carrelage au sol, salle de bain, [adresse du chantier]
• Demande du client, dans ses mots : [À COMPLÉTER : reprendre la demande du client]
• Quantités relevées · matériaux choisis : 12 m² relevés sur place le [À COMPLÉTER : date de la visite] · carrelage fourni par le client, référence [À COMPLÉTER]
• Grille tarifaire ou chiffrage interne validé · tarif horaire si régie : tarif horaire CHF [À COMPLÉTER] · temps estimé par poste [À COMPLÉTER]
• Conditions d’accès et contraintes du site : [À COMPLÉTER : étage, ascenseur, stationnement]
• Statut TVA de l’entreprise · taux applicable : [À COMPLÉTER : statut TVA] · [À VÉRIFIER : taux applicable]
• Ce qui n’est pas compris · options : non compris : fourniture du carrelage, plomberie, électricité · option : dépose de l’ancien carrelage et évacuation
• Conditions (validité, acompte, paiement, délai et son point de départ) : validité 30 jours · acompte [À ARBITRER] · paiement 30 jours net · début des travaux [À COMPLÉTER : délai] après réception de l’acompte et livraison du carrelage par le client
</donnees>
• Si une donnée tarifaire manque, écrivez [À COMPLÉTER] à la place du prix : ne proposez jamais de fourchette.

CONTRAINTES
• N’inventez aucun prix, aucune quantité, aucun délai : l’IA met en forme, elle ne chiffre pas.
• N’appliquez aucun taux de TVA de votre propre initiative : s’il manque, n’affichez aucune ligne de TVA et écrivez [À COMPLÉTER : statut TVA] [À VÉRIFIER : taux applicable] (LTVA).
• Jamais d’unité ambiguë ; chaque poste dit ce qu’il comprend et ce qu’il exclut. Séparez le prix ferme de la régie. Écrivez les hypothèses sur lesquelles repose le prix.
• Obligation de moyens, pas de résultat. Garantie nommée (CO), durée [À VÉRIFIER : base légale].
• Le matériel fourni par le client n’est pas garanti par l’entreprise.
• Si une information manque, écrivez [À COMPLÉTER] et ne la remplacez jamais par une valeur plausible.

FORMAT
Devis d’une page : en-tête (IDE, TVA si assujettie) · client · objet · tableau Désignation | Quantité | Unité | Prix hors TVA | Total hors TVA · sous-total, TVA selon statut, total CHF · hypothèses · non compris · options · conditions · signature et bon pour accord. Encadré hors devis : ce qui doit être chiffré ou vérifié avant envoi.

MÉTHODE
1 · Décrire l’ouvrage avant de le chiffrer, poste par poste dans l’ordre du chantier. 2 · Écrire ce qui n’est pas compris. 3 · Nommer les hypothèses. 4 · Séparer ferme et régie. 5 · Poser les conditions. 6 · Relire du point de vue du client.

AUTO-CONTRÔLE
Chaque prix vient-il d’une personne nommée ? La liste des exclusions figure-t-elle ? Les hypothèses sont-elles écrites ? Le délai part-il d’un événement daté ? Un client qui ne connaît pas le métier comprendrait-il ce document sans appeler ?
```

## 7 · Le bloc « Livrable »

**Livrable**

**Exemple SA** · carrelage · IDE [À COMPLÉTER] · [À COMPLÉTER : mention TVA selon statut]

**Devis n° [À COMPLÉTER]** · Yverdon-les-Bains, le [À COMPLÉTER : date]

**Client X** · [adresse du chantier]

**Objet** · pose de carrelage au sol, salle de bain, 12 m²

| N° | Désignation | Quantité | Unité | Prix unitaire hors TVA | Total hors TVA |
|---|---|---|---|---|---|
| 1 | Protection des surfaces et préparation du support (nettoyage, contrôle de planéité) | 12 | m² | CHF [À COMPLÉTER] | CHF [À COMPLÉTER] |
| 2 | Pose collée du carrelage fourni par le client, joints compris | 12 | m² | CHF [À COMPLÉTER] | CHF [À COMPLÉTER] |
| 3 | Joints silicone en périphérie | [À COMPLÉTER] | ml | CHF [À COMPLÉTER] | CHF [À COMPLÉTER] |
| 4 | Déplacements (atelier · chantier) | [À COMPLÉTER] | forfait détaillé : [À COMPLÉTER : nombre de trajets] | CHF [À COMPLÉTER] | CHF [À COMPLÉTER] |

**Sous-total hors TVA** · CHF [À COMPLÉTER]
**TVA** · [À COMPLÉTER : statut TVA] `[À VÉRIFIER : taux applicable]` · aucune ligne tant que le statut n’est pas fourni
**Total** · CHF [À COMPLÉTER]

**Hypothèses du prix** · support plan et sain après dépose ; carrelage livré sur place par le client avant le début des travaux, en quantité suffisante (coupe comprise) ; accès [À COMPLÉTER] ; une seule validation du calepinage avant la pose.

**Non compris** · fourniture du carrelage, de la colle et des joints de couleur spéciale ; dépose de l’ancien revêtement (voir option) ; travaux de plomberie et d’électricité ; réparation du support si défauts cachés découverts après dépose (avenant écrit avant exécution).

**Option** · dépose de l’ancien carrelage et évacuation en décharge agréée · 12 m² · CHF [À COMPLÉTER] hors TVA.

**Conditions** · validité 30 jours · acompte de [À ARBITRER] à la commande · paiement à 30 jours net · début des travaux [À COMPLÉTER : délai] après réception de l’acompte et livraison du carrelage · garantie selon le Code des obligations (contrat d’entreprise), durée `[À VÉRIFIER : base légale]`, à compter de la réception de l’ouvrage · le matériel fourni par le client n’est pas couvert par cette garantie · obligation de moyens.

Lieu, date, signature Exemple SA · Bon pour accord, lieu, date, signature du client

*Vos données sont traitées en Suisse, conformément à la nLPD.*

---

**Encadré hors devis · à chiffrer ou vérifier avant envoi**
· Les quatre prix unitaires et l’option : chiffrés par [À COMPLÉTER : fonction de la personne qui tranche].
· Statut TVA d’Exemple SA et taux applicable : à confirmer avant d’écrire une ligne de TVA.
· Durée de la garantie : à vérifier au texte en vigueur.

## 8 · Le Journal de confiance

Le journal ne contient aucune donnée nominative, même quand l’utilisateur a choisi de conserver les noms.

```
Journal de confiance
· Niveau de sensibilité · sensible (particulier nommé, adresse)
· Données · conservées à votre demande
· Marqueurs posés · [À COMPLÉTER] ×22 (IDE, numéro et date du devis, prix unitaires et totaux, quantités, accès, délai, personne qui chiffre) · [À VÉRIFIER] ×2 (taux de TVA, durée de garantie) · [À ARBITRER] ×1 (acompte)
· Hypothèses refusées · aucune fourchette de prix ; aucun taux de TVA de mémoire ; aucune garantie chiffrée
· Relecture humaine · requise avant envoi (document contractuel)
```

## 9 · Ce qui n’a pas été inventé

- aucun prix, aucune fourchette « entre CHF 1'500.– et CHF 2'500.– » ;
- aucun taux de TVA de mémoire, aucune ligne de TVA sans statut ;
- aucune garantie « deux ans » affirmée ;
- aucun délai nu : le début des travaux part de deux événements datés ;
- aucun prix ferme sur ce qui se cache sous l’ancien carrelage.
