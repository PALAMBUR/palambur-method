# Exemple 02 · Relance de facture

Données fictives · « Exemple SA », menuiserie de Suisse romande qui n’existe pas ; « Client X » est une gérance fictive. Gabarit : [`relance-facture.md`](../skills/palambur-method/gabarits/relance-facture.md) · niveau **M** · un lot · **Étape 0 déclenchée** (nom du client, montant, numéro de facture).

## 1 · La demande brute

> méthode palambur : rédige une relance pour la facture 2026-0148 de la gérance [nom réel dans la demande], 4'820 CHF, échue le 15.06.2026

Le mot « palambur » déclenche. La demande porte un nom d’entreprise et un montant : l’Étape 0 passe avant tout.

## 2 · Étape 0 · données nominatives

Le skill pose **une seule question, sans compteur, seule dans son message** :

> Je détecte des données nominatives (le nom de la gérance, le montant, le numéro de facture). Par défaut je les **anonymise partout** (« Client X », « Montant A ») et j’ajoute une mention nLPD. Souhaitez-vous plutôt les **conserver telles quelles** ?

*Réponse retenue pour l’exemple : « anonymise ».* La décision s’applique partout, prompt et livrable. Le montant et la date de la facture restent tels quels : ils ne désignent personne et la relance en a besoin ; c’est le nom du client qui devient « Client X ».

## 3 · Les questions, une par message

Le gabarit donne quatre questions. Aucune n’est déjà répondue par la demande : le compteur annonce quatre.

**Question 1 sur 4 · le degré**

À quel degré en est-on ?

A. premier rappel courtois, oubli supposé · défaut si vous ne précisez pas
B. deuxième rappel ferme, un rappel a déjà été envoyé
C. mise en demeure, seule ou avec toute la séquence préparée
D. Autre / je ne sais pas

*Réponse retenue : B, un rappel a été envoyé par courriel le 30.06.2026.*

**Question 2 sur 4 · la contestation**

Existe-t-il une contestation, même orale ?

A. aucune, silence pur
B. une réserve ou une réclamation sur la prestation a été exprimée
C. une promesse de paiement a été faite et non tenue
D. Autre / je ne sais pas · défaut si vous ne précisez pas

*Réponse retenue : A.*

**Question 3 sur 4 · la suite décidée**

Quelle suite est réellement décidée par la direction si le délai passe ?

A. aucune encore, on veut d’abord être payé et garder le client · défaut si vous ne précisez pas
B. suspension des livraisons ou des prestations
C. transmission au recouvrement ou poursuite
D. Autre / je ne sais pas

*Réponse retenue : A.*

**Question 4 sur 4 · les conditions générales**

Vos conditions générales prévoient-elles des intérêts ou des frais de rappel ?

A. aucune condition écrite, seul le principal est réclamé · défaut si vous ne précisez pas
B. oui, je colle la clause
C. Autre / je ne sais pas

*Réponse retenue : A.*

## 4 · Le Gabarit Palambur rempli

```
INSTRUCTION
Rédigez une relance ferme pour la facture 2026-0148 de Client X, d’un montant de CHF 4'820.–, échue le 15.06.2026, après un premier rappel resté sans réponse. Objectif : obtenir le paiement sans abîmer la relation et sans affaiblir le dossier si la poursuite devenait nécessaire.

RÔLE ET AUDIENCE
Vous êtes responsable du recouvrement chez Exemple SA, menuiserie de Suisse romande, à l’aise avec le CO (demeure) et la pratique de la LP, et vous écrivez pour être payé·e, pas pour avoir raison. Votre lecteur est la comptabilité fournisseurs de Client X : il reçoit trente relances par semaine et ne lit que la première ligne et le montant.

DONNÉES
<donnees>
• Facture (numéro, date, échéance, montant, prestation) : 2026-0148 · émise le [À COMPLÉTER] · échue le 15.06.2026 · CHF 4'820.– · [À COMPLÉTER : prestation]
• Client et fonction à relancer : Client X (gérance) · comptabilité fournisseurs
• Conditions de paiement convenues (délai, intérêts, frais) : aucune condition écrite ; seul le principal est réclamé
• Rappels déjà envoyés (dates, canal, réponse) : 30.06.2026 · courriel · aucune réponse
• Contestation ou réserve connue, même orale : aucune
• Suite décidée par la direction si le délai passe : aucune encore
• Délai accordé : 10 jours [À ARBITRER]
• Coordonnées de paiement (IBAN, titulaire, référence) : [À COMPLÉTER]
</donnees>
• Si une contestation existe, arrêtez la séquence et dites-le : la contestation se traite à part.

CONTRAINTES
• N’inventez aucun taux d’intérêt, aucun frais de rappel, aucun délai légal, aucun montant, aucun IBAN : tout vient des DONNÉES ou porte [À COMPLÉTER].
• Nommez les lois (CO pour la demeure, LP pour la poursuite), ne citez jamais un numéro d’article : écrivez [À VÉRIFIER : base légale].
• Aucune menace qui ne serait pas tenue ; aucune suite annoncée que la direction n’a pas décidée.
• Aucune allusion à des tiers, à la réputation du client, aucun ton humiliant (LCD).
• Les données du client ne sortent pas vers un tiers sans base (nLPD).
• Ton ferme et courtois ; la fermeté vient des dates, jamais du vocabulaire. Vouvoiement, aucune excuse.
• Si une information manque, écrivez [À COMPLÉTER] et ne la remplacez jamais par une valeur plausible.

FORMAT
Un courriel de 120 mots environ : objet · faits datés (facture, échéance, rappel précédent) · demande unique avec date · coordonnées de paiement · contact · ouverture. Bloc interne non envoyé : prochaine étape et date de passage de main.
```

## 5 · Le livrable

**Objet : Facture 2026-0148 · CHF 4'820.– · deuxième rappel**

Madame, Monsieur,

Notre facture 2026-0148 du [À COMPLÉTER : date d’émission], d’un montant de CHF 4'820.–, est échue depuis le 15.06.2026. Notre rappel du 30.06.2026 est resté sans réponse.

Nous vous prions de régler ce montant d’ici au [À COMPLÉTER : date, 10 jours après l’envoi · délai à arbitrer] sur le compte suivant :

IBAN [À COMPLÉTER] · Exemple SA · référence 2026-0148.

Si un élément de cette facture vous pose question, ou si un paiement est déjà en cours, appelez-nous au [À COMPLÉTER : numéro de la comptabilité] : nous préférons en parler plutôt que vous écrire une troisième fois.

Avec nos salutations les meilleures,

[Fonction du signataire] · Exemple SA

*Vos données sont traitées en Suisse, conformément à la nLPD.*

---

**Bloc interne · non envoyé**
· Si aucun paiement ni appel au [date du délai] : la direction décide de la suite (arrangement, suspension, mise en demeure). Rien n’a été annoncé au client, rien n’est donc dû.
· La mise en demeure, si elle vient, part en courrier recommandé et porte « projet · ne pas envoyer sans visa de la direction ». Elle nomme le CO (demeure) et la LP comme suite possible, sans chiffrer de délai légal `[À VÉRIFIER : base légale]`.
· Correspondance d’anonymisation : « Client X » = la gérance nommée dans la demande ; à rétablir dans la version envoyée.

## 6 · Ce qui n’a pas été inventé

- aucun taux d’intérêt moratoire, aucun frais de rappel ;
- aucun IBAN plausible ;
- aucune menace de poursuite au deuxième rappel : la direction n’a rien décidé ;
- aucun article du CO ni de la LP ;
- la date d’émission et la prestation facturée, absentes de la demande, restent `[À COMPLÉTER]` ; le solde n’a pas été recalculé.
