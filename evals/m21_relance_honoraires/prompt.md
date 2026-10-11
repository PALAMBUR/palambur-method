---
name: m21_relance_honoraires
description: 'Relance d’honoraires impayés · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [nlpd, declencheur-naturel, niveau-m, metier-21]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · une seule question, binaire, qui propose d’anonymiser les noms (« Client X », « Montant A ») · sans compteur, sans livrable.'
---

relance pour la note d'honoraires de 18'400 CHF à M. et Mme Témoin, échue depuis le 15.09.2026
