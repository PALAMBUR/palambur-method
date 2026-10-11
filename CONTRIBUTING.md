# Contribuer · Contributing

Français d’abord, English below.

---

## Français

Merci de votre intérêt. Ce dépôt porte **la Méthode Palambur** sous forme de skill : une discipline de clarification avant production, un Gabarit en cinq blocs, des garde-fous suisses et l’interdiction d’inventer. Toute contribution qui renforce l’un de ces quatre points est bienvenue. Toute contribution qui les affaiblit sera discutée avant d’être refusée.

### Trois façons de contribuer

1. **Signaler un défaut** · le skill a posé une mauvaise question, a inventé une donnée, a oublié le compteur, a cité une loi qu’il n’aurait pas dû citer. Ouvrez un ticket avec le modèle « Défaut ».
2. **Proposer un gabarit de livrable** · un fichier dans `skills/palambur-method/gabarits/` pour un livrable fréquent (offre d’emploi, devis, certificat de travail, note interne…) : ses champs DONNÉES, ses garde-fous, un exemple rempli. C’est la contribution la plus utile et la plus simple. Modèle « Nouveau gabarit ».
3. **Corriger une référence juridique** · une loi mal nommée, une base légale périmée, une convention collective citée sans source. Modèle « Correction juridique ».

Les tickets marqués **« bonne première contribution »** sont réservés aux gabarits : une personne qui écrit un gabarit sait de quoi elle parle, et c’est tout ce qu’il faut.

### Avant d’ouvrir une pull request

- **Ne modifiez pas `SKILL.md` ni les adaptations à la main** si votre contribution est un gabarit : le gabarit se pose dans `gabarits/`, le reste suit par la chaîne de contrôle.
- **Lancez la chaîne de contrôle** : `python3 outils/controle.py`. Elle refuse si la typographie, le numéro de version ou les adaptations ne sont pas conformes. Un refus n’est pas une sanction, c’est une indication.
- **Un gabarit = un fichier**, nommé par le livrable, en français suisse romand, vouvoiement, sans superlatif.

### La règle typographique maison, en trois lignes

1. **Aucun tiret de ponctuation** · ni cadratin, ni demi-cadratin, ni trait d’union entre deux mots. Le séparateur est le point médian « · ». Le trait d’union d’un mot composé (garde-fou) et la puce de liste restent.
2. **L’apostrophe est courbe** (’) dans la langue : l’outil, n’est. Elle reste droite seulement entre deux chiffres : 4'820 CHF.
3. **Le sigle français des petites et moyennes entreprises n’existe pas ici** · on écrit « entreprises ». Le contrôle le refuse.

### La règle juridique, en une ligne

**Jamais un numéro d’article de loi sans `[À VÉRIFIER]`.** On nomme le texte (CO, LTr, LEg, nLPD, LCD), on ne cite pas un numéro d’article que personne n’a vérifié à la date de la contribution. Une convention collective n’est jamais citée sans sa source. Si vous êtes certain d’un article, écrivez-le quand même avec le marqueur : la vérification appartient à la personne qui relit, pas à la personne qui écrit.

### Ce que nous ne prenons pas

- Des gabarits qui inventent des valeurs par défaut là où la Méthode exige un marqueur.
- Des références à des outils d’IA qui envoient des données hors de Suisse présentées comme « souverains ».
- Des contributions qui ajoutent de la publicité pour Palambur dans les livrables : le skill est gratuit et il le reste, sans message commercial dans ce qu’il produit.

### Licence

En contribuant, vous acceptez que votre contribution soit publiée sous la licence MIT du dépôt.

---

## English

Thank you for your interest. This repository holds **the Palambur Method** as a skill: a discipline of clarification before production, a five block template, Swiss legal safeguards and a ban on inventing data. Any contribution that strengthens one of these four points is welcome. Any contribution that weakens them will be discussed before it is declined.

### Three ways to contribute

1. **Report a defect** · the skill asked the wrong question, invented a value, forgot the counter, or cited a law it should not have cited. Open an issue with the "Defect" template.
2. **Propose a deliverable template** · a file in `skills/palambur-method/gabarits/` for a frequent deliverable (job advert, quote, employment certificate, internal memo…): its DATA fields, its safeguards, one completed example. This is the most useful and the simplest contribution. "New template" issue.
3. **Correct a legal reference** · a misnamed law, an outdated legal basis, a collective agreement cited without a source. "Legal correction" issue.

Issues labelled **"good first contribution"** are reserved for templates: someone who writes a template knows the subject, and that is all it takes.

### Before opening a pull request

- **Do not edit `SKILL.md` or the adaptations by hand** if your contribution is a template: the template goes in `gabarits/`, everything else follows through the control chain.
- **Run the control chain**: `python3 outils/controle.py`. It refuses when typography, version number or adaptations are not compliant. A refusal is not a sanction, it is a pointer.
- **One template = one file**, named after the deliverable, in Swiss French, formal address, no superlatives.

### The house typography rule, in three lines

1. **No punctuation dash** · no em dash, no en dash, no hyphen between two words. The separator is the middle dot "·". Hyphens inside compound words and list bullets stay.
2. **Apostrophes are curly** (’) in prose: l’outil, n’est. They stay straight only between two digits: 4'820 CHF.
3. **The French acronym for small and medium sized businesses is banned** · we write "entreprises" in French and "businesses" or "organisations" in English. The control chain refuses it.

### The legal rule, in one line

**Never a numbered article of law without `[À VÉRIFIER]`** (to be checked). Name the text (CO, LTr, LEg, nLPD, LCD), never quote an article number nobody has verified at the date of the contribution. A collective agreement is never cited without its source. If you are sure of an article, write it anyway with the marker: verification belongs to the reviewer, not to the writer.

### What we do not accept

- Templates that invent default values where the Method requires a marker.
- References to AI tools that send data outside Switzerland presented as "sovereign".
- Contributions that add advertising for Palambur inside deliverables: the skill is free and stays free, with no commercial message in what it produces.

### Licence

By contributing, you agree that your contribution is published under the repository’s MIT licence.
