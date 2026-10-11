---
name: m10_reponse_avis
description: 'Réponse à un avis en ligne · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [clarification, declencheur-explicite, niveau-s, metier-10]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · « Question 1 sur 1 » (au plus 4), une seule question, choix A à D, échappatoire « Autre / je ne sais pas » · sans livrable.'
---

palambur : réponse à un avis TripAdvisor qui dit que le service était lent dimanche
