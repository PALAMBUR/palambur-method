# Protection des données · playbook Palambur

À lire dès qu’une demande **contient ou joint des données** (noms de clients, personnes, montants, contrats, dossiers). Objectif : que l’utilisateur puisse envoyer le livrable **en confiance**, sans exposer son entreprise.

## Règle par défaut : anonymiser

> « Anonymiser systématiquement : "client X" au lieu du nom réel, "montant A" au lieu du chiffre exact. »

- **Comportement par défaut** : anonymiser + insérer une mention (voir plus bas).
- **Poser une seule question binaire** avant de produire, uniquement s’il y a des données : conserver les vrais noms, ou anonymiser (recommandé). La décision s’applique **partout**, prompt réutilisable ET livrable final :
  - **accepte / conserve** → vrais noms partout ;
  - **répond autre chose qu’une demande de conserver** (défaut) → anonymisation partout + mention nLPD.
- Jamais d’hybride : on ne mélange pas vrais noms et pseudonymes dans un même rendu.
- Ne jamais recopier une donnée nominative inutile au livrable (minimisation nLPD).
- Ne jamais coller contrats, fiches de paie, données financières ou secrets industriels dans une IA publique.

**Convention d’anonymisation** : `Client X`, `Client Y` · `Collaborateur·trice A` · `Montant A`, `Montant B` · `Fournisseur 1`. Garder une correspondance cohérente dans tout le document.

## Marqueurs d’information manquante (ne jamais inventer)

Quand une donnée manque, l’écrire visiblement plutôt que la combler :

- `[À COMPLÉTER]` · champ que l’utilisateur doit remplir
- `[INFO MANQUANTE]` · donnée absente des éléments fournis
- `[À VÉRIFIER]` · affirmation (article de loi, CCT, chiffre) à confirmer
- `[SOURCE NON IDENTIFIÉE]` · origine d’une donnée incertaine

## Mentions-types à insérer

- **Document externe (nLPD)** : « Vos données sont traitées en Suisse, conformément à la nLPD. »
- **Livrable juridiquement sensible (clause de non-responsabilité, verbatim)** :
  > « Ce document constitue un guide de gestion des risques structurels et ne remplace pas un avis juridique formel. Toute mise en production doit être précédée d’une revue par un conseil habilité (avocat·e nLPD/EU AI Act, auditeur sécurité indépendant). »
- **Rappel de validation humaine** : sur tout livrable sensible, préciser que la relecture par une personne responsable reste obligatoire. Pas de promesse magique.

## Outils souverains recommandés (Suisse)

- Hébergement : **Infomaniak** (Genève/Zurich), **Exoscale** (Genève/Lugano)
- Sauvegarde : **Swiss Backup**
- Signature qualifiée : **SwissSign** (PAdES)
- Modèle IA : européen (**Mistral**) ou suisse (**Apertus**, servi par Infomaniak)
- Règle absolue : **aucun sous-traitant hors CH** pour les données sensibles.

## Shadow AI (à expliquer si le livrable touche la gouvernance IA)

**Définition** : usage par les collaborateurs d’IA génératives publiques (ChatGPT, Claude, Gemini, Copilot…) **sans approbation ni politique IT**. Repère souvent cité : « plus de 70 % des collaborateurs utilisent des IA publiques sans approbation IT » `[À VÉRIFIER : source et date]` ; dans un livrable, ce chiffre ne s’écrit qu’avec sa source et son année, sinon on écrit « une part importante des collaborateurs ».

Enjeux réglementaires à rappeler, **toujours** avec le marqueur tant qu’une personne habilitée n’a pas vérifié (voir `references-juridiques.md`) :
- Registre des activités de traitement (nLPD) `[À VÉRIFIER : article et conditions d’obligation]`
- Sanction pénale prévue par la nLPD, jusqu’à **CHF 250'000** `[À VÉRIFIER : montant et personne visée]`, qui vise la personne physique responsable, pas l’entreprise
- Règlement européen sur l’IA : usages RH classés à haut risque, applicable aux entreprises suisses seulement si elles opèrent sur le marché de l’UE `[À VÉRIFIER : date d’application]`

## Réglage conseillé

Pour un livrable où l’exactitude prime (contrat, analyse juridique/financière), viser une **température basse (0.2 à 0.4)** ; défaut 0.7 pour de la rédaction courante.
