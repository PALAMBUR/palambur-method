# Protection des données · playbook Palambur

À lire dès qu'une demande **contient ou joint des données** (noms de clients, personnes, montants, contrats, dossiers). Objectif : que l'utilisateur puisse envoyer le livrable **en confiance**, sans exposer son entreprise.

## Règle par défaut : anonymiser

> « Anonymiser systématiquement : "client X" au lieu du nom réel, "montant A" au lieu du chiffre exact. »

- **Comportement par défaut** : anonymiser + insérer une mention (voir plus bas).
- **Poser une seule question binaire** avant de produire, uniquement s'il y a des données : conserver les vrais noms, ou anonymiser (recommandé). La décision s'applique **partout**, prompt réutilisable ET livrable final :
  - **accepte / conserve** → vrais noms partout ;
  - **refuse ou silence** (défaut) → anonymisation partout + mention nLPD.
- Jamais d'hybride : on ne mélange pas vrais noms et pseudonymes dans un même rendu.
- Ne jamais recopier une donnée nominative inutile au livrable (minimisation nLPD).
- Ne jamais coller contrats, fiches de paie, données financières ou secrets industriels dans une IA publique.

**Convention d'anonymisation** : `Client X`, `Client Y` · `Collaborateur·trice A` · `Montant A`, `Montant B` · `Fournisseur 1`. Garder une correspondance cohérente dans tout le document.

## Marqueurs d'information manquante (ne jamais inventer)

Quand une donnée manque, l'écrire visiblement plutôt que la combler :

- `[À COMPLÉTER]` · champ que l'utilisateur doit remplir
- `[INFO MANQUANTE]` · donnée absente des éléments fournis
- `[À VÉRIFIER]` · affirmation (article de loi, CCT, chiffre) à confirmer
- `[SOURCE NON IDENTIFIÉE]` · origine d'une donnée incertaine

## Mentions-types à insérer

- **Document externe (nLPD)** : « Vos données sont traitées en Suisse, conformément à la nLPD. »
- **Livrable juridiquement sensible (clause de non-responsabilité, verbatim)** :
  > « Ce document constitue un guide de gestion des risques structurels et ne remplace pas un avis juridique formel. Toute mise en production doit être précédée d'une revue par un conseil habilité (avocat·e nLPD/EU AI Act, auditeur sécurité indépendant). »
- **Rappel de validation humaine** : sur tout livrable sensible, préciser que la relecture par une personne responsable reste obligatoire. Pas de promesse magique.

## Outils souverains recommandés (Suisse)

- Hébergement : **Infomaniak** (Genève/Zurich), **Exoscale** (Genève/Lugano)
- Sauvegarde : **Swiss Backup**
- Signature qualifiée : **SwissSign** (PAdES)
- Modèle IA souverain cité pour les entreprises : **Mistral**
- Règle absolue : **aucun sous-traitant hors CH** pour les données sensibles.

## Shadow AI (à expliquer si le livrable touche la gouvernance IA)

**Définition** : usage par les collaborateurs d'IA génératives publiques (ChatGPT, Claude, Gemini, Copilot…) **sans approbation ni politique IT**. Repère cité : « plus de 70 % des collaborateurs utilisent des IA publiques sans approbation IT ».

Enjeux réglementaires à rappeler (marquer `[À VÉRIFIER]` si on cite une base légale précise) :
- Registre nLPD (Art. 12) obligatoire
- Sanction PFPDT jusqu'à **CHF 250'000**, visant **le dirigeant**
- EU AI Act : usages RH/crédit classés haut-risque dès **août 2026**

## Réglage conseillé

Pour un livrable où l'exactitude prime (contrat, analyse juridique/financière), viser une **température basse (0.2 à 0.4)** ; défaut 0.7 pour de la rédaction courante.
