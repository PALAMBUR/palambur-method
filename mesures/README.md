# Mesures · le relevé hebdomadaire du dépôt (point 27)

**Sans mesure, « viral » reste un mot.** Ce dossier porte une seule table, `releves.csv`, écrite par `outils/mesure.py`, et c’est elle qui fait foi. Aucun chiffre de ce dossier ne se recopie dans un autre fichier : on le cite **avec sa date**, ou on relance le script.

## Le geste

```bash
python3 outils/mesure.py
```

Une ligne par relevé, **une ligne par jour** : relancé le même jour, le script remplace la ligne du jour (idempotence). Lecture seule sur GitHub (`gh api`, jamais d’écriture). Rythme proposé : **chaque lundi**.

```bash
python3 outils/mesure.py --epreuve
```

Casse chaque garde sur témoin fabriqué (réponse API inventée, CSV temporaire), sans appeler GitHub, et exige de chaque garde sa raison. À jouer avant de faire confiance à un zéro.

## Les colonnes

| Colonne | Source GitHub | Lecture |
|---|---|---|
| `date` | jour du relevé, AAAA-MM-JJ | |
| `etoiles` | `repos/PALAMBUR/palambur-method` · `stargazers_count` | cumul depuis la création · la nôtre en fait partie |
| `forks` | idem · `forks_count` | cumul |
| `vues`, `vues_uniques` | `…/traffic/views` | **fenêtre glissante de 14 jours** · ne se cumule pas d’une semaine à l’autre |
| `clones`, `clones_uniques` | `…/traffic/clones` | **14 jours glissants** · au 11.10.2026, presque entièrement des robots d’annuaires, pas des personnes |

Les vues uniques sont le seul chiffre qui approche des **visiteurs humains**. Les clones ne mesurent pas des installations : une installation par `/plugin install` n’apparaît nulle part dans ces compteurs.

## Ce que GitHub ne mesure pas, et qu’il faudra mesurer autrement

- **Installations attestées** · le skill n’envoie rien à Palambur (promesse de la page site et du README), donc aucun compteur automatique. Une installation « attestée » est une personne qui le dit : un ticket, un message, une réponse à un post, un atelier tenu. Elles se comptent à la main, dans une colonne à ajouter le jour où la première existe, pas avant.
- **GPT ouvert** (point 17) · le nombre de conversations d’un GPT public se lit dans le tableau de bord du constructeur chez OpenAI, pas ici. Même règle : colonne ajoutée quand la donnée existe.

## Objectif proposé

**100 étoiles et 20 installations attestées à 3 mois** (soit au 11.01.2027 si le départ est le 11.10.2026) · **à valider par Victor**. Point de départ relevé le 11.10.2026 : 2 étoiles, dont la nôtre.

Ce n’est pas une prévision, c’est un seuil qui dit si la diffusion (points 21 à 26) a produit quelque chose. S’il n’est pas atteint, on change la diffusion, pas la mesure.

## Ce qu’on ne fait pas

- On ne cumule jamais deux fenêtres de 14 jours.
- On ne corrige jamais une ligne à la main : on relance le script à la bonne date (`--date AAAA-MM-JJ`) et il remplace la ligne.
- On n’écrit rien sur GitHub depuis ce script.
