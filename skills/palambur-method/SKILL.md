---
name: palambur-method
description: À utiliser dès que l'utilisateur mentionne « palambur », « méthode palambur » ou « palambur method », en particulier pour produire un livrable métier (offre d'emploi, contrat, devis, offre commerciale, relance ADV, note interne, compte-rendu, annonce, rapport, charte, courrier client…), y compris lorsqu'il faut protéger ou anonymiser des données clients. Déclencher même si la demande est courte ou peu détaillée. Ne pas utiliser pour une simple question factuelle sans production de livrable.
---

# Méthode Palambur

## Principe

Une requête métier arrive souvent **sous-spécifiée** : « fais une offre d'emploi pour un peintre à 80 % ». Produire tout de suite obligerait à inventer une dizaine de paramètres, et donnerait un livrable générique.

La Méthode Palambur inverse l'ordre : **on comble le contexte manquant AVANT de produire**. Deux promesses à tenir envers l'utilisateur, et c'est ce qui fait la valeur du skill :

- **Fluide** · peu de questions, mais bien ciblées ; une valeur par défaut prudente quand c'est possible plutôt qu'une question de plus.
- **Sûr** · protection des données par défaut, aucune donnée inventée. L'utilisateur repart avec un livrable qu'il peut envoyer **en confiance**.

**La Méthode Palambur** est l'ensemble ; **le Gabarit Palambur** en est l'outil : les 5 blocs. Le Gabarit (5 blocs + 4 blocs d'extension), les 4 niveaux S/M/L/XL, le ton et l'anti-hallucination sont dans **`methode-palambur.md`**. Les règles de protection des données sont dans **`protection-donnees.md`**. Lis-les au moment utile, pas besoin de tout charger d'avance.

<HARD-GATE>
AVANT D'ÉCRIRE LE MOINDRE MOT DU LIVRABLE, vérifie ces deux points dans l'ordre. Si l'un des deux n'est pas coché, ton PROCHAIN message est une question, pas un livrable, pas un brouillon, pas des « hypothèses signalées » :

1. [ ] La demande contient-elle des données nominatives (nom de client, personne, montant, contrat) ? → Si oui et que tu n'as pas encore posé la question binaire d'anonymisation (Étape 0), pose-la et arrête-toi.
2. [ ] La demande exige-t-elle 3 hypothèses conséquentes ou plus (Étape 1) ? → Si oui et que tu n'as pas encore posé tes questions de clarification, pose ta PREMIÈRE question (Étape 2) et arrête-toi.

Produire un livrable rempli d'hypothèses avec une liste de « points à valider » à la fin N'EST PAS une clarification, c'est l'anti-pattern que cette méthode existe pour éliminer. Les deux cases ci-dessus doivent être cochées avant toute rédaction, pas corrigées après coup.
</HARD-GATE>

## Deux cas une fois déclenché

Le skill s'active parce que le mot « palambur » est présent, **pas** parce que la demande est incomplète. Donc :

- **Il manque des éléments déterminants** → clarifie (Étapes 0→3).
- **Tout est déjà fourni** → ne questionne pas, va directement produire.

## Étape 0 · 🔒 Réflexe protection des données (toujours en premier)

Avant même d'évaluer le reste : dès que la demande **contient ou joint des données** (noms de clients, personnes, montants, contrats, dossiers) :

1. **Pose d'abord UNE question, binaire** : « Je détecte des données nominatives. Par défaut je les **anonymise partout** (« Client X », « Montant A ») et j'ajoute une mention nLPD, souhaitez-vous plutôt les **conserver telles quelles** ? »
2. **Décision binaire, appliquée partout** (prompt réutilisable ET livrable final) :
   - **L'utilisateur accepte** (conserve) → vrais noms **partout**.
   - **L'utilisateur refuse ou ne répond pas** (défaut) → anonymisation **partout** + mention nLPD.
   Pas d'hybride : on ne mélange jamais vrais noms et pseudonymes dans un même rendu.
3. Ne recopie jamais une donnée nominative qui n'est pas utile au livrable.

*Pourquoi* : en Suisse, exposer des données clients engage la responsabilité du **dirigeant** (nLPD, sanctions PFPDT). Anonymiser par défaut, c'est protéger l'utilisateur, pas une formalité. Règles, marqueurs et mentions-types : **`protection-donnees.md`**.

**Cette étape passe avant l'Étape 1** : même si la demande semble par ailleurs complète, la présence de données nominatives déclenche toujours cette question en premier.

## Étape 1 · Évaluer (rubrique en 2 axes)

Juge la demande sur deux axes, sans calcul mécanique :

- **Valeur** · la requête vise-t-elle à *produire un livrable* destiné à être envoyé, publié, signé, archivé ?
- **Spécification** · devrais-tu *inventer/supposer* plusieurs éléments importants (public, périmètre, contraintes légales, ton, données concrètes) ?

**Repère** : si tu dois faire **3 hypothèses conséquentes ou plus**, clarifie. En dessous, produis directement.

**Anti-pattern à éviter** : produire tout de suite un livrable rempli d'hypothèses prudentes, avec une liste de « points à valider » à la fin. Ça ressemble à de la fluidité mais ça viole la méthode : l'utilisateur doit être questionné **avant**, pas corriger **après**.

## Étape 2 · Clarifier (anticiper par lot de quatre, demander une par une)

La règle a **deux étages**. Ne les confonds pas.

**Lis `methode-palambur.md` (et `protection-donnees.md` s'il y a des données) UNE SEULE FOIS**, au tout début de la clarification. Ne relis PAS ces fichiers entre chaque question, c'est ce qui ralentit inutilement.

**En amont, anticipe le lot.** Avant de poser quoi que ce soit, identifie les manques réellement déterminants, ordonne-les du plus structurant au plus accessoire, et écarte tout ce qui peut recevoir un défaut prudent. Tu sais donc dès le départ **combien** de questions tu vas poser, et pourquoi. Vise environ quatre.

**En surface, ne pose qu'UNE question par message**, en annonçant le compteur : « Question 1 sur 4 ». Choix multiples, avec un **défaut prudent signalé** et une échappatoire « autre / je ne sais pas ».

*Pourquoi ces deux étages* : quatre questions dans un même message donnent un bloc long, lent à afficher et coûteux à lire, l'utilisateur décroche avant d'avoir répondu. Mais une question à la fois **sans compteur** donne l'impression d'un interrogatoire sans fin. Anticiper le lot et annoncer le compteur donne les deux : un message léger, et une clarification visiblement finie.

Ensuite :

1. **Le nombre de questions s'adapte au livrable, sans plafond fixe.** Un livrable simple (offre, relance) se cadre en un lot. Un livrable **niveau L / XL** (charte, contrat, plan d'égalité, politique interne) en mérite deux ou trois, chaque lot étant informé des réponses du précédent. Annonce le nouveau compteur à chaque lot.
2. **Question de suivi adaptative** quand une réponse ouvre une vraie branche qui change le livrable (ex. « formation à 40 % », or un apprentissage dual CFC est en principe à 100 %, donc quel cadre exact ?). Elle s'ajoute au compteur, signale-le.
3. **Ne demande QUE ce qui change vraiment le livrable.** Le reste : défaut prudent signalé, ou marqueur `[À COMPLÉTER]` dans le livrable, jamais une question de confort.
4. Reformule brièvement le contexte accumulé entre deux lots, puis produis dès que tu as de quoi faire un livrable solide.

## Étape 3 · Produire (sortie en deux temps)

<HARD-GATE>
N'atteins cette étape qu'après l'Étape 0 (donnée traitée) et l'Étape 2 (questions posées et réponses obtenues, ou demande déjà complète dès le départ). Une fois ici, les deux parties ci-dessous sont TOUJOURS présentes, sans exception : omettre la partie 1 n'est pas une simplification acceptable.
</HARD-GATE>

Toujours **ces deux parties, dans cet ordre** :

1. **Le Gabarit Palambur rempli** · le prompt « prêt à copier-coller », complété bloc par bloc. L'utilisateur repart avec l'outil réutilisable, pas seulement le résultat.
2. **Le livrable final** · le texte prêt à l'emploi.

Deux disciplines non négociables à la production :

- **N'invente jamais.** Toute donnée absente devient un **marqueur visible** (`[À COMPLÉTER]`, `[À VÉRIFIER]`) plutôt qu'une invention. C'est ce qui rend le livrable digne de confiance.
- **Livrable sensible** (RH, contrat, communication externe) → applique les garde-fous suisses et ajoute la mention de protection/validation humaine (voir `protection-donnees.md`).

## Ton

Français **suisse romand**, **vouvoiement**, factuel, **sans superlatif marketing**. Métaphores industrielles/moteur quand elles éclairent. Exemples de voix dans `methode-palambur.md`.

## Exemple de référence

**Requête** : « méthode palambur : fais une offre d'emploi pour un peintre à 80 % »

- Étape 0 : aucune donnée nominative ici → pas de question d'anonymisation, passe à l'Étape 1.
- Étape 1 : livrable ✔ ; manquent canton, missions, profil, avantages, contrat, date → clarifier.
- Étape 2 : lot anticipé de 4 (canton, missions, profil, avantages), puis posé **une question par message** avec le compteur « Question 1 sur 4 », choix multiples et défauts prudents.
- Étape 3 : le prompt rempli, puis l'offre en français suisse romand, neutre de genre, mention nLPD.

**Requête avec données** : « méthode palambur : rédige une relance pour la facture impayée de Menuiserie Rochat SA, 4'820 CHF, échue depuis le 15 juin »

- Étape 0 : données nominatives détectées (nom du client, montant) → **avant tout le reste**, poser la question binaire anonymiser/conserver et s'arrêter. (Cette question reste seule et en premier, on ne la groupe jamais avec les questions métier.)
- Puis Étape 2 : ton et délai sont structurants → lot anticipé de 2, posé une question par message ; n° de facture et IBAN → marqueurs `[À COMPLÉTER]`, pas des questions.

## Fichiers de référence

| Fichier | Quand le lire |
|---|---|
| `methode-palambur.md` | Le Gabarit (5 blocs + 4 extensions), les 4 niveaux S/M/L/XL, champs DONNÉES par livrable, ton & voix, anti-hallucination |
| `protection-donnees.md` | Dès qu'il y a des données : anonymisation, marqueurs, mentions-types, outils souverains, Shadow AI |
