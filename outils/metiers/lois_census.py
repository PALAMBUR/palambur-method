# -*- coding: utf-8 -*-
"""Recensement strict des lois et normes citées dans prompts.jsonl, par métier (préfixe NN de l’id).

`PAT` est la seule table · clé = l’abréviation telle qu’elle s’écrit dans une fiche,
valeur = les motifs acceptés dans le corpus. `generer.py` et `verifier.py` l’importent ·
une loi absente de cette table ne peut pas entrer dans une fiche.

Pourquoi des motifs en mots en plus des sigles · le 11.10.2026, l’invite PAL-26-MO-16
nommait « l’accord intercantonal » sans écrire AIMP, et la fiche 26 perdait la seule
base légale d’un maître d’ouvrage communal. Un sigle seul ne voit pas le texte nommé
en clair. À l’inverse, « AVS » dans PAL-03-SC-09 désigne un numéro d’assuré, pas la
LAVS · le recensement compte, il ne juge pas ; la portée écrite dans la fiche se relit.
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chemins  # noqa: E402

PAT = {
 'CO': [r'\bCO\b', r'Code des obligations'],
 'CC': [r'\bCC\b', r'Code civil'],
 'CP': [r'\bCP\b', r'Code pénal'],
 'CPC': [r'\bCPC\b'],
 'LTr': [r'\bLTr\b', r'Loi sur le travail'],
 'OLT 3': [r'\bOLT ?3\b'],
 'LEg': [r'\bLEg\b', r'égalité entre femmes et hommes'],
 'nLPD': [r'\bn?LPD\b', r'protection des données'],
 'RGPD': [r'\bRGPD\b'],
 'LAA': [r'\bLAA\b', r'assurance-accidents'],
 'LPP': [r'\bLPP\b', r'prévoyance professionnelle'],
 'LAVS': [r'\bLAVS\b', r'\bAVS\b'],
 'LAMal': [r'\bLAMal\b'],
 'LCA': [r'\bLCA\b'],
 'LSA': [r'\bLSA\b'],
 'LPTh': [r'\bLPTh\b'],
 'LPMéd': [r'\bLPM[ée]d\b'],
 'LCD': [r'\bLCD\b', r'concurrence déloyale'],
 'LDA': [r'\bLDA\b', r'droit d.auteur'],
 'LPM': [r'\bLPM\b', r'protection des marques'],
 'LTVA': [r'\bLTVA\b', r'\bTVA\b'],
 'LIFD': [r'\bLIFD\b', r'impôt fédéral direct'],
 'LHID': [r'\bLHID\b'],
 'LBA': [r'\bLBA\b', r'blanchiment'],
 'LP': [r'\bLP\b', r'poursuite pour dettes'],
 'LCR': [r'\bLCR\b', r'circulation routière'],
 'OETV': [r'\bOETV\b'],
 'OTR': [r'\bOTR ?[12]?\b'],
 'LDét': [r'\bLD[ée]t\b', r'travailleurs détachés'],
 'LMP': [r'\bLMP\b', r'marchés publics'],
 # 11.10.2026 · PAL-26-MO-16 nomme le texte en mots, sans le sigle ; HarmoS exclu
 'AIMP': [r'\bAIMP\b', r'accord intercantonal(?! sur l[’\']harmonisation)'],
 'OMP': [r'\bOMP\b'],
 'LTrans': [r'\bLTrans\b', r'principe de la transparence'],
 'PA': [r'\bPA\b', r'procédure administrative'],
 'LN': [r'\bLN\b', r'Loi sur la nationalité'],
 'LDP': [r'\bLDP\b', r'droits politiques'],
 'LFAIE': [r'\bLFAIE\b', r'Lex Koller'],
 'LAT': [r'\bLAT\b', r'aménagement du territoire'],
 'LPE': [r'\bLPE\b', r'protection de l.environnement'],
 'OLED': [r'\bOLED\b'],
 'OPair': [r'\bOPair\b'],
 'OPB': [r'\bOPB\b'],
 'OTConst': [r'\bOTConst\b'],
 'OPA': [r'\bOPA\b'],
 'LDAl': [r'\bLDAl\b', r'denrées alimentaires'],
 'ODAlOUs': [r'\bODAlOUs\b'],
 'OHyg': [r'\bOHyg\b'],
 'OIDAl': [r'\bOIDAl\b'],
 'HACCP': [r'\bHACCP\b'],
 'CCNT': [r'\bCCNT\b'],
 'CCT': [r'\bCCT\b', r'convention collective'],
 'SIA 118': [r'\bSIA ?118\b'],
 'SIA 102': [r'\bSIA ?102\b'],
 'SIA 103': [r'\bSIA ?103\b'],
 'SIA 112': [r'\bSIA ?112\b'],
 'SIA': [r'\bSIA\b'],
 'ISO 9001': [r'\bISO ?9001\b'],
 'ISO 13485': [r'\bISO ?13485\b'],
 'ISO 14001': [r'\bISO ?14001\b'],
 'ISO 45001': [r'\bISO ?45001\b'],
 'ISO 22301': [r'\bISO ?22301\b'],
 'ISO 27001': [r'\bISO ?27001\b'],
 'REACH': [r'\bREACH\b'],
 'LFPr': [r'\bLFPr\b', r'formation professionnelle'],
 'PER': [r'\bPER\b', r'Plan d.études romand'],
 'HarmoS': [r'\bHarmoS\b'],
 'LRens': [r'\bLRens\b'],
 'AI Act': [r'\bAI Act\b', r'règlement européen sur l.IA', r'RIA\b'],
 'CCAG': [r'\bCCAG\b'],
 'LPrD': [r'\bLPrD\b', r'loi cantonale sur la protection des données'],
 'LInfo': [r'\bLInfo\b'],
 'ODim': [r'\bODim\b', r'dispositifs médicaux'],
 'LPGA': [r'\bLPGA\b'],
 'LACI': [r'\bLACI\b', r'assurance-chômage'],
 'LAPG': [r'\bLAPG\b'],
 'LAFam': [r'\bLAFam\b', r'allocations familiales'],
 'LSE': [r'\bLSE\b', r'service de l.emploi'],
 'LEI': [r'\bLEI\b', r'étrangers et l.intégration'],
 'Lex Koller': [r'Lex Koller'],
 'MoPEC': [r'\bMoPEC\b'],
 'Swissmedic': [r'\bSwissmedic\b'],
 'FINMA': [r'\bFINMA\b'],
 'LPCC': [r'\bLPCC\b'],
 'LSFin': [r'\bLSFin\b'],
 'LEFin': [r'\bLEFin\b'],
 'Code de déontologie FMH': [r'déontologie FMH', r'\bFMH\b'],
}


def charger_invites():
    """Les lignes de prompts.jsonl · code 2 si la source de l’atelier manque."""
    chemins.exiger(chemins.PROMPTS_JSONL, 'prompts.jsonl')
    with open(chemins.PROMPTS_JSONL, encoding='utf-8') as f:
        return [json.loads(l) for l in f if l.strip()]


def par_metier(rows):
    """Les invites groupées par préfixe NN de l’id (`PAL-NN-XX-NN`)."""
    by = collections.defaultdict(list)
    for r in rows:
        by[r['id'].split('-')[1]].append(r)
    return by


def texte_invite(r):
    """Le texte sur lequel on compte · `texte_integral` seul.

    Jusqu’au 11.10.2026 on y ajoutait le titre et les blocs sérialisés ; mesuré ce
    jour-là sur les 245 citations, cela ne changeait aucun décompte, et un relecteur
    indépendant compte sur `texte_integral`. Un seul texte, un seul décompte."""
    return r['texte_integral']


def sigle(loi):
    """Le premier motif de `PAT` est le sigle (ou le nom propre) · les suivants, le nom en toutes lettres ou l’objet."""
    return PAT[loi][0]


def formes_longues(loi):
    return PAT[loi][1:]


def cite(loi, texte):
    """(par le sigle, par la forme longue seulement) · deux booléens pour une invite."""
    s = re.search(sigle(loi), texte) is not None
    l = (not s) and any(re.search(p, texte) for p in formes_longues(loi))
    return s, l


def compter(invites, loi):
    """(k, j) · k invites citent le texte (sigle ou forme longue), dont j par la forme longue seule."""
    k = j = 0
    for r in invites:
        s, l = cite(loi, texte_invite(r))
        if s or l:
            k += 1
        if l:
            j += 1
    return k, j


def main():
    rows = charger_invites()
    by = par_metier(rows)
    res = {}
    for nn in sorted(by):
        txt = '\n'.join(texte_invite(r) for r in by[nn])
        c = {}
        for k, pats in PAT.items():
            n = sum(len(re.findall(p, txt)) for p in pats)
            if n:
                c[k] = n
        res[nn] = c
        print(nn, by[nn][0]['metier'], len(by[nn]), '→',
              ', '.join('%s %d' % (k, v) for k, v in sorted(c.items(), key=lambda x: -x[1])))
    os.makedirs(chemins.CACHE, exist_ok=True)
    sortie = os.path.join(chemins.CACHE, 'lois_par_metier.json')
    with open(sortie, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    print('écrit', sortie)


if __name__ == '__main__':
    main()
