# Questions fréquentes · Frequently asked questions

*Français d’abord, English below.*

---

## Français

### Comment le skill se déclenche-t-il ?

Par l’une de trois portes. **Le mot** : votre message contient « palambur », « méthode palambur » ou « palambur method ». **La nature de la demande** : un document de travail demandé en une ou deux phrases (offre d’emploi, devis, relance, contrat, note interne), un contexte d’entreprise suisse, des noms ou des montants à protéger, ou un texte joint à relire. **L’option « toujours actif »** : vous écrivez « Méthode Palambur toujours active » dans la conversation ou dans votre `CLAUDE.md`, et le skill s’applique à tout ce que l’IA rédige, jusqu’à « Méthode Palambur désactivée ».

### Pourquoi me pose-t-il des questions au lieu de répondre ?

Parce qu’une demande d’une ligne ne contient pas ce qu’il faut pour écrire un document que vous pouvez envoyer. Sans question, l’IA devine : canton, missions, délai, montant. Le skill repère les éléments dont l’absence l’obligerait à inventer, et ne demande que ceux-là. Quatre questions au plus par lot, une par message, avec un compteur. Si tout est déjà dans votre demande, il ne demande rien et produit directement.

### Puis-je ne pas répondre ?

Oui. Chaque question propose un **défaut prudent**, marqué « · défaut si vous ne précisez pas ». Si vous passez, il s’applique. Si vous choisissez « Autre / je ne sais pas », le champ reste `[À COMPLÉTER]` dans le document, visible, à remplir par vous.

### Que devient ce que je tape ? Mes données partent-elles quelque part ?

Le skill n’envoie rien, nulle part. Il n’a pas de serveur, pas de compte, pas de télémétrie. Ce sont des fichiers texte que votre IA lit. **Vos données vont là où va votre IA**, et seulement là : si vous utilisez un hôte dont les serveurs sont hors de Suisse, c’est l’hôte qui les traite, pas le skill. C’est pour cela que le skill demande d’abord, dès qu’il voit un nom ou un montant, s’il doit anonymiser. Par défaut, il anonymise : « Client X », « Collaborateur·trice A ». Vous remettez les noms chez vous, dans le document final.

### Qu’est-ce que la question « données nominatives » du début ?

C’est l’Étape 0. Dès que votre demande porte un nom de personne, de client, un salaire ou un montant lié à quelqu’un, le skill pose une seule question binaire : anonymiser partout (défaut) ou conserver tel quel. Elle vient avant toute autre question et n’entre pas dans le compteur. Si vous conservez, il le fait ; il ne discute pas votre choix.

### Combien ça coûte ?

Rien. Le skill est gratuit, sous licence MIT, et le restera : la méthode, les gabarits, les fiches métier, les épreuves, et chaque version qui suivra. Ce que Palambur vend par ailleurs (une version pré-réglée pour une entreprise, une installation accompagnée) ajoute du service autour du skill ; rien de ce qui est dans le dépôt ne devient payant. Les livrables ne portent aucune mention Palambur.

### En quoi est-ce différent d’un bon prompt que j’écrirais moi-même ?

Un bon prompt, vous l’écrivez une fois, un jour où vous avez le temps. Le skill l’écrit à chaque demande, de la même façon, et vous le rend : c’est le **Gabarit Palambur rempli**, cinq blocs ordonnés (Instruction · Rôle et audience · Données · Contraintes · Format), que vous gardez et réutilisez. Il porte aussi ce qu’un prompt écrit à la main oublie le lundi matin : la mention nLPD, l’interdiction d’inventer, les textes de loi nommés sans numéro d’article, la neutralité de genre pour une offre d’emploi. La différence n’est pas dans un prompt ; elle est dans le fait que le centième ressemble au premier.

### Pourquoi deux parties dans la réponse ?

D’abord le Gabarit rempli, puis le livrable. Le livrable est ce que vous envoyez. Le Gabarit est ce que vous gardez : il dit exactement ce qui a été demandé à l’IA, et il se rejoue la semaine suivante avec d’autres données. Si le livrable vous déçoit, c’est le Gabarit que vous corrigez, pas le livrable.

### Que signifient `[À COMPLÉTER]`, `[À VÉRIFIER]` et les autres marqueurs ?

`[À COMPLÉTER]` : une information que vous seul avez (une date, un montant, un nom). `[À VÉRIFIER : base légale]` : le skill a nommé un texte de loi, mais ne cite jamais un numéro d’article de mémoire ; quelqu’un doit vérifier avant envoi. `[À VÉRIFIER : CCT applicable]`, `[À VÉRIFIER : taux applicable]` : même règle pour une convention collective ou un taux. `[À ARBITRER]` : un choix qui vous revient (un ton, un délai). `[À CONFIRMER]` : un fait que le skill a déduit sans pouvoir l’établir. Un marqueur qui reste dans un document envoyé est une faute ; un marqueur qui reste dans un brouillon est le skill qui fait son travail.

### Sur quels outils d’IA fonctionne-t-il ?

Le format `SKILL.md` est un standard ouvert. Dossier de skill posé directement : Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, Mistral Vibe CLI. Téléversement du skill : Gemini (application), Mistral Vibe Work. Boîte d’instructions seule : Projet Claude.ai, Euria d’Infomaniak, GPT personnalisé de ChatGPT, avec le prompt système condensé du dossier `adaptations/`. Le guide hôte par hôte est dans `portabilite/INSTALLATION.md`.

### Et si mon hôte n’offre qu’une boîte d’instructions ?

Le dossier `adaptations/` contient la méthode condensée en un prompt système autonome, en deux tailles, généré depuis le skill lui-même. Vous le collez. Les gabarits détaillés ne suivent pas ; le déroulé, les questions, les marqueurs et les garde-fous, oui.

### Le skill connaît-il le droit suisse ?

Il connaît les **noms** des textes (CO, LTr, LEg, nLPD, LCD, LP, LTVA, CC, SIA, AIMP, CCT, RGPD) et sait quand les nommer. Il ne cite jamais un numéro d’article, un délai légal ou un taux sans `[À VÉRIFIER]`. Ce n’est pas une faiblesse : un numéro d’article cité de mémoire par une IA est faux assez souvent pour qu’on ne lui fasse jamais confiance. Le skill ne remplace ni un juriste, ni une fiduciaire.

### Fonctionne-t-il en allemand, en italien, en anglais ?

Les fichiers du skill sont écrits en français. Les questions et le livrable suivent la langue de votre demande. Le `README` existe en français, en anglais, en allemand et en italien ; les versions allemande et italienne attendent une relecture par un locuteur natif.

### Puis-je lui faire relire un texte déjà écrit ?

Oui, c’est le mode relecture (Étape 4). Vous joignez le texte et demandez de le relire : aucune question, un tableau « Constat · Risque · Correction proposée », puis la version corrigée. La relecture corrige la forme, le droit et les données ; elle ne réécrit pas le fond.

### Où sont les exemples complets ?

Dans [`exemples/`](../exemples/) : dix demandes, une par gabarit, avec les questions posées, le Gabarit rempli et le livrable, sur des données fictives.

### Comment contribuer ou signaler un défaut ?

Lisez [`CONTRIBUTING.md`](../CONTRIBUTING.md). Trois façons : signaler un défaut, proposer un gabarit de livrable, corriger une référence juridique. Le [code de conduite](../CODE_OF_CONDUCT.md) s’applique.

---

## English

### How does the skill trigger?

Through one of three doors. **The word**: your message contains “palambur”, “méthode palambur” or “palambur method”. **The nature of the request**: a working document asked for in one or two sentences (job advert, quote, payment reminder, contract, internal memo), a Swiss business context, names or amounts to protect, or an attached text to review. **The “always on” option**: write “Méthode Palambur toujours active” in the conversation or in your `CLAUDE.md`, and the skill applies to everything the AI writes until “Méthode Palambur désactivée”.

### Why does it ask me questions instead of answering?

Because a one line request does not contain what is needed to write a document you can send. Without questions, the AI guesses: canton, duties, deadline, amount. The skill identifies the elements whose absence would force it to invent, and asks only for those. Four questions at most per batch, one per message, with a counter. If everything is already in your request, it asks nothing and produces directly.

### Can I skip a question?

Yes. Each question offers a **cautious default**, marked as the default if you do not specify. If you skip, it applies. If you choose “Other / I don’t know”, the field stays `[À COMPLÉTER]` (to be completed) in the document, visible, for you to fill in.

### What happens to what I type? Does my data go anywhere?

The skill sends nothing anywhere. It has no server, no account, no telemetry. It is a set of text files your AI reads. **Your data goes where your AI goes**, and only there: if you use a host whose servers are outside Switzerland, the host processes it, not the skill. That is why the skill first asks, as soon as it sees a name or an amount, whether it should anonymise. By default it does: “Client X”, “Employee A”. You put the names back on your side, in the final document.

### What is the “personal data” question at the start?

That is Step 0. As soon as your request carries a person’s or client’s name, a salary or an amount linked to someone, the skill asks a single binary question: anonymise everywhere (default) or keep as is. It comes before any other question and is not counted. If you keep, it keeps; it does not argue with your choice.

### How much does it cost?

Nothing. The skill is free, under the MIT licence, and will stay free: the method, the templates, the trade sheets, the test cases, and every version to come. What Palambur sells separately (a version pre configured for a company, an accompanied installation) adds service around the skill; nothing in the repository becomes paid. Deliverables carry no Palambur mention.

### How is this different from a good prompt I would write myself?

A good prompt is written once, on a day you have time. The skill writes it on every request, the same way, and hands it back to you: the **completed Palambur Template**, five ordered blocks (Instruction · Role and audience · Data · Constraints · Format), which you keep and reuse. It also carries what a hand written prompt forgets on a Monday morning: the data protection notice, the ban on inventing, legal texts named without article numbers, gender neutral wording for a job advert. The difference is not in one prompt; it is in the hundredth one looking like the first.

### Why two parts in the answer?

First the completed Template, then the deliverable. The deliverable is what you send. The Template is what you keep: it says exactly what was asked of the AI, and it can be replayed the following week with other data. If the deliverable disappoints you, you fix the Template, not the deliverable.

### What do `[À COMPLÉTER]`, `[À VÉRIFIER]` and the other markers mean?

`[À COMPLÉTER]` (to be completed): information only you have (a date, an amount, a name). `[À VÉRIFIER : base légale]` (to be checked: legal basis): the skill named a legal text but never quotes an article number from memory; someone must check before sending. `[À VÉRIFIER : CCT applicable]`, `[À VÉRIFIER : taux applicable]`: same rule for a collective agreement or a rate. `[À ARBITRER]` (to be decided): a choice that is yours (a tone, a deadline). `[À CONFIRMER]` (to be confirmed): a fact the skill inferred without being able to establish it. A marker left in a sent document is a mistake; a marker left in a draft is the skill doing its job.

### Which AI tools does it work with?

The `SKILL.md` format is an open standard. Skill folder placed directly: Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, Mistral Vibe CLI. Skill upload: Gemini (app), Mistral Vibe Work. Instructions box only: Claude.ai Project, Infomaniak Euria, ChatGPT custom GPT, using the condensed system prompt from the `adaptations/` folder. The host by host guide is in `portabilite/INSTALLATION.md`.

### What if my host only offers an instructions box?

The `adaptations/` folder holds the method condensed into a standalone system prompt, in two sizes, generated from the skill itself. You paste it. The detailed templates do not follow; the flow, the questions, the markers and the safeguards do.

### Does the skill know Swiss law?

It knows the **names** of the texts (CO, LTr, LEg, nLPD, LCD, LP, LTVA, CC, SIA, AIMP, CCT, GDPR) and when to name them. It never quotes an article number, a legal deadline or a rate without `[À VÉRIFIER]`. This is not a weakness: an article number quoted from memory by an AI is wrong often enough that it should never be trusted. The skill replaces neither a lawyer nor an accountant.

### Does it work in German, Italian, English?

The skill files are written in French. The questions and the deliverable follow the language of your request. The `README` exists in French, English, German and Italian; the German and Italian versions await proofreading by a native speaker.

### Can it review a text I have already written?

Yes, that is the review mode (Step 4). You attach the text and ask for a review: no questions, a table “Finding · Risk · Proposed correction”, then the corrected version. The review corrects form, law and data; it does not rewrite the substance.

### Where are the full examples?

In [`exemples/`](../exemples/): ten requests, one per template, with the questions asked, the completed Template and the deliverable, on fictional data.

### How do I contribute or report a defect?

Read [`CONTRIBUTING.md`](../CONTRIBUTING.md). Three ways: report a defect, propose a deliverable template, correct a legal reference. The [code of conduct](../CODE_OF_CONDUCT.md) applies.
