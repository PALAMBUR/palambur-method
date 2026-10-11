# Méthode Palambur · Skill `palambur-method`

*Relecture native à faire · Diese Übersetzung wartet auf das Gegenlesen durch eine Person mit deutscher Muttersprache. Massgebend ist die französische Fassung ([README.md](README.md)).*

[![Security: A · Skills Directory](https://www.skillsdirectory.com/api/skills/palambur-palambur-method/badge)](https://www.skillsdirectory.com/skills/palambur-palambur-method)

**Ein Skill, der die richtigen Fragen stellt, bevor er schreibt.** Sie bitten eine KI um ein Arbeitsdokument (Stelleninserat, Offerte, Zahlungserinnerung, Vertrag, interne Mitteilung). Statt zu raten, was fehlt, und den Rest zu erfinden, stellt Ihnen der Skill vier kurze Fragen und liefert dann ein Dokument, das Sie verschicken können. Gedacht für Unternehmen der Westschweiz, überall verwendbar. Kostenlos, MIT-Lizenz.

Weitere Sprachen: [Français · English](README.md) · [Italiano](README.it.md)

---

## Vorher / nachher, in 30 Sekunden

**Was Sie schreiben:**

> méthode palambur: schreib ein Stelleninserat für einen Maler zu 80 %

**Was der Skill antwortet** (eine Frage pro Nachricht, mit Zähler, Antworten mit Buchstaben und einem vorsichtigen Standardwert):

> **Frage 1 von 4 · der Kanton**
>
> In welchem Kanton befindet sich die Stelle?
>
> A. Waadt
> B. Genf
> C. Westschweiz, ohne nähere Angabe · Standard, wenn Sie nichts angeben
> D. Anderes / ich weiss es nicht

Dann, nach demselben Muster:

> **Frage 2 von 4 · die Aufgaben** · A. Innenmalerei und Renovation · B. Fassaden und Aussenarbeiten · C. beides · D. Anderes / ich weiss es nicht

> **Frage 3 von 4 · das Profil** · A. EFZ Maler/in, 3 Jahre Erfahrung · B. EFZ verlangt, Berufseinsteiger willkommen · C. Erfahrung ohne EFZ akzeptiert · D. Anderes / ich weiss es nicht

> **Frage 4 von 4 · die Leistungen** · A. 13. Monatslohn · B. 13. Monatslohn und Weiterbildung · C. keine besonderen · D. Anderes / ich weiss es nicht

Sie antworten mit einem Buchstaben oder in freiem Text. Wenn Sie nichts angeben, gilt der Standardwert; wählen Sie „ich weiss es nicht“, bleibt das Feld im Dokument als `[À COMPLÉTER]` (zu ergänzen) stehen.

**Was Sie erhalten**, in zwei Teilen. Zuerst die **ausgefüllte Palambur-Vorlage**, den wiederverwendbaren Prompt (Auszug; die Blocknamen bleiben französisch, wie in den Skill-Dateien):

```
INSTRUCTION
Verfassen Sie ein Stelleninserat für eine Stelle als Maler/in zu 80 %, um
qualifizierte Bewerbungen im Kanton Waadt zu gewinnen.

RÔLE ET AUDIENCE
Sie sind für die Rekrutierung in einem Unternehmen der Westschweiz zuständig,
geschult im OR, im GlG und im DSG. Sie schreiben für Bewerbende aus dem Baugewerbe.

DONNÉES
Pensum 80 % · Kanton Waadt · Innenmalerei und Renovation · EFZ Maler/in,
3 Jahre Erfahrung · 13. Monatslohn und Weiterbildung
Stellenantritt: [À COMPLÉTER] · Vertragsart: [À COMPLÉTER]

CONTRAINTES
Geschlechtsneutrale Formulierung (m/w/d). Keine Kriterien zu Alter, Herkunft
oder Zivilstand. Fehlt eine Angabe, schreiben Sie [À COMPLÉTER], niemals einen
plausiblen Wert.

FORMAT
Titel, Einstieg, Aufgaben, Profil, Leistungen, Bewerbungsweg, Datenschutzhinweis.
250 bis 350 Wörter.
```

Dann das **fertige Dokument** (Auszug):

> **Maler/in EFZ (m/w/d) · 80 % · Kanton Waadt**
>
> Sie mögen sorgfältige Arbeit und Renovationsbaustellen? Unser Unternehmen [À COMPLÉTER] sucht eine/n Maler/in zu 80 %, Stellenantritt am [À COMPLÉTER].
>
> **Ihre Aufgaben** · Vorbereitung der Untergründe, Innenmalerei, Renovation von Wohnungen und Büros, saubere Abschlussarbeiten, Beratung der Kundschaft vor Ort.
>
> **Ihr Profil** · EFZ Maler/in, mindestens drei Jahre Erfahrung, Selbständigkeit und Sinn fürs Detail.
>
> **Was wir bieten** · 13. Monatslohn, bezahlte Weiterbildung, stabiles Team.
>
> *Ihre Daten werden in der Schweiz bearbeitet, gemäss dem Datenschutzgesetz (DSG).*

Was nicht gesagt wurde, wurde nicht erfunden: es bleibt als `[À COMPLÉTER]` markiert. Enthält Ihre Anfrage Kundennamen oder Beträge, fragt der Skill zuerst, ob er sie anonymisieren soll (das ist die Standardeinstellung).

---

## Was das ist

**Zwei Namen, zwei Dinge.** *Die Méthode Palambur* ist das Ganze: die Disziplin der Klärung, die schweizerischen Leitplanken, der Schutz vor Erfindungen. *Die Palambur-Vorlage* (französisch *Gabarit Palambur*) ist ihr Werkzeug: die **5 geordneten Blöcke** eines Prompts, Instruction · Rôle et audience · Données · Contraintes · Format (Anweisung · Rolle und Zielpublikum · Daten · Vorgaben · Form), plus 4 Erweiterungsblöcke für Dokumente mit hohem Risiko (Vertrag, Charta, interne Richtlinie).

Der Skill verwandelt eine **unterbestimmte** Fachanfrage in ein **brauchbares Dokument**, indem er den fehlenden Kontext *vor* der Produktion einholt. Intern bereitet er ein Paket von etwa vier entscheidenden Fragen vor (Kanton, Aufgaben, Profil, Leistungen …), stellt aber **nur eine pro Nachricht**, mit Zähler („Frage 1 von 4“), einem ausgewiesenen vorsichtigen Standardwert und einem Ausweg „Anderes / ich weiss es nicht“. Dann liefert er:

1. die **ausgefüllte Palambur-Vorlage**, bereit zum Kopieren und Wiederverwenden;
2. das **fertige Dokument**, mit den schweizerischen Leitplanken (GlG, DSG, OR/ArG, Datensouveränität).

**Drei Versprechen.**

- **Flüssig** · wenige, gezielte Fragen, höchstens vier pro Paket. Ist alles bereits angegeben, produziert er direkt.
- **Sicher** · Datenschutz als Standard (Anonymisierung, Datenschutzhinweis), keine erfundenen Daten, keine Gesetzesartikelnummer ohne die Markierung `[À VÉRIFIER]` (zu prüfen).
- **Stumm** · dieser Skill sendet nichts, nirgendwohin. Keine Telemetrie, kein Palambur-Server, kein Konto. Es sind Textdateien, die Ihre KI liest.

**Und ein Lesemodus.** Sie hängen einen bereits geschriebenen Text an (ein Kündigungsschreiben, eine Offerte) und bitten um Durchsicht: keine Fragen, eine Tabelle „Befund · Risiko · Vorgeschlagene Korrektur“, dann die korrigierte Fassung. Die Durchsicht korrigiert Form, Recht und Daten; sie schreibt den Inhalt nicht um.

### Auslösung · drei Türen

Eine genügt.

1. **Das Wort** · Ihre Nachricht enthält **„palambur“**, **„méthode palambur“** oder **„palambur method“**.
2. **Die Art der Anfrage** · ein Arbeitsdokument, in ein oder zwei Sätzen angefragt (Stelleninserat, Offerte, Zahlungserinnerung, Vertrag, interne Mitteilung …), ein schweizerischer Unternehmenskontext, zu schützende Namen oder Beträge, oder ein angehängter Text zur Durchsicht.
3. **Die Option „immer aktiv“** · schreiben Sie **„Méthode Palambur toujours active“** in die Unterhaltung oder in Ihre `CLAUDE.md`, und der Skill gilt für alles, was die KI verfasst, bis „Méthode Palambur désactivée“.

Einmal ausgelöst: fehlen entscheidende Elemente, klärt er; ist alles angegeben, produziert er direkt.

Die Dateien des Skills sind auf Französisch geschrieben. Die Fragen und das Dokument folgen der Sprache Ihrer Anfrage.

---

## Installation

### Claude Code (Plugin)

In Claude Code dieses Repository als Marketplace hinzufügen:

```
/plugin marketplace add PALAMBUR/palambur-method
```

Dann das Plugin installieren:

```
/plugin install palambur@palambur
```

Oder den Ordner `skills/palambur-method/` nach `~/.claude/skills/` kopieren. Das Skript `outils/installer_local.sh` erledigt das für Sie (standardmässig als Probelauf, `--ecrire` zum Schreiben).

**Eine Wahrheit, das Repository.** Der Skill hat nur eine Quelle: `skills/palambur-method/` in diesem Repository. Was die Hosts lesen (`~/.claude/skills/`, `~/.agents/skills/`, ein installiertes Plugin), ist **ein Link oder eine datierte Kopie**, die sich per `git pull` oder über eine neue Plugin-Version aktualisiert, **niemals durch Bearbeiten der Dateien vor Ort**: eine Korrektur in einer Kopie geht beim nächsten Update verloren, und niemand liest sie gegen.

### Codex, Cursor, Copilot, Gemini, Mistral, ChatGPT, Infomaniak

Das Format `SKILL.md` ist ein **offener Standard**. Ein einziger symbolischer Link des Ordners `skills/palambur-method/` in `~/.agents/skills/` genügt für fünf Hosts: **Codex** (OpenAI, folgt symbolischen Links und liest auch `.agents/skills/` in einem Projekt), **Cursor**, **GitHub Copilot**, **Gemini CLI** und **Mistral Vibe CLI** (offizielle Dokumentation jedes Anbieters, Stand 11.10.2026). Gemini (App) und Mistral Vibe Work nehmen den Skill per Upload an; ChatGPT bietet native Skills je nach Abonnement. Für Hosts, die nur ein Anweisungsfeld haben (Claude.ai-Projekt, Euria von Infomaniak), liefert der Ordner [`adaptations/`](adaptations/) die Methode verdichtet als **eigenständigen System-Prompt**, in zwei Grössen, aus dem Skill selbst erzeugt.

Die Schritt-für-Schritt-Anleitung, Host für Host, mit Quellen, steht in [`portabilite/INSTALLATION.md`](portabilite/INSTALLATION.md).

---

## Aufbau des Repositorys

```
palambur-method/
├── .claude-plugin/
│   ├── plugin.json              # das Claude-Code-Plugin (Name, Version, Schlüsselwörter)
│   └── marketplace.json         # die Marketplace, die es bereitstellt
├── skills/
│   └── palambur-method/
│       ├── SKILL.md             # wann auslösen + der Ablauf (Schritte 0 bis 4)
│       ├── methode-palambur.md  # die Vorlage (5 + 4 Blöcke), die 4 Stufen, DONNÉES-Felder, Ton
│       ├── protection-donnees.md  # Anonymisierung, Markierungen, Datenschutzhinweise, souveräne Werkzeuge
│       ├── relecture.md         # der Lesemodus (Schritt 4): sechs Siebe, Ausgabetabelle
│       ├── references-juridiques.md # die Texte, die der Skill nennen darf, was er nie erfindet
│       ├── gabarits/            # eine Referenzdatei pro häufigem Dokument
│       └── metiers/             # eine Datei pro Beruf (Aufgaben, Gesetze, Wortschatz, Fallen)
├── adaptations/                 # die Prompts zum Einfügen (Claude.ai-Projekt, Euria, GPT) · erzeugt
├── portabilite/                 # den Skill Host für Host installieren · Beobachtung der Plattformen
├── epreuves/                    # zwanzig Fälle, das Bewertungsraster, mesurer.py
├── evals/                       # dieselben zwanzig Fälle im Format „claude plugin eval“
├── diffusion/                   # was dazu dient, den Skill bekannt zu machen (ausserhalb des Skills)
├── exemples/                    # zehn vollständige Beispiele, eines pro Vorlage, fiktive Daten
├── pedagogie/                   # Manifest, FAQ, Glossar, Druckblatt, Kurs, Workshop, Rundbrief
├── outils/                      # Generator der Adaptationen, Kontrollkette, Typografieregel, lokale Installation
├── CHANGELOG.md                 # das Versionsjournal
├── CONTRIBUTING.md              # wie man eine Vorlage oder eine Korrektur vorschlägt
├── CODE_OF_CONDUCT.md           # der Verhaltenskodex
├── LICENSE                      # MIT
└── README.md
```

Die Ordner `gabarits/`, `metiers/`, `portabilite/` und `diffusion/` füllen sich mit den Versionen; das [Versionsjournal](CHANGELOG.md) sagt, was vorliegt und was in Vorbereitung ist.

### Vor der Veröffentlichung prüfen

Die Kontrollkette (aktuelle Typografieregel, Typografie, kein Vorkommen des französischen Kürzels für kleine und mittlere Unternehmen, JSON, Version, Adaptationen, Frontmatter, Grösse, Links):

```bash
python3 outils/controle.py
```

Die Kontrolle bringt sich an fabrizierten Zeugen selbst zu Fall, um zu beweisen, dass sie hinschaut:

```bash
python3 outils/controle.py --epreuve
```

`controle.py` läuft **auf jedem Klon**: die Typografieregel, die sie anwendet, ist in `outils/regle_typo.py` eingebettet, eine datierte Kopie einer Regel, die in der Palambur-Werkstatt ausserhalb dieses Repositorys massgebend ist. Liegt die Werkstatt daneben, vergleicht die Kontrolle `regle` beide und lehnt eine veraltete Kopie ab; anderswo sagt sie es in einer Zeile und wird nicht rot. Der Rest der Werkstattkette (Register der Prompts, Chaptal-Korpus) setzt die Werkstatt voraus und ist nicht in diesem Repository.

Die **Prüfungen des Skills** selbst (ist er flüssig, ist er sicher?) stehen in [`epreuves/`](epreuves/): zwanzig Anfragen, ein Bewertungsraster, `mesurer.py`. Der Ordner [`evals/`](evals/) trägt dieselben zwanzig Fälle im Format `claude plugin eval`. Am 11.10.2026 **waren die 20 Fälle noch nicht gespielt**: sie zu spielen kostet Modellaufrufe, und diese Ausgabe war nicht bewilligt.

---

## Verpflichtungen

- **Der Basis-Skill ist kostenlos und bleibt es.** MIT-Lizenz: Sie dürfen ihn verwenden, kopieren, verändern, auch im kommerziellen Rahmen.
  **Der Basis-Skill ist dieses ganze Repository**: die Methode, die Vorlagen, die Berufsblätter, die Prüfungen und jede folgende Version. Was Palambur daneben verkauft (eine für ein Unternehmen voreingestellte Fassung, eine begleitete Installation, siehe [`diffusion/VERSION_ENTREPRISE_cadrage.md`](diffusion/VERSION_ENTREPRISE_cadrage.md)) **fügt Dienstleistung um den Skill herum hinzu; nichts, was hier liegt, wird kostenpflichtig.**
- **Er sendet nichts, nirgendwohin.** Keine Telemetrie, kein Netzwerkaufruf, kein Konto. Ihre Anfragen bleiben zwischen Ihnen und der KI, die Sie gewählt haben.
- **Keine Werbung im Skill.** Die Dokumente tragen keinen Hinweis auf Palambur. Was folgt, ist die einzige Ausnahme, und sie steht hier, nicht im Skill.

Der Skill ist die Tür, [Chaptal](https://palambur.ch) das Haus: 782 Berufspisten nach der Palambur-Vorlage, einsatzbereit, auf palambur.ch (Stand 11.10.2026).

## Lizenz

[MIT](LICENSE) · Palambur · Victor Semblanet · 2026
