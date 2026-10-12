# Veille juridique trimestrielle · les textes que le skill nomme

Ce fichier dit **quels textes** le skill a le droit de nommer, **où** se lit chacun dans sa version officielle, **quand** une personne l’a lu pour la dernière fois, et **ce qu’une relecture alimente** dans `skills/palambur-method/references-juridiques.md`. Il se relit **une fois par trimestre** (janvier, avril, juillet, octobre) et à chaque fois qu’une entrée en vigueur est annoncée.

Règle de lecture · la colonne « Dernière lecture » porte une date **et qui** a lu (personne ou modèle). « Jamais » veut dire que seul un modèle a nommé le texte à partir de fiches maison. La colonne « Répond le » vient d’un relevé HTTP automatisé (code de réponse), elle dit que l’adresse sert quelque chose, pas que le texte a été lu.

## Les textes suivis

| Texte | Source officielle | Répond le | Dernière lecture par une personne | Ce que la relecture alimente |
|---|---|---|---|---|
| **LPD (nLPD)** · Loi fédérale sur la protection des données, RS 235.1 | <https://www.fedlex.admin.ch/eli/cc/2022/491/fr> (page consolidée Fedlex, suit toujours l’état en vigueur) | 11.10.2026 · HTTP 200 | 31.08.2026 · relecteur Palambur · état consolidé lu : 07.07.2025 | ligne LPD / nLPD de la table Suisse ; mention-type « Document externe » de `protection-donnees.md` ; mention CH de `metiers/MARCHES.md` § 5 |
| **PFPDT** · autorité fédérale (prises de position, pas une loi) | <https://www.edoeb.admin.ch/fr> | 11.10.2026 · HTTP 200 | 31.08.2026 · relecteur Palambur | colonne « Ce que le skill ne doit JAMAIS faire » de la ligne LPD |
| **CO** · Code des obligations, RS 220 | <https://www.fedlex.admin.ch/eli/cc/27/317_321_377/fr> | 11.10.2026 · HTTP 200 | Jamais · fiches métier maison seulement | ligne CO ; gabarits contrat, certificat, licenciement, relance |
| **LTr** · Loi sur le travail, RS 822.11, et OLT 1 à 5 | <https://www.fedlex.admin.ch/eli/cc/1966/57_57_57/fr> | 11.10.2026 · HTTP 200 | Partielle · brochure SECO « Surveillance technique au poste de travail » lue le 31.08.2026 ; le texte de loi lui-même : jamais | ligne LTr ; fiches métier 05, 10, 14, 18 |
| **LEg** · Loi sur l’égalité, RS 151.1 | <https://www.fedlex.admin.ch/eli/cc/1996/1498_1498_1498/fr> | 11.10.2026 · HTTP 200 | Jamais · fiche maison 05 (Logib, BFEG) | ligne LEg ; crible LEg de `relecture.md` ; pièges des gabarits RH |
| **Code du travail** (France) | <https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/> | 11.10.2026 · HTTP 403 en accès automatisé · s’ouvre dans un navigateur | Jamais · branches France des fiches métier | ligne Code du travail de la table France ; `metiers/MARCHES.md` § 1 et 2 |
| **RGPD** · Règlement (UE) 2016/679 | <https://eur-lex.europa.eu/eli/reg/2016/679/oj/fra> (texte français) · <https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng> (texte anglais, celui de l’index UE) | 11.10.2026 · HTTP 202 en accès automatisé | 31.08.2026 · relecteur Palambur | ligne RGPD ; mentions FR, BE, DE, IT de `metiers/MARCHES.md` § 5 |
| **CNIL** · autorité française (recommandations) | <https://www.cnil.fr/fr> | 11.10.2026 · HTTP 200 | 31.08.2026 · relecteur Palambur | ligne CNIL ; mention FR § 5 |
| **Règlement européen sur l’IA** · Règlement (UE) 2024/1689 | <https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=OJ:L_202401689> | Non relevé le 11.10.2026 (adresse constatée le 31.08.2026) | 31.08.2026 · relecteur Palambur | ligne Règlement IA ; section Shadow AI de `protection-donnees.md` |

Textes nommés par les gabarits et les fiches métier et **pas encore suivis ici** (même liste que `references-juridiques.md`, « Comment tenir cette table ») : LCD, LP, LTVA, LAMal, LAA, LAVS, LPP, LEI, CC, CP, LDA, LMP, AIMP, SIA, CCNT, LFPr, LBA, LPM, LCR, LCA, LSA, LIFD, LAFam, LPrD, LPTh, LHID, LACI, CPC. Ils entrent dans cette table quand une personne les lit à la source ; d’ici là, la règle des quatre lignes s’applique : nommer, jamais chiffrer, jamais d’article.

Autorités des autres marchés nommées par `metiers/MARCHES.md` § 5, relevées le 11.10.2026 (HTTP 200, accès automatisé) et **jamais lues par une personne** : Autorité de protection des données (Belgique, <https://www.autoriteprotectiondonnees.be/citoyen>), BfDI (Allemagne, <https://www.bfdi.bund.de/DE/Home/home_node.html>), Garante per la protezione dei dati personali (Italie, <https://www.garanteprivacy.it/>).

## Le geste trimestriel

1. Relever les adresses (une commande, lecture seule) :

```bash
for u in https://www.fedlex.admin.ch/eli/cc/2022/491/fr https://www.fedlex.admin.ch/eli/cc/27/317_321_377/fr https://www.fedlex.admin.ch/eli/cc/1966/57_57_57/fr https://www.fedlex.admin.ch/eli/cc/1996/1498_1498_1498/fr https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/ https://eur-lex.europa.eu/eli/reg/2016/679/oj/fra; do curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -L --max-time 25 -A "Mozilla/5.0" "$u"; done
```

2. Ouvrir chaque page Fedlex dans un navigateur et lire la ligne « État le … » : si elle a changé depuis la colonne « Dernière lecture », une personne relit les passages que le skill nomme (ce que le texte couvre, pas les articles) et met à jour la colonne « Vérifié » de `references-juridiques.md` avec son nom de fonction et la date.
3. Reporter ici la date du jour et qui a lu. Une ligne dont la lecture a plus d’un an passe en **gras** dans la colonne « Dernière lecture » : c’est elle qu’on relit en premier au trimestre suivant.
4. Si un texte entre en vigueur ou change de nom (exemple : LEtr devenue LEI), corriger le nom dans `references-juridiques.md`, `metiers/MARCHES.md` et les fiches métier qui le portent, puis relancer `python3 outils/controle.py`.

## Journal des relectures

| Date | Qui | Ce qui a été relu | Ce qui a changé |
|---|---|---|---|
| 11.10.2026 | modèle | adresses relevées en HTTP, aucun texte lu | création du fichier ; aucune ligne de `references-juridiques.md` modifiée sur le fond |

---

Ce fichier est tenu par le mainteneur du dépôt (Palambur), qui peut confier une relecture à un relecteur juridique externe ; la fonction du relecteur, jamais son nom, s’écrit dans le journal. Première relecture trimestrielle : **janvier 2027**.
