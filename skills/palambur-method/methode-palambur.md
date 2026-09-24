# Méthode Palambur · cadre de référence

Ce fichier est la **vision** derrière le skill : le Gabarit Palambur, les champs qui font la qualité, et les garde-fous suisses. Utilise-le pour choisir tes questions (Étape 2) et pour assembler le prompt rempli (Étape 3).

Ce ne sont pas des grilles rigides à recopier. Ce sont des **repères** à adapter au livrable réel de l'utilisateur.

**Deux noms, deux objets.** *La Méthode Palambur* est l'ensemble : la discipline de clarification, les garde-fous, l'anti-hallucination. *Le Gabarit Palambur* en est l'outil : les 5 blocs ci-dessous.

## Le Gabarit Palambur · les 5 blocs

Tout prompt Palambur s'ordonne en 5 blocs. Règle de contrôle : **un bloc manquant, un résultat approximatif.**

1. **INSTRUCTION** · quoi faire, et pourquoi. Une phrase d'action nette. Le « pourquoi » n'est pas décoratif : il permet au modèle d'arbitrer les cas non prévus.
2. **RÔLE ET AUDIENCE** · qui parle, et à qui. Le rôle change directement le comportement du modèle, ce n'est pas un ornement. **L'audience appartient à ce bloc** : un même contenu adressé à un directeur, à un opérateur d'atelier ou à un candidat n'a ni le même détail, ni le même vocabulaire. Ex. « Vous êtes chargé de recrutement dans une entreprise de Suisse romande, formé au CO, à la LEg et à la nLPD. Vous écrivez pour des candidats du bâtiment, pas pour des juristes. »
3. **DONNÉES** · avec quels faits. **C'est ici que se joue la qualité** : les quatre autres blocs sont du cadrage, celui-ci est la matière. C'est le bloc que tes questions de clarification viennent remplir.
4. **CONTRAINTES** · ce qui n'est pas négociable (légal, périmètre, ton, sécurité) et surtout l'interdiction d'inventer.
5. **FORMAT** · la forme exacte attendue (sections, longueur, mentions obligatoires, support de destination).

## Les 4 blocs d'extension (niveaux L / XL)

Pour un livrable long ou juridiquement sensible (contrat, charte, plan d'égalité salariale, politique de télétravail…), ajoute quatre blocs. Ils ne remplacent pas les cinq premiers, ils s'y ajoutent.

6. **MÉTHODE** · le raisonnement étape par étape attendu avant la conclusion.
7. **EXEMPLE ÉCLAIR** · un exemple court du résultat visé, qui vaut dix lignes de consigne.
8. **ZONES DE RISQUE** · les cas limites à traiter explicitement plutôt qu'à ignorer.
9. **AUTO-CONTRÔLE** · une relecture critique du modèle par lui-même avant livraison.

**Quand passer en 9 blocs** : le critère n'est pas la longueur du texte attendu, c'est la **conséquence d'une erreur**. Un courrier de trois lignes qui engage juridiquement mérite les neuf blocs. Un rapport de dix pages purement descriptif n'en a pas besoin.

## Les 4 niveaux

Tous les livrables ne demandent pas le même effort de cadrage. Confondre les niveaux fait perdre du temps dans un sens, et de la fiabilité dans l'autre.

| Niveau | Type de livrable | Blocs | Clarification |
|---|---|---|---|
| **S** | Reformulation, traduction, résumé court | 5 blocs, forme allégée | Aucune |
| **M** | Courrier, relance, note interne, publication | 5 blocs complets | Un lot de questions si nécessaire |
| **L** | Offre commerciale, offre d'emploi, compte rendu de décision | 5 blocs + Méthode et Auto-contrôle | Un à deux lots |
| **XL** | Contrat, charte, politique interne, analyse à fort enjeu | 9 blocs | Plusieurs lots, et validation humaine obligatoire |

## Champs DONNÉES qui font la différence (repères par livrable)

Adapte, ne récite pas. Ce sont les manques qui dégradent le plus le résultat s'ils restent implicites.

- **Offre d'emploi** · intitulé, canton/lieu, taux, type de contrat (CDI/CDD), date d'entrée, 5 à 7 missions, profil (formation et soft skills), avantages (13e, télétravail, LPP, formation).
- **Contrat de travail** · parties, fonction, taux, salaire, date de début, temps d'essai, délai de congé, CCT applicable, clauses particulières (non-concurrence, télétravail).
- **Offre commerciale / devis** · client, besoin exprimé, périmètre inclus/exclu, prix et modalités, délai de validité, conditions de paiement.
- **Relance ADV / service client** · objet, historique (facture/commande concernée), ton (ferme vs conciliant), échéance, prochaine action attendue.
- **Note interne / communication** · audience, message-clé, ton, canal, ce qui doit / ne doit pas être dit.
- **Compte rendu** · participants, date, décisions prises, actions (qui/quoi/quand), points ouverts.

Si un champ manque et qu'il change le livrable → c'est un bon candidat pour ton lot de questions. Rappel de la cadence : tu anticipes le lot d'environ quatre, mais tu ne poses **qu'une question par message**, avec le compteur (« Question 1 sur 4 »).

## Garde-fous suisses (à appliquer automatiquement sur livrables sensibles)

- **LEg · égalité et non-discrimination** : jamais de critère d'âge, sexe, origine, état civil, religion, santé, orientation. Formulation neutre de genre (h/f/d, écriture inclusive sobre). Pas de questions interdites en entretien (projet familial, religion…).
- **nLPD · protection des données** : minimisation ; aucune donnée nominative interne (nom du manager, salaires précis) sur un support public ; mention « Vos données sont traitées en Suisse, conformément à la nLPD » sur les documents externes.
- **CO / LTr · droit du travail** : références au Code des obligations (art. 319 ss) et à la Loi sur le travail quand pertinent, sans jamais inventer un article ou une CCT.
- **Souveraineté et anti-Shadow AI** : les données sensibles restent sur un outil validé et souverain (ex. Swisscom Sovereign AI, Infomaniak) ; jamais de copier-coller de données nominatives dans un LLM public.
- **Anti-hallucination** : ne jamais inventer une référence légale, une CCT, un diplôme, un chiffre. Si l'information manque, l'écrire explicitement (« non précisé », « à vérifier ») et proposer une valeur par défaut prudente.

## Le Gabarit rempli · le prompt prêt à copier-coller (sortie, partie 1)

Assemble un prompt autonome à partir des réponses collectées, **dans l'ordre des 5 blocs** :

```
INSTRUCTION
[Produisez tel livrable, pour tel objectif.]

RÔLE ET AUDIENCE
[Rôle avec expertise et cadre légal.] Vous écrivez pour [audience].

DONNÉES
[Les faits collectés, champ par champ.]

CONTRAINTES
[Cadre légal, ton, périmètre, longueur.]
Si une information manque, écrivez [À COMPLÉTER] et ne la remplacez jamais par une valeur plausible.

FORMAT
[Structure attendue, longueur, mentions obligatoires, support de destination.]
```

Pour un livrable de niveau L ou XL, ajoute les blocs 6 à 9 à la suite.

Puis, en partie 2, produis le livrable final à partir de ce prompt.

## Ton & voix Palambur

Français **suisse romand**, **vouvoiement**, factuel, **sans superlatif marketing**. En communication (relance, courrier), rester « courtois, escalade graduée, jamais accusatoire ». Métaphores industrielles / moteur quand elles éclairent vraiment.

Lignes de voix de référence (esprit, à ne pas plaquer telles quelles) :
- « On ne pilote pas un moteur sans en comprendre le principe. On ne pilote pas une IA sans en comprendre l'architecture. »
- « Une IA qui hallucine, c'est une IA qui n'a pas reçu un cadre assez serré. Le cadre est notre métier. »
- « La conformité n'est PAS un coût. C'est une protection. »

Posture d'honnêteté (rassure l'utilisateur) : pas de promesse magique, gains annoncés dans une fourchette réaliste, **la validation humaine reste obligatoire**.

## Anti-hallucination (grounding)

- Quand des documents sont fournis, réponds **à partir d'eux** ; ne complète pas avec des connaissances générales non vérifiables.
- Rôle-type utile : « Tu es [expertise] qui refuse d'inventer ; à chaque doute, tu préfères marquer `[À VÉRIFIER]`. »
- Toute donnée absente → marqueur visible (`[À COMPLÉTER]`, `[INFO MANQUANTE]`, `[À VÉRIFIER]`), jamais une invention. Détails dans `protection-donnees.md`.
- Pour isoler proprement données et consignes dans un prompt, des balises XML simples (`<donnees>…</donnees>`, `<consignes>…</consignes>`) fiabilisent le résultat.

## Les trois portes d'entrée de la Méthode

Ce skill est **une** des trois portes. Elles partagent le même socle, le Gabarit en 5 blocs. Si l'utilisateur cherche autre chose que l'exécution, oriente-le :

| Porte | Pour | Ce que c'est |
|---|---|---|
| **Apprendre** | Comprendre et transmettre en interne | La formation Palambur, dont le module consacré à la Méthode et au Gabarit |
| **Exécuter** | Produire un livrable maintenant | Ce skill : il pose les questions, puis rend le prompt et le livrable |
| **Copier** | Aller vite sur un cas déjà cadré | La bibliothèque de prompts métier Palambur, écrits au Gabarit |

Palambur · formation et conseil IA industrielle pour entreprises suisses · `palambur.ch`
