---
title: "Ethereum Core Technology Interpretation"
date: 2021-02-20T12:12:17+08:00
draft: false
tags: ["blockchain", "ethereum"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Bitcoin, as a decentralized digital currency, has been extremely successful. However, limited by the Bitcoin script (which is not Turing complete and can only handle simple logic), it cannot process very complex business operations. Ethereum introduced smart contracts, allowing the concept of decentralization to be applied to a wider range of application scenarios, thus also being called blockchain 2.0. This article will interpret the core technologies of Ethereum. Any errors or omissions are welcome for discussion and correction.

## Ethereum System

In January 2014, Russian developer Vitalik Buterin published the Ethereum white paper and formed a team, aiming to create a blockchain platform that integrates a more general scripting language. One of the team members, Dr. Gavin Wood, published a yellow paper detailing the technical aspects of the Ethereum Virtual Machine (EVM). This marked the birth of Ethereum.

![ethereum_overview](https://image.pseudoyu.com/images/ethereum_overview.png)

In simple terms, Ethereum is an open-source decentralized system that uses blockchain to store system state changes, hence also known as the "world computer". It allows developers to deploy and run immutable programs on the blockchain, called smart contracts, thus supporting a wide range of application scenarios. It uses the digital currency Ether to measure system resource consumption and incentivize more people to participate in building the Ethereum system.

### Decentralized Applications (DApps)

In a narrow sense, a DApp is an application that integrates a user interface, supports smart contracts, and runs on the Ethereum blockchain.

![ethereum_architecture](https://image.pseudoyu.com/images/ethereum_architecture.png)

As shown in the above diagram, Ethereum application instances are deployed on the blockchain network (smart contracts run in the blockchain virtual machine), while the web program only needs to make RPC remote calls to the blockchain network through Web3.js. This way, users can access decentralized service applications through browsers (DApp browsers or plugin tools like MetaMask).

### Ledger

The Ethereum blockchain is a decentralized ledger (database) where all transactions in the network are stored. All nodes must keep a local copy of the data and ensure the credibility of each transaction. All transactions are public and immutable, and all nodes in the network can view and verify them.

### Accounts

When we need to log into a website or system (such as an email), we often need an account and a password. The password is stored in encrypted form in a centralized database. However, Ethereum is a decentralized system, so how are accounts generated?

Similar to the Bitcoin system principle:

1. First, generate a private key known only to yourself, let's say 'sk', and use the Elliptic Curve Digital Signature Algorithm (ECDSA) to generate the corresponding public key 'pk'
2. Use the keccak256 algorithm to calculate the hash value of the public key 'pk'
3. Take the last 160 bits as the Ethereum address

The user's private key and address together form the Ethereum account, which can store balances, initiate transactions, etc. (Bitcoin's balance is obtained by calculating all UTXOs, rather than being stored in the account like Ethereum).

In fact, Ethereum accounts are divided into two types. The above method generates what's called Externally Owned Accounts (EOA), which are regular user accounts mainly used to send/receive Ether tokens or send transactions to smart contracts (i.e., calling smart contracts).

The other type is Contract Accounts. Unlike external accounts, these accounts do not have corresponding private keys but are generated when deploying contracts and store smart contract code. It's worth noting that contract accounts must be called by external accounts or other contracts to send or receive Ether, and cannot initiate transactions on their own.

### Wallet

Software/plugins that store and manage Ethereum accounts are called wallets, providing functions such as transaction signing and balance management. Wallets are mainly generated in two ways: non-deterministic random generation or generation based on random seeds.

### Gas

Operations on the Ethereum network also require "fees", called Gas. Deploying smart contracts and transferring funds on the blockchain consume a certain amount of Gas. This is also an incentive mechanism to encourage miners to participate in building the Ethereum network, thereby making the entire network more secure and reliable.

Each transaction can set the corresponding Gas amount and Gas price. Setting a higher Gas fee often means miners will process your transaction faster, but to prevent transactions from consuming a large amount of Gas fee through multiple executions, you can set a limit through Gas Limit. Gas-related information can be queried through tools like the Ethereum Gas Tracker.

```sh
If START_GAS * GAS_PRICE > caller.balance, halt
Deduct START_GAS * GAS_PRICE from caller.balance
Set GAS = START_GAS
Run code, deducting from GAS
For negative values, add to GAS_REFUND
After termination, add GAS_REFUND to caller.balance
```

### Smart Contracts

As mentioned earlier, the Ethereum blockchain not only stores transaction information but also stores and executes smart contract code.

Smart contracts control application and transaction logic. In the Ethereum system, smart contracts use the proprietary Solidity language, with syntax similar to JavaScript. In addition, there are programming languages like Vyper and Bamboo. Smart contract code is compiled into bytecode and deployed to the blockchain, and once on-chain, it cannot be edited. The EVM, as a smart contract execution environment, can ensure the determinism of execution results.

#### Smart Contract Example: Crowdfunding

Let's imagine a more complex scenario. Suppose I want to crowdfund 10,000 yuan to develop a new product. Using existing crowdfunding platforms requires paying considerable fees and it's difficult to solve trust issues. Therefore, we can use a crowdfunding DApp to solve this problem.

First, let's set some rules for crowdfunding:

1. Each person who wants to participate in crowdfunding can donate an amount between 10-10,000 yuan
2. If the target amount is reached, the amount will be sent to me (the crowdfunding initiator) through a smart contract
3. If the target is not reached within a certain time (e.g., 1 month), the crowdfunding funds will be returned to the crowdfunding users
4. We can also set some rules, such as after a week, if the target amount is not reached, users can apply for a refund

Because these crowdfunding terms are implemented through smart contracts and deployed on the public blockchain, even the initiator cannot tamper with the terms, and anyone can view them, solving the trust issue.

You can view the complete code here: [Demo](https://www.toshblocks.com/solidity/complete-example-crowd-funding-smart-contract/)

### Transactions

What does a typical transaction in Ethereum look like?

1. Developers deploy smart contracts to the blockchain
2. DApp instantiates the contract, passes in corresponding values to execute the contract
3. DApp digitally signs the transaction
4. Local verification of the transaction
5. Broadcast the transaction to the network
6. Miner nodes receive the transaction and verify it
7. Miner nodes confirm trusted blocks and broadcast to the network
8. Local nodes synchronize with the network and receive new blocks

### Architecture

![ethereum_architecture_simple](https://image.pseudoyu.com/images/ethereum_architecture_simple.png)

Ethereum adopts an "Order - Execute - Validate - Update State" system architecture. Under this architecture, when a new transaction occurs, miners perform Proof of Work (PoW) calculations; after verification, they broadcast the block to the network through the gossip protocol; other nodes in the network receive the new block and also verify it; finally, it is submitted to the blockchain, updating the state.

Specifically, the Ethereum system has core components such as the consensus layer, data layer, and application layer. Their interaction logic is as follows:

![ethereum_architecture_concrete](https://image.pseudoyu.com/images/ethereum_architecture_concrete.png)

As shown in the above diagram, Ethereum data consists of Transaction Root and State Root. Transaction Root is a tree composed of all transactions, including From, To, Data, Value, Gas Limit, and Gas Price; while State Root is a tree composed of all accounts, including Address, Code, Storage, Balance, and Nonce.

## Conclusion

The above is an interpretation of Ethereum's core technologies. The introduction of smart contracts has brought more possibilities to blockchain applications, but there are still many security, privacy, and efficiency issues to consider. For complex enterprise-level application scenarios, consortium chains are a better choice. A detailed analysis of Hyperledger Fabric will be provided in the future, stay tuned!

## References

> 1. [COMP7408 Distributed Ledger and Blockchain Technology](https://msccs.cs.hku.hk/public/courses/2020/COMP7408A/), *Professor S.M. Yiu, HKU*
> 2. [Udacity Blockchain Developer Nanodegree](https://www.udacity.com/course/blockchain-developer-nanodegree--nd1309), *Udacity*
> 3. [Blockchain Technology and Applications](https://www.bilibili.com/video/BV1Vt411X7JF), *Xiao Zhen, Peking University*
> 4. [Advanced Blockchain Technology and Practice](https://www.ituring.com.cn/book/2434), *Cai Liang, Li Qilei, Liang Xiubo, Zhejiang University | Hyperchain Technology*
> 5. [Ethereum Architecture](https://www.zastrin.com/courses/ethereum-primer/lessons/1-5), *zastrin*
> 6. [Learn Solidity: Complete Example: Crowd Funding Smart Contract](https://www.toshblocks.com/solidity/complete-example-crowd-funding-smart-contract/), *TOSHBLOCKS*