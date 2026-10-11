# Temps gagné · protocole de mesure (point 80)

**Protocole · 11.10.2026 · session Skills et Prompt Ingénierie · décision et exécution Victor.** Aucun chiffre de temps gagné n’existe aujourd’hui, et **aucun ne sera écrit nulle part avant que cette mesure ait eu lieu**. Le README, la page du site, les posts et la formation disent « les bonnes questions avant d’écrire », jamais « x minutes gagnées », tant que la table de relevés est vide.

## Ce qu’on mesure

**Le temps entre la demande et un document que la personne déclare prête à envoyer**, pour une même tâche, avec et sans la Méthode, sur la même IA.

Trois mesures secondaires, relevées en même temps :

- le nombre de **corrections** que la personne fait à la main avant de dire « prêt » ;
- le nombre de **données inventées** par l’IA (un nom, un montant, une date, un article de loi qui ne vient pas de la personne) relevées par le lecteur ;
- le nombre de **cases `[À COMPLÉTER]`** restantes dans le document déclaré prêt.

Le temps est la mesure principale parce que c’est elle que le point 80 nomme ; les trois autres disent **ce que le temps achète**. Un document plus rapide mais plein d’inventions n’est pas un gain.

## Qui, combien, où

- **Dix personnes**, qui rédigent des documents de travail dans leur métier et n’ont jamais utilisé le skill. Pas de collaborateur de Palambur, pas de participant à la formation. Fonctions seulement dans le relevé (« responsable RH », « gérant », « assistante de direction »), jamais un nom.
- **Deux tâches** par personne, tirées des gabarits du skill : une **offre d’emploi** et une **relance de facture** (`skills/palambur-method/gabarits/`). Deux tâches de nature différente, pour que le résultat ne tienne pas à un seul livrable.
- **Une IA**, la même pour tout le monde, choisie avant la première séance et écrite dans la table. Si deux IA sont comparées, c’est une mesure de plus, pas la même.
- **Sur place ou en visioconférence**, écran partagé, chronomètre tenu par l’observateur, jamais par la personne.

## Le déroulé · croisé

Chaque personne fait les deux tâches, **une avec la Méthode, une sans**, et l’ordre alterne d’une personne à l’autre : la personne 1 fait l’offre d’emploi sans puis la relance avec ; la personne 2 fait l’offre avec puis la relance sans ; et ainsi de suite. Ainsi ni la tâche ni l’ordre ne favorisent un côté.

Pour chaque tâche :

1. L’observateur lit la **consigne** à voix haute, identique pour tous : « Rédigez une offre d’emploi pour un poste de [métier de la personne] à 80 %, dans votre canton. Vous pouvez tout demander à l’IA. Dites “prêt” quand vous l’enverriez tel quel. » Même forme pour la relance.
2. Le chronomètre part à la première touche, s’arrête au mot « prêt ».
3. L’observateur relève la durée, le nombre de messages échangés, le nombre de corrections à la main, et garde le document final (anonymisé, voir plus bas).
4. Après les deux tâches, **trois questions** à la personne, réponses notées telles quelles : « Laquelle des deux enverriez-vous vraiment ? », « Qu’est-ce qui vous a gêné ? », « Qu’est-ce qui a manqué ? »

**Sans la Méthode** : l’IA telle qu’elle est, sans skill ni prompt système. **Avec** : le skill installé par `outils/installer_local.sh`, ou l’adaptation courte collée (`adaptations/`), selon l’IA choisie ; la personne tape le mot « palambur » dans sa demande, et c’est tout ce qu’on lui dit.

## Ce qu’on relève, et où

Une ligne par tâche dans une table, **vide aujourd’hui**, à poser dans `mesures/` (le dossier existe, avec `releves.csv` pour les mesures de taille ; la table du temps gagné est un fichier à part, `temps_gagne.csv`, colonnes : date · personne (numéro) · fonction · tâche · avec ou sans · durée en secondes · messages · corrections · inventions · cases restantes · IA · observateur). Le dossier `mesures/` appartient au paquet 3 : la création du fichier lui est demandée dans le rapport, elle n’est pas faite ici.

**Le chiffre publié, s’il y en a un**, est la **médiane** des durées avec et sans, et l’écart entre les deux, avec la date de la dernière séance et le nombre de personnes : « médiane sur 10 personnes, séances du [date] au [date] ». Jamais une moyenne seule, jamais un pourcentage sans les deux durées qui le fondent, jamais une extrapolation à l’année.

## Protection des données

- Les documents produits pendant la mesure contiennent le métier et le canton de la personne, parfois le nom de son entreprise : ils sont **anonymisés avant archivage** (Jomini, ou à la main), et seule la version anonymisée est gardée.
- La personne signe le **formulaire d’autorisation** de `diffusion/produit/TEMOIGNAGES_autorisation.md` **avant** la séance, case « mesure » cochée ; sans signature, pas de séance.
- Aucun enregistrement vidéo ou audio ; le relevé de l’observateur suffit.

## Ce qui rendrait la mesure fausse

- Un observateur qui aide la personne pendant la tâche (il se tait, il chronomètre).
- Une personne qui connaît déjà le skill.
- Changer d’IA, de modèle ou de version du skill entre deux personnes sans l’écrire dans la table.
- Arrêter la mesure parce que les premiers résultats plaisent ou déplaisent : les dix se font.

## Ce qui exige Victor

1. Choisir **l’IA** de la mesure et la **version** du skill (étiquette Git).
2. Trouver **dix personnes** et obtenir leur signature.
3. Tenir le chronomètre, ou désigner qui le tient.
4. Décider, **après** la dixième ligne, si le résultat se publie, et où.

## Trous et décisions

- `[À DÉCIDER]` · l’IA et la version du skill.
- `[À DÉCIDER]` · les dates des séances.
- `[À COMPLÉTER]` · la table `mesures/temps_gagne.csv` (paquet 3, demande dans le rapport).
