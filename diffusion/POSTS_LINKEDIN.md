# Série LinkedIn · « Un livrable par semaine » (point 22)

**Brouillons · rien dans Metricool · le calendrier éditorial et Victor décident.**

Écrit le 11.10.2026 par la session Skills et Prompt Ingénierie. Quatre posts, un par semaine, chacun montre **un livrable** : la demande brute, les quatre questions, le résultat, l’appel « installez-le ». Limite LinkedIn de 3'000 caractères respectée et mesurée (`wc -m` sur chaque bloc, relevé en fin de fichier). Aucun créneau horaire n’est proposé ici : **le créneau est attribué par `_KIT/build_calendar.py`** (T, T2, T3 LinkedIn, écart de 60 minutes, au plus deux publications par réseau et par jour), jamais à la main.

Les marqueurs `[À COMPLÉTER]` **dans les livrables montrés sont voulus** : ils sont la démonstration. Aucun marqueur ne subsiste dans le texte du post lui-même.

## Règles appliquées

- Jamais le sigle interdit par la règle de marque du 04.08.2026 · on écrit « entreprises ». Vérifié par `grep`.
- Zéro tiret de ponctuation, séparateur « · », apostrophe courbe. Vérifié par `audit_typo.py`.
- Aucun prix Palambur. Le skill est gratuit, et c’est la seule mention d’argent.
- Aucun chiffre sans date ni source. Le seul chiffre du dépôt cité est le nombre d’étoiles, relevé le 11.10.2026.
- Pas d’article de loi numéroté : on nomme la loi (LEg, nLPD, CO), jamais l’article.
- Chaque livrable est **différent du précédent** dans sa forme et dans son visuel (règle de la série de juillet 2026).

## Visuel commun · gabarit maison

Kit : `0300_STRATEGIE_COMMERCIALE/03.05_Publications/_KIT/` (lu, rien n’y a été écrit). Format **carrousel 1080 × 1350** exporté en PDF pour LinkedIn par `export.sh`, feuille `palambur-social.css`, palette stricte `#0A192F` navy · `#F8FAFC` off-white · `#E53935` rouge (danger, ici « ce que l’IA aurait inventé ») · `#059669` vert (avantage, ici « ce que la Méthode a demandé »), logos `assets/logo-white.png` et `logo-navy.png` selon le fond, pied `palambur.ch` en minuscules. Appel final sur la **slide CTA** du kit (filet rouge, titre off-white, pilule blanche à texte navy), jamais de rectangle navy plein.

Structure commune des carrousels, **cinq slides** : 1 · la demande brute telle qu’on la tape · 2 · « ce qu’une IA invente » (quatre lignes rouges) · 3 · les quatre questions avec compteur · 4 · un extrait du livrable avec ses crochets · 5 · CTA « Installez la Méthode · gratuit · github.com/PALAMBUR/palambur-method ». La variation d’un post à l’autre est notée sous chaque post.

---

## Post 1 · Offre d’emploi

```
« Fais une offre d’emploi pour un peintre à 80 %. »

Neuf mots. Une IA répond en dix secondes. Et elle choisit toute seule le canton, le type de contrat, la date d’entrée, les avantages, parfois une convention collective.

Tout est plausible. Rien n’est vérifié. Et le plausible ne se voit pas à la relecture, justement parce qu’il est plausible.

La Méthode Palambur inverse l’ordre. Avant la première ligne, l’outil pose quatre questions, une par message, avec un compteur :

Question 1 sur 4 · Dans quel canton le poste est-il basé ?
A. Neuchâtel
B. Vaud
C. Genève
D. Autre / je ne sais pas (défaut : Suisse romande, sans canton nommé)
Question 2 sur 4 · Quelles sont les trois à cinq missions principales ?
Question 3 sur 4 · Quel profil : CFC exigé, expérience, permis ?
Question 4 sur 4 · Quels avantages peut-on annoncer ?

Chaque question a un défaut prudent si vous ne savez pas. Aucune ne peut être devinée : le canton change le salaire de référence, les missions changent le texte, le profil change le filtre, les avantages changent le taux de réponse.

Puis l’outil rend deux choses. Le prompt complet, en cinq blocs, que vous gardez. Et l’offre, prête à relire :

« Peintre en bâtiment CFC · 80 % · [Canton] · entrée à convenir.
Profil : CFC de peintre ou titre jugé équivalent, trois ans d’expérience en rénovation, permis [À COMPLÉTER : exigé ou souhaité].
Ce que nous offrons : [À COMPLÉTER : avantages confirmés par l’employeur].
Poste ouvert à toutes et à tous. Vos données sont traitées en Suisse, conformément à la nLPD. »

Les crochets ne sont pas un oubli. C’est ce qui manque, écrit manquant, pour que vous le voyiez. Aucune convention collective n’est citée tant qu’elle n’est pas confirmée. La formulation est neutre de genre, parce que la LEg s’applique dans les contraintes, pas à la relecture.

Le skill est publié sur GitHub, sous licence MIT. Gratuit, sans compte, sans télémétrie : rien de ce que vous tapez ne vient chez nous.

Installez-le dans Claude Code :
/plugin marketplace add PALAMBUR/palambur-method

/plugin install palambur@palambur

Il existe aussi pour ChatGPT, Codex, Gemini, Mistral et Euria d’Infomaniak. Le guide est dans le dépôt.

Semaine prochaine : la relance de facture, et la question qu’il faut poser avant toutes les autres.

#IA #Recrutement #EntreprisesSuisses #SuisseRomande #ClaudeCode #Palambur
```

**Visuel** · carrousel 5 slides, fond navy. Slide 1 : la demande en Space Grotesk, grande, seule. Slide 2 : quatre lignes rouges « Canton : inventé · Contrat : inventé · Date : inventée · CCT : inventée ». Slide 3 : les quatre questions en cartes, compteur en petites capitales vertes. Slide 4 : l’extrait d’offre, crochets surlignés. Slide 5 : CTA.

---

## Post 2 · Relance de facture

```
« Rédige une relance pour la facture impayée de Menuiserie Exemple SA, 4'820 CHF, échue depuis le 15 juin. »

Avant de parler de ton ou de délai, il y a une question qui passe devant toutes les autres.

Vous venez de coller un nom de client et un montant dans une IA.

La Méthode Palambur commence donc par ceci, et par ceci seulement :

« Je détecte des données nominatives. Par défaut, je les anonymise partout (« Client X », « Montant A ») et j’ajoute une mention nLPD. Souhaitez-vous plutôt les conserver telles quelles ? »

Une question, binaire, seule dans son message. Si vous ne répondez pas, l’outil anonymise. Pas d’hybride : jamais un vrai nom dans le prompt et un pseudonyme dans la lettre.

Ensuite seulement, le lot métier. Ici deux questions suffisent, et l’outil le dit :

Question 1 sur 2 · Quel ton : premier rappel courtois, ou relance ferme avant mise en demeure ?
Question 2 sur 2 · Quel délai de paiement accordez-vous dans ce courrier ?

Le numéro de facture et l’IBAN ne sont pas des questions. Ce sont des champs. Ils arrivent dans la lettre sous forme de crochets, vous les remplissez vous-même, l’IA ne les a jamais vus.

Extrait du résultat, version anonymisée :

« Objet : facture [n° de facture] échue le 15 juin · Montant A

Madame, Monsieur,
Sauf erreur de notre part, la facture mentionnée en objet reste ouverte à ce jour. Nous vous remercions de régler le montant de [Montant A] d’ici au [délai choisi] sur le compte [IBAN].
Si le paiement a déjà été effectué, nous vous prions de ne pas tenir compte de ce rappel.

Vos données sont traitées en Suisse, conformément à la nLPD. »

Courtois, gradué, jamais accusatoire : c’est le ton que la Méthode impose à toute relance, parce qu’un client qui paie en retard reste un client.

Le skill est public sur GitHub, licence MIT, gratuit, sans compte. Il ne transmet rien à Palambur.

Installez-le dans Claude Code :
/plugin marketplace add PALAMBUR/palambur-method

/plugin install palambur@palambur

Le guide pour ChatGPT, Codex, Gemini, Mistral et Euria d’Infomaniak est dans le dépôt.

Semaine prochaine : le certificat de travail, le document où une phrase de trop coûte cher.

#IA #ProtectionDesDonnees #nLPD #EntreprisesSuisses #SuisseRomande #Palambur
```

**Visuel** · carrousel 5 slides, fond off-white (inversion du post 1, logo navy). Slide 1 : la demande avec le nom et le montant **caviardés en rouge** à l’écran. Slide 2 : la question binaire seule, encadrée du filet rouge. Slide 3 : les deux questions métier, compteur « 1 sur 2 · 2 sur 2 » en vert. Slide 4 : la lettre anonymisée, crochets surlignés. Slide 5 : CTA.

---

## Post 3 · Certificat de travail

```
« Écris un certificat de travail pour un collaborateur qui part. »

C’est le document RH où une phrase de trop se paie, parfois des années plus tard. En Suisse, le certificat de travail doit être à la fois véridique et bienveillant, et le Code des obligations encadre ce que l’employeur doit y dire.

Une IA qui n’a rien demandé va inventer la fonction, la durée, les qualités, et glisser une formule codée qu’un recruteur lira comme un signal.

La Méthode Palambur pose d’abord ses questions. Le certificat porte un nom : la question d’anonymisation passe donc en premier, seule. Puis quatre questions, une par message :

Question 1 sur 4 · Quelle fonction, quel taux, quelles dates d’entrée et de sortie ?
Question 2 sur 4 · Certificat complet (prestations et conduite) ou simple attestation de travail ?
Question 3 sur 4 · Quelles tâches et responsabilités principales ?
Question 4 sur 4 · Qui est à l’origine du départ, et le mentionne-t-on ?

Rien de tout cela ne se devine. Et la Méthode interdit deux choses : inventer une appréciation que vous n’avez pas donnée, et citer un article de loi sans le marquer à vérifier.

Extrait, version anonymisée :

« Certificat de travail

Collaborateur A a travaillé au sein de notre entreprise du [date d’entrée] au [date de sortie] en qualité de [fonction], à un taux de [taux].
Ses tâches principales comprenaient [tâches confirmées par l’employeur].
[Appréciation des prestations et de la conduite : À COMPLÉTER par la personne responsable. Aucune formule n’est proposée par défaut.]
Nous le remercions pour sa collaboration et lui souhaitons plein succès pour la suite de son parcours. »

Le bloc appréciation reste vide, volontairement. Ce n’est pas à une IA de qualifier le travail d’une personne qu’elle n’a jamais vue. Le livrable porte la mention : relecture obligatoire par une personne responsable.

Le skill est publié sur GitHub, licence MIT, gratuit, sans compte, sans télémétrie.

Installez-le dans Claude Code :
/plugin marketplace add PALAMBUR/palambur-method

/plugin install palambur@palambur

Il existe aussi pour ChatGPT, Codex, Gemini, Mistral et Euria d’Infomaniak.

Semaine prochaine : le devis, et pourquoi le périmètre exclu compte autant que le périmètre inclus.

#IA #RessourcesHumaines #CertificatDeTravail #EntreprisesSuisses #SuisseRomande #Palambur
```

**Visuel** · carrousel 5 slides, fond navy, **mise en page « document »** : la slide 4 montre une feuille A4 posée en biais, le bloc appréciation laissé blanc avec un filet rouge « rien ici n’est inventé ». Slide 2 : une seule phrase rouge « Une formule codée, et le certificat devient un piège ». Slide 5 : CTA.

---

## Post 4 · Devis

```
« Fais-moi un devis pour la rénovation d’une cuisine. »

Le devis est le livrable où l’on perd de l’argent deux fois : une fois en oubliant ce qui est inclus, une fois en oubliant de dire ce qui ne l’est pas.

Une IA qui n’a rien demandé va écrire un devis parfaitement présenté, avec des postes qu’elle a choisis, des délais qu’elle a choisis, et des conditions de paiement qu’elle a choisies. Vous signez le sien, pas le vôtre.

La Méthode Palambur pose d’abord quatre questions, une par message, avec un compteur :

Question 1 sur 4 · Quel périmètre est inclus, et surtout qu’est-ce qui est exclu (électricité, plomberie, évacuation) ?
Question 2 sur 4 · Quels postes et quelles quantités, ou souhaitez-vous un forfait ?
Question 3 sur 4 · Quelle validité du devis, et quelles conditions de paiement (acompte, solde) ?
Question 4 sur 4 · Quel délai d’exécution annoncez-vous ?

Les prix ne sont pas une question. Ils sont des champs : l’IA ne fixe jamais un montant à votre place.

Extrait du résultat :

« Devis n° [À COMPLÉTER] · valable jusqu’au [date]

Objet : rénovation de cuisine, [adresse du chantier]

Inclus : dépose de l’existant, fourniture et pose du mobilier selon plan joint, plan de travail [matière], raccordements sanitaires sur attentes existantes.
Exclu : travaux d’électricité, modification des évacuations, peinture des murs.

Postes : [liste des postes et quantités]. Montant : [À COMPLÉTER] CHF.
Conditions : acompte de [À COMPLÉTER] % à la commande, solde à la réception. Délai d’exécution : [délai].

Vos données sont traitées en Suisse, conformément à la nLPD. »

La ligne « Exclu » est celle qui évite le litige. C’est aussi celle qu’une IA laissée seule n’écrit jamais, parce que personne ne lui a dit ce qu’elle devait laisser dehors.

Le skill est public sur GitHub, licence MIT. Gratuit, sans compte, sans télémétrie. Il a deux étoiles au 11 octobre 2026, dont la nôtre : il est jeune, il est honnête, et chaque gabarit de livrable contribué l’améliore.

Installez-le dans Claude Code :
/plugin marketplace add PALAMBUR/palambur-method

/plugin install palambur@palambur

Guide pour ChatGPT, Codex, Gemini, Mistral et Euria d’Infomaniak dans le dépôt. Et si vous voulez aller plus loin métier par métier, la bibliothèque Chaptal et la formation sont sur palambur.ch.

#IA #Devis #Artisans #EntreprisesSuisses #SuisseRomande #Palambur
```

**Visuel** · carrousel 5 slides, fond off-white, **mise en page « deux colonnes »** : slide 2 une colonne rouge « Inclus (choisi par l’IA) » face à une colonne vide « Exclu : rien », slide 4 les deux colonnes remplies avec la ligne « Exclu » en vert. Slide 5 : CTA, avec en plus la pilule « Chaptal · métier par métier ».

---

## Ordre et dépendances

| Semaine | Post | Préalable |
|---|---|---|
| 1 | Offre d’emploi | page `/methode/` complétée (point 21) ou, à défaut, lien direct vers le dépôt |
| 2 | Relance de facture | aucun |
| 3 | Certificat de travail | aucun |
| 4 | Devis | relevé des étoiles **le jour de la publication** · le chiffre « deux étoiles au 11 octobre 2026 » se remplace par le relevé du jour (`outils/mesure.py`), sinon la phrase entière se retire |

Les posts renvoient l’un vers l’autre (« Semaine prochaine : … ») : si le calendrier change l’ordre, ces phrases de clôture se réécrivent.

## Ce qui exige Victor

- **Go de publication**, post par post, après relecture dans le calendrier éditorial (`Calendrier-Editorial-Palambur.html`) puis pose en brouillon dans Metricool.
- **Choix du visuel** : carrousel PDF (proposé ici) ou image unique.
- **Les textes alternatifs** des visuels s’écrivent à la pose, pas ici.

## Mesures

Relevé `wc -m` de chaque bloc de post (texte seul, sans les clôtures de code), à rejouer avant toute pose : voir la sortie reproduite dans le rapport de session du 11.10.2026. Limite : 3'000.
