# -*- coding: utf-8 -*-
"""Génère les 26 fiches métiers du skill et leur `README.md` · section 2 et index depuis l’ARBRE,
le reste depuis `contenu_a.py` et `contenu_b.py`.

    python3 outils/metiers/generer.py                 # écrit dans skills/palambur-method/metiers/
    python3 outils/metiers/generer.py --sortie DOSSIER   # ailleurs, pour comparer sans toucher aux fiches

Refuse d’écrire une loi en section 4 si aucune invite du métier ne la cite dans
prompts.jsonl, par son sigle ou en toutes lettres · elle est retirée et nommée en fin
de course. Le 11.10.2026, cette garde a refusé « AIMP » pour la fiche 26 parce que le
motif ne connaissait que le sigle · la garde avait raison de parler, le motif avait tort
(voir `lois_census.py`). Le même jour, un relecteur a trouvé l’index du README rangé dans
un secteur qui n’existe pas dans l’ARBRE · l’index est généré depuis l’ARBRE depuis.

Code de sortie 2 si une source de l’atelier manque (dépôt cloné hors de l’atelier).
"""
import argparse
import collections
import csv
import datetime
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chemins  # noqa: E402
from contenu_a import C as CA  # noqa: E402
from contenu_b import C as CB  # noqa: E402
from lois_census import charger_invites, par_metier, compter  # noqa: E402

C = {**CA, **CB}

#: appel de note posé dans la colonne « Invites qui le citent » quand l’invite ne dit pas le sigle
NOTE = '¹'
NOTE_TEXTE = ('¹ Nommé en toutes lettres ou par son objet dans l’invite (par exemple « AVS », « TVA », '
              '« convention collective ») · le sigle de la loi est posé par la fiche.')


def date_source(chemin):
    """La date de dernière modification de la source, jj.mm.aaaa · c’est l’état de la source
    que la fiche décrit, pas le jour où quelqu’un a lancé le script. Une constante écrite à la
    main portait ici « 11.10.2026 » et aurait menti dès la deuxième exécution (CLAUDE.md § 1)."""
    return datetime.date.fromtimestamp(os.path.getmtime(chemin)).strftime('%d.%m.%Y')


def q(s):
    """Apostrophes courbes en prose · la droite ne reste qu’entre deux chiffres (TYPOGRAPHIE.md § 3)."""
    return re.sub(r"(?<![0-9])'(?![0-9])", '’', s)


def nbsp(texte):
    """Guillemets français avec espace insécable · la règle du site."""
    return texte.replace('« ', '« ').replace(' »', ' »')


def charger_arbre():
    """`_cache/arbre.json`, refait par `extraire_arbre.mjs` s’il manque ou s’il est plus vieux que la page."""
    chemins.exiger(chemins.CHAPTAL_HTML, 'outil_chaptal.html')
    perime = (not os.path.exists(chemins.ARBRE_JSON)
              or os.path.getmtime(chemins.ARBRE_JSON) < os.path.getmtime(chemins.CHAPTAL_HTML))
    if perime:
        r = subprocess.run(['node', os.path.join(chemins.ICI, 'extraire_arbre.mjs')],
                           capture_output=True, text=True)
        if r.returncode != 0:
            sys.stderr.write(r.stderr)
            sys.exit(r.returncode)
        print(r.stdout.strip().splitlines()[-1])
    with open(chemins.ARBRE_JSON, encoding='utf-8') as f:
        return json.load(f)


def charger_isco():
    """Code CH-ISCO-19 → libellé · le libellé officiel 2166 porte un demi-cadratin, 2161 une
    apostrophe droite · règle maison (séparateur ·, apostrophe courbe), décision laissée à Victor."""
    chemins.exiger(chemins.ISCO_CSV, 'CH-ISCO-19_groupes_de_base.csv')
    isco = {}
    with open(chemins.ISCO_CSV, encoding='utf-8') as f:
        for row in csv.reader(f):
            if row and re.fullmatch(r'\d{4}', row[0].strip()):
                isco[row[0].strip()] = q(row[1].strip().replace(' – ', ' · '))
    return isco


def metiers_de(arbre):
    """(secteur, métier, NN, refs) pour chaque métier · NN lu dans les `ref` des feuilles."""
    out = []
    for s in arbre['enfants']:
        for m in s['enfants']:
            refs = [f.get('ref') for fam in m['enfants'] for f in fam['enfants']]
            nn = collections.Counter(r.split('-')[1] for r in refs if r).most_common(1)[0][0]
            out.append((s['nom'], m, nn, refs))
    return out


def cellule_citations(k, j, n):
    """« k sur n », et combien d’invites ne disent que la forme longue."""
    if j == 0:
        return '%d sur %d' % (k, n)
    if j == k:
        return '%d sur %d, en toutes lettres %s' % (k, n, NOTE)
    return '%d sur %d, dont %d en toutes lettres %s' % (k, n, j, NOTE)


def fiche(secteur, m, nn, refs, invites, isco):
    c = C[nn]
    n = len(refs)
    L = []
    L.append('# %s · fiche métier allégée' % q(m['nom']))
    L.append('')
    L.append('**Secteur** · %s · code %s · %d pistes (état de l’ARBRE au %s, `outil_chaptal.html`, `const ARBRE`).'
             % (q(secteur), nn, n, date_source(chemins.CHAPTAL_HTML)))
    L.append('')
    intit = ' ; '.join('%s %s' % (code, isco.get(code, '[À VÉRIFIER]')) for code in c['isco'])
    L.append('**Intitulé officiel (CH-ISCO-19)** · %s · libellés lus dans '
             '`0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes attribués '
             'à la fiche dans `0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`.' % intit)
    L.append('')
    L.append('Version allégée. Le skill charge cette fiche à l’Étape 1 quand la demande ou le profil de '
             'l’utilisateur désigne ce métier, pour choisir ses questions (Étape 2) et son vocabulaire (Étape 3).')
    L.append('')
    L += ['## 1 · Le métier en deux lignes', '', q(c['deux_lignes']), '']
    L += ['## 2 · Les tâches types', '',
          'Les %d pistes du métier dans l’ARBRE (`outil_chaptal.html`), par famille, sous leur titre court.' % n, '']
    compte = 0
    for fam in m['enfants']:
        L.append('### %s · %d' % (q(fam['nom']), len(fam['enfants'])))
        L.append('')
        for f in fam['enfants']:
            L.append('- ' + q(f.get('nomCourt') or f['nom']))
            compte += 1
        L.append('')
    assert compte == n, (nn, compte, n)
    L += ['## 3 · Vocabulaire du métier', '',
          'Termes exacts, français de Suisse romande. Le skill les emploie dans le Gabarit et dans le '
          'livrable à la place des équivalents français de France ou anglophones.', '',
          ' · '.join(q(v) for v in c['vocab']), '']
    L += ['## 4 · Cadre légal et normatif cité par le corpus pour ce métier', '',
          'Textes nommés, jamais un numéro d’article. Un article éventuel s’écrit `[À VÉRIFIER]` (règle du '
          '10.08.2026, `reference_regle_articles_loi.md`). État du corpus au %s, '
          '`1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl`, invites `PAL-%s-*` (%d invites), comptées '
          'sur leur texte intégral.' % (date_source(chemins.PROMPTS_JSONL), nn, len(invites)), '',
          '| Texte | Ce qu’il règle pour ce métier | Invites qui le citent |', '|---|---|---|']
    retirees, note = [], False
    for loi, portee in c['lois']:
        k, j = compter(invites, loi)
        if k == 0:
            retirees.append(loi)
            continue
        note = note or j > 0
        L.append('| %s | %s | %s |' % (loi, q(portee), cellule_citations(k, j, len(invites))))
    L.append('')
    if note:
        L += [NOTE_TEXTE, '']
    L += ['## 5 · Questions que le skill pose en priorité pour ce métier', '',
          'Une question par message, avec le compteur (Étape 2 de `SKILL.md`). L’Étape 0 (données '
          'nominatives) passe toujours avant.', '']
    for i, (qq, pourquoi) in enumerate(c['questions'], 1):
        L.append('%d. **%s** · %s' % (i, q(qq), q(pourquoi)))
    L.append('')
    L += ['## 6 · Pièges', '',
          'Ce qu’un modèle invente pour ce métier quand le cadre manque. Le skill marque `[À VÉRIFIER]` au '
          'lieu de trancher.', '']
    L += ['- ' + q(p) for p in c['pieges']] + ['']
    L += ['## 7 · Données sensibles typiques du métier', '',
          'Ce qui déclenche l’Étape 0 et s’anonymise par défaut (`protection-donnees.md`).', '']
    L += ['- ' + q(d) for d in c['sensibles']] + ['']
    return nbsp('\n'.join(L)), retirees


def readme(arbre, rows):
    """Le `README.md` du dossier · l’index est lu dans l’ARBRE, secteur par secteur, jamais rangé à la main.
    Une seule mention de Chaptal, sobre, en tête (consigne du 11.10.2026)."""
    metiers = metiers_de(arbre)
    total = sum(len(refs) for _, _, _, refs in metiers)
    versions = sorted({r.get('version', '') for r in rows if r.get('version')})
    L = []
    L.append('# Les 26 métiers · fiches allégées pour le skill')
    L.append('')
    L.append('Ce dossier branche la Méthode Palambur sur les %d métiers de l’ARBRE (`outil_chaptal.html`, '
             '`const ARBRE`, %d secteurs, %d pistes, état au %s). Une fiche par métier, même structure en sept '
             'sections · version allégée, dont la version complète, avec les invites de chaque piste, est '
             'Chaptal sur palambur.ch.'
             % (len(metiers), len(arbre['enfants']), total, date_source(chemins.CHAPTAL_HTML)))
    L.append('')
    L += ['## Règle d’usage', '',
          'Quand la demande ou le profil de l’utilisateur désigne un métier (« je suis fiduciaire », « pour mon '
          'garage », « offre d’emploi de conducteur de travaux »), le skill charge **la fiche de ce métier à '
          'l’Étape 1**, avant de choisir son lot de questions. Il en tire :', '',
          '- les **questions prioritaires** (section 5) pour composer le lot de l’Étape 2, à la place des '
          'questions génériques de `methode-palambur.md` ;',
          '- le **vocabulaire** (section 3) pour le Gabarit et le livrable ;',
          '- le **cadre légal** (section 4) pour le bloc RÔLE ET AUDIENCE et le bloc CONTRAINTES, textes nommés '
          'seulement, jamais un numéro d’article sans `[À VÉRIFIER]` ;',
          '- les **pièges** (section 6) comme zones de risque et auto-contrôle ;',
          '- les **données sensibles** (section 7) pour déclencher l’Étape 0.', '',
          'Si aucun métier n’est reconnu, le skill travaille sans fiche. Si deux métiers se croisent (une '
          'fiduciaire qui recrute), il charge les deux et prend les questions RH pour le livrable RH.', '',
          'Les différences par marché (fr-CH, fr-FR, puis les autres) sont dans `MARCHES.md`.', '']
    L += ['## Structure fixe des 26 fiches', '',
          '1. Le métier en deux lignes',
          '2. Les tâches types (toutes les pistes du métier, par famille, titres courts de l’ARBRE)',
          '3. Vocabulaire du métier',
          '4. Cadre légal et normatif cité par le corpus pour ce métier',
          '5. Questions que le skill pose en priorité pour ce métier',
          '6. Pièges',
          '7. Données sensibles typiques du métier', '',
          'Chaque fiche porte en tête son intitulé officiel CH-ISCO-19 '
          '(`0600_RESSOURCES/06.12_Referentiels_Officiels/CH-ISCO-19_groupes_de_base.csv`, codes dans '
          '`0500_AGENTS_IA/0501_Prompts_Metiers/classement.json`).', '']
    L += ['## Index par secteur', '',
          'Les secteurs et leur ordre sont ceux de l’ARBRE.', '']
    for s in arbre['enfants']:
        ms = [(sec, m, nn, refs) for sec, m, nn, refs in metiers if sec == s['nom']]
        L.append('### %s · %d métiers' % (q(s['nom']), len(ms)))
        L.append('')
        L.append('| Code | Métier | Fiche | Pistes |')
        L.append('|---|---|---|---|')
        for _, m, nn, refs in ms:
            L.append('| %s | %s | `%s.md` | %d |' % (nn, q(m['nom']), C[nn]['slug'], len(refs)))
        L.append('')
    L.append('Total · %d fiches, %d pistes.' % (len(metiers), total))
    L.append('')
    L += ['## Sources des fiches', '',
          '- Tâches, familles et index · `const ARBRE` de `outil_chaptal.html` (champs `nomCourt`, `nom`, `ref`).',
          '- Cadre légal · uniquement les textes qu’une invite du métier cite, par le sigle ou en toutes lettres, '
          'dans `1300_PRODUITS_IA/03_JACQUARD/corpus/prompts.jsonl` (%d invites, versions %s). Une fiche ne cite '
          'aucun texte absent de ses invites ; quand l’invite ne dit pas le sigle, la fiche le marque %s.'
          % (len(rows), ' à '.join([versions[0], versions[-1]]) if len(versions) > 1 else versions[0], NOTE),
          '- Vocabulaire et pièges · `0600_RESSOURCES/06.12_Referentiels_Officiels/Metiers/<NN>_<Nom>/REFERENCES_<NN>_<Nom>.md`.',
          '- Règle des articles de loi · `reference_regle_articles_loi.md` (arbitrage du 10.08.2026).',
          '- Générateurs · `outils/metiers/` du dépôt (`generer.py`, `verifier.py`).', '']
    return nbsp('\n'.join(L))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--sortie', default=chemins.FICHES,
                    help='dossier des fiches (défaut · skills/palambur-method/metiers du dépôt)')
    a = ap.parse_args(argv)

    arbre = charger_arbre()
    isco = charger_isco()
    rows = charger_invites()
    by = par_metier(rows)
    os.makedirs(a.sortie, exist_ok=True)
    os.makedirs(chemins.CACHE, exist_ok=True)
    index, problemes = [], []
    for secteur, m, nn, refs in metiers_de(arbre):
        c = C[nn]
        texte, retirees = fiche(secteur, m, nn, refs, by[nn], isco)
        problemes += [(nn, l) for l in retirees]
        with open(os.path.join(a.sortie, c['slug'] + '.md'), 'w', encoding='utf-8') as f:
            f.write(texte)
        index.append((secteur, nn, m['nom'], c['slug'], len(refs)))
        print('%s %s.md · %d pistes · %d lois' % (nn, c['slug'], len(refs), len(c['lois']) - len(retirees)))
    with open(os.path.join(a.sortie, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme(arbre, rows))
    with open(os.path.join(chemins.CACHE, 'index_fiches.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
    if problemes:
        print('LOIS NON ATTESTÉES (retirées de la fiche) :', problemes)
    else:
        print('aucune loi retirée · toutes les lois citées sont attestées dans les invites du métier')
    print('%d fiches et README.md écrits dans %s' % (len(index), a.sortie))


if __name__ == '__main__':
    main()
