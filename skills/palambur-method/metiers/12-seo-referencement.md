# SEO & référencement web · fiche métier allégée

**Secteur** · Conseil, chiffres & numérique · code 12 · 30 pistes (état de l’ARBRE au 09.10.2026, `outil_chaptal.html`, `const ARBRE`).

**Intitulé officiel (CH-ISCO-19)** · 2166 Concepteurs graphiques, multimédia · graphistes ; 2431 Spécialistes du marketing et de la publicité ; 2434 Spécialistes techniques des ventes, technologies de l’information et de la communication · libellés lus dans `0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.

Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).

## 1 · Le métier en deux lignes

Le référenceur fait trouver un site et le garde trouvable. Il produit des audits techniques, des plans de mots-clés, des contenus de page, des plans de redirection, des rapports mensuels et des demandes d’accès, pour des clients, des directions et des équipes techniques.

## 2 · Les tâches types

Les 30 pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.

### Audit technique · 6

- Audit technique du site
- Exploration et indexation
- Vitesse et Core Web Vitals
- Compatibilité mobile
- URL et permaliens
- Optimisation des images

### Structure et balises · 5

- Architecture et maillage interne
- Balises title et description
- Structure des titres Hn
- Données structurées Schema.org
- Finition SEO d’une page

### Mots-clés et sémantique · 4

- Recherche de mots-clés
- Intention et pages cibles
- Cocon sémantique
- Analyse des concurrents

### Contenu · 5

- Audit de contenu
- Rédaction des pages
- Avis clients et réputation
- Règle IA · contenu publié
- Page produit · prix et mentions

### Autorité et local · 4

- Profil de liens entrants
- Référencement local
- Domain Authority
- Page Authority

### Mesure et incidents · 6

- Indicateurs et suivi
- Traceurs et consentement
- Refonte · plan de redirections
- Chute de trafic ou de positions
- Rapport mensuel
- Demande d’accès aux outils

## 3 · Vocabulaire du métier

Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le livrable à la place des équivalents français de France ou anglophones.

exploration · indexation · balise title · méta description · Hn · données structurées · maillage interne · cocon sémantique · intention de recherche · mot-clé · page cible · Core Web Vitals · redirection 301 · migration · backlink · netlinking · Domain Authority · Page Authority · référencement local · fiche Google Business · NAP · traceurs · consentement · bandeau de cookies · rapport mensuel · chute de positions

## 4 · Cadre légal et normatif cité par le corpus pour ce métier

Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du 10.08.2026, `reference_regle_articles_loi.md`). État du corpus au 09.10.2026, `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-12-*` (30 invites), comptées sur leur texte intégral.

| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |
|---|---|---|
| nLPD | les traceurs, le consentement et les données collectées par le site | 6 sur 30 |
| RGPD | les visiteurs établis dans l’Union européenne | 1 sur 30 |
| LCD | les faux avis, le dénigrement et les prix affichés | 6 sur 30 |
| LDA | les contenus et images repris ou générés | 3 sur 30 |
| CO | le mandat du référenceur et sa responsabilité | 4 sur 30 |
| LTVA | les prix affichés sur les pages de service et produit | 2 sur 30, en toutes lettres ¹ |

¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », « convention collective ») · le sigle de la loi est posé par la fiche.

## 5 · Questions que le skill pose en priorité pour ce métier

Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données nominatives) passe toujours avant.

1. **Quel est l’objectif de la page ou du site · vendre, informer, être trouvé localement ?** · L’intention de recherche commande le contenu, pas l’inverse.
2. **Quel accès avez-vous aux données · Search Console, analytics, CMS ?** · Sans données réelles, un audit est une liste d’hypothèses ; le modèle doit le dire.
3. **Le site vise-t-il la Suisse seule ou aussi l’Union européenne ?** · Cela change le socle légal des traceurs et des mentions.
4. **Qui lit le rapport · direction, client, développeur ?** · Un rapport à la direction se chiffre et se résume ; un rapport au développeur se détaille.

## 6 · Pièges

Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au lieu de trancher.

- Inventer des volumes de recherche, des positions ou des scores d’autorité.
- Présenter Domain Authority et Page Authority comme des mesures de Google.
- Présenter un bandeau informatif comme un consentement valable.
- Promettre une position ou un délai de résultat.
- Fabriquer ou suggérer de faux avis clients.

## 7 · Données sensibles typiques du métier

Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).

- Accès et identifiants aux outils et comptes
- Données d’audience et de conversion du client
- Mots-clés stratégiques et plan de contenu du client
- Données personnelles collectées par les formulaires du site
- Prix et marges mentionnés sur les pages produit avant publication
