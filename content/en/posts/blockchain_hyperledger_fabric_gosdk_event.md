---
title: "Hyperledger Fabric Go SDK 事件分析"
date: 2021-09-01T17:21:58+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "go", "gosdk"]
categories: ["Develop"]
authors:
- "Arthur"
---

## 前言

最近在做跨链适配器，需要在一条本地链上利用 Go SDK 来连接 fabric 网络，并监听事件，所以对 fabric 所支持的事件与 SDK 所提供的监听方法做一下汇总。

## Fabric 事件

![hyperledger_fabric_application_interact](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/hyperledger_fabric_application_interact.png)

事件是客户端与 Fabric 网络进行交互的一种方式，如上图所示，Fabric 网络中执行一个交易后，因为是异步进行的，所以客户端无法获取提交的交易状态（是否被接受），因此，Fabric 的 Peer 节点提供了事件机制，客户端可以通过 gRPC 接口来监听区块事件。从 fabric v1.1 开始，时间的注册发生在通道级别而不是 Peer 节点，因此可以进行更精细的控制

### 事件类型

事件主要由 Ledger 和存有链码合约的容器触发。Fabric 共支持四种事件形式：

1. BlockEvent 监控新增到 fabric 上的块时使用
2. ChaincodeEvent 监控链码中发布的事件时使用，也就是用户自定义事件
3. TxStatusEvent 监控节点上的交易完成时使用
4. FilteredBlockEvent 监控简要的区块信息

在 Fabric Go SDK 中则通过以下几种事件监听器进行操作

1. `func (c *Client) RegisterBlockEvent(filter ...fab.BlockFilter) (fab.Registration, <-chan *fab.BlockEvent, error)`
2. `func (c *Client) RegisterChaincodeEvent(ccID, eventFilter string) (fab.Registration, <-chan *fab.CCEvent, error)`
3. `func (c *Client) RegisterFilteredBlockEvent() (fab.Registration, <-chan *fab.FilteredBlockEvent, error)`
4. `func (c *Client) RegisterTxStatusEvent(txID string) (fab.Registration, <-chan *fab.TxStatusEvent, error)`

而当监听完成后需要通过 `func (c *Client) Unregister(reg fab.Registration)` 来取消注册并移除事件通道

### gRPC 通信

SDK 与 Peer 节点通过 gRPC 进行通讯，源码见 [fabric-protos/peer/events.proto](https://github.com/hyperledger/fabric-protos/blob/main/peer/events.proto)

其中，定义了以下几种 message：

1. FilteredBlock，给 FilteredBlockEvent 使用
2. FilteredTransaction 和 FilteredTransaction，给 FilteredTransactionEvent 使用
3. FilteredChaincodeAction，给 ChaincodeEvent 使用
4. BlockAndPrivateData，给私有数据使用

Response 如下：

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

以及三个 gRPC 通信接口：

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

![fabric_events](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/fabric_events.svg)

整个流程如上图所示，Go SDK 中通过实现一个 Dispatcher 将应用中的事件注册请求转换为事件订阅请求并通过 DeliverClient 发送给 Peer 节点，Peer 节点中的 DeliverServer 接收订阅请求，调用 deliverBlocks 进入循环，从 Ledger 读取区块并生成事件，最后发送给客户端，客户端中的 Dispatcher 又将其转换为应用订阅的事件响应。


### 事件实现过程

实现时间过程需要两个步骤

1. 在链码中调用 `SetEvent` 方法
2. 在在客户端中通过 Go SDK 实现事件监听器

#### SetEvent 方法

方法定义

```go
func (s *ChaincodeStub) SetEvent(name string, payload []byte) error
```

调用实例

```go
func (s *SmartContract) Invoke(stub shim.ChaincodeStubInterface) sc.Response {

    err = stub.PutState(key, value)

    if err != nil {
        return shim.Error(fmt.Sprintf("unable put state (%s), error: %v", key, err))
    }
    
    // Payload 需要转换为字节格式
    eventPayload := "Event Information"
    payloadAsBytes := []byte(eventPayload)

    // SetEvent 方法通常位于 PutState、DelState 等与账本交互的操作之后
    err = stub.SetEvent("<事件名称>", payloadAsBytes)

    if (eventErr != nil) {
        return shim.Error(fmt.Sprintf("事件触发失败"))
    }

    return shim.Success(nil)
}
```

#### 客户端事件监听器

```go
// 实现一个链码事件监听
// 传入相应参数，这里的 eventId 必须与链码里的 <事件名称> 匹配以实现监听
reg, eventChannel, err := eventClient.RegisterChaincodeEvent(chaincodeID, eventID)

if err != nil {
    log.Fatalf("Failed to regitser block event: %v\n", err)
    return
}

// 取消注册并移除事件通道 
defer eventClient.Unregister(reg)
```

## 总结

以上就是通过 Go SDK 对 fabric 网络上的事件进行监听操作的基本介绍，正在看 fabric Go SDK 源码，后续将补充一些解读。

## 参考资料

> 1. [hyperledger/fabric-sdk-go](https://github.com/hyperledger/fabric-sdk-go)
> 2. [Hyperledger Fabric Packages for Go Chaincode](https://pkg.go.dev/github.com/hyperledger/fabric-chaincode-go)
> 3. [基于通道的 Peer 节点事件服务](https://hyperledger-fabric.readthedocs.io/zh_CN/latest/peer_event_services.html)
> 4. [fabric-protos/peer/events.proto](https://github.com/hyperledger/fabric-protos/blob/main/peer/event)
> 5. [Fabric 1.4 源码解读 3：事件(Event)原理解读](https://lessisbetter.site/2019/09/20/fabric-event-source/)
> 6. [fabric 支持的事件](https://www.jianshu.com/p/aecaae8aa3da)
> 7. [如何监听 Fabric 链码的事件](http://blog.hubwiz.com/2019/07/07/Hyperledger-fabric-chaincode-event/)