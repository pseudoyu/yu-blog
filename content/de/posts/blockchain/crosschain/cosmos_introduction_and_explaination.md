---
title: "Cosmos Blockchain-Architektur und Tendermint-Konsensmechanismus"
date: 2023-02-10T20:00:03+08:00
draft: false
tags: ["blockchain", "crosschain", "cosmos", "tendermint", "consensus"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

In meiner Arbeit bin ich hauptsächlich an der architektonischen Gestaltung und Implementierung von Cross-Chain-Projekten beteiligt. Da die bestehende Lösung unseres Unternehmens auf der Cosmos-Blockchain basiert, habe ich über ein Jahr lang an einigen grundlegenden Kettenentwicklungsmodifikationen mit dem Cosmos SDK gearbeitet. Dies hat mir ein gewisses Verständnis für dessen technische Umsetzung vermittelt. Aufgrund des engen Entwicklungsplans hatte ich jedoch nie die Gelegenheit, ein systematisches Verständnis der architektonischen Gestaltung von Cosmos und des Tendermint-Konsensmechanismus zu erlangen.

Nach Abschluss des Projekts fand ich endlich die Zeit, "Blockchain-Architektur und -Implementierung: Cosmos erklärt" zu lesen. Dieser Artikel stellt mein eigenes Verständnis und meine Zusammenfassung von Cosmos und Tendermint dar.

## Entwicklung der Blockchain-Technologie

Bevor wir uns mit den Einzelheiten der Cosmos-Blockchain befassen, wollen wir zunächst die Geschichte der Blockchain-Entwicklung und die aktuellen Mainstream-Blockchain-Technologien in der Branche betrachten.

### Technische Einschränkungen

Die Blockchain entwickelt sich nun seit über einem Jahrzehnt, von der anfänglichen Bitcoin über das einst populäre EOS bis hin zu Ethereum, das allmählich zum Mainstream geworden ist. Jede hat ihre eigenen Charakteristika, aber auch ihre Einschränkungen.

- Der Aufbau auf Bitcoin oder Ethereum erfordert relativ hohe technische Expertise aufgrund der Notwendigkeit, p2p-Netzwerke, Kryptographie, Konsensalgorithmen usw. zu implementieren.
- Zugrundeliegende Ketten basierend auf dem PoW (Proof of Work) Mechanismus verbrauchen zunehmend mehr Rechenleistung (und Strom), was nicht ressourcen- und umweltfreundlich ist.
- Mit zunehmender Anzahl und Umfang der On-Chain-Anwendungen werden die Leistungsengpässe der Ketten immer deutlicher.
- Da Geschäftsszenarien komplexer werden und die Anforderungen steigen, müssen sich auch die Konsensalgorithmen der Ketten entsprechend spezifischer Szenarien weiterentwickeln.
- Die zugrundeliegenden Architekturen verschiedener Ketten unterscheiden sich stark, und verschiedene Ketten sind isoliert, was die Kommunikation untereinander erschwert. Die Implementierung von Cross-Chain-Technologielösungen ist ebenfalls eine Herausforderung.

### Technologische Fortschritte

Um diese Probleme anzugehen, hat die Branche zahlreiche technische Lösungen entwickelt.

- Aufgrund des massiven Ressourcenverbrauchs von PoW haben viele Ketten den PoS (Proof of Stake) Mechanismus übernommen, wie z.B. EOS's DPoS und Ethereums kürzlich aufgerüstetes PoS, die zunehmend ausgereift werden.
- Um die Einschränkungen der zugrundeliegenden Ketten zu überwinden, hat sich das Modell allmählich von der Erstellung separater Ketten für einzelne Anwendungen (wie Bitcoin) zur Erstellung von ÐApps unter Verwendung von Smart Contracts entwickelt.
- Um Leistungseinschränkungen zu bewältigen, hat Bitcoin Cash eine Lösung zur Erhöhung der Blockkapazität übernommen, EOS eine Lösung zur Verbesserung des TPS (behauptet Millionen von TPS), während Ethereum Sharding verwendet, um On-Chain-Transaktionen parallel zu verarbeiten.
- In Bezug auf Cross-Chain-Technologie wurde Hash-Locking in Bitcoin- und Algorand-Projekten angewendet. Daneben gibt es auch Lösungen wie Notare und Relay-Chains.

## Cosmos Blockchain-Framework

### Überblick

Cosmos ist ein Open-Source-Blockchain-Infrastrukturprojekt, das von Tendermint Inc. entwickelt wurde. Sein Ziel ist es, verschiedene Probleme zu lösen, die bei der Entwicklung der Blockchain-Technologie aufgetreten sind, und ein leistungsstarkes, hochskalierbares und einfach zu entwickelndes Blockchain-Framework bereitzustellen. Seine Open-Source-Adresse lautet wie folgt:

- [GitHub - cosmos/cosmos: Internet of Blockchains](https://github.com/cosmos/cosmos)

Cosmos kann als Multi-Chain-Netzwerk betrachtet werden, das darauf abzielt, die Vision eines "Internet der Blockchains" zu verwirklichen, wobei Tendermint und Cosmos SDK seine technischen Mittel und Implementierungspfade sind.

Um Ressourcenverbrauch und Transaktionsprobleme anzugehen, hat Cosmos einen BFT (Byzantine Fault Tolerance) + PoS (Proof of Stake) Ansatz übernommen. Um gleichzeitig die Schwelle für den Blockchain-Aufbau und die Entwicklung von Blockchain-basierten Anwendungen zu senken, hat Cosmos eine allgemeinere Projektaufbaumethode übernommen, wodurch die Kettenentwicklung basierend auf Cosmos modularer und technischer wird. Es besteht hauptsächlich aus drei Teilen: Tendermint Core, IBC und Cosmos SDK.

### Cosmos SDK Komponenten

Obwohl als "SDK" bezeichnet, was leicht zu einigen Missverständnissen führen kann, dass es sich lediglich um eine Bibliothek/Komponente zur Interaktion mit der Kette handelt, kann Cosmos SDK tatsächlich als vollständige Architektur betrachtet werden. Entwickler können es verwenden, um schnell ihre eigene Blockchain aufzubauen, was es zu einem wichtigen Teil des Cosmos-Ökosystems macht. Seine Open-Source-Adresse lautet wie folgt:

- [GitHub - cosmos/cosmos-sdk: A Framework for Building High Value Public Blockchains](https://github.com/cosmos/cosmos-sdk)

Cosmos SDK implementiert hauptsächlich einige gängige Module in der Blockchain, wie Kontosysteme, Transaktionen, On-Chain-Governance usw. Entwickler können bequem neue Funktionsmodule darauf aufbauen.

Seine Hauptmodule sind wie folgt:

- Konto- und transaktionsbezogene Module
  - auth: Systemkontoverwaltung
  - bank: On-Chain-Vermögenstransfer
- Hilfsfunktionsmodule
  - genutil: Genesis-Block
  - supply: Gesamtvermögensverwaltung
  - crisis: Invariantenverwaltung für alle Module
  - params: Parameterverwaltung für alle Module
- On-Chain-Governance-Modul
  - gov: On-Chain-Governance-Mechanismus
  - upgrade: Ketten-Upgrade
- PoS-Module
  - staking: On-Chain-Vermögens-Staking
  - slashing: Bestrafung von Validatoren für passives böswilliges Verhalten
  - evidence: Bestrafung von Validatoren für aktives böswilliges Verhalten
  - mint: On-Chain-Vermögensprägung
  - distribution: Block-Belohnungsverwaltung
  - IBC-Protokollmodul
  - ibc/core: Cross-Chain-Kommunikationsfunktionalität

Wie wir sehen können, ist das Cosmos SDK-Framework aufgrund der Object-Capability Model Sicherheitsphilosophie hochgradig modularisiert. Jedes Modul hat seinen eigenen Speicherbereich und legt nur notwendige Schnittstellen nach außen offen.

Es gibt eine spezifische Keeper-Rolle im Cosmos SDK, die zur Pflege und Aktualisierung von Zuständen verwendet wird. Durch diese Verwaltungsmethode verbergen Module spezifische Implementierungsdetails voreinander und rufen sich nur über Keeper gegenseitig auf. Darüber hinaus wird der interne Zustand jedes Moduls nur von seinem Keeper aktualisiert, was die Konsistenz der On-Chain-Zustände effektiv gewährleistet.

### Tendermint-Komponente

Tendermint ist die Kernkomponente von Cosmos, eine leistungsstarke Blockchain-Konsensus-Engine. Architektonisch ist sie hauptsächlich in drei Teile unterteilt: Peer-to-Peer-Netzwerkkommunikationsschicht, Konsensprotokollebene und obere Anwendungsebene, wobei die Konsensprotokollebene ihr wichtigster Teil ist.

Bei der Konsensfindung kümmert sich Tendermint nicht um die spezifischen Transaktionsdetails, sondern verpackt Transaktionen lediglich als Bytes in Blöcke und erreicht dann Konsens durch Mechanismen zwischen Knoten. Es erfordert, dass die Aktualisierung des oberen Anwendungszustands ein deterministischer Prozess ist, d.h. ausgehend vom gleichen Anfangszustand ist die Transaktionsreihenfolge im gesamten Netzwerk konsistent (d.h. alle normalen Knoten werden eine Sequenz von Nachrichten in der gleichen Reihenfolge verarbeiten), und der Zustand der oberen Anwendung sollte im gesamten Netzwerk konsistent bleiben. Die Blockchain wird digitale Fingerabdrücke der oberen Anwendung zur Überprüfung enthalten.

Der Tendermint-Konsens kann eine sekundengenaue Blockproduktion in Blockchain-Netzwerken mit Hunderten von Knoten unterstützen. Er bietet die Funktion der Block-für-Block-Finalität, was bedeutet, dass nach der Bestätigung eines Blocks garantiert werden kann, dass alle vorherigen Blöcke nicht verändert werden, was die Sicherheit des Blockchain-Netzwerks gewährleistet.

Nachdem ein Block eingereicht wurde, interagiert die Tendermint-Konsensprotokollebene mit der oberen Ebene durch ABCI (eine für die Interaktion zwischen Anwendungsebene und Konsensebene abstrahierte Schnittstelle), um die Transaktionsverarbeitung abzuschließen und Ergebnisse zurückzugeben. Sie teilt den Blockausführungsprozess in mehrere Schritte auf, und die obere Anwendung hat die Autonomie, Geschäftsinteraktionslogik zu definieren, zu entwickeln und durch spezifische Schnittstellen zu implementieren (wie die Implementierung von Validator-Screening-Logik oder die Wiederverwendung des Konsensprotokolls und der Peer-to-Peer-Netzwerkkommunikation von Tendermint Core, um Kettengeschäftsanforderungen zu implementieren).

Für ein detailliertes Verständnis des Tendermint-Konsensalgorithmusmechanismus können Sie das folgende Papier lesen:

- [The latest gossip on BFT consensus - Tendermint](https://arxiv.org/pdf/1807.04938.pdf)

Seine einzigartigen Mechanismen bringen erhebliche Vorteile im Blockchain-Konsensprozess.

Erstens stammt Tendermint vom PBFT SMR (State Machine Replication) Algorithmus ab, vereinfacht jedoch seinen Mechanismus. Sein Konsens basiert hauptsächlich auf Blöcken und nicht auf Benutzeranfragen und vereinheitlicht mechanisch den regulären Prozess und den View-Change-Prozess von PBFT, was es einfacher macht zu verstehen und zu implementieren.

Es bietet eine solide Infrastruktur und gute Benutzererfahrung und ist eine der frühesten zugrundeliegenden Technologien, die eine sekundengenaue Blockproduktion in Blockchain-Netzwerken mit Hunderten von Knoten unterstützen kann. Gleichzeitig stellt es sicher, dass alle vorherigen Blöcke durch Block-für-Block-Finalität nicht verändert werden, was die Sicherheit des Blockchain-Netzwerks garantiert.

Knoten kommunizieren miteinander durch das Gossip-Protokoll, erfordern keine vollständige Verbindung zwischen Knoten, sondern kommunizieren durch ein Gossip-Peer-to-Peer-Netzwerk. Dies kann die Kommunikationskosten zwischen Knoten effektiv reduzieren und gleichzeitig die Fehlertoleranz des Netzwerks effektiv verbessern.

Die Implementierungsdetails und Mechanismen des Tendermint-Algorithmus werden in späteren Artikelserien spezifisch erklärt.

### IBC-Protokollkomponente

Das IBC-Protokoll ist ein spezielles Modul im Cosmos SDK, das hauptsächlich Cross-Chain-Fähigkeiten zwischen Blockchains für Cosmos bereitstellt. Sein Hauptprinzip besteht darin, seine eigenen On-Chain-Ereignisse anderen Ketten durch kryptographische Technologie zu beweisen. Es kann verstanden werden, dass die Cross-Chain-Parteien leichte Knoten (Light Clients) füreinander sind, und die Kommunikation zwischen den beiden Ketten durch Relayer realisiert wird, wodurch Cross-Chain-Kommunikation/Transaktionen erreicht werden.

Dieser Teil beinhaltet viele Details und ist eng mit Cross-Chain verbunden, daher wird er in einem separaten Artikel detailliert erklärt.

## Fazit

Dieser Artikel ist der erste in der Cosmos- und Tendermint-Konsens-Serie und stellt hauptsächlich die technologische Entwicklung der Blockchain, Kernkomponenten wie Tendermint und Cosmos SDK im Cosmos-Blockchain-Framework vor und gibt einen Überblick über die Prinzipien und Mechanismen des Tendermint-Konsensprotokolls. Aufgrund von Platzbeschränkungen konzentriert er sich hauptsächlich auf Konzepterklärungen und Prozessübersichten, ohne auf spezifische technische Implementierungsdetails und Codeerklärungen einzugehen. Diese werden in nachfolgenden Artikelserien zum Tendermint-Konsensalgorithmus/-mechanismus und zur Cosmos SDK-Codeimplementierung ergänzt.

## Referenzen

1. > "Blockchain-Architektur und -Implementierung: Cosmos erklärt - Wen Long/Jia Yin"
2. > [Cosmos: The Internet of Blockchains](https://cosmos.network/)
3. > [Whitepaper - Resources - Cosmos Network](https://v1.cosmos.network/resources/whitepaper)
4. > [Distributed Systems and Blockchain Consensus Mechanisms · Pseudoyu](https://www.pseudoyu.com/de/2021/09/08/blockchain_consensus/)
5. > [Exploring Cosmos: Tendermint](https://tech.hyperchain.cn/cosmos-5/)
6. > [Exploring Cosmos: Cosmos SDK](https://tech.hyperchain.cn/cosmos-4/)