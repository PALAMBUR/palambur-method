#!/usr/bin/env python3
"""Joue les cas d’épreuve contre Apertus (Infomaniak AI Services) et dépose
les échanges au format que lit `mesurer.py --reponses`.

Pourquoi · le point 52 du plan du 11.10.2026 dit que rien ne prouve que la
Méthode tient hors de Claude. Ce script rejoue les cas de `cas.json` avec le
prompt d’adaptation (celui qu’on colle dans Euria, un GPT, un Projet) sur un
modèle suisse facturé en francs, et compte chaque centime.

Trois bras ·
  sans     · aucun prompt système (témoin · ce que fait le modèle seul)
  complet  · adaptations/methode-palambur-prompt.md
  court    · adaptations/methode-palambur-prompt-court.md

L’utilisateur est simulé, pressé · il répond la lettre du défaut quand elle est
annoncée, sinon « A » s’il y a des lettres, sinon « Je ne sais pas, prenez le
défaut prudent et produisez » (depuis le 12.10.2026, phases 2 et 3 · la phase 1
répondait « A » à tout) ; à la question d’anonymisation il répond toujours
« Anonymisez » ; il ne répond jamais « conserver ». La partie s’arrête quand
le livrable est là (les cinq blocs du Gabarit ou un titre « Livrable »), ou
au huitième tour de l’assistant (INCOMPLET).

Budget · la dépense est calculée depuis `usage` de chaque réponse, au tarif
relevé le 23.08.2026 (CHF 0.70 entrée / 2.50 sortie par million de jetons,
`/1/ai/models` ne publie pas de prix). Le script REFUSE d’appeler au-delà de
`--plafond` (défaut CHF 4.00, pour rester sous 5.00 même si le tarif a monté
d’un quart). Chaque appel est consigné dans `reponses/DEPENSE.csv`.

La clé vit dans le trousseau macOS (service `palambur.infomaniak.ai`, compte
`cle`), jamais dans un fichier. Python 3.9, bibliothèque standard seule.
Chemins depuis `__file__`. Un cas déjà déposé n’est pas rejoué (reprise).
"""
import argparse
import csv
import datetime as dt
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ICI = Path(__file__).resolve().parent
RACINE = ICI.parent
CAS_JSON = ICI / "cas.json"
REPONSES = ICI / "reponses"
ADAPTATIONS = RACINE / "adaptations"

PRODUIT = "108734"
URL = "https://api.infomaniak.com/2/ai/%s/openai/v1/chat/completions" % PRODUIT
MODELE = "swiss-ai/Apertus-v1.5-70B"
# Tarif relevé le 23.08.2026 sur la page des prix Infomaniak AI Tools, en CHF
# par million de jetons. À redater si la page change.
TARIF_DATE = "2026-08-23"
TARIF_ENTREE = 0.70
TARIF_SORTIE = 2.50

BRAS = {
    "sans": None,
    "complet": ADAPTATIONS / "methode-palambur-prompt.md",
    "court": ADAPTATIONS / "methode-palambur-prompt-court.md",
}
BLOCS = ["INSTRUCTION", "RÔLE ET AUDIENCE", "DONNÉES", "CONTRAINTES", "FORMAT"]
RE_LIVRABLE = re.compile(r"^#+\s*(?:\d+\s*[.·]\s*)?(?:Le\s+)?Livrable\b", re.M | re.I)
RE_DEFAUT = re.compile(r"^\s*\**([A-D])\**\s*[.)·:][^\n]*d[ée]faut", re.M | re.I)
RE_NLPD = re.compile(r"anonymis", re.I)
RE_LETTRES = re.compile(r"^\s*\**[A-D]\**\s*[.)·:]\s+\S", re.M)
TOURS_MAX = 8
# 2'500 et non 900 · la première passe du 11.10.2026 (23:21) a coupé douze
# réponses sur douze du bras complet à 900 jetons · le Gabarit et le livrable
# tiennent rarement en moins.
MAX_TOKENS = 2500


def cle():
    r = subprocess.run(
        ["security", "find-generic-password", "-s", "palambur.infomaniak.ai", "-a", "cle", "-w"],
        capture_output=True, text=True, check=True,
    )
    k = r.stdout.strip()
    if len(k) < 40:
        sys.exit("clé du trousseau trop courte · service palambur.infomaniak.ai, compte cle")
    return k


def prompt_systeme(bras):
    chemin = BRAS[bras]
    if chemin is None:
        return None, "aucun"
    texte = chemin.read_text(encoding="utf-8")
    m = re.search(r"empreinte sha256 courte ([0-9a-f]+)", texte)
    empreinte = m.group(1) if m else "inconnue"
    # On colle ce que l’utilisateur collerait · tout le fichier sauf la ligne
    # d’en-tête « Généré le … » qui s’adresse à qui lit le dépôt.
    corps = "\n".join(l for l in texte.splitlines() if not l.startswith("> Généré le"))
    return corps.strip(), empreinte


def appel(k, messages, temperature=0.2):
    corps = json.dumps({
        "model": MODELE, "messages": messages,
        "temperature": temperature, "max_tokens": MAX_TOKENS,
    }).encode("utf-8")
    req = urllib.request.Request(URL, data=corps, method="POST", headers={
        "Authorization": "Bearer " + k, "Content-Type": "application/json",
    })
    for essai in range(3):
        try:
            with urllib.request.urlopen(req, timeout=180) as rep:
                d = json.loads(rep.read().decode("utf-8"))
            choix = d["choices"][0]
            texte = choix["message"]["content"] or ""
            if choix.get("finish_reason") == "length":
                texte += "\n\n<!-- réponse coupée par max_tokens -->"
            u = d.get("usage", {})
            return texte, int(u.get("prompt_tokens", 0)), int(u.get("completion_tokens", 0))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and essai < 2:
                time.sleep(5 * (essai + 1))
                continue
            raise SystemExit("HTTP %s · %s" % (e.code, e.read()[:300]))
    raise SystemExit("trois essais sans réponse")


def question_en_suspens(texte):
    """Le dernier paragraphe non vide pose-t-il une question ?

    Première passe du 11.10.2026 · `relance_facture` en bras complet posait la
    question nLPD ET déroulait le Gabarit dans le même message, puis finissait
    par « Souhaitez-vous que je produise le texte final maintenant ? ». Le
    script y voyait un livrable et s’arrêtait · l’utilisateur simulé n’a jamais
    répondu, et la partie était jugée COMPLÈTE sur un livrable absent.
    """
    paras = [p for p in re.split(r"\n\s*\n", texte.strip()) if p.strip()]
    if any("?" in p for p in paras[-3:]):
        return True
    # Des choix lettrés quelque part · le modèle attend une lettre, même si
    # la question est plus haut et le Gabarit en dessous.
    return bool(RE_LETTRES.search(texte))


def livrable_present(texte):
    if question_en_suspens(texte):
        return False
    if RE_LIVRABLE.search(texte):
        return True
    return sum(1 for b in BLOCS if b in texte) >= 4


def reponse_utilisateur(texte_assistant):
    if RE_NLPD.search(texte_assistant) and "?" in texte_assistant:
        return "Anonymisez, s’il vous plaît."
    m = RE_DEFAUT.search(texte_assistant)
    if m:
        return m.group(1)
    if RE_LETTRES.search(texte_assistant):
        return "A"
    # Question ouverte, sans lettres · un « A » n’a aucun sens. La deuxième
    # passe du 11.10.2026 (certificat_travail, bras complet) a répondu « A » à
    # sept questions ouvertes d’affilée et le modèle n’a jamais livré. Depuis
    # le 12.10 (phases 2 et 3), l’utilisateur pressé dit ce qu’il dirait.
    return "Je ne sais pas, prenez le défaut prudent et produisez."


class Compteur:
    def __init__(self, plafond, journal):
        self.plafond = plafond
        self.journal = journal
        self.chf = 0.0
        if journal.exists():
            with journal.open(encoding="utf-8") as f:
                for ligne in csv.DictReader(f):
                    self.chf = max(self.chf, float(ligne["chf_cumule"]))
        else:
            journal.parent.mkdir(parents=True, exist_ok=True)
            with journal.open("w", encoding="utf-8", newline="") as f:
                csv.writer(f).writerow(["horodatage", "bras", "id", "tour", "jetons_entree", "jetons_sortie", "chf_appel", "chf_cumule"])

    def peut_appeler(self):
        return self.chf < self.plafond

    def consigne(self, bras, cas_id, tour, e, s):
        cout = e * TARIF_ENTREE / 1e6 + s * TARIF_SORTIE / 1e6
        self.chf += cout
        with self.journal.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerow([dt.datetime.now().isoformat(timespec="seconds"), bras, cas_id, tour, e, s, "%.6f" % cout, "%.6f" % self.chf])
        return cout


def jouer_cas(k, cas, bras, systeme, compteur, dossier):
    sortie = dossier / ("%s.md" % cas["id"])
    if sortie.exists():
        return "déjà joué"
    messages = []
    if systeme:
        messages.append({"role": "system", "content": systeme})
    messages.append({"role": "user", "content": cas["demande"]})
    lignes = ["# %s" % cas["id"], "## Demande", cas["demande"]]
    statut = "INCOMPLET"
    relance_faite = False
    for tour in range(1, TOURS_MAX + 1):
        if not compteur.peut_appeler():
            statut = "ARRÊT BUDGET"
            break
        texte, e, s = appel(k, messages)
        compteur.consigne(bras, cas["id"], tour, e, s)
        lignes += ["## Assistant · tour %d" % tour, texte.strip()]
        messages.append({"role": "assistant", "content": texte})
        if livrable_present(texte):
            statut = "COMPLET"
            break
        if "?" not in texte:
            # Le modèle n’a ni questionné ni livré au sens du Gabarit · une
            # relance, pas plus · la première passe du 11.10 en faisait sept
            # d’affilée sur le bras témoin, qui réécrivait sept fois son texte.
            if relance_faite:
                statut = "LIVRÉ SANS GABARIT"
                break
            relance_faite = True
            rep = "Oui, allez-y."
        else:
            rep = reponse_utilisateur(texte)
        lignes += ["## Utilisateur · tour %d" % tour, rep]
        messages.append({"role": "user", "content": rep})
    lignes += ["", "<!-- statut · %s · tours assistant · %d -->" % (statut, min(tour, TOURS_MAX))]
    sortie.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return statut


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--bras", default="complet", choices=sorted(BRAS))
    p.add_argument("--cas", default="", help="ids séparés par des virgules (défaut · tous)")
    p.add_argument("--famille", default="", help="livrable, metier ou piege")
    p.add_argument("--plafond", type=float, default=4.00, help="CHF, dépense totale maximale (défaut 4.00)")
    p.add_argument("--a-blanc", action="store_true", help="n’appelle pas, liste les cas et le coût estimé")
    a = p.parse_args(argv)

    cas_tous = json.loads(CAS_JSON.read_text(encoding="utf-8"))["cas"]
    voulus = set(x for x in a.cas.split(",") if x)
    cas = [c for c in cas_tous if (not voulus or c["id"] in voulus)
           and (not a.famille or (c.get("famille") or "livrable") == a.famille)]
    if voulus and len(cas) != len(voulus):
        sys.exit("ids inconnus · %s" % sorted(voulus - {c["id"] for c in cas}))

    systeme, empreinte = prompt_systeme(a.bras)
    dossier = REPONSES / ("apertus-%s" % a.bras)
    dossier.mkdir(parents=True, exist_ok=True)
    compteur = Compteur(a.plafond, REPONSES / "DEPENSE.csv")

    if a.a_blanc:
        jetons_sys = len(systeme or "") // 4
        estime = len(cas) * 5 * ((jetons_sys + 1500) * TARIF_ENTREE + 500 * TARIF_SORTIE) / 1e6
        print("%d cas · bras %s · ≈ %.2f CHF (5 tours, estimation grossière) · dépensé jusqu’ici %.4f CHF" % (len(cas), a.bras, estime, compteur.chf))
        return 0

    k = cle()
    releve = dossier / "RELEVE.md"
    if not releve.exists():
        releve.write_text(
            "# Relevé · Apertus · bras %s\n\n- Hôte · Infomaniak AI Services, produit %s, API v2\n- Modèle · %s\n"
            "- Prompt · %s (empreinte %s)\n- Première passe · %s\n- Tarif appliqué · CHF %.2f entrée / %.2f sortie par M jetons (relevé %s)\n"
            "- Joué par · le script `epreuves/jouer_apertus.py`, lancé par la session Skills et Prompt Ingénierie, utilisateur simulé pressé (voir l’en-tête du script)\n"
            % (a.bras, PRODUIT, MODELE, BRAS[a.bras].name if BRAS[a.bras] else "aucun", empreinte,
               dt.date.today().isoformat(), TARIF_ENTREE, TARIF_SORTIE, TARIF_DATE),
            encoding="utf-8")

    bilan = {}
    for c in cas:
        if not compteur.peut_appeler():
            print("plafond %.2f CHF atteint · arrêt avant %s" % (a.plafond, c["id"]))
            break
        st = jouer_cas(k, c, a.bras, systeme, compteur, dossier)
        bilan[st] = bilan.get(st, 0) + 1
        print("%-40s %-12s cumul %.4f CHF" % (c["id"], st, compteur.chf))
    print("bilan · %s · dépense cumulée %.4f CHF (plafond %.2f)" % (bilan, compteur.chf, a.plafond))
    return 0


if __name__ == "__main__":
    sys.exit(main())
