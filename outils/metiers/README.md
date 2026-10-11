# Générateurs des 26 fiches métiers

**Quoi** · ces scripts fabriquent `skills/palambur-method/metiers/<NN>-<slug>.md`, les 26 fiches allégées que le skill charge à l’Étape 1. La section 2 de chaque fiche est lue dans l’ARBRE Chaptal, la section 4 n’accepte qu’une loi attestée dans les invites du métier ; le reste (deux lignes, vocabulaire, questions, pièges, données sensibles) est rédigé dans `contenu_a.py` et `contenu_b.py`.

**Pourquoi des générateurs** · une fiche recopiée à la main vieillit en silence quand l’ARBRE bouge. Un générateur qu’on peut relancer dit l’écart, et refuse d’écrire une loi que le corpus ne cite pas (CLAUDE.md § 2 et § 4).

## Dans quel ordre

1. `extraire_arbre.mjs` · lit `const ARBRE` dans `outil_chaptal.html` et l’écrit dans `_cache/arbre.json`. **Lancé tout seul par `generer.py`** quand le cache manque ou est plus vieux que la page.
2. `generer.py` · écrit les 26 fiches. `--sortie DOSSIER` pour écrire ailleurs et comparer sans toucher aux fiches du dépôt.
3. `verifier.py` · structure en 7 sections, comptes ARBRE contre fiche, lois attestées, mot interdit, `art. N`, typographie. Code de retour 1 au premier écart.

`lois_census.py` porte la table des motifs (`PAT`) et, lancé seul, imprime le recensement par métier. `chemins.py` résout tous les chemins depuis `__file__`.

## Sources lues dans l’atelier

Les sources ne sont **pas dans ce dépôt** · elles sont atteintes en remontant de deux dossiers depuis la racine du dépôt (`../../1300_PRODUITS_IA/…`, `../../0600_RESSOURCES/…`, `../../0500_AGENTS_IA/0501_Prompts_Metiers/audit_typo.py`). Hors de l’atelier Palambur, chaque script sort avec le **code 2** et la phrase « source Palambur absente, fiches non regénérables ici », sans planter.

La règle typographique n’est jamais recopiée · `verifier.py` **importe** `audit_typo.py`.

`_cache/` est ignoré par git (`.gitignore` de ce dossier) · il contient les brouillons que les scripts créent et consomment.
