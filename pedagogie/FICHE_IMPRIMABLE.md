# Fiche imprimable · « Le Gabarit Palambur »

**Texte et structure d’une page A4 paysage.** La fabrication du PDF revient à la session qui détient le gabarit maison (`0700_BRANDING`) : bandeau en tête, logo en blanc jamais sous le bandeau, filet vertical à gauche, polices de la charte. Ce fichier donne ce qui s’imprime, dans l’ordre, et rien d’autre. Chaque zone est indiquée entre crochets ; les crochets ne s’impriment pas.

---

## [Bandeau]

**Le Gabarit Palambur** · cinq blocs pour demander un document à une IA sans qu’elle invente

## [Colonne gauche · un tiers de la page]

### Avant d’écrire le prompt

**1 · Nommez le livrable.** Une offre d’emploi, un devis, une relance, un contrat, une note. Pas « un texte ».

**2 · Cherchez ce qui manque.** Le canton, le montant, la date, le destinataire, le ton. Ce que vous ne savez pas, l’IA ne le sait pas non plus.

**3 · Protégez les noms.** Un client, un collaborateur, un salaire : remplacez-les par « Client X », « Collaborateur·trice A » avant de coller. Vous les remettrez dans le document final.

**4 · Décidez ce qui reste ouvert.** Un trou visible `[À COMPLÉTER]` vaut mieux qu’une valeur plausible.

### Les trois règles

· **Ce qui n’a pas été dit n’est pas inventé.**
· **Un texte de loi se nomme, un article ne se cite pas** sans `[À VÉRIFIER]`.
· **Le prompt se garde** : il sert la semaine suivante avec d’autres données.

## [Colonne droite · deux tiers de la page]

### Les cinq blocs, dans cet ordre

**INSTRUCTION**
Ce que l’IA doit produire, pour quoi faire. Un verbe à l’impératif, le livrable, l’objectif. *« Rédigez une offre d’emploi pour un poste de peintre en bâtiment à 80 %, afin d’attirer des candidatures qualifiées dans le canton de Vaud. »*

**RÔLE ET AUDIENCE**
Qui écrit, pour qui. Le métier de celui qui parle, ce qu’il sait, et le lecteur qui recevra le texte. *« Vous êtes chargé de recrutement dans une entreprise de Suisse romande, formé au CO, à la LEg et à la nLPD. Vous écrivez pour des candidats du bâtiment. »*

**DONNÉES**
Les faits, et seulement les faits, entre `<donnees>` et `</donnees>`, une ligne par donnée : *« • Taux : 80 % · • Canton : Vaud · • Date d’entrée : [À COMPLÉTER] »*. Ce qui n’y est pas n’existe pas pour l’IA.

**CONTRAINTES**
Ce que l’IA ne doit pas faire. *« Formulation neutre de genre. Aucun critère d’âge, d’origine ou d’état civil. Si une information manque, écrivez [À COMPLÉTER], jamais une valeur plausible. Nommez les textes de loi, ne citez aucun article. »*

**FORMAT**
La forme du résultat : longueur, sections, ton, mention finale. *« Titre, accroche, missions, profil, avantages, modalités de candidature, mention nLPD. 250 à 350 mots. »*

### Pour un livrable à fort enjeu, quatre blocs de plus

**MÉTHODE** · les étapes que l’IA suit, numérotées. **EXEMPLE ÉCLAIR** · une mauvaise phrase et sa bonne version. **ZONES DE RISQUE** · ce qui tourne mal d’habitude. **AUTO-CONTRÔLE** · les questions que l’IA se pose avant de rendre.

Un contrat, un certificat de travail, une charte : neuf blocs. Une relance, une note interne : cinq suffisent.

## [Pied de page]

Les marqueurs · `[À COMPLÉTER]` vous seul savez · `[À VÉRIFIER : base légale]` un texte est nommé, l’article non · `[À ARBITRER]` un choix vous revient · `[À CONFIRMER]` un fait déduit, non établi

Méthode Palambur · skill gratuit, licence MIT · github.com/PALAMBUR/palambur-method · le skill pose ces questions à votre place : écrivez « palambur » dans votre demande

---

## Notes pour la fabrication (ne s’impriment pas)

- Une seule page. Si le texte déborde, raccourcir les exemples en italique, jamais les cinq noms de blocs ni les trois règles.
- Les cinq noms de blocs en capitales, dans la couleur de la charte ; les exemples en italique et en corps plus petit.
- Le pied de page en deux lignes au plus.
- Aucun prix, aucune adresse, aucun nom de personne.
- Vérifier le texte avec `python3 outils/regle_typo.py pedagogie/FICHE_IMPRIMABLE.md` avant de composer.
