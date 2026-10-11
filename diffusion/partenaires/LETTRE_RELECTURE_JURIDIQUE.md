# Relecture juridique externe · brouillon de demande (point 48)

**État** : brouillon préparé le 11.10.2026 par l’agent du paquet 2. Rien n’a été envoyé. Le choix du relecteur (juriste ou fiduciaire), l’envoi et toute rémunération reviennent au fondateur. Les trous sont listés en fin de fichier.

## 1 · La lettre

Objet : relecture de deux fichiers de références juridiques d’un outil gratuit (Méthode Palambur)

Madame, Monsieur,

Palambur publie un outil gratuit et ouvert, la **Méthode Palambur**, qui aide les entreprises de Suisse romande à faire rédiger leurs documents de travail par une IA sans inventer de chiffre ni d’article de loi. Deux de ses fichiers disent **ce que l’outil a le droit de nommer** en matière de droit suisse et français : le nom d’un texte, ce qu’il couvre en une ligne, et ce que l’outil ne doit jamais écrire à son sujet. Ils ne disent pas ce que la loi exige.

Ces fichiers ont été établis par un modèle d’IA à partir de nos propres fiches, et non en lisant chaque texte à la source. Nous le disons en tête de chaque fichier. Nous cherchons une **relecture par une personne habilitée** pour que cette mention change.

Ce que nous vous demandons :

1. Lire les deux fichiers joints (environ `[À COMPLÉTER : nombre]` pages au total).
2. Pour chaque ligne, dire si le **nom** du texte, son **champ** en une ligne et la liste de ce que l’outil **ne doit jamais faire** sont justes, incomplets ou faux.
3. Signaler tout texte que l’outil devrait nommer et qui manque, pour les métiers couverts (ressources humaines, fiduciaires, bâtiment, immobilier, santé, restauration, commerce).
4. Ne pas réécrire les fichiers : vos remarques suffisent, nous les posons et vous les relisez une seconde fois si vous le souhaitez.

Ce que nous ne vous demandons pas : un avis juridique sur un cas, une garantie, ni la vérification des numéros d’articles. L’outil n’en écrit aucun ; chaque numéro porte la marque `[À VÉRIFIER]` par construction.

Ce que nous proposons en retour : votre nom de fonction et votre étude ou fiduciaire, cités dans le dépôt public et sur la page de l’outil comme relecteur de la version `[À COMPLÉTER : numéro de version]`, avec la date de votre relecture (texte exact de la mention au point 3 ci-dessous). Une rémunération peut être discutée `[À DÉCIDER]`.

Les fichiers sont publics (licence MIT), le dépôt est à l’adresse https://github.com/PALAMBUR/palambur-method. Vous pouvez répondre dans le fichier, par courriel ou lors d’un entretien d’une heure.

Avec nos salutations les meilleures,

`[À COMPLÉTER : fonction de la personne qui signe]` · Palambur · https://palambur.ch

## 2 · Ce que l’on soumet

| Fichier | Ce qu’il contient | Ce qu’on attend du relecteur |
|---|---|---|
| `skills/palambur-method/references-juridiques.md` | la règle des quatre lignes ; une table Suisse (CO, CC, LTr, LEg, LPD, OPDo, LCD, LAMal, LAA, LAVS, LPP, LEI, CCT, SIA, LP, LTVA, AIMP, LMP, CP, LDA, CCNT) ; une table France (Code du travail, RGPD, CNIL, Règlement IA) ; une table « Autres marchés » (BE, DE, IT, ES, UK, US) limitée à la mention de protection des données | noms, champs, interdits ; textes manquants ; les lignes « non appuyée » en priorité |
| `skills/palambur-method/protection-donnees.md` | niveau de sensibilité, règle d’anonymisation par défaut, formes détectées, pont vers Jomini, journal de confiance, mentions-types, refus en trois lignes, Shadow AI | les mentions-types sont-elles justes et suffisantes ; le niveau « critique » couvre-t-il ce qu’il doit |
| `skills/palambur-method/metiers/MARCHES.md` § 5 | la mention de protection des données par marché (CH, FR, BE, DE, IT, EN) et par famille de livrable | la mention CH et la mention FR d’abord ; les autres marchés si le relecteur les connaît |
| `VEILLE_JURIDIQUE.md` | les textes suivis, leur source officielle, la date de dernière lecture | le relecteur y inscrit sa relecture (date, fonction) |

Pièces à joindre à l’envoi : les quatre fichiers ci-dessus en `.md` ou en `.pdf` (gabarit PDF maison, fabriqué par la session qui tient le gabarit), et le lien du dépôt.

## 3 · La mention d’accord à publier

À poser dans `references-juridiques.md` (colonne « Vérifié »), dans le README et sur la page du site, **seulement après accord écrit du relecteur** :

> « Références juridiques relues le `[À COMPLÉTER : date]` par `[À COMPLÉTER : fonction, étude ou fiduciaire, localité]`. Cette relecture porte sur les noms des textes et sur ce que l’outil s’interdit d’écrire ; elle ne constitue pas un avis juridique et n’engage pas le relecteur sur les livrables produits. »

Le relecteur valide la phrase mot pour mot avant publication. Il peut demander à ne pas être nommé : la mention devient alors « relues par un juriste indépendant » et sa fonction est conservée dans le journal de `VEILLE_JURIDIQUE.md` seulement.

## 4 · Profil du relecteur · aide au choix, pas une décision

| Profil | Pour | Contre |
|---|---|---|
| Avocat ou juriste d’entreprise (droit du travail et protection des données) | couvre LTr, LEg, CO, LPD d’un seul regard ; mention crédible pour les livrables RH | moins à l’aise sur LTVA, AVS, LPP |
| Fiduciaire (expert fiduciaire ou comptable) | couvre LTVA, AVS, LPP, LP ; c’est aussi un relais de diffusion (plan, point 68) | ne relit pas la LEg ni la LPD au même niveau |
| Les deux, en deux passes | couverture complète | deux envois, deux mentions à concilier |

Recommandation de l’agent : deux passes, le juriste d’abord (la table Suisse est surtout du droit du travail et des données), la fiduciaire ensuite sur les quatre lignes fiscales et sociales.

---

À compléter avant envoi : `[À COMPLÉTER : nombre]` de pages ; `[À COMPLÉTER : numéro de version]` relue ; `[À COMPLÉTER : fonction de la personne qui signe]` ; `[À COMPLÉTER : date]` et `[À COMPLÉTER : fonction, étude ou fiduciaire, localité]` dans la mention. À décider : `[À DÉCIDER]` rémunération ; le choix du relecteur (§ 4).
