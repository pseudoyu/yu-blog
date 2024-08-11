---
title: "Hyperledger Fabric Go SDK Event Analysis"
date: 2021-09-01T17:21:58+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "go", "gosdk"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Recently, while working on a cross-chain adapter, I needed to use the Go SDK to connect to a Fabric network on a local chain and listen for events. Therefore, I've decided to summarize the events supported by Fabric and the listening methods provided by the SDK.

## Fabric Events

![hyperledger_fabric_application_interact](https://image.pseudoyu.com/images/hyperledger_fabric_application_interact.png)

Events are a way for clients to interact with the Fabric network. As shown in the image above, after executing a transaction in the Fabric network, because it is done asynchronously, the client cannot obtain the submitted transaction status (whether it was accepted). Therefore, Fabric's Peer nodes provide an event mechanism, allowing clients to listen to block events through the gRPC interface. Since Fabric v1.1, event registration occurs at the channel level rather than the Peer node, allowing for more fine-grained control.

### Event Types

Events are primarily triggered by the Ledger and containers holding chaincode contracts. Fabric supports four types of events:

1. BlockEvent: Used to monitor new blocks added to Fabric
2. ChaincodeEvent: Used to monitor events published in chaincode, i.e., user-defined events
3. TxStatusEvent: Used to monitor transaction completion on nodes
4. FilteredBlockEvent: Used to monitor summarized block information

In the Fabric Go SDK, these events are handled through the following event listeners:

1. `func (c *Client) RegisterBlockEvent(filter ...fab.BlockFilter) (fab.Registration, <-chan *fab.BlockEvent, error)`
2. `func (c *Client) RegisterChaincodeEvent(ccID, eventFilter string) (fab.Registration, <-chan *fab.CCEvent, error)`
3. `func (c *Client) RegisterFilteredBlockEvent() (fab.Registration, <-chan *fab.FilteredBlockEvent, error)`
4. `func (c *Client) RegisterTxStatusEvent(txID string) (fab.Registration, <-chan *fab.TxStatusEvent, error)`

After listening is complete, `func (c *Client) Unregister(reg fab.Registration)` should be used to unregister and remove the event channel.

### gRPC Communication

The SDK communicates with Peer nodes via gRPC. The source code can be found at [fabric-protos/peer/events.proto](https://github.com/hyperledger/fabric-protos/blob/main/peer/events.proto)

It defines the following messages:

1. FilteredBlock, used for FilteredBlockEvent
2. FilteredTransaction and FilteredTransaction, used for FilteredTransactionEvent
3. FilteredChaincodeAction, used for ChaincodeEvent
4. BlockAndPrivateData, used for private data

The Response is as follows:

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

And three gRPC communication interfaces:

```go
service Deliver {
    // Deliver first requires an Envelope of type ab.DELIVER_SEEK_INFO with
    // Payload data as a marshaled orderer.SeekInfo message,
    // then a stream of block replies is received
    rpc Deliver (stream common.Envelope) returns (stream DeliverResponse) {
    }
    // DeliverFiltered first requires an Envelope of type ab.DELIVER_SEEK_INFO with
    // Payload data as a marshaled orderer.SeekInfo message,
    // then a stream of **filtered** block replies is received
    rpc DeliverFiltered (stream common.Envelope) returns (stream DeliverResponse) {
    }
    // DeliverWithPrivateData first requires an Envelope of type ab.DELIVER_SEEK_INFO with
    // Payload data as a marshaled orderer.SeekInfo message,
    // then a stream of block and private data replies is received
    rpc DeliverWithPrivateData (stream common.Envelope) returns (stream DeliverResponse) {
    }
}
```

![fabric_events](https://image.pseudoyu.com/images/fabric_events.png)

The entire process is shown in the image above. In the Go SDK, a Dispatcher is implemented to convert event registration requests from the application into event subscription requests and send them to the Peer node via DeliverClient. The DeliverServer in the Peer node receives the subscription request, calls deliverBlocks to enter a loop, reads blocks from the Ledger, generates events, and finally sends them to the client. The Dispatcher in the client then converts these into event responses subscribed by the application.

### Event Implementation Process

The event implementation process requires two steps:

1. Call the `SetEvent` method in the chaincode
2. Implement an event listener in the client using the Go SDK

#### SetEvent Method

Method definition:

```go
func (s *ChaincodeStub) SetEvent(name string, payload []byte) error
```

Usage example:

```go
func (s *SmartContract) Invoke(stub shim.ChaincodeStubInterface) sc.Response {

    err = stub.PutState(key, value)

    if err != nil {
        return shim.Error(fmt.Sprintf("unable put state (%s), error: %v", key, err))
    }

    // Payload needs to be converted to byte format
    eventPayload := "Event Information"
    payloadAsBytes := []byte(eventPayload)

    // SetEvent method is typically placed after operations interacting with the ledger, such as PutState, DelState
    err = stub.SetEvent("<event name>", payloadAsBytes)

    if (eventErr != nil) {
        return shim.Error(fmt.Sprintf("Failed to trigger event"))
    }

    return shim.Success(nil)
}
```

#### Client Event Listener

```go
// Implement a chaincode event listener
// Pass in the corresponding parameters. The eventId here must match the <event name> in the chaincode to achieve listening
reg, eventChannel, err := eventClient.RegisterChaincodeEvent(chaincodeID, eventID)

if err != nil {
    log.Fatalf("Failed to register block event: %v\n", err)
    return
}

// Unregister and remove the event channel
defer eventClient.Unregister(reg)
```

## Conclusion

The above is a basic introduction to monitoring events on the Fabric network using the Go SDK. I am currently reviewing the Fabric Go SDK source code and will supplement this with some interpretations in the future.

## References

> 1. [hyperledger/fabric-sdk-go](https://github.com/hyperledger/fabric-sdk-go)
> 2. [Hyperledger Fabric Packages for Go Chaincode](https://pkg.go.dev/github.com/hyperledger/fabric-chaincode-go)
> 3. [Channel-based Peer Node Event Services](https://hyperledger-fabric.readthedocs.io/zh_CN/latest/peer_event_services.html)
> 4. [fabric-protos/peer/events.proto](https://github.com/hyperledger/fabric-protos/blob/main/peer/event)
> 5. [Fabric 1.4 Source Code Interpretation 3: Event Principle Explanation](https://lessisbetter.site/2019/09/20/fabric-event-source/)
> 6. [Events Supported by Fabric](https://www.jianshu.com/p/aecaae8aa3da)
> 7. [How to Listen to Fabric Chaincode Events](http://blog.hubwiz.com/2019/07/07/Hyperledger-fabric-chaincode-event/)