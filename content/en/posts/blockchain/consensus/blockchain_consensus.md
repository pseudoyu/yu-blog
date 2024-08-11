---
title: "Distributed Systems and Blockchain Consensus Mechanisms"
date: 2021-09-08T11:03:55+08:00
draft: false
tags: ["blockchain", "consensus", "distributed system"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

As internet systems grow increasingly complex, most have shifted from monolithic to distributed architectures. Blockchain technology, which is fundamentally based on distributed systems, heavily relies on data consistency and consensus mechanisms.

This article will introduce the concepts of consistency and consensus in distributed systems, as well as their practical applications and developments in blockchain technology.

## Distributed Systems

### The Consistency Problem

As business scenarios become more complex, a single service is often provided by multiple servers forming a cluster. However, achieving consensus among these systems with different physical locations and operating states has become a crucial issue in the distributed domain.

Generally, there are three criteria for achieving consensus in distributed systems:

1. Termination
2. Agreement
3. Validity

Distributed transactions must ensure that consensus is reached within a finite time, the result must be a proposal made by one of the nodes, and different nodes must complete the same decision.

### Strong Consistency

Achieving this in a single application or when the performance, network bandwidth, and other configurations of each node are ideal is easy. However, in real business scenarios, implementing such strong consistency is very costly. It requires ensuring absolute system stability and zero communication delays between systems. Moreover, strong consistency also reduces system performance and scalability.

Under strong consistency, data across all nodes is the same at any given moment. Strong consistency typically includes two types: sequential consistency and linearizability.

#### Sequential Consistency

Sequential consistency requires that the global execution order of all processes is consistent with each process's own order, but does not require maintaining a global order for each process in physical time. Therefore, this is a relatively practical approach.

#### Linearizability

Linearizability adds the rule of global ordering between processes on top of sequential consistency, requiring real-time synchronization of operations across all processes at all times. This absolute consistency is often difficult to achieve in practice and requires implementation through global locks or complex synchronization algorithms, often at the cost of performance.

### Weak Consistency

In real business scenarios, such absolute consistent states with real-time synchronization are often unnecessary. Therefore, it is acceptable to tolerate partial access or eventual consistency after a period of time. These consistencies that are weakened in some aspects are called weak consistency.

### Consensus Mechanisms

A consensus mechanism refers to the process by which multiple nodes in a distributed system reach agreement on a transaction. Regarding the achievement of consensus, there are several theories and principles:

- FLP Impossibility
- CAP Theorem
- ACID Principles
- BASE Theory
- Multi-phase Commit

#### FLP Impossibility

The FLP Impossibility, proposed by scientists Fischer, Lynch, and Patterson, states that in an asynchronous system with reliable networks but allowing node failures (such as crashes), it is impossible to achieve consensus in finite time.

Asynchrony refers to differences in time and other factors between system nodes, making it impossible to determine whether a non-responsive message is due to node failure or transmission failure, thus making it impossible to determine if a message is lost.

#### CAP Theorem

In engineering practice, one aspect of requirements is often weakened to meet the needs of real business scenarios. The CAP theorem addresses this issue, where CAP stands for:

- Consistency
- Availability
- Partition tolerance

Distributed systems cannot simultaneously guarantee all three points; at most, they can ensure two of these characteristics. So how is this principle applied in practice?

1. AP systems: In business scenarios such as static websites and non-real-time databases, consistency can be weakened, such as achieving consistency some time after a new version is launched.
2. CP systems: In scenarios absolutely sensitive to consistency, such as bank transfers, availability can be weakened, such as refusing service when the system fails or malfunctions.
3. AC systems: Two-phase commit and some relational databases weaken network partitioning, such as ZooKeeper.

#### ACID Principles

Transactions in distributed databases need to sacrifice some availability to achieve consistency and must follow the ACID principles:

- Atomicity: All operations in a transaction must either be fully executed or not executed at all; if failed, all should be rolled back.
- Consistency: The state before and after transaction execution must be consistent, with no intermediate states.
- Isolation: Multiple transactions can execute concurrently but are independent of each other.
- Durability: State changes are permanent.

#### BASE Principles

The BASE principles stand for:

- Basically Available
- Soft State
- Eventual Consistency

This is an approach that sacrifices strong consistency to implement the entire system, ensuring only eventual consistency.

#### Multi-phase Commit

Two-phase commit divides the transaction commit process into pre-commit and formal commit phases to avoid conflicts, but still has issues with synchronous blocking, single point of failure, and data consistency.

The TCC (Try-Confirm-Cancel) transaction mechanism mainly consists of:

- Try phase
- Confirm phase
- Cancel phase

In the Try phase, the business is checked and business resources are reserved. In the Confirm phase, resources are used to execute the business. In the Cancel phase, execution is cancelled and resources are released. This method adds more business processing to the two-phase commit, but because it is split into three interfaces, the code complexity increases.

Three-phase commit introduces a timeout mechanism and adds a tentative pre-commit step to the first phase of two-phase commit, mainly solving single point of failure and blocking problems.

## Consensus Algorithms

Based on the type of fault tolerance (whether there are malicious nodes), we divide consensus algorithms into Crash Fault Tolerance (CFT) and Byzantine Fault Tolerance (BFT).

### CFT (Crash Fault Tolerance)

Scenarios in distributed systems where faulty nodes exist but erroneous nodes do not are called CFT. In these scenarios, messages may be lost or duplicated but not erroneous. Achieving consensus under these conditions is a very common requirement in the real world.

#### Paxos

The Paxos algorithm principle is similar to two-phase commit, setting three logical nodes: proposer, acceptor, and learner. The proposer proposes proposals, the acceptor votes on and accepts proposals, and the learner obtains and broadcasts proposal results.

Only proposals made by proposers can be approved, and all nodes can compete to become proposers, but only one proposer can make a proposal in each round of consensus. This mechanism ensures a certain degree of fairness.

However, Paxos can only guarantee consensus under certain conditions and operates normally only when more than half of the nodes participate.

#### Raft

Due to the difficulty in implementing the Paxos algorithm, many variants have emerged, such as Fast Paxos, Multi-Paxos, etc., among which the Raft algorithm is quite representative.

Raft divides the consistency process into three sub-problems: leader election, log replication, and safety, and sets three logical nodes: leader, candidate, and follower.

The initial state of all nodes is follower. Those wishing to participate in leader election transform into candidates and propose election requests. If more than half of the votes are received, they successfully become the leader for this term.

The leader handles all requests and synchronizes logs to followers, and periodically sends heartbeat messages to all followers. If a failure occurs and heartbeat messages are not received after timeout, a new election process is initiated.

### BFT (Byzantine Fault Tolerance)

#### Byzantine Fault Tolerance, BFT

The Byzantine Fault Tolerance algorithm is mainly used to handle scenarios where malicious nodes exist in the network, primarily solving the Byzantine problem. It can effectively achieve consensus when malicious nodes do not exceed 1/3, but the complexity is very high (exponential).

#### Practical Byzantine Fault Tolerance, PBFT

PBFT is an optimization of the BFT algorithm, adopting cryptographic techniques such as RSA signatures, message verification, and digests, combined with related algorithms like Paxos, ultimately reducing the algorithm complexity to a square level.

In the PBFT algorithm implementation, a certain node is first selected (randomly/rotating) and set as the primary node. The primary node receives client requests within its own View and broadcasts (using a three-phase commit mechanism, see above) to other nodes. When all nodes complete processing the request, the results are returned to the client. If at least 2f + 1 identical results are received from different nodes, consensus is achieved.

- Tentative pre-commit: After receiving the message, the primary node signs and broadcasts to other nodes
- Pre-commit: After receiving the message, other nodes verify, sign if legal, and broadcast to other nodes, which also verify
- Formal commit: Sign the message and broadcast the commit status; if verified by 2f + 1 nodes, the system completes consensus

#### Others

In addition to PBFT, PoW, PoS, HotStuff, etc., are widely used in blockchain projects such as Bitcoin, Ethereum, Libra, and are constantly being optimized. Byzantine fault-tolerant algorithms are mostly used in public chain environments due to their low efficiency, while consortium chains often adopt non-Byzantine fault-tolerant methods, supplemented by access control and other methods to balance performance and security.

## Conclusion

The above is a summary of the concepts and practical applications of distributed systems and blockchain consensus mechanisms. In the future, I will also provide a more in-depth analysis of various consensus algorithms used in the industry.

## References

> 1. [Blockchain: Principle, Design and Application](https://book.douban.com/subject/27127839/)
> 2. [Distributed Transactions, This Article Is Enough](https://xiaomi-info.github.io/2020/01/02/distributed-transaction/)
> 3. [Understanding TCC, 2PC and 3PC](http://anruence.com/2018/03/05/tcc-2pc-3pc/)
> 4. [【Consensus Column】Classification of Consensus (Part 1)](https://tech.hyperchain.cn/gong-shi-zhuan-lan-gong-shi-de-fen-lei-shang/)
> 5. [【Consensus Column】Classification of Consensus (Part 2)](https://tech.hyperchain.cn/gong-shi-zhuan-lan-gong-shi-de-fen-lei-xia/)