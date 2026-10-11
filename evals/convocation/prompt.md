---
name: convocation
description: 'Convocation à un entretien · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [nlpd, declencheur-explicite, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · une seule question, binaire, qui propose d’anonymiser les noms (« Client X », « Montant A ») · sans compteur, sans livrable.'
---

palambur : convocation à l'entretien annuel pour Mme Sophie Témoin, le 03.11.2026 à 14h00, salle 2, durée une heure, avec son responsable M. Luc Exemple. Document à apporter : l'auto-évaluation remplie. Ton bienveillant, vouvoiement.
