# Architectes & ingénieurs civils · fiche métier allégée

**Secteur** · Construction & immobilier · code 21 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 2142 Ingénieurs civils ; 2161 Architectes, architectes d’intérieur · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

L’architecte et l’ingénieur civil conçoivent, coordonnent et dirigent la réalisation d’un ouvrage pour un maître de l’ouvrage. Ils produisent des contrats de mandat, des notes de faisabilité, des dossiers d’autorisation, des procès-verbaux de chantier et des décomptes d’honoraires, pour des maîtres d’ouvrage privés ou publics, des autorités et des entreprises.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Mandat et honoraires · 6

- Premier rendez-vous · le besoin
- Présentation du bureau
- Contrat de mandat et honoraires
- Prestation supplémentaire
- Relance d’honoraires impayés
- Note d’honoraires et décompte

### Concours et marché public · 3

- Marché public de prestations
- Concours d’architecture
- Comparatif des soumissions

### Étude et faisabilité · 5

- Faisabilité sur une parcelle
- Estimation de coût
- Note d’aide à la décision
- Droit d’auteur sur les plans
- Performance énergétique

### Autorisation · 3

- Autorisation de construire
- Détermination sur opposition
- Amiante et substances dangereuses

### Coordination et chantier · 7

- Planning et chemin critique
- Coordination des spécialistes
- Versions de plans et BIM
- PV de séance de chantier
- Écart d’exécution ou retard
- Réception de l’ouvrage
- Sécurité sur le chantier

### Bureau et responsabilité · 6

- Dépassement de coût
- Bureau mis en cause
- Passation à l’exploitant
- Plan de charge du bureau
- Règle IA au bureau
- Relance ou refus · trois lignes

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

maître de l’ouvrage · mandataire · contrat de mandat · honoraires · phases SIA · avant-projet · projet de l’ouvrage · autorisation de construire · mise à l’enquête · opposition · appel d’offres · soumission · tableau comparatif · direction des travaux · PV de séance de chantier · réception de l’ouvrage · avis des défauts · dossier de l’ouvrage exécuté · BIM · estimation des coûts · degré de précision · prestation supplémentaire · concours · mandats d’étude parallèles

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-21-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| CO | le contrat de mandat, la responsabilité du mandataire et le contrat d’entreprise | 9 sur 30 |
| SIA | les règlements de prestations et honoraires et les normes techniques, quand le contrat les intègre | 3 sur 30 |
| SIA 118 | les conditions générales d’exécution des travaux, si convenues | 1 sur 30 |
| LDA | le droit d’auteur sur les plans et le projet | 4 sur 30 |
| nLPD | les données des maîtres d’ouvrage, des voisins opposants et des entreprises | 23 sur 30 |
| LMP | les marchés publics fédéraux de prestations | 1 sur 30, en toutes lettres ¹ |
| AIMP | les marchés publics cantonaux et les concours | 1 sur 30 |
| PA | la procédure devant une autorité fédérale | 1 sur 30, en toutes lettres ¹ |
| LTr | les horaires du bureau | 1 sur 30 |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Dans quel canton se situe l’ouvrage ?** · Le droit des constructions est cantonal ; pièces, délais et autorités changent d’un canton à l’autre.
2. **Le contrat intègre-t-il les règlements SIA, et lesquels ?** · Une norme SIA ne lie que si le contrat la mentionne ; le modèle ne doit pas la présumer.
3. **À quelle phase en est le projet ?** · Le degré de précision d’une estimation et le contenu d’un livrable dépendent de la phase.
4. **Qui est le destinataire · maître d’ouvrage, autorité, entreprise, assureur ?** · Un écart de chantier se décrit autrement selon qu’il va à l’entreprise ou à l’assureur du bureau.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Présenter une norme SIA comme une loi qui s’applique d’office.
- Inventer des délais d’opposition, de recours ou de validité du permis sans nommer le canton.
- Calculer des honoraires d’après le coût de l’ouvrage comme si le barème était encore en vigueur.
- Affirmer que les plans « appartiennent » au client parce qu’il les a payés.
- Transposer la loi MOP française, les éléments de mission ESQ/APS/APD et la décennale.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Noms des maîtres d’ouvrage privés et des opposants
- Montants d’honoraires et estimations de coût
- Désaccords consignés en séance de chantier
- Dossiers de mise en cause et échanges avec l’assureur RC
- Plans et données de propriétés privées
