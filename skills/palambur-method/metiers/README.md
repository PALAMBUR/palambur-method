# Les 26 métiers · fiches allégées pour le skill

Ce dossier branche la Méthode Palambur sur les 26 métiers de l’ARBRE (`outil_chaptal.html`, `const ARBRE`, 6 secteurs, 782 pistes, état au 09.10.2026). Une fiche par métier, même structure en sept sections · version allégée, dont la version complète, avec les invites de chaque piste, est Chaptal sur palambur.ch.

## Règle d’usage

Quand la demande ou le profil de l’utilisateur désigne un métier (« je suis fiduciaire », « pour mon garage », « offre d’emploi de conducteur de travaux »), le skill charge **la fiche de ce métier à l’Étape 1**, avant de choisir son lot de questions. Il en tire :

- les **questions prioritaires** (section 5) pour composer le lot de l’Étape 2, à la place des questions génériques de `methode-palambur.md` ;
- le **vocabulaire** (section 3) pour le Gabarit et le livrable ;
- le **cadre légal** (section 4) pour le bloc RÔLE ET AUDIENCE et le bloc CONTRAINTES, textes nommés seulement, jamais un numéro d’article sans `[À VÉRIFIER]` ;
- les **pièges** (section 6) comme zones de risque et auto-contrôle ;
- les **données sensibles** (section 7) pour déclencher l’Étape 0.

Si aucun métier n’est reconnu, le skill travaille sans fiche. Si deux métiers se croisent (une fiduciaire qui recrute), il charge les deux et prend les questions RH pour le livrable RH.

Les différences par marché (fr-CH, fr-FR, puis les autres) sont dans `MARCHES.md`.

## Structure fixe des 26 fiches

1. Le métier en deux lignes
2. Les tâches types (toutes les pistes du métier, par famille, titres courts de l’ARBRE)
3. Vocabulaire du métier
4. Cadre légal et normatif cité par le corpus pour ce métier
5. Questions que le skill pose en priorité pour ce métier
6. Pièges
7. Données sensibles typiques du métier

Chaque fiche porte en tête son intitulé officiel CH-ISCO-19 (`0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`).

## Index par secteur

Les secteurs et leur ordre sont ceux de l’ARBRE.

### Fonctions transverses · 5 métiers

| Code | Métier | Fiche | Pistes |
|---|---|---|---|
| 01 | Direction & stratégie | `01-direction-strategie.md` | 30 |
| 08 | Chef de projet | `08-chef-de-projet.md` | 30 |
| 05 | Ressources humaines | `05-ressources-humaines.md` | 30 |
| 02 | Commerce & ventes | `02-commerce-ventes.md` | 30 |
| 03 | ADV & service client | `03-adv-service-client.md` | 30 |

### Industrie, atelier & mobilité · 4 métiers

| Code | Métier | Fiche | Pistes |
|---|---|---|---|
| 14 | Industrie & usinage de précision | `14-industrie-usinage.md` | 30 |
| 18 | Horlogerie & sous-traitance | `18-horlogerie-sous-traitance.md` | 30 |
| 22 | Garage & automobile | `22-garage-automobile.md` | 30 |
| 20 | Transport & logistique | `20-transport-logistique.md` | 30 |

### Construction & immobilier · 5 métiers

| Code | Métier | Fiche | Pistes |
|---|---|---|---|
| 21 | Architectes & ingénieurs civils | `21-architectes-ingenieurs.md` | 30 |
| 07 | Conducteur de travaux | `07-conducteur-travaux.md` | 30 |
| 09 | Artisan du bâtiment | `09-artisan-batiment.md` | 30 |
| 06 | Agent immobilier | `06-agent-immobilier.md` | 31 |
| 26 | Maître d’ouvrage | `26-maitre-ouvrage.md` | 30 |

### Conseil, chiffres & numérique · 4 métiers

| Code | Métier | Fiche | Pistes |
|---|---|---|---|
| 16 | Fiduciaires & cabinets comptables | `16-fiduciaires-comptables.md` | 31 |
| 23 | Assurance & courtage | `23-assurance-courtage.md` | 30 |
| 12 | SEO & référencement web | `12-seo-referencement.md` | 30 |
| 13 | OSINT & recherche web | `13-osint-recherche-web.md` | 30 |

### Communication, écrit & campagne · 3 métiers

| Code | Métier | Fiche | Pistes |
|---|---|---|---|
| 04 | Marketing & communication | `04-marketing-communication.md` | 30 |
| 11 | Critique littéraire | `11-critique-litteraire.md` | 30 |
| 17 | Communication de campagne | `17-communication-campagne.md` | 30 |

### Public, santé & accueil · 5 métiers

| Code | Métier | Fiche | Pistes |
|---|---|---|---|
| 15 | Administrations & communes | `15-administrations-communes.md` | 30 |
| 19 | Santé & cabinets | `19-sante-cabinets.md` | 30 |
| 10 | Restaurateur | `10-restaurateur.md` | 30 |
| 24 | Associations & fondations | `24-associations-fondations.md` | 30 |
| 25 | Enseignement scolaire et professionnel | `25-enseignement.md` | 30 |

Total · 26 fiches, 782 pistes.

## Sources des fiches

- Tâches, familles et index · `const ARBRE` de `outil_chaptal.html` (champs `nomCourt`, `nom`, `ref`).
- Cadre légal · uniquement les textes qu’une invite du métier cite, par le sigle ou en toutes lettres, dans `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl` (782 invites, versions 2026-08-31 à 2026-09-14). Une fiche ne cite aucun texte absent de ses invites ; quand l’invite ne dit pas le sigle, la fiche le marque ¹.
- Vocabulaire et pièges · `0600_RESSOURCES/06.12_Referentiels_Officiels/Metiers/<NN>_<Nom>/REFERENCES_<NN>_<Nom>.md`.
- Règle des articles de loi · `reference_regle_articles_loi.md` (arbitrage du 10.08.2026).
- Générateurs · `outils/metiers/` du dépôt (`generer.py`, `verifier.py`).
