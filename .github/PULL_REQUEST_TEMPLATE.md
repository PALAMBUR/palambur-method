<!-- English first, Français below. Cochez ce qui s’applique · une case non cochée sans explication fait attendre la pull request. -->

## English

**What this pull request changes** (a template, a legal correction, a language, a tool…)

…

**Why** (the defect observed, the linked issue · `#…`)

…

### Checks · the rules of `CONTRIBUTING.md`

- [ ] `python3 outils/controle.py` passes
- [ ] `python3 outils/generer_adaptations.py --ecrire` was rerun if any file under `skills/` changed · the adaptations follow the skill, they are never edited by hand
- [ ] No numbered article of law without `[À VÉRIFIER]` · the text is named (CO, LTr, LEg, nLPD, LCD), no collective agreement without a source
- [ ] The banned French acronym for small and medium sized businesses does not appear · write "entreprises"
- [ ] House typography · no punctuation dash, "·" separator, curly apostrophes in prose, straight only between two digits
- [ ] Example data is fictional · no real name, no address, no real amount
- [ ] For a new language · a native speaker reviewer, other than the translator, named by their **role** (never their name), with the review date and the files reviewed
- [ ] `CHANGELOG.md` is updated under “Unreleased”

---

## Français

**Ce que change cette pull request** (un gabarit, une correction juridique, une langue, un outil…)

…

**Pourquoi** (le défaut observé, le ticket lié · `#…`)

…

### Vérifications · les règles de `CONTRIBUTING.md`

- [ ] `python3 outils/controle.py` est vert
- [ ] `python3 outils/generer_adaptations.py --ecrire` a été relancé si un fichier de `skills/` a changé · les adaptations suivent le skill, on ne les édite pas à la main
- [ ] Aucun numéro d’article de loi sans `[À VÉRIFIER]` · le texte est nommé (CO, LTr, LEg, nLPD, LCD), aucune convention collective sans source
- [ ] Le sigle interdit par la règle de marque n’apparaît pas · on écrit « entreprises »
- [ ] Typographie maison · aucun tiret de ponctuation, séparateur « · », apostrophe courbe dans la langue, droite entre deux chiffres
- [ ] Les données d’exemple sont fictives · aucun nom réel, aucune adresse, aucun montant réel
- [ ] Pour une nouvelle langue · un relecteur natif, autre que la personne qui traduit, nommé par sa **fonction** (jamais son nom), avec la date de sa relecture et les fichiers relus
- [ ] `CHANGELOG.md` est mis à jour sous « Unreleased » (le journal s’écrit en anglais depuis le 13.10.2026)
