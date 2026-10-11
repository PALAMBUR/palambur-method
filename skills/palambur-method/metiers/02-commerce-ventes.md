# Commerce & ventes · fiche métier allégée

**Secteur** · Fonctions transverses · code 02 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 3322 Représentants et techniciens commerciaux · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

Le commercial prospecte, qualifie, propose et conclut. Il produit des offres, des réponses à appel d’offres, des argumentaires, des relances et des comptes rendus de visite, pour des acheteurs d’entreprises, des adjudicateurs publics et sa propre direction.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Prospection · 5

- Recherche sur un prospect
- Cold email de prospection
- Plan de chasse mensuel
- Préparation d’un salon
- Cartographie des décideurs

### Offre et appel d’offres · 5

- Devis à partir d’un brief
- Réponse à un appel d’offres
- Soutenance d’appel d’offres
- Répondre ou renoncer
- Questionnaire fournisseur

### Entretien et négociation · 5

- Discovery call
- Argumentaire par persona
- Négociation d’une remise
- Pitch de 30 secondes
- Phrase de closing

### Relance et suivi · 5

- Relance commerciale
- Compte-rendu de RDV
- Comptes dormants à réactiver
- Demande de référence client
- Message commercial trop long

### Prix et conditions · 5

- Conditions générales de vente
- Hausse tarifaire
- Grille de remises
- Retard ou rupture · le client
- Qualification d’un revendeur

### Portefeuille et litige · 5

- Audit du pipeline
- Analyse d’une affaire perdue
- Plan de compte clé
- Créance impayée
- Client mécontent

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

offre · devis · conditions générales de vente · délai de validité · conditions de paiement · escompte · remise · appel d’offres · soumission · adjudication · critères d’adjudication · cahier des charges · compte rendu de visite · pipeline · qualification · objection · prix de revient · marge brute · TVA · Incoterms · exclusivité · contrat cadre

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-02-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| CO | la formation du contrat, l’offre et son acceptation, la vente et la garantie | 2 sur 30 |
| LCD | la publicité comparative, les allégations et le dénigrement d’un concurrent | 3 sur 30 |
| LTVA | la TVA mentionnée sur toute offre et facture | 2 sur 30, en toutes lettres ¹ |
| nLPD | les fichiers de prospects et les données de contact | 10 sur 30 |
| AIMP | les marchés publics cantonaux et communaux | 4 sur 30 |
| LMP | les marchés publics fédéraux | 3 sur 30, dont 2 en toutes lettres ¹ |
| OMP | l’ordonnance d’application des marchés publics fédéraux | 1 sur 30 |
| LP | le recouvrement d’une créance commerciale impayée | 2 sur 30 |
| ISO 9001 | la qualité, quand le client l’exige dans son appel d’offres | 1 sur 30 |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Le client est-il privé ou un adjudicateur public ?** · Un marché public impose procédure, critères et délais ; une offre privée se négocie.
2. **Quel est le périmètre exclu de l’offre ?** · C’est l’exclusion qui protège la marge et évite le litige, pas la liste des inclusions.
3. **Prix, TVA, délai de validité et conditions de paiement sont-ils arrêtés ?** · Sans ces quatre champs, le modèle invente des conditions commerciales et les présente comme vôtres.
4. **Quel ton · première approche, relance ferme, réponse à une objection ?** · La relance commerciale se gradue ; le ton se décide avant d’écrire.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Inventer un prix de marché, une remise « habituelle » ou un délai de livraison.
- Affirmer un seuil de marché public en francs sans le vérifier dans l’AIMP ou la LMP en vigueur.
- Comparer nommément un concurrent en des termes que la LCD interdit.
- Promettre une exclusivité ou une garantie que le signataire n’a pas accordée.
- Omettre la TVA ou la mentionner de façon ambiguë.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Noms et coordonnées des prospects et contacts chez le client
- Prix négociés et marges
- Contenu d’une soumission avant l’ouverture des offres
- Historique d’impayés d’un client
- Conditions accordées à un autre client
