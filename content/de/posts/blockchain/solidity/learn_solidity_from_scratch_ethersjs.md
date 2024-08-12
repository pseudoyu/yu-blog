---
title: "Solidity Smart Contract Entwicklung - Beherrschung von ethers.js"
date: 2022-06-08T00:25:45+08:00
draft: false
tags: ["blockchain", "solidity", "ethereum", "web3", "smart contract", "javascript", "ethers.js"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《後來的我們 - 五月天》" >}}

## Vorwort

Im vorherigen Artikel "[Solidity Smart Contract Entwicklung - Grundlagen](https://www.pseudoyu.com/de/2022/05/25/learn_solidity_from_scratch_basic/)" haben wir die grundlegende Syntax von Solidity kennengelernt und verstanden, dass wir mit Frameworks wie [Brownie](https://github.com/eth-brownie/brownie) und [HardHat](https://github.com/NomicFoundation/hardhat) debuggen können. In einem weiteren Artikel "[Solidity Smart Contract Entwicklung - Beherrschung von Web3.py](https://www.pseudoyu.com/de/2022/05/30/learn_solidity_from_scratch_web3py/)" haben wir auch direkt mit unserem lokalen Ganache-Node mittels Web3.py interagiert.

Ursprünglich hatte ich geplant, aufgrund meiner größeren Vertrautheit mit Python, das Brownie-Framework für die weitere Entwicklung zu verwenden. Nach einiger Recherche stellte ich jedoch fest, dass in der Branche überwiegend das HardHat-Framework verwendet wird, das auch mehr Erweiterungen bietet. Zudem wurde das Solidity-Tutorial, dem ich folge, auf eine [Javascript-Version](https://www.youtube.com/watch?v=gyMwXuJrbJQ) aktualisiert, weshalb ich beschloss, es zu erlernen.

Um die Prinzipien besser zu verstehen und eine gute Grundlage für unsere spätere Verwendung des Frameworks zu schaffen, werden wir diesmal [ethers.js](https://github.com/ethers-io/ethers.js/) verwenden, um mit unserem auf der [Alchemy](https://dashboard.alchemyapi.io)-Plattform bereitgestellten Rinkeby-Testnetzwerk zu interagieren. Wir werden die grundlegende Vertragskompilierung, die Bereitstellung im Rinkeby-Netzwerk und die Interaktion mit dem Vertrag implementieren.

Sie können [hier](https://github.com/pseudoyu/learn-solidity/tree/master/ethers_simple_storage) auf das Code-Repository für dieses Test-Demo zugreifen.

## ethers.js

ethers.js ist eine Open-Source-Bibliothek für Javascript, die mit dem Ethereum-Netzwerk interagieren kann. Ihre GitHub-Adresse lautet [ethers.io/ethers.js](https://github.com/ethers-io/ethers.js/), und Sie können ihre [offizielle Dokumentation](https://docs.ethers.io/) für die Verwendung besuchen.

### Installation

Wir können `ethers.js` mit yarn wie folgt installieren:

```bash
yarn add ethers
```

![yarn_add_ethers](https://image.pseudoyu.com/images/yarn_add_ethers.png)

### Verwendung

Importieren Sie die Bibliothek mit `require`, um sie zu verwenden

```javascript
const ethers = require('ethers');
```

## Kompilierung des Solidity-Vertrags

### Quellcode des Vertrags

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract SimpleStorage {
    uint256 favoriteNumber;
    bool favoriteBool;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People public person = People({favoriteNumber: 2, name: "Arthur"});

    People[] public people;

    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public returns (uint256) {
        favoriteNumber = _favoriteNumber;
        return favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
```

Dies ist ein einfacher Speichervertrag, der ein People-Strukturobjekt verwendet, um den Namen einer Person und ihre Lieblingszahl zu speichern, ein Array verwendet, um Informationen für mehrere Personen zu speichern, und Methoden zum Hinzufügen und Suchen bereitstellt.

### Lesen der Vertragssquelldatei

Nachdem wir das Schreiben und die Syntaxprüfung des Solidity-Vertrags durch VSCode oder andere Editoren abgeschlossen haben, müssen wir den Vertrag in eine ABI-Datei und Bytecode kompilieren.

Wir können das `solc`-Kommandozeilentool über `yarn` für die Bearbeitung installieren, und wir können die entsprechende Version wählen. Der Befehl lautet wie folgt:

```bash
yarn add solc@0.8.7-fixed
```

Nach der Installation können wir den `solcjs`-Befehl zur Kompilierung verwenden. Der Befehl lautet wie folgt:

```bash
yarn solcjs --bin --abi --include-path node_modules/ --base-path . -o . SimpleStorage.sol
```

Da das Kompilieren von Verträgen eine häufige Operation ist, können wir den `compile`-Skriptbefehl in `package.json` wie folgt konfigurieren:

```json
"scripts": {
    "compile": "yarn solcjs --bin --abi --include-path node_modules/ --base-path . -o . SimpleStorage.sol"
}
```

Danach müssen Sie nur noch `yarn compile` ausführen, um die Vertragskompilierungsdateien zu generieren.

### Erhalt der Kompilierungsergebnisse

Nach der Kompilierung werden ABI- und Bytecode-Dateien generiert, mit `.bin` bzw. `.abi` als Suffixe.

#### Erhalt von Bytecode und ABI

Die Bereitstellung und Interaktion von Solidity-Verträgen erfordern zwei Teile: Bytecode und ABI. Wir können sie durch den folgenden Code in entsprechende Variablen für nachfolgende Operationen schreiben.

```javascript
const fs = require('fs-extra');

const abi = fs.readFileSync("./SimpleStorage_sol_SimpleStorage.abi", "utf-8");
const binary = fs.readFileSync("./SimpleStorage_sol_SimpleStorage.bin", "utf-8");
```

## Erstellung einer Rinkeby-Testnetzwerkumgebung (Alchemy)

Das Debuggen von Smart Contracts erfordert die Bereitstellung des Vertrags in einer tatsächlichen Kette. Wir wählen die Bereitstellung im Rinkeby-Testnetzwerk auf der Alchemy-Plattform für nachfolgendes Debugging und Entwicklung.

### Alchemy-Plattform

Zunächst besuchen wir die [offizielle Alchemy-Website](https://dashboard.alchemyapi.io), registrieren uns und melden uns an, und wir sehen ihr Dashboard, das alle erstellten Anwendungen anzeigt.

![alchemy_dashboard](https://image.pseudoyu.com/images/alchemy_dashboard.png)

Nach der Installation wählen Sie Create App, um schnell einen Rinkeby-Testnetzwerk-Node zu erstellen.

![alchemy_create_app](https://image.pseudoyu.com/images/alchemy_create_app.png)

Nach der Erstellung klicken Sie auf View Details, um die detaillierten Informationen der App zu sehen, die wir gerade erstellt haben. Klicken Sie oben rechts auf View Key, um unsere Node-Informationen abzufragen. Wir müssen die HTTP-URL für die spätere Verbindung notieren.

![alchemy_app_detail](https://image.pseudoyu.com/images/alchemy_app_detail.png)

## Erstellung eines Rinkeby-Testkontos (MetaMask)

### MetaMask

Nachdem wir die Rinkeby-Testnetzwerkumgebung erstellt haben, müssen wir ein Konto über MetaMask erstellen, einige Test-Token erhalten und den privaten Schlüssel des Kontos für die spätere Verwendung notieren.

![metamask_private_key](https://image.pseudoyu.com/images/metamask_private_key.png)

### Erhalt von Test-Token

Nach der Erstellung eines Kontos benötigen wir einige Test-Token für die nachfolgende Entwicklung und das Debugging. Wir können sie über die folgenden URLs erhalten:

- https://faucets.chain.link
- https://rinkebyfaucet.com/

## Verbindung zum Test-Node und Wallet

### Verbindung zum Node

`ethers.js` bietet eine Bibliothek, die sich leicht mit unserem Test-Node verbinden lässt, wobei `process.env.ALCHEMY_RPC_URL` die HTTP-URL der App ist, die wir auf der Alchemy-Plattform erstellt haben:

```javascript
const ethers = require('ethers');

const provider = new ethers.providers.JsonRpcProvider(process.env.ALCHEMY_RPC_URL);
```

### Verbindung zur Wallet

`ethers.js` bietet auch eine Methode, um sich mit unserer Test-Wallet zu verbinden, wobei `process.env.RINKEBY_PRIVATE_KEY` der private Schlüssel ist, den wir aus MetaMask kopiert haben.

```javascript
const ethers = require('ethers');

const wallet = new ethers.Wallet(
	process.env.RINKEBY_PRIVATE_KEY,
	provider
);
```

## Bereitstellung des Solidity-Vertrags

### Erstellung des Vertrags

Wir können einen Vertrag über die `ethers.js`-Bibliothek erstellen.

```javascript
const contractFactory = new ethers.ContractFactory(abi, binary, wallet);
```

### Bereitstellung des Vertrags

Nachfolgend werden wir erläutern, wie man einen Vertrag über die `ethers.js`-Bibliothek bereitstellt, wobei die ABI- und BIN-Dateien des `SimpleStorage`-Vertrags bereits im obigen Code eingelesen wurden.

#### Erstellung des Vertrags

```javascript
const contractFactory = new ethers.ContractFactory(abi, binary, wallet);
```

#### Bereitstellung des Vertrags

```javascript
const contract = await contractFactory.deploy();
await contract.deployTransaction.wait(1);
```

### Interaktion mit dem Vertrag

Wir können auch mit dem Vertrag über `ethers.js` interagieren.

#### retrieve()

```javascript
const currentFavoriteNumber = await contract.retrieve();
```

#### store()

```javascript
const transactionResponse = await contract.store("7")
const transactionReceipt = await transactionResponse.wait(1);
```

### Konstruktion einer Transaktion aus Rohdaten

Zusätzlich zum direkten Aufruf von Methoden zur Bereitstellung von Verträgen können wir auch selbst Transaktionen konstruieren.

#### Konstruktion der Transaktion

```javascript
const nonce = await wallet.getTransactionCount();
const tx = {
	nonce: nonce,
	gasPrice: 20000000000,
	gasLimit: 1000000,
	to: null,
	value: 0,
	data: "0x" + binary,
	chainId: 1337,
};
```

#### Signierung der Transaktion

```javascript
const signedTx = await wallet.signTransaction(tx);
```

#### Senden der Transaktion

```javascript
const sentTxResponse = await wallet.sendTransaction(tx);
await sentTxResponse.wait(1);
```

## Fazit

Dies sind die Schritte zur Interaktion mit dem Rinkeby-Testnetzwerk von Alchemy über die `ethers.js`-Bibliothek. In der tatsächlichen Projektentwicklung verwenden wir im Allgemeinen nicht direkt Bibliotheken wie `ethers.js`, sondern weiter gekapselte Frameworks wie Brownie und HardHat. Das Verständnis der Verwendung von Bibliotheken wie `Web3.py` oder `ethers.js` ist jedoch ebenfalls sehr wichtig. Ich werde in Zukunft die Verwendung des HardHat-Frameworks weiter erläutern.

## Referenzen

> 1. [Solidity Smart Contract Entwicklung - Grundlagen](https://www.pseudoyu.com/de/2022/05/25/learn_solidity_from_scratch_basic/)
> 2. [Solidity Smart Contract Entwicklung - Beherrschung von Web3.py](https://www.pseudoyu.com/de/2022/05/30/learn_solidity_from_scratch_web3py/)
> 3. [Solidity, Blockchain und Smart Contract - Javascript-Version](https://www.youtube.com/watch?v=gyMwXuJrbJQ)
> 4. [ethers.js Projektrepository](https://github.com/ethers-io/ethers.js/)
> 5. [ethers.js Offizielle Dokumentation](https://docs.ethers.io/)
> 6. [Alchemy Offizielle Website](https://dashboard.alchemyapi.io)