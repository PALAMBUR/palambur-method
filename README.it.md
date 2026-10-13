# Méthode Palambur · skill `palambur-method`

[English](README.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · Italiano

[![Controllo](https://github.com/PALAMBUR/palambur-method/actions/workflows/controle.yml/badge.svg)](https://github.com/PALAMBUR/palambur-method/actions/workflows/controle.yml) [![Licenza MIT](https://img.shields.io/badge/licence-MIT-blue)](LICENSE) [![Versione](https://img.shields.io/github/v/release/PALAMBUR/palambur-method)](https://github.com/PALAMBUR/palambur-method/releases) [![Security: A · Skills Directory](https://www.skillsdirectory.com/api/skills/palambur-palambur-method/badge)](https://www.skillsdirectory.com/skills/palambur-palambur-method)

**Uno skill che pone le domande giuste prima di scrivere.** Lei chiede a un’IA un documento di lavoro (annuncio di impiego, preventivo, sollecito, contratto, nota interna). Invece di indovinare ciò che manca e inventare il resto, lo skill Le pone al massimo quattro domande brevi, una alla volta, poi restituisce un documento che può inviare. Pensato per le imprese della Svizzera romanda, utilizzabile ovunque. Gratuito, licenza MIT.

**Lo skill in sé è scritto in francese** · produce documenti in francese per le imprese della Svizzera romanda, e le misure pubblicate sono state fatte su quel testo. Ciò che si legge prima di installare (questo README, la guida ai contributi, la guida d’installazione) è in inglese.

---

<a id="essayer"></a>
## Provare in due minuti

**Claude Code** · due comandi nella conversazione, poi una richiesta.

```
/plugin marketplace add PALAMBUR/palambur-method
```

```
/plugin install palambur@palambur
```

Poi scriva: `méthode palambur : fais une offre d’emploi pour un peintre à 80 %`

**Nel Suo browser** (Claude.ai, ChatGPT, Euria di Infomaniak, Mistral…) · apra [`adaptations/methode-palambur-prompt.md`](adaptations/methode-palambur-prompt.md), copi **il blocco sotto la riga** e lo incolli nelle istruzioni del Suo progetto o del Suo assistente. Niente da installare. Per una casella di istruzioni con un limite stretto di caratteri, prenda il [prompt breve](adaptations/methode-palambur-prompt-court.md). Entrambi i prompt sono in francese; le domande e il documento seguono la lingua della Sua richiesta.

**Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe** · un solo collegamento simbolico della cartella `skills/palambur-method/` in `~/.agents/skills/` basta per i cinque host. I comandi, host per host, sono in [`docs/portabilite/INSTALLATION.md`](docs/portabilite/INSTALLATION.md) (in inglese).

**Verificare che lo skill sia caricato** · in Claude Code, `/plugin` poi la scheda **Installed**; oppure, su qualsiasi host, chieda «méthode palambur : qual è la tua prima domanda?» e attenda una risposta che inizi con «Domanda 1 di N».

---

## Sommario

- [Provare in due minuti](#essayer)
- [Prima / dopo, in 30 secondi](#avant-apres)
- [Che cos’è](#ce-que-c-est)
- [Attivazione · tre porte](#declenchement)
- [Installazione](#installation)
- [Struttura del repository](#structure)
- [Misure e prove](#mesures)
- [Impegni](#engagements)
- [Contribuire](#contribuer) · [Citare](#citer) · [Licenza](#licence)

---

<a id="avant-apres"></a>
## Prima / dopo, in 30 secondi

![Le quattro domande, poi il Gabarit e il Livrable](docs/demo-quatre-questions.svg)

**Ciò che Lei scrive:**

> méthode palambur : fais une offre d’emploi pour un peintre à 80 %

**Ciò che lo skill risponde** (qui reso in italiano; risponde nella lingua della Sua richiesta). Alla prima attivazione, tre righe di apertura, il livello di sensibilità, poi la prima domanda, nello stesso messaggio:

> **Méthode Palambur.** Le porrò prima alcune domande, una alla volta, per non inventare nulla al posto Suo.
> Risponde con una lettera o in testo libero; se passa, si applica un valore prudente che resta visibile.
> Riceverà poi due blocchi da copiare: il **Gabarit Palambur**, riutilizzabile, poi il **Livrable**.
>
> Livello di sensibilità · ordinario (nessun nome, nessun importo)
>
> **Domanda 1 di 4 · il luogo e il quadro**
>
> Dove si trova il posto, e in quale quadro?
>
> A. un solo luogo di lavoro, cantone da indicare
> B. più sedi o spostamenti regolari
> C. telelavoro parziale possibile, quota da precisare
> D. Altro / non so · predefinito se non precisa

Poi, **una domanda per messaggio**, sempre con un contatore, scelte con lettere, un valore predefinito prudente segnalato e una via d’uscita:

> **Domanda 2 di 4 · le mansioni** · A. le fornisco io · B. proponga le mansioni correnti del mestiere, correggo io · predefinito se non precisa · C. il posto è nuovo, le mansioni non sono ancora definite · D. Altro / non so

> **Domanda 3 di 4 · il profilo** · A. un titolo richiesto (AFC, attestato professionale federale, maestria) · B. AFC o esperienza equivalente riconosciuta · predefinito se non precisa · C. nessun titolo richiesto, formazione interna assicurata · D. Altro / non so

> **Domanda 4 di 4 · ciò che l’impresa offre** · A. nulla oltre il quadro contrattuale e del contratto collettivo · predefinito se non precisa · B. vantaggi da indicare · C. vantaggi da indicare e una fascia salariale lorda pubblicata · D. Altro / non so

Risposte scelte per l’esempio: A (Canton Vaud, officina a Yverdon-les-Bains), B, A (AFC di pittore edile), B (tredicesima e formazione continua). Se sceglie «non so», il campo resta `[À COMPLÉTER]` nel documento.

**Ciò che Lei riceve.** Prima **una riga di contesto**, che dice ciò che è stato ritenuto:

> Contexte retenu · annuncio di impiego · pittore edile all’80 % · Canton Vaud · tono fattuale · dati: nessuno · 4 risposte, 0 predefiniti, 10 marcatori

Poi il **Gabarit Palambur compilato**, il prompt riutilizzabile (estratto):

```
Gabarit Palambur

INSTRUCTION
Rediga un annuncio di impiego completo per un posto di pittore edile all’80 %,
destinato alla pubblicazione su [À COMPLÉTER : canali]. Obiettivo: ottenere
candidature qualificate dicendo il lavoro reale, il luogo, l’orario e il
quadro, senza promettere nulla che non sia stato convalidato dalla direzione.

RÔLE ET AUDIENCE
Lei è responsabile del reclutamento presso Exemple SA, impresa di pittura
edile del Canton Vaud, formato al CO, alla LEg (LPar), alla LTr (LL) e alla
nLPD (LPD). Scrive per una persona del mestiere che legge l’annuncio sul
telefono.

DONNÉES
• Denominazione del posto: pittore edile (m/f/d)
• Luogo di lavoro e cantone: officina di Yverdon-les-Bains, cantieri nel
  Canton Vaud
• Grado di occupazione · tipo di contratto · data di entrata: 80 % · durata
  indeterminata · da convenire
• Profilo indispensabile: AFC di pittore edile
• Vantaggi convalidati dalla direzione: tredicesima · formazione continua
• Contratto collettivo di lavoro applicabile, se noto: [À COMPLÉTER]

CONTRAINTES
Nessun criterio discriminatorio (LEg, CO), neutralità di genere (m/f/d).
Nessun salario, nessuna durata di vacanze inventati. Nessun articolo di legge
citato: se si applica un CCL, lo nomini e ponga [À VÉRIFIER : CCL applicabile].

FORMAT
Sei sezioni: titolo e accroche · l’impresa · le Sue mansioni · il Suo profilo ·
ciò che offriamo · candidarsi. Da 400 a 600 parole. Forma di cortesia, italiano
della Svizzera. Menzione del trattamento dei dati a fine annuncio.
```

Poi il **Livrable** (estratto):

> **Pittore edile AFC (m/f/d) · 80 % · Yverdon-les-Bains**
>
> Ama il lavoro accurato e i cantieri di ristrutturazione? Exemple SA cerca un pittore edile all’80 %, entrata in servizio da convenire.
>
> **Le Sue mansioni** [À VALIDER : elenco proposto, da correggere dalla direzione] · preparazione dei supporti, pittura interna di abitazioni e uffici, posa di rivestimenti murali, finiture, consulenza al cliente sul posto.
>
> **Il Suo profilo** · indispensabile: AFC di pittore edile · auspicato: [À COMPLÉTER : anni di esperienza], licenza di condurre [À COMPLÉTER : categoria].
>
> **Ciò che offriamo** · tredicesima · formazione continua a carico dell’impresa.
>
> **Candidarsi** · invii il Suo dossier a [À COMPLÉTER : funzione del destinatario] tramite [À COMPLÉTER : canale].
>
> *I Suoi dati di candidatura sono trattati da Exemple SA mediante [À COMPLÉTER : strumento], ospitato in [À COMPLÉTER : paese], e conservati per [À COMPLÉTER : durata].*

E, per chiudere, il **Journal de confiance**, cinque righe che dicono ciò che è stato protetto, marcato e rifiutato:

```
Journal de confiance
· Livello di sensibilità · ordinario (nessuna persona nominata)
· Dati · nessuno
· Marcatori posti · [À COMPLÉTER] ×7 · [À VÉRIFIER] ×2 (CCL applicabile, annuncio del posto) · [À VALIDER] ×1 (mansioni)
· Ipotesi rifiutate · nessun salario cifrato; nessun CCL nominato di memoria; nessun luogo di hosting dei dati affermato
· Rilettura umana · richiesta prima della pubblicazione (documento RU)
```

Ciò che non è stato detto non è stato inventato: resta marcato. Se la Sua richiesta contiene **nomi di clienti o importi**, lo skill chiede prima, in una domanda a sé, se deve anonimizzarli (è l’impostazione predefinita). Lo scambio completo è in [`docs/exemples/01-offre-emploi.md`](docs/exemples/01-offre-emploi.md); altri nove percorsi, uno per gabarit, sono in [`docs/exemples/`](docs/exemples/) (in francese).

---

<a id="ce-que-c-est"></a>
## Che cos’è

**Due nomi, due oggetti.** *La Méthode Palambur* è l’insieme: la disciplina del chiarimento, le salvaguardie svizzere, il rifiuto di inventare. *Il Gabarit Palambur* ne è lo strumento: i **5 blocchi** ordinati di un prompt, Instruction · Rôle et audience · Données · Contraintes · Format, più 4 blocchi di estensione per i documenti ad alta posta (contratto, carta, politica interna).

Lo skill trasforma una richiesta professionale **sottospecificata** in un **documento di qualità**, colmando il contesto mancante *prima* di produrre. Prepara internamente un lotto di al massimo quattro domande determinanti (luogo e quadro, mansioni, profilo, vantaggi…), ma ne pone **una sola per messaggio**, con un contatore («Domanda 1 di 4»), un valore predefinito prudente segnalato e una via d’uscita «Altro / non so». Poi consegna:

1. il **Gabarit Palambur compilato**, pronto da copiare, incollare e riutilizzare;
2. il **Livrable** redatto, con le salvaguardie svizzere (LEg, nLPD, CO, LTr, sovranità dei dati), chiuso da un Journal de confiance.

**Tre promesse.**

- **Fluido** · poche domande, ben mirate, al massimo quattro per lotto. Se tutto è già fornito, produce direttamente.
- **Sicuro** · protezione dei dati per impostazione predefinita (anonimizzazione, menzione nLPD), nessun dato inventato, nessun numero di articolo di legge scritto senza il marcatore `[À VÉRIFIER]`.
- **Silenzioso** · questo skill non invia nulla, da nessuna parte. Nessuna telemetria, nessun server Palambur, nessun account. Sono file di testo che la Sua IA legge.

**Un profilo d’impresa, per non rispondere due volte.** Lo skill legge un file `profil-entreprise.md` posto alla **radice della Sua cartella di lavoro**: cantone, contratto collettivo, tono, firma, lingua. I suoi campi compilati valgono come risposte, e le domande che risolve non Le vengono più poste. Il modello da copiare è nello skill: [`skills/palambur-method/profil-entreprise.md`](skills/palambur-method/profil-entreprise.md).

**E una modalità di rilettura.** Lei allega un testo già scritto (una lettera di licenziamento, un preventivo) e chiede di rileggerlo: nessuna domanda, una tabella «Constatazione · Rischio · Correzione proposta», poi la versione corretta. La rilettura corregge la forma, il diritto e i dati; non riscrive la sostanza ([`relecture.md`](skills/palambur-method/relecture.md)).

<a id="declenchement"></a>
## Attivazione · tre porte

Una sola basta.

1. **La parola** · il Suo messaggio contiene **«palambur»**, **«méthode palambur»** o **«palambur method»**.
2. **La natura della richiesta** · un documento di lavoro chiesto in una o due frasi (annuncio di impiego, preventivo, sollecito, contratto, nota interna…), un contesto d’impresa svizzera, nomi o importi da proteggere, oppure un testo allegato da rileggere.
3. **L’opzione «sempre attivo»** · scriva **«Méthode Palambur toujours active»** nella conversazione o nel Suo `CLAUDE.md`, e lo skill si applica a tutto ciò che l’IA redige, fino a «Méthode Palambur désactivée».

Una volta attivato: se mancano elementi determinanti, **chiarisce**; se tutto è fornito, produce direttamente; se un testo è allegato per rilettura, rilegge senza porre domande.

I file dello skill sono scritti in **francese**. Le domande e il documento seguono la lingua della Sua richiesta.

---

<a id="installation"></a>
## Installazione

### Prerequisiti

- **Per usare lo skill** · un host che legge il formato `SKILL.md` (Claude Code aggiornato, Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe) o qualsiasi IA dotata di una casella di istruzioni. Nient’altro.
- **Per gli strumenti del repository** (controllo, prove, generatori) · Python 3.9 o più recente. Facoltativo: non Le serve per usare lo skill.

### Claude Code · plugin

In Claude Code, aggiunga questo repository come marketplace:

```
/plugin marketplace add PALAMBUR/palambur-method
```

Poi installi il plugin:

```
/plugin install palambur@palambur
```

Gli aggiornamenti arrivano con ogni **nuova versione** del plugin; `/plugin` poi **Installed** mostra quella che ha.

### Copia locale · `outils/installer_local.sh`

Se preferisce una copia in `~/.claude/skills/` senza passare dal marketplace, cloni il repository e avvii lo script. In prova per impostazione predefinita, mostra ciò che farebbe:

```bash
bash outils/installer_local.sh
```

Con `--ecrire`, posa realmente la copia:

```bash
bash outils/installer_local.sh --ecrire
```

Lo script **rifiuta** se la destinazione è già un collegamento simbolico, per non scrivere in un altro clone attraverso il collegamento.

### Codex, Cursor, Copilot, Gemini CLI, Mistral Vibe · `.agents/skills`

Il formato `SKILL.md` è uno **standard aperto**. Un solo collegamento simbolico della cartella `skills/palambur-method/` in `~/.agents/skills/` basta per cinque host: **Codex** (che segue i collegamenti simbolici e legge anche `.agents/skills/` in un progetto), **Cursor**, **GitHub Copilot**, **Gemini CLI** e **Mistral Vibe CLI** (documentazione ufficiale di ogni editore, rilevata l’11.10.2026). Gemini (applicazione) e Mistral Vibe Work accettano lo skill per caricamento. La guida passo per passo, host per host, con le sue fonti datate, è in [`docs/portabilite/INSTALLATION.md`](docs/portabilite/INSTALLATION.md); la conformità dello skill allo standard è rilevata in [`docs/portabilite/CONFORMITE_STANDARD.md`](docs/portabilite/CONFORMITE_STANDARD.md) (entrambe in francese).

### Caselle di istruzioni · Progetto Claude.ai, Euria, altri assistenti

Per gli host che offrono solo una **casella di istruzioni di sistema**, la cartella [`adaptations/`](adaptations/) fornisce il metodo condensato in un prompt autonomo, **generato dallo skill stesso** a ogni versione: una [versione completa](adaptations/methode-palambur-prompt.md) sotto 8'000 caratteri e una [versione breve](adaptations/methode-palambur-prompt-court.md) sotto 1'500 caratteri. Su questi host, l’assistente *è* il metodo: si applica a ogni richiesta, senza parola di attivazione. La tabella «quale host, quale versione, dove incollare» è in [`adaptations/README.md`](adaptations/README.md).

**Una sola verità, il repository.** Lo skill ha una sola fonte: `skills/palambur-method/` in questo repository. Ciò che gli host leggono (`~/.claude/skills/`, `~/.agents/skills/`, un plugin installato, un prompt incollato) è **un collegamento o una copia datata**, che si aggiorna con `git pull` o con una nuova versione del plugin, **mai modificando i file sul posto**: una correzione fatta in una copia è persa all’aggiornamento successivo, e nessuno la rilegge.

---

<a id="structure"></a>
## Struttura del repository

```
palambur-method/
├── README.md · README.fr.md · README.de.md · README.it.md   # questo file, in quattro lingue
├── CHANGELOG.md · CONTRIBUTING.md · CODE_OF_CONDUCT.md      # versioni, contributi, condotta
├── SECURITY.md · CITATION.cff · LICENSE                     # segnalazione, citazione, MIT
├── .claude-plugin/          # plugin.json e marketplace.json · il plugin Claude Code
├── .github/                 # modelli di ticket, modello di PR, workflows/controle.yml (CI)
├── .agents/skills/palambur-method/   # posizione per Codex e host .agents · un README, il collegamento si posa da Lei
├── skills/palambur-method/  # LO SKILL · la sola fonte
│   ├── SKILL.md             # quando attivarsi, le tappe da 0 a 4, la forma delle domande
│   ├── methode-palambur.md  # il Gabarit (5 + 4 blocchi), i 4 livelli, il tono, tre percorsi
│   ├── protection-donnees.md   # livelli di sensibilità, anonimizzazione, Journal de confiance
│   ├── relecture.md         # la modalità di rilettura · sei vagli, tabella di uscita
│   ├── references-juridiques.md   # i testi che lo skill può nominare, ciò che non inventa mai
│   ├── profil-entreprise.md # il modello del profilo d’impresa letto alla radice della cartella di lavoro
│   ├── gabarits/            # un file per documento frequente (domande, campi DONNÉES, trappole)
│   ├── metiers/             # un file per mestiere (vocabolario, testi di legge nominati, trappole)
│   └── agents/openai.yaml   # metadati facoltativi letti da Codex
├── adaptations/             # i prompt di sistema generati · completo (sotto 8'000 caratteri) e breve
├── docs/
│   ├── exemples/            # dieci percorsi completi, uno per gabarit, dati fittizi
│   ├── pedagogie/           # MANIFESTE.md, FAQ.md, GLOSSAIRE.md
│   ├── portabilite/         # INSTALLATION.md (host per host), CONFORMITE_STANDARD.md
│   ├── VEILLE_JURIDIQUE.md  # ciò che alimenta la tabella dei riferimenti giuridici
│   └── DIX_COMMANDEMENTS.md # la protezione dei dati in dieci righe
├── epreuves/                # 149 casi (cas.json), grille.md, mesurer.py, generer_evals.py,
│                            # jouer_apertus.py, risultati e protocollo, reponses/ (trascrizioni)
├── evals/                   # solo README · i casi «claude plugin eval» si rigenerano
└── outils/                  # controle.py, generer_adaptations.py, installer_local.sh, regle_typo.py, metiers/
```

Le cartelle `gabarits/` e `metiers/` si completano di versione in versione; il [giornale delle versioni](CHANGELOG.md) dice ciò che è presente, con una nota di qualità per versione. I [dieci comandamenti](docs/DIX_COMMANDEMENTS.md) tengono la protezione dei dati in una pagina; le [FAQ](docs/pedagogie/FAQ.md), il [manifesto](docs/pedagogie/MANIFESTE.md) e il [glossario](docs/pedagogie/GLOSSAIRE.md) rispondono alle domande ricorrenti. La documentazione al di fuori di questo README è in francese; i README in [tedesco](README.de.md) e in [italiano](README.it.md) attendono una **rilettura da parte di madrelingua**.

---

<a id="mesures"></a>
## Misure e prove

**La catena di controllo** verifica il repository prima di ogni pubblicazione: regola tipografica, parola vietata, JSON validi, numero di versione unico in tre file, adattamenti aggiornati rispetto alle loro fonti, frontmatter e dimensione di `SKILL.md`, collegamenti relativi. Gira su qualsiasi clone e nella CI (`.github/workflows/controle.yml`), senza segreto né chiamata a un modello:

```bash
python3 outils/controle.py
```

Il controllo **si rompe da solo** su testimoni fabbricati, per provare che guarda:

```bash
python3 outils/controle.py --epreuve
```

**Le prove dello skill** (è fluido, è sicuro?) sono in [`epreuves/`](epreuves/): **149 casi** in tre famiglie (documenti, compiti di mestiere, trappole che spingono a inventare · rilevamento dell’11.10.2026, `python3 epreuves/mesurer.py --compter` fa fede), una [griglia di valutazione](epreuves/grille.md) a venti guardie, e `mesurer.py`, che valuta una risposta contro la griglia e sa anch’esso rompersi (`--epreuve`). Gli stessi casi nel formato `claude plugin eval` si **rigenerano** da `epreuves/cas.json` con `python3 epreuves/generer_evals.py`; non sono più versionati, [`evals/README.md`](evals/README.md) dice come avviarli.

**La misura pubblicata.** Misurato il 12.10.2026 su Apertus (Infomaniak) con il **prompt di adattamento completo**, non lo skill nativo: **1 verde su 149**. Il modello pone la domanda di anonimizzazione, poi consegna il Gabarit e il documento nello stesso messaggio, senza chiarire e senza marcatori. Dettaglio, guardie rosse per famiglia e spesa esatta in [`epreuves/RESULTATS_APERTUS_2026-10-11.md`](epreuves/RESULTATS_APERTUS_2026-10-11.md) (in francese). **Lo skill nativo su Claude, misurato il 13.10.2026** con `claude plugin eval` (Claude Code 2.1.296, modello `claude-opus-5-5`), solo il primo turno, un’esecuzione per caso, sui dieci casi del protocollo a tre modelli: **8 verdi su 10 con lo skill, 0 su 10 senza** (stesso modello, stesse richieste, plugin rimosso). I due rossi sono dello strumento, non del Metodo: alla lettura, entrambi i primi turni seguono il Metodo, uno nomina la legge fittizia nel suo rifiuto, l’altro propone « Client X » senza la parola « anonimizzare ». Senza lo skill il modello scrive tutto il documento in una volta, cita un articolo di legge e un tasso d’interesse senza verifica, e scivola verso il diritto francese in tre casi svizzeri. Trascrizioni dei due bracci, spesa stimata e limiti della misura in [`epreuves/RESULTATS_CLAUDE_NATIF_2026-10-13.md`](epreuves/RESULTATS_CLAUDE_NATIF_2026-10-13.md) (in francese).

---

<a id="engagements"></a>
## Impegni

- **Lo skill di base è gratuito e lo resterà.** Licenza MIT: può usarlo, copiarlo, modificarlo, anche in un quadro commerciale. **Lo skill di base è tutto questo repository**: il metodo, i gabarit, le schede di mestiere, le prove, e ogni versione che seguirà. Palambur vende **servizio attorno** (una versione preimpostata per un’impresa, un’installazione accompagnata); nulla di ciò che è qui diventa a pagamento.
- **Non invia nulla, da nessuna parte.** Nessuna telemetria, nessuna chiamata di rete, nessun account. Le Sue richieste restano tra Lei e l’IA che ha scelto.
- **Nessuna pubblicità nello skill.** I documenti non portano alcuna menzione Palambur. Lo skill nomina **un solo strumento Palambur, Jomini** (anonimizzazione gratuita nel browser, senza account), perché serve la protezione dei dati; è la sola menzione. Ciò che segue è l’altra eccezione, ed è qui, non nello skill.

Lo skill è la porta, [Chaptal](https://palambur.ch) la casa: **782 piste di mestiere** al Gabarit Palambur, pronte all’uso, su palambur.ch (rilevamento dell’11.10.2026).

---

<a id="contribuer"></a>
## Contribuire

Un gabarit mancante, una correzione giuridica, una nuova lingua: [`CONTRIBUTING.md`](CONTRIBUTING.md) dice come proporre, ciò che la catena di controllo esige e la **regola del madrelingua** per le traduzioni. Il [codice di condotta](CODE_OF_CONDUCT.md) si applica a tutti gli scambi; una falla o un comportamento dello skill che espone dei dati si segnala secondo [`SECURITY.md`](SECURITY.md), non in un ticket pubblico.

<a id="citer"></a>
## Citare

Per citare la Méthode Palambur in un lavoro, un corso o un articolo, i **metadati di citazione** sono in [`CITATION.cff`](CITATION.cff); GitHub ne propone la forma APA e BibTeX dalla pagina del repository.

<a id="licence"></a>
## Licenza

[MIT](LICENSE) · Palambur · Victor Semblanet · 2026
