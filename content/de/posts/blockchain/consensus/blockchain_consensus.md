---
title: "Verteilte Systeme und Blockchain-Konsensmechanismen"
date: 2021-09-08T11:03:55+08:00
draft: false
tags: ["blockchain", "consensus", "distributed system"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Mit zunehmender Komplexität der Internetsysteme haben sich die meisten von monolithischen zu verteilten Architekturen entwickelt. Die Blockchain-Technologie, die im Wesentlichen auf verteilten Systemen basiert, ist in hohem Maße auf Datenkonsistenz und Konsensmechanismen angewiesen.

Dieser Artikel wird die Konzepte der Konsistenz und des Konsens in verteilten Systemen sowie deren praktische Anwendungen und Entwicklungen in der Blockchain-Technologie vorstellen.

## Verteilte Systeme

### Das Konsistenzproblem

Mit zunehmender Komplexität der Geschäftsszenarien wird ein einzelner Dienst oft von mehreren Servern bereitgestellt, die einen Cluster bilden. Die Erreichung eines Konsenses zwischen diesen Systemen mit unterschiedlichen physischen Standorten und Betriebszuständen ist jedoch zu einem entscheidenden Problem im verteilten Bereich geworden.

Im Allgemeinen gibt es drei Kriterien für die Erreichung eines Konsenses in verteilten Systemen:

1. Terminierung
2. Übereinstimmung
3. Gültigkeit

Verteilte Transaktionen müssen sicherstellen, dass innerhalb einer endlichen Zeit ein Konsens erreicht wird, das Ergebnis muss ein Vorschlag eines der Knoten sein, und verschiedene Knoten müssen die gleiche Entscheidung treffen.

### Starke Konsistenz

Dies in einer einzelnen Anwendung oder wenn die Leistung, Netzwerkbandbreite und andere Konfigurationen jedes Knotens ideal sind, ist einfach zu erreichen. In realen Geschäftsszenarien ist die Implementierung einer solch starken Konsistenz jedoch sehr kostspielig. Sie erfordert die Gewährleistung absoluter Systemstabilität und keine Kommunikationsverzögerungen zwischen den Systemen. Darüber hinaus reduziert starke Konsistenz auch die Systemleistung und Skalierbarkeit.

Bei starker Konsistenz sind die Daten über alle Knoten zu jedem Zeitpunkt gleich. Starke Konsistenz umfasst typischerweise zwei Arten: sequentielle Konsistenz und Linearisierbarkeit.

#### Sequentielle Konsistenz

Sequentielle Konsistenz erfordert, dass die globale Ausführungsreihenfolge aller Prozesse mit der eigenen Reihenfolge jedes Prozesses übereinstimmt, erfordert jedoch nicht die Aufrechterhaltung einer globalen Reihenfolge für jeden Prozess in der physischen Zeit. Daher ist dies ein relativ praktischer Ansatz.

#### Linearisierbarkeit

Linearisierbarkeit fügt der sequentiellen Konsistenz die Regel der globalen Ordnung zwischen Prozessen hinzu und erfordert eine Echtzeitsynchronisation der Operationen über alle Prozesse zu jeder Zeit. Diese absolute Konsistenz ist in der Praxis oft schwer zu erreichen und erfordert die Implementierung durch globale Sperren oder komplexe Synchronisationsalgorithmen, oft auf Kosten der Leistung.

### Schwache Konsistenz

In realen Geschäftsszenarien sind solche absolut konsistenten Zustände mit Echtzeitsynchronisation oft unnötig. Daher ist es akzeptabel, teilweisen Zugriff oder eventuelle Konsistenz nach einer gewissen Zeit zu tolerieren. Diese in einigen Aspekten abgeschwächten Konsistenzen werden als schwache Konsistenz bezeichnet.

### Konsensmechanismen

Ein Konsensmechanismus bezieht sich auf den Prozess, durch den mehrere Knoten in einem verteilten System eine Einigung über eine Transaktion erreichen. Bezüglich der Erreichung eines Konsenses gibt es mehrere Theorien und Prinzipien:

- FLP-Unmöglichkeit
- CAP-Theorem
- ACID-Prinzipien
- BASE-Theorie
- Mehrphasiges Commit

#### FLP-Unmöglichkeit

Die FLP-Unmöglichkeit, vorgeschlagen von den Wissenschaftlern Fischer, Lynch und Patterson, besagt, dass es in einem asynchronen System mit zuverlässigen Netzwerken, aber mit Knotenausfällen (wie Abstürzen), unmöglich ist, in endlicher Zeit einen Konsens zu erreichen.

Asynchronität bezieht sich auf Unterschiede in Zeit und anderen Faktoren zwischen Systemknoten, wodurch es unmöglich wird zu bestimmen, ob eine nicht reaktive Nachricht auf einen Knotenausfall oder einen Übertragungsfehler zurückzuführen ist, und somit unmöglich zu bestimmen, ob eine Nachricht verloren gegangen ist.

#### CAP-Theorem

In der Ingenieurpraxis wird oft ein Aspekt der Anforderungen abgeschwächt, um den Bedürfnissen realer Geschäftsszenarien gerecht zu werden. Das CAP-Theorem behandelt dieses Problem, wobei CAP für Folgendes steht:

- Consistency (Konsistenz)
- Availability (Verfügbarkeit)
- Partition tolerance (Partitionstoleranz)

Verteilte Systeme können nicht gleichzeitig alle drei Punkte garantieren; bestenfalls können sie zwei dieser Eigenschaften sicherstellen. Wie wird dieses Prinzip also in der Praxis angewendet?

1. AP-Systeme: In Geschäftsszenarien wie statischen Websites und nicht-Echtzeit-Datenbanken kann die Konsistenz abgeschwächt werden, z.B. durch Erreichen der Konsistenz einige Zeit nach dem Start einer neuen Version.
2. CP-Systeme: In Szenarien, die absolut konsistenzsensitiv sind, wie Banküberweisungen, kann die Verfügbarkeit abgeschwächt werden, z.B. durch Verweigerung des Dienstes bei Systemausfall oder Fehlfunktion.
3. AC-Systeme: Zweiphasiges Commit und einige relationale Datenbanken schwächen die Netzwerkpartitionierung ab, wie z.B. ZooKeeper.

#### ACID-Prinzipien

Transaktionen in verteilten Datenbanken müssen einige Verfügbarkeit opfern, um Konsistenz zu erreichen, und müssen den ACID-Prinzipien folgen:

- Atomicity (Atomarität): Alle Operationen in einer Transaktion müssen entweder vollständig ausgeführt oder gar nicht ausgeführt werden; bei Fehlschlag sollten alle zurückgesetzt werden.
- Consistency (Konsistenz): Der Zustand vor und nach der Transaktionsausführung muss konsistent sein, ohne Zwischenzustände.
- Isolation (Isolation): Mehrere Transaktionen können gleichzeitig ausgeführt werden, sind aber voneinander unabhängig.
- Durability (Dauerhaftigkeit): Zustandsänderungen sind permanent.

#### BASE-Prinzipien

Die BASE-Prinzipien stehen für:

- Basically Available (grundsätzlich verfügbar)
- Soft State (weicher Zustand)
- Eventual Consistency (eventuelle Konsistenz)

Dies ist ein Ansatz, der starke Konsistenz opfert, um das gesamte System zu implementieren, und nur eventuelle Konsistenz sicherstellt.

#### Mehrphasiges Commit

Das zweiphasige Commit teilt den Transaktions-Commit-Prozess in Pre-Commit- und formale Commit-Phasen auf, um Konflikte zu vermeiden, hat aber immer noch Probleme mit synchroner Blockierung, Single Point of Failure und Datenkonsistenz.

Der TCC (Try-Confirm-Cancel) Transaktionsmechanismus besteht hauptsächlich aus:

- Try-Phase
- Confirm-Phase
- Cancel-Phase

In der Try-Phase wird das Geschäft überprüft und Geschäftsressourcen werden reserviert. In der Confirm-Phase werden Ressourcen verwendet, um das Geschäft auszuführen. In der Cancel-Phase wird die Ausführung abgebrochen und Ressourcen werden freigegeben. Diese Methode fügt dem zweiphasigen Commit mehr Geschäftsverarbeitung hinzu, aber da sie in drei Schnittstellen aufgeteilt ist, erhöht sich die Codekomplexität.

Das dreiphasige Commit führt einen Timeout-Mechanismus ein und fügt der ersten Phase des zweiphasigen Commits einen vorläufigen Pre-Commit-Schritt hinzu, wodurch hauptsächlich Probleme mit Single Point of Failure und Blockierung gelöst werden.

## Konsensalgorithmen

Basierend auf der Art der Fehlertoleranz (ob es bösartige Knoten gibt) unterteilen wir Konsensalgorithmen in Crash Fault Tolerance (CFT) und Byzantine Fault Tolerance (BFT).

### CFT (Crash Fault Tolerance)

Szenarien in verteilten Systemen, in denen fehlerhafte Knoten existieren, aber fehlerhafte Knoten nicht vorhanden sind, werden als CFT bezeichnet. In diesen Szenarien können Nachrichten verloren gehen oder dupliziert werden, aber nicht fehlerhaft sein. Die Erreichung eines Konsenses unter diesen Bedingungen ist eine sehr häufige Anforderung in der realen Welt.

#### Paxos

Das Paxos-Algorithmus-Prinzip ähnelt dem zweiphasigen Commit und setzt drei logische Knoten: Proposer, Acceptor und Learner. Der Proposer schlägt Vorschläge vor, der Acceptor stimmt über Vorschläge ab und akzeptiert sie, und der Learner erhält und verbreitet Vorschlagsergebnisse.

Nur von Proposern gemachte Vorschläge können genehmigt werden, und alle Knoten können darum konkurrieren, Proposer zu werden, aber nur ein Proposer kann in jeder Konsensrunde einen Vorschlag machen. Dieser Mechanismus gewährleistet ein gewisses Maß an Fairness.

Paxos kann jedoch nur unter bestimmten Bedingungen Konsens garantieren und funktioniert nur normal, wenn mehr als die Hälfte der Knoten teilnehmen.

#### Raft

Aufgrund der Schwierigkeit bei der Implementierung des Paxos-Algorithmus sind viele Varianten entstanden, wie Fast Paxos, Multi-Paxos usw., unter denen der Raft-Algorithmus recht repräsentativ ist.

Raft teilt den Konsistenzprozess in drei Teilprobleme auf: Führungswahl, Log-Replikation und Sicherheit, und setzt drei logische Knoten: Leader, Candidate und Follower.

Der Anfangszustand aller Knoten ist Follower. Diejenigen, die an der Führungswahl teilnehmen möchten, verwandeln sich in Candidates und schlagen Wahlanträge vor. Wenn mehr als die Hälfte der Stimmen erhalten wird, werden sie erfolgreich zum Leader für diese Amtszeit.

Der Leader bearbeitet alle Anfragen und synchronisiert Logs zu Followers und sendet periodisch Heartbeat-Nachrichten an alle Followers. Wenn ein Ausfall auftritt und nach Timeout keine Heartbeat-Nachrichten empfangen werden, wird ein neuer Wahlprozess eingeleitet.

### BFT (Byzantine Fault Tolerance)

#### Byzantine Fault Tolerance, BFT

Der Byzantine Fault Tolerance Algorithmus wird hauptsächlich verwendet, um Szenarien zu behandeln, in denen bösartige Knoten im Netzwerk existieren, und löst in erster Linie das byzantinische Problem. Er kann effektiv einen Konsens erreichen, wenn bösartige Knoten 1/3 nicht überschreiten, aber die Komplexität ist sehr hoch (exponentiell).

#### Practical Byzantine Fault Tolerance, PBFT

PBFT ist eine Optimierung des BFT-Algorithmus und verwendet kryptografische Techniken wie RSA-Signaturen, Nachrichtenverifizierung und Digests, kombiniert mit verwandten Algorithmen wie Paxos, um letztendlich die Algorithmuskomplexität auf ein quadratisches Niveau zu reduzieren.

In der PBFT-Algorithmusimplementierung wird zunächst ein bestimmter Knoten ausgewählt (zufällig/rotierend) und als primärer Knoten festgelegt. Der primäre Knoten empfängt Clientanfragen innerhalb seiner eigenen View und sendet sie (unter Verwendung eines dreiphasigen Commit-Mechanismus, siehe oben) an andere Knoten. Wenn alle Knoten die Anfrage abgeschlossen haben, werden die Ergebnisse an den Client zurückgegeben. Wenn mindestens 2f + 1 identische Ergebnisse von verschiedenen Knoten empfangen werden, wird ein Konsens erreicht.

- Vorläufiger Pre-Commit: Nach Erhalt der Nachricht signiert der primäre Knoten und sendet sie an andere Knoten
- Pre-Commit: Nach Erhalt der Nachricht überprüfen andere Knoten, signieren bei Rechtmäßigkeit und senden an andere Knoten, die ebenfalls überprüfen
- Formaler Commit: Signieren der Nachricht und Senden des Commit-Status; wenn von 2f + 1 Knoten verifiziert, schließt das System den Konsens ab

#### Andere

Neben PBFT werden PoW, PoS, HotStuff usw. in Blockchain-Projekten wie Bitcoin, Ethereum, Libra weit verbreitet eingesetzt und ständig optimiert. Byzantinische fehlertolerante Algorithmen werden aufgrund ihrer geringen Effizienz meist in Public-Chain-Umgebungen eingesetzt, während Konsortium-Chains oft nicht-byzantinische fehlertolerante Methoden anwenden, ergänzt durch Zugangskontrolle und andere Methoden, um Leistung und Sicherheit auszugleichen.

## Schlussfolgerung

Das oben Genannte ist eine Zusammenfassung der Konzepte und praktischen Anwendungen von verteilten Systemen und Blockchain-Konsensmechanismen. In Zukunft werde ich auch eine tiefere Analyse verschiedener in der Industrie verwendeter Konsensalgorithmen bieten.

## Referenzen

> 1. [Blockchain: Prinzip, Design und Anwendung](https://book.douban.com/subject/27127839/)
> 2. [Verteilte Transaktionen, Dieser Artikel ist ausreichend](https://xiaomi-info.github.io/2020/01/02/distributed-transaction/)
> 3. [TCC, 2PC und 3PC verstehen](http://anruence.com/2018/03/05/tcc-2pc-3pc/)
> 4. [【Konsens-Kolumne】Klassifizierung des Konsenses (Teil 1)](https://tech.hyperchain.cn/gong-shi-zhuan-lan-gong-shi-de-fen-lei-shang/)
> 5. [【Konsens-Kolumne】Klassifizierung des Konsenses (Teil 2