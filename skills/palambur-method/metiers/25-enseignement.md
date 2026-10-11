# Enseignement scolaire et professionnel · fiche métier allégée

**Secteur** · Public, santé & accueil · code 25 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 2320 Professeurs, enseignement technique et professionnel ; 2330 Professeurs, enseignement secondaire ; 2341 Instituteurs, enseignement primaire · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

L’enseignant enseigne, évalue et accompagne un élève ou un apprenti, de la classe à la formation professionnelle. Il produit des séquences alignées sur le PER, des plans d’intervention, des grilles d’évaluation, des communications aux parents, des comptes rendus de conseil de classe et des rapports de visite en entreprise, pour des élèves, des parents, des collègues, des directions et des entreprises formatrices.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Cours et séquences · 3

- Séquence alignée sur le PER
- Différenciation pédagogique
- Projet interdisciplinaire

### Élèves à besoins particuliers · 2

- Plan d’intervention élève
- Adaptation pour l’inclusion

### Évaluation · 3

- Retour formatif
- Grille d’évaluation sommative
- Bilan de fin d’année

### Parents et famille · 4

- Communication à un parent
- Présentation de l’année
- Réunion de parents
- Communication de crise

### Vie de classe · 5

- Gestion d’un incident en classe
- Outil numérique pour la classe
- Suivi disciplinaire
- Entretien avec un élève
- Charte de classe

### Équipe pédagogique · 4

- Conseil de classe
- Intervenant externe
- Retour à un collègue
- Développement professionnel

### Formation professionnelle · 9

- Évaluation d’un·e apprenti·e
- Procédure de qualification
- Entreprise formatrice
- Apprenti·e en difficulté
- Plan de cours du métier
- Visite en entreprise
- Adultes en reconversion
- Refus ou réorientation
- Portfolio de l’apprenti·e

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

Plan d’études romand · cycle 1, 2, 3 · domaine disciplinaire · formation générale · capacités transversales · séquence d’enseignement · différenciation pédagogique · plan d’intervention · élève présentant des besoins spéciaux · inclusion · évaluation formative · évaluation sommative · note sur 6 · conseil de classe · représentants légaux · discernement · charte de classe · entreprise formatrice · contrat d’apprentissage · ordonnance de formation · plan de formation · procédure de qualification · portfolio · HarmoS · HEP · HEFP

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-25-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| PER | le Plan d’études romand, cadre des contenus de la scolarité obligatoire | 5 sur 30 |
| LFPr | la formation professionnelle, le contrat d’apprentissage, l’entreprise formatrice et la procédure de qualification | 4 sur 30, en toutes lettres ¹ |
| nLPD | citée par les invites comme repère ; à l’école publique c’est la loi cantonale sur la protection des données qui s’applique | 6 sur 30, dont 3 en toutes lettres ¹ |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Quel degré et quel canton · primaire, secondaire, école professionnelle ?** · Le vocabulaire, le statut et les règles de communication aux parents dépendent du degré et du canton.
2. **Qui lit · élève, parents, collègue, direction, entreprise formatrice ?** · Un même constat s’écrit différemment pour chacun, et certaines informations ne vont pas à tous.
3. **Quelle est l’exigence du PER ou du plan de formation visée ?** · Une séquence ou une grille sans objectif nommé est générique ; le modèle doit partir du vôtre.
4. **Le texte parle-t-il d’un élève identifiable, d’un diagnostic ou d’une situation familiale ?** · Donnée sensible : anonymiser, et vérifier qui a le droit de la recevoir.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Noter sur 20 et parler de « professeur des écoles » ou d’agrégation.
- Mettre un handicap ou un diagnostic dans une liste de classe.
- Informer les parents automatiquement quand l’élève a le discernement.
- Recommander un outil numérique grand public sans vérification de l’établissement.
- Confondre l’école professionnelle et l’entreprise formatrice.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Nom de l’élève, notes, diagnostics et mesures d’aide
- Situation familiale et données des représentants légaux
- Incidents disciplinaires et signalements
- Données de l’apprenti et de l’entreprise formatrice
- Évaluations de collègues après observation
