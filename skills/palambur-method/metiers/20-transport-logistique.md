# Transport & logistique · fiche métier allégée

**Secteur** · Industrie, atelier & mobilité · code 20 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 1324 Directeurs et cadres de direction, approvisionnement, distribution et assimilés · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

Le transport et la logistique déplacent, stockent et livrent, à l’heure et sans casse. Ils produisent des plannings, des consignes aux chauffeurs, des réponses à réclamation, des contrats de transport et des rapports d’incident, pour des clients expéditeurs, des chauffeurs et des autorités.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Offre et contrat · 6

- Offre pour tournée régulière
- Prix de revient au kilomètre
- Indexation carburant
- Réponse au cahier des charges
- Devis de déménagement
- Contrat de prestation logistique

### Exploitation et tournées · 5

- Plan de tournée
- Planning des chauffeurs
- Tableau de bord mensuel
- Affréter un confrère
- Refuser ou décaler une course

### Conducteurs et véhicules · 6

- Durées de conduite et de repos
- Entretien du parc
- Recruter un chauffeur
- Permis et formation continue
- Redevance poids lourds
- Consommation et émissions

### Charge et sécurité · 4

- Contrôle avant départ
- Marchandises dangereuses
- Accident d’un véhicule
- Document reçu après contrôle

### Entrepôt et marchandise · 5

- Réception de marchandise
- Chaîne du froid
- Inventaire et écarts
- Comptes de palettes
- Dossier douanier

### Litige et assurance · 4

- Géolocalisation des chauffeurs
- Incident de livraison · réponse
- Responsabilité du transporteur
- Avarie ou perte de marchandise

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

lettre de voiture · tournée · créneau de livraison · quai · palette · chargement · arrimage · tachygraphe · temps de conduite · temps de repos · ADR · marchandises dangereuses · affrètement · sous-traitant transporteur · avarie · réserve à la livraison · franco · incoterm · entrepôt · inventaire · picking · cross-docking · retour

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-20-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| OTR | les durées de conduite et de repos des chauffeurs | 2 sur 30 |
| LCR | la circulation routière et les véhicules | 3 sur 30 |
| LTr | la durée du travail du personnel de quai et d’entrepôt | 4 sur 30 |
| CCT | la convention collective de la branche quand elle s’applique | 6 sur 30 |
| CO | le contrat de transport et la responsabilité pour avarie | 4 sur 30 |
| nLPD | les données des chauffeurs, la géolocalisation et les données des destinataires | 18 sur 30 |
| LAA | les accidents de travail et de la circulation professionnelle | 1 sur 30 |

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Le texte s’adresse-t-il au client expéditeur, au chauffeur ou à une autorité ?** · Une consigne de sécurité et une réponse à réclamation n’ont rien en commun.
2. **Quelles sont les contraintes de temps · créneaux, repos obligatoires, fermetures ?** · Un planning qui ignore les repos de l’OTR est faux, et le modèle ne connaît pas vos repos.
3. **Y a-t-il des marchandises dangereuses, du froid ou du fragile ?** · Chaque cas ajoute des mentions et des responsabilités.
4. **Qui porte le risque de l’avarie, et à quel moment ?** · Les réserves à la livraison et les incoterms se décident avant d’écrire la réponse.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Inventer des durées maximales de conduite ou des temps de repos en les attribuant à l’OTR.
- Chiffrer une indemnité d’avarie sans contrat ni convention.
- Confondre la responsabilité du transporteur et celle de l’expéditeur pour l’emballage.
- Transposer le droit français du transport (contrat type, lettre de voiture CMR obligatoire en national).
- Promettre un créneau que le planning ne tient pas.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Noms et adresses des destinataires
- Données de géolocalisation et du tachygraphe des chauffeurs
- Infractions et accidents des chauffeurs
- Tarifs négociés avec les clients et les sous-traitants
- Contenu et valeur des marchandises
