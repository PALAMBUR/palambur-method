---
name: "Nouvelle langue ou nouveau marché · New language or market"
about: "Proposer une version de la Méthode dans une autre langue ou pour un autre pays · Propose a version of the Method in another language or for another country"
title: "[Langue] "
labels: ["langue"]
---

<!-- Français d’abord, English below. Une langue = un marché nommé, un cadre légal nommé, une relecture par un locuteur natif. -->

## Français

**La langue et le marché visés** (code langue et pays, par exemple `de-CH`, `it-CH`, `en-US`, `fr-BE`)

…

**Ce qui est traduit** (le corps du skill, un fichier de référence, un gabarit, un prompt d’adaptation · nommer les fichiers)

…

**Ce qui est adapté, pas seulement traduit** · le cadre légal change avec le pays (en Suisse on nomme le CO, la LTr, la LEg, la nLPD ; ailleurs d’autres textes). Nommer les textes du marché visé, chaque numéro d’article avec `[À VÉRIFIER]`, et les montants au niveau de prix du pays, jamais convertis depuis le franc suisse.

…

**Qui traduit, et quelle est sa langue maternelle** (fonction, pas de nom de personne obligatoire)

…

**Le locuteur natif qui relit** · la règle du dépôt (`CONTRIBUTING.md`) exige qu’une langue ajoutée soit relue par une personne dont c’est la langue maternelle, autre que la personne qui traduit. Indiquer la fonction du relecteur et la date de la relecture.

…

**Vérifications**

- [ ] Relecture faite par un locuteur natif, autre que la personne qui traduit, date indiquée
- [ ] Les textes de loi du pays sont nommés, chaque numéro d’article porte `[À VÉRIFIER]`
- [ ] Les exemples chiffrés sont au niveau de prix du pays, avec date et source
- [ ] Aucun tiret de ponctuation, séparateur « · », apostrophes courbes
- [ ] Le sigle interdit par la règle de marque n’apparaît pas · on écrit « entreprises »
- [ ] Les marqueurs `[À COMPLÉTER]` et `[À VÉRIFIER]` restent en français dans toutes les langues
- [ ] `python3 outils/controle.py` passe

---

## English

**Target language and market** (language and country code, for example `de-CH`, `it-CH`, `en-US`, `fr-BE`)

…

**What is translated** (the skill body, a reference file, a template, an adaptation prompt · name the files)

…

**What is adapted, not merely translated** · the legal framework changes with the country (in Switzerland we name the CO, LTr, LEg, nLPD; elsewhere other texts). Name the texts of the target market, every article number with `[À VÉRIFIER]`, and amounts at the country’s price level, never converted from Swiss francs.

…

**Who translates, and their native language** (role, no personal name required)

…

**The native speaker who reviews** · the repository rule (`CONTRIBUTING.md`) requires that any added language be reviewed by a person whose native language it is, other than the translator. Give the reviewer’s role and the review date.

…

**Checks**

- [ ] Review done by a native speaker, other than the translator, date given
- [ ] The country’s legal texts are named, every article number carries `[À VÉRIFIER]`
- [ ] Figures are at the country’s price level, with date and source
- [ ] No punctuation dash, "·" separator, curly apostrophes
- [ ] The banned French acronym for small and medium sized businesses does not appear · write "entreprises"
- [ ] The markers `[À COMPLÉTER]` and `[À VÉRIFIER]` stay in French in every language
- [ ] `python3 outils/controle.py` passes
