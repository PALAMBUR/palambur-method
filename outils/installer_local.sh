#!/bin/bash
# Palambur · pose le skill du dépôt dans ~/.claude/skills/palambur-method/
#
#     bash outils/installer_local.sh            # à blanc · montre le diff et ce que rsync ferait
#     bash outils/installer_local.sh --ecrire   # pose réellement
#
# POURQUOI · une copie du skill posée à la main dans ~/.claude/skills finit par
# dériver du dépôt (relevé du 11.10.2026 · une copie locale portait encore des
# corrections faites sur GitHub deux semaines plus tôt). Le dépôt est la SEULE
# source de vérité · la copie locale n’est plus éditée à la main, elle est
# posée par ce script depuis le dépôt.
#
# CE QU’IL FAIT · un `diff -ru` lisible, puis `rsync -a --delete` de
# `skills/palambur-method/` vers `~/.claude/skills/palambur-method/`.
# `--delete` retire de la cible ce que le dépôt ne porte plus · une version
# remplacée n’est pas perdue, l’historique git du dépôt l’archive.
#
# À BLANC PAR DÉFAUT · sans `--ecrire`, rsync tourne avec `-n` et n’écrit rien.
# Vous validez ce que vous voyez avant de poser.
#
# SI LA CIBLE EST UN LIEN SYMBOLIQUE · refus, dans les deux modes. Un rsync à
# travers un lien écrirait DANS LE DOSSIER VISÉ PAR LE LIEN (souvent un autre
# clone), pas dans le dossier qu’on croit poser, et son `--delete` y ferait le
# ménage. Deux voies, aucune exécutée par ce script ·
#   (a) garder le lien et mettre à jour le clone qu’il vise · `git pull` là-bas
#   (b) refaire le lien vers ce dépôt ·
#       `ln -sfn <dépôt>/skills/palambur-method ~/.claude/skills/palambur-method`
#       (le dépôt est alors servi en direct, ce script devient inutile)
# Le script imprime les deux commandes, prêtes à copier, au moment du refus.
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
  echo "  Deux voies, à votre choix (voir docs/portabilite/INSTALLATION.md § 1b) :"
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
