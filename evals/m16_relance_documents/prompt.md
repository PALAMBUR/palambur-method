---
name: m16_relance_documents
description: 'Relance des documents fiscaux · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [nlpd, declencheur-naturel, niveau-s, metier-16]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · une seule question, binaire, qui propose d’anonymiser les noms (« Client X », « Montant A ») · sans compteur, sans livrable.'
---

relance à M. Hugo Témoin, indépendant, qui n'a toujours pas envoyé ses pièces pour la déclaration 2025
