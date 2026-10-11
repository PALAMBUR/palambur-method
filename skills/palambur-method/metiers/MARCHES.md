# Les marchés · ce qui change d’un pays à l’autre pour les 26 métiers

Les fiches de ce dossier sont écrites pour le marché racine **fr-CH** (Suisse romande). Ce fichier dit ce qui change quand l’utilisateur travaille pour un autre marché, d’abord **fr-FR** (France), puis les autres marchés déjà ouverts.

Nomenclature des marchés reprise de l’arborescence des tâches par marché (`project_arborescence_taches_par_marche.md`) · fr-CH racine, puis fr-FR, de-CH, de-DE, it-CH, it-IT, en-US, es. Socle commun, puis branches par marché.

## 1 · Le socle fr-CH contre fr-FR · ce qui change pour tous les métiers

Sources · `0500_AGENTS_IA/0501_Prompts_Metiers/_Traductions_multilingue/ANNEXES_CORRESPONDANCE_JURIDIQUE.md` (section France) · `NOTE_CADRAGE_PILOTE_ARBORESCENCE_2026-09-13.md` · `NOTE_COUVERTURE_LOI_MOP_2026-09-13.md` · `feedback_montants_adaptes_pas_convertis.md`.

| Sujet | fr-CH | fr-FR | Ce que le skill fait |
|---|---|---|---|
| Protection des données | nLPD, autorité PFPDT (loi cantonale pour les organes cantonaux et communaux) | RGPD + loi Informatique et Libertés, autorité CNIL | Remplace « nLPD / PFPDT » par « RGPD / CNIL » sans `[À VÉRIFIER]` (annexes, ligne nLPD) ; la mention type devient « Vos données sont traitées conformément au RGPD » |
| Droit du travail | CO, LTr, LEg, CCT de branche | Code du travail, convention collective (IDCC), préavis selon l’ancienneté | Pose la question de la convention collective, jamais la CCT ; les délais suisses ne se transposent jamais |
| Égalité salariale | Analyse Logib, dès 100 employés | Index Egapro, dès 50 salariés, publication avant le 1er mars | Demande l’effectif, parce que le seuil d’obligation diffère (annexes, fichier du 02.09.2026) |
| Prévoyance | AVS (1er pilier), LPP (2e pilier par capitalisation) | Sécurité sociale / CNAV, AGIRC-ARRCO (répartition à points) | Ne décrit jamais la LPP comme « capital » côté France ; `[À VÉRIFIER]` si le texte entre dans le détail (annexes) |
| Accidents | LAA, un régime pro et non pro | Branche AT/MP + assurance maladie (CPAM), deux régimes | `[À VÉRIFIER]` systématique sur tout chiffre d’indemnisation (annexes) |
| Marchés publics | LMP (Confédération), AIMP (cantons), publication sur simap | Code de la commande publique, publication BOAMP puis JOUE | Ne fige jamais un seuil en euros, ils bougent (annexes, fichier du 02.09.2026 · le décret du 15.08.2026 qu’elles citent est [À VÉRIFIER]) |
| Concurrence et publicité | LCD | Code de la consommation, DGCCRF, responsabilité civile | Remplace la LCD, garde l’exigence de preuve des allégations |
| Normes de construction | SIA (règlements et normes), SIA 118 | NF DTU + Eurocodes ; CCAG Travaux pour les marchés publics | Écrit « NF DTU + Eurocodes », jamais un seul mot (annexes) |
| Recouvrement | LP, Office des poursuites | Injonction de payer, commissaire de justice (terme officiel depuis le 01.07.2022), prescription de droit commun 5 ans | N’écrit plus « huissier » ; ne transpose aucun délai suisse (annexes, fichier du 02.09.2026) |
| Hygiène alimentaire | Chimiste cantonal, autorités cantonales | DGAL (cadre), DDPP (contrôles départementaux) | Remplace « chimiste cantonal » par « DDPP », pas par « autorité cantonale » (annexes) |
| Frontaliers et permis | Permis G, L, B, libre circulation UE/AELE | Aucun permis pour les citoyens UE/EEE | Supprime les questions de permis pour un public UE (annexes) |
| Monnaie et montants | CHF, écriture `CHF 20'000.–` | €, écriture « 20 000 € » | Montants **adaptés au niveau de prix du pays, jamais convertis** au chiffre près ; seuils légaux jamais inventés (`feedback_montants_adaptes_pas_convertis.md`) |
| Dates et nombres | 11.10.2026 ; septante, nonante | 11/10/2026 ; soixante-dix, quatre-vingt-dix | Suit le marché dans le livrable |
| Vouvoiement | Vouvoiement | Vouvoiement | Inchangé |
| Mots du métier | Cadre, apprenti (CFC), maître de l’ouvrage, mise à l’enquête | Cadre, apprenti (CAP, Bac pro), maître d’ouvrage, enquête publique | Prend le vocabulaire fr-FR de la section 3 quand il existe, sinon `[À VÉRIFIER]` |

## 2 · Par métier · la différence décisive fr-CH contre fr-FR

Une ligne par métier où la différence change le livrable. Les branches fr-FR du pilote (05, 06, 07, 16, 21) et le métier 26 sont appuyées sur `NOTE_CADRAGE_PILOTE_ARBORESCENCE_2026-09-13.md` et `NOTE_COUVERTURE_LOI_MOP_2026-09-13.md` ; les autres lignes reposent sur les annexes de correspondance quand elles les couvrent, sinon elles sont marquées `[À VÉRIFIER]` et attendent un fichier du projet.

| Code | Métier | fr-CH | fr-FR | Ce qui change dans les questions du skill | Source |
|---|---|---|---|---|---|
| 01 | Direction et stratégie | CO (SA, Sàrl), organe de révision, registre du commerce | Code de commerce, SAS/SARL, commissaire aux comptes, greffe | « Forme juridique ? » reçoit des réponses françaises ; seuils de révision `[À VÉRIFIER]` | `[À VÉRIFIER]` · aucun fichier du projet ne couvre ce métier côté France |
| 02 | Commerce et ventes | AIMP / LMP, simap, TVA suisse | Code de la commande publique, BOAMP, TVA française | « Adjudicateur public ? » renvoie au BOAMP ; aucun seuil chiffré | annexes (marchés publics) |
| 03 | ADV et service client | CO, LP, nLPD | Code de la consommation, injonction de payer, RGPD | « Suisse ou UE ? » devient inutile, le RGPD s’applique ; relance finale nomme l’injonction de payer | annexes (recouvrement, nLPD) |
| 04 | Marketing et communication | LCD, nLPD, opt-in | Code de la consommation, DGCCRF, RGPD, CNIL | La question du consentement cite la CNIL ; allégations toujours prouvées | annexes (nLPD, LCD) |
| 05 | Ressources humaines | CO, LTr, LEg, CCT, Logib dès 100 | Code du travail, convention collective, Egapro dès 50, rupture conventionnelle, entretien professionnel, CSE, DUERP | « Canton et CCT ? » devient « Convention collective et effectif ? » ; tâches propres fr-FR · rupture conventionnelle, entretien professionnel, CSE, DUERP | note pilote (05) · annexes (droit du travail) |
| 06 | Agent immobilier | CO courtage, LFAIE, PPE, notaire | Loi Hoguet, DDT, délai de rétractation, Tracfin, encadrement des loyers, compromis | « Acquéreur étranger ? » (Lex Koller) disparaît ; s’ajoutent « DDT réunis ? », « zone d’encadrement des loyers ? » | note pilote (06) |
| 07 | Conducteur de travaux | SIA 118, OTConst, LDét, situation de travaux | CCAG Travaux, ordre de service, décompte général définitif, PPSPS, coordination SPS | « SIA 118 convenue ? » devient « CCAG Travaux applicable ? » ; tâches propres · ordre de service, DGD | note pilote (07) · note MOP (chapeau entreprise) |
| 08 | Chef de projet | nLPD, CO prestataires | RGPD, Code de commerce pour les prestataires | La question sur les données renvoie au RGPD | annexes (nLPD) |
| 09 | Artisan du bâtiment | CO garantie des défauts, hypothèque légale, OLED | Garantie décennale et assurance décennale, Code de la consommation pour le particulier, devis réglementé | « Réceptionné quand ? » reste ; s’ajoute « attestation décennale fournie ? » | note MOP (Spinetta) · annexes (LCD) · détails `[À VÉRIFIER]` |
| 10 | Restaurateur | ODAlOUs, OHyg, OIDAl, chimiste cantonal, CCNT | Règlements UE 852/2004 et 853/2004, DDPP, convention collective HCR | « Quel canton ? » devient « quel département / quelle DDPP ? » | annexes (hygiène alimentaire) |
| 11 | Critique littéraire | LDA droit de citation, Conseil suisse de la presse | Code de la propriété intellectuelle, droit de réponse | Questions inchangées ; textes `[À VÉRIFIER]` | `[À VÉRIFIER]` |
| 12 | SEO et référencement web | nLPD traceurs, OIP prix | RGPD, recommandations CNIL sur les cookies, affichage des prix | « Suisse ou UE ? » devient inutile ; consentement selon la CNIL | annexes (nLPD) |
| 13 | OSINT et recherche web | nLPD, CO données du candidat | RGPD, CNIL, Code du travail pour le candidat | Mêmes questions, textes français ; détails `[À VÉRIFIER]` | annexes (nLPD) |
| 14 | Industrie et usinage | LTr, OPA, ISO, CCT | Code du travail, DUERP, convention collective de la métallurgie | S’ajoute « DUERP à jour ? » pour tout livrable sécurité | note pilote (05, DUERP) · reste `[À VÉRIFIER]` |
| 15 | Administrations et communes | Loi cantonale sur les données, LInfo cantonale, préavis, organe délibérant | Code général des collectivités territoriales, CADA, conseil municipal, délibération | Le vocabulaire change entièrement (préavis, exécutif en collège) ; textes `[À VÉRIFIER]` | `[À VÉRIFIER]` |
| 16 | Fiduciaires et cabinets comptables | LTVA (méthodes), AVS, LBA, impôt à la source | Liasse fiscale, DSN, prélèvement à la source, dépôt des comptes au greffe, expert-comptable (ordre) | « Forme et canton ? » devient « Forme et régime fiscal ? » ; tâches propres · liasse, DSN, PAS, dépôt des comptes | note pilote (16) |
| 17 | Communication de campagne | LDP et OFipo, seuils fédéraux de financement | CNCCFP, mandataire financier, plafond de dépenses, compte de campagne | « Quel pays, quel scrutin ? » est la première question ; aucun plafond chiffré sans pays | `REFERENCES_17_Communication_campagne.md` (CNCCFP) |
| 18 | Horlogerie et sous-traitance | « Swiss Made », LPM, LCD secret d’affaires | Marché quasi inexistant côté France pour la sous-traitance horlogère | Fiche fr-CH conservée ; marché fr-FR non ouvert | `[À VÉRIFIER]` |
| 19 | Santé et cabinets | CP secret professionnel, LAMal tiers garant/payant, loi cantonale sur la santé | Code de la santé publique, Sécurité sociale (CPAM), Ordre des médecins, DMP | « Tiers garant ou payant ? » disparaît ; textes `[À VÉRIFIER]` | `[À VÉRIFIER]` |
| 20 | Transport et logistique | OTR, LCR, CCT | Code des transports, règlement UE sur les temps de conduite | Mêmes questions sur les repos ; textes `[À VÉRIFIER]` | `[À VÉRIFIER]` |
| 21 | Architectes et ingénieurs civils | SIA 102/103, LDA plans, autorisation cantonale | Loi MOP reprise au Code de la commande publique, éléments de mission ESQ/APS/APD/PRO/ACT/EXE/DET/OPC/AOR, décennale et dommages-ouvrage, DIUO, DAACT, RE 2020 | « Canton ? » devient « commune, PLU ? » ; « règlements SIA intégrés ? » devient « mission de base et éléments de mission ? » | note pilote (21) · note MOP (chapeau maître d’œuvre) |
| 22 | Garage et automobile | LCR, OETV, service des automobiles cantonal | Code de la route, contrôle technique périodique national, Code de la consommation | « Quelle garantie ? » reste ; périodicité du contrôle technique `[À VÉRIFIER]` | `[À VÉRIFIER]` |
| 23 | Assurance et courtage | LSA, registre FINMA, LCA réticence | Code des assurances, ORIAS, devoir de conseil DDA | Mêmes questions ; textes `[À VÉRIFIER]` | `[À VÉRIFIER]` |
| 24 | Associations et fondations | CC (association), exonération LIFD, extrait spécial du casier | Loi de 1901, reçu fiscal, rescrit, préfecture | « Exonérée, inscrite au RC, assujettie TVA ? » devient « déclarée, reconnue d’intérêt général ? » ; textes `[À VÉRIFIER]` | `[À VÉRIFIER]` |
| 25 | Enseignement | PER, HarmoS, LFPr, note sur 6, HEP | Éducation nationale, programmes nationaux, note sur 20, professeur des écoles, CAP et Bac pro | « Degré et canton ? » devient « Degré et académie ? » ; l’échelle de notation change | `REFERENCES_25_Enseignement.md` (section 6) |
| 26 | Maître d’ouvrage | LMP/AIMP, SIA 112 phases, SIA 118, permis cantonal, KBOB | Code de la commande publique Livre IV (ex loi MOP), AMO et conduite d’opération, CCAG Travaux et CCAG-MOE, Spinetta, dommages-ouvrage, coordination SPS, permis de construire (Code de l’urbanisme) | « Public ou privé, quel canton ? » devient « quel acheteur, quelle commune ? » ; « montage ? » reçoit lots séparés, entreprise générale, conception-réalisation | note MOP (chapeau maître d’ouvrage) · `REFERENCES_26_Maitre_ouvrage.md` (section 4 France) |

## 3 · Les autres marchés déjà ouverts

| Marché | Droit et autorités | Langue et conventions | État dans le projet (`project_arborescence_taches_par_marche.md`, `feedback_montants_adaptes_pas_convertis.md`) |
|---|---|---|---|
| de-CH | Le même droit suisse que fr-CH | Allemand de Suisse, `TERMINOLOGIE_DE-CH.md`, `CONVENTIONS_ECRITURE_DE-CH.md` | Corpus allemand clos le 22.09.2026 et posé |
| it-CH | Le même droit suisse que fr-CH | Italien de Suisse, `TERMINOLOGIE_IT-CH.md`, `CONVENTIONS_ECRITURE_IT-CH.md` | Corpus italien clos le 29.09.2026 |
| de-DE | BGB, KSchG, ArbZG, AGG, EntgTranspG, Logib-D ; RGPD | `CORRESPONDANCE_DE-DE.md`, `CONVENTIONS_ECRITURE_DE-DE.md` ; montants à 75 à 90 % du niveau suisse | Montants adaptés le 02.10.2026 |
| it-IT | Codice Civile, Statuto dei Lavoratori, Codice delle pari opportunità ; RGPD | `CORRESPONDANCE_IT-IT.md`, `CONVENTIONS_ECRITURE_IT-IT.md` ; montants à 55 à 70 % du niveau suisse | Montants adaptés le 02.10.2026 |
| es | Estatuto de los Trabajadores, Real Decreto 902/2020 ; RGPD | Annexes, section Espagne ; aucun outil équivalent à Logib à nommer | Corpus espagnol clos le 02.10.2026 |
| en-US | Droit américain, pas de correspondance posée dans les annexes | Anglais américain | Traduction anglaise en ligne depuis le 05.09.2026 (`project_traduction_corpus_anglais.md`) ; correspondance juridique `[À VÉRIFIER]` |

## 4 · Ce qui change dans les questions du skill, marché par marché

1. **La question du lieu change de grain.** fr-CH demande le canton (droit cantonal des constructions, de la santé, des données publiques). fr-FR demande la commune ou le département seulement quand une autorité locale intervient (DDPP, permis de construire) ; sinon la question disparaît.
2. **La question du texte applicable change de nom, pas de place.** « Quelle CCT ? » devient « quelle convention collective ? », « SIA 118 convenue ? » devient « CCAG Travaux applicable ? », « tiers garant ou tiers payant ? » disparaît. La question reste au même rang dans le lot.
3. **La question des données ne change pas, sa mention change.** L’Étape 0 est identique partout ; la mention type nomme la nLPD en Suisse et le RGPD ailleurs.
4. **Les montants.** Toute valeur chiffrée donnée en exemple est adaptée au niveau de prix du marché ; un seuil légal n’est jamais inventé, il porte `[À VÉRIFIER]` et le nom du texte.
5. **Les tâches propres à un marché** (rupture conventionnelle, DDT, DSN, décennale, ordre de service) ne s’ajoutent pas à la fiche fr-CH ; elles vivent dans la branche fr-FR de l’arborescence. Le skill les reconnaît si l’utilisateur les nomme et pose alors les questions fr-FR.
6. **Le vouvoiement ne change pas.** Il reste la règle sur tous les marchés francophones, et son équivalent de politesse dans les autres langues (`CONVENTIONS_ECRITURE_*.md`).

## 5 · La mention de protection des données, par marché et par famille de livrable

La mention se **nomme**, elle ne cite aucun article. Le texte de loi et l’autorité viennent de `references-juridiques.md` (tables Suisse, France, Autres marchés) ; ce qui n’y est pas appuyé est marqué. Trois familles de livrable, une mention chacune ; la famille « RH » et la famille « juridique » ajoutent toujours le rappel de validation humaine de `protection-donnees.md`.

| Marché | Texte et autorité nommés | Document externe (courrier, e-mail, offre, devis, CGV) | Livrable RH (offre d’emploi, contrat, certificat, convocation) | Livrable juridique ou gouvernance (charte, politique, règlement) |
|---|---|---|---|---|
| **CH** (fr-CH, de-CH, it-CH) | LPD (usage : nLPD), PFPDT · appui : texte officiel dans le dossier | « Vos données sont traitées en Suisse, conformément à la nLPD. » | « Les données de ce dossier sont traitées conformément à la nLPD et ne sont accessibles qu’aux personnes qui en ont besoin. » | « Ce document s’appuie sur la nLPD ; il ne remplace pas un avis juridique. Relecture par une personne habilitée avant mise en vigueur. » |
| **FR** (fr-FR) | RGPD, loi Informatique et Libertés, CNIL · appui : texte RGPD et documents CNIL dans le dossier | « Vos données sont traitées conformément au RGPD. » | « Les données de ce dossier sont traitées conformément au RGPD et à la loi Informatique et Libertés ; accès limité aux personnes habilitées. » | « Ce document s’appuie sur le RGPD et les recommandations de la CNIL ; il ne remplace pas un avis juridique. Relecture par une personne habilitée avant mise en vigueur. » |
| **BE** (fr-BE) | RGPD, Autorité de protection des données (APD) · `[À VÉRIFIER : loi belge d’exécution]` · non appuyé dans le dossier | « Vos données sont traitées conformément au RGPD. » | « Les données de ce dossier sont traitées conformément au RGPD ; accès limité aux personnes habilitées. » | « Ce document s’appuie sur le RGPD ; autorité compétente : Autorité de protection des données `[À VÉRIFIER]`. Il ne remplace pas un avis juridique. » |
| **DE** (de-DE) | DSGVO (RGPD), BDSG `[À VÉRIFIER]`, BfDI et autorités des Länder · non appuyé dans le dossier | « Ihre Daten werden gemäss der DSGVO verarbeitet. » | « Die Daten dieser Akte werden gemäss DSGVO verarbeitet; Zugriff nur für berechtigte Personen. » | « Dieses Dokument stützt sich auf die DSGVO; es ersetzt keine Rechtsberatung. Prüfung durch eine befugte Person vor Inkraftsetzung. » |
| **IT** (it-IT) | GDPR (RGPD), Codice privacy `[À VÉRIFIER]`, Garante per la protezione dei dati personali · non appuyé dans le dossier | « I suoi dati sono trattati in conformità al GDPR. » | « I dati di questo fascicolo sono trattati in conformità al GDPR; accesso limitato alle persone autorizzate. » | « Questo documento si basa sul GDPR; non sostituisce una consulenza legale. Verifica da parte di una persona autorizzata prima dell’entrata in vigore. » |
| **EN** (en-US et anglais hors UE) | aucune loi fédérale générale aux États-Unis ; lois d’État (exemple : CCPA, Californie) `[À VÉRIFIER : État applicable]` ; au Royaume-Uni : UK GDPR, ICO (appui : index UK du dossier) | « Your data is processed in accordance with the applicable data protection law [TO VERIFY: jurisdiction]. » | « The data in this file is processed in accordance with the applicable data protection law [TO VERIFY: jurisdiction]; access is limited to authorised persons. » | « This document relies on the applicable data protection law [TO VERIFY: jurisdiction]; it does not replace legal advice. Review by a qualified person before it takes effect. » |

Règles d’emploi :

1. **Une seule mention par document**, à la fin, avant la signature. Elle ne se répète pas dans le Gabarit.
2. **La langue de la mention est celle du livrable**, pas celle de la conversation.
3. **de-CH et it-CH prennent la mention CH** traduite (« gemäss dem DSG », « in conformità alla LPD ») : le droit est suisse, la langue change. `[À VÉRIFIER : formulation par un locuteur natif]` tant que la règle du point 54 n’a pas été appliquée.
4. **Un marqueur `[À VÉRIFIER]` reste visible dans le livrable** s’il est dans la table : il dit à l’utilisateur qu’une personne doit confirmer, il ne s’efface pas pour faire propre.
5. La colonne « Texte et autorité nommés » sert au journal de confiance ; la mention elle-même ne nomme l’autorité que dans la famille juridique.
