---
title: "Blockchain-Grundlagen und Schlüsseltechnologien"
date: 2021-02-12T12:12:17+08:00
draft: false
tags: ["blockchain", "guide", "knowledge"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Kürzlich habe ich an der HKU den Kurs `<COMP7408 Distributed Ledger and Blockchain Technology>` belegt, der mir ein systematischeres Verständnis der Grundkonzepte der Blockchain vermittelt hat. In Verbindung mit Professor Xiao Zhens öffentlichem Kurs "[Blockchain-Technologie und Anwendungen](https://www.bilibili.com/video/BV1Vt411X7JF)" der Peking-Universität, den ich zuvor absolviert habe, ist mir die Weite des Blockchain-Wissenssystems bewusst geworden. Ich plane, eine Reihe von Artikeln zu veröffentlichen, um das Wissen über Blockchain, Bitcoin, Ethereum usw. systematisch zu organisieren. Sollten Fehler oder Auslassungen vorliegen, bitte ich um Diskussion und Korrektur.

## Kryptographische Prinzipien in der Blockchain

Die Blockchain ist eng mit der Kryptographie verbunden, wie beispielsweise die zentrale Public-Private-Key-Verschlüsselungstechnologie, digitale Signaturen und das Hashing, die in Bitcoin verwendet werden, einschließlich vieler Konsensalgorithmen, die auf komplexen kryptographischen Konzepten basieren. Daher müssen wir vor dem Erlernen der Blockchain mehrere zentrale kryptographische Konzepte verstehen, um ein tieferes Verständnis ihrer Anwendungen im Blockchain-System zu erlangen.

### Hash-Funktionen

Eine Hash-Funktion ist eine Methode, die Quelldaten beliebiger Länge durch eine Reihe von Algorithmen in einen Ausgabewert fester Länge umwandelt. Das Konzept ist einfach, aber seine verschiedenen Eigenschaften machen es in vielen Bereichen weit verbreitet.

Sie können diese [Demo](https://andersbrownworth.com/blockchain/hash) besuchen, um zu erfahren, wie Hash-Funktionen funktionieren (am Beispiel von `SHA256`)!

Die erste Eigenschaft ist die Einweg-Irreversibilität. Es ist einfach, eine Hash-Operation auf eine Eingabe x durchzuführen, um den Wert H(x) zu erhalten, aber bei einem gegebenen Wert H(x) ist es nahezu unmöglich, den Wert von x rückwärts zu ermitteln. Diese Eigenschaft schützt die Quelldaten gut.

Die zweite Eigenschaft ist die Kollisionsresistenz. Bei einem gegebenen Wert x und einem anderen Wert y, wenn x nicht gleich y ist, ist es nahezu unmöglich, dass H(x) gleich H(y) ist. Es ist nicht vollständig unmöglich, aber die Wahrscheinlichkeit ist äußerst gering. Daher ist der Hash-Wert eines Datensatzes fast einzigartig, was gut in Szenarien wie der Identitätsverifizierung genutzt werden kann.

Die dritte Eigenschaft ist, dass Hash-Berechnungen unvorhersehbar sind. Es ist schwierig, den Hash-Wert basierend auf bestehenden Bedingungen abzuleiten, aber es ist einfach zu überprüfen, ob er korrekt ist. Dieser Mechanismus wird hauptsächlich im `PoW`-Mining-Mechanismus angewendet.

### Verschlüsselung/Entschlüsselung

Verschlüsselungsmechanismen werden hauptsächlich in zwei Kategorien unterteilt: symmetrische Verschlüsselung und asymmetrische Verschlüsselung.

Der symmetrische Verschlüsselungsmechanismus verwendet denselben Schlüssel für die Informationsverschlüsselung und -entschlüsselung auf beiden Seiten. Er ist bequem und hocheffizient, birgt jedoch ein großes Risiko bei der Schlüsselverteilung. Bei der Verteilung über Netzwerke oder andere Mittel kann der Schlüssel leicht preisgegeben werden, was zu Informationslecks führt.

Der asymmetrische Verschlüsselungsmechanismus bezieht sich hauptsächlich auf den Public-Private-Key-Verschlüsselungsmechanismus. Jede Person generiert durch einen Algorithmus ein Schlüsselpaar, das als öffentlicher Schlüssel und privater Schlüssel bezeichnet wird. Wenn A eine Nachricht an B senden möchte, kann er die Datei mit Bs öffentlichem Schlüssel verschlüsseln und die verschlüsselte Information an B senden. Während dieses Prozesses wird selbst bei Abfangen oder Leckage der Information die Quelldatei nicht offengelegt, sodass sie auf beliebigem Wege verbreitet werden kann. Wenn B die verschlüsselte Datei erhält, verwendet er seinen eigenen privaten Schlüssel zur Entschlüsselung, um den Dateiinhalt zu erhalten. Bs privater Schlüssel wurde über keinen Kanal übertragen und ist nur ihm selbst bekannt, sodass er äußerst sicher ist.

In praktischen Anwendungen ist die asymmetrische Verschlüsselung sehr großer Dateien ineffizient, daher wird in der Regel ein kombinierter Mechanismus angewendet: Angenommen, A möchte eine große Datei D an B senden, verschlüsselt er zunächst die Datei D symmetrisch mit einem Schlüssel K und dann den Schlüssel K asymmetrisch mit Bs öffentlichem Schlüssel. A sendet den verschlüsselten Schlüssel K und die Datei D an B. Selbst wenn sie während der Übertragung abgefangen oder durchgesickert werden, kann der Schlüssel K nicht erhalten werden, da Bs privater Schlüssel nicht verfügbar ist, und somit kann auf die Datei D nicht zugegriffen werden. Nachdem B die verschlüsselte Datei und den Schlüssel erhalten hat, entschlüsselt er zunächst mit seinem privaten Schlüssel, um den Schlüssel K zu erhalten, und verwendet dann den Schlüssel K, um die Datei D zu entschlüsseln und somit den Dateiinhalt zu erhalten.

### Digitale Signaturen

Digitale Signaturen sind eine weitere Anwendung des asymmetrischen Verschlüsselungsmechanismus. Wie bereits erwähnt, hat jeder ein Paar generierter öffentlicher und privater Schlüssel. Bei Verschlüsselungs-/Entschlüsselungsanwendungen wird der öffentliche Schlüssel zur Verschlüsselung und der private Schlüssel zur Entschlüsselung verwendet, während der digitale Signaturmechanismus genau umgekehrt funktioniert. Angenommen, ein Dateibesitzer verschlüsselt die Datei mit seinem privaten Schlüssel, können andere sie mit seinem öffentlichen Schlüssel entschlüsseln. Wenn ein Ergebnis erzielt wird, kann dies den Besitz der Datei beweisen.

Die typischste Anwendung des digitalen Signaturmechanismus findet sich im Bitcoin-Blockchain-Netzwerk, wo private Schlüssel verwendet werden, um den Besitz von Bitcoins zu beweisen und Transaktionen zu signieren, während andere öffentliche Schlüssel verwenden können, um zu überprüfen, ob die Transaktion legal ist. Der gesamte Prozess erfordert keine Offenlegung des eigenen privaten Schlüssels, was die Sicherheit der Vermögenswerte gewährleistet.

## Grundkonzepte der Blockchain

Im Laufe der Geschichte haben sich die Buchführungsmethoden der Menschen von der einfachen Buchführung über die doppelte Buchführung und die digitale Buchführung bis hin zur verteilten Buchführung entwickelt. Die traditionelle zentralisierte digitale Buchführung beruht oft auf der Glaubwürdigkeit bestimmter Organisationen, was einige Vertrauensrisiken birgt. Die Blockchain-Technologie ist im Wesentlichen eine verteilte Ledger-Technologie, bei der eine Gruppe von Menschen gemeinsam eine dezentrale Datenbank pflegt und Konsensmechanismen verwendet, um gemeinsam Buch zu führen. Die Blockchain erleichtert die Rückverfolgung historischer Aufzeichnungen, und aufgrund der Existenz dezentraler Vertrauensmechanismen ist sie nahezu fälschungssicher (oder die Kosten für Manipulationen übersteigen bei weitem den Nutzen).

Im Vergleich zu traditionellen Datenbanken hat die Blockchain nur zwei Operationen: Hinzufügen und Abfragen. Alle historischen Aufzeichnungen von Operationen werden genau im Ledger aufbewahrt und sind unveränderlich, was hohe Transparenz und Sicherheit bietet. Natürlich besteht der Kompromiss darin, dass alle Knoten durch bestimmte Mechanismen einen Konsens erreichen müssen (daher geringere Effizienz, ungeeignet für Echtzeitoperationen), und da jeder Knoten dauerhaft historische Aufzeichnungen speichern muss, nimmt dies viel Speicherplatz in Anspruch.

### Anwendungsszenarien

> Wie also bestimmen wir, ob ein Unternehmen/Geschäft für die Einführung der Blockchain als Lösung geeignet ist?

1. Wird eine Datenbank benötigt?
2. Ist ein gemeinsamer Schreibzugriff erforderlich?
3. Ist die Herstellung von Vertrauen zwischen mehreren Parteien erforderlich?
4. Kann es ohne Eingreifen von Drittinstitutionen funktionieren?
5. Kann es ohne Berechtigungsmechanismen funktionieren?

Die Blockchain als verteilte Datenbank dient hauptsächlich der Informationsspeicherung. Durch ihre verschiedenen Mechanismen ermöglicht sie es Einheiten mit gemeinsamen Bedürfnissen, aber ohne gegenseitiges Vertrauen, zu relativ geringen Kosten einen Konsens zu erreichen, ohne dass Drittinstitutionen eingreifen müssen, und erfüllt damit Bedürfnisse. Darüber hinaus verfügt das System über Funktionen wie verschlüsselte Authentifizierung und hohe Transparenz, die einige geschäftliche Anforderungen erfüllen können. Wenn jedoch die betroffenen Daten nicht öffentlich gemacht werden können, das Datenvolumen sehr groß ist, externe Dienste zur Datenspeicherung benötigt werden oder wenn sich Geschäftsregeln häufig ändern, dann ist die Blockchain als Lösung nicht geeignet.

> Daher sind unter den oben genannten Kriterien die folgenden Bedürfnisse sehr gut für die Blockchain als Lösung geeignet:

1. Notwendigkeit, eine gemeinsame Datenbank mit mehreren beteiligten Parteien einzurichten
2. Die am Geschäft beteiligten Parteien haben kein Vertrauen aufgebaut
3. Das bestehende Geschäft vertraut einer oder mehreren Vertrauensinstitutionen
4. Das bestehende Geschäft hat verschlüsselte Authentifizierungsbedürfnisse
5. Daten müssen in verschiedene Datenbanken integriert werden, und der Bedarf an Geschäftsdigitalisierung und Konsistenz ist dringend
6. Es gibt einheitliche Regeln für Systemteilnehmer
7. Mehrparteien-Entscheidungsfindung ist transparent
8. Objektive, unveränderliche Aufzeichnungen werden benötigt
9. Nicht-Echtzeit-Geschäftsabwicklung

In der Praxis müssen Unternehmen in vielen Anwendungsszenarien jedoch einige Kompromisse zwischen Dezentralisierung und Effizienz eingehen. Manchmal haben viele komplexe Geschäfte unterschiedliche Anforderungen an Transparenz und Regeln. Daher gibt es basierend auf komplexen kommerziellen Bedürfnissen auch Lösungen wie "Konsortium-Chains", die sich besser in bestehende Systeme integrieren lassen, um geschäftliche Anforderungen zu erfüllen.

## Arten von Blockchains

Es gibt verschiedene Arten von Blockchains, hauptsächlich private Chains, öffentliche Chains und Konsortium-Chains.

Private Chains werden hauptsächlich in einem bestimmten Bereich angewendet oder laufen nur innerhalb eines bestimmten Unternehmens und dienen vor allem dazu, Vertrauensprobleme zu lösen, wie beispielsweise in Szenarien der abteilungsübergreifenden Zusammenarbeit. Im Allgemeinen müssen externe Institutionen nicht auf die Daten zugreifen.

Öffentliche Chains sind offene Transaktionen, die oft in Geschäften verwendet werden, die eine Offenlegung von Transaktionen/Daten erfordern, wie Authentifizierung, Rückverfolgbarkeit, Finanzen und andere Szenarien, wie Bitcoin, Ethereum und `EOS`.

Das größte Merkmal von Konsortium-Chains ist, dass Knoten Berechtigungen verifizieren müssen, bevor sie am Blockchain-Netzwerk teilnehmen können, und die Authentifizierung ist in der Regel mit ihren realen Rollen verbunden. Daher haben Konsortium-Chains auch zentralisierte Attribute, aber Effizienz, Skalierbarkeit und Transaktionsprivatsphäre sind stark verbessert, was den Anforderungen von Unternehmensanwendungen entspricht. Am weitesten verbreitet ist dabei `Hyperledger Fabric`. Erwähnenswert ist, dass Konsortium-Chains oft keine Token als Anreize benötigen, sondern die teilnehmenden Knoten als Buchführungsknoten verwenden und die wirtschaftlichen Vorteile, die durch abteilungsübergreifende Geschäftszusammenarbeit durch Blockchain-Mechanismen entstehen, als interne Anreize nutzen, was eine gesündere Methode ist, die besser zu Unternehmensanwendungen passt.

Langfristig werden öffentliche Chains und Konsortium-Chains technologisch allmählich konvergieren. Selbst für dasselbe Geschäft können Daten, die Vertrauen erfordern, auf öffentlichen Chains platziert werden, während einige Branchendaten und private Daten auf Konsortium-Chains platziert werden können, um die Transaktionsprivatsphäre durch Berechtigungsverwaltung zu schützen.

## Grundstruktur der Blockchain

> Woraus besteht also eine Blockchain?

1. Blöcke
2. Blockchain
3. P2P-Netzwerk
4. Konsensmechanismus
5. ...

### Blöcke

Die Blockchain ist ein Ökosystem, das aus Blöcken besteht. Jeder Block enthält den Hash-Wert des vorherigen Blocks, Zeitstempel, `Merkle Root`, `Nonce` und Blockdaten. Die Blockgröße von Bitcoin beträgt 1 MB. Sie können diese [Demo](https://andersbrownworth.com/blockchain/block) besuchen, um den Prozess der Blockerstellung zu erleben.

Da jeder Block den Hash-Wert des vorherigen Blocks enthält, führen selbst extrem kleine Änderungen aufgrund der zuvor erwähnten Hash-Eigenschaften zu völlig anderen Hash-Werten, was es einfach macht, festzustellen, ob ein Block manipuliert wurde. Der Nonce-Wert wird hauptsächlich verwendet, um die Mining-Schwierigkeit anzupassen und die Zeit auf etwa 10 Minuten zu begrenzen, um die Sicherheit zu gewährleisten.

### Blockchain

Alle miteinander verbundenen Blöcke bilden die Blockchain, die ein Ledger ist, das alle historischen Transaktionsaufzeichnungen im Netzwerk speichert. Da jeder Block die Hash-Informationen des vorherigen Blocks enthält (zum Beispiel nimmt das Bitcoin-System den Block-Header des vorherigen Blocks zweimal), wird eine Änderung einer Transaktion dazu führen, dass die Blockchain bricht. Es gibt eine kleine [Demo](https://andersbrownworth.com/blockchain/blockchain), die diesen Prozess gut demonstriert, Sie können sie ausprobieren!

### P2P-Netzwerk

Ein P2P-Netzwerk ist eine Art verteiltes Netzwerk, das zum Teilen von Informationen und Ressourcen zwischen verschiedenen Benutzern verwendet wird. Es ist ein verteiltes Netzwerk, in dem jeder eine Kopie der Informationen erhalten und Zugriffsrechte haben kann. Im Gegensatz dazu ist ein zentralisiertes Netzwerk eines, bei dem sich jeder mit einem (oder einer Gruppe von) zentralisierten Netzwerk(en) verbindet; ein dezentralisiertes Netzwerk hat mehrere solcher zentralen Netzwerke, aber kein einzelnes Netzwerk kann alle Informationen haben. Das folgende Bild erklärt gut die Unterschiede zwischen ihnen:

![blockchain_network](https://image.pseudoyu.com/images/blockchain_network.png)

### Konsensmechanismus

Das Blockchain-Netzwerk besteht aus mehreren Netzwerkknoten, von denen jeder eine Kopie der Informationen speichert. Wie einigen sie sich also auf Transaktionen? Mit anderen Worten, als unabhängige Knoten benötigen sie einen Mechanismus, um gegenseitiges Vertrauen zu gewährleisten, was der Konsensmechanismus ist.

Gängige Konsensmechanismen umfassen `PoW (Proof of Work)`, `PoS (Proof of Stake)`, `DPoS (Delegated Proof of Stake)`, `DBFT (Delegated Byzantine Fault Tolerance)` usw.

Bitcoin/Ethereum verwendet hauptsächlich den Proof-of-Work-Mechanismus, der die Kosten für böswillige Knoten durch Rechenleistungswettbewerb erhöht. Durch dynamische Anpassung der Mining-Schwierigkeit wird die Zeit für eine Transaktion auf etwa 10 Minuten kontrolliert (6 Bestätigungen), aber da Bitcoin-Mining immer beliebter wird und immer mehr Ressourcen verbraucht, verursacht es Schäden für die Umwelt. Einige Mining-Pools mit großen Ressourcen können auch einige Zentralisierungsrisiken verursachen.

Der Proof-of-Stake-Mechanismus erreicht Konsens durch Abstimmung der Stake-Inhaber (in der Regel Token). Dieser Mechanismus erfordert keinen großen Rechenleistungswettbewerb wie Proof of Work, birgt aber auch einige Risiken, das sogenannte `Nothing at Stake`-Problem, bei dem viele Stake-Inhaber auf alle Blöcke wetten und davon profitieren werden. Um dieses Problem zu lösen, legt das System einige Regeln fest, wie zum Beispiel die Festlegung einiger Strafmechanismen für Benutzer, die gleichzeitig Blöcke auf mehreren Ketten erstellen oder Blöcke auf falschen Ketten erstellen. Ethereum wechselt derzeit zu diesem Konsensmechanismus.

`EOS` verwendet delegierten Proof of Stake und wählt einige repräsentative Knoten für die Abstimmung aus. Diese Methode zielt darauf ab, die Effizienz und die Ergebnisse der Community-Abstimmung zu optimieren, bringt aber einige Zentralisierungsrisiken mit sich.

Der `DBFT`-Konsensmechanismus erreicht Konsens, indem er den Knoten unterschiedliche Rollen zuweist, was den Overhead erheblich reduzieren und Forks vermeiden kann, aber es besteht auch das Risiko, dass Kernrollen böswillig handeln.

## Blockchain-Sicherheit und Datenschutz

### Sicherheit

Als relativ neue Technologie hat die Blockchain auch viele Sicherheitslücken, wie Angriffe auf Kryptowährungsbörsen, Schwachstellen in Smart Contracts, Angriffe auf Konsensprotokolle, Angriffe auf Netzwerkverkehr (Internet ISP) und das Hochladen bösartiger Daten. Berühmte Fälle sind der Mt.Gox-Vorfall und der Ethereum DAO-Vorfall. Daher sind die Sicherheitsrisiken der Blockchain auch eine wichtige Forschungsrichtung für die Blockchain.

Risikoanalysen können aus den Perspektiven von Protokollen, Verschlüsselungsschemata, Anwendungen, Programmentwicklung und Systemen durchgeführt werden, um die Sicherheit von Blockchain-Anwendungen zu verbessern. Zum Beispiel kann in der Ethereum-Blockchain eine Analyse der Programmiersprache `Solidity`, der `EVM` und der Blockchain selbst durchgeführt werden.

Ein Beispiel für einen Angriff, der als kostengünstiger Angriff in Smart Contracts bezeichnet wird, besteht darin, Operationen mit relativ niedrigen `Gas`-Gebühren im Ethereum-Netzwerk zu identifizieren und diese wiederholt auszuführen, um das gesamte Netzwerk zu stören.

Für Sicherheitsprobleme wäre der Aufbau eines allgemeinen Code-Detektors zur Überprüfung auf bösartigen Code eine universellere Lösung.

### Datenschutz

Bei der Diskussion von Blockchain-Konzepten erwähnten wir eines ihrer wichtigen Merkmale: Privatsphäre. Das heißt, jeder kann die Transaktionsdetails und historischen Aufzeichnungen auf der Kette sehen. Diese Funktion wird hauptsächlich in Lieferketten wie Lebensmittel und Medikamente angewendet, aber für einige Finanzszenarien, wie persönliche Kontostände und Transaktionsinformationen, kann sie leicht einige Datenschutzrisiken verursachen.

> Welche Technologien können also angewendet werden, um die Privatsphäre in diesen hochwertigen, sensiblen Informationsszenarien zu schützen?

Auf Hardwareebene können vertrauenswürdige Ausführungsumgebungen eingesetzt werden, die sichere Hardware wie `Intel SGX` verwenden, was die Privatsphäre stark gewährleistet; das Netzwerk kann Mehrwege-Weiterleitung verwenden, um zu vermeiden, dass echte Identitäten aus Knoten-IP-Adressen abgeleitet werden.

Auf technischer Ebene kann die Coin-Mixing-Technologie viele Transaktionen mischen, was es schwierig macht, den entsprechenden Transaktionsabsender und -empfänger herauszufinden; die Blind-Signature-Technologie kann sicherstellen, dass Drittinstitutionen die an der Transaktion beteiligten Parteien nicht verknüpfen können; Ring-Signaturen werden verwendet, um die Anonymität von Transaktionssignaturen zu gewährleisten; Zero-Knowledge-Beweise können angewendet werden, damit eine Partei (Beweisführer) einer anderen Partei (Verifizierer) beweisen kann, dass eine Aussage korrekt ist, ohne andere Informationen als die Tatsache preiszugeben, dass die Aussage korrekt ist; homomorphe Verschlüsselung kann die Originaldaten schützen, bei gegebenen E(x) und E(y) ist es einfach, einige verschlüsselte Funktionswerte über x und y zu berechnen (homomorphe Operationen); attributbasierte Verschlüsselung (ABE) fügt jedem Knoten einige Attribute/Rollen hinzu und implementiert Berechtigungskontrolle, wodurch die Privatsphäre geschützt wird.

Es ist erwähnenswert, dass selbst wenn eine Transaktion mehrere Ein- und Ausgänge erzeugt, die Adressen dieser Ein- und Ausgänge immer noch von Menschen assoziiert werden können; außerdem können Adresskonten und reale Identitäten ebenfalls assoziiert werden.

## Fazit

Das oben Genannte ist eine Zusammenfassung des Grundwissens über Blockchain, hauptsächlich mit Fokus auf Konzepte und Prinzipien. In Zukunft werde ich Analysen und Gedanken zu typischen Anwendungen wie Bitcoin, Ethereum, `Hyperledger Fabric` aktualisieren und heiße Technologien wie IPFS, Cross-Chain, NFT usw. erforschen. Bleiben Sie dran!

## Referenzen

> 1. [COMP7408 Distributed Ledger and Blockchain Technology](https://msccs.cs.hku.hk/public/courses/2020/COMP7408A/), *Professor S.M. Yiu, HKU*
> 2. [Udacity Blockchain Developer Nanodegree](https://www.udacity.com/course/blockchain-developer-nanodegree--nd1309), *Udacity*
> 3. [Blockchain Technology and Applications](https://www.bilibili.com/video/BV1Vt411X7JF), *Xiao Zhen, Peking University*
> 4. [Advanced Blockchain Technology and Practice](https://www.ituring.com.cn/book/2434), *Cai Liang, Li Qilei, Liang Xiubo, Zhejiang University | Hyperchain*