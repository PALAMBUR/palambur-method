# Expérience · la Méthode tient-elle sur Apertus ?

Session Skills et Prompt Ingénierie · 11.10.2026 · budget autorisé par le fondateur : **5 CHF**, modèle Apertus (Infomaniak AI Services). Point 52 du plan en 100 points.

## Question

Le prompt d’adaptation (ce qu’on colle dans Euria, un GPT ou un Projet) suffit-il pour qu’un modèle qui n’est pas Claude applique la Méthode : question d’anonymisation d’abord, une question à la fois avec compteur et lettres, quatre questions au plus, deux blocs de sortie, marqueurs au lieu d’inventions ?

## Plan

Trois bras, même grille (`grille.md`), même instrument (`mesurer.py`), même utilisateur simulé pressé (`jouer_apertus.py`).

| Bras | Prompt système | Ce qu’il mesure |
|---|---|---|
| `sans` | aucun | le témoin · ce que fait le modèle seul |
| `complet` | `adaptations/methode-palambur-prompt.md` | la promesse du dépôt |
| `court` | `adaptations/methode-palambur-prompt-court.md` | ce qu’on perd avec la version courte |

Trois phases, chacune soumise au plafond du compteur (`--plafond`, CHF 4.00 au tarif relevé le 23.08.2026, pour rester sous 5.00 même si le tarif a monté d’un quart) :

1. **Les dix cas du protocole** (`PROTOCOLE_TROIS_MODELES.md` § 2) sur les trois bras. Vérifie que l’instrument tourne et donne la première lecture témoin / complet / court.
2. **Tous les livrables et tous les pièges** (25 + 20) sur le bras `complet` seul.
3. **Les cas métier** (104) sur le bras `complet`, tant que le plafond le permet ; ce qui n’est pas joué est dit.

Une seule passe par cas et par bras (température 0,2) : on regarde si la méthode passe, pas sa variance. Huit tours de l’assistant au plus, sinon INCOMPLET.

## Ce qu’on lit

Par bras, la sortie de `mesurer.py --reponses epreuves/reponses/apertus-<bras>` : cas verts, gardes qui rougissent et leur raison. La comparaison `sans` / `complet` dit ce que le prompt apporte ; `complet` / `court` ce que la version courte coûte. La dépense exacte est dans `reponses/DEPENSE.csv`, le contexte dans chaque `RELEVE.md`.

## Limites dites d’avance

- Un utilisateur simulé répond toujours la lettre du défaut : il ne teste pas la qualité des questions, seulement la discipline du modèle.
- Apertus n’est pas Claude : un rouge ici ne condamne pas le skill natif, il dit ce que vaut le prompt collé sur ce modèle.
- Le tarif n’est pas publié par l’API ; il vient d’un relevé daté. La dépense réelle se lit dans le manager Infomaniak.

## Résultats

Joués du 11.10.2026 23 h 21 au 12.10.2026 1 h 37, dépense **2.8991 CHF** sur les 4.00 du plafond (`reponses/DEPENSE.csv`). Les trois phases ont été jouées en entier, aucun cas laissé de côté.

| Bras | Cas notés | Verts | Rouges |
|---|---|---|---|
| `sans` | 10 | 0 | 10 |
| `court` | 10 | 0 | 10 |
| `complet` | 149 | 1 | 148 |

Le détail (gardes par famille, transcriptions lues, ce que l’expérience a réparé dans le dépôt, versions de l’instrument, suite proposée) est dans **`RESULTATS_APERTUS_2026-10-11.md`**. En une phrase · le prompt collé fait poser la question nLPD et rendre le Gabarit, il ne fait ni clarifier avant de produire, ni poser les marqueurs à la place des inventions.

**Deuxième passe (12.10, 1 h 48)** · prompt complet réécrit avec quatre règles tirées de la première passe, dix cas rejoués (bras `complet-v2`, 0.0780 CHF) · **10 rouges sur 10**, aucun gain, une règle de plus a produit un défaut de plus (§ 9 des résultats). Dépense totale de l’expérience · **2.9772 CHF**.
