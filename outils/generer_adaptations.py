#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palambur · fabrique les deux prompts d’adaptation depuis le skill lui-même.

    python3 outils/generer_adaptations.py             # à blanc · tailles et diff
    python3 outils/generer_adaptations.py --ecrire    # écrit les deux fichiers
    python3 outils/generer_adaptations.py --epreuve   # casse ses gardes sur témoins
    python3 outils/generer_adaptations.py --source <dépôt>   # à blanc, sur une copie

POURQUOI CE SCRIPT EXISTE · le 11.10.2026, le relevé du dépôt public a montré
que les deux prompts du dossier `adaptations/` dataient du 12.07.2026, alors
que le skill avait changé le 04.08 et le 24.09. Trois mois de dérive, parce
que les adaptations étaient retouchées à la main et que personne n’y pensait
après avoir touché le skill. Une copie faite à la main est une divergence qui
attend sa date.

CE QU’IL FAIT · il lit les trois fichiers du skill (`SKILL.md`,
`methode-palambur.md`, `protection-donnees.md`), en extrait les règles qui
portent la méthode (les blocs du Gabarit, les niveaux, les garde-fous, la
question d’anonymisation, le compteur, le ton) et les injecte dans un GABARIT
DE RÉDACTION fixe, écrit ici. Il lit aussi la TABLE DES HÔTES
d’`adaptations/README.md` (quel hôte reçoit quelle version, et dans quel état
au dernier relevé) pour écrire le chapeau de chaque fichier · une seule source
pour les noms des hôtes, parce que le 11.10.2026 le chapeau citait encore
« Agent Mistral (Le Chat) » et « Gemini Gem », deux produits que la veille
avait déclarés remplacés le même jour. Il rend deux fichiers :

    adaptations/methode-palambur-prompt.md        · ≤ 8'000 caractères
    adaptations/methode-palambur-prompt-court.md  · ≤ 1'500 caractères (le bloc à coller)

et c’est la table du README qui dit à qui chacun est destiné.

Chaque fichier commence par une ligne « Généré le … (empreinte sha256 courte …)
· ne pas éditer à la main ». L’empreinte est celle des SOURCES, pas du
produit · `outils/controle.py` la recalcule et refuse si elle ne correspond
plus, ce qui rend la dérive de juillet impossible à reproduire en silence.

CE QU’IL REFUSE, ET POUR QUELLE RAISON · chaque refus porte un code, parce
qu’une épreuve doit demander « as-tu refusé POUR CETTE RAISON » et jamais
« as-tu refusé » (CLAUDE.md § 4, incident du 18.08.2026) ·

    taille     · le bloc à coller dépasse la limite de sa plateforme
    pme        · une source porte le mot interdit (on dit « entreprises »)
    structure  · une section attendue manque dans une source, une case de la
                 table des niveaux est tronquée, la table des hôtes manque ·
                 le skill a changé de forme et le gabarit ne sait plus où lire
    source     · un fichier source est introuvable

POURQUOI LE GABARIT EST ICI ET PAS DANS UN FICHIER À PART · les autres
plateformes n’ont pas la divulgation progressive de Claude Code · elles
reçoivent UNE boîte d’instructions, bornée. Le prompt n’est donc pas une copie
du skill, c’est une CONDENSATION, et l’ordre des sections, les transitions et
ce qu’on sacrifie en premier sont des décisions de rédaction. Elles vivent
dans le code, relues avec lui.

CE QUI VIENT DES VERSIONS DU 12.07 ET A ÉTÉ GARDÉ · le compteur « Question 1
sur 4 », le lot anticipé de quatre posé une question par message, la sortie en
deux temps (Gabarit rempli puis livrable), la liste des plateformes visées, la
remarque « sur ces plateformes, l’assistant EST la méthode, il n’y a pas de mot
déclencheur ». Ce qui a été retiré · tout chiffre que la source ne porte plus.

TYPOGRAPHIE · les sources écrivent encore l’apostrophe droite (`l'outil`) ·
la maison publie la courbe (`l’outil`), arbitré par Victor le 17.08.2026. La
règle fait foi dans `0501_Prompts_Metiers/audit_typo.py` ; ce script lit sa
copie EMBARQUÉE et DATÉE, `outils/regle_typo.py`, qui porte l’empreinte de la
source et que `controle.py` compare à l’original dès que l’atelier est à côté.
La première version importait la source quand elle la trouvait et ne faisait
rien sinon · sur un clone public, elle réécrivait les adaptations avec des
apostrophes droites, et le contrôle les accusait d’avoir été éditées à la main
(relecture du 11.10.2026).
"""

import difflib
import hashlib
import io
import os
import re
import shutil
import sys
import tempfile
from datetime import date

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(ICI)
SKILL = os.path.join(DEPOT, 'skills', 'palambur-method')
ADAPTATIONS = os.path.join(DEPOT, 'adaptations')
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import regle_typo  # noqa: E402  · la règle embarquée et datée, voir son en-tête

#: l’ordre est FIXE · il entre dans l’empreinte, et une empreinte qui dépend
#: de l’ordre de lecture du disque n’est pas une empreinte. Les trois fichiers
#: du skill, puis la table des hôtes (le README d’`adaptations/`), qui écrit
#: le chapeau · un chapeau qui changerait sans changer l’empreinte serait
#: accusé par `controle.py` d’avoir été édité à la main
SOURCES_SKILL = ('SKILL.md', 'methode-palambur.md', 'protection-donnees.md')
SOURCE_HOTES = 'adaptations/README.md'
SOURCES = SOURCES_SKILL + (SOURCE_HOTES,)

#: limites des champs d’instructions · 8'000 caractères pour le champ le plus
#: large rencontré (GPT personnalisé, Projet Claude), 1'500 pour le plus court
#: (Instructions personnalisées ChatGPT). Relevé du 12.07.2026 ; la table des
#: hôtes d’`adaptations/README.md`, datée, dit qui reçoit quoi aujourd’hui
LIMITE_COMPLET = 8000
LIMITE_COURT = 1500

PRODUITS = {
    'complet': ('methode-palambur-prompt.md', LIMITE_COMPLET),
    'court': ('methode-palambur-prompt-court.md', LIMITE_COURT),
}

#: le mot interdit, assemblé pour que ce fichier ne le porte pas en clair ·
#: `controle.py` relit tout le dépôt, ce script compris
MOT_INTERDIT = re.compile(r'\bP' + r'ME\b')

ENTETE = ('> Généré le %s depuis SKILL.md, methode-palambur.md, '
          'protection-donnees.md et la table des hôtes d’adaptations/README.md '
          '(empreinte sha256 courte %s) · '
          'ne pas éditer à la main, relancer `outils/generer_adaptations.py`.')


class Refus(Exception):
    """Un refus qui sait POURQUOI il refuse · `raison` est un des codes de l’en-tête."""

    def __init__(self, raison, message):
        Exception.__init__(self, message)
        self.raison = raison


# ---------------------------------------------------------------------------
# La règle typographique · la copie embarquée, datée et surveillée
# ---------------------------------------------------------------------------

#: le même nom qu’avant pour `controle.py`, qui lit `gen.DROITE`
DROITE, COURBE = regle_typo.DROITE, regle_typo.COURBE
courber = regle_typo.courber


# ---------------------------------------------------------------------------
# Lire les sources
# ---------------------------------------------------------------------------

def lire_sources(dossier=SKILL, dossier_adaptations=None):
    """Rend {nom: texte} des quatre sources, ou refuse (`source`, `pme`).

    `dossier` est le dossier du skill ; `dossier_adaptations` celui du README
    des hôtes, déduit du premier (`../../adaptations`) quand il n’est pas donné ·
    c’est la disposition du dépôt, et celle que les épreuves reproduisent.

    Le refus « pme » est ici et pas dans le contrôle final parce qu’un mot
    interdit dans la source finirait dans les deux produits · autant refuser
    AVANT de fabriquer. Le 24.09.2026, trois occurrences ont été corrigées sur
    GitHub · la copie locale du skill les porte encore le 11.10.
    """
    if dossier_adaptations is None:
        dossier_adaptations = os.path.join(os.path.dirname(os.path.dirname(dossier)),
                                           'adaptations')
    textes = {}
    for nom in SOURCES:
        chemin = (os.path.join(dossier_adaptations, 'README.md') if nom == SOURCE_HOTES
                  else os.path.join(dossier, nom))
        if not os.path.isfile(chemin):
            raise Refus('source', 'source introuvable · %s' % chemin)
        textes[nom] = io.open(chemin, encoding='utf-8').read()
    for nom, texte in textes.items():
        for m in MOT_INTERDIT.finditer(texte):
            ligne = texte[:m.start()].count('\n') + 1
            raise Refus('pme', 'mot interdit dans %s ligne %d · on dit '
                        '« entreprises »' % (nom, ligne))
    return textes


def empreinte(textes):
    """Les douze premiers hexadécimaux du sha256 des sources, dans l’ordre fixe."""
    h = hashlib.sha256()
    for nom in SOURCES:
        h.update(textes[nom].encode('utf-8'))
        h.update(b'\0')
    return h.hexdigest()[:12]


# ---------------------------------------------------------------------------
# Extraire · par section et par liste, jamais par position de ligne
# ---------------------------------------------------------------------------

def motif_souple(aiguille):
    """Le motif d’une aiguille dont les apostrophes acceptent la droite ET la courbe.

    Le 11.10.2026 les sources sont passées à l’apostrophe courbe (règle maison,
    Victor 17.08.2026) et le générateur, qui cherchait « blocs d'extension »
    avec la droite, a refusé un skill intact. La forme de l’apostrophe n’est
    pas un changement de structure · on ne refuse pas pour elle.
    """
    #: une seule passe · deux `replace` successifs réinjecteraient la seconde
    #: apostrophe dans la classe que la première vient d’écrire
    return re.sub("['’]", "['’]", re.escape(aiguille))


def section(texte, titre, nom_source):
    """Le corps d’une section `## titre…` jusqu’au prochain `## ` ou `# `.

    On cherche le titre par son DÉBUT, pas en entier · un titre peut gagner
    une précision sans que la section change de sens. S’il manque, c’est que
    le skill a changé de forme · refus `structure`, parce qu’un gabarit qui
    injecterait une chaîne vide rendrait un prompt troué et vert.
    """
    m = re.search(r'^##+ [^\n]*' + motif_souple(titre) + r'[^\n]*\n(.*?)(?=^#{1,2} |\Z)',
                  texte, re.M | re.S)
    if not m:
        raise Refus('structure', 'section « %s » introuvable dans %s'
                    % (titre, nom_source))
    return m.group(1).strip()


def puces(corps, minimum, quoi):
    """Les items d’une liste (`- `, `1. `) · refuse s’il y en a moins que prévu."""
    items = [m.group(1).strip() for m in
             re.finditer(r'^(?:- |\d+\. )(.+)$', corps, re.M)]
    if len(items) < minimum:
        raise Refus('structure', '%s · %d item(s) trouvé(s), %d attendu(s)'
                    % (quoi, len(items), minimum))
    return items


def phrase_contenant(texte, fragment, nom_source):
    """La ligne qui porte `fragment` (apostrophe droite ou courbe), ou refus `structure`."""
    motif = re.compile(motif_souple(fragment))
    for ligne in texte.splitlines():
        if motif.search(ligne):
            return ligne.strip()
    raise Refus('structure', '« %s » introuvable dans %s' % (fragment, nom_source))


#: un renvoi vers un fichier du skill, entre parenthèses · « (voir `x.md`) »,
#: « (règle et table dans `x.md`) ». Le 11.10.2026 le prompt complet renvoyait
#: à `references-juridiques.md`, qu’un utilisateur de ChatGPT n’a pas · un
#: renvoi vers un fichier absent est une promesse creuse, on le retire
RENVOI_FICHIER = re.compile(r'\s*\([^()]*`[^`]+\.md`[^()]*\)')


def sans_renvois(texte):
    """Le texte sans ses renvois parenthésés vers des fichiers du skill."""
    return RENVOI_FICHIER.sub('', texte).strip()


def nom_et_corps(item):
    """`**NOM** · corps` → (NOM, corps) · la forme des blocs du Gabarit."""
    m = re.match(r'\*\*(.+?)\*\*\s*[·:]\s*(.*)$', item, re.S)
    if not m:
        raise Refus('structure', 'item sans nom en gras · %s' % item[:60])
    return m.group(1).strip(), sans_renvois(m.group(2))


def phrases(texte):
    """Les phrases d’un texte, l’exemple « Ex. » retiré · pour tenir la limite."""
    texte = re.sub(r'\s*Ex\. «.*?»\s*', ' ', texte).strip()
    return [p for p in re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ü«*])', texte) if p]


def premieres_phrases(texte, n):
    """Les `n` premières phrases."""
    return ' '.join(phrases(texte)[:n]).strip()


def condenser(texte):
    """La première phrase, puis celle que la SOURCE met en gras · sinon la deuxième.

    Décidé le 11.10.2026 en relisant le produit · à deux phrases par bloc, le
    bloc RÔLE ET AUDIENCE perdait « L’audience appartient à ce bloc », qui est
    la phrase que la source souligne, au profit d’une phrase de transition.
    Quand l’auteur a mis une phrase en gras, c’est celle-là qu’il veut voir
    survivre à la condensation · on ne choisit pas à sa place.
    """
    liste = phrases(texte)
    if len(liste) < 2:
        return ' '.join(liste)
    grasse = next((p for p in liste[1:] if '**' in p), liste[1])
    return liste[0] + ' ' + grasse


def extraire(textes):
    """Tout ce que le gabarit injecte · un dict, chaque clé fabriquée ou refusée."""
    skill = textes['SKILL.md']
    methode = textes['methode-palambur.md']
    donnees = textes['protection-donnees.md']
    r = {}

    #: la question binaire d’anonymisation, mot pour mot · la seule phrase
    #: que les plateformes doivent prononcer à l’identique
    ligne = phrase_contenant(skill, 'Je détecte des données nominatives', 'SKILL.md')
    m = re.search(r'« Je détecte.*»', ligne)
    if not m:
        raise Refus('structure', 'question binaire mal formée dans SKILL.md')
    r['question_binaire'] = m.group(0)

    m = re.search(r'\*\*(\d+) hypothèses conséquentes ou plus\*\*', skill)
    if not m:
        raise Refus('structure', 'repère « N hypothèses conséquentes » absent de SKILL.md')
    r['seuil_hypotheses'] = m.group(1)

    #: le compteur se cherche NU · la forme du 04.08 l’écrivait entre guillemets
    #: dans la prose, celle du 11.10 le montre dans un bloc de code
    m = re.search(r'(Question 1 sur \d+)', skill)
    if not m:
        raise Refus('structure', 'compteur « Question 1 sur N » absent de SKILL.md')
    r['compteur'] = m.group(1)

    #: la taille du lot se lit dans le TITRE de l’Étape 2 · « anticiper par lot
    #: de quatre » (04.08) comme « anticiper un lot de quatre » (11.10). La
    #: première version lisait « Vise environ quatre » dans le corps, phrase
    #: que la réécriture du 11.10 a retirée · la garde a parlé le jour même
    m = re.search(r'^## Étape 2[^\n]*\blot de (\w+)', skill, re.M)
    if not m:
        raise Refus('structure', 'titre de l’Étape 2 sans « lot de N » dans SKILL.md')
    r['taille_lot'] = m.group(1)

    #: le mode relecture (Étape 4, né le 11.10) n’existe que si la source le
    #: porte · on injecte un paragraphe, ou rien, jamais une promesse creuse
    r['relecture'] = bool(re.search(r'^## Étape 4[^\n]*relecture', skill, re.M | re.I))

    promesses = puces(section(skill, 'Principe', 'SKILL.md'), 2, 'les deux promesses')
    r['promesses'] = [nom_et_corps(p) for p in promesses[:2]]

    blocs = puces(section(methode, 'les 5 blocs', 'methode-palambur.md'), 5, 'les 5 blocs')
    r['blocs'] = [nom_et_corps(b) for b in blocs[:5]]
    ext = puces(section(methode, "blocs d'extension", 'methode-palambur.md'), 4,
                'les 4 blocs d’extension')
    r['extensions'] = [nom_et_corps(b) for b in ext[:4]]
    r['critere_extension'] = phrase_contenant(methode, 'Quand passer en 9 blocs',
                                              'methode-palambur.md')

    corps = section(methode, 'Les 4 niveaux', 'methode-palambur.md')
    lignes = [l for l in corps.splitlines() if l.startswith('| **')]
    if len(lignes) < 4:
        raise Refus('structure', 'table des 4 niveaux · %d ligne(s)' % len(lignes))
    r['niveaux'] = []
    for l in lignes[:4]:
        cases = [c.strip().replace('**', '') for c in l.strip('|').split('|')]
        if len(cases) < 4:
            raise Refus('structure', 'niveau %s · %d case(s), 4 attendues' % (cases[0], len(cases)))
        #: la 4e case dit la cadence (« 0 à 1, jamais de lot ») · une case d’un
        #: seul mot est un fragment, et le prompt du 11.10 a rendu « ; aucune. »
        #: sans que rien ne le voie · deux mots au moins, ou refus
        if len(cases[3].split()) < 2:
            raise Refus('structure', 'niveau %s · cadence tronquée « %s »' % (cases[0], cases[3]))
        r['niveaux'].append(cases)

    #: la ligne « Contexte retenu · … » (Étape 3) et le zéro jargon (Ton) ·
    #: le 11.10.2026 au soir, dix cas sur dix joués sur Apertus avec le prompt
    #: complet rougissaient G17 (contexte absent) et G16 (« prompt »,
    #: « hallucination » face à l’utilisateur) · le prompt collé ne portait ni
    #: l’une ni l’autre, alors que le skill natif les exige depuis le matin
    m = re.search(r'`(Contexte retenu · [^`]+)`', skill)
    if not m:
        raise Refus('structure', 'forme fixe `Contexte retenu · …` absente de SKILL.md')
    r['contexte'] = m.group(1)
    jargon = phrase_contenant(skill, 'Zéro jargon face à l’utilisateur', 'SKILL.md')
    m = re.search(r'\*\*Zéro jargon.*?\. ', jargon + ' ')
    if not m:
        raise Refus('structure', 'règle « Zéro jargon » mal formée dans SKILL.md')
    r['jargon'] = m.group(0).strip()

    r['hotes'] = table_hotes(textes[SOURCE_HOTES])

    r['champs'] = [nom_et_corps(c) for c in
                   puces(section(methode, 'Champs DONNÉES', 'methode-palambur.md'),
                         4, 'les champs DONNÉES')]
    r['garde_fous'] = [nom_et_corps(g) for g in
                       puces(section(methode, 'Garde-fous suisses', 'methode-palambur.md'),
                             4, 'les garde-fous suisses')]
    r['ton'] = section(methode, 'Ton & voix', 'methode-palambur.md').split('\n\n')[0]

    r['convention'] = phrase_contenant(donnees, "Convention d'anonymisation",
                                       'protection-donnees.md')
    r['marqueurs'] = [re.match(r'(`\[[^\]]+\]`)', p).group(1) for p in
                      puces(section(donnees, 'Marqueurs', 'protection-donnees.md'),
                            3, 'les marqueurs')
                      if re.match(r'`\[', p)]
    #: la mention nLPD d’un document externe est lue pour vérifier qu’elle
    #: existe encore · le garde-fou nLPD la porte déjà mot pour mot dans le
    #: produit, on ne l’écrit pas deux fois
    phrase_contenant(donnees, 'Document externe', 'protection-donnees.md')
    return r


def table_hotes(readme):
    """La table « Où coller le prompt » d’`adaptations/README.md`, lue, jamais recopiée.

    Rend {'releve': 'jj.mm.aaaa', 'complète': [hôtes], 'courte': [hôtes]} · les
    hôtes dont la colonne « Quelle version » commence par « complète » ou
    « courte ». Les lignes « aucune » (le skill lui-même suffit) ne vont pas
    dans un chapeau de prompt collable. Refus `structure` si la section, la
    table ou la date de relevé manquent · un chapeau sans hôte serait vert et
    vide.
    """
    corps = section(readme, 'Où coller le prompt', SOURCE_HOTES)
    m = re.search(r'relevé le \*\*(\d\d\.\d\d\.\d{4})\*\*', corps)
    if not m:
        raise Refus('structure', 'date de relevé « relevé le **jj.mm.aaaa** » absente de %s'
                    % SOURCE_HOTES)
    hotes = {'releve': m.group(1), 'complète': [], 'courte': []}
    for l in corps.splitlines():
        if not l.startswith('| ') or l.startswith('|---'):
            continue
        cases = [c.strip() for c in l.strip().strip('|').split('|')]
        #: l’en-tête se reconnaît à sa case ENTIÈRE · un hôte dont le nom
        #: commencerait par « Hôte » a été sauté par la première version
        if len(cases) < 4 or cases[0] == 'Hôte' or set(cases[0]) <= set('-: '):
            continue
        version = cases[1].lower()
        for cle in ('complète', 'courte'):
            if version.startswith(cle):
                hotes[cle].append(cases[0])
    if not hotes['complète'] or not hotes['courte']:
        raise Refus('structure', 'table des hôtes · %d « complète », %d « courte » dans %s'
                    % (len(hotes['complète']), len(hotes['courte']), SOURCE_HOTES))
    return hotes


def nombre(n):
    """`8166` → `8'166` · le séparateur de milliers suisse, apostrophe droite."""
    return '{:,}'.format(n).replace(',', "'")


# ---------------------------------------------------------------------------
# Le gabarit de rédaction · les sections sont fixes, le contenu est injecté
# ---------------------------------------------------------------------------

def _blocs_numerotes(blocs):
    return '\n'.join('%d. **%s** · %s' % (i, nom, condenser(corps))
                     for i, (nom, corps) in enumerate(blocs, 1))


def rediger_complet(r):
    """Le bloc à coller de la version complète · l’ordre est une décision."""
    niveaux = '\n'.join('- **%s** · %s → %s ; %s.' % (n[0], n[1].lower(), n[2].lower(),
                                                      n[3].lower().rstrip('.'))
                        for n in r['niveaux'])
    #: les noms seuls · la glose d’une phrase par bloc (≈ 200 caractères) a
    #: cédé la place à la ligne de contexte et au zéro jargon le 11.10 au soir
    extensions = ', '.join('**%s**' % nom for nom, _ in r['extensions'])
    garde_fous = '\n'.join('- **%s** · %s' % (nom, condenser(corps)) for nom, corps in r['garde_fous'])
    #: une phrase par livrable · la ligne de contexte et le zéro jargon (11.10
    #: au soir) ont pris 400 caractères sous le plafond ChatGPT de 8'000
    champs = '\n'.join('- **%s** · %s' % (nom, premieres_phrases(corps, 1)) for nom, corps in r['champs'])
    promesses = ' et '.join('**%s** (%s)' % (nom.lower(), premieres_phrases(corps, 1).rstrip('.'))
                            for nom, corps in r['promesses'])
    critere = re.sub(r'^\*\*Quand passer en 9 blocs\*\*\s*:\s*', '', r['critere_extension'])
    critere = premieres_phrases(critere[:1].upper() + critere[1:], 1)
    relecture = ''
    if r['relecture']:
        relecture = ('\n## Mode relecture\n\nSi l’utilisateur joint un texte déjà écrit et demande de le '
                     'relire, le vérifier ou le passer au crible : aucune question. Rends un tableau '
                     '« Constat · Risque · Correction proposée » (données inventées, articles de loi '
                     'non sourcés, LEg, nLPD, ton), puis la version corrigée. La relecture corrige la '
                     'forme, le droit et les données ; elle ne réécrit pas le fond.\n')

    return '''Tu es l’assistant **Méthode Palambur**. Tu transformes une demande métier souvent sous-spécifiée en **livrable de haute qualité** (offre d’emploi, contrat, devis, offre commerciale, relance client, note interne, compte rendu, courrier, charte…), pensé pour les **entreprises de Suisse romande**. **La Méthode** est l’ensemble ; **le Gabarit Palambur** en est l’outil, les 5 blocs ci-dessous.

Deux promesses · %(promesses)s. L’utilisateur repart avec un livrable qu’il peut envoyer **en confiance**.

## Règle d’or · questionner AVANT de produire

Avant d’écrire le moindre mot du livrable, vérifie dans l’ordre :

1. **Données nominatives ?** Si la demande contient des noms de clients ou de personnes, des montants, des contrats, ta toute première réponse est UNE question binaire, seule :
   %(question_binaire)s
   Puis applique la décision **partout** (Gabarit ET livrable). Jamais d’hybride : on ne mélange pas vrais noms et pseudonymes.
2. **Devrais-tu faire %(seuil)s hypothèses conséquentes ou plus ?** Si oui, clarifie avant de produire, selon la cadence ci-dessous.

Jamais un livrable rempli d’hypothèses prudentes suivi d’une liste de « points à valider » : on questionne **avant**, pas après. Si tout est déjà fourni, produis directement.

## Cadence · anticiper par lot de %(taille_lot)s, demander une par une

**En amont, anticipe le lot** : les manques réellement déterminants, du plus structurant au plus accessoire ; tout ce qui peut recevoir un défaut prudent en sort. Au plus %(taille_lot)s.

**En surface, ne pose qu’UNE question par message**, avec le compteur : « %(compteur)s ». Choix lettrés A, B, C, D (deux à quatre), **défaut prudent signalé**, échappatoire « autre / je ne sais pas ». Un livrable simple se cadre en un lot ; un livrable complexe (charte, contrat, politique interne) en mérite deux ou trois. Ne demande QUE ce qui change le livrable ; pour le reste, défaut signalé ou marqueur %(marqueur_completer)s.

## Le Gabarit Palambur · les 5 blocs

Règle de contrôle : **un bloc manquant, un résultat approximatif.**

%(blocs)s

**Quatre blocs d’extension** pour un livrable long ou juridiquement sensible : %(extensions)s. %(critere)s

## Les 4 niveaux

%(niveaux)s

## Champs DONNÉES qui font la différence

%(champs)s

## Sortie en DEUX temps, toujours, dans cet ordre

D’abord **une ligne de contexte**, forme fixe : `%(contexte)s`.

Puis deux parties, chacune sous un titre fixe :

1. **Gabarit Palambur** (titre du bloc) · le Gabarit rempli, autonome, prêt à copier-coller, assemblé depuis les réponses, dans l’ordre des 5 blocs. Dans CONTRAINTES, écris : « si une information manque, écrivez %(marqueur_completer)s et ne la remplacez jamais par une valeur plausible ».
2. **Livrable** (titre du bloc) · le texte prêt à l’emploi, produit à partir du Gabarit.

La partie 1 n’est jamais omise. Ne produis la sortie qu’une fois les questions posées et répondues : jamais de Gabarit dans le même message qu’une question.
%(relecture)s
## Garde-fous suisses (tout livrable sensible · RH, contrat, communication externe)

%(garde_fous)s

Marqueurs d’information manquante, jamais une invention : %(marqueurs)s. Sur tout livrable sensible, rappelle que **la validation humaine reste obligatoire**.

## Anonymisation (si décision « anonymiser »)

%(convention)s

## Ton

%(ton)s

%(jargon)s
''' % dict(
        promesses=promesses,
        contexte=r['contexte'],
        jargon=r['jargon'],
        question_binaire=r['question_binaire'],
        seuil=r['seuil_hypotheses'],
        taille_lot=r['taille_lot'],
        compteur=r['compteur'],
        blocs=_blocs_numerotes(r['blocs']),
        extensions=extensions,
        critere=critere,
        relecture=relecture,
        niveaux=niveaux,
        champs=champs,
        garde_fous=garde_fous,
        marqueurs=', '.join(r['marqueurs']),
        marqueur_completer=r['marqueurs'][0],
        convention=re.sub(r"^\*\*Convention d['’]anonymisation\*\*\s*:\s*", '', r['convention']),
        #: sans la phrase sur les métaphores · elle décore, les deux autres règlent
        ton=re.sub(r'\s*Métaphores[^.]*\.', '', r['ton']),
    )


def rediger_court(r):
    """Le bloc à coller de la version courte · ce qu’on sacrifie est décidé ici.

    Gardé · la question binaire (résumée), le seuil, le lot et le compteur,
    les noms des 5 blocs, les garde-fous par leur nom, les marqueurs, le ton.
    Sacrifié · les niveaux, les champs DONNÉES, les blocs d’extension. À
    1'500 caractères, chaque phrase ajoutée en chasse une autre.
    """
    noms_blocs = ' · '.join(nom.capitalize() if nom.isupper() else nom
                            for nom, _ in r['blocs'])
    noms_gf = []
    for nom, _ in r['garde_fous']:
        court = nom.split('·')[0].strip()
        noms_gf.append(court if court[:1].isupper() and court[1:2].isupper() or court.startswith('n')
                       else court[:1].lower() + court[1:])
    relecture = ''
    if r['relecture']:
        relecture = ('\n**Relecture :** texte joint → aucune question ; tableau '
                     '« Constat · Risque · Correction », puis version corrigée.\n')
    return '''Tu es l’assistant **Méthode Palambur** : tu transformes une demande métier sous-spécifiée en livrable prêt à l’emploi pour les **entreprises de Suisse romande**.

**Questionne AVANT de produire :**
1. Données nominatives (noms, montants, contrats) → pose d’abord UNE question binaire : anonymiser (défaut, « Client X », mention nLPD) ou conserver ? Applique le choix partout, sans hybride.
2. Si tu devrais faire %(seuil)s hypothèses conséquentes ou plus → clarifie. **Anticipe un lot de %(taille_lot)s questions au plus, mais n’en pose qu’une par message**, avec le compteur (« %(compteur)s »), choix lettrés A, B, C, D, défaut prudent et « Autre / je ne sais pas ».
Si tout est fourni → produis directement.

**Sortie, après les réponses :** ligne « Contexte retenu · … », puis bloc **Gabarit Palambur** rempli (%(blocs)s), puis bloc **Livrable**. Zéro jargon (« prompt », « hallucination ») face à l’utilisateur.
%(relecture)s
**Garde-fous suisses :** %(gf)s. Données sensibles → outil souverain seulement.

**Anti-hallucination :** n’invente jamais une loi, une CCT, un chiffre. Donnée manquante → marqueur visible %(marqueurs)s. Validation humaine obligatoire sur livrable sensible.

**Ton :** %(ton)s
''' % dict(
        seuil=r['seuil_hypotheses'],
        taille_lot=r['taille_lot'],
        compteur=r['compteur'],
        blocs=noms_blocs,
        gf=', '.join(noms_gf[:4]),
        #: les deux marqueurs que la version du 12.07 retenait · à compléter
        #: (le champ) et à vérifier (l’article de loi), pas « info manquante »
        marqueurs=' / '.join(m for m in r['marqueurs']
                             if 'COMPLÉTER' in m or 'VÉRIFIER' in m),
        ton=premieres_phrases(r['ton'], 1),
        relecture=relecture,
    )


def chapeau(cle, hotes, taille):
    """Le chapeau d’un fichier généré · les hôtes viennent de la table du README.

    Les noms d’hôtes ne sont écrits nulle part ici · le 11.10.2026 ce chapeau
    nommait encore « Agent Mistral (Le Chat) » et « Gemini Gem », deux produits
    remplacés par leurs éditeurs, pendant que `adaptations/README.md` disait le
    contraire deux dossiers plus loin. Une seule table, datée, lue par les deux.
    """
    liste = ' · '.join('**%s**' % h for h in hotes[cle_hotes(cle)])
    commun = ('> Relevé des hôtes au %s dans `adaptations/README.md` (sources officielles et '
              'ce qui reste non confirmé y sont notés).\n'
              '> Sur ces hôtes, l’assistant **est** la méthode : elle s’applique à chaque '
              'demande, sans mot déclencheur « palambur ».' % hotes['releve'])
    if cle == 'complet':
        return ('# Méthode Palambur · prompt système (version complète)\n\n'
                '> Prompt autonome, prêt à copier-coller dans un champ d’instructions large : %s.\n'
                '> Tient dans %s caractères (bloc sous le trait : %s caractères). Pour un champ '
                'borné, prendre la **version courte**.\n%s'
                % (liste, nombre(LIMITE_COMPLET), nombre(taille), commun))
    return ('# Méthode Palambur · prompt système (version courte)\n\n'
            '> Version condensée pour les champs d’instructions bornés : %s.\n'
            '> Tient dans %s caractères · copier uniquement le bloc sous le trait '
            '(%s caractères).\n%s'
            % (liste, nombre(LIMITE_COURT), nombre(taille), commun))


def cle_hotes(cle):
    return {'complet': 'complète', 'court': 'courte'}[cle]


def fabriquer(textes, limites=None, jour=None):
    """Rend {clé: (nom_fichier, contenu, taille_du_bloc)} ou refuse `taille`.

    `limites` et `jour` existent pour l’épreuve · on serre la limite pour voir
    le refus, on fige le jour pour comparer deux fabrications.
    """
    limites = limites or {k: v[1] for k, v in PRODUITS.items()}
    jour = jour or date.today().isoformat()
    r = extraire(textes)
    blocs = {'complet': rediger_complet(r), 'court': rediger_court(r)}
    produits = {}
    for cle, (nom, _) in PRODUITS.items():
        bloc = courber(blocs[cle]).strip() + '\n'
        taille = len(bloc)
        if taille > limites[cle]:
            raise Refus('taille', '%s · le bloc à coller fait %d caractères, '
                        'limite %d' % (nom, taille, limites[cle]))
        contenu = '\n'.join([
            ENTETE % (jour, empreinte(textes)),
            '',
            chapeau(cle, r['hotes'], taille),
            '',
            '---',
            '',
            bloc,
        ])
        produits[cle] = (nom, contenu, taille)
    return produits


def corps_sans_date(contenu):
    """Tout sauf la ligne d’en-tête datée · ce que le contrôle compare.

    Deux fabrications à deux dates différentes ne diffèrent que par la date ·
    la comparer ferait rougir le contrôle tous les matins, et un contrôle qui
    rougit sans raison finit par ne plus être lu.
    """
    return contenu.split('\n', 1)[1] if '\n' in contenu else ''


def empreinte_declaree(contenu):
    """L’empreinte écrite dans l’en-tête d’un fichier généré, ou None."""
    m = re.search(r'empreinte sha256 courte ([0-9a-f]{12})', contenu.split('\n', 1)[0])
    return m.group(1) if m else None


def motif_a_poser(ancien, contenu, emp):
    """Pourquoi un fichier sur le disque doit être réécrit, ou None s’il est à jour.

    Deux motifs, et le second a manqué le 11.10.2026 · une autre session avait
    retouché SKILL.md dans une partie que le générateur n’extrait pas. Le corps
    fabriqué était identique à l’octet, le générateur a dit « inchangé » et n’a
    rien écrit · l’en-tête gardait l’ancienne empreinte, et `controle.py`
    rougissait en demandant de relancer un générateur qui répondait que tout
    était à jour. L’empreinte déclarée se compare donc à part du corps.
    """
    if corps_sans_date(ancien) != corps_sans_date(contenu):
        return 'corps'
    if empreinte_declaree(ancien) != emp:
        return 'empreinte'
    return None


# ---------------------------------------------------------------------------
# Les deux modes · à blanc, puis --ecrire
# ---------------------------------------------------------------------------

def principal(ecrire, depot=DEPOT):
    """À blanc ou en écriture · `depot` permet de viser une copie (`--source`), à blanc seulement."""
    skill = os.path.join(depot, 'skills', 'palambur-method')
    adaptations = os.path.join(depot, 'adaptations')
    textes = lire_sources(skill, adaptations)
    produits = fabriquer(textes)
    print('GÉNÉRATEUR D’ADAPTATIONS · %s · empreinte des sources %s · règle typographique '
          'embarquée du %s · mode %s'
          % (depot, empreinte(textes), regle_typo.COPIE_DU, 'ÉCRITURE' if ecrire else 'à blanc'))
    print('-' * 72)
    changements = 0
    emp = empreinte(textes)
    for cle in ('complet', 'court'):
        nom, contenu, taille = produits[cle]
        chemin = os.path.join(adaptations, nom)
        ancien = io.open(chemin, encoding='utf-8').read() if os.path.isfile(chemin) else ''
        motif = motif_a_poser(ancien, contenu, emp)
        print('  %-40s bloc %5d / %d caractères · %s'
              % (nom, taille, PRODUITS[cle][1],
                 {None: 'inchangé', 'corps': 'DIFFÈRE',
                  'empreinte': 'même corps, EMPREINTE périmée'}[motif]))
        if motif is None:
            continue
        changements += 1
        if ecrire:
            io.open(chemin, 'w', encoding='utf-8').write(contenu)
            print('  %-40s écrit' % '')
        else:
            for l in difflib.unified_diff(ancien.splitlines(), contenu.splitlines(),
                                          'avant/' + nom, 'après/' + nom, lineterm='', n=1):
                print('    ' + l)
    print('-' * 72)
    if not changements:
        print('  les deux adaptations sont à jour · rien à écrire')
    elif not ecrire:
        print('  %d fichier(s) différent(s) · relancer avec --ecrire pour poser' % changements)
    return 0


# ---------------------------------------------------------------------------
# L’épreuve · chaque garde cassée sur témoin fabriqué, refus POUR SA raison
# ---------------------------------------------------------------------------

def epreuve():
    """Casse chaque garde et exige le code de refus attendu, pas un refus quelconque.

    Les témoins se FABRIQUENT dans un dossier temporaire créé et détruit ici ·
    une pièce à conviction rangée avec les sources est une pièce que quelqu’un
    peut archiver (CLAUDE.md § 4).
    """
    textes = lire_sources()
    dossier = tempfile.mkdtemp(prefix='epreuve_adaptations_')
    rouges = 0
    #: le total s’obtient en COMPTANT les lignes imprimées · la première
    #: version annonçait « 14 témoins » pour 13 lignes, un libellé que rien ne
    #: vérifiait (CLAUDE.md § 5)
    joues = []

    def dire(ok, nom, attendu, vu):
        nonlocal rouges
        rouges += 0 if ok else 1
        joues.append(nom)
        print('  %-8s %-58s attendu %-10s vu %s'
              % ('conforme' if ok else 'ÉCHEC', nom, attendu, vu))

    def temoin(nom, modif):
        """Une copie des sources dans la disposition du dépôt, une seule modifiée par `modif(texte)`.

        Rend le dossier du skill de la copie · `lire_sources(d)` retrouve
        `adaptations/README.md` deux niveaux plus haut, comme dans le dépôt.
        """
        racine = os.path.join(dossier, nom)
        d = os.path.join(racine, 'skills', 'palambur-method')
        os.makedirs(d)
        os.makedirs(os.path.join(racine, 'adaptations'))
        for n in SOURCES:
            t = textes[n]
            if n == modif[0]:
                t = modif[1](t)
            io.open(os.path.join(racine, n) if n == SOURCE_HOTES else os.path.join(d, n),
                    'w', encoding='utf-8').write(t)
        return d

    def attendu(nom, fonction, raison):
        try:
            fonction()
            vu = 'aucun refus'
        except Refus as e:
            vu = e.raison
        dire(vu == raison, nom, raison, vu)

    def sain(nom, fonction):
        try:
            fonction()
            ok = True
        except Refus:
            ok = False
        dire(ok, nom, 'passe', 'passe' if ok else 'refus')

    print('ÉPREUVE · témoins fabriqués, chaque garde refuse POUR SA raison')
    print('-' * 72)
    try:
        sain('les sources réelles passent', lambda: fabriquer(textes))

        # (a) dépassement de taille · on serre la limite, le texte ne change pas
        attendu('un bloc complet au-dessus de la limite est refusé',
                lambda: fabriquer(textes, {'complet': 100, 'court': LIMITE_COURT}), 'taille')
        attendu('un bloc court au-dessus de la limite est refusé',
                lambda: fabriquer(textes, {'complet': LIMITE_COMPLET, 'court': 100}), 'taille')

        # (b) le mot interdit dans une source
        d = temoin('pme', ('protection-donnees.md',
                           lambda t: t.replace('entreprises', 'P' + 'ME', 1)))
        attendu('le mot interdit dans une source est refusé',
                lambda: lire_sources(d), 'pme')
        d = temoin('pme_mot_entier', ('SKILL.md', lambda t: t + '\nLa P' + 'MEUBLE SA.\n'))
        sain('un mot qui CONTIENT les trois lettres n’est pas le mot',
             lambda: lire_sources(d))

        # (c) l’empreinte change si la source change
        d = temoin('empreinte', ('methode-palambur.md', lambda t: t.replace('5 blocs', '5 blocs ', 1)))
        change = empreinte(lire_sources(d)) != empreinte(textes)
        dire(change, 'une espace de plus dans une source change l’empreinte',
             'différente', 'différente' if change else 'IDENTIQUE')
        meme = empreinte(lire_sources(SKILL)) == empreinte(textes)
        dire(meme, 'relire les mêmes sources rend la même empreinte',
             'identique', 'identique' if meme else 'DIFFÉRENTE')

        # (d) le skill qui change de forme
        d = temoin('structure', ('methode-palambur.md',
                                 lambda t: t.replace('## Garde-fous suisses', '## Garde-feux')))
        attendu('une section disparue est refusée pour sa structure',
                lambda: fabriquer(lire_sources(d)), 'structure')
        #: TOUTES les occurrences · le fichier écrit aussi « Question 1 sur 2 » et
        #: « Question 1 sur 3 », qui satisferaient la garde si on n’effaçait que le 4
        d = temoin('compteur', ('SKILL.md', lambda t: re.sub(r'Question 1 sur \d+', 'Q1', t)))
        attendu('le compteur disparu est refusé pour sa structure',
                lambda: fabriquer(lire_sources(d)), 'structure')
        d = temoin('lot', ('SKILL.md', lambda t: re.sub(r'^## Étape 2.*$', '## Étape 2 · Clarifier',
                                                        t, count=1, flags=re.M)))
        attendu('un titre d’Étape 2 sans taille de lot est refusé',
                lambda: fabriquer(lire_sources(d)), 'structure')
        d = temoin('source', ('SKILL.md', lambda t: t))
        os.remove(os.path.join(d, 'protection-donnees.md'))
        attendu('une source manquante est refusée comme source',
                lambda: lire_sources(d), 'source')
        #: la 4e case des niveaux · le prompt du 11.10 a rendu « ; aucune. »
        d = temoin('niveau_tronque', ('methode-palambur.md', lambda t: re.sub(
            r'^(\| \*\*S\*\* \|[^|]*\|[^|]*\|)[^|]*\|', r'\1 aucune. |', t, count=1, flags=re.M)))
        attendu('une cadence de niveau tronquée (« aucune. ») est refusée',
                lambda: fabriquer(lire_sources(d)), 'structure')
        #: la ligne de contexte et le zéro jargon (11.10 au soir) · chacun a sa
        #: raison de refus, cassée ici exprès
        d = temoin('contexte', ('SKILL.md', lambda t: t.replace('`Contexte retenu · ', '`Contexte · ')))
        attendu('un SKILL.md sans la forme fixe « Contexte retenu · » est refusé',
                lambda: fabriquer(lire_sources(d)), 'structure')
        d = temoin('jargon', ('SKILL.md', lambda t: t.replace('**Zéro jargon face à l’utilisateur**',
                                                              '**Zéro mot technique**')))
        attendu('un SKILL.md sans la règle « Zéro jargon » est refusé',
                lambda: fabriquer(lire_sources(d)), 'structure')
        #: l’apostrophe courbe dans un titre n’est pas un changement de forme
        d = temoin('apostrophe', ('methode-palambur.md', lambda t: t.replace('’', "'")))
        sain('un skill à l’apostrophe droite passe comme à la courbe',
             lambda: fabriquer(lire_sources(d)))
        #: les renvois vers des fichiers du skill ne sortent pas du skill
        p0 = fabriquer(textes, jour='2026-01-01')
        sans = all('.md`)' not in p0[k][1].split('\n---\n', 1)[1] for k in p0)
        dire(sans, 'aucun renvoi « (voir `x.md`) » dans les blocs à coller',
             'aucun', 'aucun' if sans else 'PRÉSENT')

        # (d bis) la table des hôtes
        d = temoin('hotes_absents', (SOURCE_HOTES,
                                     lambda t: t.replace('## Où coller le prompt', '## Ailleurs')))
        attendu('une table des hôtes disparue est refusée pour sa structure',
                lambda: fabriquer(lire_sources(d)), 'structure')
        d = temoin('hotes_sans_date', (SOURCE_HOTES,
                                       lambda t: re.sub(r'relevé le \*\*[\d.]+\*\*', 'relevé', t)))
        attendu('une table des hôtes sans date de relevé est refusée',
                lambda: fabriquer(lire_sources(d)), 'structure')
        d = temoin('hotes_renomme', (SOURCE_HOTES,
                                     lambda t: t.replace('| Claude · Projet', '| Hôte témoin', 1)))
        renomme = 'Hôte témoin' in fabriquer(lire_sources(d), jour='2026-01-01')['complet'][1]
        dire(renomme, 'un hôte renommé dans la table change le chapeau',
             'présent', 'présent' if renomme else 'ABSENT')

        # (e) deux fabrications le même jour rendent le même texte
        p1 = fabriquer(textes, jour='2026-01-01')
        p2 = fabriquer(textes, jour='2026-01-01')
        stable = all(p1[k][1] == p2[k][1] for k in p1)
        dire(stable, 'deux fabrications rendent le même texte',
             'identique', 'identique' if stable else 'DIFFÉRENT')

        # (f) le corps comparé ignore la date, pas le contenu
        p3 = fabriquer(textes, jour='2026-01-02')
        meme_corps = corps_sans_date(p1['court'][1]) == corps_sans_date(p3['court'][1])
        dire(meme_corps, 'la date seule ne fait pas un corps différent',
             'identique', 'identique' if meme_corps else 'DIFFÉRENT')
        autre_corps = corps_sans_date(p1['court'][1]) != corps_sans_date(
            p1['court'][1].replace('Gabarit Palambur', 'Gabarit'))
        dire(autre_corps, 'un mot changé dans le corps fait un corps différent',
             'différent', 'différent' if autre_corps else 'IDENTIQUE')
        declaree = empreinte_declaree(p1['court'][1]) == empreinte(textes)
        dire(declaree, 'l’en-tête déclare l’empreinte des sources',
             'identique', 'identique' if declaree else 'DIFFÉRENTE')

        # (g) ce qui décide d’écrire · le corps, OU l’empreinte seule
        emp = empreinte(textes)
        court = p1['court'][1]
        for nom, ancien, voulu in (
                ('un fichier identique n’est pas à poser', court, None),
                ('un corps différent est à poser pour son corps',
                 court.replace('Gabarit Palambur', 'Gabarit'), 'corps'),
                ('une empreinte périmée seule est à poser pour son empreinte',
                 court.replace(emp, '0' * 12), 'empreinte'),
                ('un fichier absent est à poser pour son corps', '', 'corps')):
            vu = motif_a_poser(ancien, court, emp)
            dire(vu == voulu, nom, str(voulu), str(vu))
    finally:
        shutil.rmtree(dossier)

    print('-' * 72)
    if rouges:
        print('  %d témoin(s) en échec sur %d · le générateur ne fait pas ce qu’il dit.'
              % (rouges, len(joues)))
        return 1
    print('  %d témoins · le générateur sait dire oui ET non.' % len(joues))
    return 0


if __name__ == '__main__':
    try:
        if '--epreuve' in sys.argv:
            sys.exit(epreuve())
        depot = DEPOT
        if '--source' in sys.argv:
            #: une copie du dépôt, À BLANC seulement · on n’écrit pas chez un
            #: autre depuis ici
            depot = os.path.abspath(sys.argv[sys.argv.index('--source') + 1])
            if '--ecrire' in sys.argv:
                print('REFUS (source) · --source ne s’écrit pas, il se regarde')
                sys.exit(1)
        sys.exit(principal('--ecrire' in sys.argv, depot))
    except Refus as e:
        print('REFUS (%s) · %s' % (e.raison, e))
        sys.exit(1)
