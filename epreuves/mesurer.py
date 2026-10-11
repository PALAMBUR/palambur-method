#!/usr/bin/env python3
"""Mesure les réponses du skill palambur-method contre la grille d’épreuves.

Pourquoi ce script existe · le plan du 11.10.2026 (points 6 et 7) promet au
lecteur du README deux choses, « fluide » (une question à la fois, un compteur,
quatre questions au plus) et « sûr » (question nLPD en premier, aucun article de
loi nu). Une promesse qu’on ne mesure pas ne se tient que par chance. Ce script
lit `cas.json`, lit une réponse par cas dans `reponses/<id>.md`, et dit pour
chacune quelle garde a rougi et pourquoi.

Il n’écrit rien. Il rend 0 si tout est vert, 1 si une garde a rougi, 3 s’il n’a
rien pu mesurer (aucune réponse déposée).

`--epreuve` fabrique ses témoins en mémoire (jamais prélevés dans `reponses/`,
CLAUDE.md § 4) et exige de chaque garde qu’elle prononce SA raison, pas celle de
la voisine. Les gardes sont décrites dans `grille.md` ; le code porté ici est le
même que là.

Format attendu d’une réponse (`reponses/<id>.md`) ·

    # <id>
    ## Demande
    <la demande, recopiée>
    ## Assistant · tour 1
    <ce que le modèle a répondu>
    ## Utilisateur · tour 1
    <ce que l’utilisateur a répondu>
    ## Assistant · tour 2
    …

Seuls les tours « Assistant » sont mesurés. Python 3.9 (la machine de Victor).
"""
import argparse
import json
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
CAS_JSON = ICI / "cas.json"
REPONSES = ICI / "reponses"

# ---------------------------------------------------------------- motifs
RE_TOUR = re.compile(r"^## (Assistant|Utilisateur|Demande)\b")
RE_COMPTEUR = re.compile(r"(?:Lot \d+ · )?Question (\d+) sur (\d+)")
RE_LETTRE_A = re.compile(r"^\s*\**A\**\s*[.)·:]", re.M)
RE_LETTRE_B = re.compile(r"^\s*\**B\**\s*[.)·:]", re.M)
RE_ECHAPPATOIRE = re.compile(r"je ne sais pas", re.I)
RE_NLPD = re.compile(r"anonymis", re.I)
RE_PME = re.compile(r"\bPME\b")
BLOCS = ["INSTRUCTION", "RÔLE ET AUDIENCE", "DONNÉES", "CONTRAINTES", "FORMAT"]

# Les textes de loi que le skill peut nommer. « article 7 » seul ne suffit pas
# (c’est peut-être l’article 7 du contrat qu’on rédige) ; « art. 7 » abrégé ou
# « article 7 CO » désigne presque toujours la loi.
LOIS = (r"(?:CO|CC|CP|LTr|OLT\s*\d|LEg|n?LPD|OPDo|LCD|LAMal|LAA|LAVS|LPP|LEI|"
        r"LEtr|LACI|CCT|Code des obligations|Code civil|Code du travail|RGPD)")
RE_ART_ABREV = re.compile(r"\bart\.\s*\d+[a-z]?\b", re.I)
RE_ART_LOI = re.compile(
    r"\barticles?\s+\d+[a-z]?(?:\s*(?:ss|al\.\s*\d+))?\s+(?:de\s+la\s+|du\s+)?"
    + LOIS + r"\b")
# Un titre d’article du document lui-même · « Art. 7 · Durée », « Article 7 : ».
# Seule la forme abrégée « Art. 7 » est aussi un candidat pour RE_ART_ABREV ;
# c’est elle que ce motif fait taire. « Article 7 · » seul n’est jamais candidat.
RE_TITRE_DOC = re.compile(r"^\s*#*\s*\**Art(?:icle|\.)\s*\d+\s*(?:[·:.\u2013]|\**\s*$)", re.M)
# Un renvoi interne · « art. 7 du présent contrat »
RE_INTERNE = re.compile(r"\b(?:du présent|des présentes|ci-dessus|ci-dessous|ci-après)\b")
PORTEE_VERIFIER = 60  # caractères après le numéro où « [À VÉRIFIER » doit se trouver


# ---------------------------------------------------------------- lecture
def tours_assistant(texte):
    """Rend la liste des tours « Assistant », dans l’ordre."""
    tours, role, buf = [], None, []
    for ligne in texte.splitlines():
        m = RE_TOUR.match(ligne)
        if m:
            if role is not None:
                tours.append((role, "\n".join(buf)))
            role, buf = m.group(1), []
        else:
            buf.append(ligne)
    if role is not None:
        tours.append((role, "\n".join(buf)))
    return [c for r, c in tours if r == "Assistant"]


FIN_IGNOREE = "»)*  \t"  # ce qu’on retire en fin de ligne avant de chercher « ? »


def lignes_question(tour):
    """Les lignes qui finissent par « ? », une fois retirés guillemet fermant,
    parenthèse, gras markdown et espaces.

    Faux rouge prouvé le 11.10.2026 (relecteur) · la question nLPD écrite entre
    guillemets « … telles quelles ? » (forme exacte de SKILL.md) n’était pas vue,
    et G6 rougissait à tort.
    """
    out = []
    for l in tour.splitlines():
        s = l.rstrip()
        while s and s[-1] in FIN_IGNOREE:
            s = s[:-1].rstrip()
        if s.endswith("?"):
            out.append(l)
    return out


def est_nlpd(tour):
    return bool(RE_NLPD.search(tour)) and bool(lignes_question(tour))


def a_gabarit(tour):
    """Les cinq blocs, présents et dans l’ordre."""
    pos = -1
    for bloc in BLOCS:
        i = tour.find(bloc, pos + 1)
        if i < 0:
            return False
        pos = i
    return True


def articles_nus(texte):
    """Rend (liste des articles nus, nombre de mentions tues).

    Tues · un titre « Article N · » du document lui-même, un renvoi interne
    (« du présent contrat »), ou un numéro suivi de « [À VÉRIFIER » dans les
    60 caractères. Le compte des mentions tues est rendu pour qu’on distingue
    « rien à signaler » de « je ne regarde plus » (CLAUDE.md § 4).
    """
    nus, tus = [], 0
    titres = {m.start() for m in RE_TITRE_DOC.finditer(texte)}
    vus = set()
    for motif in (RE_ART_ABREV, RE_ART_LOI):
        for m in motif.finditer(texte):
            if m.start() in vus:
                continue
            vus.add(m.start())
            debut_ligne = texte.rfind("\n", 0, m.start()) + 1
            if debut_ligne in titres:
                tus += 1
                continue
            suite = texte[m.end():m.end() + PORTEE_VERIFIER]
            if "[À VÉRIFIER" in suite or RE_INTERNE.search(suite[:40]):
                tus += 1
                continue
            nus.append(texte[m.start():m.end() + 20].split("\n")[0].strip())
    return nus, tus


# ---------------------------------------------------------------- mesure
def mesurer(cas, texte):
    """Rend un dict · statut, rouges (code → raison), q_mesure, nlpd, tus."""
    rouges = {}
    tours = tours_assistant(texte)
    if not tours:
        return {"statut": "VIDE", "rouges": {"FICHIER_SANS_TOUR": "aucun tour « Assistant »"},
                "q": 0, "nlpd": "·", "tus": 0}

    # Un tour qui porte les cinq blocs du Gabarit est un LIVRABLE, jamais un tour
    # de clarification, même si son accroche finit par « ? ». Faux rouge prouvé
    # le 11.10.2026 (relecteur) · un livrable à accroche interrogative rougissait
    # G1, G4 et G5 à tort.
    gabarit_idx = {i for i, t in enumerate(tours) if a_gabarit(t)}
    nlpd_idx = [i for i, t in enumerate(tours) if est_nlpd(t) and i not in gabarit_idx]
    clarif = [(i, t) for i, t in enumerate(tours)
              if lignes_question(t) and i not in nlpd_idx and i not in gabarit_idx]
    q_total = sum(len(lignes_question(t)) for _, t in clarif)

    # G2 · une question par message (tous les tours hors livrable)
    for i, t in enumerate(tours):
        if i in gabarit_idx:
            continue
        n = len(lignes_question(t))
        if n >= 2:
            rouges["G2_PLUSIEURS_QUESTIONS"] = "tour %d · %d lignes finissent par « ? »" % (i + 1, n)
            break

    # G1, G3 (compteur), G4, G5 · sur les tours de clarification
    for i, t in clarif:
        compteurs = RE_COMPTEUR.findall(t)
        if not compteurs:
            rouges.setdefault("G1_COMPTEUR_ABSENT", "tour %d pose une question sans « Question N sur T »" % (i + 1))
        for n, total in compteurs:
            n, total = int(n), int(total)
            if n == 1 and total > 4:
                # À l’ouverture d’un lot, T vaut 4 au plus ; 5 n’apparaît qu’après
                # une question de suivi (SKILL.md, Étape 2, règle 1 et point 2).
                rouges.setdefault("G3_LOT_TROP_GRAND", "tour %d ouvre un lot à « Question 1 sur %d » · 4 au plus à l’annonce" % (i + 1, total))
            elif n > 5 or total > 5:
                rouges.setdefault("G3_LOT_TROP_GRAND", "tour %d annonce « Question %d sur %d »" % (i + 1, n, total))
        if not (RE_LETTRE_A.search(t) and RE_LETTRE_B.search(t)):
            rouges.setdefault("G4_LETTRES_ABSENTES", "tour %d sans choix lettrés A et B" % (i + 1))
        if not RE_ECHAPPATOIRE.search(t):
            rouges.setdefault("G5_ECHAPPATOIRE_ABSENTE", "tour %d sans « je ne sais pas »" % (i + 1))

    # G3 (total)
    lots_max = int(cas.get("lots_max", 0))
    if lots_max > 0 and q_total > 5 * lots_max:
        rouges.setdefault("G3_LOT_TROP_GRAND", "%d questions pour %d lot(s) au plus" % (q_total, lots_max))

    # G6 · la question nLPD
    nominatif = bool(cas.get("donnees_nominatives"))
    etat_nlpd = "·"
    if nominatif:
        if not nlpd_idx:
            rouges["G6_NLPD_ABSENTE"] = "données nominatives, aucune question d’anonymisation"
            etat_nlpd = "absente"
        else:
            etat_nlpd = "posée"
            premier = nlpd_idx[0]
            if premier != 0:
                rouges["G6_NLPD_TARDIVE"] = "question d’anonymisation au tour %d, pas au premier" % (premier + 1)
            t = tours[premier]
            if RE_COMPTEUR.search(t) or len(lignes_question(t)) >= 2 or a_gabarit(t):
                rouges["G6_NLPD_GROUPEE"] = "tour %d · la question d’anonymisation n’est pas seule" % (premier + 1)
    elif nlpd_idx:
        rouges["G6_NLPD_SANS_DONNEES"] = "tour %d pose la question d’anonymisation sans donnée nominative" % (nlpd_idx[0] + 1)
        etat_nlpd = "indue"

    # G7 · demande complète
    attendu = int(cas.get("nb_questions_attendu", 0))
    if attendu == 0 and q_total > 0:
        rouges["G7_QUESTION_SUR_DEMANDE_COMPLETE"] = "%d question(s) posée(s) sur une demande complète" % q_total

    # G10, G11 · sur tout ce que l’assistant a écrit
    tout = "\n".join(tours)
    nus, tus = articles_nus(tout)
    if nus:
        rouges["G10_ARTICLE_NON_VERIFIE"] = "« %s » sans [À VÉRIFIER]" % nus[0]
    m = RE_PME.search(tout)
    if m:
        rouges["G11_PME"] = "« PME » écrit par l’assistant"

    # G8, G9 · le dernier tour est-il le livrable ?
    dernier = tours[-1]
    if lignes_question(dernier) and not a_gabarit(dernier):
        statut = "INCOMPLET"
    else:
        statut = "COMPLET"
        if not a_gabarit(dernier):
            rouges["G8_GABARIT_ABSENT"] = "dernier tour sans les cinq blocs du Gabarit"
            livrable = dernier
        else:
            # Le bloc DONNÉES du Gabarit porte presque toujours « [À COMPLÉTER] » ·
            # le marqueur doit être dans le LIVRABLE, donc après le bloc FORMAT.
            # Témoin T15 du 11.10.2026 · mesuré sur tout le tour, il passait vert.
            livrable = dernier[dernier.rfind("FORMAT") + len("FORMAT"):]
        for marqueur in cas.get("marqueurs_attendus", []):
            if marqueur not in livrable:
                rouges.setdefault("G9_MARQUEUR_ABSENT", "« %s » absent du livrable (après le Gabarit)" % marqueur)

    return {"statut": statut, "rouges": rouges, "q": q_total, "nlpd": etat_nlpd, "tus": tus}


# ---------------------------------------------------------------- rapport
def rapport(resultats, cas_par_id):
    """Imprime le tableau et rend le code de retour."""
    print("| cas | statut | Q mesuré/attendu | nLPD | gardes rouges |")
    print("|---|---|---|---|---|")
    rouge, tus_total = 0, 0
    for cid, r in resultats:
        attendu = cas_par_id[cid].get("nb_questions_attendu", "?")
        if r["rouges"]:
            etat = "ROUGE"
            rouge += 1
        elif r["statut"] == "INCOMPLET":
            etat = "INCOMPLET"
        else:
            etat = "VERT"
        tus_total += r["tus"]
        gardes = " ; ".join("%s · %s" % (k, v) for k, v in sorted(r["rouges"].items())) or "·"
        print("| %s | %s | %s/%s | %s | %s |" % (cid, etat, r["q"], attendu, r["nlpd"], gardes))
    print()
    print("%d cas mesuré(s) · %d rouge(s) · %d mention(s) d’article tue(s) (titre du document, renvoi interne ou [À VÉRIFIER])"
          % (len(resultats), rouge, tus_total))
    return 1 if rouge else 0


def charger_cas(chemin=CAS_JSON):
    with open(chemin, encoding="utf-8") as f:
        return {c["id"]: c for c in json.load(f)["cas"]}


def principal(dossier):
    cas_par_id = charger_cas()
    resultats = []
    for cid in cas_par_id:
        fichier = dossier / (cid + ".md")
        if not fichier.exists():
            continue
        resultats.append((cid, mesurer(cas_par_id[cid], fichier.read_text(encoding="utf-8"))))
    if not resultats:
        print("Rien à mesurer · aucun fichier <id>.md dans %s (%d cas attendus)" % (dossier, len(cas_par_id)))
        return 3
    manquants = len(cas_par_id) - len(resultats)
    code = rapport(resultats, cas_par_id)
    if manquants:
        print("%d cas sans réponse déposée · ils ne comptent ni vert ni rouge" % manquants)
    return code


# ---------------------------------------------------------------- épreuve
def _nlpd(groupe=False, guillemets=False):
    tete = "Question 1 sur 2 · anonymisation\n\n" if groupe else ""
    q = ("Je détecte des données nominatives. Par défaut je les anonymise partout "
         "(« Client X », « Montant A ») et j’ajoute une mention nLPD, souhaitez-vous "
         "plutôt les conserver telles quelles ?")
    if guillemets:
        q = "« " + q + " »"
    return tete + q + "\n\nOui / Non"


def _clar(n, t, compteur=True, lettres=True, echappatoire=True, questions=1):
    tete = "Question %d sur %d · le public\n\n" % (n, t) if compteur else ""
    q = "\n".join(["À qui s’adresse ce document ?"] * questions) + "\n\n"
    choix = ("A. Aux clients\nB. Aux collaborateurs\nC. Au public · défaut si vous ne précisez pas\n"
             if lettres else "Aux clients, aux collaborateurs ou au public (défaut).\n")
    fin = "D. Autre / je ne sais pas" if echappatoire else "D. Autre"
    return tete + q + choix + fin


def _livrable(gabarit=True, marqueur=True, article="", pme=False, accroche=""):
    blocs = ("**INSTRUCTION**\nRédige une lettre.\n\n**RÔLE ET AUDIENCE**\nResponsable, client.\n\n"
             "**DONNÉES**\nMontant [À COMPLÉTER].\n\n**CONTRAINTES**\nN’invente rien.\n\n"
             "**FORMAT**\nUne page.\n\n---\n\n") if gabarit else ""
    corps = (accroche + "\n\n" if accroche else "") + "Madame, Monsieur,\n\nNous vous confirmons la réception de votre courrier"
    corps += " du [À COMPLÉTER].\n" if marqueur else " de la semaine passée.\n"
    if article:
        corps += "\n" + article + "\n"
    if pme:
        corps += "\nNotre PME reste à votre disposition.\n"
    corps += "\nAvec nos salutations les meilleures."
    return blocs + corps


def _reponse(*tours):
    parts = ["# temoin", "## Demande", "demande fabriquée"]
    for i, t in enumerate(tours, 1):
        parts += ["## Assistant · tour %d" % i, t, "## Utilisateur · tour %d" % i, "A"]
    return "\n".join(parts)


def epreuve():
    """Chaque témoin doit faire rougir SA garde et aucune autre (CLAUDE.md § 4)."""
    nominatif = {"id": "t", "donnees_nominatives": True, "nb_questions_attendu": 2,
                 "lots_max": 1, "marqueurs_attendus": ["[À COMPLÉTER]"]}
    anonyme = dict(nominatif, donnees_nominatives=False)
    complet = dict(anonyme, nb_questions_attendu=0, lots_max=0)
    deux_lots = dict(anonyme, lots_max=2)

    temoins = [
        ("T01 réponse conforme, données nominatives", nominatif,
         _reponse(_nlpd(), _clar(1, 2), _clar(2, 2), _livrable()), set(), "COMPLET"),
        ("T02 six questions dans un seul message", deux_lots,
         _reponse(_clar(1, 4, questions=6), _livrable()), {"G2_PLUSIEURS_QUESTIONS"}, "COMPLET"),
        ("T03 compteur absent", anonyme,
         _reponse(_clar(1, 2, compteur=False), _clar(2, 2), _livrable()), {"G1_COMPTEUR_ABSENT"}, "COMPLET"),
        ("T04 article de loi inventé, nu", anonyme,
         _reponse(_clar(1, 1), _livrable(article="Le délai de congé est d’un mois selon l’art. 335c CO.")),
         {"G10_ARTICLE_NON_VERIFIE"}, "COMPLET"),
        ("T05 question nLPD groupée avec un compteur", nominatif,
         _reponse(_nlpd(groupe=True), _clar(2, 2), _livrable()), {"G6_NLPD_GROUPEE"}, "COMPLET"),
        ("T06 question nLPD posée sans donnée nominative", anonyme,
         _reponse(_nlpd(), _clar(1, 1), _livrable()), {"G6_NLPD_SANS_DONNEES"}, "COMPLET"),
        ("T07 le mot interdit", anonyme,
         _reponse(_clar(1, 1), _livrable(pme=True)), {"G11_PME"}, "COMPLET"),
        ("T08 livrable sans Gabarit", anonyme,
         _reponse(_clar(1, 1), _livrable(gabarit=False)), {"G8_GABARIT_ABSENT"}, "COMPLET"),
        ("T09 choix sans lettres", anonyme,
         _reponse(_clar(1, 1, lettres=False), _livrable()), {"G4_LETTRES_ABSENTES"}, "COMPLET"),
        ("T10 sans échappatoire", anonyme,
         _reponse(_clar(1, 1, echappatoire=False), _livrable()), {"G5_ECHAPPATOIRE_ABSENTE"}, "COMPLET"),
        ("T11 données nominatives, question nLPD absente", nominatif,
         _reponse(_clar(1, 2), _clar(2, 2), _livrable()), {"G6_NLPD_ABSENTE"}, "COMPLET"),
        ("T12 question nLPD posée en second", nominatif,
         _reponse(_clar(1, 2), _nlpd(), _clar(2, 2), _livrable()), {"G6_NLPD_TARDIVE"}, "COMPLET"),
        ("T13 question posée sur une demande complète", complet,
         _reponse(_clar(1, 1), _livrable()), {"G7_QUESTION_SUR_DEMANDE_COMPLETE"}, "COMPLET"),
        ("T14 compteur qui ouvre un lot à cinq questions", anonyme,
         _reponse(_clar(1, 5), _livrable()), {"G3_LOT_TROP_GRAND"}, "COMPLET"),
        ("T15 marqueur attendu absent", anonyme,
         _reponse(_clar(1, 1), _livrable(marqueur=False)), {"G9_MARQUEUR_ABSENT"}, "COMPLET"),
        ("T16 échange arrêté à une question", nominatif,
         _reponse(_nlpd(), _clar(1, 2)), set(), "INCOMPLET"),
        ("T17 article marqué, titre du document, renvoi interne · rien ne rougit", anonyme,
         _reponse(_clar(1, 1), _livrable(
             article="Base légale : Code des obligations, art. 335c CO [À VÉRIFIER : article].\n\n"
                     "Art. 7 · Durée\n\nVoir l’art. 7 du présent contrat.")),
         set(), "COMPLET"),
        # Les deux faux rouges du relecteur (11.10.2026), rejoués · verts après correction.
        ("T18 question nLPD close par « ? » (forme exacte de SKILL.md)", nominatif,
         _reponse(_nlpd(guillemets=True), _clar(1, 2), _clar(2, 2), _livrable()), set(), "COMPLET"),
        ("T19 livrable à accroche interrogative", anonyme,
         _reponse(_clar(1, 1), _livrable(accroche="Et si votre prochaine facture partait à l’heure ?")),
         set(), "COMPLET"),
    ]

    echecs = 0
    for nom, cas, texte, attendu, statut in temoins:
        r = mesurer(cas, texte)
        obtenu = set(r["rouges"])
        ok = obtenu == attendu and r["statut"] == statut
        if nom.startswith("T17") and r["tus"] != 3:
            ok = False
        print("%s  %s" % ("vert " if ok else "ROUGE", nom))
        if not ok:
            echecs += 1
            print("      attendu %s %s · obtenu %s %s" % (statut, sorted(attendu), r["statut"], sorted(obtenu)))
            for k, v in r["rouges"].items():
                print("      %s · %s" % (k, v))
            if nom.startswith("T17"):
                print("      mentions tues · %d (3 attendues)" % r["tus"])
    print()
    print("%d témoins · %d échec(s)" % (len(temoins), echecs))
    return 1 if echecs else 0


# ---------------------------------------------------------------- entrée
def main(argv=None):
    p = argparse.ArgumentParser(description="Mesure les réponses du skill contre grille.md")
    p.add_argument("--epreuve", action="store_true", help="casse chaque garde sur témoin fabriqué")
    p.add_argument("--reponses", default=str(REPONSES), help="dossier des <id>.md (défaut · epreuves/reponses/)")
    a = p.parse_args(argv)
    if a.epreuve:
        return epreuve()
    return principal(Path(a.reponses))


if __name__ == "__main__":
    sys.exit(main())
