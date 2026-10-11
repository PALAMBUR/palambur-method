# Administrations & communes · fiche métier allégée

**Secteur** · Public, santé & accueil · code 15 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 3343 Secrétaires d’administration et secrétaires exécutifs · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

L’administration communale décide en collège, motive et informe. Elle produit des préavis, des décisions motivées, des règlements, des réponses aux citoyens, des avis d’enquête et des communiqués, pour l’organe délibérant, les habitants, les sociétés locales, la presse et les autorités cantonales.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Séance et organe délibérant · 5

- PV de séance et communiqué
- Préavis à l’organe délibérant
- Convocation et ordre du jour
- Réponse à une motion ou question
- Rapport de gestion annuel

### Acte et règlement · 5

- Projet de règlement communal
- Décision administrative motivée
- Traitement des oppositions
- Règlement en langage clair
- Dossier de naturalisation

### Marché public · 3

- Cahier des charges du marché
- Rapport d’adjudication
- Autorisation de manifestation

### Citoyen et guichet · 6

- Réponse à un courrier citoyen
- Réponse à une demande d’accès
- Rappel de facture communale
- Usage d’une salle communale
- Subvention · réponse au requérant
- Nuisance ou incivilité

### Information et presse · 6

- Avis de mise à l’enquête
- Communiqué de presse communal
- Information à la population
- Communication de crise communale
- Demande de presse et interview
- Séance publique d’information

### Finances, RH et données · 5

- Règle IA à la commune
- Présentation du budget
- Registre des traitements
- Recrutement à l’administration
- Personnel et vidéosurveillance

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

exécutif communal · organe délibérant · préavis · séance · procès-verbal · décision motivée · voies de droit · délai de recours · règlement communal · mise à l’enquête · opposition · autorisation de manifestation · domaine public · marché public · adjudication · naturalisation · préavis communal · demande d’accès aux documents officiels · principe de transparence · registre des traitements · vidéosurveillance · budget communal · taxe · rappel · communiqué

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-15-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| LPrD | la loi cantonale sur la protection des données, qui s’applique à la commune à la place de la nLPD | 4 sur 30, dont 3 en toutes lettres ¹ |
| nLPD | citée par les invites comme repère ; elle ne régit pas les organes communaux, le droit cantonal le fait | 27 sur 30 |
| LTrans | le principe de transparence au niveau fédéral, dont les cantons ont leurs équivalents | 1 sur 30 |
| PA | la procédure administrative fédérale, dont la motivation et les voies de droit sont le modèle | 1 sur 30, en toutes lettres ¹ |
| AIMP | les marchés publics cantonaux et communaux | 1 sur 30 |
| LMP | les marchés publics fédéraux, par renvoi | 1 sur 30, en toutes lettres ¹ |
| CO | le personnel communal engagé sous droit privé et les conventions | 2 sur 30 |
| CC | les associations locales partenaires et la naturalisation par renvoi | 1 sur 30 |
| LAVS | les cotisations du personnel communal | 1 sur 30, en toutes lettres ¹ |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Dans quel canton se trouve la commune ?** · Protection des données, transparence, procédure et marchés publics sont cantonaux ; une règle vaudoise ne vaut pas à Neuchâtel.
2. **Le texte est-il une décision, un préavis, une information ou une réponse ?** · Une décision exige motivation et voies de droit ; une information n’en a pas besoin.
3. **Qui décide · l’exécutif en collège, un service, l’organe délibérant ?** · L’auteur et le ton du texte en dépendent, ainsi que la mention des compétences.
4. **Des données de citoyens figurent-elles · nom, adresse, situation, dossier ?** · Elles tombent sous la loi cantonale et déclenchent l’anonymisation.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Citer la nLPD fédérale pour un traitement communal.
- Omettre les voies de droit ou inventer un délai de recours.
- Généraliser une règle cantonale (délais LInfo vaudois, émoluments) à toute la Suisse.
- Exiger une justification pour une demande d’accès à un document officiel.
- Transposer le Code général des collectivités territoriales français ou la CADA.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Noms, adresses et dossiers des habitants
- Dossiers de naturalisation (origine, situation, audition)
- Données du personnel communal et images de vidéosurveillance
- Oppositions nominatives et conflits de voisinage
- Délibérations à huis clos avant publication
