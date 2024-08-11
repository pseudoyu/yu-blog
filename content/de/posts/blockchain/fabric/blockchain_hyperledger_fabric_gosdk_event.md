---
title: "Analyse der Hyperledger Fabric Go SDK Events"
date: 2021-09-01T17:21:58+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "go", "gosdk"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Vorwort

Kürzlich musste ich im Rahmen der Arbeit an einem Cross-Chain-Adapter das Go SDK verwenden, um eine Verbindung zu einem Fabric-Netzwerk auf einer lokalen Chain herzustellen und Events zu überwachen. Daher habe ich mich entschieden, die von Fabric unterstützten Events und die vom SDK bereitgestellten Überwachungsmethoden zusammenzufassen.

## Fabric Events

![hyperledger_fabric_application_interact](https://image.pseudoyu.com/images/hyperledger_fabric_application_interact.png)

Events sind eine Möglichkeit für Clients, mit dem Fabric-Netzwerk zu interagieren. Wie in der obigen Abbildung dargestellt, kann der Client nach der Ausführung einer Transaktion im Fabric-Netzwerk aufgrund der asynchronen Verarbeitung den Status der eingereichten Transaktion (ob sie akzeptiert wurde) nicht unmittelbar erfahren. Daher stellen die Peer-Knoten von Fabric einen Event-Mechanismus bereit, der es Clients ermöglicht, über die gRPC-Schnittstelle Block-Events zu überwachen. Seit Fabric v1.1 erfolgt die Event-Registrierung auf Kanalebene und nicht mehr auf Peer-Knotenebene, was eine feinere Kontrolle ermöglicht.

### Event-Typen

Events werden hauptsächlich vom Ledger und den Containern ausgelöst, die Chaincode-Verträge enthalten. Fabric unterstützt vier Arten von Events:

1. BlockEvent: Wird verwendet, um neue Blöcke zu überwachen, die zu Fabric hinzugefügt werden
2. ChaincodeEvent: Wird verwendet, um Events zu überwachen, die im Chaincode veröffentlicht werden, d.h. benutzerdefinierte Events
3. TxStatusEvent: Wird verwendet, um den Abschluss von Transaktionen auf Knoten zu überwachen
4. FilteredBlockEvent: Wird verwendet, um zusammengefasste Blockinformationen zu überwachen

Im Fabric Go SDK werden diese Events durch die folgenden Event-Listener behandelt:

1. `func (c *Client) RegisterBlockEvent(filter ...fab.BlockFilter) (fab.Registration, <-chan *fab.BlockEvent, error)`
2. `func (c *Client) RegisterChaincodeEvent(ccID, eventFilter string) (fab.Registration, <-chan *fab.CCEvent, error)`
3. `func (c *Client) RegisterFilteredBlockEvent() (fab.Registration, <-chan *fab.FilteredBlockEvent, error)`
4. `func (c *Client) RegisterTxStatusEvent(txID string) (fab.Registration, <-chan *fab.TxStatusEvent, error)`

Nach Abschluss der Überwachung sollte `func (c *Client) Unregister(reg fab.Registration)` verwendet werden, um die Registrierung aufzuheben und den Event-Kanal zu entfernen.

### gRPC-Kommunikation

Das SDK kommuniziert über gRPC mit den Peer-Knoten. Der Quellcode ist unter [fabric-protos/peer/events.proto](https://github.com/hyperledger/fabric-protos/blob/main/peer/events.proto) zu finden.

Es definiert die folgenden Nachrichten:

1. FilteredBlock, verwendet für FilteredBlockEvent
2. FilteredTransaction und FilteredTransaction, verwendet für FilteredTransactionEvent
3. FilteredChaincodeAction, verwendet für ChaincodeEvent
4. BlockAndPrivateData, verwendet für private Daten

Die Antwort sieht wie folgt aus:

```go
// DeliverResponse
message DeliverResponse {
    oneof Type {
        common.Status status = 1;
        common.Block block = 2;
        FilteredBlock filtered_block = 3;
        BlockAndPrivateData block_and_private_data = 4;
    }
}
```

Und drei gRPC-Kommunikationsschnittstellen:

```go
service Deliver {
    // Deliver erfordert zunächst einen Envelope vom Typ ab.DELIVER_SEEK_INFO mit
    // Payload-Daten als serialisierte orderer.SeekInfo-Nachricht,
    // dann wird ein Stream von Block-Antworten empfangen
    rpc Deliver (stream common.Envelope) returns (stream DeliverResponse) {
    }
    // DeliverFiltered erfordert zunächst einen Envelope vom Typ ab.DELIVER_SEEK_INFO mit
    // Payload-Daten als serialisierte orderer.SeekInfo-Nachricht,
    // dann wird ein Stream von **gefilterten** Block-Antworten empfangen
    rpc DeliverFiltered (stream common.Envelope) returns (stream DeliverResponse) {
    }
    // DeliverWithPrivateData erfordert zunächst einen Envelope vom Typ ab.DELIVER_SEEK_INFO mit
    // Payload-Daten als serialisierte orderer.SeekInfo-Nachricht,
    // dann wird ein Stream von Block- und Private-Data-Antworten empfangen
    rpc DeliverWithPrivateData (stream common.Envelope) returns (stream DeliverResponse) {
    }
}
```

![fabric_events](https://image.pseudoyu.com/images/fabric_events.png)

Der gesamte Prozess ist in der obigen Abbildung dargestellt. Im Go SDK wird ein Dispatcher implementiert, um Event-Registrierungsanfragen von der Anwendung in Event-Abonnementanfragen umzuwandeln und sie über den DeliverClient an den Peer-Knoten zu senden. Der DeliverServer im Peer-Knoten empfängt die Abonnementanfrage, ruft deliverBlocks auf, um in eine Schleife einzutreten, liest Blöcke aus dem Ledger, generiert Events und sendet sie schließlich an den Client. Der Dispatcher im Client wandelt diese dann in Event-Antworten um, die von der Anwendung abonniert wurden.

### Event-Implementierungsprozess

Der Event-Implementierungsprozess erfordert zwei Schritte:

1. Aufruf der `SetEvent`-Methode im Chaincode
2. Implementierung eines Event-Listeners im Client unter Verwendung des Go SDK

#### SetEvent-Methode

Methodendefinition:

```go
func (s *ChaincodeStub) SetEvent(name string, payload []byte) error
```

Verwendungsbeispiel:

```go
func (s *SmartContract) Invoke(stub shim.ChaincodeStubInterface) sc.Response {

    err = stub.PutState(key, value)

    if err != nil {
        return shim.Error(fmt.Sprintf("unable put state (%s), error: %v", key, err))
    }

    // Payload muss in Byte-Format konvertiert werden
    eventPayload := "Event-Informationen"
    payloadAsBytes := []byte(eventPayload)

    // SetEvent-Methode wird typischerweise nach Operationen platziert, die mit dem Ledger interagieren, wie PutState, DelState
    err = stub.SetEvent("<event name>", payloadAsBytes)

    if (eventErr != nil) {
        return shim.Error(fmt.Sprintf("Fehler beim Auslösen des Events"))
    }

    return shim.Success(nil)
}
```

#### Client Event-Listener

```go
// Implementierung eines Chaincode-Event-Listeners
// Übergeben Sie die entsprechenden Parameter. Die eventId hier muss mit dem <event name> im Chaincode übereinstimmen, um das Listening zu erreichen
reg, eventChannel, err := eventClient.RegisterChaincodeEvent(chaincodeID, eventID)

if err != nil {
    log.Fatalf("Fehler bei der Registrierung des Block-Events: %v\n", err)
    return
}

// Aufheben der Registrierung und Entfernen des Event-Kanals
defer eventClient.Unregister(reg)
```

## Fazit

Dies ist eine grundlegende Einführung in die Überwachung von Events im Fabric-Netzwerk unter Verwendung des Go SDK. Ich überprüfe derzeit den Quellcode des Fabric Go SDK und werde dies in Zukunft mit einigen Interpretationen ergänzen.

## Referenzen

> 1. [hyperledger/fabric-sdk-go](https://github.com/hyperledger/fabric-sdk-go)
> 2. [Hyperledger Fabric Packages for Go Chaincode](https://pkg.go.dev/github.com/hyperledger/fabric-chaincode-go)
> 3. [Channel-based Peer Node Event Services](https://hyperledger-fabric.readthedocs.io/zh_CN/latest/peer_event_services.html)
> 4. [fabric-protos/peer/events.proto](https://github.com/hyperledger/fabric-protos/blob/main/peer/event)
> 5. [Fabric 1.4 Source Code Interpretation 3: Event Principle Explanation](https://lessisbetter.site/2019/09/20/fabric-event-source/)
> 6. [Events Supported by Fabric](https://www.jianshu.com/p/aecaae8aa3da)
> 7. [How to Listen to Fabric Chaincode Events](http://blog.hubwiz.com/2019/07/07/Hyperledger-fabric-chaincode-event/)