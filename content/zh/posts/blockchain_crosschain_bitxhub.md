---
title: "BitXHub 跨链插件（Fabric）源码解读"
date: 2021-09-09T15:14:26+08:00
draft: false
tags: ["blockchain", "cross chain", "bitxhub", "hyperledger fabric", "go"]
categories: ["Develop"]
authors:
- "Arthur"
---

## 前言

之前提到过趣链科技的 BitXHub 跨链平台是业界较为完善的跨链开源解决方案，主要通过中继链、网关和插件机制对跨链流程中的功能、安全性和灵活性等进行了优化。

目前公司团队在做一个 BaaS 平台的跨链模块，我在其中负责跨链适配器部分，对应 BitXHub 平台就是监听模块和应用链插件模块。适配器将对应用链上的跨链事件作监听，并将相应参数传给网关作跨链相关的业务逻辑需求。

因此，打算对 BitXHub 的 [meshplus/pier-client-fabric](https://github.com/meshplus/pier-client-fabric) 插件源码作深入解读，学习其优秀的代码结构和功能模块，以便更好地实现自己的适配器功能。

## 跨链交易流程

![cross_chain_plugin](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/cross_chain_plugin.svg)

根据跨链业务需求，典型的跨链调用流程如上图所示。

1. 需要进行跨链交易的子链需要安装适配器并部署提供的跨链合约和业务合约
2. 用户通过 SDK 调用业务合约时，合约将调用跨链合约并抛出跨链事件
3. 子链相应适配器将会轮询或订阅跨链合约抛出的跨链事件并发送到跨链网关的监听模块
4. 跨链网关将从跨链事件中提取的响应方法和参数转换为目标子链可识别的交易
5. 跨链网关将转换后的交易提交到目标子链并执行

## 适配器机制

### 接口设计

适配器主要负责与子链之间的交互，并以接口调用的方式参与跨链交互。主要提供以下接口。

#### 调用链码

适配器接收跨链网关发送的交易参数，封装为已适配子链接受的数据结构并调用链码。

#### 查询跨链交易

子链将跨链相关细节存在 payload 字段中，如合约、用户等，适配器对这些信息进行解析与封装，提供相应接口给跨链网关查询。

#### 查询历史交易信息

适配器需要提供历史交易查询接口，以便于当跨链事件因网络传输等原因未收到时主动进行查询。

#### 查询应用链基本信息

适配器需要提供其所适配子链相关信息的查询接口以便于跨链网关进行查询，如名称、类型等。

## 源码解读

接下来将对 BitXHub 跨链插件（Fabric）的核心功能模块源码进行解读。

### 设计模式

插件项目采用的是典型的“生产者-消费者”模型，很适合这样需要轮询/订阅接收数据的并发场景。这种模型用到了任意时刻只有一个 goroutine 对 channel 中的某一个数据进行访问的特性。

#### 订阅/轮询跨链事件

插件需要构建一个生产者对象来订阅自己相应子链的跨链事件。

```go
// 构造生产者
ec, err := event.New(c.channelProvider, event.WithBlockEvents())
if err != nil {
    return fmt.Errorf("failed to create fabcli, error: %v", err)
}

c.eventClient = ec

// 订阅跨链事件
registration, notifier, err := ec.RegisterChaincodeEvent(c.meta.CCID, c.meta.EventFilter)
if err != nil {
    return fmt.Errorf("failed to register chaincode event, error: %v", err)
}
c.registration = registration
```

订阅事件的方法是调用了 `fabric-sdk-go` 的 `RegisterChaincodeEvent()` 方法，需要注意的是，当不需要监听事件时，需要调用 `Unregister()` 方法来取消订阅。

方法中的 `ccID` 是需要监听的链码 ID，`eventFilter` 是需要监听的链码时间，而这个方法会返回一个 channel 接收数据（当取消订阅时，channel 会关闭）。

```go
func (c *Client) RegisterChaincodeEvent(ccID, eventFilter string) (fab.Registration, <-chan *fab.CCEvent, error) {
	return c.eventService.RegisterChaincodeEvent(ccID, eventFilter)
}
```

将订阅了跨链合约的对象（即生产者）与消费者都置于无限循环中，当有跨链事件抛出时，生产者将会不断地向 channel 中放入数据，而消费者也不断从通道中取出数据。

```go
go func() {
    for {
        select {
        // 生产者将跨链事件写入通道
        case ccEvent := <-notifier:
            if ccEvent != nil {
                c.handle(ccEvent)
            }
        // 消费者从通道中取出跨链事件数据
        case <-c.ctx:
            return
        }
    }
}()
```

因为生产者和消费者都在无限循环中，生产者的 goroutine 不会退出，channel 持续写入数据，而当没有新事件时，消费者将会阻塞，等待生产者接收新的数据并写入 channel。

### 插件初始化、运行与关闭

看了整体的设计模式，我们从程序的主入口看看整个插件项目运行的机制。

#### 初始化

在 client 程序初始化中，首先根据自定义的结构构造了消费者对象。

```go
// 构造消费者
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

#### 运行

程序运行的入口很简单，就是对跨链合约进行轮询，并启动消费者对象。

```go
func (c *Client) Start() error {
	logger.Info("Fabric consumer started")
	go c.polling()
	return c.consumer.Start()
}
```

#### 关闭

关闭插件也很简单，即停止程序运行并取消订阅事件。

```go
// 关闭插件
func (c *Client) Stop() error {
	c.ticker.Stop()
	c.done <- true
	return c.consumer.Shutdown()
}
```

在 consumer 包中取消订阅事件。

```go
func (c *Consumer) Shutdown() error {
	c.eventClient.Unregister(c.registration)
	return nil
}
```

再深一层看，取消订阅事件是调用了 `fabric-sdk-go` 的 `Unregister()` 方法，会取消该事件的订阅并关闭相应通道。

```go
func (c *Client) Unregister(reg fab.Registration) {
	c.eventService.Unregister(reg)
}
```


### 接口实现

除了对事件进行订阅监听外，插件还提供了一系列查询接口供网关调用，以完成相应跨链操作。

#### getProof()

如获取 Proof 信息等

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

该接口用于获取链的 ID

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

#### 其他接口

其他更多接口实现细节详见 [meshplus/pier-client-fabric/client.go](https://github.com/meshplus/pier-client-fabric/blob/master/client.go)。

### 跨链合约

跨链合约是实现插件监听的重要部分，当业务需要跨链时，将会统一调用跨链合约，并与跨链网关进行交互。

跨链合约提供了一系列接口供业务合约进行实现，因此按照一定的规范撰写业务合约则能简化跨链业务的开发和维护，跨链合约编写的规范详见<[跨链合约编写文档](https://github.com/meshplus/bitxhub/wiki/跨链合约编写文档)>。

#### 事件实现

跨链合约是怎样将跨链事件抛出给插件的呢？

在跨链合约的 `Invoke()` 方法中，跨链合约首先通过 `GetFunctionAndParameters()` 方法获取了合约调用者（也就是业务合约）的调用方法和相应参数，然后通过对方法名进行判断，从而调用不同的合约。

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

我们着重来分析一下当调用了 `EmitInterchainEvent()` 时，跨链合约做了什么，相应说明见注释。

```go
func (broker *Broker) EmitInterchainEvent(stub shim.ChaincodeStubInterface, args []string) pb.Response {
    // 判断传入参数数量是否正确
    // 跨链合约需要传入很多参数，如调用失败在链上容易产生安全问题
	if len(args) != 5 {
		return shim.Error("incorrect number of arguments, expecting 7")
	}

	// 读取参数并存入相应变量

	// 目标链 ID
	dstServiceID := args[0]

	// 自己的链码 ID
	cid, err := getChaincodeID(stub)
	if err != nil {
		return shim.Error(err.Error())
	}

	// 获取 bxhID 和 appchainID
	curFullID, err := broker.genFullServiceID(stub, cid)
	if err != nil {
		return shim.Error(err.Error())
	}

	// 将当前链 ID 和目标链 ID 组合成输出跨链服务组
	outServicePair := genServicePair(curFullID, dstServiceID)

	// 获取输出值的键值对
	outMeta, err := broker.getMap(stub, outterMeta)
	if err != nil {
		return shim.Error(err.Error())
	}

	// 查询输出跨链服务组是否在键值对中，否则设为 0
	if _, ok := outMeta[outServicePair]; !ok {
		outMeta[outServicePair] = 0
	}

	// 封装交易信息
	tx := &Event{
		Index:     outMeta[outServicePair] + 1,
		DstFullID: dstServiceID,
		SrcFullID: curFullID,
		Func:      args[1],
		Args:      args[2],
		Argscb:    args[3],
		Argsrb:    args[4],
	}

	// 输出服务自增
	outMeta[outServicePair]++

	// 将交易信息转为 json 格式
	txValue, err := json.Marshal(tx)
	if err != nil {
		return shim.Error(err.Error())
	}

	// 将输出事件消息格式化
	key := broker.outMsgKey(outServicePair, strconv.FormatUint(tx.Index, 10))

	// 将消息与交易信息写入账本（持久化）
	if err := stub.PutState(key, txValue); err != nil {
		return shim.Error(fmt.Errorf("persist event: %w", err).Error())
	}

	// 设定相应跨链交易事件名称，并将交易信息存入 payload 中
	if err := stub.SetEvent(interchainEventName, txValue); err != nil {
		return shim.Error(fmt.Errorf("set event: %w", err).Error())
	}

	// 将元数据状态写入账本
	if err := broker.putMap(stub, outterMeta, outMeta); err != nil {
		return shim.Error(err.Error())
	}

	return shim.Success(nil)
}
```

以上就是调用跨链合约时所做的，本质上其实只是在跨链合约中通过 `SetEvent()` 设置了一个触发一个事件，再在插件中通过 `RegisterChaincodeEvent()` 进行订阅监听。

```go
SetEvent(name string, payload []byte) error
```

`SetEvent()` 是 `shim` 包下的一个接口，主要传入名称与 payload 数组，关于链码事件监听原理与细节详见 <[Hyperledger Fabric Go SDK 事件分析](https://www.pseudoyu.com/zh/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)>。

### 业务合约

分析完了跨链合约，我们来看看业务合约是如何调用跨链合约的呢，以示例中的 `data_swapper.go` 数据交换合约为例。

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

如想在 `data_swapper.go` 业务合约中获取其他链的信息，通过 `switch...case...` 在调用 `get` 方法时首先对输入参数数组 `args []string` 的长度进行判断，当长度为 1 时，正常调用自身合约进行查询，而当长度为 2 时，首先通过 fabric 提供的 `ToChaincodeArgs()` 方法将参数从 `string` 转为链码参数数组格式。

```go
func ToChaincodeArgs(args ...string) [][]byte {
	bargs := make([][]byte, len(args))
	for i, arg := range args {
		bargs[i] = []byte(arg)
	}
	return bargs
}
```

然后直接在业务链码中通过 `InvokeChaincode()` 方法调用跨链合约，并传入参数和通道 ID，至此就完成了一次跨链数据查询链码调用。

## 总结

以上就是对跨链交易流程与 BitXHub 跨链插件（Fabric）源码解读，也希望在此过程中加深对跨链机制和相关平台的理解，未来能更好地参与到其开源建设中。

## 参考资料

> 1. [跨链技术平台 BitXHub](https://github.com/gocn/opentalk/tree/main/PhaseTen_BitXHub)
> 2. [BitXHub Document](https://meshplus.github.io/bitxhub/bitxhub/introduction/summary/)
> 3. [meshplus/pier-client-fabric](https://github.com/meshplus/pier-client-fabric)
> 4. [十问 BitXHub:谈谈跨链平台的架构设计](https://tech.hyperchain.cn/bitxhub-design-thinking/)
> 5. [跨链合约编写文档](https://github.com/meshplus/bitxhub/wiki/跨链合约编写文档)
> 6. [Hyperledger Fabric Go SDK 事件分析](https://www.pseudoyu.com/zh/2021/09/01/blockchain_hyperledger_fabric_gosdk_event/)