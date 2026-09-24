# Palambur

[![Security: A — Skills Directory](https://www.skillsdirectory.com/api/skills/palambur-palambur-method/badge)](https://www.skillsdirectory.com/skills/palambur-palambur-method)

Plugin de skills [Claude Code](https://docs.claude.com/en/docs/claude-code) au standard communautaire (inspiré de [superpowers](https://github.com/obra/superpowers)).

## Méthode Palambur

Le skill `palambur-method` transforme une requête métier **sous-spécifiée** en **livrable de haute qualité**, en comblant le contexte manquant *avant* de produire. Pensé pour les entreprises de Suisse romande.

**Deux noms, deux objets.** *La Méthode Palambur* est l'ensemble : la discipline de clarification, les garde-fous suisses, l'anti-hallucination. *Le Gabarit Palambur* en est l'outil : les **5 blocs** ordonnés d'un prompt, Instruction · Rôle et audience · Données · Contraintes · Format, plus 4 blocs d'extension pour les livrables à fort enjeu.

Au lieu de :

> « fais une offre d'emploi pour un peintre à 80 % »

…qui donnerait un texte générique, le skill **clarifie d'abord**. Il anticipe en interne un lot d'environ quatre questions déterminantes (canton, missions, profil, avantages…), mais n'en pose **qu'une par message**, avec un compteur (« Question 1 sur 4 »), un défaut prudent signalé et une échappatoire. Puis il livre :

1. le **Gabarit Palambur rempli** (prêt à copier-coller, réutilisable) ;
2. le **livrable final** rédigé, avec les garde-fous suisses (LEg, nLPD, CO/LTr, souveraineté).

### Déclenchement

Le skill s'active dès que le message contient **« palambur »**, **« méthode palambur »** ou **« palambur method »**. Une fois déclenché : s'il manque des éléments déterminants, il clarifie ; si tout est fourni, il produit directement.

## Installation

Ajouter ce dépôt comme marketplace, puis installer le plugin :

```
/plugin marketplace add PALAMBUR/palambur-method
/plugin install palambur
```

Ou cloner localement dans le dossier des plugins de votre installation Claude Code.

## Structure

```
palambur-method/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── skills/
│   └── palambur-method/
│       ├── SKILL.md               # quand se déclencher + le déroulé (Étapes 0→3)
│       ├── methode-palambur.md    # le Gabarit (5 + 4 blocs), les 4 niveaux, champs DONNÉES, ton
│       └── protection-donnees.md  # anonymisation, marqueurs, mentions nLPD, outils souverains
├── adaptations/                   # versions prompt pour ChatGPT, Gemini, Mistral, Infomaniak
└── README.md
```

## Autres IA (ChatGPT, Gemini, Mistral, Infomaniak)

Ces plateformes n'ont pas la divulgation progressive de Claude Code. Le dossier [`adaptations/`](adaptations/) fournit la méthode condensée en **un prompt système autonome** (deux tailles) et un **guide d'installation par plateforme** : GPT personnalisé, Gem, Agent Mistral, AI Tools / Euria d'Infomaniak.

## Licence

MIT
