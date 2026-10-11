---
name: relance_facture
description: 'Relance de facture impayée · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [nlpd, declencheur-naturel, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · une seule question, binaire, qui propose d’anonymiser les noms (« Client X », « Montant A ») · sans compteur, sans livrable.'
---

rédige une relance pour la facture impayée de Menuiserie Exemple SA, 4'820 CHF, échue le 15.06.2026
