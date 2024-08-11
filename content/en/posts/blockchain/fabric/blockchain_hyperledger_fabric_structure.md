---
title: "Detailed Explanation of Hyperledger Fabric System Architecture"
date: 2021-03-20T12:12:17+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "structure"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

As my graduation case study project was primarily based on the Ethereum public chain and lacked enterprise application scenarios, my previous understanding of Hyperledger Fabric was mostly limited to concepts such as its permission management mechanism, channels, and flexible smart contract writing. I had only a vague understanding of its architecture, the roles of various nodes, and operational mechanisms. Recently, while taking the course "FITE3011 Distributed Ledger and Blockchain" at HKU, the professor provided a detailed explanation of Hyperledger Fabric's working principles, network setup, and chaincode-related knowledge. I found it immensely beneficial. Through this article, I aim to organize my thoughts on the subject. If there are any errors or omissions, I welcome discussions and corrections.

## Overview of Hyperledger

To learn about Hyperledger Fabric, let's first look at what its parent project, Hyperledger, is.

Enterprise-level applications have complex business logic and participant role divisions, with high requirements for business execution efficiency and security. For common scenarios such as payment and data/information transactions, privacy protection is also of paramount importance. Therefore, common public chains like Bitcoin and Ethereum do not meet the needs of most enterprise applications. However, the distributed and immutable historical ledger characteristics of blockchain can avoid complex operational processes caused by legal regulations and currencies of different countries/regions in scenarios such as traceability and cross-border e-commerce, greatly improving efficiency. As a result, consortium chains aimed at enterprises are continuously developing.

Consortium chains are not truly "decentralized" in the strict sense. They introduce permission management mechanisms (combining enterprise roles in real business) to weaken the prevention mechanism against node malicious behavior, thereby improving efficiency and addressing complex business logic.

Among them, Hyperledger is a set of open-source projects maintained by the Linux Foundation that focuses on cross-industry distributed technologies. It aims to create enterprise-grade, open-source, distributed classification frameworks and code libraries to support business use cases; provide neutral, open, and community-driven infrastructure; build technical communities and promote them; develop blockchain and shared ledger proofs of concept, use cases, trials, and deployments; establish industry standards; encourage more enterprises to participate in the construction and application of distributed ledger technology; and form an open ecosystem; educate the public about market opportunities in blockchain technology.

### Design Philosophy

![hyperledger_design_philosophy](https://image.pseudoyu.com/images/hyperledger_design_philosophy.png)

Hyperledger has several core design philosophies:

1. It improves efficiency for specific enterprise business scenarios and has unique advantages in traceability and other scenarios. Each enterprise can maintain an independent Hyperledger project for its own scenarios. Therefore, it does not need to use digital currency to incentivize users to participate in the blockchain system like public chains do.
2. Enterprise application scenarios are relatively complex, and Hyperledger often participates in only one or some aspects. Therefore, interaction with other existing systems is essential. Thus, Hyperledger focuses on providing complete APIs for other systems to call and interact with in its design.
3. Hyperledger's framework structure is modular and extensible. Enterprises can choose different modules according to specific business needs, avoiding complex business logic and bloated systems.
4. Security is paramount for enterprise applications, especially in many application scenarios involving high-value transactions or sensitive data. Therefore, many mechanisms are provided to ensure security (such as Fabric's channel mechanism).
5. In addition to interacting with existing systems, enterprise blockchain applications may interact with many different blockchain networks in the future. Therefore, most smart contracts/applications should have portability across blockchain networks to form more complex and powerful networks.

![hyperledger_family](https://image.pseudoyu.com/images/hyperledger_family.png)

#### Frameworks

Hyperledger has the following projects, among which Fabric is currently the most widely applied. This article will mainly introduce the Fabric blockchain network:
- Burrow
- Fabric
- Grid
- Indy
- Iroha
- Sawtooth

#### Tools

1. Hyperledger Cello. Mainly used for more convenient setup and management of blockchain services, reducing the complexity of project framework deployment and maintenance; can be used to build blockchain BaaS platforms; can create and manage blockchains through a dashboard, allowing technical personnel to develop and deploy more conveniently; can introduce SaaS deployment models into blockchain systems, helping enterprises further develop frameworks.
2. Hyperledger Explorer. A visualization tool for blockchain operations, which can be used to create user-friendly web applications; it is the first blockchain explorer for Hyperledger, allowing users to view/invoke/deploy/query transactions, networks, smart contracts, storage, and other information.

## Hyperledger Fabric

Let's focus on the Fabric project, which is the most widely applied. It is a modular, extensible blockchain consortium chain project maintained by the Linux Foundation, not dependent on any cryptocurrency. It provides protection for businesses between entities that have common goals (business needs) but do not fully trust each other, such as cross-border e-commerce, fund transactions, traceability, etc.

### Architecture

![ethereum_architecture_simple](https://image.pseudoyu.com/images/ethereum_architecture_simple.png)

In most public chains, the architecture is "Order - Execute - Validate - Update State". For example, in the Bitcoin blockchain, when there is a new transaction, it first uses the PoW mechanism to order the Block, then each node in the Bitcoin network verifies it individually, and finally updates the state. Because verification needs to be done sequentially, this method determines that its execution efficiency is relatively low.

Fabric adopts the "Execute - Order - Validate - Update State" architecture.

![hyperledger_fabric_architecture](https://image.pseudoyu.com/images/hyperledger_fabric_architecture.png)

After receiving a new transaction, it is first submitted to the endorsement node for local simulation of transaction execution (and endorsement), then the endorsed transactions are ordered and broadcast, and each node validates the transaction before updating the state.

![hyperledger_fabric_architecture_complete](https://image.pseudoyu.com/images/hyperledger_fabric_architecture_complete.png)

As mentioned in the consortium chain characteristics above, joining the Fabric network requires permission (identity verification), and each node in the Fabric network has its own identity.

Overall, Fabric supports complex enterprise business scenarios through modular, pluggable architecture, weakens node malicious behavior through identity verification (binding real identities), and greatly enhances system security and privacy protection using the channel mechanism.

#### MSP (Membership Service Provider)

So, how are the identities of participants in the Fabric network managed?

Fabric has an MSP (Membership Service Provider) that mainly uses CA certificates to verify which members are trustworthy. The Fabric CA module is independent and can manage certificate services, and also allows third-party CA access, greatly expanding the application scope of the system.

![hyperledger_fabric_ca_structure](https://image.pseudoyu.com/images/hyperledger_fabric_ca_structure.png)

As shown in the above figure, Fabric CA provides both client and SDK methods to interact with CA. Each Fabric CA has a root CA or intermediate CA. To further enhance CA security, clusters can be used to build intermediate CAs.

![hyperledger_fabric_ca_hierarchy](https://image.pseudoyu.com/images/hyperledger_fabric_ca_hierarchy.png)

Looking more specifically at the CA hierarchy, it generally adopts a three-layer tree structure of root CA, business CA, and user CA. All lower-level CAs inherit the trust system of the upper-level CA. The root CA is used to issue business CAs, while business CAs are used to issue specific user CAs (identity authentication CA, transaction signature, secure communication CA, etc.)

#### Channels

As mentioned above, Fabric uses the Channel mechanism to ensure transaction security and privacy. Essentially, each channel is an independent ledger, also an independent blockchain, with different world states. A node in the network can join multiple channels simultaneously. This mechanism can effectively divide different business scenarios without worrying about transaction information leakage.

#### Chaincode

Fabric also has smart contracts similar to Ethereum, called Chaincode. Smart contracts allow external applications to interact with the ledger in the Fabric network. Unlike Ethereum, Fabric uses Docker instead of a specific virtual machine to store chaincode, providing a secure, lightweight language execution environment.

Chaincode is mainly divided into system chaincode and user chaincode. System chaincode is embedded in the system, providing support for system configuration and management; user chaincode runs in separate Docker containers, providing support for upper-layer applications. Users can write user chaincode through chaincode-related APIs to update the state in the ledger.

Chaincode can be invoked after installation and instantiation. During installation, it needs to be specified which Peer node to install on (some nodes may not have chaincode), and during instantiation, the channel and endorsement policy need to be specified.

Chaincodes can also call each other, thus creating more flexible application logic.

#### Consensus Mechanism

The broad consensus mechanism in Fabric includes endorsement, ordering, and validation. In the narrow sense, consensus refers to ordering.

In the Fabric blockchain network, transactions between different participants must be written to the distributed ledger in the order they occur, relying on the consensus mechanism. There are mainly three types:
- SOLO (limited to development)
- Kafka (a messaging platform)
- Raft (more centralized compared to Kafka)

#### Network Protocol

So how is the state distribution among nodes in the Fabric network carried out?

External clients use gRPC to make remote calls to various nodes in the Fabric network, while synchronization between nodes in the P2P network is done through the Gossip protocol.

The Gossip protocol is mainly used for data exchange between multiple nodes in the network. It is relatively easy to implement and has a high fault tolerance rate. The principle is that the data sender randomly selects several nodes from the network to send to, and after these nodes receive the data, they randomly send it to several nodes other than the sender, repeatedly, until all nodes reach consensus (complexity is LogN).

#### Distributed Ledger

Finally, all transactions are recorded in the distributed ledger, which is the core of many blockchain features. In Fabric, transactions can store relevant business information. A block is a collection of ordered transactions, and linking blocks through cryptographic algorithms forms the blockchain. The distributed ledger mainly records the world state (the latest distributed ledger state, generally using CouchDB for easy querying) and transaction logs (update history of the world state, recording the blockchain structure, using LevelDB). Every operation on the ledger is recorded in the log and is immutable.

#### Application Programming Interface

For applications based on Fabric, two main ways of interaction are provided: SDK development toolkit and CLI command line.

### Core Roles in Fabric Blockchain

First, it should be mentioned that the roles in the Fabric network are all logical roles. For example, Peer node A might be both an ordering node and an endorsement node in some businesses, and a role is not necessarily played by a single node.

Next, let's introduce the functions and roles of each role.

Clients mainly sign transactions, submit transaction Proposals to endorsement nodes, receive endorsed transactions and broadcast them to ordering nodes; endorsement nodes locally simulate the execution of transaction Proposals to verify transactions (policies are set by Chaincode), sign and return endorsed transactions; ordering nodes package transactions into blocks and then broadcast them to various nodes, not participating in transaction execution and verification. Multiple ordering nodes can form an OSN; all nodes maintain the blockchain ledger.

### Summary of Advantages

Fabric allocates various complex aspects of enterprise applications to different logical role nodes (endorsement, ordering, etc.), eliminating network bottlenecks as not all nodes need to undertake resource-intensive operations like ordering; after role allocation, certain transactions are only deployed and executed on specific nodes, and can be executed concurrently, greatly improving efficiency and security, while also hiding some business logic; therefore, various flexible allocation schemes can be formed according to different business needs, greatly enhancing the system's extensibility.

Setting consensus mechanisms, permission management, encryption mechanisms, ledgers, and other modules as pluggable, and allowing different chaincodes to set different endorsement policies, makes the trust mechanism more flexible, allowing efficient systems to be set up according to business needs.

The Fabric CA for member identity management is a separate project, capable of providing more functions and directly interfacing and interacting with many third-party CAs, making it more powerful and suitable for complex enterprise scenarios.

The multi-channel feature isolates data between different channels, improving security and privacy protection.

Chaincode supports different programming languages such as Java, Go, Node, etc., making it more flexible and supporting more third-party extension applications, reducing business migration and maintenance costs.

### Fabric Application Development and Interaction

![hyperledger_fabric_application_interact](https://image.pseudoyu.com/images/hyperledger_fabric_application_interact.png)

The above diagram shows the development and interaction process for a blockchain developer applying the Fabric blockchain.

Developers are mainly responsible for developing applications and smart contracts (chaincode). Applications interact with smart contracts through SDK, while the logic of smart contracts can perform operations such as get, put, delete on the ledger.

### Fabric Workflow

![hyperledger_fabric_transaction_flow](https://image.pseudoyu.com/images/hyperledger_fabric_transaction_flow.png)

Next, let's review the working principle of the Fabric network through a complete transaction flow

0. Before all operations, it's necessary to obtain a legal identity from CA and specify the channel
1. First, the Client submits a transaction Proposal (with its own signature) to the endorsement nodes
2. After receiving the transaction Proposal, the endorsement nodes simulate execution using local state, endorse and sign the transaction, and return it (including Read-Write Set, signature, etc.)
3. After the Client collects enough endorsements (policy set by Chaincode, as in the example in the diagram, obtaining 2 endorsements), it submits the endorsed transaction to the ordering nodes (OSN)
4. The ordering nodes package transactions into blocks, order them (without executing or verifying transaction correctness), and broadcast to all nodes
5. All nodes validate the new blocks and commit them to the ledger

![hyperledger_fabric_processes](https://image.pseudoyu.com/images/hyperledger_fabric_processes.png)

Next, let's break down each stage in detail

#### Execution/Endorsement Stage

After the Client submits the transaction proposal, the endorsement nodes first verify the Client's signature, simulate execution using local state, sign the transaction, and return Read-Write Sets to Clients. R-W Sets mainly include three attributes: key, version, and value. The Read-Set contains all variables read during transaction execution and their version. If there's a write operation on the ledger, the version will change. The Write-Set contains all edited variables and their new values.

When executing transactions, endorsement nodes only check if the chaincode is correct based on the local blockchain state, execute, and return.

Fabric supports multiple endorsement policies. The Client verifies if endorsement requirements are met before submitting to the ordering nodes. It's worth noting that if only ledger query operations are performed, the Client won't submit to OSN.

The transaction proposal mentioned above mainly includes chaincode, chaincode input values, and Client signature, while the information returned by endorsement nodes to the Client includes return values, R-W Set of simulated execution results, and endorsement node signatures, which together form the endorsed nodes.

Endorsement is the approval of transactions by relevant organizations, i.e., relevant nodes signing the transaction. For a chaincode transaction, the endorsement policy is specified during chaincode instantiation. An effective transaction must be signed by organizations related to the endorsement policy to take effect. Essentially, transaction verification in the Fabric blockchain is based on trust in endorsement nodes, which is one of the reasons why Fabric is not considered strictly decentralized.

Here's a simple example of chaincode execution

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

In this simple example, the main operation of the chaincode is to update the key-value pair. After this operation, the version will change.

The R-W Set returned after execution is

```go
key: 1
value: JSON form of Product { Name: "Test Product", Description: "Just a test product to make sure chaincode is running", CreatedBy: "admin", ProductId: "1" }
```

#### Ordering Stage

The Client submits endorsed transactions to ordering nodes (ordering nodes can form OSN through some consensus strategies). After receiving transactions, ordering nodes package them into blocks and order them according to the rules in the configuration. During this process, they only perform ordering operations without any execution or verification. After ordering is complete, they send to all nodes.

The ordering service is used to reach consensus on transactions across the entire network, only responsible for reaching consensus on transaction order, avoiding network bottlenecks and making it easier to scale horizontally to improve network efficiency. Currently, it supports two types: Kafka and Raft. The unity/integrity of the Fabric blockchain network depends on the consistency of ordering nodes.

The Raft consensus mechanism belongs to the non-Byzantine consensus mechanism and uses a leader and follower model. When a leader is elected, log information is unidirectionally replicated from the leader to followers, making it easier to manage. In design, it allows all nodes to become Orderer nodes, making it more centralized compared to Kafka. It actually also allows the use of PBFT consensus mechanism, but the performance is often very poor.

#### Validation Stage

When a node receives blocks sent by ordering nodes, it validates all transactions in the block and marks whether they are trustworthy. It mainly verifies two aspects: 1. Whether it meets the endorsement policy. 2. The legality of the transaction structure, whether there are state conflicts, such as whether the version in the Read-Set is consistent, etc.

## Conclusion

The above is a review of the Hyperledger Fabric architecture. Although it has sacrificed some of the decentralization concept, as an open-source consortium chain oriented towards enterprise applications, it encourages more enterprises to participate in the construction and application of distributed ledger technology. Now there are many self-developed consortium chain platforms in China, such as Ant Chain, Qulian, etc. I believe that more enterprises will participate in this open ecosystem in the future!

## References

> 1. [FITE3011 Distributed Ledger and Blockchain](https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2019/fite3011.html), *Allen Au, HKU*
> 2. [Enterprise Blockchain Practical Tutorial](https://github.com/yingpingzhang/enterprise_blockchain_tutorial), *Zhang Yingping*