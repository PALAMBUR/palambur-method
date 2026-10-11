#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palambur · le relevé hebdomadaire du dépôt public `PALAMBUR/palambur-method`.

Pourquoi ce fichier existe · le plan en 30 points du 11.10.2026 (point 27)
dit : « sans mesure, "viral" reste un mot ». Le constat de départ du même
plan a été relevé à la main (`gh repo view`, `gh api …/traffic`), et un
chiffre relevé à la main n'a ni date fiable ni lendemain. Ce script pose
UNE ligne datée par relevé dans `mesures/releves.csv`, et c'est cette table
qui fait foi, pas un nombre recopié dans un `.md`.

Ce qu'il relève, en LECTURE SEULE sur GitHub (`gh api`, jamais d'écriture) ·
    étoiles, forks            ← repos/PALAMBUR/palambur-method
    vues, vues uniques        ← …/traffic/views   (14 derniers jours)
    clones, clones uniques    ← …/traffic/clones  (14 derniers jours)

Idempotence · relancé le même jour, il REMPLACE la ligne du jour au lieu
d'en ajouter une. Un relevé hebdomadaire qu'on relance deux fois le lundi ne
doit pas compter double, sinon la courbe ment dès la deuxième semaine.

Les deux chiffres de trafic sont des fenêtres glissantes de 14 jours : deux
relevés à sept jours d'écart se recouvrent à moitié. On les garde tels que
GitHub les rend, on ne les cumule jamais.

    python3 outils/mesure.py             # relève et écrit la ligne du jour
    python3 outils/mesure.py --a-blanc   # relève, affiche, n'écrit rien
    python3 outils/mesure.py --epreuve   # témoins fabriqués, GitHub jamais appelé

Règle 4 de `CLAUDE.md` · un contrôle vert ne vaut que si on l'a fait rougir.
L'épreuve n'appelle jamais GitHub : elle fabrique ses témoins (une réponse
API inventée, un fichier CSV temporaire) et exige de chaque garde SA raison,
pas seulement un refus.
"""

import argparse
import csv
import datetime as _dt
import json
import os
import subprocess
import sys
import tempfile

DEPOT = "PALAMBUR/palambur-method"
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
CSV_PAR_DEFAUT = os.path.join(RACINE, "mesures", "releves.csv")

# L'ordre des colonnes est un contrat · `mesures/README.md` le décrit, et un
# lecteur (tableur, script) le lit par position. On ne le change pas sans
# changer l'en-tête ET le README.
COLONNES = ["date", "etoiles", "forks", "vues", "vues_uniques",
            "clones", "clones_uniques"]


class RefusReleve(Exception):
    """Un refus NOMMÉ · le message dit pourquoi, pour que l'épreuve puisse
    exiger la bonne raison et pas seulement « ça a refusé »."""


# ---------------------------------------------------------------- lecture

def _gh_api(chemin):
    """Appelle `gh api <chemin>` et rend le JSON. Lecture seule par
    construction : `gh api` sans `-X` ni `-f` est un GET."""
    try:
        sortie = subprocess.run(
            ["gh", "api", chemin],
            check=True, capture_output=True, text=True, timeout=60,
        ).stdout
    except FileNotFoundError:
        raise RefusReleve("gh absent · installez le CLI GitHub et connectez-vous (gh auth login)")
    except subprocess.CalledProcessError as e:
        raise RefusReleve("gh api a refusé %s · %s" % (chemin, e.stderr.strip()[:200]))
    try:
        return json.loads(sortie)
    except json.JSONDecodeError:
        raise RefusReleve("réponse non JSON pour %s" % chemin)


def relever(lire=_gh_api):
    """Rend le dict du relevé. `lire` est injectable pour l'épreuve : on
    passe une fausse fonction et GitHub n'est jamais appelé."""
    depot = lire("repos/%s" % DEPOT)
    vues = lire("repos/%s/traffic/views" % DEPOT)
    clones = lire("repos/%s/traffic/clones" % DEPOT)

    def entier(d, cle, source):
        if not isinstance(d, dict) or cle not in d:
            raise RefusReleve("champ manquant · %s dans %s" % (cle, source))
        v = d[cle]
        if not isinstance(v, int) or isinstance(v, bool) or v < 0:
            raise RefusReleve("valeur non entière ou négative · %s=%r dans %s" % (cle, v, source))
        return v

    return {
        "etoiles": entier(depot, "stargazers_count", "repos"),
        "forks": entier(depot, "forks_count", "repos"),
        "vues": entier(vues, "count", "traffic/views"),
        "vues_uniques": entier(vues, "uniques", "traffic/views"),
        "clones": entier(clones, "count", "traffic/clones"),
        "clones_uniques": entier(clones, "uniques", "traffic/clones"),
    }


# ---------------------------------------------------------------- écriture

def lire_csv(chemin):
    """Rend (lignes, en_tete_vu). Un CSV absent vaut zéro ligne. Un CSV dont
    l'en-tête ne correspond pas aux COLONNES est REFUSÉ : écrire à la suite
    d'une table qu'on ne comprend pas, c'est la rendre illisible pour tous."""
    if not os.path.exists(chemin):
        return [], None
    with open(chemin, newline="", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        lignes = list(lecteur)
    if not lignes:
        return [], None
    en_tete = lignes[0]
    if en_tete != COLONNES:
        raise RefusReleve("en-tête inattendu dans %s · %r" % (chemin, en_tete))
    return lignes[1:], en_tete


def poser(releve, jour, chemin=CSV_PAR_DEFAUT, a_blanc=False):
    """Pose UNE ligne pour `jour` · remplace celle du jour si elle existe
    (idempotence), sinon l'ajoute. Rend le tuple (action, ligne) où action
    vaut 'ajoutee' ou 'remplacee'. Les lignes restent triées par date."""
    lignes, _ = lire_csv(chemin)
    ligne = [jour] + [str(releve[c]) for c in COLONNES[1:]]
    deja = [l for l in lignes if l and l[0] == jour]
    action = "remplacee" if deja else "ajoutee"
    autres = [l for l in lignes if l and l[0] != jour]
    nouvelles = sorted(autres + [ligne], key=lambda l: l[0])
    if not a_blanc:
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        with open(chemin, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(COLONNES)
            w.writerows(nouvelles)
    return action, ligne


# ---------------------------------------------------------------- épreuve

def epreuve():
    """Témoins FABRIQUÉS · GitHub n'est jamais appelé. Chaque garde doit
    prononcer SA raison (règle 4, corollaire du 18.08.2026)."""
    resultats = []

    def att(nom, ok, detail=""):
        resultats.append((nom, ok, detail))

    # Un faux GitHub, cohérent, qui rend des entiers connus.
    faux = {
        "repos/%s" % DEPOT: {"stargazers_count": 7, "forks_count": 2},
        "repos/%s/traffic/views" % DEPOT: {"count": 40, "uniques": 9},
        "repos/%s/traffic/clones" % DEPOT: {"count": 120, "uniques": 100},
    }
    appels = []

    def lire_faux(chemin):
        appels.append(chemin)
        return faux[chemin]

    r = relever(lire=lire_faux)
    att("1 · le relevé lit les trois points de l'API, et rien d'autre",
        appels == ["repos/%s" % DEPOT, "repos/%s/traffic/views" % DEPOT,
                   "repos/%s/traffic/clones" % DEPOT], str(appels))
    att("2 · les six valeurs sont celles du témoin",
        r == {"etoiles": 7, "forks": 2, "vues": 40, "vues_uniques": 9,
              "clones": 120, "clones_uniques": 100}, str(r))

    # Garde · champ manquant doit refuser POUR CETTE RAISON.
    casse = dict(faux)
    casse["repos/%s/traffic/views" % DEPOT] = {"count": 40}
    try:
        relever(lire=lambda c: casse[c])
        att("3 · champ manquant refusé", False, "aucun refus")
    except RefusReleve as e:
        att("3 · champ manquant refusé pour cette raison",
            "champ manquant · uniques" in str(e), str(e))

    # Garde · valeur non entière (une chaîne, un booléen, un négatif).
    for temoin in ("12", True, -1):
        casse = dict(faux)
        casse["repos/%s" % DEPOT] = {"stargazers_count": temoin, "forks_count": 2}
        try:
            relever(lire=lambda c: casse[c])
            att("4 · valeur %r refusée" % (temoin,), False, "aucun refus")
        except RefusReleve as e:
            att("4 · valeur %r refusée pour cette raison" % (temoin,),
                "non entière ou négative" in str(e), str(e))

    # Idempotence sur un CSV temporaire fabriqué.
    with tempfile.TemporaryDirectory() as d:
        chemin = os.path.join(d, "releves.csv")
        a1, _ = poser(r, "2026-10-04", chemin)
        a2, _ = poser(r, "2026-10-11", chemin)
        r2 = dict(r, etoiles=8)
        a3, ligne3 = poser(r2, "2026-10-11", chemin)
        lignes, _ = lire_csv(chemin)
        att("5 · première ligne ajoutée, seconde ajoutée, même jour remplacé",
            (a1, a2, a3) == ("ajoutee", "ajoutee", "remplacee"), str((a1, a2, a3)))
        att("6 · deux lignes seulement, pas trois",
            len(lignes) == 2, "%d lignes" % len(lignes))
        att("7 · la ligne du 11.10 porte la nouvelle valeur 8",
            lignes[1] == ["2026-10-11", "8", "2", "40", "9", "120", "100"], str(lignes[1]))
        att("8 · les lignes sont triées par date",
            [l[0] for l in lignes] == ["2026-10-04", "2026-10-11"], str([l[0] for l in lignes]))

        # À blanc · rien n'est écrit.
        avant = open(chemin, encoding="utf-8").read()
        poser(dict(r, etoiles=99), "2026-10-18", chemin, a_blanc=True)
        apres = open(chemin, encoding="utf-8").read()
        att("9 · --a-blanc ne modifie pas le fichier", avant == apres)

        # Garde · en-tête étranger refusé POUR CETTE RAISON.
        with open(chemin, "w", encoding="utf-8") as f:
            f.write("jour,stars\n2026-10-04,1\n")
        try:
            poser(r, "2026-10-11", chemin)
            att("10 · en-tête étranger refusé", False, "aucun refus")
        except RefusReleve as e:
            att("10 · en-tête étranger refusé pour cette raison",
                "en-tête inattendu" in str(e), str(e))

    rouge = [x for x in resultats if not x[1]]
    for nom, ok, detail in resultats:
        print("  %s  %s%s" % ("VERT " if ok else "ROUGE", nom, ("  · " + detail) if (detail and not ok) else ""))
    print("%d épreuves · %d rouge(s) · GitHub jamais appelé" % (len(resultats), len(rouge)))
    return 0 if not rouge else 1


# ---------------------------------------------------------------- main

def main(argv=None):
    p = argparse.ArgumentParser(description="Relevé daté du dépôt public (lecture seule sur GitHub).")
    p.add_argument("--epreuve", action="store_true", help="témoins fabriqués, GitHub jamais appelé")
    p.add_argument("--a-blanc", action="store_true", help="relève et affiche, n'écrit rien")
    p.add_argument("--csv", default=CSV_PAR_DEFAUT, help="chemin du CSV (défaut : mesures/releves.csv)")
    p.add_argument("--date", default=None, help="date du relevé AAAA-MM-JJ (défaut : aujourd'hui)")
    a = p.parse_args(argv)

    if a.epreuve:
        return epreuve()

    jour = a.date or _dt.date.today().isoformat()
    try:
        _dt.date.fromisoformat(jour)
    except ValueError:
        print("REFUS · date invalide %r (attendu AAAA-MM-JJ)" % jour, file=sys.stderr)
        return 1

    try:
        r = relever()
        action, ligne = poser(r, jour, a.csv, a_blanc=a.a_blanc)
    except RefusReleve as e:
        print("REFUS · %s" % e, file=sys.stderr)
        return 1

    print(",".join(COLONNES))
    print(",".join(ligne))
    print("%s · ligne %s dans %s" % (
        "À BLANC, rien écrit" if a.a_blanc else "écrit", action,
        os.path.relpath(a.csv, RACINE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
