---
title: "Prinzipien und Praxis der Cross-Chain-Technologie"
date: 2021-09-06T15:34:40+08:00
draft: false
tags: ["blockchain", "crosschain"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Derzeit werden Blockchain-Plattformen immer vielfältiger, darunter etablierte wie Hyperledger Fabric und Ethereum sowie inländische Plattformen wie Hyperchain und Z-ledger. Mit zunehmender Komplexität der Blockchain-Anwendungsökosysteme stößt die Single-Chain-Leistung auf gewisse Engpässe. Folglich sind die Zusammenarbeit und Interaktion zwischen Chains (Informationssynchronisation, Austausch, Vertragsinteroperabilität usw.) zu entscheidenden Aspekten der Chain- und Anwendungsökosystementwicklung geworden.

Dieser Artikel bietet einen Überblick über die Konzepte der Cross-Chain-Technologie und gängige Lösungen.

## Überblick über Cross-Chain-Technologie

Aufgrund von Ähnlichkeiten im zugrunde liegenden Chain-Design, in Konsensalgorithmen und Netzwerkstrukturen ist die Interaktion zwischen homogenen Blockchains relativ unkompliziert. Die Interaktion zwischen heterogenen Blockchains ist jedoch komplexer und erfordert oft Hilfsplattformen oder -dienste zur Datenformatkonvertierung zwischen den beiden Chains.

### Cross-Chain-Mechanismen

Derzeit gibt es mehrere Hauptlösungen für Cross-Chain-Interaktionen:

1. Notarmechanismus
2. Hash-Locking
3. Verteilte Private-Key-Kontrolle
4. Sidechains/Relay-Chains

#### Notarmechanismus

Der Notarmechanismus ist eine Methode, die die Interaktion zwischen verschiedenen Chains durch einen Drittanbieter-Vermittler ermöglicht. Im Wesentlichen vertrauen beide Parteien einem Dritten, der Cross-Chain-Daten oder Interaktionsoperationen überprüft und weiterleitet. Dieser Ansatz unterstützt effektiv heterogene Blockchains, ist aber von Natur aus zentralisiert.

Viele digitale Währungsbörsen verwenden diese Methode, um Transaktionen und Konvertierungen zwischen verschiedenen digitalen Währungen durchzuführen. Grundsätzlich gleicht die Börse Trades ab, was eine hohe Effizienz bietet, aber gewisse Sicherheitsrisiken birgt und nur den Vermögensaustausch unterstützt.

#### Hash-Locking

Hash-Locking erschien erstmals im Bitcoin Lightning Network. Es verwendet Hash-Locks und Time-Locks, um die Vermögenswerte beider Parteien in einer Cross-Chain-Transaktion zu sichern. Time-Locks beschränken Transaktionen auf einen bestimmten Zeitrahmen, wobei die Transaktion ungültig wird, wenn sie die Zeitbegrenzung überschreitet, wodurch Verluste verhindert werden. Diese Methode kann jedoch nur den Vermögensaustausch, nicht den Vermögenstransfer ermöglichen.

#### Sidechains

Die Sidechain-Technologie beinhaltet eine bidirektionale Koppelung, die ursprünglich in Bezug auf die Bitcoin-Hauptchain entwickelt wurde, wie etwa BTC-Relay. Diese Sidechains ermöglichen die Entwicklung und Tests neuer Funktionen für Bitcoin und können die Netzwerkdurchsatzleistung effektiv erweitern, wenn viele Benutzer auf dem Bitcoin-Netzwerk Transaktionen durchführen. Beispielsweise können Vermögenstransaktionen und Werttransfers auf der Ethereum-Hauptchain stattfinden, während DApps, die einen höheren TPS erfordern, auf Ethereum-Sidechains laufen können.

Verschiedene Sidechains derselben Hauptchain können auch über die Hauptchain interagieren, was das grundlegende Prinzip der Cross-Chain-Interaktion über Sidechains bildet.

#### Relay-Chains

Relay-Chains stellen eine umfassende Anwendung der oben genannten Sidechain- und Notarmechanismen dar. Sie erreichen den Informationsaustausch und die Interaktion zwischen heterogenen Chains durch die Einrichtung von Cross-Chain-Interaktionsmechanismen (wie Cosmos' IBC). Parallelketten, die Cross-Chain-Funktionalität benötigen, verbinden sich mit einer Relay-Chain, um bei der Transaktionsverifizierung und -interaktion zu helfen.

## Cross-Chain-Technologie in der Praxis

### Entwicklungsimplementierung

Ich arbeite derzeit an einer Cross-Chain-Funktionalität für eine BaaS-Plattform. Ihre grundlegende Architektur ist wie folgt:

![cross_chain_framework](https://image.pseudoyu.com/images/cross_chain_framework.png)

Sub-Chains implementieren hauptsächlich verschiedene Geschäfte und Anwendungen. Wenn eine Sub-Chain mit anderen Chains für Cross-Chain-Geschäfte interagieren muss, führt sie einen Cross-Chain-Vertrag aus. Wir bieten ein Cross-Chain-Gateway, um diese Cross-Chain-Verträge zu überwachen. Für heterogene Blockchains wie Hyperledger Fabric und Ethereum bieten wir verschiedene Adapter, um die Interaktion zwischen dem Cross-Chain-SDK und dem Cross-Chain-Gateway zu erleichtern. Diese Adapter bieten Funktionen zur Abfrage von Cross-Chain-Vertragsinformationen. Wenn das SDK einer anderen Geschäftskette eine Cross-Chain-Vertragsmethode empfängt, ruft es direkt die entsprechende Vertragsmethode auf, wenn es sich um Vertragsaufrufe oder Datenübertragungen handelt.

Mein Hauptfokus liegt auf der Cross-Chain-Adapter-Schnittstelle. Der Adapter, der als Plugin für verschiedene Chains dient, ist in das Cross-Chain-Gateway eingebettet, um sich an verschiedene Anwendungsketten anzupassen und das Cross-Chain-Gateway effektiv bei der Überwachung, Synchronisierung und Ausführung von Transaktionen zu unterstützen.

Bei spezifischen Implementierungen, wie in einem Fabric-Netzwerk, ruft die Sub-Chain den Cross-Chain-Geschäftsvertrag auf, der wiederum einheitlich einen Adapter-Vertrag aufruft. Innerhalb dieses Adapter-Vertrags implementieren wir die Eingabe von Transaktionsinformationen. Durch den Ereignismechanismus von Fabric erreichen wir die Überwachung von Cross-Chain-Verträgen (d.h. die Implementierung der `SetEvent`-Methode im Vertrag und die Registrierung entsprechender Ereignisse im Adapter).

Für Details zur Fabric-Ereignisüberwachung und -implementierung siehe "[Hyperledger Fabric Go SDK Event Analysis](https://www.pseudoyu.com/de/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)".

### Funktionale Erweiterung

Derzeit ist QulianTechs [BitXHub Cross-Chain-Plattform](https://meshplus.github.io/bitxhub/bitxhub/introduction/summary/) eine der umfassender implementierten Open-Source-Cross-Chain-Lösungen in der Branche. Ihre Architektur ist wie folgt:

![bitxhub_structure](https://image.pseudoyu.com/images/bitxhub_structure.png)

Sie optimiert hauptsächlich Funktionalität, Sicherheit und Flexibilität im Cross-Chain-Prozess durch Relay-Chains, Gateways und Plugin-Mechanismen. Zudem wurde das IBTP (Inter-Blockchain Transfer Protocol) entwickelt, um mit der "Gateway + Relay-Chain"-Architektur zusammenzuarbeiten und Verifizierungs-, Routing- und andere Probleme bei Cross-Chain-Transaktionen anzugehen.

## Fazit

Das oben Genannte fasst die Konzepte und praktische Implementierung der Cross-Chain-Technologie zusammen. Um ein tieferes Verständnis verschiedener Aspekte von Cross-Chain-Mechanismen zu erlangen, werde ich in Zukunft eingehendere Analysen und Quellcode-Interpretationen des Cross-Chain-Dienstes, an dem ich derzeit arbeite, und der BitXHub-Plattform durchführen.

## Referenzen

> 1. [Analysis and Thoughts on Cross-Chain Technology](https://tech.hyperchain.cn/blockchain-interoperability/)
> 2. [A Brief Study of Cross-Chain: From Principles to Technology](https://zhuanlan.zhihu.com/p/92667917)
> 3. [Cross-Chain Technology Platform BitXHub](https://github.com/gocn/opentalk/tree/main/PhaseTen_BitXHub)
> 4. [Blockchain Cross-Chain Technology: Hash Time Locks](https://yuanxuxu.com/2020/08/05/区块链跨链技术之哈希时间锁/)
> 5. [Hyperledger Fabric Go SDK Event Analysis](https://www.pseudoyu.com/de/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)
> 6. [BitXHub Document](https://meshplus.github.io/bitxhub/bitxhub/introduction/summary/)
> 7. [Ten Questions about BitXHub: Discussing the Architectural Design of Cross-Chain Platforms](https://tech.hyperchain.cn/bitxhub-design-thinking/)