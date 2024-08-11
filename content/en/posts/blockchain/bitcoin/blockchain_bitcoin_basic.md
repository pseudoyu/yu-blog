---
title: "Bitcoin Core Technology Interpretation"
date: 2021-02-17T12:12:17+08:00
draft: false
tags: ["blockchain", "bitcoin"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

In the previous article "[Blockchain Fundamentals and Key Technologies](https://www.pseudoyu.com/en/2021/02/12/blockchain_basic/)", I outlined the basic knowledge and key technologies of blockchain. As Bitcoin is the most typical application of blockchain, this article will interpret the core technologies of Bitcoin. If there are any errors or omissions, please feel free to discuss and correct them.

## Bitcoin System

Bitcoin is a digital currency invented by Satoshi Nakamoto in 2009, mainly to counter the centralized banking system. Due to its ingenious system design and security, its value has been rapidly increasing. At the same time, because it is not tied to real-world identities, it has strong anonymity and has also been used for illegal transactions, money laundering, extortion, and other malicious activities, causing some controversy.

As a decentralized blockchain system, everyone can access it and maintain a node locally to participate in the Bitcoin network. The following text will also use the Bitcoin Core client to maintain a node locally.

![bitcoin_network_nodes](https://image.pseudoyu.com/images/bitcoin_network_nodes.png)

Nodes are divided into full nodes and light nodes. In the early days, all nodes were full nodes, but as the amount of data grew larger, Bitcoin clients running on devices such as mobile phones or tablets do not need to store information about the entire blockchain. These are called Simplified Payment Verification (SPV) nodes, or light nodes.

The Bitcoin Core client is a full node, which will be discussed in detail below. Full nodes are always online, maintaining complete blockchain information. Because they maintain a complete set of UTXOs in memory, they can verify the legitimacy of transactions by verifying the block and transaction information of the entire blockchain (from the genesis block to the latest block). They also decide which transactions will be packaged into blocks. Verifying transactions, i.e., mining, can decide which chain to continue mining on, and in the case of equal-length forks, can choose which fork to follow. They also monitor blocks mined by other miners and verify their legitimacy.

Light nodes do not need to be online all the time, nor do they need to retain the entire blockchain (which is a large amount of data). They only need to keep the block headers of each block and only need to save the blocks related to themselves, rather than all transactions on the chain. Because they do not save all the information, they cannot verify the legitimacy of most transactions and the correctness of new blocks published online. They can only check the blocks related to themselves. They can verify the existence of a transaction through Merkle Proof, but cannot confirm that a transaction does not exist. They can verify the difficulty of mining because it is stored in the block header.

> Let's explain the transaction verification methods of full nodes and light nodes through an example.

Suppose we need to verify a transaction T located in block 300,000. A full node would examine all 300,000 blocks (up to the genesis block), building a complete UTXO database to ensure this transaction has not been spent. A light node, on the other hand, would use the Merkle Path to link all blocks related to transaction T, then wait for blocks 300,001 to 300,006 for confirmation, thereby verifying the legitimacy of the transaction.

### Blockchain Structure

Blockchain is a data structure composed of sequentially linked blocks, which can be stored in a single file or database. The Bitcoin Client uses Google's LevelDB database to store data. Each block points to the previous block. If any block is modified, all subsequent blocks will be affected. Therefore, to tamper with a block, one needs to tamper with all subsequent blocks simultaneously, which requires a large amount of computing power. Often, the cost outweighs the benefit, thus greatly ensuring security.

The blockchain structure includes several core components: Block Size (4 bytes), Block Header, Transaction Counter (1-9 bytes), and Transactions.

The block header size is 80 bytes, storing Version (4 bytes), Previous Block Hash (32 bytes), Merkle Tree Root (32 bytes), Timestamp (4 bytes), Difficulty Target (4 bytes), and Nonce (4 bytes).

The hash value of each block is obtained by performing a double hash operation on the block header, i.e., SHA256(SHA256(Block Header)). It does not exist in the blockchain structure but is calculated by each node after receiving the block and is unique. In addition, Block Height can also serve as an identifier for the block.

#### Merkle Tree

The Merkle Tree is a very important data structure in blockchain, mainly used to verify larger data sets through hash algorithms (also through a double hash method SHA256(SHA256(Block Header))). The structure is shown in the following diagram:

![merkle_tree_example](https://image.pseudoyu.com/images/merkle_tree_example.png)

Using the Merkle Tree method, one can quickly verify that a transaction exists in a certain block (with an algorithm complexity of LogN). For example, to verify that a transaction K exists in a block, only a few nodes need to be accessed.

![merkle_proof_example](https://image.pseudoyu.com/images/merkle_proof_example.png)

Because there are a large number of transactions in the Bitcoin network, this method can greatly improve efficiency, as shown in the following diagram:

![merkle_proof_efficiency](https://image.pseudoyu.com/images/merkle_proof_efficiency.png)

Because light nodes (such as Bitcoin wallets on mobile phones) do not save the entire blockchain data, transactions can be easily found through the Merkle Tree structure. Light nodes will construct a Bloom filter to obtain transactions related to themselves:
1. First, initialize the Bloom filter to an empty value, get all addresses in the wallet, create a retrieval pattern to match the addresses related to this transaction output, and add the retrieval pattern to the Bloom filter;
2. Then the Bloom filter is sent to various nodes (via the filterload message);
3. After receiving it, the node will send a merkleblock message containing the block headers that meet the conditions and the Merkle Path of the matching transactions, and a tx message containing the filtering results.

During the process, the light node will use the Merkle Path to link transactions with blocks, and use block headers to form the blockchain, thus being able to verify that transactions exist in the blockchain.

Using a Bloom filter will return results that meet the screening conditions, and there will also be some false positives, so many irrelevant results are returned, which can also protect privacy when light nodes request relevant addresses from other nodes.

### Bitcoin Network

The Bitcoin system runs on a P2P peer-to-peer network, where nodes are equal, without distinction of identity or permissions; there are no centralized servers, and the network has no hierarchical distinctions.

Each node needs to maintain a set of transactions waiting to be chained. Each block is 1M in size, so it takes a few seconds to pass to most nodes. Suppose a node monitors a transaction from A to B, it will write it into the set. If it simultaneously discovers a double-spending attack from A to C, it will not write it in. If it monitors the same A to B transaction or an A to C transaction from the same coin source, it will delete the A to B transaction in that set.

### Bitcoin Consensus Protocol

As an open system that anyone can participate in, Bitcoin needs to solve the threat of malicious nodes. The solution is the proof-of-work mechanism, which is also known as the computing power voting mechanism. When a new transaction occurs, new data records are broadcast, and the whole network executes the consensus algorithm. Miners mine to verify the records, i.e., solve for random numbers. The miner who first solves the puzzle gets the right to record, generates a new block, then broadcasts the new block externally. After other nodes verify and pass, it is added to the main chain.

### Wallet

As a digital currency system, Bitcoin has its own wallet system, mainly composed of three parts: private key, public key, and wallet address.

> The process of generating a wallet address is as follows:

1. Using the ECDSA (Elliptic Curve Digital Signature Algorithm), generate the corresponding public key using the private key.
2. The public key is long and difficult to input and remember, so a public key hash value is obtained through SHA256 and RIPEMD160 algorithms.
3. Finally, it is processed with Base58Check to obtain a more readable wallet address.

### Transaction Process

With a wallet (and assets), you can start trading. Let's understand this process through a typical Bitcoin transaction:

A and B both have a Bitcoin wallet address (which can be generated by Bitcoin Client, the principle is as above). Suppose A wants to transfer 5 BTC to B. A needs to get B's wallet address, then use their own private key to sign the transaction "A transfers 5 BTC to B" (because only A knows their private key, having the private key is equivalent to owning the wallet assets). Then publish this transaction. In the Bitcoin system, initiating a transaction requires paying a small miner fee as a transaction fee. Miners will start verifying the legitimacy of this transaction. After six confirmations, the transaction can be accepted by the Bitcoin ledger. The entire verification process takes about 10 minutes.

> Why do miners consume a large amount of computing power to verify transactions?

Miners can get block rewards and miner fees during the verification process. Block rewards will decrease every four years, so in the later stages, the main incentive is miner fees.

> Why does verification take 10 minutes?

Bitcoin is not absolutely secure. New transactions are susceptible to some malicious attacks. By controlling the mining difficulty to control the verification process to about 10 minutes, malicious attacks can be prevented to a large extent. This is just a probabilistic guarantee.

> How does the Bitcoin system avoid double spending?

Bitcoin adopted a concept called UTXO (Unspent Transaction Outputs). When a user receives a BTC transaction, it is recorded in the UTXO.

In this example, A wants to transfer 5 BTC to B. A's 5 BTC might come from two UTXOs (2 BTC + 3 BTC). Therefore, when A transfers to B, what the miner needs to check is whether these two UTXOs have been spent before this transaction. If they detect that it has already been spent, then the transaction is invalid.

The following diagram well illustrates the flow of multiple transactions and the related concept of UTXO

![btc_utxo_example](https://image.pseudoyu.com/images/btc_utxo_example.png)

In addition, UTXO has a very important characteristic: it is indivisible. Suppose A has 20 BTC and wants to transfer 5 BTC to B. The transaction will first take 20 BTC as input, then produce two outputs, one transferring 5 BTC to B, and one returning the remaining 15 BTC to A. Therefore, A now owns a UTXO worth 15 BTC. If a single UTXO is not enough to pay, multiple UTXOs can be combined to form an input, but the total must be greater than the transaction amount.

> How do miners verify that the transaction initiator has sufficient balance?

This question seems simple at first glance. The first reaction might be to check if the balance is sufficient, like Alipay does. However, Bitcoin is a transaction-based ledger model without the concept of accounts. Therefore, balance cannot be directly queried. To know the remaining assets of an account, one needs to review all previous transactions and find and add up all UTXOs.

### Transaction Model

> We've discussed how a transaction occurs, but what parts make up a Bitcoin transaction?

![blockchain_bitcoin_script_detail](https://image.pseudoyu.com/images/blockchain_bitcoin_script_detail.png)

As shown in the figure, the first part is Version, indicating the version.

Then comes the information related to Input: Input Count indicates the number, and Input Info indicates the content of the input, which is the Unlocking Script, mainly used to check the source of the input, whether the input is available, and other input details.
- Previous output hash - All inputs can be traced back to an output. This points to the UTXO that will be spent in that input. The hash value of this UTXO is stored here in reverse order.
- Previous output index - A transaction can have multiple UTXOs referenced by their index numbers. The first index is 0.
- Unlocking Script Size - The byte size of the Unlocking Script.
- Unlocking Script - The hash that satisfies the UTXO Unlocking Script.
- Sequence Number - Default is ffffffff.

Next is the information related to Output. Output Count indicates the number, and Output Info indicates the content of the output, which is the Locking Script, mainly used to record how many bitcoins were output, the conditions for future expenditure, and output details.
- Amount - The amount of bitcoin output expressed in Satoshis (the smallest unit of bitcoin). 10^8 Satoshis = 1 bitcoin.
- Locking Script Size - This is the byte size of the Locking Script.
- Locking Script - This is the hash of the Locking Script, which specifies the conditions that must be met to use this output.

Finally, there's Locktime, which indicates the earliest time/block a transaction can be added to the blockchain. If it's less than 500 million, it directly reads the block height, and if it's greater than 500 million, it reads the timestamp.

### Bitcoin Script

In the transaction, we mentioned Unlocking script and Locking script. So what is a Bitcoin script?

Bitcoin script is a list of instructions recorded in each transaction. When the script is executed, it can check whether the transaction is valid, whether the bitcoin can be used, etc. A typical script looks like this:

```sh
<sig> <pubKey> OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

Bitcoin script is executed from left to right based on a stack, using Opcodes to operate on the data. In this script language, data enclosed in <> is to be pushed onto the stack, those without <> and prefixed with OP_ are operators (OP can be omitted). Scripts can also embed data permanently recorded on the chain (not exceeding 40 bytes), and the recorded data does not affect UTXO.

In a transaction, `<sig> <pubKey>` is the Unlocking script, and `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` is the Locking script.

Compared to most programming languages, Bitcoin script is not Turing-complete. It has no loops or complex flow control, is simple to execute, produces deterministic results no matter where it's executed, and doesn't save state. Moreover, scripts are independent of each other. Because of these characteristics, although Bitcoin script is relatively safe, it cannot handle very complex logic, so it is not suitable for handling some complex business. Ethereum's smart contracts made innovative breakthroughs in this aspect, thus giving birth to many decentralized applications.

### Mining

We mentioned mining in the previous discussion of the entire transaction process. Let's discuss it in detail now.

Some nodes, in order to obtain block rewards and miner fees and earn profits, will verify transactions, which is called mining. Block rewards are created by coinbase and decrease every four years, from 25 in 2009 to 6.5 now.

Mining is actually a process of constantly trying random numbers to reach a certain set target value, such as less than a certain target value. This difficulty is artificially set to adjust the verification time and enhance security, not to solve mathematical problems.

Miners will constantly try this value. The success rate is very low, but the number of attempts can be very high. Therefore, nodes with stronger computing power have a proportional advantage and are more likely to solve the puzzle.

> Why does the mining difficulty need to be adjusted?

In the Bitcoin system, if the block time is too short, it's easy to produce forks. If there are too many forks, it will affect the system's ability to reach consensus, endangering system security. The Bitcoin system adjusts the difficulty to stabilize the block generation speed at around 10 minutes, thereby preventing transactions from being tampered with.

> How is the mining difficulty adjusted?

The system adjusts the target threshold every 2016 blocks (about two weeks), stored in the block header. All nodes across the network need to follow the new difficulty for mining. If malicious nodes do not adjust the target in their code, honest miners will not recognize it.

Target threshold = Target threshold * (Actual time to produce 2016 blocks / Expected time to produce 2016 blocks)

When Bitcoin was first born, there were few miners and the mining difficulty was relatively low. Most mining was done directly using home computers (CPUs). As more and more people participated in the Bitcoin ecosystem, the difficulty of mining increased. Gradually, people started using some GPUs with stronger computing power for mining. Some specialized ASIC (Application Specific Integrated Circuit) mining chips and mining machines have also gradually emerged in response to market demand. Now, there are also many large mining pools that combine a large amount of computing power across the network for centralized mining.

In this large mining pool system, the Pool Manager acts as a full node, while the large number of gathered miners calculate hash values together, and finally distribute profits through the proof of work mechanism. However, if computing power is too concentrated, it can easily produce some centralization risks. For example, if a large mining pool reaches more than 51% of the network's computing power, it could roll back transactions or boycott certain transactions.

### Forks

In the Bitcoin system, there can also be situations where consensus is not reached, called forks. Forks are mainly divided into two types: one is a state fork, which is often deliberately carried out by some nodes; the other is called a protocol fork, which means there are some disagreements about the Bitcoin protocol.

Protocol forks can be further divided into two types. One is called a hard fork, which means incompatible changes have been made to parts of the protocol. For example, changing the block size of Bitcoin from 1M to 4M. This type of fork is permanent, forming two parallel chains developing from a certain node, such as Bitcoin Classic, resulting in two types of coins.

The other is called a soft fork. For example, still adjusting the block size of Bitcoin, but from 1M to 0.5M. After such an adjustment, there will be a situation where new nodes mine small blocks and old nodes mine large blocks. Soft forks are non-permanent. Typical examples include modifying the content of coinbase and the fork produced by P2SH (Pay to Script Hash).

## Bitcoin Core Client

Bitcoin Core is the implementation of Bitcoin, also known as Bitcoin-QT or Satoshi-client. Through this client, you can connect to the Bitcoin network, verify the blockchain, send and receive bitcoins, etc. There are three networks: Mainnet, Testnet, and Regnet, which can be switched between.

It provides a Debug Console to interact directly with the Bitcoin blockchain. Common operations are as follows:

> Blockchain

- getblockchaininfo: Returns various state information about blockchain processing
- getblockcount: Returns the number of blocks in the blockchain
- verifychain: Verifies blockchain database

> Hash

- getblockhash: Returns the hash of the provided block
- getnetworkhashps: Returns the estimated network hashes per second based on the last n blocks
- getbestblockhash: Returns the hash of the best (tip) block in the longest blockchain

> Blocks

- getblock: Returns detailed information about a block
- getblockheader: Returns information about block header
- generate: Immediately mine the specified number of blocks to a wallet address

> Wallet

- getwalletinfo: Returns an object containing various wallet state info
- listwallets: Returns a list of currently loaded wallets
- walletpassphrasechange: Changes the wallet passphrase

> Mempool

- getmempoolinfo: Returns details on the active state of the TX memory pool
- getrawmempool: Returns all transaction ids in memory pool
- getmempoolentry: Returns mempool data for given transaction

> Transaction

- getchaintxstats: Compute statistics about the total number and rate of transactions in the chain
- getrawtransaction: Returns raw transaction data
- listtransactions: Returns list of transactions for given account

> Signature

- signrawtransaction: Sign inputs for raw transaction
- signmessage: Sign a message with the private key of an address
- dumpprivkey: Reveals the private key corresponding to an address

> Network

- getnetworkinfo: Returns an object containing various state info regarding P2P networking
- getpeerinfo: Returns data about each connected network node
- getconnectioncount: Returns the number of connections to other nodes

> Mining

- getmininginfo: Returns an object containing mining-related information
- getblocktemplate: Returns data needed to construct a block to work on
- prioritisetransaction: Accepts or prioritizes a transaction in the mempool for mining

## Conclusion

The above is an interpretation of Bitcoin's core technology, mainly focusing on its basic principles and data model. Through the study of Bitcoin, we can better understand the design philosophy and operational mechanism of blockchain. Next, we will study and analyze Ethereum, which is known as Blockchain 2.0. Stay tuned!

## References

> 1. [COMP7408 Distributed Ledger and Blockchain Technology](https://msccs.cs.hku.hk/public/courses/2020/COMP7408A/), *Professor S.M. Yiu, HKU*
> 2. [Udacity Blockchain Developer Nanodegree](https://www.udacity.com/course/blockchain-developer-nanodegree--nd1309), *Udacity*
> 3. [Blockchain Technology and Applications](https://www.bilibili.com/video/BV1Vt411X7JF), *Xiao Zhen, Peking University*
> 4. [Blockchain Technology: Advanced and Practice](https://www.ituring.com.cn/book/2434), *Cai Liang, Li Qilei, Liang Xiubo, Zhejiang University | Hyperchain Technology*