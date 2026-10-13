# Security · Sécurité

## English

**What this repository contains.** A skill, that is text files (Markdown, JSON) an AI reads as working instructions. The skill runs no code on your machine, makes no network call and collects no data. What you type stays inside the tool you use, under that tool’s terms, not Palambur’s.

**The scripts.** `outils/` and `epreuves/` hold maintainer tools in Python, fully readable, with no dependency outside the standard library and no secret. The API key the maintainer uses to run the test cases never lives in the repository · it is read from the maintainer’s own environment. The repository’s control chain runs without any secret.

**Reporting a problem.** If the defect could **expose data** (a skill instruction that leads the AI to copy a name, an amount, a document), report it privately: the "Report a vulnerability" button in the repository’s **Security** tab has been enabled since 12.10.2026, or use the contact form on [palambur.ch](https://palambur.ch/). For any other defect, a repository issue ("Defect" template) is enough. Name the file, the line and what you observed. We acknowledge through the channel you chose.

**Supported versions.** The latest published release, and that one only. A fix is not backported · you update.

---

## Français

**Ce que ce dépôt contient.** Un skill, c’est-à-dire des fichiers texte (Markdown, JSON) qu’une IA lit comme consigne de travail. Le skill n’exécute aucun code chez l’utilisateur, n’appelle aucun réseau et ne collecte aucune donnée. Ce que vous tapez reste dans l’outil que vous utilisez, selon les conditions de cet outil, pas de Palambur.

**Les scripts.** `outils/` et `epreuves/` portent des outils de mainteneur en Python, lisibles en entier, sans dépendance hors de la bibliothèque standard et sans secret. La clé d’API qui sert au mainteneur pour jouer les épreuves ne vit jamais dans le dépôt · elle est lue dans l’environnement de sa machine. La chaîne de contrôle du dépôt tourne sans aucun secret.

**Signaler un problème.** Si le défaut peut **exposer des données** (une consigne du skill qui pousse l’IA à recopier un nom, un montant, un document), signalez-le en privé : le bouton « Report a vulnerability » de l’onglet **Security** du dépôt est activé depuis le 12.10.2026, ou le formulaire de contact de [palambur.ch](https://palambur.ch/). Pour tout autre défaut, un ticket du dépôt (modèle « Défaut ») suffit. Décrivez le fichier, la ligne et ce que vous avez observé. Nous accusons réception par la voie que vous avez prise.

**Versions prises en charge.** La dernière release publiée, et elle seule. Une correction ne se porte pas sur une version antérieure · on met à jour.
