# ADV & service client · fiche métier allégée

**Secteur** · Fonctions transverses · code 03 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 4110 Employés de bureau, fonctions générales · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

L’administration des ventes et le service client tiennent la relation après la signature : commandes, factures, réclamations, relances et retours. Ils produisent des courriers, des courriels, des scripts et des procédures, pour des clients, des transporteurs et les équipes internes.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Demande entrante et devis · 5

- Réponse client en 5 langues
- Devis depuis une demande
- Réponse à une comparaison de prix
- Qualification d’une demande
- FAQ client

### Commande et livraison · 5

- Accusé de réception de commande
- Commande en lignes structurées
- Planning de livraison
- Anomalies dans les commandes
- Alerte de rupture de stock

### Réclamation et litige · 6

- Réclamation client
- Litige fournisseur
- Retour produit et SAV
- Rappel produit
- Transmission à l’assurance
- Règles d’escalade

### Paiement et conditions · 4

- Relance de paiement
- Demande nLPD d’un client
- Engagements de service
- Dire non sans perdre le client

### Suivi et reporting · 6

- Note CRM après un appel
- Upsell et cross-sell
- Revue mensuelle de portefeuille
- Reporting hebdomadaire ADV
- Audit ISO 9001 · volet ADV
- Enquête de satisfaction

### Dossier et passation · 4

- Migration de catalogue produit
- Passation d’un portefeuille
- Lancement d’une commande
- Réponse client en langage clair

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

confirmation de commande · bon de livraison · facture · note de crédit · relance · rappel · mise en demeure · délai de paiement · réclamation · retour marchandise · avoir · garantie · délai de livraison · rupture de stock · suivi d’expédition · escalade · ticket · accusé de réception · conditions générales · registre des traitements

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-03-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| CO | la vente, la livraison, le retard, la garantie et la mise en demeure | 5 sur 30 |
| LTVA | la facture et la note de crédit | 3 sur 30, en toutes lettres ¹ |
| nLPD | les données clients dans le CRM et les échanges | 25 sur 30 |
| RGPD | les clients établis dans l’Union européenne | 21 sur 30 |
| ISO 9001 | le traitement des réclamations quand l’entreprise est certifiée | 2 sur 30 |
| LP | la poursuite après l’échec des relances | 1 sur 30 |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Quel est l’objet précis · facture, commande, livraison, et son identifiant ?** · Le modèle ne doit pas inventer un numéro ni une date ; sans eux il pose un marqueur [À COMPLÉTER].
2. **Où en est l’historique · premier rappel, deuxième, mise en demeure ?** · L’escalade est graduée ; sauter une étape abîme la relation ou affaiblit la créance.
3. **Ton attendu · conciliant, ferme, final ?** · Le même impayé se traite autrement selon la valeur du client.
4. **Le client est-il en Suisse ou dans l’Union européenne ?** · Cela décide entre nLPD et RGPD, et change les mentions de la correspondance.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Inventer des intérêts moratoires, des frais de rappel ou des délais légaux de paiement.
- Menacer d’une poursuite avec une procédure décrite de façon inexacte.
- Promettre un geste commercial que l’entreprise n’a pas validé.
- Confondre garantie légale et garantie commerciale.
- Recopier des données nominatives dans un script ou une FAQ destinée à être partagée.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Noms, adresses et coordonnées des clients
- Montants dus et historique de paiement
- Contenu des réclamations et des litiges
- Données bancaires sur les factures et avoirs
- Numéro AVS d’un client, jamais demandé au premier contact
- Conditions particulières accordées à un client
