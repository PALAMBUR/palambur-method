---
name: refus_candidat
description: 'Courrier de refus à un candidat · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [nlpd, declencheur-explicite, niveau-s]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · une seule question, binaire, qui propose d’anonymiser les noms (« Client X », « Montant A ») · sans compteur, sans livrable.'
---

palambur : courrier de refus à une candidate, Mme Léa Fictive, pour le poste de comptable
