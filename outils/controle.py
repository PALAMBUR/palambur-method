#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palambur · la chaîne de contrôle du dépôt du skill, avant chaque push.

    python3 outils/controle.py                   # tout le dépôt · code de retour 0 ou 1
    python3 outils/controle.py --epreuve         # casse chaque garde sur témoin fabriqué
    python3 outils/controle.py --racine <dépôt>  # une copie du dépôt, ailleurs

POURQUOI · le plan en 30 points du 11.10.2026 (point 30) demande qu’aucune
version ne parte sur GitHub sans une chaîne de contrôle, parce qu’un push est
une publication. Ce que ce dépôt a déjà laissé passer sans elle · un tiret
cadratin dans la description du plugin, le mot « PME » dans trois fichiers
jusqu’au 24.09, des adaptations de trois mois en retard sur le skill, une
licence annoncée dans le README et absente du dépôt.

LES DIX CONTRÔLES · chacun porte un nom, et chacun dit COMBIEN il fait taire
(CLAUDE.md § 4 · sinon « rien à signaler » et « je ne regarde plus » s’écrivent
pareil) ·

    regle         la règle typographique embarquée (`outils/regle_typo.py`) est
                  à jour sur sa source · si l’`audit_typo.py` de l’atelier est à
                  côté du dépôt, les empreintes doivent coïncider ; s’il n’y est
                  pas (un clone public), le contrôle le dit en une ligne, sans
                  rougir
    typographie   zéro tiret de ponctuation dans les .md et les chaînes des
                  .json · par la règle embarquée · compte les apostrophes
                  droites qu’il ne condamne pas
    pme           le mot interdit absent de tout fichier texte · ne fait taire
                  que la citation de la règle elle-même, « PME » entre guillemets
                  ou entre accents graves, et dit combien
    json          chaque .json se charge
    version       le même numéro dans plugin.json, marketplace.json et la
                  première entrée du CHANGELOG
    adaptations   les deux prompts d’`adaptations/` sont ceux que
                  `generer_adaptations.py` fabriquerait aujourd’hui depuis les
                  trois fichiers du skill et la table des hôtes du README ·
                  empreinte déclarée = empreinte des sources, et corps identique
    frontmatter   SKILL.md ouvre sur un frontmatter avec `name` (= le dossier)
                  et `description` non vides
    taille_skill  SKILL.md tient en 500 lignes ou moins
    taille_corps  le CORPS de SKILL.md (hors frontmatter) tient en 2'800 mots
                  ou moins · la spécification recommande moins de 5'000 jetons
                  pour ce qui est chargé à l’activation · seuil dérivé au-dessus
                  de LIMITE_MOTS_CORPS · né le 11.10.2026 (plan, point 88)
    liens         aucun lien relatif cassé dans les .md · fait taire les liens
                  externes (http, mailto, ancres) et dit combien

CE QUE CE CONTRÔLE NE FAIT PAS · il n’écrit dans aucun fichier, délibérément.
Un instrument partagé qui corrige tout seul écrase le travail d’une autre
session en croyant bien faire (CLAUDE.md § 3). Il mesure, il rend compte.

L’ÉPREUVE · chaque garde est cassée sur un témoin FABRIQUÉ dans un dossier
temporaire, et l’épreuve exige qu’elle refuse POUR SA raison · le constat doit
porter le code du contrôle éprouvé et nommer le témoin. Un témoin qui
réveillerait le voisin (incident du 18.08.2026, `registre_invites.py`) serait
un ÉCHEC, pas un vert. Chaque garde montre aussi qu’elle sait dire oui, sur un
témoin sain.

HORS DE L’ATELIER PALAMBUR · la règle typographique fait foi dans
`0500_AGENTS_IA/0501_Prompts_Metiers/audit_typo.py`, à côté de ce dépôt. Le
dépôt en embarque une COPIE DATÉE, `outils/regle_typo.py`, qui porte
l’empreinte sha256 de sa source · le contrôle `regle` compare les deux dès que
l’atelier est là, et refuse une copie en retard. Deux copies d’une règle
finissent par diverger (CLAUDE.md § 7) ; celle-ci diverge à voix haute. La
première version importait la source et rendait NON ÉVALUÉ sans elle · un
clone public ne pouvait jamais être CONFORME (relecture du 11.10.2026).
"""

import hashlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(ICI)
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import generer_adaptations as gen  # noqa: E402
import regle_typo  # noqa: E402  · la copie embarquée et datée de la règle

#: où l’atelier range la source de la règle, relativement au dépôt
SOURCE_REGLE = os.path.join('..', '0501_Prompts_Metiers', 'audit_typo.py')
EMPREINTE_DECLAREE = re.compile(r"^SOURCE_SHA256 = '([0-9a-f]{64})'", re.M)

DOSSIERS_IGNORES = {'.git', 'node_modules', '__pycache__', '.DS_Store'}
#: les transcriptions déposées sous `epreuves/reponses/` sont CE QU’UN MODÈLE A
#: ÉCRIT, jugé par `mesurer.py` (G11 pour le mot interdit) · ce ne sont pas des
#: textes Palambur. Le 11.10.2026 au soir, trente transcriptions Apertus ont
#: fait rougir la typographie 208 fois et le mot interdit 18 fois · le dépôt
#: ne pouvait plus partir à cause de phrases que personne chez nous n’avait
#: écrites. Seuls les transcriptions sont tues · `RELEVE.md` et `LISEZ-MOI.md`,
#: écrits par nous, restent contrôlés. Le compte des fichiers tus est rendu.
DOSSIER_TRANSCRIPTIONS = os.path.join('epreuves', 'reponses')
NOTRE_PROSE = {'RELEVE.md', 'LISEZ-MOI.md', 'README.md'}


def est_transcription(racine, chemin):
    rel = relatif(racine, chemin)
    return rel.startswith(DOSSIER_TRANSCRIPTIONS + os.sep) and os.path.basename(rel) not in NOTRE_PROSE
EXT_TEXTE = ('.md', '.json', '.py', '.sh', '.yml', '.yaml', '.txt', '.html')

#: le mot interdit, assemblé pour que ce fichier ne le porte pas en clair
MOT_INTERDIT = re.compile(r'\bP' + r'ME\b')
#: sa citation légitime · entre guillemets français ou entre accents graves
CITATION = re.compile(r'« P' + r'ME »|`P' + r'ME`')

LIMITE_LIGNES_SKILL = 500

#: le corps de SKILL.md, hors frontmatter, en MOTS. La spécification Agent
#: Skills (`https://agentskills.io/specification`, lue le 11.10.2026) écrit,
#: dans « Progressive disclosure » · « Instructions (< 5000 tokens
#: recommended): The full SKILL.md body is loaded when the skill is activated ».
#: Un jeton ne se compte pas sans le découpeur du modèle, qu’un clone public
#: n’a pas · on convertit, et on dit comment. Le glossaire d’Anthropic
#: (`https://platform.claude.com/docs/en/about-claude/glossary`, lu le
#: 11.10.2026) · sur les modèles d’avant Claude 4.7, « a token represents
#: approximately 3.5 English characters » · 5'000 jetons font 17'500
#: caractères. Le corps mesuré le 11.10.2026 pesait 15'685 caractères pour
#: 2'555 mots (`str.split`, espaces et balises comprises), soit 6,1 caractères
#: par mot · 17'500 ÷ 6,1 = 2'850 mots, arrondis EN DESSOUS à 2'800. La même
#: page avertit que les découpeurs de Claude 4.7 et suivants rendent
#: « approximately 30 percent more tokens for the same text » · à ce compte le
#: seuil tomberait vers 2'200 mots et le corps du 11.10 serait déjà au-delà.
#: Le seuil retenu est donc la lecture la plus indulgente des deux, et il le
#: dit · le jour où un comptage exact de jetons est fait (API de comptage,
#: avec le modèle visé), c’est lui qui remplace cette dérivation.
LIMITE_MOTS_CORPS = 2800
SEMVER = re.compile(r'^\d+\.\d+\.\d+$')


def fichiers(racine, extensions):
    """Les fichiers du dépôt portant une de ces extensions, hors dossiers ignorés."""
    trouves = []
    for dossier, sous, noms in os.walk(racine):
        sous[:] = sorted(d for d in sous if d not in DOSSIERS_IGNORES)
        for n in sorted(noms):
            if n.endswith(extensions):
                trouves.append(os.path.join(dossier, n))
    return trouves


def relatif(racine, chemin):
    return os.path.relpath(chemin, racine)


# ---------------------------------------------------------------------------
# Les contrôles · chacun rend (constats, tus, note)
#   constats · liste de chaînes, chacune préfixée par le code du contrôle
#   tus      · combien le contrôle a fait taire en connaissance de cause
#   note     · ce qu’il a regardé, pour que le verdict dise sur quoi il porte
# ---------------------------------------------------------------------------

def ctrl_regle(racine):
    """La règle embarquée est à jour sur sa source, quand la source est là.

    Lit l’empreinte DÉCLARÉE dans `outils/regle_typo.py` du dépôt contrôlé
    (pas celle du module importé · sur une copie, c’est la copie qu’on juge),
    hache `../0501_Prompts_Metiers/audit_typo.py` s’il existe, compare. Sans
    atelier à côté, une ligne de note et pas de constat · un clone public n’a
    pas la source, et ce n’est pas une faute du clone.
    """
    chemin_copie = os.path.join(racine, 'outils', 'regle_typo.py')
    if not os.path.isfile(chemin_copie):
        return ['regle · outils/regle_typo.py absent du dépôt'], 0, ''
    m = EMPREINTE_DECLAREE.search(io.open(chemin_copie, encoding='utf-8').read())
    if not m:
        return ['regle · outils/regle_typo.py ne déclare pas SOURCE_SHA256'], 0, ''
    declaree = m.group(1)
    date = re.search(r"^COPIE_DU = '([^']+)'", io.open(chemin_copie, encoding='utf-8').read(), re.M)
    date = date.group(1) if date else '?'
    source = os.path.normpath(os.path.join(racine, SOURCE_REGLE))
    if not os.path.isfile(source):
        return [], 0, 'clone hors atelier, règle embarquée du %s' % date
    reelle = hashlib.sha256(open(source, 'rb').read()).hexdigest()
    if reelle != declaree:
        return (['regle · copie en retard sur la source · regle_typo.py déclare %s…, '
                 'audit_typo.py fait %s… · reporter la règle et son empreinte'
                 % (declaree[:12], reelle[:12])], 0, 'atelier à côté')
    return [], 0, 'atelier à côté, empreinte identique, règle du %s' % date


def ctrl_typographie(racine):
    """Zéro tiret de ponctuation · `.md` par `regle_typo.releve`, `.json` sur leurs chaînes."""
    constats, droites, lus, transcriptions = [], 0, 0, 0
    for chemin in fichiers(racine, ('.md',)):
        if est_transcription(racine, chemin):
            transcriptions += 1
            continue
        mesure = []
        for ligne, quoi, extrait in regle_typo.releve(chemin, True, mesure):
            constats.append('typographie · %s ligne %d · %s · …%s…'
                            % (relatif(racine, chemin), ligne, quoi, extrait.strip()))
        if len(mesure) >= 3:
            droites += mesure[2]
        lus += 1
    for chemin in fichiers(racine, ('.json',)):
        try:
            donnees = json.load(io.open(chemin, encoding='utf-8'))
        except ValueError:
            continue                      # c’est le contrôle `json` qui le dira
        for texte in _chaines(donnees):
            for tiret in regle_typo.CADRATINS:
                if tiret in texte and not regle_typo.MONTANT.search(texte):
                    constats.append('typographie · %s · cadratin dans une chaîne · …%s…'
                                    % (relatif(racine, chemin), texte[:60]))
            if regle_typo.SEPARATEUR.search(texte):
                constats.append('typographie · %s · trait d’union séparateur · …%s…'
                                % (relatif(racine, chemin), texte[:60]))
        lus += 1
    note = '%d fichier(s) lus · %d apostrophe(s) droite(s) comptée(s), non fautives' % (lus, droites)
    if transcriptions:
        note += ' · %d transcription(s) de modèle tue(s) (%s, jugées par mesurer.py)' % (
            transcriptions, DOSSIER_TRANSCRIPTIONS)
    return constats, droites + transcriptions, note


def _chaines(valeur):
    if isinstance(valeur, str):
        yield valeur
    elif isinstance(valeur, dict):
        for v in valeur.values():
            yield from _chaines(v)
    elif isinstance(valeur, list):
        for v in valeur:
            yield from _chaines(v)


#: un fichier qui TRAQUE le mot écrit son motif en clair · `\b`, les trois
#: lettres, `\b` (la lettre b colle au P, donc MOT_INTERDIT ne voit pas le motif
#: lui-même, et ce commentaire n’écrit pas le mot non plus). Ce fichier
#: est un instrument, et ses témoins fabriqués ont le droit de porter le mot.
#: Le 11.10.2026, `epreuves/mesurer.py` fabriquait « Notre P.. reste à votre
#: disposition » pour éprouver sa garde G11, et le contrôle l’accusait. On
#: DÉCOUVRE l’instrument à son motif, on ne tient pas une liste de noms à la
#: main (CLAUDE.md § 7 · une liste écrite à la main ne connaît que le passé).
MOTIF_TRAQUEUR = re.compile(r'\\bP' + r'ME\\b')


def ctrl_pme(racine):
    """Le mot interdit absent · la citation de la règle et les instruments qui le
    traquent sont tus, et comptés à part."""
    constats, tus, instruments, transcriptions = [], 0, [], 0
    for chemin in fichiers(racine, EXT_TEXTE):
        if est_transcription(racine, chemin):
            transcriptions += 1
            continue
        texte = io.open(chemin, encoding='utf-8', errors='replace').read()
        cites = {m.start() + 2 for m in CITATION.finditer(texte)}
        cites |= {m.start() + 1 for m in CITATION.finditer(texte)}
        traqueur = chemin.endswith('.py') and MOTIF_TRAQUEUR.search(texte) is not None
        dans_instrument = 0
        for m in MOT_INTERDIT.finditer(texte):
            if m.start() in cites:
                tus += 1
                continue
            if traqueur:
                dans_instrument += 1
                continue
            ligne = texte[:m.start()].count('\n') + 1
            constats.append('pme · %s ligne %d · on dit « entreprises »'
                            % (relatif(racine, chemin), ligne))
        if dans_instrument:
            instruments.append((relatif(racine, chemin), dans_instrument))
    note = '%d citation(s) de la règle tue(s)' % tus
    if instruments:
        note += ' · %d témoin(s) tu(s) dans %d instrument(s) qui traquent le mot (%s)' % (
            sum(n for _, n in instruments), len(instruments),
            ', '.join('%s×%d' % (f, n) for f, n in instruments))
    if transcriptions:
        note += ' · %d transcription(s) de modèle tue(s) (%s, G11 de mesurer.py)' % (
            transcriptions, DOSSIER_TRANSCRIPTIONS)
    return constats, tus + sum(n for _, n in instruments) + transcriptions, note


def ctrl_json(racine):
    """Chaque .json se charge."""
    constats, n = [], 0
    for chemin in fichiers(racine, ('.json',)):
        n += 1
        try:
            json.load(io.open(chemin, encoding='utf-8'))
        except ValueError as e:
            constats.append('json · %s · %s' % (relatif(racine, chemin), e))
    return constats, 0, '%d fichier(s) JSON' % n


def _version_changelog(racine):
    chemin = os.path.join(racine, 'CHANGELOG.md')
    if not os.path.isfile(chemin):
        return None
    m = re.search(r'^## \[(\d+\.\d+\.\d+)\]', io.open(chemin, encoding='utf-8').read(), re.M)
    return m.group(1) if m else None


def ctrl_version(racine):
    """Un seul numéro de version, dans les trois endroits qui le portent."""
    constats = []
    versions = {}
    try:
        p = json.load(io.open(os.path.join(racine, '.claude-plugin', 'plugin.json'), encoding='utf-8'))
        versions['plugin.json'] = p.get('version')
        m = json.load(io.open(os.path.join(racine, '.claude-plugin', 'marketplace.json'), encoding='utf-8'))
        for i, plugin in enumerate(m.get('plugins', [])):
            versions['marketplace.json plugins[%d]' % i] = plugin.get('version')
    except (OSError, ValueError) as e:
        return ['version · fichier de plugin illisible · %s' % e], 0, ''
    versions['CHANGELOG.md'] = _version_changelog(racine)
    for ou, v in versions.items():
        if not v:
            constats.append('version · %s · aucune version' % ou)
        elif not SEMVER.match(v):
            constats.append('version · %s · « %s » n’est pas X.Y.Z' % (ou, v))
    distinctes = {v for v in versions.values() if v}
    if len(distinctes) > 1:
        constats.append('version · divergence · ' + ', '.join(
            '%s=%s' % (ou, v) for ou, v in versions.items()))
    return constats, 0, 'version %s' % (distinctes.pop() if len(distinctes) == 1 else '?')


def ctrl_adaptations(racine):
    """Les deux prompts d’adaptation sont ceux que le générateur fabriquerait aujourd’hui.

    Deux questions, dans l’ordre · l’en-tête déclare-t-il l’empreinte des
    sources d’aujourd’hui (sinon le skill a bougé après la génération), et le
    corps est-il celui que le générateur rend (sinon quelqu’un a édité le
    produit à la main). La date de l’en-tête est ignorée · voir
    `generer_adaptations.corps_sans_date`.
    """
    constats = []
    skill = os.path.join(racine, 'skills', 'palambur-method')
    try:
        textes = gen.lire_sources(skill, os.path.join(racine, 'adaptations'))
        produits = gen.fabriquer(textes)
    except gen.Refus as e:
        return ['adaptations · le générateur refuse (%s) · %s' % (e.raison, e)], 0, ''
    attendue = gen.empreinte(textes)
    for cle, (nom, contenu, _) in produits.items():
        chemin = os.path.join(racine, 'adaptations', nom)
        if not os.path.isfile(chemin):
            constats.append('adaptations · %s · absent' % nom)
            continue
        actuel = io.open(chemin, encoding='utf-8').read()
        declaree = gen.empreinte_declaree(actuel)
        if declaree != attendue:
            constats.append('adaptations · %s · empreinte déclarée %s, sources %s · '
                            'relancer generer_adaptations.py --ecrire' % (nom, declaree, attendue))
        elif gen.corps_sans_date(actuel) != gen.corps_sans_date(contenu):
            constats.append('adaptations · %s · corps différent de ce que le générateur '
                            'rend · édité à la main ?' % nom)
    return constats, 0, 'empreinte des sources %s' % attendue


def ctrl_frontmatter(racine):
    """SKILL.md ouvre sur `---`, `name` égal au dossier, `description` non vide."""
    constats = []
    for dossier in sorted(os.listdir(os.path.join(racine, 'skills'))) \
            if os.path.isdir(os.path.join(racine, 'skills')) else []:
        chemin = os.path.join(racine, 'skills', dossier, 'SKILL.md')
        if not os.path.isfile(chemin):
            constats.append('frontmatter · skills/%s · pas de SKILL.md' % dossier)
            continue
        texte = io.open(chemin, encoding='utf-8').read()
        m = re.match(r'---\n(.*?)\n---\n', texte, re.S)
        if not m:
            constats.append('frontmatter · skills/%s/SKILL.md · aucun frontmatter en tête' % dossier)
            continue
        champs = dict(re.findall(r'^(\w+):\s*(.*)$', m.group(1), re.M))
        if not champs.get('name', '').strip():
            constats.append('frontmatter · skills/%s/SKILL.md · `name` absent ou vide' % dossier)
        elif champs['name'].strip() != dossier:
            constats.append('frontmatter · skills/%s/SKILL.md · `name` « %s » ≠ dossier'
                            % (dossier, champs['name'].strip()))
        if not champs.get('description', '').strip():
            constats.append('frontmatter · skills/%s/SKILL.md · `description` absente ou vide' % dossier)
    return constats, 0, ''


def ctrl_taille_skill(racine):
    """SKILL.md tient en 500 lignes · au-delà, la divulgation progressive a échoué."""
    constats, note = [], ''
    for chemin in fichiers(os.path.join(racine, 'skills'), ('SKILL.md',)) \
            if os.path.isdir(os.path.join(racine, 'skills')) else []:
        n = io.open(chemin, encoding='utf-8').read().count('\n')
        note = '%d ligne(s)' % n
        if n > LIMITE_LIGNES_SKILL:
            constats.append('taille_skill · %s · %d lignes, limite %d'
                            % (relatif(racine, chemin), n, LIMITE_LIGNES_SKILL))
    return constats, 0, note


FRONTMATTER = re.compile(r'---\n(.*?)\n---\n', re.S)


def mots_corps(texte):
    """Le nombre de mots du corps d’un SKILL.md, frontmatter retiré.

    Sans frontmatter reconnaissable, tout le texte est le corps · c’est au
    contrôle `frontmatter` de dire qu’il manque, pas à celui-ci de se taire.
    """
    m = FRONTMATTER.match(texte)
    corps = texte[m.end():] if m else texte
    return len(corps.split())


def ctrl_taille_corps(racine):
    """Le corps de SKILL.md tient en LIMITE_MOTS_CORPS mots · au-delà, ce qui est
    chargé à chaque activation dépasse la recommandation de la spécification."""
    constats, note = [], ''
    for chemin in fichiers(os.path.join(racine, 'skills'), ('SKILL.md',)) \
            if os.path.isdir(os.path.join(racine, 'skills')) else []:
        n = mots_corps(io.open(chemin, encoding='utf-8').read())
        note = '%d mot(s) hors frontmatter, limite %d' % (n, LIMITE_MOTS_CORPS)
        if n > LIMITE_MOTS_CORPS:
            constats.append('taille_corps · %s · %d mots hors frontmatter, limite %d'
                            % (relatif(racine, chemin), n, LIMITE_MOTS_CORPS))
    return constats, 0, note


LIEN = re.compile(r'!?\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
EXTERNE = ('http://', 'https://', 'mailto:', '#')


def ctrl_liens(racine):
    """Aucun lien relatif cassé dans les .md · les liens externes sont tus et comptés."""
    constats, tus, transcriptions = [], 0, 0
    for chemin in fichiers(racine, ('.md',)):
        #: une transcription cite les chemins que LE MODÈLE a lus chez lui · le
        #: 12.10.2026, Codex écrivait « .agents/skills/palambur-method/SKILL.md »,
        #: vrai dans son dossier de travail, faux depuis `epreuves/reponses/`, et
        #: le dépôt rougissait sur une phrase qu’on ne corrige pas (pièce à conviction)
        if est_transcription(racine, chemin):
            transcriptions += 1
            continue
        texte = io.open(chemin, encoding='utf-8').read()
        texte = re.sub(r'```.*?```', '', texte, flags=re.S)
        #: le code EN LIGNE aussi · le 11.10.2026, `portabilite/ANNUAIRES.md`
        #: montrait le format d’une ligne d’annuaire, `[skill-name](url)`, entre
        #: accents graves, et le contrôle le lisait comme un lien cassé vers « url »
        texte = re.sub(r'`[^`\n]*`', '', texte)
        for m in LIEN.finditer(texte):
            cible = m.group(1)
            if cible.startswith(EXTERNE):
                tus += 1
                continue
            chemin_cible = os.path.normpath(os.path.join(
                os.path.dirname(chemin), unquote(cible.split('#')[0])))
            if not os.path.exists(chemin_cible):
                constats.append('liens · %s · « %s » ne mène nulle part'
                                % (relatif(racine, chemin), cible))
    return constats, tus, '%d lien(s) externe(s) tu(s) · %d transcription(s) de modèle tue(s)' % (tus, transcriptions)


CONTROLES = [
    ('regle', ctrl_regle),
    ('typographie', ctrl_typographie),
    ('pme', ctrl_pme),
    ('json', ctrl_json),
    ('version', ctrl_version),
    ('adaptations', ctrl_adaptations),
    ('frontmatter', ctrl_frontmatter),
    ('taille_skill', ctrl_taille_skill),
    ('taille_corps', ctrl_taille_corps),
    ('liens', ctrl_liens),
]


def principal(racine=DEPOT):
    print('CHAÎNE DE CONTRÔLE DU SKILL · %s' % racine)
    print('-' * 72)
    total = 0
    for nom, ctrl in CONTROLES:
        constats, tus, note = ctrl(racine)
        total += len(constats)
        etat = 'conforme' if not constats else '%d constat(s)' % len(constats)
        print('  %-13s %-14s %s' % (nom, etat, note))
        for c in constats:
            print('      ' + c)
    print('-' * 72)
    print('VERDICT · %s' % ('CONFORME · le dépôt peut partir' if total == 0
                            else '%d constat(s) · on ne pousse pas' % total))
    return 0 if total == 0 else 1


# ---------------------------------------------------------------------------
# L’épreuve
# ---------------------------------------------------------------------------

#: ce qui compose le dépôt SAIN de l’épreuve · une liste fixe, pas « tout le
#: dépôt » · d’autres sessions y déposent des fichiers en cours, et l’épreuve
#: doit juger l’instrument, pas leur travail du jour
SAIN = ('LICENSE', 'CHANGELOG.md', '.claude-plugin/plugin.json',
        '.claude-plugin/marketplace.json', 'skills/palambur-method/SKILL.md',
        'skills/palambur-method/methode-palambur.md',
        'skills/palambur-method/protection-donnees.md',
        'adaptations/README.md', 'outils/regle_typo.py')
#: ce que les liens relatifs des fichiers SAIN visent · posés vides dans la copie
CIBLES_LIENS_SAIN = ('README.md', 'outils/generer_adaptations.py',
                     'portabilite/INSTALLATION.md', 'portabilite/VEILLE_PLATEFORMES.md')


def epreuve():
    """Casse chaque garde sur témoin fabriqué · refus POUR SA raison, et oui sur le sain."""
    racine_tmp = tempfile.mkdtemp(prefix='epreuve_controle_')
    rouges, joues = 0, []

    def depot(nom):
        """Une copie du dépôt sain, prête à être cassée."""
        d = os.path.join(racine_tmp, nom)
        for rel in SAIN:
            src, dst = os.path.join(DEPOT, rel), os.path.join(d, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy(src, dst)
        #: les adaptations du dépôt sain se FABRIQUENT depuis les sources
        #: copiées, elles ne se prélèvent pas sur le disque · le 11.10.2026,
        #: d’autres sessions retouchaient SKILL.md toutes les dix minutes, et
        #: l’épreuve rougissait sur « sain » parce que les fichiers du disque
        #: avaient une empreinte de retard · elle jugeait leur travail du jour,
        #: pas l’instrument (CLAUDE.md § 4 · un témoin se fabrique)
        textes = gen.lire_sources(os.path.join(d, 'skills', 'palambur-method'),
                                  os.path.join(d, 'adaptations'))
        for nom, contenu, _ in gen.fabriquer(textes).values():
            ecrire(d, os.path.join('adaptations', nom), contenu)
        #: les cibles des liens relatifs d’`adaptations/README.md`, vides · le
        #: dépôt sain juge l’instrument, pas le contenu des voisins
        for rel in CIBLES_LIENS_SAIN:
            if not os.path.exists(os.path.join(d, rel)):
                ecrire(d, rel, '')
        return d

    def ecrire(d, rel, contenu):
        chemin = os.path.join(d, rel)
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        io.open(chemin, 'w', encoding='utf-8').write(contenu)

    def modifier(d, rel, fonction):
        chemin = os.path.join(d, rel)
        texte = io.open(chemin, encoding='utf-8').read()
        io.open(chemin, 'w', encoding='utf-8').write(fonction(texte))

    def dire(ok, nom, attendu, vu):
        nonlocal rouges
        rouges += 0 if ok else 1
        joues.append(nom)
        print('  %-8s %-56s attendu %-12s vu %s'
              % ('conforme' if ok else 'ÉCHEC', nom, attendu, vu))

    #: ce que chaque contrôle fait DÉJÀ taire sur le dépôt sain · le CHANGELOG
    #: cite « PME » deux fois et porte deux liens externes. Un témoin s’attend
    #: à un nombre EN PLUS de cette base, pas à un nombre absolu · la première
    #: version comparait en absolu et rougissait sur un instrument juste
    base_tus = {}

    def rougit(nom, code, d, indice, tus_en_plus=None):
        """Le contrôle `code` doit parler, pour SA raison, et nommer l’indice."""
        ctrl = dict(CONTROLES)[code]
        constats, tus, _ = ctrl(d)
        siens = [c for c in constats if c.startswith(code + ' ·')]
        pertinents = [c for c in siens if indice in c]
        ok = bool(pertinents) and len(siens) == len(constats)
        delta = tus - base_tus.get(code, 0)
        if tus_en_plus is not None:
            ok = ok and delta == tus_en_plus
        vu = ('%d constat(s), %d pour « %s »' % (len(constats), len(pertinents), indice)
              if constats else 'silence')
        if tus_en_plus is not None:
            vu += ', %d tu(s) en plus' % delta
        dire(ok, nom, code, vu)

    def se_tait(nom, code, d, tus_en_plus=None):
        ctrl = dict(CONTROLES)[code]
        constats, tus, _ = ctrl(d)
        delta = tus - base_tus.get(code, 0)
        ok = not constats and (tus_en_plus is None or delta == tus_en_plus)
        vu = ('silence' if not constats else '%d constat(s)' % len(constats))
        if tus_en_plus is not None:
            vu += ', %d tu(s) en plus' % delta
        dire(ok, nom, 'silence', vu)

    print('ÉPREUVE · témoins fabriqués, chaque garde refuse POUR SA raison')
    print('-' * 72)
    try:
        # le dépôt sain passe tous les contrôles, et fixe la base des « tus »
        d = depot('sain')
        for code, ctrl in CONTROLES:
            base_tus[code] = ctrl(d)[1]
            se_tait('sain · %s se tait' % code, code, d)

        # regle · un atelier FABRIQUÉ à côté de la copie, jamais le vrai
        def atelier(d, contenu):
            chemin = os.path.normpath(os.path.join(d, SOURCE_REGLE))
            os.makedirs(os.path.dirname(chemin), exist_ok=True)
            io.open(chemin, 'w', encoding='utf-8').write(contenu)
        d = depot('regle_hors_atelier')
        constats, _, note = ctrl_regle(d)
        dire(not constats and 'hors atelier' in note and regle_typo.COPIE_DU in note,
             'sans atelier à côté · une ligne, pas de constat', 'silence daté',
             'silence · ' + note if not constats else '%d constat(s)' % len(constats))
        d = depot('regle_a_jour')
        source_vraie = 'REGLE = 1\n'
        atelier(d, source_vraie)
        modifier(d, 'outils/regle_typo.py', lambda t: EMPREINTE_DECLAREE.sub(
            "SOURCE_SHA256 = '%s'" % hashlib.sha256(source_vraie.encode()).hexdigest(), t))
        constats, _, note = ctrl_regle(d)
        dire(not constats and 'identique' in note,
             'atelier à côté, même empreinte · silence', 'silence', note if not constats else constats[0])
        d = depot('regle_en_retard')
        atelier(d, 'REGLE = 2\n')
        rougit('atelier à côté, empreinte différente · copie en retard', 'regle', d, 'copie en retard')
        d = depot('regle_sans_empreinte')
        modifier(d, 'outils/regle_typo.py', lambda t: EMPREINTE_DECLAREE.sub('SOURCE_SHA256 = None', t))
        rougit('une copie qui ne déclare pas son empreinte', 'regle', d, 'SOURCE_SHA256')

        # typographie · le cadratin se compose depuis la règle, jamais écrit ici
        CAD = regle_typo.CADRATINS[0]
        d = depot('typo_md')
        ecrire(d, 'temoin.md', 'Le devis est parti ' + CAD + ' le client ne répond pas.\n')
        rougit('un cadratin dans un .md est signalé', 'typographie', d, 'temoin.md')
        d = depot('typo_json')
        ecrire(d, 'temoin.json', json.dumps({'description': 'Méthode ' + CAD + ' outil'}))
        rougit('un cadratin dans une chaîne JSON est signalé', 'typographie', d, 'temoin.json')
        d = depot('typo_sep')
        ecrire(d, 'temoin.json', json.dumps({'description': 'simple - et sûr'}))
        rougit('un trait d’union séparateur dans un JSON est signalé', 'typographie', d, 'temoin.json')
        d = depot('typo_montant')
        ecrire(d, 'temoin.json', json.dumps({'prix': 'CHF 20\'000.' + regle_typo.CADRATINS[1]}))
        se_tait('un montant suisse dans un JSON reste exempt', 'typographie', d)

        # pme
        d = depot('pme_nu')
        ecrire(d, 'temoin.md', 'Pensé pour les P' + 'ME de Suisse romande.\n')
        rougit('le mot interdit à nu est signalé', 'pme', d, 'temoin.md', tus_en_plus=0)
        d = depot('pme_cite')
        ecrire(d, 'temoin.md', 'Le mot « P' + 'ME » est interdit ; `P' + 'ME` aussi.\n')
        se_tait('la citation de la règle est tue, et comptée deux fois', 'pme', d, tus_en_plus=2)
        d = depot('pme_dans_mot')
        ecrire(d, 'temoin.md', 'La P' + 'MEUBLE SA livre.\n')
        se_tait('un mot qui contient les trois lettres n’est pas le mot', 'pme', d, tus_en_plus=0)
        #: l’instrument qui traque le mot a le droit de fabriquer un témoin
        traque = 'RE = re.compile(r"\\bP' + 'ME\\b")\n'
        d = depot('pme_instrument')
        ecrire(d, 'temoin.py', traque + 'TEMOIN = "Notre P' + 'ME reste ouverte."\n')
        se_tait('le témoin d’un instrument qui traque le mot est tu, et compté', 'pme', d, tus_en_plus=1)
        d = depot('pme_py_sans_traque')
        ecrire(d, 'temoin.py', 'TEXTE = "Notre P' + 'ME reste ouverte."\n')
        rougit('le mot dans un .py qui ne le traque pas est signalé', 'pme', d, 'temoin.py', tus_en_plus=0)
        d = depot('pme_md_traque')
        ecrire(d, 'temoin.md', traque + 'Notre P' + 'ME reste ouverte.\n')
        rougit('un .md n’est pas un instrument, même s’il montre le motif', 'pme', d, 'temoin.md', tus_en_plus=0)

        # json
        d = depot('json')
        ecrire(d, 'temoin.json', '{"a": 1,}')
        rougit('un JSON invalide est signalé', 'json', d, 'temoin.json')

        # version
        d = depot('version_market')
        modifier(d, '.claude-plugin/marketplace.json', lambda t: t.replace('"1.0.0"', '"1.0.1"'))
        rougit('une version qui diverge dans marketplace.json', 'version', d, 'divergence')
        d = depot('version_changelog')
        modifier(d, 'CHANGELOG.md', lambda t: t.replace('## [1.0.0]', '## [1.1.0]', 1))
        rougit('une version qui diverge dans le CHANGELOG', 'version', d, 'divergence')
        d = depot('version_forme')
        modifier(d, '.claude-plugin/plugin.json', lambda t: t.replace('"1.0.0"', '"v1"'))
        rougit('une version qui n’est pas X.Y.Z', 'version', d, 'X.Y.Z')

        # adaptations
        d = depot('adapt_source')
        modifier(d, 'skills/palambur-method/methode-palambur.md',
                 lambda t: t.replace('## Garde-fous suisses', '## Garde-fous suisses ', 1))
        rougit('une source modifiée sans régénérer · empreinte', 'adaptations', d, 'empreinte déclarée')
        d = depot('adapt_main')
        modifier(d, 'adaptations/methode-palambur-prompt-court.md',
                 lambda t: t.replace('Gabarit Palambur', 'Gabarit', 1))
        rougit('un produit édité à la main · corps', 'adaptations', d, 'corps différent')
        d = depot('adapt_absent')
        os.remove(os.path.join(d, 'adaptations/methode-palambur-prompt.md'))
        rougit('un produit absent', 'adaptations', d, 'absent')
        d = depot('adapt_pme')
        modifier(d, 'skills/palambur-method/protection-donnees.md',
                 lambda t: t.replace('entreprises', 'P' + 'ME', 1))
        rougit('une source qui fait refuser le générateur', 'adaptations', d, 'refuse (pme)')

        # frontmatter
        d = depot('fm_desc')
        modifier(d, 'skills/palambur-method/SKILL.md',
                 lambda t: re.sub(r'^description:.*\n', '', t, count=1, flags=re.M))
        rougit('SKILL.md sans description', 'frontmatter', d, 'description')
        d = depot('fm_nom')
        modifier(d, 'skills/palambur-method/SKILL.md',
                 lambda t: t.replace('name: palambur-method', 'name: autre-nom', 1))
        rougit('SKILL.md dont le name n’est pas le dossier', 'frontmatter', d, 'dossier')
        d = depot('fm_aucun')
        modifier(d, 'skills/palambur-method/SKILL.md', lambda t: t.split('---\n', 2)[2])
        rougit('SKILL.md sans frontmatter', 'frontmatter', d, 'aucun frontmatter')

        # taille
        d = depot('taille')
        modifier(d, 'skills/palambur-method/SKILL.md',
                 lambda t: t + '\n' * (LIMITE_LIGNES_SKILL + 1 - t.count('\n')))
        rougit('SKILL.md de 501 lignes', 'taille_skill', d, 'limite')

        # taille du corps en mots · le témoin ajoute ses mots sur UNE ligne,
        # pour ne pas réveiller le voisin `taille_skill`
        d = depot('corps_long')
        modifier(d, 'skills/palambur-method/SKILL.md',
                 lambda t: t + '\n' + ' '.join(['mot'] * (LIMITE_MOTS_CORPS + 1 - mots_corps(t))) + '\n')
        rougit('un corps de %d mots' % (LIMITE_MOTS_CORPS + 1), 'taille_corps', d, 'mots')
        d = depot('corps_frontmatter_gras')
        modifier(d, 'skills/palambur-method/SKILL.md',
                 lambda t: t.replace('---\n', '---\nbourre: ' + ' '.join(['mot'] * LIMITE_MOTS_CORPS) + '\n', 1))
        se_tait('%d mots dans le frontmatter ne comptent pas dans le corps' % LIMITE_MOTS_CORPS,
                'taille_corps', d)

        # liens
        d = depot('lien_casse')
        ecrire(d, 'temoin.md', 'Voir [le guide](portabilite/INEXISTANT.md).\n')
        rougit('un lien relatif cassé est signalé', 'liens', d, 'INEXISTANT', tus_en_plus=0)
        d = depot('lien_sain')
        ecrire(d, 'temoin.md', 'Voir [le journal](CHANGELOG.md#journal), [le site](https://palambur.ch) '
                               'et [l’ancre](#ici).\n')
        se_tait('un lien relatif juste et deux externes tus', 'liens', d, tus_en_plus=2)
        d = depot('lien_code')
        ecrire(d, 'temoin.md', 'Exemple :\n\n```md\n[x](INEXISTANT.md)\n```\n')
        se_tait('un lien dans un bloc de code n’est pas un lien', 'liens', d)
        d = depot('lien_code_en_ligne')
        ecrire(d, 'temoin.md', 'Format attendu : `[skill-name](url)`, puis [vrai](CHANGELOG.md).\n')
        se_tait('un lien dans du code en ligne n’est pas un lien', 'liens', d)
        d = depot('lien_transcription')
        ecrire(d, 'epreuves/reponses/hote-x/cas.md', 'Lu [le skill](.agents/skills/x/SKILL.md).\n')
        ecrire(d, 'epreuves/reponses/hote-x/RELEVE.md', 'Voir [le cas](cas.md) et [rien](INEXISTANT.md).\n')
        rougit('un lien cassé dans une transcription est tu, le même dans RELEVE.md parle',
               'liens', d, 'INEXISTANT', tus_en_plus=0)
    finally:
        shutil.rmtree(racine_tmp)

    print('-' * 72)
    if rouges:
        print('  %d témoin(s) en échec sur %d · le contrôle ne fait pas ce qu’il dit.'
              % (rouges, len(joues)))
        return 1
    print('  %d témoins · le contrôle sait dire oui ET non.' % len(joues))
    return 0


if __name__ == '__main__':
    if '--epreuve' in sys.argv:
        sys.exit(epreuve())
    racine = DEPOT
    if '--racine' in sys.argv:
        #: une copie du dépôt, ailleurs · le contrôle lit, il n’écrit nulle part
        racine = os.path.abspath(sys.argv[sys.argv.index('--racine') + 1])
    sys.exit(principal(racine))
