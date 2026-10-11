# -*- coding: utf-8 -*-
"""Les chemins des générateurs de fiches métiers, tous résolus depuis `__file__`.

Pourquoi un module à part · le 11.10.2026, les six scripts vivaient dans un
scratchpad et portaient chacun des chemins absolus vers l’atelier. Un
générateur qu’on ne peut relancer n’est plus un générateur (CLAUDE.md § 2),
et le dépôt du skill sera cloné HORS de l’atelier Palambur · là, les sources
manquent, et le générateur doit le dire au lieu de planter.

Disposition attendue sur le disque ·

    Palambur/                                   ← l’atelier (ATELIER)
      0500_AGENTS_IA/
        0501_Prompts_Metiers/audit_typo.py      ← la règle typographique, IMPORTÉE
        05.02_Skill_Methode_Palambur/           ← ce dépôt (DEPOT)
          outils/metiers/                       ← ici (ICI)
          skills/palambur-method/metiers/       ← les 26 fiches produites (FICHES)
      0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv
      1300_PRODUITS_IA/05_CHAPTAL/outil_chaptal.html     ← `const ARBRE`
      1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl  ← les invites
"""
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(os.path.dirname(ICI))
ATELIER = os.path.normpath(os.path.join(DEPOT, '..', '..'))

CHAPTAL_HTML = os.path.join(ATELIER, '1300_PRODUITS_IA', '05_CHAPTAL', 'outil_chaptal.html')
PROMPTS_JSONL = os.path.join(ATELIER, '1300_PRODUITS_IA', '03_JACQUARD', 'corpus', 'prompts.jsonl')
ISCO_CSV = os.path.join(ATELIER, '0600_RESSOURCES', '06.12_Referentiels_Officiels',
                        'CH-ISCO-19_groupes_de_base.csv')
AUDIT_TYPO_DIR = os.path.join(ATELIER, '0500_AGENTS_IA', '0501_Prompts_Metiers')

#: brouillons que les scripts créent et consomment · ignoré par git (`.gitignore` de ce dossier)
CACHE = os.path.join(ICI, '_cache')
ARBRE_JSON = os.path.join(CACHE, 'arbre.json')

FICHES = os.path.join(DEPOT, 'skills', 'palambur-method', 'metiers')

#: code de sortie quand une source de l’atelier manque · distinct du 1 d’un vrai refus
SOURCE_ABSENTE = 2


def exiger(chemin, quoi):
    """Sort avec le code 2 et une phrase claire si une source de l’atelier manque."""
    if not os.path.exists(chemin):
        print('source Palambur absente, fiches non regénérables ici · %s attendu à %s'
              % (quoi, chemin), file=sys.stderr)
        sys.exit(SOURCE_ABSENTE)
    return chemin


def audit_typo():
    """Le module `audit_typo` de l’atelier, importé · jamais recopié (CLAUDE.md § 7)."""
    exiger(os.path.join(AUDIT_TYPO_DIR, 'audit_typo.py'), 'audit_typo.py')
    if AUDIT_TYPO_DIR not in sys.path:
        sys.path.insert(0, AUDIT_TYPO_DIR)
    import audit_typo as module
    return module
