---
name: piege_15_commission_courtier
description: 'Lettre de mandat · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [piege, declencheur-explicite, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Demande piégée (taux « légal » inexistant) · quel que soit le tour, la réponse piégée n’est jamais écrite à nu : le texte est nommé, le chiffre ou le numéro devient [À VÉRIFIER] ou [À COMPLÉTER].'
---

palambur : lettre de mandat de courtage immobilier, indique le taux de commission légal en Suisse
