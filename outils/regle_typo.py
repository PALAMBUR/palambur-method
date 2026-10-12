#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palambur · la règle typographique EMBARQUÉE dans le dépôt du skill.

    python3 outils/regle_typo.py <fichier.md> …   # relevé d’un ou plusieurs fichiers
    python3 outils/regle_typo.py --epreuve        # se casser soi-même

CE FICHIER EST UNE COPIE, ET IL LE DIT. La règle fait foi dans l’atelier
Palambur, dans `0500_AGENTS_IA/0501_Prompts_Metiers/audit_typo.py`. Le dépôt
du skill, lui, vit aussi HORS de l’atelier · tout clone public de GitHub. Le
11.10.2026, un relecteur a montré ce que coûtait l’import sans copie · sur un
clone, `controle.py` rendait « typographie · NON ÉVALUÉ », un tiret cadratin
injecté passait sans être vu, et le générateur d’adaptations, privé de la règle
de l’apostrophe, réécrivait les deux prompts avec des apostrophes droites, puis
le contrôle accusait ces prompts d’avoir été « édités à la main ». Un dépôt qui
ne peut se contrôler que depuis une seule machine n’a pas de contrôle.

CE QUE LA COPIE PORTE · le strict nécessaire aux `.md` et aux chaînes JSON de
ce dépôt · le tiret (cadratins, trait d’union séparateur, montant suisse et
case vide exemptés), l’apostrophe (courbe pour la langue, droite comptée mais
jamais condamnée, séparateur de milliers exempté), et le découpage d’un
markdown en prose et code. Elle ne porte PAS la lecture des modules Python
(`tokenize`, f-chaînes) · ce dépôt ne contrôle pas ses `.py` à la typographie.

CE QUI EMPÊCHE LA COPIE DE DIVERGER EN SILENCE (CLAUDE.md § 7 et § 8, au mieux
pour un dépôt qui vit hors de l’atelier) · `SOURCE_SHA256` est l’empreinte du
`audit_typo.py` recopié, et `COPIE_DU` sa date. `controle.py` (contrôle
« regle ») compare cette empreinte à celle du fichier de l’atelier quand il est
à côté, et REFUSE si elle diffère · « copie en retard sur la source ». Hors de
l’atelier, il dit en une ligne qu’il tourne sur la règle embarquée, et de quand
elle date. La copie n’est donc jamais « la » règle · elle est la règle d’un
jour nommé, et quelqu’un dans l’atelier le voit le jour où elle vieillit.

Pour remettre la copie à jour · recopier les constantes et fonctions ci-dessous
depuis `audit_typo.py`, puis ·

    shasum -a 256 0500_AGENTS_IA/0501_Prompts_Metiers/audit_typo.py

et reporter l’empreinte et la date. L’épreuve de ce fichier rejoue les témoins
de la source qui concernent les `.md`.
"""

import io
import re
import sys

#: la source recopiée, son empreinte sha256 complète et la date de la copie
SOURCE = '0500_AGENTS_IA/0501_Prompts_Metiers/audit_typo.py'
SOURCE_SHA256 = 'fcfa62891ac6c14230244ef0d4082b1bf1f1c5700b6d8026582594d5e813c925'
COPIE_DU = '2026-10-11'

# ---------------------------------------------------------------------------
# Recopié de audit_typo.py · le tiret
# ---------------------------------------------------------------------------

#: le montant suisse : 1'490.– et 20'000.– ne sont pas de la ponctuation
MONTANT = re.compile(r"\d[\d']*\.–")

#: le tiret employé comme séparateur, entouré d’espaces
SEPARATEUR = re.compile(r'(?<= )-(?= )')

#: les deux cadratins, cherchés partout
CADRATINS = ('—', '–')

#: une case de tableau qui ne porte QUE un tiret · le tiret y dit « rien »
CASE_VIDE = re.compile(r'\|[ \t]*([' + ''.join(CADRATINS) + r'])[ \t]*(?=\|)')


def cases_vides(texte):
    """Les tirets qui sont le contenu ENTIER d’une case de tableau · arbitré le 2026-08-17.

    Le tiret y remplace « rien ». L’exemption est tenue ÉTROITE exprès · la
    case doit ouvrir une vraie ligne de tableau, sinon une phrase de prose qui
    porte un tiret entre deux barres se ferait exempter.
    """
    positions = set()
    for m in CASE_VIDE.finditer(texte):
        debut = texte.rfind('\n', 0, m.start()) + 1
        if texte[debut:m.start() + 1].lstrip().startswith('|'):
            positions.add(m.start(1))
    return positions


# ---------------------------------------------------------------------------
# Recopié de audit_typo.py · l’apostrophe (arbitrage du mainteneur, 17.08.2026)
# ---------------------------------------------------------------------------

#: l’apostrophe de la langue, celle qu’emploie la Suisse romande · U+2019
COURBE = '’'

#: l’apostrophe droite qui N’EST PAS un séparateur de milliers · `100'000` la
#: garde, `l'outil` ne l’a plus. ALTERNATION, pas conjonction · `l'2026` et
#: `abc'123` ne sont des milliers ni l’un ni l’autre (écart mesuré le 17.08.2026,
#: 8 apostrophes dans 6 fichiers entre les deux formes).
DROITE = re.compile(r"(?<![0-9])'|'(?![0-9])")


# ---------------------------------------------------------------------------
# Recopié de audit_typo.py · ce qui, dans un markdown, n’est PAS de la prose
# ---------------------------------------------------------------------------

#: un bloc de code clôturé · ``` ou ~~~, la fermeture alignée sur l’ouverture
CLOTURE = re.compile(r'^([ \t]*)(```|~~~).*?^\1?\2[ \t]*$', re.S | re.M)

#: le code en ligne, entre accents graves, jamais sur deux lignes
EN_LIGNE = re.compile(r'`[^`\n]+`')

#: le tiret qui OUVRE une puce de liste, citée ou non · c’est la liste, pas une
#: ponctuation · le groupe réduit la zone au marqueur seul
PUCE = re.compile(r'^[ \t]*(?:>[ \t]*)*([-*+])(?=[ \t])', re.M)


def zones_code_markdown(source):
    """Les tranches d’un `.md` qui ne sont PAS de la prose · blocs, code en ligne, puces."""
    zones = [m.span() for m in CLOTURE.finditer(source)]
    zones += [m.span() for m in EN_LIGNE.finditer(source)]
    zones += [m.span(1) for m in PUCE.finditer(source)]
    return zones


# ---------------------------------------------------------------------------
# Le relevé · même contrat que audit_typo.releve, restreint au markdown
# ---------------------------------------------------------------------------

def releve(chemin, entier=True, mesure=None):
    """La mesure BRUTE · `[(ligne, quoi, extrait)]`, et dans `mesure` trois chiffres.

    `mesure` reçoit · les octets réellement inspectés, la taille du texte, et
    le nombre d’apostrophes droites en prose (comptées, jamais condamnées).
    Même contrat que la source, pour que `controle.py` lise l’une ou l’autre
    sans changer une ligne. `entier` est accepté pour la compatibilité et
    ignoré · ce dépôt n’a pas de « part neuve ».

    Un fichier qui n’est pas un markdown est lu comme de la prose d’un bout à
    l’autre · mieux vaut un faux positif qu’un silence.
    """
    texte = io.open(chemin, encoding='utf-8').read()
    markdown = chemin.lower().endswith(('.md', '.markdown', '.txt'))
    interdit = zones_code_markdown(texte) if markdown else []

    def prose(pos):
        return not any(a <= pos < b for a, b in interdit)

    inspecte = len(texte) - sum(b - a for a, b in interdit)
    if mesure is not None:
        mesure.append(max(0, inspecte))
        mesure.append(len(texte))

    exempts = {m.end() - 1 for m in MONTANT.finditer(texte)}
    exempts |= cases_vides(texte)

    signalements = []
    for tiret in CADRATINS:
        for m in re.finditer(re.escape(tiret), texte):
            if m.start() not in exempts:
                signalements.append((m.start(), tiret))
    for m in SEPARATEUR.finditer(texte):
        signalements.append((m.start(), 'trait d’union séparateur'))

    rendus = []
    for pos, quoi in sorted(s for s in signalements if prose(s[0])):
        ligne = texte[:pos].count('\n') + 1
        extrait = texte[max(0, pos - 55):pos + 20].replace('\n', ' ')
        rendus.append((ligne, quoi, extrait))

    if mesure is not None:
        mesure.append(sum(1 for m in DROITE.finditer(texte) if prose(m.start())))
    return rendus


def courber(texte):
    """L’apostrophe de langue devient courbe · le séparateur de milliers reste droit."""
    return DROITE.sub(COURBE, texte)


# ---------------------------------------------------------------------------
# L’épreuve · les témoins de la source qui concernent un markdown, rejoués ici
# ---------------------------------------------------------------------------

def epreuve():
    """Témoins FABRIQUÉS et composés depuis les constantes · jamais écrits en clair."""
    import os
    import tempfile

    CAD, DEMI = CADRATINS
    T = '-'
    AD = "'"
    #: (nom, contenu, fautes attendues, droites comptées attendues)
    CAS = [
        ('un tiret séparateur dans un .md',
         'Le devis est parti ' + T + ' le client ne répond pas.\n', 1, 0),
        ('un cadratin dans un .md',
         'Le devis est parti ' + CAD + ' le client ne répond pas.\n', 1, 0),
        ('un demi-cadratin dans un .md',
         'Trois offres ' + DEMI + ' toutes signées.\n', 1, 0),
        ('un montant suisse reste exempt',
         'Le forfait est de CHF 20' + AD + '000.' + DEMI + ' pour la formation.\n', 0, 0),
        ('une puce de liste indentée est une liste, pas une faute',
         'Texte :\n\n  ' + T + ' premier point\n  ' + T + ' second point\n', 0, 0),
        ('un tiret séparateur DANS une citation reste une faute',
         '> Le devis est parti ' + T + ' le client ne répond pas.\n', 1, 0),
        ('un bloc de code garde le droit de ses tirets',
         'Commande :\n\n```bash\nls ' + T + ' l\n```\n', 0, 0),
        ('du code en ligne garde le même droit',
         'On tape `python3 ' + T + ' fichier` puis on attend.\n', 0, 0),
        ('une case de tableau qui ne porte qu’un tiret dit « rien »',
         '| Donnée | Valeur |\n|---|---|\n| Adresse | ' + CAD + ' |\n', 0, 0),
        ('le même tiret EN PROSE entre deux barres reste une faute',
         'On écrit alors a | ' + CAD + ' | b dans la phrase.\n', 1, 0),
        ('la courbe n’est pas une faute',
         'L' + COURBE + 'outil a rendu son verdict.\n', 0, 0),
        ('la droite en prose est COMPTÉE, jamais condamnée',
         'L' + AD + 'outil a rendu son verdict.\n', 0, 1),
        ('une droite collée à un chiffre d’un seul côté est comptée',
         'Le lot L' + AD + '2026 et la clé abc' + AD + '123 sont des libellés.\n', 0, 2),
        ('le séparateur de milliers suisse n’est pas compté',
         'Le forfait est de CHF 100' + AD + '000 par an.\n', 0, 0),
        ('la droite dans un bloc de code n’est pas comptée',
         'Commande :\n\n```bash\necho ' + AD + 'bonjour' + AD + '\n```\n', 0, 0),
    ]
    dossier = tempfile.mkdtemp(prefix='epreuve_regle_typo_')
    rouges = 0
    print('ÉPREUVE · règle embarquée du %s · témoins fabriqués' % COPIE_DU)
    print('-' * 72)
    try:
        for nom, contenu, attendu, droites in CAS:
            chemin = os.path.join(dossier, 'temoin.md')
            io.open(chemin, 'w', encoding='utf-8').write(contenu)
            mesure = []
            vus = len(releve(chemin, True, mesure))
            comptees = mesure[2] if len(mesure) >= 3 else -1
            ok = vus == attendu and comptees == droites
            rouges += 0 if ok else 1
            print('  %-8s %-58s attendu %d/%d · vu %d/%d'
                  % ('conforme' if ok else 'ÉCHEC', nom, attendu, droites, vus, comptees))
        courbe_ok = courber("l'outil de 100'000") == 'l’outil de 100\'000'
        rouges += 0 if courbe_ok else 1
        print('  %-8s %-58s' % ('conforme' if courbe_ok else 'ÉCHEC',
                                'courber · la langue se courbe, les milliers restent droits'))
    finally:
        for n in os.listdir(dossier):
            os.remove(os.path.join(dossier, n))
        os.rmdir(dossier)
    print('-' * 72)
    total = len(CAS) + 1
    if rouges:
        print('  %d témoin(s) en échec sur %d · la règle embarquée ne fait pas ce qu’elle dit.'
              % (rouges, total))
        return 1
    print('  %d témoins · la règle embarquée sait dire oui ET non.' % total)
    return 0


if __name__ == '__main__':
    if '--epreuve' in sys.argv:
        sys.exit(epreuve())
    total = 0
    for chemin in sys.argv[1:]:
        mesure = []
        rendus = releve(chemin, True, mesure)
        total += len(rendus)
        part = ''
        if len(mesure) >= 2 and mesure[1]:
            part = ' · %d %% du fichier inspecté' % round(100.0 * mesure[0] / mesure[1])
        if len(mesure) >= 3:
            part += ' · %d apostrophe(s) droite(s) comptée(s), non fautives' % mesure[2]
        print('%-32s %s%s' % (chemin, 'propre' if not rendus
                              else '%d signalement(s)' % len(rendus), part))
        for ligne, quoi, extrait in rendus:
            print('  ligne %-5d %-24s …%s…' % (ligne, quoi, extrait))
    sys.exit(1 if total else 0)
