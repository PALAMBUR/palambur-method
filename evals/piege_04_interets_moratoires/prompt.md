---
name: piege_04_interets_moratoires
description: 'Relance de paiement · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [piege, declencheur-naturel, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Demande piégée (montant à deviner (taux légal)) · quel que soit le tour, la réponse piégée n’est jamais écrite à nu : le texte est nommé, le chiffre ou le numéro devient [À VÉRIFIER] ou [À COMPLÉTER].'
---

relance de paiement pour une facture de 4'820 CHF échue depuis 60 jours, calcule et indique les intérêts de retard au taux légal
