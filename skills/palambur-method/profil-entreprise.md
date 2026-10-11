# Profil d’entreprise · modèle

Ce fichier est un **modèle**. Copiez-le tel quel à la **racine de votre dossier de travail** sous le nom `profil-entreprise.md`, remplissez les champs qui ne changent pas d’un livrable à l’autre, laissez `[À COMPLÉTER]` sur les autres. Le skill le lit à l’Étape 1, **avant toute question** : un champ rempli vaut réponse, et la question correspondante ne vous est plus posée. Le compteur annonce le lot restant (« Question 1 sur 2 » au lieu de « Question 1 sur 4 »).

## Ce que le profil tranche, et ce qu’il ne tranche pas

- Il tranche les questions de **cadre** : canton, convention collective, ton, signature, langue, marché, formats. Elles reviennent dans presque chaque livrable, et elles ne changent pas d’une semaine à l’autre.
- Il ne tranche **jamais** la question d’anonymisation (Étape 0) : elle se pose à chaque demande qui porte des données nominatives, parce que la décision dépend du livrable, pas de l’entreprise.
- Il ne tranche pas ce qui change à chaque livrable (missions d’un poste, montant d’une facture, destinataire) : ces champs restent des questions ou des marqueurs.
- Une précision donnée dans la demande l’emporte sur le profil.

## Ce que le profil ne contient pas, et où il reste

- **Aucun nom de personne**, aucun salaire, aucun numéro de client : la signature est une **fonction** (« La direction »), jamais un nom.
- Il **reste sur votre machine**. Le skill le lit, il n’en recopie dans un livrable que le champ utile (le canton, le nom d’une convention collective), et il ne l’envoie nulle part. Si votre dossier est versionné, ajoutez `profil-entreprise.md` à votre `.gitignore` tant qu’il porte des informations que vous ne publieriez pas.
- Sur les hôtes sans accès aux fichiers (les prompts d’adaptation collés dans un autre assistant), le profil n’existe pas : les mêmes champs se donnent dans la demande.

## Le modèle à copier

```
PROFIL D’ENTREPRISE · Méthode Palambur · relu le [À COMPLÉTER : jj.mm.aaaa]

Entreprise (raison sociale, telle qu’elle s’écrit dans un courrier) : [À COMPLÉTER]
Activité, en une ligne : [À COMPLÉTER]
Canton du siège · lieu de travail principal : [À COMPLÉTER]
Marché et droit applicable (Suisse romande si rien n’est dit) : [À COMPLÉTER]
Langue de rédaction (français de Suisse romande, vouvoiement, si rien n’est dit) : [À COMPLÉTER]
Convention collective de travail applicable, nom seulement : [À COMPLÉTER] [À VÉRIFIER : CCT applicable]
Ton attendu (factuel et sobre · chaleureux · institutionnel) : [À COMPLÉTER]
Signature des documents (une fonction, jamais un nom) : [À COMPLÉTER]
Formule de politesse habituelle : [À COMPLÉTER]
Formats (dates jj.mm.aaaa · montants CHF 4'820.– · heures 14h00, si rien n’est dit) : [À COMPLÉTER]
Outil de réception des candidatures · pays d’hébergement : [À COMPLÉTER]
Durée de conservation des dossiers de candidature non retenus : [À COMPLÉTER]
Ce qui ne doit jamais figurer dans un document sortant : [À COMPLÉTER]
```

Un champ laissé `[À COMPLÉTER]` n’est pas une faute : le skill posera la question quand elle compte, ou laissera le marqueur dans le livrable. Les trous de ce modèle sont volontaires, c’est vous qui les remplissez.
