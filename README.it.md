# Méthode Palambur · skill `palambur-method`

*Relecture native à faire · Questa traduzione attende la rilettura di una persona di madrelingua italiana. Fa fede la versione francese ([README.md](README.md)).*

[![Security: A · Skills Directory](https://www.skillsdirectory.com/api/skills/palambur-palambur-method/badge)](https://www.skillsdirectory.com/skills/palambur-palambur-method)

**Uno skill che pone le domande giuste prima di scrivere.** Chiedete a un’IA un documento di lavoro (annuncio di impiego, preventivo, sollecito, contratto, nota interna). Invece di indovinare ciò che manca e inventare il resto, lo skill vi pone quattro domande brevi, poi restituisce un documento che potete inviare. Pensato per le imprese della Svizzera romanda, utilizzabile ovunque. Gratuito, licenza MIT.

Altre lingue: [Français · English](README.md) · [Deutsch](README.de.md)

---

## Prima / dopo, in 30 secondi

**Ciò che scrivete:**

> méthode palambur: fai un annuncio di impiego per un pittore all’80 %

**Ciò che lo skill risponde** (una domanda per messaggio, con un contatore, scelte con lettere e un valore predefinito prudente):

> **Domanda 1 di 4 · il cantone**
>
> In quale cantone si trova il posto?
>
> A. Vaud
> B. Ginevra
> C. Svizzera romanda, senza precisare · predefinito se non precisate
> D. Altro / non so

Poi, sullo stesso modello:

> **Domanda 2 di 4 · le mansioni** · A. pittura interna e ristrutturazione · B. facciate e lavori esterni · C. entrambe · D. Altro / non so

> **Domanda 3 di 4 · il profilo** · A. AFC di pittore edile, 3 anni di esperienza · B. AFC richiesto, principianti accettati · C. esperienza senza AFC accettata · D. Altro / non so

> **Domanda 4 di 4 · i vantaggi** · A. tredicesima · B. tredicesima e formazione continua · C. nessuno in particolare · D. Altro / non so

Rispondete con una lettera o in testo libero. Se non precisate, si applica il valore predefinito; se scegliete « non so », il campo resta `[À COMPLÉTER]` (da completare) nel documento.

**Ciò che ricevete**, in due parti. Prima il **Modello Palambur compilato**, il prompt riutilizzabile (estratto; i nomi dei blocchi restano in francese, come nei file dello skill):

```
INSTRUCTION
Redigete un annuncio di impiego per un posto di pittore edile all’80 %, per
attirare candidature qualificate nel cantone di Vaud.

RÔLE ET AUDIENCE
Siete responsabile del reclutamento in un’impresa della Svizzera romanda,
formato al CO, alla LPar e alla LPD. Scrivete per candidati dell’edilizia.

DONNÉES
Grado di occupazione 80 % · cantone di Vaud · pittura interna e ristrutturazione ·
AFC di pittore edile, 3 anni di esperienza · tredicesima e formazione continua
Data di entrata in servizio: [À COMPLÉTER] · Tipo di contratto: [À COMPLÉTER]

CONTRAINTES
Formulazione neutra rispetto al genere (m/f/d). Nessun criterio di età, origine
o stato civile. Se manca un’informazione, scrivete [À COMPLÉTER], mai un valore
plausibile.

FORMAT
Titolo, apertura, mansioni, profilo, vantaggi, modalità di candidatura,
menzione sulla protezione dei dati. Da 250 a 350 parole.
```

Poi il **documento finale** (estratto):

> **Pittore edile AFC (m/f/d) · 80 % · cantone di Vaud**
>
> Vi piacciono il lavoro accurato e i cantieri di ristrutturazione? La nostra impresa [À COMPLÉTER] cerca un/una pittore/pittrice edile all’80 %, entrata in servizio il [À COMPLÉTER].
>
> **Le vostre mansioni** · preparazione dei supporti, pittura interna, ristrutturazione di appartamenti e uffici, finiture accurate, consulenza ai clienti sul posto.
>
> **Il vostro profilo** · AFC di pittore edile, almeno tre anni di esperienza, autonomia e attenzione ai dettagli.
>
> **Ciò che offriamo** · tredicesima, formazione continua a nostro carico, squadra stabile.
>
> *I vostri dati sono trattati in Svizzera, conformemente alla Legge sulla protezione dei dati (LPD).*

Ciò che non è stato detto non è stato inventato: resta marcato `[À COMPLÉTER]`. Se la vostra richiesta contiene nomi di clienti o importi, lo skill chiede prima se deve anonimizzarli (è l’impostazione predefinita).

---

## Che cos’è

**Due nomi, due oggetti.** *La Méthode Palambur* è l’insieme: la disciplina della chiarificazione, le tutele svizzere, la protezione contro le invenzioni. *Il Modello Palambur* (in francese *Gabarit Palambur*) ne è lo strumento: i **5 blocchi** ordinati di un prompt, Instruction · Rôle et audience · Données · Contraintes · Format (Istruzione · Ruolo e pubblico · Dati · Vincoli · Formato), più 4 blocchi di estensione per i documenti ad alto rischio (contratto, carta, politica interna).

Lo skill trasforma una richiesta professionale **sottospecificata** in un **documento di qualità**, colmando il contesto mancante *prima* di produrre. Prepara internamente un lotto di circa quattro domande determinanti (cantone, mansioni, profilo, vantaggi …), ma ne pone **una sola per messaggio**, con un contatore (« Domanda 1 di 4 »), un valore predefinito prudente segnalato e una via d’uscita « Altro / non so ». Poi consegna:

1. il **Modello Palambur compilato**, pronto da copiare e riutilizzare;
2. il **documento finale** redatto, con le tutele svizzere (LPar, LPD, CO/LL, sovranità dei dati).

**Tre promesse.**

- **Fluido** · poche domande, ben mirate, al massimo quattro per lotto. Se tutto è già fornito, produce direttamente.
- **Sicuro** · protezione dei dati per impostazione predefinita (anonimizzazione, menzione LPD), nessun dato inventato, nessun numero di articolo di legge senza la marcatura `[À VÉRIFIER]` (da verificare).
- **Silenzioso** · questo skill non invia nulla, da nessuna parte. Nessuna telemetria, nessun server Palambur, nessun account. Sono file di testo che la vostra IA legge.

**E una modalità di rilettura.** Allegate un testo già scritto (una lettera di licenziamento, un preventivo) e chiedete di rileggerlo: nessuna domanda, una tabella « Constatazione · Rischio · Correzione proposta », poi la versione corretta. La rilettura corregge la forma, il diritto e i dati; non riscrive la sostanza.

### Attivazione · tre porte

Una sola basta.

1. **La parola** · il vostro messaggio contiene **« palambur »**, **« méthode palambur »** o **« palambur method »**.
2. **La natura della richiesta** · un documento di lavoro chiesto in una o due frasi (annuncio di impiego, preventivo, sollecito, contratto, nota interna …), un contesto di impresa svizzera, nomi o importi da proteggere, o un testo allegato da rileggere.
3. **L’opzione « sempre attivo »** · scrivete **« Méthode Palambur toujours active »** nella conversazione o nel vostro `CLAUDE.md`, e lo skill si applica a tutto ciò che l’IA redige, fino a « Méthode Palambur désactivée ».

Una volta attivato: se mancano elementi determinanti, chiarisce; se tutto è fornito, produce direttamente.

I file dello skill sono scritti in francese. Le domande e il documento seguono la lingua della vostra richiesta.

---

## Installazione

### Claude Code (plugin)

In Claude Code, aggiungere questo repository come marketplace:

```
/plugin marketplace add PALAMBUR/palambur-method
```

Poi installare il plugin:

```
/plugin install palambur@palambur
```

Oppure copiare la cartella `skills/palambur-method/` in `~/.claude/skills/`. Lo script `outils/installer_local.sh` lo fa per voi (in prova per impostazione predefinita, `--ecrire` per scrivere).

**Una sola verità, il repository.** Lo skill ha una sola fonte: `skills/palambur-method/` in questo repository. Ciò che gli host leggono (`~/.claude/skills/`, `~/.agents/skills/`, un plugin installato) è **un collegamento o una copia datata**, che si aggiorna con `git pull` o con una nuova versione del plugin, **mai modificando i file sul posto**: una correzione fatta in una copia si perde all’aggiornamento successivo, e nessuno la rilegge.

### Codex, Cursor, Copilot, Gemini, Mistral, ChatGPT, Infomaniak

Il formato `SKILL.md` è uno **standard aperto**. Un solo collegamento simbolico della cartella `skills/palambur-method/` in `~/.agents/skills/` basta per cinque host: **Codex** (OpenAI, che segue i collegamenti simbolici e legge anche `.agents/skills/` in un progetto), **Cursor**, **GitHub Copilot**, **Gemini CLI** e **Mistral Vibe CLI** (documentazione ufficiale di ogni editore, rilevata l’11.10.2026). Gemini (applicazione) e Mistral Vibe Work accettano lo skill per caricamento; ChatGPT offre skill nativi secondo l’abbonamento. Per gli host che offrono solo un campo di istruzioni (Progetto Claude.ai, Euria di Infomaniak), la cartella [`adaptations/`](adaptations/) fornisce il metodo condensato in **un prompt di sistema autonomo**, in due dimensioni, generato dallo skill stesso.

La guida passo per passo, host per host, con le sue fonti, è in [`portabilite/INSTALLATION.md`](portabilite/INSTALLATION.md).

---

## Struttura del repository

```
palambur-method/
├── .claude-plugin/
│   ├── plugin.json              # il plugin Claude Code (nome, versione, parole chiave)
│   └── marketplace.json         # la marketplace che lo serve
├── skills/
│   └── palambur-method/
│       ├── SKILL.md             # quando attivarsi + lo svolgimento (Tappe da 0 a 4)
│       ├── methode-palambur.md  # il Modello (5 + 4 blocchi), i 4 livelli, campi DONNÉES, tono
│       ├── protection-donnees.md  # anonimizzazione, marcatori, menzioni LPD, strumenti sovrani
│       ├── relecture.md         # la modalità di rilettura (Tappa 4): sei filtri, tabella di uscita
│       ├── references-juridiques.md # i testi che lo skill può nominare, ciò che non inventa mai
│       ├── gabarits/            # un file di riferimento per documento frequente
│       └── metiers/             # un file per mestiere (compiti, leggi, vocabolario, trappole)
├── adaptations/                 # i prompt da incollare (Progetto Claude.ai, Euria, GPT) · generati
├── portabilite/                 # installare lo skill host per host · osservazione delle piattaforme
├── epreuves/                    # venti casi, la griglia di valutazione, mesurer.py
├── evals/                       # gli stessi venti casi nel formato « claude plugin eval »
├── diffusion/                   # ciò che serve a far conoscere lo skill (fuori dallo skill)
├── exemples/                    # dieci esempi completi, uno per modello, dati fittizi
├── pedagogie/                   # manifesto, FAQ, glossario, scheda stampabile, corso, laboratorio, lettera
├── outils/                      # generatore degli adattamenti, catena di controllo, regola tipografica, installazione locale
├── CHANGELOG.md                 # il giornale delle versioni
├── CONTRIBUTING.md              # come proporre un modello o una correzione
├── CODE_OF_CONDUCT.md           # il codice di condotta
├── LICENSE                      # MIT
└── README.md
```

Le cartelle `gabarits/`, `metiers/`, `portabilite/` e `diffusion/` si riempiono con le versioni; il [giornale delle versioni](CHANGELOG.md) dice ciò che è posato e ciò che è in preparazione.

### Verificare prima di pubblicare

La catena di controllo (regola tipografica aggiornata, tipografia, nessuna occorrenza della sigla francese delle piccole e medie imprese, JSON, versione, adattamenti, frontmatter, dimensione, collegamenti):

```bash
python3 outils/controle.py
```

Il controllo si rompe da sé su testimoni fabbricati, per provare che guarda:

```bash
python3 outils/controle.py --epreuve
```

`controle.py` gira **su qualsiasi clone**: la regola tipografica che applica è incorporata in `outils/regle_typo.py`, copia datata di una regola che fa fede nell’atelier Palambur, fuori da questo repository. Quando l’atelier è accanto, il controllo `regle` confronta i due e rifiuta una copia in ritardo; altrove lo dice in una riga e non diventa rosso. Il resto della catena dell’atelier (registro dei prompt, corpus Chaptal) presuppone l’atelier e non è in questo repository.

Le **prove dello skill** stesso (è fluido, è sicuro?) sono in [`epreuves/`](epreuves/): venti richieste, una griglia di valutazione, `mesurer.py`. La cartella [`evals/`](evals/) porta gli stessi venti casi nel formato `claude plugin eval`. All’11.10.2026, **i 20 casi non erano ancora stati giocati**: giocarli consuma chiamate al modello, e questa spesa non era stata autorizzata.

---

## Impegni

- **Lo skill di base è gratuito e lo resterà.** Licenza MIT: potete usarlo, copiarlo, modificarlo, anche in un contesto commerciale.
  **Lo skill di base è tutto questo repository**: il metodo, i modelli, le schede per mestiere, le prove, e ogni versione che seguirà. Ciò che Palambur vende a parte (una versione preimpostata per un’impresa, un’installazione accompagnata, vedere [`diffusion/VERSION_ENTREPRISE_cadrage.md`](diffusion/VERSION_ENTREPRISE_cadrage.md)) **aggiunge servizio attorno allo skill; nulla di ciò che è qui diventa a pagamento.**
- **Non invia nulla, da nessuna parte.** Nessuna telemetria, nessuna chiamata di rete, nessun account. Le vostre richieste restano tra voi e l’IA che avete scelto.
- **Nessuna pubblicità nello skill.** I documenti non portano alcuna menzione Palambur. Ciò che segue è la sola eccezione, ed è qui, non nello skill.

Lo skill è la porta, [Chaptal](https://palambur.ch) la casa: 782 piste per mestiere secondo il Modello Palambur, pronte all’uso, su palambur.ch (rilevamento dell’11.10.2026).

## Licenza

[MIT](LICENSE) · Palambur · Victor Semblanet · 2026
