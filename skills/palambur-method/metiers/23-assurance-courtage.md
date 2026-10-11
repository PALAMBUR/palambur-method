# Assurance & courtage · fiche métier allégée

**Secteur** · Conseil, chiffres & numérique · code 23 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 3321 Agents d’assurances · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

L’intermédiaire d’assurance analyse le besoin, couvre et accompagne l’indemnisation. Il produit des questionnaires de découverte, des analyses de besoins, des recommandations écrites, des comparatifs, des déclarations de sinistre et des mandats de courtage, pour des particuliers, des entreprises et des compagnies.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Découverte et conseil · 6

- Questionnaire de découverte
- Analyse des besoins
- Devoir de conseil
- Recommandation écrite
- Revue annuelle
- Note de synthèse du dossier

### Comparaison et souscription · 6

- Comparatif de couvertures
- Réticence avant la proposition
- Dossier de souscription
- Changement de compagnie
- Somme assurée et sous-assurance
- Valeur à neuf, vénale, vétusté

### Branches et couvertures · 5

- Tour des risques d’une entreprise
- Perte de gain maladie
- Certificat de prévoyance
- Maladie · base et complémentaires
- Protection juridique

### Sinistre · 4

- Déclaration de sinistre
- Expertise après sinistre
- Refus de prestation
- Recours contre un tiers

### Portefeuille et agence · 5

- Mandat de courtage
- Reprise d’un portefeuille
- Personnes clés de l’entreprise
- Prime impayée
- Registre et formation continue

### Déontologie et données · 4

- Transparence sur la rémunération
- Données des assurés
- Démarchage et prospection
- Refuser d’antidater

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

intermédiaire lié · intermédiaire non lié · registre FINMA · devoir d’information · devoir de conseil · analyse des besoins · recommandation écrite · proposition d’assurance · réticence · somme assurée · sous-assurance · règle proportionnelle · valeur à neuf · valeur vénale · vétusté · franchise · perte de gain maladie · certificat de prévoyance · assurance de base · complémentaire · déclaration de sinistre · expertise · refus de prestation · recours contre un tiers · mandat de courtage · rémunération · courtage · prime impayée

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-23-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| LSA | l’inscription, le devoir d’information, les conflits d’intérêts et la transparence sur la rémunération | 6 sur 30 |
| LCA | le contrat d’assurance, la réticence, la sous-assurance et le sinistre | 4 sur 30 |
| LAMal | l’assurance de base et son obligation d’admission | 3 sur 30 |
| nLPD | les données des assurés, en particulier de santé | 29 sur 30 |
| CO | le mandat de courtage et sa révocation | 4 sur 30 |
| LPP | le certificat de prévoyance et la lecture du 2e pilier | 2 sur 30 |
| LAA | l’assurance-accidents des entreprises clientes | 2 sur 30 |
| LCD | le démarchage, la prospection et la comparaison | 2 sur 30 |
| LAVS | le 1er pilier dans la vue d’ensemble de la prévoyance | 1 sur 30, en toutes lettres ¹ |
| CCT | les couvertures imposées par une convention de branche au client employeur | 1 sur 30, en toutes lettres ¹ |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Particulier ou entreprise, et quelles branches sont concernées ?** · Perte de gain, prévoyance, choses et responsabilité n’obéissent pas aux mêmes textes.
2. **Le client a-t-il répondu au questionnaire de santé ou de risque lui-même ?** · La réticence se juge sur ses réponses ; un formulaire prérempli engage le client.
3. **Sommes assurées et valeurs faites-vous entrer, et d’où viennent-elles ?** · Le modèle ne doit jamais fixer une somme assurée ; la sous-assurance se découvre au sinistre.
4. **Le texte parle-t-il de rémunération ou de comparaison entre compagnies ?** · La transparence sur la rémunération et la loyauté de la comparaison sont des obligations écrites.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Chiffrer une prime, une franchise ou une indemnité sans tarif réel.
- Présenter la réticence comme exigeant une intention de tromper.
- Annoncer un changement de caisse comme un simple transfert, complémentaires comprises.
- Omettre la clause de transparence sur la rémunération.
- Transposer le Code des assurances français, l’ORIAS et la loi Hamon.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Données de santé des assurés et questionnaires médicaux
- Situation financière, patrimoine et prévoyance du client
- Historique de sinistres
- Rémunérations et commissions perçues
- Dossiers de refus de prestation et de contestation
