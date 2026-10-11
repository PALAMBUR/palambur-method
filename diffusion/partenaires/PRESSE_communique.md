# Presse spécialisée romande · communiqué et angles par titre (point 70)

**Brouillon · rien n’est envoyé · go Victor.** Préparé le 11.10.2026. **Sans embargo, sans date de diffusion** : le communiqué part quand la version 1.0.0 est publique (étiquette et release, go Victor), pas avant. Aucune personne nommée : la citation est attribuée à une fonction. Aucun prix. Aucun chiffre sans date et source.

## Le communiqué · une page

> **COMMUNIQUÉ**
>
> **Une méthode suisse, publiée sous licence MIT, oblige l’IA à poser quatre questions avant d’écrire un document d’entreprise**
>
> *Neuchâtel* · Palambur publie la version 1.0.0 de la Méthode Palambur, un « skill » au standard ouvert qui s’installe dans les principaux assistants d’intelligence artificielle et change l’ordre des choses : l’assistant clarifie d’abord, puis rédige une seule fois, au lieu de produire tout de suite un texte plausible et d’inventer ce qu’on ne lui a pas dit.
>
> **Le problème.** Demandez à un modèle de langage « une offre d’emploi pour un peintre à 80 % » : il rend en dix secondes un canton, un type de contrat, une date d’entrée, des avantages, parfois une convention collective. Aucun de ces éléments n’était dans la demande ; tous se lisent comme vrais. Dans une entreprise où la personne qui rédige le contrat le signe souvent aussi, cette invention plausible est un risque qui ne se voit pas à la relecture.
>
> **La méthode.** Une fois installée, elle anticipe les quatre décisions que le modèle aurait prises seul et les pose à l’utilisateur, une par message, avec un compteur, des réponses par lettre et un défaut prudent. Elle rend ensuite deux textes : le prompt complet, réutilisable, et le document. Ce qui n’a pas été dit reste marqué « à compléter », entre crochets. Trois refus sont écrits dans la méthode : ne jamais inventer une référence légale, ne jamais combler un manque par une valeur plausible, ne jamais terminer un document par une liste d’hypothèses à valider.
>
> **Les données d’abord.** Si la demande contient le nom d’un client, un montant ou une adresse, la première question de l’assistant est celle de l’anonymisation, et le silence vaut oui. Les numéros de facture et les coordonnées bancaires ne sont jamais confiés au modèle.
>
> « Clarifier avant de produire, tout professionnel soigneux le fait. Nous l’avons écrit pour qu’une machine le fasse aussi, et nous l’avons publié pour que chacun puisse lire ce que l’assistant fait d’une demande avant de lui en confier une », déclare le fondateur de Palambur.
>
> **Gratuit, public, sans télémétrie.** La méthode est publiée sous licence MIT sur GitHub (github.com/PALAMBUR/palambur-method), avec ses épreuves et sa chaîne de contrôle. Elle n’envoie rien à Palambur, ne demande aucun compte et ne porte aucune publicité. Elle suit le standard ouvert des « Agent Skills » et se charge dans Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI et Mistral Vibe ; pour les assistants qui n’offrent qu’une boîte d’instructions, dont Euria d’Infomaniak, hébergé en Suisse, un texte à coller est fourni. Le skill existait sans numéro de version depuis le 12 juillet 2026 (journal des versions du dépôt) ; la version 1.0.0 lui donne une licence affichée, des épreuves et une chaîne de contrôle.
>
> **Démonstration.** Palambur propose aux rédactions une démonstration en direct, sur une demande choisie par le journaliste, en deux minutes.
>
> **À propos de Palambur.** Entreprise de conseil et de formation en intelligence artificielle à Neuchâtel, Palambur accompagne les entreprises de Suisse romande dans l’usage de l’IA sans jargon, avec l’hébergement suisse des données comme règle par défaut. palambur.ch
>
> **Contact presse** · Palambur · contact@palambur.ch · palambur.ch

**Règles du communiqué** : 450 mots au plus pour le corps ; une seule citation, attribuée à une fonction ; aucun chiffre de diffusion (les 2 étoiles et 1 fork du 11.10.2026, `mesures/releves.csv`, ne sont pas un argument de presse et ne figurent pas ici) ; aucune adresse postale.

## L’angle par titre

Les trois titres nommés par le plan, et ce qu’on a pu vérifier d’eux le 11.10.2026.

| Titre | État vérifié le 11.10.2026 | Lectorat | L’angle proposé | La première phrase du courriel d’accompagnement |
|---|---|---|---|---|
| **Bilan** | `bilan.ch` répond par une suite de redirections vers lui-même pour nos outils (trois fois HTTP 302), titre de page non lu ; déjà noté « à revérifier » dans `RELAIS_ROMANDS.md` `[À VÉRIFIER au navigateur avant envoi]` | dirigeants et cadres de Suisse romande | **La responsabilité de la direction.** Qui signe le contrat qu’une IA a complété ? La méthode comme réflexe de gouvernance : données clients jamais collées, références légales jamais inventées, un document qu’on peut signer. | « Vos lecteurs signent des documents qu’une IA a rédigés. Voici une méthode publiée pour qu’ils sachent ce qu’elle a inventé. » |
| **ICTjournal** | titre de page lu : « Accueil \| ICTjournal » ; déjà vérifié dans `RELAIS_ROMANDS.md` | décideurs informatiques | **Le standard ouvert et la vérifiabilité.** Un `SKILL.md` lu par six hôtes, une chaîne de contrôle publique qui refuse une version qui dérive, zéro télémétrie, et la question de l’hébergement (Euria d’Infomaniak comme hôte suisse). | « Un skill au standard Agent Skills, publié par une entreprise neuchâteloise, avec sa chaîne de contrôle en clair : de quoi lire ce que fait un agent avant de l’installer. » |
| **Le Temps** (rédaction et podcast « IA qu’à m’expliquer ») | titre de page lu : « Le Temps: actualités et informations en Suisse et dans le Monde » ; le podcast est vérifié dans `RELAIS_ROMANDS.md` | grand public éclairé | **Pourquoi l’IA invente, et comment on l’en empêche.** Le mécanisme (prédire le contenu du trou), l’exemple du peintre, la démonstration parlée en deux minutes (voir `PODCASTS_pitch.md`). | « Pourquoi une IA invente-t-elle un canton qu’on ne lui a pas donné ? Une méthode suisse répond en quatre questions, et se démontre à l’antenne. » |

Les deux-points du titre du Temps sont cités **comme donnée** (le site l’écrit ainsi), pas choisis.

## Ce qui part avec le communiqué

- Le lien du dépôt et le lien de la page `palambur.ch/methode/`.
- **Une capture** de l’échange avant/après (la demande du peintre, la Question 1 sur 4, le livrable avec ses crochets), fabriquée par la session Site ou Branding au gabarit maison `[À COMPLÉTER : la capture n’existe pas au 11.10.2026]`.
- Aucune pièce jointe lourde, aucun dossier de presse.

## Ce qui exige Victor

- Le **go**, après la publication de la version 1.0.0 ; jamais avant.
- La **fonction** à laquelle attribuer la citation (ce brouillon écrit « le fondateur de Palambur »), et la signature du courriel.
- L’ordre : `RELAIS_ROMANDS.md` propose les médias **quand il existe au moins un atelier tenu à raconter**. Ce communiqué peut partir avant, sur la seule version 1.0.0 ; c’est un arbitrage.

## Marqueurs laissés dans ce fichier

- `[À VÉRIFIER au navigateur avant envoi]` · identité et contact de Bilan.
- `[À COMPLÉTER : la capture n’existe pas au 11.10.2026]` · le visuel avant/après.
