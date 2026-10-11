# Infomaniak · demande pour figurer dans les exemples d’usage d’Euria et d’AI Tools (point 66)

**Brouillon · rien n’est envoyé · go Victor.** Préparé le 11.10.2026. Aucun contact pris avec Infomaniak. Les citations ci-dessous sont **mot pour mot** celles des pages lues ce jour ; les noms de personnes ne figurent pas, on écrit à une fonction.

## Ce qu’on demande, et pourquoi à Infomaniak

Palambur demande que la Méthode Palambur figure **parmi les exemples d’usage** qu’Infomaniak montre pour Euria (assistant de kSuite) et pour AI Tools / AI Services (API). L’argument est la **souveraineté** : la méthode protège les données par défaut et ne les envoie nulle part ; Euria est le seul des hôtes relevés dans `portabilite/VEILLE_PLATEFORMES.md` qui soit hébergé en Suisse. Les deux promesses se complètent, et Infomaniak gagne un exemple concret, suisse, gratuit et vérifiable.

**Ce qui a été lu le 11.10.2026**, et seulement cela :

| Page | Ce qu’elle écrit (mot pour mot) | Ce qu’on en tire |
|---|---|---|
| `https://www.infomaniak.com/fr/euria` | « Exclusivement hébergée en Suisse » · « L’IA souveraine d’Infomaniak garantit la gouvernance de vos données ainsi qu’une conformité totale à la LPD et au RGPD. » | Euria est l’hôte à nommer dans l’argument souveraineté |
| `https://www.infomaniak.com/fr/hebergement/ai-services` | « Nos services d’IA et GPU sont propulsés au coeur de l’Europe dans nos data centers en Suisse, sans dépendance à des acteurs étrangers. » · « Aucune requête n’est stockée » | AI Services pour les entreprises qui branchent leur propre assistant |
| FAQ 2907 et 1369 (relevées dans la veille) | Euria offre des **Projets** avec Instructions et documents ; kSuite Free, 2 projets | la méthode s’y pose en collant le prompt complet, sans développement |
| FAQ 2177 (relevée dans la veille) | le system prompt d’un assistant AI Tools se règle dans le Manager | idem pour AI Tools |

**Ce qui n’a pas été trouvé** : une page « exemples d’usage », « cas d’usage » ou « témoignages » pour Euria ou AI Services. Le relevé des titres de la page Euria (grep « exemple », « cas d’usage ») n’en montre pas. La demande est donc formulée **sans présumer du format** : galerie d’exemples, article de blog, FAQ, fiche dans le Manager. `[À VÉRIFIER : existence d’une rubrique d’exemples ou de témoignages chez Infomaniak, et son responsable]`.

## Ce que Palambur apporte, concrètement

1. **Un Projet Euria prêt** : nom, description, instructions (le bloc sous le trait de `adaptations/methode-palambur-prompt.md`, version complète, dont la tête dit déjà qu’il vise « Infomaniak · Euria (kSuite) »). Un utilisateur de kSuite Free le reconstitue en cinq minutes avec la FAQ 2907.
2. **Un system prompt AI Tools** identique, pour les entreprises qui branchent un assistant sur l’API.
3. **Un texte d’exemple** de 150 à 300 mots, au choix d’Infomaniak (ci-dessous), et une démonstration enregistrable : la relance de facture avec un nom de client et un montant, où la première réponse de l’assistant est la question d’anonymisation.
4. **La licence MIT** : Infomaniak peut reproduire la méthode, la citer, l’adapter, sans rien demander.

En retour, Palambur ne demande **ni paiement, ni lien commercial, ni exclusivité** : une mention dans les exemples, avec le lien vers le dépôt. Palambur est client d’AI Services `[À VÉRIFIER : Victor confirme le produit et depuis quand, avant d’écrire la phrase]`.

## Le message · brouillon (vouvoiement, sobre, moins de 250 mots)

**Destinataire** : l’équipe produit Euria, ou la personne en charge des partenariats et du contenu chez Infomaniak (fonction à relever le jour de l’envoi ; canal `[À DÉCIDER : formulaire de contact, adresse presse ou partenariats, LinkedIn de l’entreprise]`).

**Objet** : Une méthode publiée sous licence MIT, pensée pour Euria · proposition d’exemple d’usage

> Madame, Monsieur,
>
> Palambur, entreprise de conseil à Neuchâtel, a publié sous licence MIT une méthode qui oblige un assistant d’IA à **poser quatre questions avant d’écrire** un document d’entreprise, à **anonymiser par défaut** les noms et les montants qu’on lui confie, et à ne jamais remplacer une information manquante par une valeur plausible. Elle est gratuite, publique et vérifiable ligne à ligne : github.com/PALAMBUR/palambur-method.
>
> Nous l’avons adaptée à **Euria** : elle se pose dans un Projet, par ses Instructions, sans aucun développement. Nous l’avons choisie pour cela parce que votre page écrit qu’Euria est « Exclusivement hébergée en Suisse » : une méthode qui protège les données n’a de sens que sur un hôte qui ne les exporte pas. La même adaptation sert de system prompt à un assistant **AI Tools**.
>
> Nous vous proposons de la faire figurer **parmi vos exemples d’usage**, sous la forme qui vous convient : un projet Euria prêt à reproduire, un texte court, une démonstration. Nous ne demandons ni rémunération ni lien commercial : une mention et le lien vers le dépôt.
>
> Si le sujet vous paraît utile, un échange de vingt minutes suffit pour voir la forme qui convient à vos pages.
>
> Avec nos salutations les meilleures,
>
> La direction de Palambur · palambur.ch · contact@palambur.ch

## Le texte d’exemple à proposer (250 mots, Infomaniak coupe ce qu’il veut)

> **Quatre questions avant d’écrire, sur une IA hébergée en Suisse**
>
> Une entreprise de conseil neuchâteloise, Palambur, a publié sous licence MIT une méthode de travail pour les assistants d’IA : avant de rédiger un document d’entreprise, l’assistant pose au plus quatre questions, une par message, puis rend le document et le prompt complet qui l’a produit. Ce qui n’a pas été dit n’est pas inventé : il reste écrit `[À COMPLÉTER]`.
>
> La première règle passe avant toutes les autres : si la demande contient le nom d’un client, un montant ou une adresse, l’assistant propose d’abord de les anonymiser, et c’est le réglage par défaut. Les numéros de facture et les coordonnées bancaires ne lui sont jamais confiés ; ils deviennent des cases à remplir à la main.
>
> Sur Euria, la méthode se pose en cinq minutes : un Projet, et ses Instructions. Aucun développement, aucun compte supplémentaire, aucune donnée qui quitte la Suisse. Pour une fiduciaire qui rédige des relances pour ses clients, pour un service du personnel qui écrit des certificats de travail, c’est la combinaison la plus courte entre une méthode qui protège et un hôte qui ne transfère pas.
>
> La méthode, ses fichiers et sa chaîne de contrôle sont publics : github.com/PALAMBUR/palambur-method.

## Ce qui exige Victor

- Le **go d’envoi**, le canal et la fonction destinataire relevée le jour même.
- La phrase « client d’AI Services » : la garder, la préciser ou la retirer.
- Si Infomaniak répond oui : la relecture du texte final, et la cohérence avec `diffusion/PAGE_SITE_methode.md` (la page site doit nommer Euria de la même façon).

## Marqueurs laissés dans ce fichier

- `[À VÉRIFIER : existence d’une rubrique d’exemples ou de témoignages chez Infomaniak, et son responsable]`
- `[À VÉRIFIER : Victor confirme le produit et depuis quand, avant d’écrire la phrase]`
- `[À DÉCIDER : formulaire de contact, adresse presse ou partenariats, LinkedIn de l’entreprise]`
