# -*- coding: utf-8 -*-
"""Vérification double des fiches métiers · structure, comptes ARBRE vs fiche, lois attestées et
recomptées par un second chemin, « P·ME », `art. N`, typographie, mention unique de Chaptal,
index du README contre l’ARBRE.

    python3 outils/metiers/verifier.py                  # les fiches du dépôt
    python3 outils/metiers/verifier.py --dossier DOSSIER   # un autre dossier de fiches

La règle typographique est IMPORTÉE de `audit_typo.py` (CLAUDE.md § 7), jamais recopiée.
Le second comptage (contrôle 3) relit `prompts.jsonl` ligne à ligne, sans passer par
`lois_census.par_metier`, et compare aux nombres ÉCRITS dans les fiches · il partage les
motifs de `PAT` (une seule table), pas l’assemblage du texte ni le groupement.
Code de sortie 1 au premier écart, 2 si une source de l’atelier manque.

Contrôle 9 (12.10.2026) · aucun chemin ni nom de fichier de l’atelier dans les fiches. L’audit du
dépôt public a trouvé ce jour-là, dans les 26 fiches et le README, `outil_chaptal.html`,
`const ARBRE`, `0600_RESSOURCES/…`, `prompts.jsonl` · des chemins qu’aucun utilisateur ne possède,
relus par son IA à chaque chargement. Le générateur a été corrigé ; ce contrôle empêche le retour.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chemins  # noqa: E402
from lois_census import PAT, charger_invites, par_metier, texte_invite, cite  # noqa: E402

SECTIONS = ['## 1 · Le métier en deux lignes', '## 2 · Les tâches types', '## 3 · Vocabulaire du métier',
            '## 4 · Cadre légal et normatif cité par le corpus pour ce métier',
            '## 5 · Questions que le skill pose en priorité pour ce métier',
            '## 6 · Pièges', '## 7 · Données sensibles typiques du métier']
#: assemblé pour que ce fichier ne porte pas le mot en clair
MOT_INTERDIT = 'P' + 'ME'
CELLULE = re.compile(r'^(\d+) sur (\d+)(?:, (?:dont (\d+) )?en toutes lettres ¹)?$')
#: traces de l’atelier qu’une fiche publiée ne doit pas porter (contrôle 9, relevé du 12.10.2026)
ATELIER = re.compile(r'outil_chaptal|const ARBRE|0600_RESSOURCES|prompts\.jsonl|0500_AGENTS|0501_Prompts|'
                     r'1300_PRODUITS|classement\.json|reference_regle_articles_loi')


def arbre_charge():
    import generer  # l’extraction et la lecture de l’ARBRE vivent chez lui
    return generer, generer.charger_arbre()


def second_comptage():
    """{NN: {loi: (k, j)}} relu ligne à ligne dans prompts.jsonl, pour toutes les lois de PAT."""
    chemins.exiger(chemins.PROMPTS_JSONL, 'prompts.jsonl')
    res = {}
    with open(chemins.PROMPTS_JSONL, encoding='utf-8') as f:
        for ligne in f:
            if not ligne.strip():
                continue
            r = json.loads(ligne)
            nn = r['id'][4:6]
            d = res.setdefault(nn, {})
            for loi in PAT:
                s, l = cite(loi, r['texte_integral'])
                k, j = d.get(loi, (0, 0))
                d[loi] = (k + (1 if (s or l) else 0), j + (1 if l else 0))
    return res


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dossier', default=chemins.FICHES)
    a = ap.parse_args(argv)
    ecarts_total = 0

    audit_typo = chemins.audit_typo()
    generer, arbre_brut = arbre_charge()
    metiers = generer.metiers_de(arbre_brut)
    arbre = {nn: (m['nom'], len(refs)) for _, m, nn, refs in metiers}
    by = par_metier(charger_invites())
    fiches = sorted(glob.glob(os.path.join(a.dossier, '[0-9][0-9]-*.md')))
    tous = sorted(glob.glob(os.path.join(a.dossier, '*.md')))
    print('Fiches trouvées : %d dans %s' % (len(fiches), a.dossier))

    print('\n== 1 · Structure (7 sections, même ordre) ==')
    bon_tout = True
    for f in fiches:
        t = open(f, encoding='utf-8').read()
        pos = [t.find(s) for s in SECTIONS]
        heads = re.findall(r'^## .*$', t, flags=re.M)
        bon = all(p >= 0 for p in pos) and pos == sorted(pos) and len(heads) == 7
        if not bon:
            bon_tout = False
            print('  ÉCART', os.path.basename(f), pos, heads)
    print('  structure conforme sur %d fiches' % len(fiches) if bon_tout else '  structure AVEC ÉCARTS')
    ecarts_total += 0 if bon_tout else 1

    print('\n== 2 · Nombre de tâches · métier · ARBRE · fiche · écart ==')
    total_a = total_f = ecarts = 0
    for f in fiches:
        nn = os.path.basename(f)[:2]
        t = open(f, encoding='utf-8').read()
        sec2 = t.split(SECTIONS[1])[1].split(SECTIONS[2])[0]
        n_fiche = len(re.findall(r'^- ', sec2, flags=re.M))
        nom, n_arbre = arbre[nn]
        e = n_fiche - n_arbre
        ecarts += abs(e)
        total_a += n_arbre
        total_f += n_fiche
        print('  %s %-45s ARBRE %3d · fiche %3d · écart %+d' % (nn, nom, n_arbre, n_fiche, e))
    print('  TOTAL ARBRE %d · fiches %d · écart cumulé %d' % (total_a, total_f, ecarts))
    ecarts_total += ecarts

    print('\n== 3 · Lois de la section 4 · attestées, et décomptes recomptés par un second chemin ==')
    second = second_comptage()
    non_attestees, faux, n_lois, n_notes = [], [], 0, 0
    for f in fiches:
        nn = os.path.basename(f)[:2]
        t = open(f, encoding='utf-8').read()
        sec4 = t.split(SECTIONS[3])[1].split(SECTIONS[4])[0]
        lignes = [l for l in sec4.splitlines() if l.startswith('|') and not l.startswith('|---') and not l.startswith('| Texte')]
        txt = '\n'.join(texte_invite(r) for r in by[nn])
        for l in lignes:
            cells = [c.strip() for c in l.strip('|').split('|')]
            loi, cellule = cells[0], cells[2]
            n_lois += 1
            if loi not in PAT:
                non_attestees.append((nn, loi, 'motif inconnu'))
                continue
            if not any(re.search(p, txt) for p in PAT[loi]):
                non_attestees.append((nn, loi, 'absente des invites'))
            m = CELLULE.match(cellule)
            if not m:
                faux.append((nn, loi, cellule, 'cellule illisible'))
                continue
            k, n, j = int(m.group(1)), int(m.group(2)), int(m.group(3) or (m.group(1) if 'en toutes lettres' in cellule and not m.group(3) else 0))
            if 'en toutes lettres' in cellule:
                n_notes += 1
            k2, j2 = second[nn].get(loi, (0, 0))
            if (k, j, n) != (k2, j2, len(by[nn])):
                faux.append((nn, loi, cellule, 'second comptage %d sur %d, dont %d en toutes lettres' % (k2, len(by[nn]), j2)))
    print('  %d citations de textes contrôlées · non attestées : %d · décomptes faux : %d · cellules notées ¹ : %d'
          % (n_lois, len(non_attestees), len(faux), n_notes))
    for x in non_attestees:
        print('  NON ATTESTÉE', x)
    for x in faux:
        print('  DÉCOMPTE', x)
    ecarts_total += len(non_attestees) + len(faux)

    print('\n== 4 · « %s » ==' % MOT_INTERDIT)
    r = subprocess.run(['grep', '-n', MOT_INTERDIT] + tous, capture_output=True, text=True)
    print('  ' + (r.stdout.strip().replace('\n', '\n  ') if r.stdout.strip() else 'aucune occurrence'))
    ecarts_total += len(r.stdout.strip().splitlines())

    print('\n== 5 · art. N sans [À VÉRIFIER] ==')
    r = subprocess.run(['grep', '-nE', r'art\. ?[0-9]+'] + tous, capture_output=True, text=True)
    lignes = r.stdout.splitlines()
    fautes = [l for l in lignes if '[À VÉRIFIER]' not in l]
    print('  occurrences : %d · sans [À VÉRIFIER] : %d' % (len(lignes), len(fautes)))
    for l in fautes:
        print('  ' + l)
    ecarts_total += len(fautes)

    print('\n== 6 · audit_typo.releve sur chaque fichier (règle importée) ==')
    for f in tous:
        mesure = []
        constats = audit_typo.releve(f, True, mesure)
        inspecte, taille, droites = (mesure + [0, 0, 0])[:3]
        pct = round(100 * inspecte / taille) if taille else 0
        if constats:
            print('  %s · %d signalement(s)' % (os.path.basename(f), len(constats)))
            for ligne, quoi, extrait in constats:
                print('    ligne %-5d %-24s …%s…' % (ligne, quoi, extrait))
        else:
            print('  %s propre · %d %% du fichier inspecté · %d apostrophe(s) droite(s) comptée(s), non fautives'
                  % (os.path.basename(f), pct, droites))
        ecarts_total += len(constats)

    print('\n== 7 · « Chaptal » · une seule mention dans le dossier ==')
    occ = sum(open(f, encoding='utf-8').read().count('Chaptal') for f in tous)
    print('  %d occurrence(s) dans %d fichiers' % (occ, len(tous)))
    ecarts_total += abs(occ - 1)

    print('\n== 8 · Index du README contre l’ARBRE (secteurs, effectifs, ordre) ==')
    chemin_readme = os.path.join(a.dossier, 'README.md')
    if os.path.exists(chemin_readme):
        t = open(chemin_readme, encoding='utf-8').read()
        attendu = ['### %s · %d métiers' % (generer.q(s['nom']), len(s['enfants'])) for s in arbre_brut['enfants']]
        trouve = re.findall(r'^### .*$', t, flags=re.M)
        if trouve == attendu:
            print('  %d secteurs, mêmes noms, mêmes effectifs, même ordre que l’ARBRE' % len(attendu))
        else:
            print('  ÉCART · README', trouve, '· ARBRE', attendu)
            ecarts_total += 1
    else:
        print('  README.md absent du dossier')
        ecarts_total += 1

    print('\n== 9 · Chemins et fichiers de l’atelier · aucun dans les fiches publiées ==')
    traces = []
    for f in tous:
        for i, ligne in enumerate(open(f, encoding='utf-8'), 1):
            m = ATELIER.search(ligne)
            if m:
                traces.append((os.path.basename(f), i, m.group(0)))
    print('  %s' % ('aucune trace dans %d fichiers' % len(tous) if not traces else '%d trace(s)' % len(traces)))
    for x in traces:
        print('  TRACE', x)
    ecarts_total += len(traces)

    print('\nVERDICT ·', 'CONFORME' if ecarts_total == 0 else 'ÉCARTS · %d' % ecarts_total)
    return 0 if ecarts_total == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
