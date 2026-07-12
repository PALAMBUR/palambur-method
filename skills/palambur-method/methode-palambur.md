# Méthode Palambur — cadre de référence

Ce fichier est la **vision** derrière le skill : la structure de prompt, les champs qui font la qualité, et les garde-fous suisses. Utilise-le pour choisir tes questions (Étape 2) et pour assembler le prompt rempli (Étape 3).

Ce ne sont pas des grilles rigides à recopier. Ce sont des **repères** à adapter au livrable réel de l'utilisateur.

## Les 5 blocs

Tout prompt Palambur s'ordonne en 5 blocs :

1. **INSTRUCTION · clarté** — QUOI faire et POURQUOI. Une phrase d'action nette.
2. **RÔLE · expertise** — le persona/expertise à endosser (ex. « chargé·e de recrutement PME suisse romande, formé·e au CO, à la LEg, à la nLPD »).
3. **DONNÉES · contexte** — les faits concrets fournis. **C'est ici que se joue la qualité** : c'est le bloc que tes questions de clarification viennent remplir.
4. **CONTRAINTES · limites** — ce qui est non négociable (légal, ton, périmètre, sécurité).
5. **FORMAT · output** — la forme exacte attendue (sections, longueur, ton, mentions obligatoires).

## Les 4 blocs supplémentaires (cas complexes, niveaux L / XL)

Pour un livrable juridiquement sensible ou long (contrat, charte, plan d'égalité salariale, politique de télétravail…), ajoute :

6. **MÉTHODE** — raisonnement étape par étape (chain-of-thought) attendu.
7. **EXEMPLE ÉCLAIR** — un exemple court (few-shot) qui montre le résultat visé.
8. **ZONES DE RISQUE** — les cas limites à surveiller.
9. **AUTO-CONTRÔLE** — une auto-relecture critique avant de livrer.

## Champs DONNÉES qui font la différence (repères par livrable)

Adapte, ne récite pas. Ce sont les manques qui dégradent le plus le résultat s'ils restent implicites.

- **Offre d'emploi** — intitulé, canton/lieu, taux, type de contrat (CDI/CDD), date d'entrée, 5–7 missions, profil (formation + soft skills), avantages (13e, télétravail, LPP, formation).
- **Contrat de travail** — parties, fonction, taux, salaire, date de début, temps d'essai, délai de congé, CCT applicable, clauses particulières (non-concurrence, télétravail).
- **Offre commerciale / devis** — client, besoin exprimé, périmètre inclus/exclu, prix et modalités, délai de validité, conditions de paiement.
- **Relance ADV / service client** — objet, historique (facture/commande concernée), ton (ferme vs conciliant), échéance, prochaine action attendue.
- **Note interne / communication** — audience, message-clé, ton, canal, ce qui doit / ne doit pas être dit.
- **Compte-rendu** — participants, date, décisions prises, actions (qui/quoi/quand), points ouverts.

Si un champ manque et qu'il change le livrable → c'est un bon candidat pour ta prochaine question (une à la fois).

## Garde-fous suisses (à appliquer automatiquement sur livrables sensibles)

- **LEg — égalité / non-discrimination** : jamais de critère d'âge, sexe, origine, état civil, religion, santé, orientation. Formulation neutre de genre (h/f/d, écriture inclusive sobre). Pas de questions interdites en entretien (projet familial, religion…).
- **nLPD — protection des données** : minimisation ; aucune donnée nominative interne (nom du manager, salaires précis) sur un support public ; mention « Vos données sont traitées en Suisse, conformément à la nLPD » sur les documents externes.
- **CO / LTr — droit du travail** : références au Code des obligations (art. 319 ss) et à la Loi sur le travail quand pertinent — sans jamais inventer un article ou une CCT.
- **Souveraineté / anti–Shadow AI** : les données sensibles restent sur un outil validé et souverain (ex. Swisscom Sovereign AI, Infomaniak) ; jamais de copier-coller de données nominatives dans un LLM public.
- **Anti-hallucination** : ne jamais inventer une référence légale, une CCT, un diplôme, un chiffre. Si l'information manque, l'écrire explicitement (« non précisé », « à vérifier ») et proposer une valeur par défaut prudente.

## Gabarit du « prompt prêt à copier-coller » (sortie, partie 1)

Assemble un prompt autonome à partir des réponses collectées, dans cet esprit :

```
Tu es [RÔLE avec expertise + cadre légal].
[INSTRUCTION : produis tel livrable, pour tel objectif].
Contexte : [DONNÉES collectées, champ par champ].
Contraintes : [CONTRAINTES légales et de ton applicables].
Format : [structure attendue, longueur, mentions obligatoires].
Si une donnée manque, signale-le et propose une formulation prudente à valider.
```

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
