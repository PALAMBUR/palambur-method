#!/usr/bin/env python3
"""Fabrique `evals/` (le format de `claude plugin eval`) depuis `epreuves/cas.json`.

Pourquoi un générateur plutôt que vingt dossiers écrits à la main · deux copies
d’une même vérité divergent toujours (CLAUDE.md § 8 du dossier Palambur). Les
vingt demandes vivent dans `cas.json` ; `mesurer.py` les lit pour l’échange
entier, ce script les lit pour le premier tour que `claude plugin eval` sait
juger. Si un cas change, on relance, et les deux instruments repartent du même
texte.

Format produit (vérifié le 11.10.2026 sur code.claude.com/docs/en/plugin-evals) ·

    evals/
    ├── .gitignore              # results/
    └── <id>/
        ├── prompt.md           # frontmatter · name, description, tags, max_turns,
        │                       #   allowed_tools, expected_outcome · corps · la demande
        └── graders/<nom>.md    # un grader par fichier · regex ou tool_used seulement

Aucun grader `llm` · il coûterait un appel de juge par cas et par passe. Les
regex sont en syntaxe JavaScript (pas de `(?i)`, le drapeau va dans `flags`).

Relançable · les dossiers `evals/<id>/` des cas connus sont effacés puis
réécrits ; tout autre dossier sous `evals/` est laissé en place. Python 3.9.
"""
import json
import shutil
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
CAS_JSON = ICI / "cas.json"
EVALS = ICI.parent / "evals"
SKILL = "palambur-method"

# Les mêmes motifs que mesurer.py, en syntaxe JavaScript. Ils sont recopiés et
# non importés parce qu’ils partent dans des fichiers YAML lus par un autre
# programme ; la seule source reste cas.json, pas ces motifs.
RE_COMPTEUR_1 = r"Question 1 sur [1-4]\b"
RE_COMPTEUR = r"Question \d+ sur \d+"
RE_LETTRE_A = r"^\s*\**A\**\s*[.)·:]"
RE_ECHAPPATOIRE = r"je ne sais pas"
RE_NLPD = r"anonymis"
RE_GABARIT = r"INSTRUCTION[\s\S]*R[ÔO]LE ET AUDIENCE[\s\S]*DONN[ÉE]ES[\s\S]*CONTRAINTES[\s\S]*FORMAT"
RE_ARTICLE_NU = r"\bart\.\s*\d+[a-z]?\b(?![^\n]{0,60}\[À VÉRIFIER)"
RE_PME = r"\bPME\b"
RE_SKILL = r'"skill"\s*:\s*"(?:[\w-]+:)?' + SKILL + r'"'


def yaml_str(s):
    """Une chaîne YAML entre guillemets simples (le seul échappement · doubler)."""
    return "'" + s.replace("'", "''") + "'"


def grader_regex(pattern, flags="", match="", weight=1):
    lignes = ["---", "type: regex", "pattern: " + yaml_str(pattern)]
    if flags:
        lignes.append("flags: " + flags)
    if match:
        lignes.append("match: " + yaml_str(match) if match.startswith("count:") else "match: " + match)
    if weight != 1:
        lignes.append("weight: %s" % weight)
    lignes += ["---", ""]
    return "\n".join(lignes)


def grader_skill():
    return "\n".join(["---", "type: tool_used", "tool: Skill",
                      "input_match: " + yaml_str(RE_SKILL), "---", ""])


def slug(marqueur):
    return (marqueur.strip("[]").lower().replace("à ", "a-").replace("é", "e")
            .replace(" ", "-"))


def graders_pour(cas):
    """Rend {nom_fichier: contenu} selon la famille du cas."""
    g = {"skill-fired.md": grader_skill(),
         "pas-de-pme.md": grader_regex(RE_PME, match="not_contains")}
    nominatif = cas["donnees_nominatives"]
    attendu = cas["nb_questions_attendu"]
    if nominatif:
        # Premier tour attendu · la question binaire d’anonymisation, seule.
        g["question-nlpd.md"] = grader_regex(RE_NLPD, flags="i", weight=2)
        g["une-seule-question.md"] = grader_regex(r"\?", match="count:1")
        g["pas-de-compteur.md"] = grader_regex(RE_COMPTEUR, match="not_contains")
        g["pas-de-livrable.md"] = grader_regex("INSTRUCTION", match="not_contains")
    elif attendu > 0:
        # Premier tour attendu · « Question 1 sur T », une question, lettres, échappatoire.
        g["compteur.md"] = grader_regex(RE_COMPTEUR_1, weight=2)
        g["une-seule-question.md"] = grader_regex(r"\?", match="count:1")
        g["lettres.md"] = grader_regex(RE_LETTRE_A, flags="m")
        g["echappatoire.md"] = grader_regex(RE_ECHAPPATOIRE, flags="i")
        g["pas-de-livrable.md"] = grader_regex("INSTRUCTION", match="not_contains")
    else:
        # Demande complète · le Gabarit puis le livrable, aucune question.
        g["gabarit.md"] = grader_regex(RE_GABARIT, weight=2)
        g["aucune-question.md"] = grader_regex(RE_COMPTEUR, match="not_contains")
        g["article-non-verifie.md"] = grader_regex(RE_ARTICLE_NU, match="not_contains")
        for m in cas["marqueurs_attendus"]:
            g["marqueur-%s.md" % slug(m)] = grader_regex(m.replace("[", r"\[").replace("]", r"\]"))
    return g


def attente(cas):
    if cas["donnees_nominatives"]:
        return ("Premier tour · une seule question, binaire, qui propose d’anonymiser les noms "
                "(« Client X », « Montant A ») · sans compteur, sans livrable.")
    if cas["nb_questions_attendu"] > 0:
        return ("Premier tour · « Question 1 sur %d » (au plus 4), une seule question, choix A à D, "
                "échappatoire « Autre / je ne sais pas » · sans livrable." % cas["nb_questions_attendu"])
    return ("Un seul tour · le Gabarit rempli (INSTRUCTION, RÔLE ET AUDIENCE, DONNÉES, CONTRAINTES, "
            "FORMAT) puis le livrable · aucune question, aucun article de loi sans [À VÉRIFIER].")


def prompt_pour(cas):
    famille = ("nlpd" if cas["donnees_nominatives"]
               else "clarification" if cas["nb_questions_attendu"] > 0 else "complet")
    declencheur = "declencheur-explicite" if cas["declencheur_explicite"] else "declencheur-naturel"
    tags = "[%s, %s, niveau-%s]" % (famille, declencheur, cas["niveau"].lower())
    description = ("%s · généré par epreuves/generer_evals.py depuis epreuves/cas.json, "
                   "ne pas éditer à la main" % cas["livrable"])
    fm = ["---",
          "name: " + cas["id"],
          "description: " + yaml_str(description),
          "tags: " + tags,
          "max_turns: 10",
          "allowed_tools: [Read, Glob, Grep, Skill]",
          "expected_outcome: " + yaml_str(attente(cas)),
          "---", "", cas["demande"], ""]
    return "\n".join(fm)


def main():
    with open(CAS_JSON, encoding="utf-8") as f:
        cas = json.load(f)["cas"]
    EVALS.mkdir(exist_ok=True)
    (EVALS / ".gitignore").write_text("results/\n", encoding="utf-8")
    effaces, fichiers = 0, 0
    for c in cas:
        d = EVALS / c["id"]
        if d.exists():
            shutil.rmtree(d)
            effaces += 1
        (d / "graders").mkdir(parents=True)
        (d / "prompt.md").write_text(prompt_pour(c), encoding="utf-8")
        fichiers += 1
        for nom, contenu in graders_pour(c).items():
            (d / "graders" / nom).write_text(contenu, encoding="utf-8")
            fichiers += 1
    autres = [p.name for p in EVALS.iterdir() if p.is_dir() and p.name not in {c["id"] for c in cas}]
    print("%d cas · %d dossier(s) réécrit(s) · %d fichier(s) écrit(s) sous %s"
          % (len(cas), effaces, fichiers, EVALS))
    if autres:
        print("laissés en place (pas dans cas.json) · " + ", ".join(sorted(autres)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
