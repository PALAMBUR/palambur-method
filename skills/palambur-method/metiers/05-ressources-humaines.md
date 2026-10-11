# Ressources humaines · fiche métier allégée

**Secteur** · Fonctions transverses · code 05 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 2423 Spécialistes, ressources humaines et évolution de carrière · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

Les ressources humaines recrutent, contractualisent, accompagnent et séparent. Elles produisent des offres d’emploi, des contrats, des avertissements, des certificats, des règlements et des plans d’égalité, pour des candidats, des collaborateurs, des cadres et des autorités.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Recrutement · 6

- Offre d’emploi
- Tri et scoring de CV
- Entretien de recrutement
- Assessment center
- Refus après entretien
- Annonce · version par canal

### Engagement et contrat · 5

- Contrat de travail
- Plan d’onboarding J1 → J90
- Contrat d’apprentissage
- Engagement d’un frontalier
- Fiche de fonction

### Suivi et évaluation · 5

- Entretien annuel
- Plan de formation annuel
- Entretien RH · compte rendu
- Matrice de compétences d’équipe
- Retour après absence longue

### Sanction et fin de rapport · 5

- Réponse à une démission
- Certificat de travail
- Avertissement écrit
- Licenciement ordinaire
- Médiation d’un conflit

### Climat et communication · 4

- Communication interne sensible
- Signalement de harcèlement
- Sondage interne anonyme
- Bilan social annuel

### Conformité et données · 5

- Règle IA en entreprise
- Suivi de la masse salariale
- Égalité salariale · Logib
- Politique de télétravail
- Dossier du personnel · nLPD

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

contrat de travail · temps d’essai · délai de congé · certificat de travail · attestation de travail · avertissement · licenciement · convention de départ · règlement du personnel · cahier des charges · entretien d’évaluation · taux d’occupation · 13e salaire · LPP · CCT applicable · protection de la personnalité · analyse de l’égalité salariale · heures supplémentaires · travail supplémentaire · télétravail · congé maternité · APG · permis de séjour et de travail

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-05-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| CO | le contrat de travail, le temps d’essai, le congé, le certificat et la protection de la personnalité | 12 sur 30 |
| LTr | la durée du travail, le repos, le travail de nuit et du dimanche, l’enregistrement du temps | 8 sur 30 |
| OLT 3 | la protection de la santé au poste de travail | 1 sur 30 |
| LEg | l’égalité femmes-hommes et l’analyse de l’égalité salariale | 14 sur 30 |
| nLPD | le dossier du personnel, le recrutement, la surveillance et les transferts de données | 25 sur 30, dont 2 en toutes lettres ¹ |
| CCT | la convention collective applicable à la branche, quand il y en a une | 10 sur 30, dont 1 en toutes lettres ¹ |
| LAA | l’assurance-accidents obligatoire | 3 sur 30 |
| LPP | la prévoyance professionnelle | 4 sur 30, dont 1 en toutes lettres ¹ |
| LAVS | les cotisations sociales | 1 sur 30, en toutes lettres ¹ |
| LFPr | le contrat d’apprentissage | 2 sur 30, en toutes lettres ¹ |
| AI Act | la transparence des outils d’IA utilisés en recrutement quand le marché européen est visé | 1 sur 30 |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Quel canton, et quelle CCT s’applique, s’il y en a une ?** · Les délais, salaires minimaux et jours fériés dépendent du canton et de la CCT ; le modèle ne doit pas les deviner.
2. **Quel est le taux d’occupation, le type de contrat et la date d’entrée ?** · Ces trois champs structurent une offre comme un contrat ; ils ne se remplacent pas par un défaut.
3. **Le texte sera-t-il lu par la personne concernée ou par un tiers · autorité, assureur, tribunal ?** · Un avertissement ou un certificat change de registre selon qui le lira ensuite.
4. **Y a-t-il des données nominatives · nom, salaire, motif, état de santé ?** · Elles déclenchent l’anonymisation par défaut et les garde-fous LEg et nLPD.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Inventer un délai de congé, un salaire minimal ou un nombre de semaines de vacances en l’attribuant à une CCT.
- Citer un article du CO ou de la LTr avec un numéro précis sans vérification.
- Glisser un critère d’âge, de sexe, d’origine, d’état civil ou de santé dans une offre ou un entretien.
- Transposer des notions françaises · rupture conventionnelle, CDI/CDD au sens du Code du travail, préavis légal uniforme.
- Présenter un modèle de contrat comme valable dans tous les cantons et toutes les branches.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Nom, adresse, date de naissance et numéro AVS du collaborateur
- Salaire, bonus et évaluations
- Motif d’un licenciement ou d’un avertissement
- Certificats médicaux, incapacité de travail, grossesse
- Permis de séjour, nationalité, situation familiale
- Données de candidats non retenus
