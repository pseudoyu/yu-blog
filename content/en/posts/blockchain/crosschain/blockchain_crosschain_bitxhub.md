---
title: "BitXHub Cross-chain Plugin (Fabric) Source Code Analysis"
date: 2021-09-09T15:14:26+08:00
draft: false
tags: ["blockchain", "crosschain", "bitxhub", "hyperledger fabric", "go"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

I previously mentioned that BitXHub cross-chain platform by QulianTech is a relatively comprehensive open-source cross-chain solution in the industry. It mainly optimizes the functionality, security, and flexibility of the cross-chain process through relay chain, gateway, and plugin mechanisms.

Currently, our company's team is working on a cross-chain module for a BaaS platform. I am responsible for the cross-chain adapter part, which corresponds to the listening module and application chain plugin module in the BitXHub platform. The adapter will listen to cross-chain events on the application chain and pass the corresponding parameters to the gateway for cross-chain related business logic requirements.

Therefore, I plan to conduct an in-depth analysis of the source code of BitXHub's [meshplus/pier-client-fabric](https://github.com/meshplus/pier-client-fabric) plugin to learn its excellent code structure and functional modules, in order to better implement my own adapter functionality.

## Cross-chain Transaction Process

![cross_chain_plugin](https://image.pseudoyu.com/images/cross_chain_plugin.png)

According to cross-chain business requirements, a typical cross-chain invocation process is shown in the above diagram.

1. The subchain that needs to perform cross-chain transactions must install the adapter and deploy the provided cross-chain contract and business contract
2. When a user invokes the business contract through the SDK, the contract will call the cross-chain contract and throw a cross-chain event
3. The corresponding adapter of the subchain will poll or subscribe to the cross-chain events thrown by the cross-chain contract and send them to the listening module of the cross-chain gateway
4. The cross-chain gateway will convert the response method and parameters extracted from the cross-chain event into a transaction recognizable by the target subchain
5. The cross-chain gateway will submit the converted transaction to the target subchain and execute it

## Adapter Mechanism

### Interface Design

The adapter is mainly responsible for interaction between subchains and participates in cross-chain interactions through interface calls. It mainly provides the following interfaces.

#### Invoke Chaincode

The adapter receives transaction parameters sent by the cross-chain gateway, encapsulates them into a data structure accepted by the adapted subchain, and invokes the chaincode.

#### Query Cross-chain Transaction

The subchain stores cross-chain related details in the payload field, such as contract, user, etc. The adapter parses and encapsulates this information and provides corresponding interfaces for the cross-chain gateway to query.

#### Query Historical Transaction Information

The adapter needs to provide a historical transaction query interface to actively query when cross-chain events are not received due to network transmission or other reasons.

#### Query Application Chain Basic Information

The adapter needs to provide a query interface for information related to its adapted subchain for the cross-chain gateway to query, such as name, type, etc.

## Source Code Analysis

Next, we will analyze the core functional module source code of the BitXHub cross-chain plugin (Fabric).

### Design Pattern

The plugin project adopts a typical "producer-consumer" model, which is very suitable for concurrent scenarios that need to poll/subscribe to receive data. This model utilizes the characteristic that only one goroutine accesses a certain data in the channel at any moment.

#### Subscribe/Poll Cross-chain Events

The plugin needs to construct a producer object to subscribe to cross-chain events of its corresponding subchain.

```go
// Construct producer
ec, err := event.New(c.channelProvider, event.WithBlockEvents())
if err != nil {
    return fmt.Errorf("failed to create fabcli, error: %v", err)
}

c.eventClient = ec

// Subscribe to cross-chain events
registration, notifier, err := ec.RegisterChaincodeEvent(c.meta.CCID, c.meta.EventFilter)
if err != nil {
    return fmt.Errorf("failed to register chaincode event, error: %v", err)
}
c.registration = registration
```

The method to subscribe to events is to call the `RegisterChaincodeEvent()` method of `fabric-sdk-go`. It's important to note that when you no longer need to listen to events, you should call the `Unregister()` method to cancel the subscription.

The `ccID` in the method is the chaincode ID to be monitored, `eventFilter` is the chaincode event to be monitored, and this method will return a channel to receive data (when the subscription is canceled, the channel will be closed).

```go
func (c *Client) RegisterChaincodeEvent(ccID, eventFilter string) (fab.Registration, <-chan *fab.CCEvent, error) {
	return c.eventService.RegisterChaincodeEvent(ccID, eventFilter)
}
```

Place both the object that has subscribed to the cross-chain contract (i.e., the producer) and the consumer in an infinite loop. When a cross-chain event is thrown, the producer will continuously put data into the channel, and the consumer will continuously take data out of the channel.

```go
go func() {
    for {
        select {
        // Producer writes cross-chain events to the channel
        case ccEvent := <-notifier:
            if ccEvent != nil {
                c.handle(ccEvent)
            }
        // Consumer takes cross-chain event data from the channel
        case <-c.ctx:
            return
        }
    }
}()
```

Because both the producer and consumer are in an infinite loop, the producer's goroutine will not exit, and the channel continues to write data. When there are no new events, the consumer will block, waiting for the producer to receive new data and write it to the channel.

### Plugin Initialization, Running, and Closure

After looking at the overall design pattern, let's look at the mechanism of how the entire plugin project runs from the main entry point of the program.

#### Initialization

In the initialization of the client program, a consumer object is first constructed according to a custom structure.

```go
// Construct consumer
mgh, err := newFabricHandler(contractmeta.EventFilter, eventC, appchainID)
if err != nil {
    return err
}

done := make(chan bool)
csm, err := NewConsumer(configPath, contractmeta, mgh, done)
if err != nil {
    return err
}
```

#### Running

The entry point for program execution is simple, just polling the cross-chain contract and starting the consumer object.

```go
func (c *Client) Start() error {
	logger.Info("Fabric consumer started")
	go c.polling()
	return c.consumer.Start()
}
```

#### Closure

Closing the plugin is also simple, just stop the program from running and unsubscribe from events.

```go
// Close plugin
func (c *Client) Stop() error {
	c.ticker.Stop()
	c.done <- true
	return c.consumer.Shutdown()
}
```

Unsubscribe from events in the consumer package.

```go
func (c *Consumer) Shutdown() error {
	c.eventClient.Unregister(c.registration)
	return nil
}
```

Looking deeper, unsubscribing from events calls the `Unregister()` method of `fabric-sdk-go`, which will cancel the subscription to that event and close the corresponding channel.

```go
func (c *Client) Unregister(reg fab.Registration) {
	c.eventService.Unregister(reg)
}
```

### Interface Implementation

In addition to subscribing to and monitoring events, the plugin also provides a series of query interfaces for the gateway to call to complete corresponding cross-chain operations.

#### getProof()

Such as obtaining Proof information, etc.

```go
func (c *Client) getProof(response channel.Response) ([]byte, error) {
	var proof []byte
	var handle = func(response channel.Response) ([]byte, error) {
		// query proof from fabric
		l, err := ledger.New(c.consumer.channelProvider)
		if err != nil {
			return nil, err
		}

		t, err := l.QueryTransaction(response.TransactionID)
		if err != nil {
			return nil, err
		}
		pd := &common.Payload{}
		if err := proto.Unmarshal(t.TransactionEnvelope.Payload, pd); err != nil {
			return nil, err
		}

		pt := &peer.Transaction{}
		if err := proto.Unmarshal(pd.Data, pt); err != nil {
			return nil, err
		}

		return pt.Actions[0].Payload, nil
	}

	if err := retry.Retry(func(attempt uint) error {
		var err error
		proof, err = handle(response)
		if err != nil {
			logger.Error("Can't get proof", "error", err.Error())
			return err
		}
		return nil
	}, strategy.Wait(2*time.Second)); err != nil {
		logger.Error("Can't get proof", "error", err.Error())
	}

	return proof, nil
}
```

#### getChainID()

This interface is used to get the chain ID

```go
func (c *Client) GetChainID() (string, string) {
	request := channel.Request{
		ChaincodeID: c.meta.CCID,
		Fcn:         GetChainId,
	}

	response, err := c.consumer.ChannelClient.Execute(request)
	if err != nil || response.Payload == nil {
		return "", ""
	}
	chainIds := strings.Split(string(response.Payload), "-")
	if len(chainIds) != 2 {
		return "", ""
	}
	return chainIds[0], chainIds[1]
}
```

#### Other Interfaces

For more interface implementation details, please refer to [meshplus/pier-client-fabric/client.go](https://github.com/meshplus/pier-client-fabric/blob/master/client.go).

### Cross-chain Contract

The cross-chain contract is an important part of implementing plugin monitoring. When business needs to cross chains, it will uniformly call the cross-chain contract and interact with the cross-chain gateway.

The cross-chain contract provides a series of interfaces for business contracts to implement. Therefore, writing business contracts according to certain specifications can simplify the development and maintenance of cross-chain business. For details on writing cross-chain contracts, please refer to <[Cross-chain Contract Writing Documentation](https://github.com/meshplus/bitxhub/wiki/跨链合约编写文档)>.

#### Event Implementation

How does the cross-chain contract throw cross-chain events to the plugin?

In the `Invoke()` method of the cross-chain contract, the cross-chain contract first obtains the calling method and corresponding parameters of the contract caller (i.e., the business contract) through the `GetFunctionAndParameters()` method, and then calls different contracts by judging the method name.

```go
func (broker *Broker) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
	function, args := stub.GetFunctionAndParameters()
    // ...
    	switch function {
            // ...
            case "getChainId":
                return broker.getChainId(stub)
            case "getInMessage":
                return broker.getInMessage(stub, args)
            case "getOutMessage":
                return broker.getOutMessage(stub, args)
            // ...
            case "EmitInterchainEvent":
                return broker.EmitInterchainEvent(stub, args)
            default:
                return shim.Error("invalid function: " + function + ", args: " + strings.Join(args, ","))
	}
}
```

Let's focus on analyzing what the cross-chain contract does when `EmitInterchainEvent()` is called. The corresponding explanations are in the comments.

```go
func (broker *Broker) EmitInterchainEvent(stub shim.ChaincodeStubInterface, args []string) pb.Response {
    // Judge whether the number of input parameters is correct
    // Cross-chain contracts need to pass in many parameters, as call failures can easily cause security issues on the chain
	if len(args) != 5 {
		return shim.Error("incorrect number of arguments, expecting 7")
	}

	// Read parameters and store in corresponding variables

	// Target chain ID
	dstServiceID := args[0]

	// Own chaincode ID
	cid, err := getChaincodeID(stub)
	if err != nil {
		return shim.Error(err.Error())
	}

	// Get bxhID and appchainID
	curFullID, err := broker.genFullServiceID(stub, cid)
	if err != nil {
		return shim.Error(err.Error())
	}

	// Combine current chain ID and target chain ID into output cross-chain service group
	outServicePair := genServicePair(curFullID, dstServiceID)

	// Get key-value pairs of output values
	outMeta, err := broker.getMap(stub, outterMeta)
	if err != nil {
		return shim.Error(err.Error())
	}

	// Check if the output cross-chain service group is in the key-value pair, if not, set to 0
	if _, ok := outMeta[outServicePair]; !ok {
		outMeta[outServicePair] = 0
	}

	// Encapsulate transaction information
	tx := &Event{
		Index:     outMeta[outServicePair] + 1,
		DstFullID: dstServiceID,
		SrcFullID: curFullID,
		Func:      args[1],
		Args:      args[2],
		Argscb:    args[3],
		Argsrb:    args[4],
	}

	// Output service self-increment
	outMeta[outServicePair]++

	// Convert transaction information to json format
	txValue, err := json.Marshal(tx)
	if err != nil {
		return shim.Error(err.Error())
	}

	// Format output event message
	key := broker.outMsgKey(outServicePair, strconv.FormatUint(tx.Index, 10))

	// Write message and transaction information to the ledger (persistence)
	if err := stub.PutState(key, txValue); err != nil {
		return shim.Error(fmt.Errorf("persist event: %w", err).Error())
	}

	// Set the corresponding cross-chain transaction event name and store the transaction information in the payload
	if err := stub.SetEvent(interchainEventName, txValue); err != nil {
		return shim.Error(fmt.Errorf("set event: %w", err).Error())
	}

	// Write metadata status to the ledger
	if err := broker.putMap(stub, outterMeta, outMeta); err != nil {
		return shim.Error(err.Error())
	}

	return shim.Success(nil)
}
```

This is what happens when calling the cross-chain contract. Essentially, it just sets an event trigger through `SetEvent()` in the cross-chain contract, and then subscribes and monitors it in the plugin through `RegisterChaincodeEvent()`.

```go
SetEvent(name string, payload []byte) error
```

`SetEvent()` is an interface under the `shim` package, mainly passing in name and payload array. For details on chaincode event monitoring principles and details, please refer to <[Hyperledger Fabric Go SDK Event Analysis](https://www.pseudoyu.com/en/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)>.

### Business Contract

After analyzing the cross-chain contract, let's see how the business contract calls the cross-chain contract, taking the data exchange contract `data_swapper.go` in the example as an instance.

```go
func (s *DataSwapper) get(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	switch len(args) {
	case 1:
		// args[0]: key
		value, err := stub.GetState(args[0])
		if err != nil {
			return shim.Error(err.Error())
		}

		return shim.Success(value)
	case 2:
		// args[0]: destination service id
		// args[1]: key
		b := util.ToChaincodeArgs(emitInterchainEventFunc, args[0], "interchainGet,interchainSet,", args[1], args[1], "")
		response := stub.InvokeChaincode(brokerContractName, b, channelID)
		if response.Status != shim.OK {
			return shim.Error(fmt.Errorf("invoke broker chaincode %s error: %s", brokerContractName, response.Message).Error())
		}

		return shim.Success(nil)
	default:
		return shim.Error("incorrect number of arguments")
	}
}
```

To get information from other chains in the `data_swapper.go` business contract, it first judges the length of the input parameter array `args []string` through `switch...case...` when calling the `get` method. When the length is 1, it normally calls its own contract for query, and when the length is 2, it first uses the `ToChaincodeArgs()` method provided by Fabric to convert the parameters from `string` to chaincode parameter array format.

```go
func ToChaincodeArgs(args ...string) [][]byte {
	bargs := make([][]byte, len(args))
	for i, arg := range args {
		bargs[i] = []byte(arg)
	}
	return bargs
}
```

Then, it directly calls the cross-chain contract through the `InvokeChaincode()` method in the business chaincode, and passes in parameters and channel ID, thus completing a cross-chain data query chaincode call.

## Conclusion

The above is an analysis of the cross-chain transaction process and BitXHub cross-chain plugin (Fabric) source code. I hope that through this process, I can deepen my understanding of cross-chain mechanisms and related platforms, and be able to better participate in its open-source construction in the future.

## References

> 1. [Cross-chain Technology Platform BitXHub](https://github.com/gocn/opentalk/tree/main/PhaseTen_BitXHub)
> 2. [BitXHub Document](https://meshplus.github.io/bitxhub/bitxhub/introduction/summary/)
> 3. [meshplus/pier-client-fabric](https://github.com/meshplus/pier-client-fabric)
> 4. [Ten Questions about BitXHub: Discussing the Architecture Design of Cross-chain Platforms](https://tech.hyperchain.cn/bitxhub-design-thinking/)
> 5. [Cross-chain Contract Writing Documentation](https://github.com/meshplus/bitxhub/wiki/跨链合约编写文档)
> 6. [Hyperledger Fabric Go SDK Event Analysis](https://www.pseudoyu.com/en/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)