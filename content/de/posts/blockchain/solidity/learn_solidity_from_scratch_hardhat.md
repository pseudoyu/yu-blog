---
title: "Solidity Smart Contract Entwicklung - Verwendung des Hardhat Frameworks"
date: 2022-06-09T14:38:10+08:00
draft: false
tags: ["blockchain", "solidity", "ethereum", "web3", "smart contract", "javascript", "ethers.js", "hardhat", "yarn"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Vorwort

Nach den vorherigen Artikeln über Smart Contract Grundlagen, Web3.py und ethers.js haben wir die grundlegenden Kenntnisse zur direkten Interaktion mit Blockchain-Netzwerken durch Programme erworben. Für diejenigen, die damit nicht vertraut sind, können Sie folgende Artikel nachlesen:

- [Solidity Smart Contract Entwicklung - Grundlagen](https://www.pseudoyu.com/de/2022/05/25/learn_solidity_from_scratch_basic/)
- [Solidity Smart Contract Entwicklung - Beherrschung von Web3.py](https://www.pseudoyu.com/de/2022/05/30/learn_solidity_from_scratch_web3py/)
- [Solidity Smart Contract Entwicklung - Beherrschung von ethers.js](https://www.pseudoyu.com/de/2022/06/08/learn_solidity_from_scratch_ethersjs/)

In realen komplexen Geschäftsszenarien verwenden wir jedoch oft weiter gekapselte Frameworks wie HardHat, Brownie, Truffle usw. HardHat ist am weitesten verbreitet und verfügt über die leistungsfähigsten Plugin-Erweiterungen. Diese Serie wird sich ab diesem Artikel auf die Verwendung und Best Practices des Hardhat-Frameworks konzentrieren, und dieser Artikel wird dessen Installation, Konfiguration und Verwendung anhand eines einfachen Beispiels abschließen.

Dieser Artikel ist eine Zusammenfassung des Lernens aus [Patrick Collins](https://twitter.com/PatrickAlphaC)' Tutorial ["Learn Blockchain, Solidity, and Full Stack Web3 Development with JavaScript"](https://www.youtube.com/watch?v=gyMwXuJrbJQ). Es wird dringend empfohlen, das originale Tutorial-Video für weitere Details anzusehen.

Sie können [hier](https://github.com/pseudoyu/learn-solidity/tree/master/hardhat_simple_storage) auf das Code-Repository für dieses Test-Demo zugreifen.

## Einführung in Hardhat

![hardhat_homepage](https://image.pseudoyu.com/images/hardhat_homepage.png)

Hardhat ist eine JavaScript-basierte Entwicklungsumgebung für Smart Contracts, die zur flexiblen Kompilierung, Bereitstellung, Testung und Fehlersuche von EVM-basierten Smart Contracts verwendet werden kann. Es bietet eine Reihe von Toolchains zur Integration von Code mit externen Werkzeugen und bietet ein reichhaltiges Plugin-Ökosystem zur Verbesserung der Entwicklungseffizienz. Darüber hinaus stellt es auch einen lokalen Hardhat-Netzwerkknoten bereit, der Ethereum simuliert und leistungsstarke lokale Debugging-Fähigkeiten bietet.

Seine GitHub-Adresse ist [NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat), und Sie können seine [offizielle Dokumentation](https://hardhat.org/getting-started) besuchen, um mehr zu erfahren.

## Verwendung von Hardhat

### Initialisierung des Projekts

Um ein Hardhat-Projekt von Grund auf zu erstellen, müssen wir zunächst die `node.js` und `yarn` Umgebungen vorinstallieren. Dieser Teil kann gemäß den offiziellen Anweisungen basierend auf Ihrer Systemumgebung installiert werden.

Zuerst müssen wir das Projekt initialisieren und das `hardhat` Abhängigkeitspaket installieren.

```bash
yarn init
yarn add --dev hardhat
```

![yarn_add](https://image.pseudoyu.com/images/yarn_add.png)

### Initialisierung von Hardhat

Dann müssen wir `yarn hardhat` ausführen, um durch interaktive Befehle zu initialisieren. Konfigurieren Sie es entsprechend den Projektanforderungen. Für unser Test-Demo wählen wir die Standardwerte.

![hardhat_project_init](https://image.pseudoyu.com/images/hardhat_project_init.png)

### Optimierung der Code-Formatierung

#### VS Code Konfiguration

Ich entwickle Code lokal mit VS Code. Sie können den Code formatieren, indem Sie die Plugins `Solidity + Hardhat` und `Prettier` installieren. Sie können die VS Code-Einstellungen öffnen und die folgende Formatierungskonfiguration in `settings.json` hinzufügen:

```json
{
    //...

    "[solidity]": {
        "editor.defaultFormatter": "NomicFoundation.hardhat-solidity"
    },
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
    }
}
```

#### Projektkonfiguration

Um die Code-Formatierungsstile von Entwicklern, die verschiedene Projekte verwenden, zu vereinheitlichen, können wir auch `prettier` und das `prettier-plugin-solidity` Plugin für das Projekt konfigurieren:

```bash
yarn add --dev prettier prettier-plugin-solidity
```

![yarn_add_prettier_plugin](https://image.pseudoyu.com/images/yarn_add_prettier_plugin.png)

Nach dem Hinzufügen der Abhängigkeiten können Sie `.prettierrc` und `.prettierignore` Konfigurationsdateien im Projektverzeichnis hinzufügen, um die Formatierung zu vereinheitlichen:

Meine `.prettierrc` Konfiguration ist:

```json
{
    "tabWidth": 4,
    "useTabs": false,
    "semi": false,
    "singleQuote": false
}
```

Meine `.prettierignore` Konfiguration ist:

```plaintext
node_modules
package.json
img
artifacts
cache
coverage
.env
.*
README.md
coverage.json
```

### Kompilierung von Verträgen

Es ist nicht notwendig, den `compile` Befehl wie in `ethers.js` anzupassen. HardHat bietet einen eingebauten `compile` Befehl. Sie können Verträge im Verzeichnis `contracts` platzieren und sie dann mit dem Befehl `yarn hardhat compile` kompilieren:

![hardhat_compile_contract](https://image.pseudoyu.com/images/hardhat_compile_contract.png)

### Hinzufügen von `dotenv` Unterstützung

Bevor wir mit dem Schreiben von Bereitstellungsskripten beginnen, lassen Sie uns das `dotenv` Plugin konfigurieren. Auf diese Weise können wir `dotenv` verwenden, um Umgebungsvariablen zu erhalten. Während der Entwicklung werden wir mit vielen privaten Informationen umgehen, wie zum Beispiel privaten Schlüsseln usw. Wir möchten sie in einer `.env` Datei speichern oder direkt im Terminal setzen, wie zum Beispiel unser `RINKEBY_PRIVATE_TOKEN`. Auf diese Weise können wir `process.env.RINKEBY_PRIVATE_TOKEN` verwenden, um den Wert im Bereitstellungsskript zu erhalten, ohne ihn explizit im Code zu schreiben, was das Risiko einer Privatsphärenverletzung reduziert.

#### Installation von `dotenv`

```bash
yarn add --dev dotenv
```

![yarn_add_dotenv](https://image.pseudoyu.com/images/yarn_add_dotenv.png)

#### Festlegen von Umgebungsvariablen

In der `.env` Datei können wir Umgebungsvariablen festlegen, wie zum Beispiel:

```plaintext
RINKEBY_RPC_URL=url
RINKEBY_PRIVATE_KEY=0xkey
ETHERSCAN_API_KEY=key
COINMARKETCAP_API_KEY=key
```

Wir können dann Umgebungsvariablen in `hardhat.config.js` lesen:

```javascript
require("dotenv").config()

const RINKEBY_RPC_URL =
    process.env.RINKEBY_RPC_URL || "https://eth-rinkeby/example"
const RINKEBY_PRIVATE_KEY = process.env.RINKEBY_PRIVATE_KEY || "0xkey"
const ETHERSCAN_API_KEY = process.env.ETHERSCAN_API_KEY || "key"
const COINMARKETCAP_API_KEY = process.env.COINMARKETCAP_API_KEY || "key"
```

### Konfiguration der Netzwerkumgebung

Oft müssen unsere Verträge auf verschiedenen Blockchain-Netzwerken laufen, wie lokale Tests, Entwicklungs- und Produktionsumgebungen. Hardhat bietet auch eine bequeme Möglichkeit, Netzwerkumgebungen zu konfigurieren.

#### Starten des Netzwerks

Wir können direkt ein Skript ausführen, um ein Netzwerk zu starten, das mit Hardhat mitgeliefert wird, aber dieses Netzwerk existiert nur während der Skriptausführung. Um ein lokal nachhaltiges Netzwerk zu starten, müssen Sie den Befehl `yarn hardhat node` ausführen:

![hardhat_localhost_node](https://image.pseudoyu.com/images/hardhat_localhost_node.png)

Nach der Ausführung werden Testnetzwerke und Testkonten für die anschließende Entwicklung und Fehlersuche generiert.

Wir können auch unsere eigenen Testnetzwerk-Knoten über Plattformen wie Alchemy oder Infura generieren und ihre `RPC_URL` für die Programmverbindung aufzeichnen.

#### Definition von Netzwerken

Nach der Vorbereitung der Netzwerkumgebung können wir Netzwerke in der Projektkonfiguration `hardhat.config.js` definieren:

```javascript
const RINKEBY_RPC_URL =
    process.env.RINKEBY_RPC_URL || "https://eth-rinkeby/example"
const RINKEBY_PRIVATE_KEY = process.env.RINKEBY_PRIVATE_KEY || "0xkey"

module.exports = {
    defaultNetwork: "hardhat",
    networks: {
        locakhost: {
            url: "http://localhost:8545",
            chainId: 31337,
        },
        rinkeby: {
            url: RINKEBY_RPC_URL,
            accounts: [RINKEBY_PRIVATE_KEY],
            chainId: 4,

        },
    },
    // ...,
}
```

### Skripte

In einem Hardhat-Projekt können wir Funktionen wie die Bereitstellung implementieren, indem wir Skripte im Verzeichnis `scripts` schreiben und Skripte durch bequeme Befehle ausführen.

#### Schreiben von Bereitstellungsskripten

Als Nächstes beginnen wir mit dem Schreiben des `deploy.js` Skripts.

Zuerst müssen wir notwendige Pakete aus `hardhat` importieren:

```javascript
const { ethers, run, network } = require("hardhat")
```

Dann schreiben wir die `main` Methode, die unsere Kern-Bereitstellungslogik enthält:

```javascript
async function main() {
    const SimpleStorageFactory = await ethers.getContractFactory(
        "SimpleStorage"
    )
    console.log("Deploying SimpleStorage Contract...")
    const simpleStorage = await SimpleStorageFactory.deploy()
    await simpleStorage.deployed()
    console.log("SimpleStorage Contract deployed at:", simpleStorage.address)

    // Aktuellen Wert abrufen
    const currentValue = await simpleStorage.retrieve()
    console.log("Current value:", currentValue)

    // Wert setzen
    const transactionResponse = await simpleStorage.store(7)
    await transactionResponse.wait(1)

    // Aktualisierten Wert abrufen
    const updatedValue = await await simpleStorage.retrieve()
    console.log("Updated value:", updatedValue)
}
```

Schließlich führen wir unsere `main` Methode aus:

```javascript
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error)
        process.exit(1)
    })
```

#### Ausführen von Skripten

Nach Abschluss des Skriptschreibens können Sie das Skript mit dem von Hardhat bereitgestellten `run` Befehl ausführen.

Wenn kein Netzwerkparameter hinzugefügt wird, wird standardmäßig das `hardhat` Netzwerk verwendet. Sie können das Netzwerk mit dem Parameter `--network` angeben:

```bash
yarn hardhat run scripts/deploy.js --network rinkeby
```

![hardhat_deploy_rinkeby](https://image.pseudoyu.com/images/hardhat_deploy_rinkeby.png)

### Hinzufügen von Etherscan-Vertragsverifizierungsunterstützung

Nach der Bereitstellung des Vertrags im Rinkeby-Testnetzwerk können Sie die Vertragsadresse auf Etherscan anzeigen und verifizieren. Wir können dies über die Website tun, aber Hardhat bietet Plugin-Unterstützung, die es bequemer macht, Verifizierungsoperationen durchzuführen.

#### Installation des hardhat-etherscan Plugins

Wir installieren das Plugin mit dem Befehl `yarn add --dev @nomiclabs/hardhat-etherscan`.

![yarn_add_etherscan_verify_support](https://image.pseudoyu.com/images/yarn_add_etherscan_verify_support.png)

#### Aktivierung der Etherscan-Vertragsverifizierungsunterstützung

Nach der Installation müssen wir in `hardhat.config.js` konfigurieren:

```javascript
require("@nomiclabs/hardhat-etherscan")

module.exports = {
    // ...,
    etherscan: {
        apiKey: ETHERSCAN_API_KEY,
    },
    // ...,
}
```

#### Definition der Verifizierungsmethode

Als Nächstes müssen wir eine `verify` Methode im Bereitstellungsskript `deploy.js` hinzufügen.

```javascript
const { ethers, run, network } = require("hardhat")

async function verify(contractAddress, args) {
    console.log("Verifying SimpleStorage Contract...")
    try {
        await run("verify:verify", {
            address: contractAddress,
            constructorArguements: args,
        })
    } catch (e) {
        if (e.message.toLowerCase().includes("already verified!")) {
            console.log("Already Verified!")
        } else {
            console.log(e)
        }
    }
}
```

In dieser Methode rufen wir die `run` Methode aus dem `hardhat` Paket auf, übergeben einen `verify` Befehl und übergeben einen Parameter `{ address: contractAddress, constructorArguements: args }`. Da unser Vertrag möglicherweise bereits auf Etherscan verifiziert wurde, führen wir eine `try...catch...` Fehlerbehandlung durch. Wenn er bereits verifiziert ist, wird ein Fehler geworfen und eine Meldung ausgegeben, ohne unseren Bereitstellungsprozess zu beeinträchtigen.

#### Einrichten des Post-Deployment-Aufrufs

Nachdem wir unsere `verify` Methode definiert haben, können wir sie im Bereitstellungsskript aufrufen:

```javascript
async function main() {
    //...

    if (network.config.chainId === 4 && process.env.ETHERSCAN_API_KEY) {
        await simpleStorage.deployTransaction.wait(6)
        await verify(simpleStorage.address, [])
    }

    // ...
}
```

Hier haben wir zwei besondere Behandlungen vorgenommen.

Erstens müssen wir den Vertrag nur im `rinkeby` Netzwerk verifizieren, nicht in lokalen oder anderen Netzwerkumgebungen. Daher prüfen wir `network.config.chainId`. Wenn es `4` ist, führen wir die Verifizierungsoperation durch; andernfalls nicht. Außerdem führen wir die Verifizierungsoperation nur durch, wenn eine `ETHERSCAN_API_KEY` Umgebungsvariable vorhanden ist.

Außerdem benötigt Etherscan möglicherweise etwas Zeit nach der Bereitstellung, um die Vertragsadresse zu erhalten, daher haben wir `.wait(6)` konfiguriert, um 6 Blöcke vor der Verifizierung zu warten.

Der Ausführungseffekt ist wie folgt:

![hardhat_verify_contract_etherscan](https://image.pseudoyu.com/images/hardhat_verify_contract_etherscan.png)

![verified_contract_on_etherscan](https://image.pseudoyu.com/images/verified_contract_on_etherscan.png)

Nach der Verifizierung durch Etherscan können wir direkt den Vertragsquellcode einsehen und damit interagieren.

![interact_with_contract_on_etherscan](https://image.pseudoyu.com/images/interact_with_contract_on_etherscan.png)

### Vertragstests

Bei Smart Contracts müssen die meisten Operationen on-chain bereitgestellt werden, mit Vermögenswerten interagieren, Gas verbrauchen, und sobald es Sicherheitslücken gibt, wird es schwerwiegende Folgen haben. Daher müssen wir detaillierte Tests an Smart Contracts durchführen.

Hardhat bietet umfassende Test- und Debugging-Tools. Wir können Testskripte im Verzeichnis `tests` schreiben und Tests mit dem Befehl `yarn hardhat test` ausführen.

#### Schreiben von Testskripten

Lassen Sie uns ein `test-deploy.js` Testprogramm für unser Bereitstellungsskript schreiben. Zuerst müssen wir die notwendigen Pakete importieren:

```javascript
const { assert } = require("chai")
const { ethers } = require("hardhat")
```

Dann schreiben wir die Testlogik:

```javascript
describe("SimpleStorage", () => {
    let simpleStorageFactory, simpleStorage
    beforeEach(async () => {
        simpleStorageFactory = await ethers.getContractFactory("SimpleStorage")
        simpleStorage = await simpleStorageFactory.deploy()
    })

    it("Should start with a favorite number of 0", async () => {
        const currentValue = await simpleStorage.retrieve()
        const expectedValue = "0"

        assert.equal(currentValue.toString(), expectedValue)
        // expect(currentValue.toString()).to.equal(expectedValue)
    })

    it("Should update when we call store", async () => {
        const expectedValue = "7"
        const transactionRespense = await simpleStorage.store(expectedValue)
        await transactionRespense.wait(1)

        const currentValue = await simpleStorage.retrieve()

        assert.equal(currentValue.toString(), expectedValue)
        // expect(currentValue.toString()).to.equal(expectedValue)
    })
```

Im Testskript von Hardhat verwenden wir `describe`, um die Testklasse zu umschließen, und `it`, um die Testmethode zu umschließen. Wir müssen sicherstellen, dass der Vertrag vor dem Testen bereitgestellt wird, daher verwenden wir die `beforeEach` Methode, um `simpleStorageFactory.deploy()` vor jeder Testmethode aufzurufen und das zurückgegebene `simpleStorage` Objekt der `simpleStorage` Variable zuzuweisen.

Wir verwenden `assert.equal(currentValue.toString(), expectedValue)`, um das Ausführungsergebnis mit dem erwarteten Ergebnis zu vergleichen. Es kann durch `expect(currentValue.toString()).to.equal(expectedValue)` ersetzt werden, was den gleichen Effekt hat.

Darüber hinaus können wir `it.only()` verwenden, um zu spezifizieren, dass nur eine der Testmethoden ausgeführt wird.

#### Ausführen von Testskripten

Wir führen den Test mit `yarn hardhat test` aus und können Testmethoden mit `yarn hardhat test --grep store` spezifizieren.

![hardhat_run_tests](https://image.pseudoyu.com/images/hardhat_run_tests.png)

### Hinzufügen von `gas-reporter` Unterstützung

Wie oben erwähnt, ist Gas eine Ressource, auf die wir während der Entwicklung besonders achten müssen, insbesondere teuer im Ethereum-Mainnet. Daher müssen wir den Gasverbrauch während des Testens überprüfen. HardHat hat auch ein `gas-reporter` Plugin, das bequem Gasverbrauchsinformationen ausgeben kann.

#### Installation des `gas-reporter` Plugins

Wir installieren das Plugin mit dem Befehl `yarn add --dev hardhat-gas-reporter`:

![yarn_add_gas_reporter](https://image.pseudoyu.com/images/yarn_add_gas_reporter.png)

#### Aktivierung der `gas-reporter` Unterstützung

Wir aktivieren das Plugin, indem wir `gasReporter: true` und zusätzliche Konfigurationselemente in `hardhat.config.js` hinzufügen:

```javascript
require("hardhat-gas-reporter")

const COINMARKETCAP_API_KEY = process.env.COINMARKETCAP_API_KEY || "key"

module.exports = {
    // ...,
    gasReporter: {
        enabled: true,
        outputFile: "gas-reporter.txt",
        noColors: true,
        currency: "USD",
        coinmarketcap: COINMARKETCAP_API_KEY,
        token: "MATIC",
    },
}
```

Wir können Ausgabedatei, ob Farben aktiviert werden sollen, Währung, Token-Name und CoinMarketCap API-Schlüssel angeben, um die Ausgabe gemäß dem Projekt weiter zu steuern.

Gemäß der obigen Konfiguration erzeugt die Ausführung von `yarn hardhat test` den folgenden Effekt:

![hardhat_add_gas_reporter_support_and_export](https://image.pseudoyu.com/images/hardhat_add_gas_reporter_support_and_export.png)

### Hinzufügen von `solidity-coverage` Unterstützung

Vertragstests sind entscheidend für die Sicherstellung der Korrektheit der Geschäftslogik und der Sicherheitsvorbeugung. Daher müssen wir Abdeckungstests an Verträgen durchführen. HardHat hat auch ein `solidity-coverage` Plugin, das bequem Abdeckungsinformationen ausgeben kann.

#### Installation des `solidity-coverage` Plugins

Wir installieren das Plugin mit dem Befehl `yarn add --dev solidity-coverage`:

![yarn_add_coverage_support](https://image.pseudoyu.com/images/yarn_add_coverage_support.png)

#### Aktivierung der `solidity-coverage` Unterstützung

Wir müssen nur das Paket in `hardhat.config.js` importieren, um Unterstützung für Abdeckungstests hinzuzufügen:

```javascript
require("solidity-coverage")
```

#### Durchführung des Abdeckungstests

Führen Sie den Abdeckungstest mit `yarn hardhat coverage` durch:

![hardhat_coverage](https://image.pseudoyu.com/images/hardhat_coverage.png)

### Aufgabe

Oben haben wir einige grundlegende Funktionen und Skripte der `hardhat` Bibliothek verwendet. Darüber hinaus können wir auch einige Aufgaben für die Entwicklung und Fehlersuche anpassen.

#### Schreiben von Aufgaben

In Hardhat definieren wir Aufgaben im Verzeichnis `tasks`. Wir werden eine `block-number.js` Aufgabe schreiben, um die Blockhöhe zu erhalten:

```javascript
const { task } = require("hardhat/config")

task("block-number", "Prints the current block number").setAction(
    async (taskArgs, hre) => {
        const blockNumber = await hre.ethers.provider.getBlockNumber()
        console.log(`Current Block Number: ${blockNumber}`)
    }
)
```

Aufgaben werden mit der Methode `task()` erstellt und die Ausführungsfunktion wird mit der Methode `setAction()` festgelegt. Hier ist `taskArgs` ein Objekt, das alle Parameter enthält, und `hre` ist ein `HardhatRuntimeEnvironment` Objekt, das verwendet werden kann, um andere Ressourcen zu erhalten.

#### Ausführen von Aufgaben

Nach der Definition wird unsere neu definierte `block-number` Aufgabe in den `AVAILABLE TASKS` des Projektbefehls erscheinen. Sie können die Aufgabe mit dem Befehl `yarn hardhat block-number` ausführen. Ebenso können wir ein bestimmtes Netzwerk für die Ausführung angeben:

```bash
yarn hardhat block-number --network rinkeby
```

![hardhat_run_tasks](https://image.pseudoyu.com/images/hardhat_run_tasks.png)

### Hardhat Konsole

Schließlich können wir neben der Interaktion mit der Kette/dem Vertrag durch Code auch Projekte debuggen, den Kettenstatus, Vertragseingaben und -ausgaben usw. durch die `Hardhat Konsole` einsehen. Wir können die Hardhat Konsole öffnen und mit dem Befehl `yarn hardhat console` interagieren.

![hardhat_console](https://image.pseudoyu.com/images/hardhat_console.png)

## Fazit

Das oben Genannte ist meine grundlegende Konfiguration und Verwendung des Hardhat-Frameworks. Es ist ein sehr leistungsfähiges Entwicklungsframework, und ich werde in Zukunft weiter in mehr seiner Funktionen und Anwendungstechniken eintauchen. Wenn Sie interessiert sind, können Sie weiterhin folgen. Ich hoffe, dies ist für alle hilfreich.

## Referenzen

> 1. [Learn Blockchain, Solidity, and Full Stack Web3 Development with JavaScript](https://www.youtube.com/watch?v=gyMwXuJrbJQ)
> 2. [NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat)
> 3. [Hardhat Offizielle Dokumentation](https://hardhat.org/getting-started)
> 4. [Solidity Smart Contract Entwicklung - Grundlagen](https://www.pseudoyu.com/de/2022/05/25/learn_solidity_from_scratch_basic/)
> 5. [Solidity Smart Contract Entwicklung - Beherrschung von Web3.py](https://www.pseudoyu.com/de/2022/05/30/learn_solidity_from_scratch_web3py/)
> 6. [Solidity Smart Contract Entwicklung - Beherrschung von ethers.js](https://www.pseudoyu.com/de/2022/06/08/learn_solidity_from_scratch_ethersjs/)