---
title: "Uright - Blockchain-basierte ÐApp für Musikurheberrechtsmanagement"
date: 2021-05-10T19:30:25+08:00
draft: false
tags: ["blockchain", "ethereum", "ipfs", "hku"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

# Uright - Blockchain-basierte ÐApp für Musikurheberrechtsmanagement

![uright_chain](https://image.pseudoyu.com/images/uright_chain.png)

### Einführung

Eine dezentralisierte Anwendung (ÐApp) für Musikurheberrechtsmanagement, basierend auf Angular+Solidity+Web3.js, unter Anwendung von Technologien wie IPFS, ENS und Oracles, bereitgestellt auf Ethereum mit Truffle.

Die Uright dezentralisierte Anwendung ermöglicht es Musikern (Inhaltseigentümern), ihre Werke als "Manifestationen" zu registrieren und auf der Ethereum-Blockchain zu verzeichnen.

"Manifestationen" präsentieren die Werke der Musiker als Inhaltsfragmente, um Urheberschaft und Eigentum zu beweisen. Dies wird durch den "Manifestations" Smart Contract erreicht, der den IPFS-Hash, der den Inhalt des Werkes anzeigt, den Titel (geplante zusätzliche Metadaten) und die Registrierungszeit aufzeichnet. Diese Informationen können verwendet werden, um die Urheberschaft zu beweisen, und der Inhalt kann aus dem IPFS-Dateispeichersystem abgerufen werden.

Allerdings reicht die bloße Registrierung einer "Manifestation" nicht aus; es sollten Beweismaterialien bereitgestellt werden, andernfalls läuft die "Manifestation" nach einem Tag ab. Diese Beweismaterialien werden typischerweise vom Musiker (Werkuploader) registriert, aber jeder kann Beweismaterialien hinzufügen. Beweismaterialien können jede Art von Datei sein, wie Screenshots oder PDF-Dokumente. Der "UploadEvidences" Smart Contract lädt die Beweismaterialien in das IPFS-Dateisystem hoch.

Zusätzlich ermöglicht der "YouTubeEvidences" Smart Contract Musikern, ihre Werk-"Manifestationen" in der Upload-Beschreibung auf Plattformen wie YouTube zu deklarieren, und der Smart Contract erkennt dies automatisch als Beweismaterial.

(In Entwicklung...) Wenn jemand anderes bereits das Originalwerk/Beweismaterial eines Musikers registriert hat, kann der Musiker Einspruch erheben. Die Vertragsfunktionalität wurde implementiert, ist aber in der Webanwendung noch nicht verfügbar.

(In Entwicklung...) Tokenisierung der Werke von Musikern mittels NFT-Technologie.

Projektadresse: [GitHub](https://github.com/pseudoyu/uright)

### Architektur

![uright_architecture](https://image.pseudoyu.com/images/uright_architecture.png)

### Kerntechnologien

#### IPFS

Wenn Musiker ihre Werke mit digitalen Dateien (wie .mp3-Formatdateien) registrieren, werden die Dateien auf IPFS hochgeladen, und der generierte IPFS-Identifikator (Hash-Wert) wird verwendet, um das Werk auf der Ethereum-Blockchain zu registrieren. Benutzer können wählen, ob sie ihre Werke in das IPFS-Netzwerk hochladen oder privat halten möchten, indem sie den Inhalt nicht in das IPFS-Netzwerk hochladen lassen und nur den Hash-Wert des Werkes generieren.

Benutzer müssen die exakt gleiche Datei aufbewahren, die zur Generierung des Werk-Hashes verwendet wurde, was später als Beweis für den Besitz der digitalen Datei zur Hash-Verifizierung verwendet werden kann. Der IPFS-Hash-Wert wird auch verwendet, um den hochgeladenen Inhalt abzurufen.

#### Ethereum Naming System (ENS)

Das Uright-Projekt integriert das ethereum-ens-Paket, das im Ethereum-Mainnet, Ropsten, Rinkeby-Testnetzen und lokalen Testnetzen verwendet werden kann. Das ensdomains/ens-Paket wird verwendet, um Adressnamen festzulegen.

#### Orakel

Das Orakel-Modul ist in den Smart Contract für das Hochladen von YouTube-Beweisen integriert. Es verwendet die YouTube-Video-ID (https://www.youtube.com/watch?v=VIDEO_ID), um abzurufen, ob die Videobeschreibung einen spezifischen Werk-Hash enthält.

Diese Funktion ermöglicht es Musikern zu beweisen, dass das Werk auf der YouTube-Plattform existiert und ihnen gehört (da nur der Uploader die Videobeschreibung bearbeiten kann, um den Hash-Wert des Werkes einzufügen).

Der Online-Service von Oraclize kann für Abfragen verwendet werden: http://app.oraclize.it/home/test_query

#### Aktualisierbarkeit

Um den Werkregistrierungsvertrag aktualisierbar zu machen, wurde der AdminUpgradeabilityProxy von ZeppelinOS eingeführt, der das Delegationsmuster durch Relay-Proxies implementiert.

### Entwurfsmuster

![uright_design_architecture](https://image.pseudoyu.com/images/uright_design_architecture.png)

Das Smart-Contract-Design des Uright-Projekts erleichtert die Modularität und Wiederverwendbarkeit. Zum Beispiel wird die Validierungsablauf-Funktionalität als Entitätsbibliothek implementiert; und die "Evidencable"-Bibliothek ermöglicht es registrierten Werken, mehrere Beweismaterialien zu akkumulieren, was auch bei der späteren Entwicklung der Einspruchsfunktion von Vorteil sein kann.

Darüber hinaus kann die Bereitstellung dieser Funktionalitäten als Bibliotheken die Bereitstellungskosten reduzieren.

#### Circuit Breaker Pattern / Notfall-Stopp

Das Circuit-Breaker-Muster kann verhindern, dass eine Anwendung wiederholt versucht, eine Operation auszuführen, die wahrscheinlich fehlschlagen wird, und ermöglicht es ihr, fortzufahren, ohne auf die Behebung des Fehlers zu warten oder Prozessorzyklen zu verschwenden, während sie feststellt, dass der Fehler langanhaltend ist. Das Circuit-Breaker-Muster ermöglicht es einer Anwendung auch, festzustellen, ob der Fehler behoben wurde. Wenn ein Problem auftritt, kann die Anwendung versuchen, die Operation aufzurufen.

#### Automatische Entwertung

Darüber hinaus wird ein Muster ähnlich der "Automatischen Entwertung" für registrierte Werke implementiert. Wenn ein Benutzer also ein Werk registriert, aber keine Beweismaterialien bereitstellt, läuft seine Registrierung nach einer festgelegten Zeit ab. In diesem Fall bedeutet Ablauf, dass das Werk von einem anderen Benutzer neu registriert und überschrieben werden kann.

### Sicherheitsmaßnahmen

Alle Smart Contracts wurden mit Remix- und Solhint-Tools auf Code überprüft. Diese beiden Tools prüfen auf häufige Sicherheitsprobleme wie Reentrancy oder Zeitstempelabhängigkeit.

Die SafeMath-Bibliothek wird verwendet, um Integer-Überlauf- und Unterlaufprobleme zu vermeiden.

Schließlich wird Solhint als Schritt im definierten Workflow für kontinuierliche Integration und Bereitstellung festgelegt. Auf diese Weise führt travis jedes Mal, wenn Code auf GitHub gepusht wird, alle Tests aus (für Verträge und Angular-Frontend), und wenn alle Tests bestanden werden, ist es für die Bereitstellung verantwortlich.

Zusätzlich wird das Solhint-Tool auch vor dem Testen ausgeführt, um potenzielle Sicherheitsprobleme zu verfolgen, die auftreten könnten.

### Verwandte Bibliotheken

Das Uright-Projekt importiert einige Bibliotheken aus ZeppelinOS- und OpenZeppelin-Paketen zur Funktionsimplementierung.

#### ZeppelinOS

- AdminUpgradeabilityProxy: Implementiert die Aktualisierbarkeit von Smart Contracts
- Initializable: Implementiert die Proxy-Initialisierung durch aktualisierbare Smart Contracts

#### OpenZeppelin

- Pausable: Implementiert das "Circuit Breaker Pattern / Notfall-Stopp" Entwurfsmuster, erweitert Ownable, um sicherzustellen, dass nur der Eigentümer stoppen kann
- SafeMath: Verwendet, um Integer-Überlauf- und Unterlaufprobleme zu vermeiden
- OraclizeAPI-Paket, usingOraclize, verwendet zur Überprüfung, ob ein YouTube-Video einem bestimmten Benutzer gehört und an ein urheberrechtlich geschütztes Werk gebunden ist

### Smart Contract Details

#### Manifestations.sol

Dieser Smart Contract wird für die Werkregistrierung verwendet, wobei die Metadaten des Werks (derzeit der Titel) und der IPFS-Hash des Inhalts mit der Identität des Autors (d.h. Ethereum-Kontoadresse) verknüpft werden, um den Werkbesitz zu beweisen. Dasselbe Werk kann als Einzelautor oder als gemeinschaftliche Autoren deklariert werden. Wenn außerdem versucht wird, ein neues Werk mit einem bereits registrierten Inhalts-Hash erneut zu registrieren, erkennt das System dies als Fehler.

#### UploadEvidences.sol

Dieser Smart Contract wird hauptsächlich für die Registrierung von Beweismaterialien verwendet, indem Beweise durch Hochladen des Werkdateiinhalts in das IPFS-Dateisystem registriert werden. Für dasselbe Werk können mehrere Beweise hinzugefügt werden (können aber nicht wiederholt hinzugefügt werden).

#### ExpirableLib.sol

Dieser Smart Contract wird hauptsächlich verwendet, um die Projektlogik für Werkerstellungs- und Ablaufzeiten zu verwalten und implementiert die zeitliche Wirksamkeit der Werkregistrierung (oder Einsprüche).

### Funktionen

Die Uright ÐApp bietet Musikern und Benutzern Dienste zur Verwaltung von Musikurheberrechten über einen Web-Client.

1. Urheberrechtsregistrierung: Generieren eines eindeutigen Hash-Wertes aus der Werkdatei, Registrieren des Werks des Musikers in der Blockchain, um das Urheberrecht zu beweisen.

![uright_register](https://image.pseudoyu.com/images/uright_register.png)

- Registrieren neuer Werke, die noch nie registriert wurden
- Registrieren von Werken mit bestehenden Registrierungseinträgen und Einlegen von Einsprüchen
- Hinzufügen von Beweismaterialien zum Nachweis des Urheberrechts am Werk

![uright_evidence_upload](https://image.pseudoyu.com/images/uright_evidence_upload.png)

![uright_youtube_evidence](https://image.pseudoyu.com/images/uright_youtube_evidence.png)

2. Urheberrechtsabruf: Überprüfen, ob ein Werk anhand seines Hash-Wertes registriert wurde

![uright_music_search](https://image.pseudoyu.com/images/uright_music_search.png)

- Meine Werke: Alle registrierten Werke des aktuellen Musikers finden
- Urheberrechtsbibliothek: Alle in der Blockchain registrierten Werke finden
- Details: Klicken Sie auf "Details", um detaillierte Informationen einschließlich aller hochgeladenen Beweise anzuzeigen

![uright_music_library](https://image.pseudoyu.com/images/uright_music_library.png)

3. Urheberrechtsverwaltung: Verwalten Sie die registrierten Werke, einschließlich der Möglichkeit, Beweise hinzuzufügen oder zu entfernen

![uright_manage](https://image.pseudoyu.com/images/uright_manage.png)

4. Blockchain-Explorer: Überprüfen Sie den Status der Blockchain und die Details der Transaktionen

![uright_explorer](https://image.pseudoyu.com/images/uright_explorer.png)

### Entwicklungsumgebung

- Truffle v5.1.39 (Core: 5.1.39)
- Solidity v0.5.16 (solc-js)
- Node v12.18.3
- Web3.js v1.2.1
- Angular CLI: 10.0.5
- Angular: 10.0.7

### Deployment

1. Klonen Sie das Repository

```bash
git clone https://github.com/pseudoyu/uright.git
```

2. Installieren Sie die erforderlichen Pakete

```bash
cd uright
npm install
```

3. Starten Sie die lokale Blockchain (ganache-cli)

```bash
ganache-cli
```

4. Kompilieren und migrieren Sie die Smart Contracts

```bash
truffle compile
truffle migrate
```

5. Starten Sie den Angular-Entwicklungsserver

```bash
ng serve
```

6. Öffnen Sie http://localhost:4200 in Ihrem Browser

### Testumgebung

- Chai: v4.2.0
- Mocha: 8.1.1

### Tests ausführen

```bash
truffle test
```

### Zukünftige Entwicklung

1. Implementierung der Einspruchsfunktion in der Web-Anwendung
2. Tokenisierung von Musikerwerken mit NFT-Technologie
3. Verbesserung der Benutzeroberfläche und Benutzererfahrung
4. Integration mit Streaming-Plattformen für automatische Urheberrechtsverfolgung
5. Implementierung eines Marktplatzes für den Handel mit Musikrechten

### Beitrag

Beiträge sind willkommen! Bitte fühlen Sie sich frei, Pull-Requests einzureichen oder Issues zu öffnen, um Verbesserungen oder neue Funktionen vorzuschlagen.

### Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Details finden Sie in der [LICENSE](https://github.com/pseudoyu/uright/blob/master/LICENSE)-Datei.

### Kontakt

Yu ZHANG - [@pseudoyu](https://github.com/pseudoyu) - pseudoyu@gmail.com

Projektlink: [https://github.com/pseudoyu/uright](https://github.com/pseudoyu/uright)