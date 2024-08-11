---
title: "Detaillierte Erklärung der Systemarchitektur von Hyperledger Fabric"
date: 2021-03-20T12:12:17+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "structure"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Da mein Abschlussprojekt hauptsächlich auf der öffentlichen Ethereum-Blockchain basierte und es an Szenarien für Unternehmensanwendungen mangelte, beschränkte sich mein bisheriges Verständnis von Hyperledger Fabric größtenteils auf Konzepte wie den Berechtigungsverwaltungsmechanismus, Kanäle und flexible Smart-Contract-Erstellung. Ich hatte nur eine vage Vorstellung von seiner Architektur, den Rollen verschiedener Knoten und den Betriebsmechanismen. Kürzlich, während ich den Kurs "FITE3011 Distributed Ledger and Blockchain" an der HKU belegte, gab der Professor eine detaillierte Erklärung der Funktionsprinzipien von Hyperledger Fabric, der Netzwerkeinrichtung und des Chaincode-bezogenen Wissens. Ich fand es ungemein nützlich. Durch diesen Artikel möchte ich meine Gedanken zu diesem Thema ordnen. Sollte es Fehler oder Auslassungen geben, freue ich mich über Diskussionen und Korrekturen.

## Überblick über Hyperledger

Um Hyperledger Fabric zu verstehen, schauen wir uns zunächst an, was sein übergeordnetes Projekt, Hyperledger, ist.

Anwendungen auf Unternehmensebene haben komplexe Geschäftslogiken und Teilnehmerrolleneinteilungen, mit hohen Anforderungen an die Effizienz der Geschäftsausführung und Sicherheit. Für gängige Szenarien wie Zahlungen und Daten-/Informationstransaktionen ist auch der Datenschutz von höchster Bedeutung. Daher erfüllen gängige öffentliche Blockchains wie Bitcoin und Ethereum nicht die Bedürfnisse der meisten Unternehmensanwendungen. Die verteilten und unveränderlichen historischen Ledger-Eigenschaften der Blockchain können jedoch komplexe betriebliche Prozesse vermeiden, die durch rechtliche Vorschriften und Währungen verschiedener Länder/Regionen in Szenarien wie Rückverfolgbarkeit und grenzüberschreitendem E-Commerce verursacht werden, und so die Effizienz erheblich verbessern. Infolgedessen entwickeln sich Konsortium-Blockchains für Unternehmen kontinuierlich weiter.

Konsortium-Blockchains sind im strengen Sinne nicht wirklich "dezentralisiert". Sie führen Berechtigungsverwaltungsmechanismen ein (die Unternehmensrollen in realen Geschäften kombinieren), um den Präventionsmechanismus gegen böswilliges Verhalten von Knoten zu schwächen und dadurch die Effizienz zu verbessern und komplexe Geschäftslogiken zu bewältigen.

Unter ihnen ist Hyperledger eine Reihe von Open-Source-Projekten, die von der Linux Foundation gepflegt werden und sich auf branchenübergreifende verteilte Technologien konzentrieren. Es zielt darauf ab, unternehmenstaugliche, quelloffene, verteilte Klassifizierungsframeworks und Codebibliotheken zu erstellen, die Geschäftsanwendungsfälle unterstützen; eine neutrale, offene und community-gesteuerte Infrastruktur bereitzustellen; technische Communities aufzubauen und zu fördern; Blockchain- und Shared-Ledger-Konzeptnachweise, Anwendungsfälle, Versuche und Bereitstellungen zu entwickeln; Industriestandards zu etablieren; mehr Unternehmen zur Teilnahme am Aufbau und der Anwendung von Distributed-Ledger-Technologie zu ermutigen und ein offenes Ökosystem zu bilden; die Öffentlichkeit über Marktchancen in der Blockchain-Technologie aufzuklären.

### Designphilosophie

![hyperledger_design_philosophy](https://image.pseudoyu.com/images/hyperledger_design_philosophy.png)

Hyperledger hat mehrere Kern-Designphilosophien:

1. Es verbessert die Effizienz für spezifische Geschäftsszenarien von Unternehmen und hat einzigartige Vorteile in Szenarien wie der Rückverfolgbarkeit. Jedes Unternehmen kann ein unabhängiges Hyperledger-Projekt für seine eigenen Szenarien pflegen. Daher muss es keine digitale Währung verwenden, um Benutzer zur Teilnahme am Blockchain-System zu motivieren, wie es öffentliche Blockchains tun.
2. Unternehmensanwendungsszenarien sind relativ komplex, und Hyperledger beteiligt sich oft nur an einem oder einigen Aspekten. Daher ist die Interaktion mit anderen bestehenden Systemen unerlässlich. Aus diesem Grund konzentriert sich Hyperledger in seinem Design darauf, vollständige APIs für andere Systeme bereitzustellen, um sie aufzurufen und mit ihnen zu interagieren.
3. Die Rahmenstruktur von Hyperledger ist modular und erweiterbar. Unternehmen können verschiedene Module entsprechend spezifischen Geschäftsanforderungen auswählen und vermeiden so komplexe Geschäftslogiken und aufgeblähte Systeme.
4. Sicherheit ist für Unternehmensanwendungen von größter Bedeutung, insbesondere in vielen Anwendungsszenarien, die hochwertige Transaktionen oder sensible Daten beinhalten. Daher werden viele Mechanismen bereitgestellt, um die Sicherheit zu gewährleisten (wie z.B. der Kanal-Mechanismus von Fabric).
5. Neben der Interaktion mit bestehenden Systemen könnten Unternehmens-Blockchain-Anwendungen in Zukunft mit vielen verschiedenen Blockchain-Netzwerken interagieren. Daher sollten die meisten Smart Contracts/Anwendungen Portabilität über Blockchain-Netzwerke hinweg haben, um komplexere und leistungsfähigere Netzwerke zu bilden.

![hyperledger_family](https://image.pseudoyu.com/images/hyperledger_family.png)

#### Frameworks

Hyperledger hat die folgenden Projekte, von denen Fabric derzeit am weitesten verbreitet ist. Dieser Artikel wird hauptsächlich das Fabric-Blockchain-Netzwerk vorstellen:
- Burrow
- Fabric
- Grid
- Indy
- Iroha
- Sawtooth

#### Tools

1. Hyperledger Cello. Wird hauptsächlich für eine bequemere Einrichtung und Verwaltung von Blockchain-Diensten verwendet, reduziert die Komplexität der Projektrahmen-Bereitstellung und -Wartung; kann zum Aufbau von Blockchain-BaaS-Plattformen verwendet werden; kann Blockchains über ein Dashboard erstellen und verwalten, sodass technisches Personal bequemer entwickeln und bereitstellen kann; kann SaaS-Bereitstellungsmodelle in Blockchain-Systeme einführen und Unternehmen dabei helfen, Frameworks weiterzuentwickeln.
2. Hyperledger Explorer. Ein Visualisierungstool für Blockchain-Operationen, das zur Erstellung benutzerfreundlicher Webanwendungen verwendet werden kann; es ist der erste Blockchain-Explorer für Hyperledger, der es Benutzern ermöglicht, Transaktionen, Netzwerke, Smart Contracts, Speicher und andere Informationen anzuzeigen/aufzurufen/bereitzustellen/abzufragen.

## Hyperledger Fabric

Konzentrieren wir uns auf das Fabric-Projekt, das am weitesten verbreitet ist. Es ist ein modulares, erweiterbares Blockchain-Konsortium-Kettenprojekt, das von der Linux Foundation gepflegt wird und nicht von Kryptowährungen abhängig ist. Es bietet Schutz für Geschäfte zwischen Entitäten, die gemeinsame Ziele (Geschäftsanforderungen) haben, sich aber nicht vollständig vertrauen, wie z.B. grenzüberschreitender E-Commerce, Fondstransaktionen, Rückverfolgbarkeit usw.

### Architektur

![ethereum_architecture_simple](https://image.pseudoyu.com/images/ethereum_architecture_simple.png)

In den meisten öffentlichen Blockchains ist die Architektur "Ordnen - Ausführen - Validieren - Zustand aktualisieren". Zum Beispiel verwendet die Bitcoin-Blockchain bei einer neuen Transaktion zunächst den PoW-Mechanismus, um den Block zu ordnen, dann verifiziert jeder Knoten im Bitcoin-Netzwerk ihn individuell, und schließlich wird der Zustand aktualisiert. Da die Verifizierung sequentiell erfolgen muss, bestimmt diese Methode, dass ihre Ausführungseffizienz relativ niedrig ist.

Fabric verwendet die Architektur "Ausführen - Ordnen - Validieren - Zustand aktualisieren".

![hyperledger_fabric_architecture](https://image.pseudoyu.com/images/hyperledger_fabric_architecture.png)

Nach Erhalt einer neuen Transaktion wird sie zunächst dem Endorsement-Knoten zur lokalen Simulation der Transaktionsausführung (und Endorsement) vorgelegt, dann werden die bestätigten Transaktionen geordnet und gesendet, und jeder Knoten validiert die Transaktion, bevor der Zustand aktualisiert wird.

![hyperledger_fabric_architecture_complete](https://image.pseudoyu.com/images/hyperledger_fabric_architecture_complete.png)

Wie oben in den Merkmalen der Konsortium-Blockchain erwähnt, erfordert der Beitritt zum Fabric-Netzwerk eine Berechtigung (Identitätsüberprüfung), und jeder Knoten im Fabric-Netzwerk hat seine eigene Identität.

Insgesamt unterstützt Fabric komplexe Geschäftsszenarien von Unternehmen durch eine modulare, steckbare Architektur, schwächt böswilliges Knotenverhalten durch Identitätsüberprüfung (Bindung an reale Identitäten) und verbessert die Systemsicherheit und den Datenschutz erheblich durch den Kanal-Mechanismus.

#### MSP (Membership Service Provider)

Wie werden also die Identitäten der Teilnehmer im Fabric-Netzwerk verwaltet?

Fabric verfügt über einen MSP (Membership Service Provider), der hauptsächlich CA-Zertifikate verwendet, um zu überprüfen, welche Mitglieder vertrauenswürdig sind. Das Fabric CA-Modul ist unabhängig und kann Zertifikatsdienste verwalten, ermöglicht aber auch den Zugriff von Drittanbieter-CAs, was den Anwendungsbereich des Systems stark erweitert.

![hyperledger_fabric_ca_structure](https://image.pseudoyu.com/images/hyperledger_fabric_ca_structure.png)

Wie in der obigen Abbildung gezeigt, bietet Fabric CA sowohl Client- als auch SDK-Methoden zur Interaktion mit CA. Jede Fabric CA hat eine Root CA oder eine Zwischeninstanz-CA. Um die CA-Sicherheit weiter zu verbessern, können Cluster verwendet werden, um Zwischeninstanz-CAs aufzubauen.

![hyperledger_fabric_ca_hierarchy](https://image.pseudoyu.com/images/hyperledger_fabric_ca_hierarchy.png)

Betrachten wir die CA-Hierarchie genauer, so verwendet sie im Allgemeinen eine dreischichtige Baumstruktur von Root CA, Business CA und User CA. Alle untergeordneten CAs erben das Vertrauenssystem der übergeordneten CA. Die Root CA wird verwendet, um Business CAs auszustellen, während Business CAs verwendet werden, um spezifische User CAs auszustellen (Identitätsauthentifizierungs-CA, Transaktionssignatur, sichere Kommunikations-CA usw.)

#### Kanäle

Wie bereits erwähnt, verwendet Fabric den Kanal-Mechanismus, um die Transaktionssicherheit und den Datenschutz zu gewährleisten. Im Wesentlichen ist jeder Kanal ein unabhängiges Ledger, auch eine unabhängige Blockchain, mit unterschiedlichen Weltzuständen. Ein Knoten im Netzwerk kann gleichzeitig mehreren Kanälen beitreten. Dieser Mechanismus kann verschiedene Geschäftsszenarien effektiv unterteilen, ohne sich Sorgen um die Offenlegung von Transaktionsinformationen machen zu müssen.

#### Chaincode

Fabric verfügt auch über Smart Contracts ähnlich wie Ethereum, genannt Chaincode. Smart Contracts ermöglichen es externen Anwendungen, mit dem Ledger im Fabric-Netzwerk zu interagieren. Im Gegensatz zu Ethereum verwendet Fabric Docker anstelle einer spezifischen virtuellen Maschine zur Speicherung von Chaincode und bietet eine sichere, leichtgewichtige Sprachausführungsumgebung.

Chaincode ist hauptsächlich in Systemchaincode und Benutzerchaincode unterteilt. Systemchaincode ist in das System eingebettet und bietet Unterstützung für Systemkonfiguration und -verwaltung; Benutzerchaincode läuft in separaten Docker-Containern und bietet Unterstützung für Anwendungen der oberen Ebene. Benutzer können Benutzerchaincode über Chaincode-bezogene APIs schreiben, um den Zustand im Ledger zu aktualisieren.

Chaincode kann nach Installation und Instanziierung aufgerufen werden. Während der Installation muss angegeben werden, auf welchem Peer-Knoten er installiert werden soll (einige Knoten haben möglicherweise keinen Chaincode), und während der Instanziierung müssen der Kanal und die Endorsement-Richtlinie angegeben werden.

Chaincodes können sich auch gegenseitig aufrufen, wodurch eine flexiblere Anwendungslogik geschaffen wird.

#### Konsensmechanismus

Der breite Konsensmechanismus in Fabric umfasst Endorsement, Ordering und Validierung. Im engeren Sinne bezieht sich Konsens auf das Ordering.

Im Fabric-Blockchain-Netzwerk müssen Transaktionen zwischen verschiedenen Teilnehmern in der Reihenfolge ihres Auftretens in das verteilte Ledger geschrieben werden, was sich auf den Konsensmechanismus stützt. Es gibt hauptsächlich drei Typen:
- SOLO (beschränkt auf Entwicklung)
- Kafka (eine Messaging-Plattform)
- Raft (zentralisierter im Vergleich zu Kafka)

#### Netzwerkprotokoll

Wie wird also die Zustandsverteilung zwischen den Knoten im Fabric-Netzwerk durchgeführt?

Externe Clients verwenden gRPC, um Fernaufrufe an verschiedene Knoten im Fabric-Netzwerk zu machen, während die Synchronisierung zwischen Knoten im P2P-Netzwerk über das Gossip-Protokoll erfolgt.

Das Gossip-Protokoll wird hauptsächlich für den Datenaustausch zwischen mehreren Knoten im Netzwerk verwendet. Es ist relativ einfach zu implementieren und hat eine hohe Fehlertoleranzrate. Das Prinzip besteht darin, dass der Datensender zufällig mehrere Knoten aus dem Netzwerk auswählt, um an sie zu senden, und nachdem diese Knoten die Daten erhalten haben, senden sie sie zufällig an mehrere Knoten außer dem Absender, wiederholt, bis alle Knoten einen Konsens erreichen (Komplexität ist LogN).

#### Verteiltes Ledger

Schließlich werden alle Transaktionen im verteilten Ledger aufgezeichnet, das der Kern vieler Blockchain-Funktionen ist. In Fabric können Transaktionen relevante Geschäftsinformationen speichern. Ein Block ist eine Sammlung geordneter Transaktionen, und die Verknüpfung von Blöcken durch kryptografische Algorithmen bildet die Blockchain. Das verteilte Ledger zeichnet hauptsächlich den Weltzustand (den neuesten Zustand des verteilten Ledgers, im Allgemeinen unter Verwendung von CouchDB für einfache Abfragen) und Transaktionsprotokolle (Aktualisierungsverlauf des Weltzustands, Aufzeichnung der Blockchain-Struktur, unter Verwendung von LevelDB) auf. Jede Operation am Ledger wird im Protokoll aufgezeichnet und ist unveränderlich.

#### Anwendungsprogrammierschnittstelle

Für Anwendungen, die auf Fabric basieren, werden zwei Hauptmöglichkeiten der Interaktion bereitgestellt: SDK-Entwicklungstoolkit und CLI-Befehlszeile.

### Kernrollen in der Fabric-Blockchain

Zunächst sollte erwähnt werden, dass die Rollen im Fabric-Netzwerk allesamt logische Rollen sind. Zum Beispiel könnte Peer-Knoten A in einigen Geschäften sowohl ein Ordering-Knoten als auch ein Endorsement-Knoten sein, und eine Rolle wird nicht unbedingt von einem einzelnen Knoten gespielt.

Als Nächstes stellen wir die Funktionen und Rollen jeder Rolle vor.

Clients unterzeichnen hauptsächlich Transaktionen, reichen Transaktionsvorschläge bei Endorsement-Knoten ein, erhalten bestätigte Transaktionen und senden sie an Ordering-Knoten; Endorsement-Knoten simulieren lokal die Ausführung von Transaktionsvorschlägen, um Transaktionen zu verifizieren (Richtlinien werden durch Chaincode festgelegt), unterzeichnen und geben bestätigte Transaktionen zurück; Ordering-Knoten verpacken Transaktionen in Blöcke und senden sie dann an verschiedene Knoten, ohne an der Transaktionsausführung und -verifizierung teilzunehmen. Mehrere Ordering-Knoten können ein OSN bilden; alle Knoten führen das Blockchain-Ledger.

### Zusammenfassung der Vorteile

Fabric weist verschiedene komplexe Aspekte von Unternehmensanwendungen verschiedenen logischen Rollenknoten zu (Endorsement, Ordering usw.), wodurch Netzwerkengpässe beseitigt werden, da nicht alle Knoten ressourcenintensive Operationen wie Ordering übernehmen müssen; nach der Rollenzuweisung werden bestimmte Transaktionen nur auf bestimmten Knoten bereitgestellt und ausgeführt und können parallel ausgeführt werden, was die Effizienz und Sicherheit erheblich verbessert und gleichzeitig einige Geschäftslogiken verbirgt; daher können verschiedene flexible Zuweisungsschemata entsprechend unterschiedlichen Geschäftsanforderungen gebildet werden, wodurch die Erweiterbarkeit des Systems stark verbessert wird.

Die Einstellung von Konsensmechanismen, Berechtigungsverwaltung, Verschlüsselungsmechanismen, Ledgern und anderen Modulen als steckbar und die Möglichkeit, dass verschiedene Chaincodes unterschiedliche Endorsement-Richtlinien festlegen können, macht den Vertrauensmechanismus flexibler und ermöglicht die Einrichtung effizienter Systeme entsprechend den Geschäftsanforderungen.

Die Fabric CA für die Mitgliederidentitätsverwaltung ist ein separates Projekt, das mehr Funktionen bereitstellen und direkt mit vielen Drittanbieter-CAs kommunizieren und interagieren kann, was es leistungsfähiger und für komplexe Unternehmensszenarien geeigneter macht.

Die Multikanal-Funktion isoliert Daten zwischen verschiedenen Kanälen und verbessert so die Sicherheit und den Datenschutz.

Chaincode unterstützt verschiedene Programmiersprachen wie Java, Go, Node usw., was es flexibler macht und mehr Drittanbieter-Erweiterungsanwendungen unterstützt, wodurch die Kosten für Geschäftsmigration und -wartung reduziert werden.

### Fabric-Anwendungsentwicklung und Interaktion

![hyperledger_fabric_application_interact](https://image.pseudoyu.com/images/hyperledger_fabric_application_interact.png)

Das obige Diagramm zeigt den Entwicklungs- und Interaktionsprozess für einen Blockchain-Entwickler, der die Fabric-Blockchain anwendet.

Entwickler sind hauptsächlich für die Entwicklung von Anwendungen und Smart Contracts (Chaincode) verantwortlich. Anwendungen interagieren mit Smart Contracts über SDK, während die Logik von Smart Contracts Operationen wie get, put, delete am Ledger durchführen kann.

### Fabric-Arbeitsablauf

![hyperledger_fabric_transaction_flow](https://image.pseudoyu.com/images/hyperledger_fabric_transaction_flow.png)

Als Nächstes überprüfen wir das Arbeitsprinzip des Fabric-Netzwerks anhand eines vollständigen Transaktionsablaufs

0. Vor allen Operationen ist es notwendig, eine rechtmäßige Identität von CA zu erhalten und den Kanal anzugeben
1. Zuerst reicht der Client einen Transaktionsvorschlag (mit seiner eigenen Unterschrift) bei den Endorsement-Knoten ein
2. Nach Erhalt des Transaktionsvorschlags simulieren die Endorsement-Knoten die Ausführung unter Verwendung des lokalen Zustands, bestätigen und unterzeichnen die Transaktion und geben sie zurück (einschließlich Read-Write Set, Unterschrift usw.)
3. Nachdem der Client genügend Bestätigungen gesammelt hat (Richtlinie durch Chaincode festgelegt, wie im Beispiel im Diagramm, Erhalt von 2 Bestätigungen), reicht er die bestätigte Transaktion bei den Ordering-Knoten (OSN) ein
4. Die Ordering-Knoten verpacken Transaktionen in Blöcke, ordnen sie (ohne Ausführung oder Überprüfung der Transaktionsrichtigkeit) und senden sie an alle Knoten
5. Alle Knoten validieren die neuen Blöcke und übertragen sie in das Ledger

![hyperledger_fabric_processes](https://image.pseudoyu.com/images/hyperledger_fabric_processes.png)

Als Nächstes zerlegen wir jede Phase im Detail

#### Ausführungs-/Endorsement-Phase

Nachdem der Client den Transaktionsvorschlag eingereicht hat, überprüfen die Endorsement-Knoten zunächst die Unterschrift des Clients, simulieren die Ausführung unter Verwendung des lokalen Zustands, unterzeichnen die Transaktion und geben Read-Write Sets an Clients zurück. R-W Sets enthalten hauptsächlich drei Attribute: Schlüssel, Version und Wert. Das Read-Set enthält alle während der Transaktionsausführung gelesenen Variablen und ihre Version. Wenn es eine Schreiboperation am Ledger gibt, ändert sich die Version. Das Write-Set enthält alle bearbeiteten Variablen und ihre neuen Werte.

Bei der Ausführung von Transaktionen überprüfen Endorsement-Knoten nur, ob der Chaincode basierend auf dem lokalen Blockchain-Zustand korrekt ist, führen aus und geben zurück.

Fabric unterstützt mehrere Endorsement-Richtlinien. Der Client überprüft, ob die Endorsement-Anforderungen erfüllt sind, bevor er an die Ordering-Knoten übermittelt. Es ist erwähnenswert, dass der Client, wenn nur Ledger-Abfrageoperationen durchgeführt werden, nicht an OSN übermittelt.

Der oben erwähnte Transaktionsvorschlag enthält hauptsächlich Chaincode, Chaincode-Eingabewerte und Client-Unterschrift, während die von Endorsement-Knoten an den Client zurückgegebenen Informationen Rückgabewerte, R-W Set der simulierten Ausführungsergebnisse und Unterschriften der Endorsement-Knoten umfassen, die zusammen die bestätigten Knoten bilden.

Endorsement ist die Genehmigung von Transaktionen durch relevante Organisationen, d.h. relevante Knoten unterzeichnen die Transaktion. Für eine Chaincode-Transaktion wird die Endorsement-Richtlinie während der Chaincode-Instanziierung festgelegt. Eine wirksame Transaktion muss von Organisationen unterzeichnet werden, die mit der Endorsement-Richtlinie in Zusammenhang stehen, um wirksam zu werden. Im Wesentlichen basiert die Transaktionsverifizierung in der Fabric-Blockchain auf dem Vertrauen in Endorsement-Knoten, was einer der Gründe ist, warum Fabric nicht als streng dezentralisiert gilt.

Hier ist ein einfaches Beispiel für die Ausführung von Chaincode

```go
func (t *SimpleChaincode) InitLedger(ctx contractapi.TransactionContextInterface) error {
    var product = Product { Name: "Test Product", Description: "Just a test product to make sure chaincode is running", CreatedBy: "admin", ProductId: "1" }

    productAsBytes, err := json.Marshal(product)

    err = ctx.GetStub().PutState("1", productAsBytes)

    if err != nil {
        return err
    }
}
```

In diesem einfachen Beispiel besteht die Hauptoperation des Chaincodes darin, das Schlüssel-Wert-Paar zu aktualisieren. Nach dieser Operation wird sich die Version ändern.

Das nach der Ausführung zurückgegebene R-W Set ist

```go
key: 1
value: JSON-Form von Product { Name: "Test Product", Description: "Just a test product to make sure chaincode is running", CreatedBy: "admin", ProductId: "1" }
```

#### Ordering-Phase

Der Client reicht bestätigte Transaktionen bei Ordering-Knoten ein (Ordering-Knoten können durch einige Konsensstrategien OSN bilden). Nach Erhalt von Transaktionen verpacken Ordering-Knoten sie in Blöcke und ordnen sie gemäß den Regeln in der Konfiguration. Während dieses Prozesses führen sie nur Ordering-Operationen durch, ohne jegliche Ausführung oder Überprüfung. Nach Abschluss des Orderings senden sie an alle Knoten.

Der Ordering-Service wird verwendet, um einen Konsens über Transaktionen im gesamten Netzwerk zu erreichen und ist nur für das Erreichen eines Konsenses über die Transaktionsreihenfolge verantwortlich, vermeidet Netzwerkengpässe und erleichtert die horizontale Skalierung zur Verbesserung der Netzwerkeffizienz. Derzeit unterstützt es zwei Typen: Kafka und Raft. Die Einheit/Integrität des Fabric-Blockchain-Netzwerks hängt von der Konsistenz der Ordering-Knoten ab.

Der Raft-Konsensmechanismus gehört zum nicht-byzantinischen Konsensmechanismus und verwendet ein Leader-Follower-Modell. Wenn ein Leader gewählt wird, werden Loginformationen unidirektional vom Leader zu den Followern repliziert, was die Verwaltung erleichtert. Im Design erlaubt es allen Knoten, Orderer-Knoten zu werden, was es im Vergleich zu Kafka zentralisierter macht. Es erlaubt tatsächlich auch die Verwendung des PBFT-Konsensmechanismus, aber die Leistung ist oft sehr schlecht.

#### Validierungsphase

Wenn ein Knoten Blöcke erhält, die von Ordering-Knoten gesendet werden, validiert er alle Transaktionen im Block und markiert, ob sie vertrauenswürdig sind. Er überprüft hauptsächlich zwei Aspekte: 1. Ob es die Endorsement-Richtlinie erfüllt. 2. Die Rechtmäßigkeit der Transaktionsstruktur, ob es Zustandskonflikte gibt, wie z.B. ob die Version im Read-Set konsistent ist, usw.

## Fazit

Das Obige ist eine Überprüfung der Hyperledger Fabric-Architektur. Obwohl es einige der Dezentralisierungskonzepte geopfert hat, ermutigt es als Open-Source-Konsortium-Blockchain für Unternehmensanwendungen mehr Unternehmen zur Teilnahme am Aufbau und der Anwendung von Distributed-Ledger-Technologie. Jetzt gibt es in China viele selbst entwickelte Konsortium-Blockchain-Plattformen wie Ant Chain, Qulian usw. Ich glaube, dass in Zukunft mehr Unternehmen an diesem offenen Ökosystem teilnehmen werden!

## Referenzen

> 1. [FITE3011 Distributed Ledger and Blockchain](https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2019/fite3011.html), *Allen Au, HKU*
> 2. [Enterprise Blockchain Practical Tutorial](https://github.com/yingpingzhang/enterprise_blockchain_tutorial), *Zhang Yingping*