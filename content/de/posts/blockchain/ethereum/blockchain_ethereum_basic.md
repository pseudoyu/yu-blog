---
title: "Interpretation der Ethereum-Kerntechnologie"
date: 2021-02-20T12:12:17+08:00
draft: false
tags: ["blockchain", "ethereum"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Bitcoin als dezentralisierte digitale Währung war äußerst erfolgreich. Aufgrund der Einschränkungen des Bitcoin-Skripts (das nicht Turing-vollständig ist und nur einfache Logik verarbeiten kann) ist es jedoch nicht in der Lage, sehr komplexe Geschäftsoperationen zu verarbeiten. Ethereum führte Smart Contracts ein, die es ermöglichen, das Konzept der Dezentralisierung auf ein breiteres Spektrum von Anwendungsszenarien anzuwenden, und wird daher auch als Blockchain 2.0 bezeichnet. Dieser Artikel wird die Kerntechnologien von Ethereum interpretieren. Für Fehler oder Auslassungen bin ich dankbar für Diskussionen und Korrekturen.

## Ethereum-System

Im Januar 2014 veröffentlichte der russische Entwickler Vitalik Buterin das Ethereum-Whitepaper und bildete ein Team mit dem Ziel, eine Blockchain-Plattform zu schaffen, die eine allgemeinere Skriptsprache integriert. Eines der Teammitglieder, Dr. Gavin Wood, veröffentlichte ein Gelbpaper, das die technischen Aspekte der Ethereum Virtual Machine (EVM) detailliert beschrieb. Dies markierte die Geburt von Ethereum.

![ethereum_overview](https://image.pseudoyu.com/images/ethereum_overview.png)

Vereinfacht gesagt ist Ethereum ein Open-Source-dezentralisiertes System, das Blockchain verwendet, um Systemzustandsänderungen zu speichern, weshalb es auch als "Weltcomputer" bezeichnet wird. Es ermöglicht Entwicklern, unveränderliche Programme, sogenannte Smart Contracts, auf der Blockchain zu implementieren und auszuführen, wodurch ein breites Spektrum an Anwendungsszenarien unterstützt wird. Es verwendet die digitale Währung Ether, um den Systemressourcenverbrauch zu messen und mehr Menschen dazu zu motivieren, am Aufbau des Ethereum-Systems teilzunehmen.

### Dezentralisierte Anwendungen (DApps)

Im engeren Sinne ist eine DApp eine Anwendung, die eine Benutzeroberfläche integriert, Smart Contracts unterstützt und auf der Ethereum-Blockchain läuft.

![ethereum_architecture](https://image.pseudoyu.com/images/ethereum_architecture.png)

Wie in der obigen Abbildung gezeigt, werden Ethereum-Anwendungsinstanzen im Blockchain-Netzwerk bereitgestellt (Smart Contracts laufen in der Blockchain-Virtual-Machine), während das Webprogramm nur RPC-Fernaufrufe an das Blockchain-Netzwerk über Web3.js durchführen muss. Auf diese Weise können Benutzer über Browser (DApp-Browser oder Plugin-Tools wie MetaMask) auf dezentralisierte Dienstanwendungen zugreifen.

### Ledger

Die Ethereum-Blockchain ist ein dezentralisiertes Ledger (Datenbank), in dem alle Transaktionen im Netzwerk gespeichert werden. Alle Knoten müssen eine lokale Kopie der Daten aufbewahren und die Glaubwürdigkeit jeder Transaktion sicherstellen. Alle Transaktionen sind öffentlich und unveränderlich, und alle Knoten im Netzwerk können sie einsehen und verifizieren.

### Konten

Wenn wir uns bei einer Website oder einem System anmelden müssen (z.B. E-Mail), benötigen wir oft ein Konto und ein Passwort. Das Passwort wird in verschlüsselter Form in einer zentralisierten Datenbank gespeichert. Ethereum ist jedoch ein dezentralisiertes System, wie werden also Konten generiert?

Ähnlich dem Bitcoin-Systemprinzip:

1. Zuerst wird ein nur Ihnen bekannter privater Schlüssel generiert, nennen wir ihn 'sk', und mit dem Elliptic Curve Digital Signature Algorithm (ECDSA) wird der entsprechende öffentliche Schlüssel 'pk' generiert
2. Mit dem keccak256-Algorithmus wird der Hash-Wert des öffentlichen Schlüssels 'pk' berechnet
3. Die letzten 160 Bits werden als Ethereum-Adresse verwendet

Der private Schlüssel und die Adresse des Benutzers bilden zusammen das Ethereum-Konto, das Guthaben speichern, Transaktionen initiieren usw. kann. (Bitcoins Guthaben wird durch Berechnung aller UTXOs ermittelt, nicht wie bei Ethereum im Konto gespeichert).

Tatsächlich gibt es zwei Arten von Ethereum-Konten. Die oben beschriebene Methode generiert sogenannte Externally Owned Accounts (EOA), die reguläre Benutzerkonten sind und hauptsächlich zum Senden/Empfangen von Ether-Token oder zum Senden von Transaktionen an Smart Contracts (d.h. Aufrufen von Smart Contracts) verwendet werden.

Die andere Art sind Contract Accounts. Im Gegensatz zu externen Konten haben diese Konten keine entsprechenden privaten Schlüssel, sondern werden beim Bereitstellen von Verträgen generiert und speichern Smart-Contract-Code. Es ist erwähnenswert, dass Contract Accounts von externen Konten oder anderen Verträgen aufgerufen werden müssen, um Ether zu senden oder zu empfangen, und keine Transaktionen von sich aus initiieren können.

### Wallet

Software/Plugins, die Ethereum-Konten speichern und verwalten, werden als Wallets bezeichnet und bieten Funktionen wie Transaktionssignierung und Guthabenverwaltung. Wallets werden hauptsächlich auf zwei Arten generiert: nicht-deterministische Zufallsgenerierung oder Generierung basierend auf zufälligen Seeds.

### Gas

Operationen im Ethereum-Netzwerk erfordern ebenfalls "Gebühren", die als Gas bezeichnet werden. Die Bereitstellung von Smart Contracts und die Übertragung von Geldern auf der Blockchain verbrauchen eine bestimmte Menge an Gas. Dies ist auch ein Anreizmechanismus, um Miner zu ermutigen, am Aufbau des Ethereum-Netzwerks teilzunehmen und dadurch das gesamte Netzwerk sicherer und zuverlässiger zu machen.

Jede Transaktion kann die entsprechende Gas-Menge und den Gas-Preis festlegen. Eine höhere Gas-Gebühr bedeutet oft, dass Miner Ihre Transaktion schneller verarbeiten, aber um zu verhindern, dass Transaktionen durch mehrfache Ausführungen eine große Menge an Gas-Gebühren verbrauchen, können Sie ein Limit durch Gas Limit setzen. Gas-bezogene Informationen können über Tools wie den Ethereum Gas Tracker abgefragt werden.

```sh
Wenn START_GAS * GAS_PRICE > caller.balance, halte an
Ziehe START_GAS * GAS_PRICE von caller.balance ab
Setze GAS = START_GAS
Führe Code aus, ziehe von GAS ab
Für negative Werte, addiere zu GAS_REFUND
Nach Beendigung, addiere GAS_REFUND zu caller.balance
```

### Smart Contracts

Wie bereits erwähnt, speichert die Ethereum-Blockchain nicht nur Transaktionsinformationen, sondern auch Smart-Contract-Code und führt diesen aus.

Smart Contracts steuern die Anwendungs- und Transaktionslogik. Im Ethereum-System verwenden Smart Contracts die proprietäre Sprache Solidity, deren Syntax JavaScript ähnelt. Darüber hinaus gibt es Programmiersprachen wie Vyper und Bamboo. Smart-Contract-Code wird in Bytecode kompiliert und auf der Blockchain bereitgestellt, und einmal auf der Chain kann er nicht mehr bearbeitet werden. Die EVM als Ausführungsumgebung für Smart Contracts kann die Determinismus der Ausführungsergebnisse sicherstellen.

#### Beispiel für Smart Contract: Crowdfunding

Stellen wir uns ein komplexeres Szenario vor. Angenommen, ich möchte 10.000 Yuan Crowdfunding sammeln, um ein neues Produkt zu entwickeln. Die Nutzung bestehender Crowdfunding-Plattformen erfordert erhebliche Gebühren, und es ist schwierig, Vertrauensprobleme zu lösen. Daher können wir eine Crowdfunding-DApp verwenden, um dieses Problem zu lösen.

Legen wir zunächst einige Regeln für das Crowdfunding fest:

1. Jede Person, die am Crowdfunding teilnehmen möchte, kann einen Betrag zwischen 10-10.000 Yuan spenden
2. Wenn der Zielbetrag erreicht wird, wird der Betrag über einen Smart Contract an mich (den Crowdfunding-Initiator) gesendet
3. Wenn das Ziel innerhalb einer bestimmten Zeit (z.B. 1 Monat) nicht erreicht wird, werden die Crowdfunding-Gelder an die Crowdfunding-Nutzer zurückgegeben
4. Wir können auch einige Regeln festlegen, wie zum Beispiel, dass nach einer Woche, wenn der Zielbetrag nicht erreicht ist, Benutzer eine Rückerstattung beantragen können

Da diese Crowdfunding-Bedingungen durch Smart Contracts implementiert und auf der öffentlichen Blockchain bereitgestellt werden, kann selbst der Initiator die Bedingungen nicht manipulieren, und jeder kann sie einsehen, wodurch das Vertrauensproblem gelöst wird.

Sie können den vollständigen Code hier einsehen: [Demo](https://www.toshblocks.com/solidity/complete-example-crowd-funding-smart-contract/)

### Transaktionen

Wie sieht eine typische Transaktion in Ethereum aus?

1. Entwickler stellen Smart Contracts auf der Blockchain bereit
2. DApp instanziiert den Vertrag, übergibt entsprechende Werte zur Ausführung des Vertrags
3. DApp signiert die Transaktion digital
4. Lokale Verifizierung der Transaktion
5. Übertragung der Transaktion an das Netzwerk
6. Miner-Knoten empfangen die Transaktion und verifizieren sie
7. Miner-Knoten bestätigen vertrauenswürdige Blöcke und übertragen sie an das Netzwerk
8. Lokale Knoten synchronisieren sich mit dem Netzwerk und empfangen neue Blöcke

### Architektur

![ethereum_architecture_simple](https://image.pseudoyu.com/images/ethereum_architecture_simple.png)

Ethereum verwendet eine "Order - Execute - Validate - Update State" Systemarchitektur. Unter dieser Architektur führen Miner bei einer neuen Transaktion Proof of Work (PoW) Berechnungen durch; nach der Verifizierung übertragen sie den Block über das Gossip-Protokoll an das Netzwerk; andere Knoten im Netzwerk empfangen den neuen Block und verifizieren ihn ebenfalls; schließlich wird er der Blockchain übermittelt und aktualisiert den Zustand.

Konkret verfügt das Ethereum-System über Kernkomponenten wie die Konsensschicht, Datenschicht und Anwendungsschicht. Ihre Interaktionslogik ist wie folgt:

![ethereum_architecture_concrete](https://image.pseudoyu.com/images/ethereum_architecture_concrete.png)

Wie in der obigen Abbildung gezeigt, bestehen Ethereum-Daten aus Transaction Root und State Root. Transaction Root ist ein Baum, der aus allen Transaktionen besteht, einschließlich From, To, Data, Value, Gas Limit und Gas Price; während State Root ein Baum ist, der aus allen Konten besteht, einschließlich Address, Code, Storage, Balance und Nonce.

## Fazit

Das oben Genannte ist eine Interpretation der Kerntechnologien von Ethereum. Die Einführung von Smart Contracts hat mehr Möglichkeiten für Blockchain-Anwendungen eröffnet, aber es gibt immer noch viele Sicherheits-, Datenschutz- und Effizienzprobleme zu berücksichtigen. Für komplexe Anwendungsszenarien auf Unternehmensebene sind Konsortium-Blockchains eine bessere Wahl. Eine detaillierte Analyse von Hyperledger Fabric wird in Zukunft bereitgestellt, bleiben Sie dran!

## Referenzen

> 1. [COMP7408 Distributed Ledger and Blockchain Technology](https://msccs.cs.hku.hk/public/courses/2020/COMP7408A/), *Professor S.M. Yiu, HKU*
> 2. [Udacity Blockchain Developer Nanodegree](https://www.udacity.com/course/blockchain-developer-nanodegree--nd1309), *Udacity*
> 3. [Blockchain Technology and Applications](https://www.bilibili.com/video/BV1Vt411X7JF), *Xiao Zhen, Peking University*
> 4. [Advanced Blockchain Technology and Practice](https://www.ituring.com.cn/book/2434), *Cai Liang, Li Qilei, Liang Xiubo, Zhejiang University | Hyperchain Technology*
> 5. [Ethereum Architecture](https://www.zastrin.com/courses/ethereum-primer/lessons/1-5), *zastrin*
> 6. [Learn Solidity: Complete Example: Crowd Funding Smart Contract](https://www.toshblocks.com/solidity/complete-example-crowd-funding-smart-contract/), *TOSHBLOCKS*