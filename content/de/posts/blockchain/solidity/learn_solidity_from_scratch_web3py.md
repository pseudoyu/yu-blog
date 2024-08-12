---
title: "Solidity Smart Contract Entwicklung - Meistern von Web3.py"
date: 2022-05-30T15:25:45+08:00
draft: false
tags: ["blockchain", "solidity", "ethereum", "web3", "smart contract", "python"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Vorwort

Im vorherigen Artikel "[Solidity Smart Contract Entwicklung - Grundlagen](https://www.pseudoyu.com/de/2022/05/25/learn_solidity_from_scratch_basic/)" haben wir die grundlegende Syntax von Solidity kennengelernt und verstanden, dass wir mit Frameworks wie [Brownie](https://github.com/eth-brownie/brownie) und [HardHat](https://github.com/NomicFoundation/hardhat) debuggen können. Bevor wir jedoch diese vorgefertigten Frameworks verwenden, können wir mit Web3.py direkt mit unserem lokalen Ganache-Node interagieren, um die Prinzipien besser zu verstehen und eine solide Grundlage für unsere spätere Verwendung von Frameworks zu schaffen.

In diesem Artikel wird Web3.py als Beispiel verwendet, um die grundlegende Vertragskompilierung, Bereitstellung im lokalen Ganache-Netzwerk und Interaktion mit Verträgen zu implementieren.

Sie können [hier](https://github.com/pseudoyu/learn-solidity/tree/master/web3_py_simple_storage) auf das Code-Repository für dieses Test-Demo zugreifen.

## Web3.py

Web3.py ist eine Open-Source-Bibliothek für Python, die eine einfache API bereitstellt, mit der wir über Python-Programme mit dem Ethereum-Netzwerk interagieren können. Die GitHub-Adresse lautet [ethereum/web3.py](https://github.com/ethereum/web3.py), und Sie können die [offizielle Dokumentation](https://web3py.readthedocs.io/en/stable/) für die Verwendung besuchen.

### Installation

Wir können Web3.py mit dem Python-Paketmanagement-Tool pip installieren, wie folgt:

```bash
pip3 install web3
```

![pip_install_web3](https://image.pseudoyu.com/images/pip_install_web3.png)

### Verwendung

Importieren Sie einfach die erforderlichen Methoden mit `import`, um sie zu verwenden

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
```

## Solidity-Vertragskompilierung

### Vertragsquellcode

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

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

### Lesen der Vertragsquelldatei

Nachdem wir das Schreiben und die Syntaxprüfung des Solidity-Vertrags mit VSCode oder anderen Editoren abgeschlossen haben, müssen wir die Vertragsquelldatei lesen und in einer Variable für die anschließende Kompilierung speichern.

```python
import os

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
```

Der obige Code liest den Inhalt der Datei `SimpleStorage.sol` in die Variable `simple_storage_file` ein.

### Kompilieren des Vertrags

#### Installation von `solcx`

Die Vertragskompilierung erfordert die vorherige Installation des `solcx`-Tools.

```bash
pip3 install py-solc-x
```

![pip_install_solcx](https://image.pseudoyu.com/images/pip_install_solcx.png)

#### Importieren von `solcx`

Verwenden Sie `import`, um die erforderlichen Methoden zu importieren

```python
from solcx import compile_standard, install_solc
```

#### Kompilierung

```python
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
```

Im obigen Code haben wir Version 0.6.0 des Solidity-Kompilierungsprogramms installiert, die `compile_standard`-Methode aus der `solcx`-Bibliothek verwendet, um die zuvor gelesene Vertragsquelldatei zu kompilieren, und das Kompilierungsergebnis in der Variable `compiled_sol` gespeichert.

#### Erhalten der Kompilierungsergebnisse

Nach erfolgreicher Kompilierung verwenden Sie den folgenden Code, um den kompilierten Vertrag in eine Datei zu schreiben

```python
import json

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
```

#### Erhalten von Bytecode und ABI

Die Bereitstellung und Interaktion von Solidity-Verträgen erfordern zwei Teile: Bytecode und ABI. Wir können sie mit dem folgenden Code in entsprechende Variablen für nachfolgende Operationen schreiben.

```python
# Bytecode abrufen
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# ABI abrufen
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
```

## Lokale Ganache-Umgebung

Das Debuggen von Smart Contracts erfordert die Bereitstellung des Vertrags auf einer tatsächlichen Chain, aber die Bereitstellung im Ethereum-Mainnet oder in Testnets wie Rinkeby/Koven ist für das Debuggen nicht praktisch. Daher benötigen wir eine lokale Blockchain-Umgebung, und Ganache bietet uns eine solche lokale Debugging-Umgebung. Ganache gibt es hauptsächlich in zwei Installationsmethoden: GUI und CLI.

### Ganache GUI

In Ihrer lokalen Umgebung, wie Mac/Windows-Systemen, können wir den Ganache-Client mit einer grafischen Benutzeroberfläche wählen. Die Installation und Verwendung sind sehr bequem. Sie können die entsprechende Version auf der [offiziellen Ganache-Website](https://trufflesuite.com/ganache/) auswählen.

![ganache_download](https://image.pseudoyu.com/images/ganache_download.png)

Nach der Installation wird durch Auswahl von Quick Start schnell ein lokal laufendes Blockchain-Netzwerk gestartet und zehn Konten mit jeweils 100 ETH initialisiert, die während der Entwicklung und beim Debuggen verwendet werden können.

![ganache_account](https://image.pseudoyu.com/images/ganache_account.png)

### Ganache CLI-Installation

Wenn Ihr System keine GUI-Installation unterstützt, können wir die CLI-Installation verwenden. Die Installationsmethode ist wie folgt:

```bash
npm install --global yarn
yarn global add ganache-cli
```

![ganache_cli_install](https://image.pseudoyu.com/images/ganache_cli_install.png)

Nach Abschluss der Installation können Sie das lokale Testnetzwerk starten. Wie bei Ganache GUI enthält es auch initialisierte Konten und Guthaben.

![ganache_cli_start](https://image.pseudoyu.com/images/ganache_cli_start.png)

### Verbindung zur lokalen Ganache-Umgebung über web3

web3 bietet eine Bibliothek, mit der man sich einfach mit der lokalen Ganache-Umgebung verbinden kann:

```python
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 5777
my_address = "0x2F490e1eA91DF6d3cC856e7AC391a20b1eceD6A5"
private_key = "0fa88bf96b526a955a6126ae4cca0e72c9c82144ae9af37b497eb6afbe8a9711"
```

## Solidity-Vertragsbereitstellung

### Erstellen eines Vertrags

Wir können einen Vertrag mit der web3-Bibliothek erstellen.

```python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
```

### Bereitstellen des Vertrags

Die Bereitstellung eines Vertrags besteht aus drei Hauptschritten:

1. Erstellen der Transaktion
2. Signieren der Transaktion
3. Senden der Transaktion

#### Erstellen der Transaktion

```python
nonce = w3.eth.getTransactionCount(my_address)

transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
```

#### Signieren der Transaktion

```python
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
```

#### Senden der Transaktion

```python
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
```

### Interaktion mit dem Vertrag

Ähnlich wie bei den Schritten zur Bereitstellung eines Vertrags können wir mit der web3-Bibliothek mit dem Vertrag interagieren, was ebenfalls aus drei Schritten besteht: Erstellen der Transaktion, Signieren der Transaktion und Senden der Transaktion.

#### Erstellen der Transaktion

```python
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

store_transaction = simple_storage.functions.store(67).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
```

#### Signieren der Transaktion

```python
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
```

#### Senden der Transaktion

```python
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
```

## Fazit

Dies sind die Schritte zur Interaktion mit dem lokalen Ganache-Testnetzwerk unter Verwendung der Web3.py-Bibliothek. In der tatsächlichen Produktionsprojektentwicklung verwenden wir in der Regel keine Bibliotheken wie Web3.py direkt, sondern verwenden weiter gekapselte Bibliotheken wie Brownie und HardHat. Das Verständnis der Verwendung von Bibliotheken wie Web3.py oder Web3.js ist jedoch ebenfalls sehr wichtig.

## Referenzen

> 1. [Solidity Smart Contract Entwicklung - Grundlagen](https://www.pseudoyu.com/de/2022/05/25/learn_solidity_from_scratch_basic/)
> 2. [ethereum/web3.py](https://github.com/ethereum/web3.py)
> 3. [Solidity, Blockchain und Smart Contract - Anfänger bis Experte Vollständiger Kurs | Python Edition](https://github.com/smartcontractkit/full-blockchain-solidity-course-py)