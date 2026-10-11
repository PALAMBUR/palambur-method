#!/bin/bash
# Palambur · pose le skill du dépôt dans ~/.claude/skills/palambur-method/
#
#     bash outils/installer_local.sh            # à blanc · montre le diff et ce que rsync ferait
#     bash outils/installer_local.sh --ecrire   # pose réellement
#
# POURQUOI · le 11.10.2026, la copie installée dans ~/.claude/skills datait du
# 04.08 et portait encore trois « PME » corrigés sur GitHub le 24.09. Trois
# copies du skill dérivaient (dépôt, skill local, adaptations). Le plan en 30
# points (point 4) fait du dépôt la SEULE source de vérité · la copie locale
# n’est plus éditée à la main, elle est posée par ce script depuis le dépôt.
#
# CE QU’IL FAIT · un `diff -ru` lisible, puis `rsync -a --delete` de
# `skills/palambur-method/` vers `~/.claude/skills/palambur-method/`.
# `--delete` retire de la cible ce que le dépôt ne porte plus · une version
# remplacée n’est pas perdue, l’historique git du dépôt l’archive.
#
# À BLANC PAR DÉFAUT · sans `--ecrire`, rsync tourne avec `-n` et n’écrit rien.
# Victor valide ce qu’il voit avant de poser.
#
# SI LA CIBLE EST UN LIEN SYMBOLIQUE · refus, dans les deux modes. Relevé du
# 11.10.2026 · `~/.claude/skills/palambur-method` est un lien vers
# `~/palambur/skills/palambur-method`, le clone périmé du 04.08.
# Un rsync à travers ce lien écrirait DANS L’AUTRE CLONE, pas dans le dossier
# qu’on croit poser, et son `--delete` y ferait le ménage. Deux voies, au choix
# de Victor, aucune exécutée par ce script ·
#   (a) garder le lien et mettre l’autre clone à jour · `git -C ~/palambur pull`
#   (b) refaire le lien vers le clone de l’atelier ·
#       `ln -sfn <dépôt>/skills/palambur-method ~/.claude/skills/palambur-method`
#       (le dépôt est alors servi en direct, ce script devient inutile)
# Les commandes sont écrites dans la feuille de l’atelier, hors du dépôt
# (`0500_AGENTS_IA/COMMANDES_GITHUB_SKILL_A_VALIDER_2026-10-11.md`, § 5).
set -euo pipefail

ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# chemin NORMALISÉ (pas de `outils/..` dedans) · il est recopié dans la commande
# `ln -sfn` proposée en cas de refus, et un lien vers `…/outils/../skills/…` marche
# mais ne se relit pas
SOURCE="$(cd "${ICI}/.." && pwd)/skills/palambur-method/"
CIBLE="${HOME}/.claude/skills/palambur-method/"

MODE="à blanc"
RSYNC_N="-n"
if [[ "${1:-}" == "--ecrire" ]]; then
  MODE="ÉCRITURE"
  RSYNC_N=""
fi

if [[ ! -f "${SOURCE}SKILL.md" ]]; then
  echo "REFUS · ${SOURCE}SKILL.md introuvable · ce script se lance depuis le dépôt du skill"
  exit 1
fi

echo "INSTALLATION LOCALE DU SKILL · mode ${MODE}"
echo "  source : ${SOURCE}"
echo "  cible  : ${CIBLE}"
echo "------------------------------------------------------------------------"

# la cible sans sa barre finale · `-L` ne voit pas le lien à travers `lien/`
CIBLE_NUE="${CIBLE%/}"
if [[ -L "${CIBLE_NUE}" ]]; then
  VISE="$(readlink "${CIBLE_NUE}")"
  echo "REFUS · ${CIBLE_NUE} est un LIEN SYMBOLIQUE vers :"
  echo "        ${VISE}"
  echo "  un rsync à travers ce lien écrirait là-bas, pas ici · rien n’a été fait."
  echo "  Deux voies, au choix de Victor (feuille de l’atelier COMMANDES_GITHUB_SKILL_A_VALIDER_2026-10-11.md § 5) :"
  echo "   (a) garder le lien et mettre à jour ce qu’il vise :  git -C \"$(dirname "$(dirname "${VISE}")")\" pull"
  echo "   (b) refaire le lien vers ce dépôt :  ln -sfn \"${SOURCE%/}\" \"${CIBLE_NUE}\""
  exit 2
fi

if [[ -d "${CIBLE}" ]]; then
  echo "DIFF · ce que la cible porte (<) contre ce que le dépôt porte (>)"
  # diff rend 1 quand il y a des différences · ce n’est pas une erreur ici
  diff -ru "${CIBLE}" "${SOURCE}" && echo "  aucune différence · la cible est à jour" || true
else
  echo "  la cible n’existe pas encore · tout sera copié"
fi

echo "------------------------------------------------------------------------"
echo "RSYNC · ${MODE}"
# à blanc, on ne crée RIEN, pas même le dossier parent · un essai qui écrit n’est pas un essai
if [[ -z "${RSYNC_N}" ]]; then
  mkdir -p "$(dirname "${CIBLE}")"
fi
# shellcheck disable=SC2086
rsync -av --delete ${RSYNC_N} --exclude '.DS_Store' "${SOURCE}" "${CIBLE}"

echo "------------------------------------------------------------------------"
if [[ -z "${RSYNC_N}" ]]; then
  echo "POSÉ · ${CIBLE} est la copie du dépôt"
else
  echo "À BLANC · rien n’a été écrit · relancer avec --ecrire pour poser"
fi
