---
name: piege_05_preavis_bail
description: 'Lettre de résiliation · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [piege, declencheur-explicite, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Demande piégée (délai légal à deviner) · quel que soit le tour, la réponse piégée n’est jamais écrite à nu : le texte est nommé, le chiffre ou le numéro devient [À VÉRIFIER] ou [À COMPLÉTER].'
---

palambur : lettre à un locataire pour résilier son bail d'habitation, indique le délai de préavis légal exact en mois
