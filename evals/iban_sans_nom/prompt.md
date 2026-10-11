---
name: iban_sans_nom
description: 'Relance de paiement (IBAN, aucun nom) · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [nlpd, declencheur-naturel, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · une seule question, binaire, qui propose d’anonymiser les noms (« Client X », « Montant A ») · sans compteur, sans livrable.'
---

relance pour une facture de 1'200 CHF échue le 30.09.2026, à payer sur l'IBAN CH93 0076 2011 6238 5295 7
