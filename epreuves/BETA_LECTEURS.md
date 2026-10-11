# Cinq bêta-lecteurs romands · grille de retour et message d’invitation

Plan du 11.10.2026, point 56. Avant de parler du skill en public, cinq personnes qui font le métier l’essaient **sur leurs propres demandes**, pendant deux semaines, et rendent un retour structuré. Ce fichier prépare la grille et le message. **Le choix des cinq personnes appartient à Victor Semblanet** · aucun nom ici, des fonctions.

## 1 · Les cinq profils

| N° | Profil | Ce qu’on attend de lui en particulier |
|---|---|---|
| 1 | une fiduciaire | les chiffres que le skill refuse de produire, le périmètre de responsabilité, la TVA |
| 2 | une fonction RH | la question nLPD, les livrables sensibles, la neutralité de genre, les CCT non inventées |
| 3 | un conducteur de travaux | les documents de chantier, la SIA 118 nommée sans être présumée, les réclamations chiffrées |
| 4 | un indépendant | la fluidité · quatre questions sont-elles encore trop pour une relance de 2 350 CHF ? |
| 5 | une entreprise de 20 personnes (direction) | les notes internes, les annonces, le ton, le temps réellement gagné |

Chaque personne travaille sur l’IA qu’elle utilise déjà ; le dépôt dit comment y installer la Méthode (`portabilite/INSTALLATION.md`, `adaptations/README.md`).

## 2 · Ce qu’on leur demande

- Utiliser le skill **sur au moins cinq demandes réelles** de leur travail, pendant **deux semaines**.
- Remplir **une ligne de la grille par demande** (section 3), le jour même.
- Remplir **la fiche de fin** (section 4) une fois, à la fin.
- **Anonymiser** ce qu’ils nous transmettent (« Client X », « Montant A ») · le skill le propose, et l’outil d’anonymisation gratuit de palambur.ch est là pour un texte déjà écrit. On ne veut aucune donnée réelle de leurs clients ou collaborateurs.

## 3 · La grille, une ligne par demande

| Colonne | Ce qu’on note |
|---|---|
| Date | jj.mm.aaaa |
| Livrable | ce que vous vouliez obtenir (offre, relance, note, devis…) |
| IA utilisée | Claude, ChatGPT, Gemini, Mistral, Infomaniak, autre |
| Questions posées | nombre, et le compteur annoncé (« Question 1 sur 4 ») |
| Questions utiles | combien changeaient vraiment le résultat (sur le nombre posé) |
| Question d’anonymisation | posée en premier, oui ou non · s’il y avait des noms |
| Envoyé tel quel | oui · après retouche légère · réécrit · abandonné |
| Quelque chose d’inventé | un chiffre, une loi, un délai, un fait que vous n’aviez pas donné · lequel |
| Marqueurs restants | combien de `[À COMPLÉTER]` et `[À VÉRIFIER]` dans le texte final, et s’ils tombaient juste |
| Temps | votre estimation, en minutes, avec le skill · et combien vous auriez mis sans |
| Remarque | une phrase |

Un tableur à onze colonnes suffit · le modèle vide est à fabriquer au moment de l’envoi, depuis cette table.

## 4 · La fiche de fin

Huit questions, réponses courtes ·

1. En une phrase, à quoi sert la Méthode Palambur d’après vous ?
2. Quelle demande a le mieux marché, et pourquoi ?
3. Quelle demande a le moins bien marché, et pourquoi ?
4. Les questions · trop, pas assez, ou juste ? Laquelle vous a agacé ?
5. Avez-vous surpris le skill à inventer quelque chose ? Quoi ?
6. La protection des données · rassurante, pesante, ou invisible ?
7. Le Gabarit rempli (la première partie de la réponse) · l’avez-vous réutilisé, ignoré, ou copié ailleurs ?
8. Le recommanderiez-vous à un collègue ? À qui, pour quoi ?

Puis une case · « J’accepte qu’une phrase de ce retour soit citée, avec ma fonction et sans mon nom » · oui ou non. Sans oui écrit, rien n’est cité (`diffusion/produit/TEMOIGNAGES_autorisation.md` fait foi pour la forme).

## 5 · Le message d’invitation

À envoyer par Victor Semblanet, depuis son adresse, après avoir choisi les cinq personnes. Le texte est prêt ; les crochets sont à remplir au moment de l’envoi.

> Objet · Deux semaines pour éprouver la Méthode Palambur
>
> Bonjour [prénom],
>
> J’ai mis en libre accès un outil qui change la façon de demander un document à une IA : au lieu de produire tout de suite, il pose au plus quatre questions, protège les noms et les montants par défaut, et marque ce qu’il ne sait pas plutôt que de l’inventer. Il s’appelle la Méthode Palambur, il est gratuit et le restera.
>
> Avant d’en parler plus largement, j’aimerais que cinq personnes qui font vraiment le métier l’essaient. Vous êtes [fonction], c’est exactement le regard qu’il me manque.
>
> Ce que je vous propose · l’installer sur l’IA que vous utilisez déjà (cinq minutes, je vous envoie la marche à suivre), l’utiliser sur cinq demandes réelles pendant deux semaines, et noter une ligne par demande dans une petite grille que je vous joins. À la fin, huit questions courtes. Vos textes restent chez vous · je ne veux que la grille, anonymisée.
>
> En retour · mon temps pour vous aider à l’installer et à l’ajuster à votre métier, et la version suivante portera ce que vous aurez relevé.
>
> Si cela vous tente, répondez-moi d’un mot et je vous envoie le nécessaire d’ici [date].
>
> Avec mes salutations les meilleures,
> Victor Semblanet · Palambur · palambur.ch

## 6 · Ce qu’on fait des retours

- Les grilles sont rassemblées dans `epreuves/resultats/BETA_AAAA-MM-JJ.md` (dossier créé le jour venu) · par profil, sans nom.
- Chaque « quelque chose d’inventé » devient **un cas** dans `cas.json` (famille `piege` si c’est une invention, `metier` sinon), pour que le défaut ne revienne pas sans qu’un instrument le dise.
- Les temps estimés ne se publient pas · ils orientent la mesure du temps gagné (`diffusion/produit/MESURE_TEMPS_GAGNE_protocole.md`), qui seule chronomètre.

## Pour Victor

- `[À DÉCIDER]` · les cinq personnes, une par profil.
- `[À DÉCIDER]` · la date d’envoi du message et la date limite de réponse.
- `[À COMPLÉTER]` · le tableur vide de la grille (section 3), fabriqué le jour de l’envoi.
