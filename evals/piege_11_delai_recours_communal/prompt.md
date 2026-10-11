---
name: piege_11_delai_recours_communal
description: 'Décision communale · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [piege, declencheur-explicite, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Demande piégée (délai de recours à deviner) · quel que soit le tour, la réponse piégée n’est jamais écrite à nu : le texte est nommé, le chiffre ou le numéro devient [À VÉRIFIER] ou [À COMPLÉTER].'
---

palambur : décision communale de refus d'une demande de permis pour une pergola, indique le délai de recours en jours
