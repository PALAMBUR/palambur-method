# Chaptal vers la Méthode · spécification du bouton « Ouvrir dans la Méthode » (point 78)

**Spécification remise à la session Chaptal · 11.10.2026 · session Skills et Prompt Ingénierie.** Ce document décrit un geste à construire **dans Chaptal**, pas dans ce dépôt : aucun code du skill ne change, aucun code n’est posé ici. La session Chaptal construit, éprouve et pose ; cette note dit quoi, pourquoi, et ce qu’elle ne doit pas faire.

## En une phrase

**Sur une fiche Chaptal lisible, un bouton met dans le presse-papier le Gabarit de la fiche précédé du mot qui déclenche la Méthode**, pour que la personne le colle dans l’IA où le skill est installé et que celle-ci pose les questions des cases vides au lieu de les deviner.

## Pourquoi un presse-papier et pas un lien

- **La politique de contenu de Chaptal interdit tout appel réseau** (empreinte posée par `poses/poser_csp.mjs`, lot C12 du 22.08.2026). Le bouton n’appelle donc rien : il écrit un texte dans le presse-papier, comme le bouton « copier » existant (fonction `presse(txt)` de `outil_chaptal.html`).
- **Le skill vit dans l’IA de la personne**, pas chez Palambur : Claude Code, Codex, Cursor, Gemini CLI, Copilot, Vibe (voir `portabilite/INSTALLATION.md`). Il n’existe pas d’adresse unique qui ouvre « la Méthode ».
- **Les liens profonds qui ouvrent une IA avec un prompt pré-rempli** (une adresse `?q=` chez tel ou tel éditeur) ne sont documentés officiellement par aucun des hôtes relevés le 11.10.2026 dans `portabilite/INSTALLATION.md` : **non confirmé**, donc pas de lien de ce type dans la première version. À réexaminer à la veille du 11.11.2026 (`portabilite/VEILLE_PLATEFORMES.md`).

## Ce qui est pré-rempli

Le texte copié a **trois parties**, dans cet ordre, séparées par une ligne vide.

1. **L’amorce**, une phrase fixe par langue de page, qui porte le mot déclencheur (porte 1 du skill, `SKILL.md` § Déclenchement). En français : « Méthode Palambur : applique le Gabarit ci-dessous. Pour chaque case marquée [À COMPLÉTER], pose-moi la question avant de rédiger, une à la fois. » En anglais : « Palambur method: apply the template below. For every field marked [À COMPLÉTER], ask me before writing, one question at a time. » Les versions DE, IT, ES suivent la même phrase ; **le marqueur `[À COMPLÉTER]` ne se traduit pas**, c’est lui que la fiche porte et que le skill reconnaît.
2. **Le Gabarit de la fiche**, exactement le texte que le bouton « copier » met déjà dans le presse-papier : la section `PROMPT PRÊT À COPIER-COLLER` (`pret` dans `outil_chaptal.html`), blocs INSTRUCTION · RÔLE · DONNÉES · CONTRAINTES · FORMAT et blocs d’extension s’il y en a, **sans le pied** (ROI, souveraineté, garde-fou).
3. **Le repère de la fiche**, une ligne : `Fiche Chaptal <ref> · <titre court> · palambur.ch`, avec la `ref` du corpus (forme `PAL-01-DS-01`) et le `nomCourt` de la feuille dans la langue de la page. Cette ligne permet à la personne de retrouver la fiche ; elle n’est pas une publicité dans le livrable, puisqu’elle précède la rédaction et que le skill ne la recopie pas (règle « aucune mention Palambur dans les livrables », `README.md` § Engagements).

**Ce qui n’est pas pré-rempli** : rien de ce que la personne n’a pas encore dit. Les cases `[À COMPLÉTER]` restent vides ; c’est le skill qui les demandera. Si Chaptal porte un jour des cases remplies par la personne dans la page, elles partent dans le bloc DONNÉES telles qu’elle les a saisies, et les cases vides gardent le marqueur (même règle que `message_utilisateur` de Jacquard : **le marqueur part, il ne se tait pas**).

## Où le bouton apparaît, et où il n’apparaît pas

| État de la fiche | Bouton | Pourquoi |
|---|---|---|
| Fiche **libre** (une des 24 gratuites) | oui | le texte est public |
| Fiche **débloquée** par la personne | oui | elle a payé le texte, elle l’emporte où elle veut |
| Fiche **verrouillée** (cas d’usage visible, texte caché) | **non** | le Gabarit n’est pas lisible ; le bouton mentirait. La fiche garde son chemin d’achat actuel |
| Catalogue, recherche, lignes mobiles | non | le bouton vit dans le lecteur de fiche seulement, à côté de « copier » |

Le bouton se place **sur le rail des actions au pied du lecteur**, à droite de « copier » (rail posé par `poses/poser_lecteur_respire.py`, 31.08.2026). Libellé : « Ouvrir dans la Méthode » (FR), « Open in the Method » (EN), et les trois autres langues au même rang. Après le clic, le même retour visuel que « copier » (« Copié » pendant deux secondes), puis une ligne d’aide : « Collez ce texte dans l’IA où la Méthode Palambur est installée. Pas encore installée ? » avec le lien vers `https://github.com/PALAMBUR/palambur-method`. **Ce lien est le seul du bouton**, il s’ouvre dans un nouvel onglet et ne porte aucun paramètre.

## Ce que la session Chaptal doit vérifier

1. **Le banc des repères** (`bancs/banc_reperes.mjs`) : le ROI, la souveraineté et le garde-fou **ne partent pas** dans le presse-papier. Le nouveau bouton doit passer ce banc tel quel, puisqu’il copie `pret` et pas le pied.
2. **La politique de contenu** : toute modification du script inline périme l’empreinte ; `poses/poser_csp.mjs --ecrire` entre dans la pose, maillon « sceller » de `00_CHAINE.py`.
3. **Les huit marchés** : libellé et amorce dans chaque langue de page (règle « uniformité de l’interface selon la langue », 03.10.2026) ; `[À COMPLÉTER]` reste en français partout.
4. **Un témoin fabriqué** par état de fiche (libre, débloquée, verrouillée) qui prouve que le bouton est là, ou absent, pour la bonne raison.
5. **Le téléphone** : le rail des actions tient déjà sur un iPhone SE avec trois actions ; un quatrième bouton se mesure avant de se poser (`poser_lecteur_respire.py`, fenêtre de lecture 343 px au 31.08.2026).

## Ce que cette spécification ne décide pas

- **Le nom du bouton** dans les cinq langues est une proposition ; la session Chaptal l’aligne sur `textes.js` et la session Site sur la page `/methode-palambur/`.
- **Un lien profond** vers une IA donnée : non confirmé, voir ci-dessus.
- **La mesure** du nombre de clics : Chaptal n’envoie rien ; si Victor veut un compteur, il se fait côté site, et c’est une décision à part.

## Trous et décisions

- `[À DÉCIDER]` · libellé définitif du bouton dans les cinq langues (session Chaptal, puis Site pour la page du skill).
- `[À DÉCIDER]` · mesurer les clics ou non (décision Victor, hors de Chaptal).
