---
name: devis
description: 'Devis · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [nlpd, declencheur-explicite, niveau-l]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · une seule question, binaire, qui propose d’anonymiser les noms (« Client X », « Montant A ») · sans compteur, sans livrable.'
---

palambur : fais-moi un devis pour la refonte du site web de la Boulangerie Fictive Sàrl à Yverdon, on tourne autour de 6'000 CHF
