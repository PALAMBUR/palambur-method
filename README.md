# Palambur

Plugin de skills [Claude Code](https://docs.claude.com/en/docs/claude-code) au standard communautaire (inspiré de [superpowers](https://github.com/obra/superpowers)).

## Méthode Palambur

Le skill `palambur-method` transforme une requête métier **sous-spécifiée** en **livrable de haute qualité**, en comblant le contexte manquant *avant* de produire — pensé pour les PME de Suisse romande.

Au lieu de :

> « fais une offre d'emploi pour un peintre à 80 % »

…qui donnerait un texte générique, le skill pose **une question à la fois** (canton, missions, profil, avantages…) puis livre :

1. le **prompt Méthode Palambur rempli** (prêt à copier-coller, réutilisable) ;
2. le **livrable final** rédigé, avec les garde-fous suisses (LEg, nLPD, souveraineté).

### Déclenchement

Le skill s'active dès que le message contient **« palambur »**, **« méthode palambur »** ou **« palambur method »**. Une fois déclenché : s'il manque des éléments déterminants, il clarifie ; si tout est fourni, il produit directement.

## Installation

Ajouter ce dépôt comme marketplace, puis installer le plugin :

```
/plugin marketplace add PALAMBUR/palambur
/plugin install palambur
```

Ou cloner localement dans le dossier des plugins de votre installation Claude Code.

## Structure

```
palambur/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── skills/
│   └── palambur-method/
│       ├── SKILL.md              # quand se déclencher + le déroulé
│       └── methode-palambur.md   # cadre : 5 blocs, champs DONNÉES, garde-fous
└── README.md
```

## Licence

MIT
