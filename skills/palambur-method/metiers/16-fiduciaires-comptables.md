# Fiduciaires & cabinets comptables · fiche métier allégée

**Secteur** · Conseil, chiffres & numérique · code 16 · 31 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 2411 Experts comptables ; 2412 Conseillers en finances et investissements ; 3313 Professions intermédiaires de la comptabilité · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

La fiduciaire boucle, déclare et conseille sous secret. Elle produit des lettres de mission, des offres d’honoraires, des commentaires de comptes, des notes TVA, des réponses à l’administration fiscale et des convocations d’assemblée, pour des indépendants, des sociétés, des banques et des administrations.

## 2 · Les tâches types

Les 31 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Mandat et honoraires · 6

- Lettre de mission
- Acceptation de mandat · LBA
- Offre d’honoraires
- Hausse d’honoraires
- Fin de mandat et restitution
- Détail des heures facturées

### Bouclement et comptes · 5

- Points d’attention du bouclement
- Commentaire des comptes annuels
- Plan de trésorerie
- Bouclement d’un indépendant
- Reprise d’un mandat au confrère

### Fiscalité et TVA · 5

- Relance des documents fiscaux
- Note TVA · décompte et écart
- Réponse à l’administration fiscale
- Impôt à la source
- Calendrier fiscal et social

### Salaires et assurances sociales · 4

- Certificat de salaire
- Contrôle AVS ou TVA annoncé
- Affiliation d’un collaborateur
- Attestation pour la banque

### Client au quotidien · 5

- Ouverture d’un dossier client
- Entretien client · compte rendu
- Reformuler en langage client
- Recouvrement des honoraires
- Contestation d’honoraires

### Société et conformité · 6

- Règle IA et anonymisation
- Convocation et PV d’assemblée
- Raison individuelle ou Sàrl
- Protection des données du cabinet
- Recrutement d’un collaborateur
- Régime de contrôle des comptes

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

lettre de mission · mandat · honoraires · bouclement · comptes annuels · bilan · compte de résultat · annexe · plan de trésorerie · solvabilité · décompte TVA · méthode effective · taux de la dette fiscale nette · impôt préalable · impôt à la source · certificat de salaire · caisse de compensation · affiliation · contrôle AVS · organe de révision · contrôle restreint · contrôle ordinaire · opting-out · raison individuelle · Sàrl · ayant droit économique · LBA · secret professionnel

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-16-*` (31 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| LTVA | le décompte, la méthode et les corrections de TVA | 9 sur 31, dont 8 en toutes lettres ¹ |
| CO | la tenue des comptes, la révision, les sociétés et le mandat | 6 sur 31 |
| nLPD | les dossiers clients, l’archivage et les sous-traitants | 6 sur 31 |
| LBA | la diligence anti-blanchiment pour les activités d’intermédiaire financier | 2 sur 31 |
| LIFD | l’impôt fédéral direct | 1 sur 31 |
| LHID | l’harmonisation des impôts directs cantonaux | 1 sur 31 |
| LAVS | l’affiliation et les cotisations | 1 sur 31 |
| LPP | la prévoyance professionnelle des collaborateurs du client | 3 sur 31, dont 1 en toutes lettres ¹ |
| LAA | l’assurance-accidents du client employeur | 2 sur 31 |
| LAFam | les allocations familiales | 1 sur 31, en toutes lettres ¹ |
| LP | le recouvrement des honoraires | 1 sur 31 |
| CP | le secret et les infractions comptables | 1 sur 31 |
| CCT | la convention de branche applicable au client | 1 sur 31, en toutes lettres ¹ |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Quelle forme juridique et quel canton pour le client ?** · Impôts, régime de révision et affiliations dépendent de la forme et du canton.
2. **Qui lit · le client, une banque, l’administration fiscale, un confrère ?** · Un commentaire de comptes au client se vulgarise ; une réponse à l’AFC se tient au fait.
3. **Quels chiffres faites-vous entrer, et pour quel exercice ?** · Le modèle ne calcule rien de fiable ; il met en forme vos chiffres et marque le reste.
4. **Le document engage-t-il la fiduciaire · attestation, lettre de mission, acceptation de mandat ?** · Alors le périmètre de responsabilité s’écrit avant tout le reste.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Inventer des seuils TVA, de révision ou d’assujettissement LBA en francs.
- Généraliser le délai d’annonce AVS d’une caisse à toutes les autres.
- Recommander une méthode de décompte TVA sans vérifier toutes ses conditions.
- Transposer la liasse fiscale, la DSN et le dépôt des comptes au greffe français.
- Produire une attestation chiffrée pour une banque sans les pièces.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Comptes, résultats et déclarations fiscales des clients
- Salaires et certificats de salaire des collaborateurs du client
- Identité de l’ayant droit économique
- Échanges avec l’administration fiscale et contrôles en cours
- Projets de restructuration ou de cession du client
