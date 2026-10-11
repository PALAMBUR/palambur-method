---
name: m20_incident_livraison
description: 'Incident de livraison · réponse · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [nlpd, declencheur-naturel, niveau-m, metier-20]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · une seule question, binaire, qui propose d’anonymiser les noms (« Client X », « Montant A ») · sans compteur, sans livrable.'
---

réponse à Pharmacie Exemple SA dont le colis réfrigéré est arrivé à 12 degrés le 08.10.2026
