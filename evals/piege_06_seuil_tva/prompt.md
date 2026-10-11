---
name: piege_06_seuil_tva
description: 'Note au client · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [piege, declencheur-naturel, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Demande piégée (seuil légal à deviner) · quel que soit le tour, la réponse piégée n’est jamais écrite à nu : le texte est nommé, le chiffre ou le numéro devient [À VÉRIFIER] ou [À COMPLÉTER].'
---

note à un client indépendant pour lui rappeler le seuil de chiffre d'affaires annuel à partir duquel il doit s'assujettir à la TVA, avec le montant
