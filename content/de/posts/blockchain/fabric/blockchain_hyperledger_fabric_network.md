---
title: "Eine kurze Analyse des Netzwerks und Sicherheitssystems von Hyperledger Fabric"
date: 2021-03-23T12:12:17+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "security"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Im vorherigen Artikel "[Detaillierte Erklärung der Hyperledger Fabric Architektur](https://www.pseudoyu.com/en/2021/03/20/blockchain_hyperledger_fabric_structure/)" haben wir eine umfassende Interpretation und Analyse der Architektur und Funktionsprinzipien von Fabric gegeben. Als Blockchain-System auf Unternehmensebene stellt sich die Frage: Wie konstruiert es Netzwerke basierend auf komplexen Geschäftsanforderungen? Welche Sicherheitsprobleme existieren während des Betriebs und wie geht Fabric diese Probleme präventiv durch seine Mechanismen an?

Dieser Artikel wird anhand von Beispielen veranschaulichen, wie ein vereinfachtes Fabric-Unternehmensnetzwerk aufgebaut ist, und sein Netzwerk- und Sicherheitssystem analysieren. Für Fehler oder Auslassungen bin ich offen für Diskussion und Korrektur.

## Hyperledger Fabric Netzwerk

### Beispiel für ein Hyperledger Fabric Anwendungsszenario

#### Geschäftsrollen

Betrachten wir ein Anwendungsszenario unter Verwendung des Fabric-Systems.

Es gibt vier Organisationen: R1, R2, R3 und R4. R4 ist der Netzwerkinitiator, während R1 und R4 gemeinsam als Netzwerkadministratoren fungieren.

Das System hat zwei Kanäle eingerichtet, C1 und C2. R1 und R2 nutzen Kanal C1, während R2 und R3 Kanal C2 nutzen.

Anwendung A1 gehört zur Organisation R1 und läuft auf Kanal C1; Anwendung A2 gehört zur Organisation R2 und läuft auf beiden Kanälen C1 und C2; Anwendung A3 gehört zur Organisation R3 und läuft auf Kanal C2.

P1, P2 und P3 sind Knoten der Organisationen R1, R2 bzw. R3.

Der Ordering-Knoten wird von O4 bereitgestellt und gehört zur Organisation R4.

#### Konstruktionsprozess

Im Vergleich zu realen kommerziellen Anwendungsszenarien sind die Rollen und die Geschäftslogik stark vereinfacht, aber dies eignet sich zum Verständnis der Funktionen und Interaktionen zwischen verschiedenen Knoten und Rollen. Als Nächstes werde ich den Netzwerkaufbauprozess Schritt für Schritt erklären.

> Netzwerk erstellen und Netzwerkadministratoren hinzufügen

Jede Organisation benötigt ein von der CA-Behörde im MSP ausgestelltes Zertifikat, um dem Netzwerk beizutreten, daher muss jeder Knoten über eine entsprechende CA verfügen.

Als Netzwerkinitiator muss R4 zuerst das Netzwerk konfigurieren und den O4 Ordering-Knoten einrichten! Nach der Netzwerkerstellung wird R1 als Netzwerkadministrator hinzugefügt, sodass R1 und R4 das Netzwerk konfigurieren können (NC4).

![fabric_network_example_1](https://image.pseudoyu.com/images/fabric_network_example_1.png)

> Konsortium definieren und Kanal erstellen

R1 und R2 werden über C1 interagieren, daher muss im Netzwerk ein Konsortium definiert werden. Da sowohl R1 als auch R4 jetzt das Netzwerk konfigurieren können, können beide das Konsortium definieren.

Anschließend wird für dieses Konsortium der Kanal C1 erstellt (verbunden mit dem Ordering-Service O4).

![fabric_network_example_2](https://image.pseudoyu.com/images/fabric_network_example_2.png)

> Knoten beitreten, Smart Contracts und Anwendungen bereitstellen

Knoten P1 tritt dem erstellten Kanal C1 bei und pflegt ein Ledger L1.

An diesem Punkt können Smart Contracts auf dem Knoten installiert und instanziiert werden. Die Smart Contracts von Fabric sind Chaincodes. Die Speicherung des Chaincodes im Dateisystem des Knotens wird als Installation eines Smart Contracts bezeichnet. Nach der Installation muss der Chaincode auf einem spezifischen Kanal gestartet und instanziiert werden. An diesem Punkt können Anwendungen Transaktionsvorschläge an Endorsing-Knoten senden (gemäß der vom Chaincode festgelegten Endorsement-Richtlinie).

Wie in der folgenden Abbildung gezeigt, kann Knoten P1, nachdem er Chaincode S5 installiert und auf Kanal C1 instanziiert hat, auf Chaincode-Aufrufe von Anwendung A1 reagieren; nachdem Knoten P2 Chaincode S5 installiert und auf Kanal C1 instanziiert hat, kann er auf Chaincode-Aufrufe von Anwendung A2 reagieren.

Jeder Knoten im Kanal ist ein Committing-Knoten, der neue Blöcke (von Ordering-Knoten) zur Validierung und Festschreibung im Ledger empfangen kann; einige Knoten mit bereitgestellten Chaincodes können zu Endorsing-Knoten werden.

![fabric_network_example_4](https://image.pseudoyu.com/images/fabric_network_example_4.png)

> Neues Konsortium definieren, neuen Kanal erstellen

Definieren Sie ein neues Konsortium im Netzwerk und treten Sie Kanal C2 bei.

![fabric_network_example_5](https://image.pseudoyu.com/images/fabric_network_example_5.png)

> Neue Knoten beitreten und Smart Contracts und Anwendungen bereitstellen

Es ist erwähnenswert, dass einige Knoten mehreren Kanälen beitreten und in verschiedenen Geschäftsbereichen unterschiedliche Rollen spielen werden. Andere Prozesse sind die gleichen wie oben.

![fabric_network_example_6](https://image.pseudoyu.com/images/fabric_network_example_6.png)

> Netzwerkaufbau abgeschlossen

![hyperledger_fabric_network_example](https://image.pseudoyu.com/images/hyperledger_fabric_network_example.png)

Fabric verwendet Mechanismen wie Berechtigungsverwaltung und Kanäle und verbessert die Effizienz des Systembetriebs durch funktionale Aufteilung verschiedener Knoten, während gleichzeitig Sicherheit und Privatsphäre in komplexen Geschäftsszenarien gewährleistet werden. Leistungsfähige Chaincodes und anpassbare Endorsement-Richtlinien gewährleisten auch die Skalierbarkeit des Systems und die Fähigkeit, komplexe Geschäftslogik zu handhaben.

## Sicherheitsanalyse von Hyperledger Fabric

### Fabric Sicherheitsmechanismen

Fabric hat viele Mechanismen entwickelt, um die Systemsicherheit zu gewährleisten.

#### Systemkonfiguration und Mitgliederverwaltung

Im Gegensatz zu öffentlichen Blockchains wie Bitcoin und Ethereum erfordert der Beitritt zum Fabric-Netzwerk eine Berechtigungsüberprüfung. Fabric CA verwendet den X.509-Zertifikatsmechanismus für die Mitgliederverwaltung, um seine Berechtigungen sicherzustellen und potenzielle Spoofing-Angriffe zu vermeiden.

Bestehende Systemmitglieder müssen Regeln für die Aufnahme neuer Mitglieder festlegen, wie zum Beispiel Mehrheitsabstimmungen; bestehende Mitglieder müssen auch über Netzwerk- und Smart-Contract-Updates und -Änderungen entscheiden, was in hohem Maße verhindern kann, dass bösartige Knoten die Systemsicherheit gefährden; bestehende Knoten können nicht eigenständig Berechtigungen upgraden; darüber hinaus müssen sie über systemweite Datenmodelle und andere Einstellungen entscheiden.

Die Netzwerkübertragung von Fabric verwendet TLSv1.2, was die Datensicherheit gewährleisten kann; Operationen im System, wie das Initiieren von Transaktionen und Endorsements, werden durch digitale Signaturverfahren aufgezeichnet, was es erleichtert, einige böswillige Operationen zurückzuverfolgen. Es ist jedoch erwähnenswert, dass Ordering-Knoten auf Transaktionsdaten aller Knoten im System zugreifen können. Daher ist die Einrichtung von Ordering-Service-Knoten besonders wichtig für die Sicherheit des gesamten Systems. Seine Unparteilichkeit wird den Betrieb des gesamten Systems stark beeinflussen und sogar bestimmen, ob das gesamte System vertrauenswürdig ist. Daher muss es basierend auf Geschäft und Systemstruktur sorgfältig ausgewählt werden.

In öffentlichen Blockchain-Systemen haben alle Knoten eine Kopie des Blockchain-Ledgers und führen Smart Contracts aus; im Fabric-System bilden geschäftsbezogene Knoten Knotengruppen, speichern Ledger, die mit ihren Transaktionen (Geschäften) zusammenhängen, und Updates des Ledgers durch Chaincode sind auch auf den Umfang der Knotengruppe beschränkt, wodurch die Stabilität des gesamten Systems gewährleistet wird.

Die Ausführung von Smart Contracts wird als Transaktion bezeichnet. Für Transaktionen innerhalb des Fabric-Systems muss auch die Konsistenz gewahrt bleiben. Oft werden kryptografische Techniken verwendet, um zu verhindern, dass Transaktionen manipuliert werden, wie z.B. die Verwendung von SHA256, ECDSA usw., um Änderungen zu erkennen. Fabric verwendet ein modulares, steckbares Design, das Transaktionsausführung, Validierung und Konsens trennt, sodass unterschiedliche Konsensmechanismen oder Regeln angenommen werden können. Dies ermöglicht nicht nur die Auswahl verschiedener Konsensmechanismen nach Bedarf, was mehr Skalierbarkeit bietet, sondern verbessert auch die Systemsicherheit.

Diese Konfigurationen und Regeln bestimmen gemeinsam die Sicherheit des Systems und müssen gegen Geschäftsanforderungen, Effizienz und Sicherheit abgewogen werden.

#### Sicherheit von Smart Contracts

Der Chaincode von Fabric muss auf Knoten installiert und instanziiert werden. Die Installation von Chaincode erfordert eine CA-Verifizierung, daher muss die Berechtigungsverwaltung berücksichtigt werden; einmal gestartet, läuft er in einem unabhängigen Docker-Container, was leichtgewichtiger ist, aber da er auf das Fabric-Netzwerk zugreifen kann, kann es zu einigen böswilligen Konsequenzen führen, wenn er keiner strengen Code-Prüfung und Netzwerkisolierung unterzogen wurde.

Der Chaincode von Fabric kann in mehreren Mehrzweck-Programmiersprachen geschrieben werden, wie Go, Java usw., was dem System eine stärkere Skalierbarkeit verleiht und die Integration in bestehende Systeme und Tools erleichtert. Da jedoch seine Ausführungsergebnisse deterministisch sind, können einige Funktionen von Programmiersprachen (wie Zufallszahlen, Systemzeitstempel, Zeiger usw.) dazu führen, dass verschiedene Endorsing-Knoten unterschiedliche Ausführungsergebnisse produzieren, was zu Systeminkonsistenzen führt. Da Chaincode zudem auf einige externe Webdienste, Systembefehle, Dateisysteme und Bibliotheken von Drittanbietern zugreifen kann, kann dies auch einige potenzielle Risiken bergen. Daher müssen in diesen Mehrzweck-Sprachen entwickelte Chaincodes relativ unabhängig sein und einer verstärkten Code-Prüfung unterzogen werden, um einige Sicherheitsrisiken zu vermeiden, die durch Programmiersprachen entstehen können.

#### Transaktionsprivatsphäre

Fabric verwendet einen Kanalmechanismus, um das gesamte System in mehrere Teil-Blockchains (Ledger) zu unterteilen, und nur Knoten, die dem Kanal beitreten, können Transaktionsinformationen einsehen und speichern, aber Ordering-Knoten können sie sehen.

> Wie kann also die Privatsphäre einiger privater Daten innerhalb eines Kanals gewährleistet werden?

Fabric bietet eine Möglichkeit, private Daten zu speichern, die es Knoten im Kanal erlaubt, spezifische Datenobjekte zum Teilen auszuwählen (Knoten).

![fabric_security_private_data](https://image.pseudoyu.com/images/fabric_security_private_data.png)

Unter diesem Mechanismus werden echte Daten über das Gossip-Protokoll an spezifizierte Knoten gesendet und in einer privaten Datenbank gespeichert, auf die nur autorisierte Knoten über Chaincode zugreifen können. Da dieser Prozess den Ordering-Service nicht einbezieht, können Ordering-Knoten die Daten nicht erhalten.

Die Daten, die innerhalb des Systems verbreitet, geordnet und in das Ledger geschrieben werden, sind eine gehashte Version, sodass die Transaktion immer noch von jedem Knoten verifiziert werden kann, aber aufgrund der Natur des Hashens kann es effektiv verhindern, dass die Originaldaten durchsickern.

Es ist jedoch erwähnenswert, dass, wenn Daten während des Transaktionssimulationsprozesses auf Endorsing-Knoten verwendet werden müssen, zusätzliche Mechanismen angewendet werden müssen, um die Lesbarkeit der Daten für Endorsing-Knoten und ihre Unsichtbarkeit für andere Knoten zu gewährleisten (wie asymmetrische Verschlüsselung).

## Fazit

Das oben Genannte ist eine Analyse des Netzwerkaufbaus und Sicherheitssystems von Hyperledger Fabric. Als Nächstes werde ich mit dem Erlernen von Go und der Chaincode-Entwicklung beginnen und durch Projektpraxis ein tieferes Verständnis gewinnen!

## Referenzen

> 1. [FITE3011 Distributed Ledger and Blockchain](https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2019/fite3011.html), *Allen Au，HKU*