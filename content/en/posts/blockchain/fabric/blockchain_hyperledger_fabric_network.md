---
title: "A Brief Analysis of Hyperledger Fabric Network and Security System"
date: 2021-03-23T12:12:17+08:00
draft: false
tags: ["blockchain", "hyperledger fabric", "security"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

In the previous article, "[Detailed Explanation of Hyperledger Fabric Architecture](https://www.pseudoyu.com/en/2021/03/20/blockchain_hyperledger_fabric_structure/)", we provided a comprehensive interpretation and analysis of Fabric's architecture and operational principles. As an enterprise-grade blockchain system, how does it construct networks based on complex business requirements? What security issues exist during its operation, and how does Fabric preventively address these issues through its mechanisms?

This article will illustrate how a simplified enterprise Fabric network is constructed through examples, and analyze its network and security system. Any errors or omissions are welcome for discussion and correction.

## Hyperledger Fabric Network

### Hyperledger Fabric Application Scenario Example

#### Business Roles

Let's consider an application scenario using the Fabric system.

There are four organizations: R1, R2, R3, and R4. R4 is the network initiator, while R1 and R4 jointly serve as network administrators.

The system has set up two channels, C1 and C2. R1 and R2 use channel C1, while R2 and R3 use channel C2.

Application A1 belongs to organization R1 and runs on channel C1; application A2 belongs to organization R2 and runs on both channels C1 and C2; application A3 belongs to organization R3 and runs on channel C2.

P1, P2, and P3 are nodes of organizations R1, R2, and R3, respectively.

The ordering node is provided by O4, belonging to organization R4.

#### Construction Process

Compared to real commercial application scenarios, the roles and business logic are greatly simplified, but this is suitable for understanding the functions and interactions between different nodes and roles. Next, I will explain the network construction process step by step.

> Create network and add network administrators

Each organization needs a certificate issued by the CA authority in the MSP to join the network, so each node needs to have a corresponding CA.

As the network initiator, R4 needs to configure the network first and establish the O4 ordering node! After the network is created, R1 is added as a network administrator, so R1 and R4 can configure the network (NC4).

![fabric_network_example_1](https://image.pseudoyu.com/images/fabric_network_example_1.png)

> Define consortium and create channel

R1 and R2 will interact through C1, so a consortium needs to be defined in the network. Since both R1 and R4 can now configure the network, both can define the consortium.

Then create channel C1 for this consortium (connected to ordering service O4).

![fabric_network_example_2](https://image.pseudoyu.com/images/fabric_network_example_2.png)

> Join nodes, deploy smart contracts and applications

Node P1 joins the established channel C1, maintaining a ledger L1.

At this point, smart contracts can be installed and instantiated on the node. Fabric's smart contracts are chaincodes. Storing chaincode on the node's file system is called installing a smart contract. After installation, the chaincode needs to be launched and instantiated on a specific channel. At this point, applications can send transaction proposals to endorsing nodes (following the endorsement policy set by the chaincode).

As shown in the figure below, after node P1 installs chaincode S5 and instantiates it on channel C1, it can respond to chaincode invocations from application A1; after node P2 installs chaincode S5 and instantiates it on channel C1, it can respond to chaincode invocations from application A2.

Every node in the channel is a committing node, capable of receiving new blocks (from ordering nodes) for validation and committing to the ledger; some nodes with deployed chaincodes can become endorsing nodes.

![fabric_network_example_4](https://image.pseudoyu.com/images/fabric_network_example_4.png)

> Define new consortium, create new channel

Define a new consortium in the network and join channel C2.

![fabric_network_example_5](https://image.pseudoyu.com/images/fabric_network_example_5.png)

> Join new nodes and deploy smart contracts and applications

It's worth noting that some nodes will join multiple channels, playing different roles in different businesses. Other processes are the same as above.

![fabric_network_example_6](https://image.pseudoyu.com/images/fabric_network_example_6.png)

> Network construction complete

![hyperledger_fabric_network_example](https://image.pseudoyu.com/images/hyperledger_fabric_network_example.png)

Fabric adopts mechanisms such as permission management and channels, and improves system operational efficiency through functional division of different nodes, while ensuring security and privacy in complex business scenarios. Powerful chaincodes and customizable endorsement policies also ensure the system's scalability and ability to handle complex business logic.

## Hyperledger Fabric Security Analysis

### Fabric Security Mechanisms

Fabric has designed many mechanisms to ensure system security.

#### System Configuration and Membership Management

Unlike public chains such as Bitcoin and Ethereum, joining the Fabric network requires permission verification. Fabric CA uses the X.509 certificate mechanism for membership management to ensure its permissions and avoid potential spoofing attacks.

Existing system members need to establish rules for adding new members, such as majority voting; existing members also need to decide on network and smart contract updates and changes, which can greatly prevent malicious nodes from compromising system security; existing nodes cannot upgrade permissions on their own; in addition, they need to decide on system-wide data models and other settings.

Fabric's network transmission uses TLSv1.2, which can ensure data security; operations in the system, such as initiating transactions and endorsements, will be recorded through digital signature technology, making it easy to trace some malicious operations. However, it's worth noting that ordering nodes can access transaction data from all nodes in the system. Therefore, the setting of ordering service nodes is particularly important for the security of the entire system. Its impartiality will greatly affect the operation of the entire system and even determine whether the entire system is trustworthy. Therefore, it needs to be carefully selected based on business and system structure.

In public chain systems, all nodes have a copy of the blockchain ledger and execute smart contracts; in the Fabric system, business-related nodes form node groups, storing ledgers related to their transactions (business), and updates to the ledger through chaincode are also limited to the scope of the node group, thereby ensuring the stability of the entire system.

The execution of smart contracts is called a transaction. For transactions within the Fabric system, consistency must also be maintained. Cryptographic techniques are often used to prevent transactions from being tampered with, such as using SHA256, ECDSA, etc., to detect modifications. Fabric adopts a modular, pluggable design, separating transaction execution, validation, and consensus, so different consensus mechanisms or rules can be adopted. This not only allows for the selection of different consensus mechanisms according to needs, providing more scalability, but also improves system security.

These configurations and rules collectively determine the security of the system and need to be balanced against business requirements, efficiency, and security.

#### Smart Contract Security

Fabric's chaincode needs to be installed on nodes and instantiated. Installing chaincode requires CA verification, so permission management needs to be considered; once launched, it runs in an independent Docker container, which is more lightweight, but because it can access the Fabric network, it can cause some malicious consequences if it hasn't undergone strict code auditing and network isolation.

Fabric's chaincode can be written in multiple general-purpose programming languages, such as Go, Java, etc., which gives the system stronger scalability and makes it easier to integrate with existing systems and tools. However, because its execution results are deterministic, some features of programming languages (such as random numbers, system timestamps, pointers, etc.) may cause different endorsing nodes to produce different execution results, leading to system inconsistency. In addition, because chaincode can access some external Web services, system commands, file systems, and third-party libraries, it can also pose some potential risks. Therefore, chaincodes developed in these general-purpose languages need to be relatively independent and undergo enhanced code auditing to avoid some security risks brought by programming languages.

#### Transaction Privacy

Fabric uses a channel mechanism to divide the entire system into multiple sub-blockchains (ledgers), and only nodes that join the channel can view and store transaction information, but ordering nodes can see it.

> So how can privacy of some private data be ensured within a channel?

Fabric provides a way to store private data, allowing nodes in the channel to choose specific data sharing objects (nodes).

![fabric_security_private_data](https://image.pseudoyu.com/images/fabric_security_private_data.png)

Under this mechanism, real data is sent to specified nodes through the gossip protocol and stored in a private database, which can only be accessed through chaincode by authorized nodes. Because this process does not involve the ordering service, ordering nodes cannot obtain the data.

The data propagated, ordered, and written to the ledger within the system is a hashed version, so the transaction can still be verified by each node, but due to the nature of hashing, it can effectively protect the original data from being leaked.

However, it's worth noting that if data needs to be used during the transaction simulation process on endorsing nodes, additional mechanisms need to be adopted to ensure the readability of the data to endorsing nodes and its invisibility to other nodes (such as asymmetric encryption).

## Conclusion

The above is an analysis of Hyperledger Fabric network construction and security system. Next, I will start learning Go and chaincode development, gaining a deeper understanding through project practice!

## References

> 1. [FITE3011 Distributed Ledger and Blockchain](https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2019/fite3011.html), *Allen Au，HKU*