# Vidéo 60 secondes · « Quatre questions avant d’écrire » (point 23)

**Brouillon de scénario · 11.10.2026 · rien n’est animé, rien n’est rendu, rien n’est publié.** Format **9:16 · 1080 × 1920**, le format par défaut des pubs Palambur. **Une phrase par écran**, aucun sous-titre, au moins 5 secondes par écran dès qu’il y a du texte à lire (leçon de la pub Volney v2 du 02.10.2026). Le mot interdit par l’arbitrage du 07.10.2026 n’apparaît pas : on dit **écran**.

## Base visuelle

La base **claire** des quatre pubs d’outils validées le 03.10.2026 : fond `#F8FAFC` quadrillé, barre rouge signature, logo marine, carte de fin identique, couverture pleine tenue 1 seconde à l’écran 0 (règle commune `0900_HYPERFRAMES/_COUVERTURES_PUBS/couverture.py`). Musique **B**, retenue pour les quatre pubs le 02.10.2026. Le personnage, s’il en faut un, est **le portrait** (rond plein, buste blanc, sans visage) choisi le 07.10.2026 pour le film.

Les titres sont **coupés à la main par groupes de sens** : le signe `/` ci-dessous marque la fin d’une ligne. La taille se mesure dans la vraie police avant le rendu (`_source/verifier_titres.py` du film, à réutiliser), jamais par un compte de caractères.

Langue : **français** pour la première version (la série LinkedIn qui l’accompagne est en français). Les quatre pubs d’outils sont en anglais ; Victor décide si cette vidéo suit la même règle `[À DÉCIDER par Victor : FR ou EN]`.

## Le scénario

| Écran | Texte à l’écran | Voix | Durée |
|---|---|---|---|
| 0 | Couverture · **Quatre questions / avant d’écrire.** · logo | (silence, musique seule) | 1 s |
| 1 | « fais une offre d’emploi / pour un peintre à 80 % » (tapé dans une barre de saisie, curseur) | Neuf mots. C’est ce qu’on tape. | 5 s |
| 2 | Une IA répond en dix secondes. | Et une IA répond en dix secondes. | 4 s |
| 3 | Canton · Contrat · Date · Avantages · CCT (cinq mots qui s’affichent en rouge, un à un) | Elle a choisi toute seule le canton, le contrat, la date, les avantages, et une convention collective. | 7 s |
| 4 | **Tout est plausible, / rien n’est vérifié.** | Tout est plausible, rien n’est vérifié. | 5 s |
| 5 | La Méthode Palambur / inverse l’ordre. | La Méthode Palambur inverse l’ordre. | 4 s |
| 6 | **Question 1 sur 4** · Dans quel canton ? | Avant d’écrire, elle pose quatre questions. Une par message. | 5 s |
| 7 | **Question 2 sur 4** · Quelles missions ? | Avec un compteur, pour que vous sachiez quand ça finit. | 5 s |
| 8 | **Question 3 sur 4** · Quel profil ? | Chaque question a un défaut prudent si vous ne savez pas. | 5 s |
| 9 | **Question 4 sur 4** · Quels avantages ? | Et aucune ne peut être devinée. | 4 s |
| 10 | L’offre apparaît · deux lignes portent des crochets **[À COMPLÉTER]** surlignés en vert | Puis elle écrit. Ce qui manque reste écrit manquant, pour que vous le voyiez. | 6 s |
| 11 | Gratuit · Sans compte · Sans télémétrie | Le skill est gratuit, public, et rien de ce que vous tapez ne vient chez nous. | 5 s |
| 12 | Carte de fin · `github.com/PALAMBUR/palambur-method` · **L’IA sans jargon.** · logo | Installez-le. Palambur. | 4 s |

**Total : 1 + 5 + 4 + 7 + 5 + 4 + 5 + 5 + 5 + 4 + 6 + 5 + 4 = 60 secondes.** Addition vérifiée par script en fin de fichier.

## Notes de mise en scène

- **Écrans 6 à 9** · un même écran type, la carte de question glisse vers le haut et la suivante arrive ; le compteur reste à la même place, c’est lui qui donne le rythme. Pas de cascade, pas de rebond (retour « trop scolaire » du 31.08.2026).
- **Écran 3** · le rouge est réservé à ce que l’IA invente (sémantique de la charte : rouge = danger). **Écran 10** · le vert est réservé aux crochets, c’est-à-dire à ce que la Méthode a protégé (vert = avantage). Aucune autre couleur que la palette du kit.
- **Écran 10** · l’offre montrée est celle du post LinkedIn 1 et de la page `/methode/` : **le même exemple partout**, pour qu’on le reconnaisse d’un support à l’autre. Les crochets sont la démonstration, pas un oubli.
- **Écran 12** · la carte de fin reprend celle des quatre pubs (logo, slogan, adresse web palambur.ch). Le lien GitHub est le seul appel à l’action. Aucun prix, aucune mention de la formation à l’écran : la vidéo vend la Méthode, la page site fait le pont.
- **Voix** · ton posé, factuel, vouvoiement. La voix ne dit jamais plus que ce que l’écran montre.
- **Raccourci possible** · une version de 30 secondes se taille dans celle-ci en gardant les écrans 1, 3, 4, 6, 9, 10, 12 (fondu de 0,3 s entre deux écrans, jamais de coupe sèche : il n’existe aucun écran vide entre deux scènes) `[À DÉCIDER par Victor]`.

## Ce qui reste à faire, et par qui

1. **Victor** · valider le scénario, trancher la langue, donner le go d’animation. Rien ne s’anime avant.
2. **Fabrique** · `0900_HYPERFRAMES/`, nouveau projet `palambur-methode-pub-vertical/` sur le modèle des quatre pubs (`_source/build.py`, couverture commune, `STORYBOARD.md` fabriqué). Charger le skill d’animation HyperFrames avant d’écrire le moindre mouvement (règle du 31.08.2026).
3. **Mesure des titres** dans la vraie police avant le rendu.
4. **Publication** · calendrier éditorial d’abord, Metricool ensuite, go de Victor à chaque étape.

## Vérification de la durée

```bash
python3 -c "d=[1,5,4,7,5,4,5,5,5,4,6,5,4]; print(sum(d), 'secondes', '· OK' if sum(d)<=60 else '· TROP LONG')"
```
