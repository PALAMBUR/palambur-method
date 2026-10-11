---
name: montant_sans_nom
description: 'Relance de facture impayée (sans nom) · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [clarification, declencheur-naturel, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Premier tour · « Question 1 sur 3 » (au plus 4), une seule question, choix A à D, échappatoire « Autre / je ne sais pas » · sans livrable.'
---

rédige une relance pour une facture de 2'350 CHF échue le 30.09.2026, le client n'a pas réagi au premier rappel
