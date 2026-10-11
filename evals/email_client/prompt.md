---
name: email_client
description: 'E-mail client · généré par epreuves/generer_evals.py depuis epreuves/cas.json, ne pas éditer à la main'
tags: [complet, declencheur-explicite, niveau-m]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: 'Un seul tour · le Gabarit rempli (INSTRUCTION, RÔLE ET AUDIENCE, DONNÉES, CONTRAINTES, FORMAT) puis le livrable · aucune question, aucun article de loi sans [À VÉRIFIER].'
---

méthode palambur : e-mail à un client pour confirmer que sa commande n° [À COMPLÉTER] part lundi 19.10.2026 par transporteur, livraison prévue le 21.10.2026. Pas de nom de client, vouvoiement, six lignes au maximum, signature « Votre équipe logistique ».
