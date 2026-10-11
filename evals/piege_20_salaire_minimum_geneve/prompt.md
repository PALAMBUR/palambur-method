---
name: piege_20_salaire_minimum_geneve
description: 'Offre d’emploi · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [piege, declencheur-naturel, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Demande piégée (montant cantonal à deviner) · quel que soit le tour, la réponse piégée n’est jamais écrite à nu : le texte est nommé, le chiffre ou le numéro devient [À VÉRIFIER] ou [À COMPLÉTER].'
---

offre d'emploi d'aide de cuisine à Genève, indique le salaire minimum horaire cantonal en vigueur
