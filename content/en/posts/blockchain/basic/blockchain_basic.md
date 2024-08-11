---
title: "Blockchain Fundamentals and Key Technologies"
date: 2021-02-12T12:12:17+08:00
draft: false
tags: ["blockchain", "guide", "knowledge"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

Recently, I've been taking the course `<COMP7408 Distributed Ledger and Blockchain Technology>` at HKU, which has given me a more systematic understanding of the basic concepts of blockchain. Combined with Professor Xiao Zhen's public course "[Blockchain Technology and Applications](https://www.bilibili.com/video/BV1Vt411X7JF)" from Peking University that I took previously, I've come to realize the vastness of the blockchain knowledge system. I plan to update a series of articles to systematically organize the knowledge of blockchain, Bitcoin, Ethereum, etc. If there are any errors or omissions, please feel free to discuss and correct them.

## Cryptographic Principles in Blockchain

Blockchain is closely related to cryptography, such as the core public-private key encryption technology, digital signatures, and hashing used in Bitcoin, including many consensus algorithms based on complex cryptographic concepts. Therefore, before starting to learn blockchain, we need to understand several core cryptographic concepts to gain a deeper understanding of their applications in the blockchain system.

### Hash Functions

A hash function is a method that transforms source data of arbitrary length into a fixed-length output value through a series of algorithms. The concept is simple, but its several characteristics make it widely used in various fields.

You can visit this [Demo](https://andersbrownworth.com/blockchain/hash) to experience how hash functions work (using `SHA256` as an example)!

The first characteristic is one-way irreversibility. It's easy to perform a hash operation on an input x to get the value H(x), but given a value H(x), it's almost impossible to reverse-engineer the value of x. This characteristic protects the source data well.

The second characteristic is collision resistance. Given a value x and another value y, if x is not equal to y, then H(x) is almost impossible to equal H(y). It's not completely impossible, but the probability is extremely low. Therefore, the hash value of a piece of data is almost unique, which can be well used in scenarios such as identity verification.

The third characteristic is that hash calculations are unpredictable. It's difficult to derive the hash value based on existing conditions, but it's easy to verify if it's correct. This mechanism is mainly applied in the `PoW` mining mechanism.

### Encryption/Decryption

Encryption mechanisms are mainly divided into two categories: symmetric encryption and asymmetric encryption.

Symmetric encryption mechanism is where both parties use the same key for information encryption and decryption. It's convenient and highly efficient, but there's a great risk in key distribution. If distributed through networks or other means, it's easy for the key to be leaked, leading to information leakage.

Asymmetric encryption mechanism mainly refers to the public-private key encryption mechanism. Each person generates a pair of keys through an algorithm, called the public key and the private key. If A wants to send a message to B, they can encrypt the file using B's public key and send the encrypted information to B. During this process, even if the information is intercepted or leaked, the source file will not be exposed, so it can be spread by any means. When B receives the encrypted file, they use their own private key for decryption to obtain the file content. B's private key has not been transmitted through any channel and is only known to themselves, so it has extremely high security.

In practical applications, asymmetric encryption of very large files is inefficient, so a combination mechanism is generally adopted: Suppose A wants to send a large file D to B, they first symmetrically encrypt file D with a key K, then asymmetrically encrypt key K with B's public key. A sends the encrypted key K and file D to B. Even if intercepted or leaked during transmission, because B's private key is not available, the key K cannot be obtained, and thus file D cannot be accessed. After B receives the encrypted file and key, they first decrypt with their private key to obtain key K, then use key K to decrypt file D, thereby obtaining the file content.

### Digital Signatures

Digital signatures are another use of asymmetric encryption mechanisms. As mentioned above, everyone has a pair of generated public and private keys. In encryption/decryption applications, the public key is used for encryption and the private key for decryption, while the digital signature mechanism is just the opposite. Suppose a file owner encrypts the file with their private key, others can decrypt it with their public key. If a result is obtained, it can prove the ownership of the file.

The most typical application of the digital signature mechanism is in the Bitcoin blockchain network, where private keys are used to prove ownership of bitcoins and sign transactions, while others can use public keys to verify whether the transaction is legal. The entire process does not require exposing one's private key, ensuring the security of assets.

## Basic Concepts of Blockchain

As history has progressed, people's bookkeeping methods have evolved from single-entry bookkeeping to double-entry bookkeeping, digital bookkeeping, and finally to distributed bookkeeping. Traditional centralized digital bookkeeping often relies on the credibility of certain organizations, posing some trust risks. Blockchain technology, in essence, is a distributed ledger technology where a group of people jointly maintain a decentralized database and use consensus mechanisms to keep accounts together. Blockchain makes it easy to trace historical records, and due to the existence of decentralized trust mechanisms, it is almost tamper-proof (or the cost of tampering far exceeds the benefits).

Compared to traditional databases, blockchain only has two operations: add and query. All historical records of operations are accurately preserved in the ledger and are immutable, providing high transparency and security. Of course, the trade-off is that all nodes must reach consensus through certain mechanisms (thus lower efficiency, unsuitable for real-time operations), and because each node must permanently store historical records, it occupies a large amount of storage space.

### Application Scenarios

> So how do we determine whether a company/business is suitable for adopting blockchain as a solution?

1. Is a database needed?
2. Is shared write access required?
3. Is multi-party trust establishment needed?
4. Can it operate without third-party institutions?
5. Can it operate without permission mechanisms?

Blockchain, as a distributed database, mainly does the work of information storage. Through its various mechanisms, it allows entities with common needs but not mutual trust to reach consensus at a relatively low cost without the intervention of third-party institutions, thereby meeting needs. In addition, the system also has features such as encrypted authentication and high transparency, which can meet some business needs. However, if the data involved cannot be made public, the data volume is very large, external services are needed to store data, or if business rules change frequently, then blockchain is not suitable as a solution.

> Therefore, under the above criteria, the following needs are very suitable for blockchain as a solution:

1. Need to establish a shared database with multiple parties involved
2. Parties involved in the business have not established trust
3. Existing business trusts one or more trust institutions
4. Existing business has encrypted authentication needs
5. Data needs to be integrated into different databases, and the need for business digitization and consistency is urgent
6. There are unified rules for system participants
7. Multi-party decision-making is transparent
8. Objective, immutable records are needed
9. Non-real-time business processing

But in fact, in many application scenarios, enterprises need to make some trade-offs between decentralization and efficiency. Sometimes many complex businesses have different requirements for transparency and rules. Therefore, based on complex commercial needs, there are also solutions like "consortium chains" that can better integrate with existing systems to meet business needs.

## Types of Blockchain

There are different types of blockchain, mainly private chains, public chains, and consortium chains.

Private chains are mainly applied to a specific field or only run within a certain enterprise, mainly used to solve trust issues, such as cross-departmental collaboration scenarios. Generally, external institutions do not need to access the data.

Public chains are open transactions, often used in businesses that require transaction/data disclosure, such as authentication, traceability, finance, and other scenarios, like Bitcoin, Ethereum, and `EOS`.

The biggest feature of consortium chains is that nodes need to verify permissions before participating in the blockchain network, and authentication is generally associated with their real-world roles. Therefore, consortium chains also have centralized attributes, but efficiency, scalability, and transaction privacy are greatly improved, meeting the needs of enterprise-level applications. The most widely used among them is `Hyperledger Fabric`. It's worth mentioning that consortium chains often do not need tokens as incentives, but use the participating nodes as bookkeeping nodes, and use the economic benefits brought by cross-departmental business collaboration through blockchain mechanisms as internal incentives, which is a healthier way that is more in line with enterprise applications.

In the long run, public chains and consortium chains will gradually converge in technology. Even for the same business, data that needs trust can be placed on public chains, while some industry data and private data can be placed on consortium chains, protecting transaction privacy through permission management.

## Basic Framework of Blockchain

> So what parts does a blockchain consist of?

1. Blocks
2. Blockchain
3. P2P network
4. Consensus mechanism
5. ...

### Blocks

The blockchain is an ecosystem composed of blocks. Each block contains the hash value of the previous block, timestamp, `Merkle Root`, `Nonce`, and block data. The block size of Bitcoin is 1 MB. You can visit this [Demo](https://andersbrownworth.com/blockchain/block) to experience the process of generating a block.

Because each block contains the hash value of the previous block, according to the hash properties mentioned earlier, even extremely small changes will result in completely different hash values, making it easy to detect whether a block has been tampered with. The Nonce value is mainly used to adjust the mining difficulty, controlling the time to about 10 minutes to ensure security.

### Blockchain

All blocks linked together form the blockchain, which is a ledger storing all historical transaction records in the network. Because each block contains the hash information of the previous block (for example, the Bitcoin system takes the block header of the previous block twice), if a transaction changes, it will cause the blockchain to break. There's a small [Demo](https://andersbrownworth.com/blockchain/blockchain) that demonstrates this process well, you can experience it!

### P2P Network

A P2P network is a type of distributed network used for sharing information and resources between different users. It's a distributed network where everyone can get a copy of the information and has access rights. In contrast, a centralized network is where everyone connects to one (or a group of) centralized network(s); a decentralized network has multiple such central networks, but no single-point network can have all the information. The following image explains well the differences between them:

![blockchain_network](https://image.pseudoyu.com/images/blockchain_network.png)

### Consensus Mechanism

The blockchain network is composed of multiple network nodes, each of which stores a copy of information. So how do they reach agreement on transactions? In other words, as independent nodes, they need a mechanism to ensure mutual trust, which is the consensus mechanism.

Common consensus mechanisms include `PoW (Proof of Work)`, `PoS (Proof of Stake)`, `DPoS (Delegated Proof of Stake)`, `DBFT (Delegated Byzantine Fault Tolerance)`, etc.

Bitcoin/Ethereum mainly adopts the proof of work mechanism, increasing the cost of malicious nodes through computing power competition. By dynamically adjusting the difficulty of mining, the time for a transaction is controlled to about 10 minutes (6 confirmations), but as Bitcoin mining becomes more and more popular, consuming more and more resources, it causes damage to the environment. Some mining pools with large resources may also cause some centralization risks.

The proof of stake mechanism reaches consensus through voting by stake (usually token) holders. This mechanism does not require a large amount of computing power competition like proof of work, but it also has some risks, called the `Nothing at Stake` problem, where many stake holders will bet on all blocks and profit from them. To solve this problem, the system sets some rules, such as setting some punishment mechanisms for users who create blocks on multiple chains simultaneously or create blocks on wrong chains. Ethereum is currently transitioning to this consensus mechanism.

`EOS` adopts delegated proof of stake, selecting some representative nodes for voting. This method aims to optimize the efficiency and results of community voting, but it brings some centralization risks.

The `DBFT` consensus mechanism reaches consensus by assigning different roles to nodes, which can greatly reduce overhead and avoid forks, but there is also a risk of core roles acting maliciously.

## Blockchain Security and Privacy

### Security

As a relatively new technology, blockchain also has many security vulnerabilities, such as attacks on cryptocurrency exchanges, smart contract vulnerabilities, attacks on consensus protocols, attacks on network traffic (Internet ISP), and uploading malicious data. Famous cases include the Mt.Gox incident and the Ethereum DAO incident. Therefore, the security risks of blockchain are also an important research direction for blockchain.

Risk analysis can be conducted from the perspectives of protocols, encryption schemes, applications, program development, and systems to improve the security of blockchain applications. For example, in the Ethereum blockchain, analysis can be performed on the `Solidity` programming language, `EVM`, and the blockchain itself.

For example, a type of attack called low-cost attack in smart contracts is to identify operations with relatively low `Gas` fees in the Ethereum network and repeatedly execute them to disrupt the entire network.

For security issues, building a general code detector to check for malicious code would be a more universal solution.

### Privacy

When discussing blockchain concepts, we mentioned one of its important features: privacy. That is, everyone can see the transaction details and historical records on the chain. This feature is mainly applied in supply chain links such as food and medicine, but for some financial scenarios, such as personal account balances and transaction information, it can easily cause some privacy risks.

> So what technologies can be applied to protect privacy in these high-value, sensitive information scenarios?

At the hardware level, trusted execution environments can be adopted, using some secure hardware such as `Intel SGX`, which greatly ensures privacy; the network can adopt multi-path forwarding to avoid inferring real identities from node IP addresses.

At the technical level, coin mixing technology can mix many transactions, making it difficult to find out the corresponding transaction sender and receiver; blind signature technology can ensure that third-party institutions cannot link the parties involved in the transaction; ring signatures are used to ensure the anonymity of transaction signatures; zero-knowledge proofs can be applied to one party (prover) proving to another party (verifier) that a statement is correct without revealing any information other than the fact that the statement is correct; homomorphic encryption can protect the original data, given E(x) and E(y), it's easy to calculate some encrypted function values about x and y (homomorphic operations); attribute-based encryption (ABE) adds some attributes/roles to each node, implementing permission control, thereby protecting privacy.

It's worth noting that even if a transaction generates multiple inputs and outputs, the addresses of these inputs and outputs may still be associated by people; in addition, address accounts and real-world identities may also be associated.

## Conclusion

The above is a summary of the basic knowledge of blockchain, mainly focusing on concepts and principles. In the future, I will update analyses and thoughts on typical applications such as Bitcoin, Ethereum, `Hyperledger Fabric`, and explore hot technologies such as IPFS, cross-chain, NFT, etc. Stay tuned!

## References

> 1. [COMP7408 Distributed Ledger and Blockchain Technology](https://msccs.cs.hku.hk/public/courses/2020/COMP7408A/), *Professor S.M. Yiu, HKU*
> 2. [Udacity Blockchain Developer Nanodegree](https://www.udacity.com/course/blockchain-developer-nanodegree--nd1309), *Udacity*
> 3. [Blockchain Technology and Applications](https://www.bilibili.com/video/BV1Vt411X7JF), *Xiao Zhen, Peking University*
> 4. [Advanced Blockchain Technology and Practice](https://www.ituring.com.cn/book/2434), *Cai Liang, Li Qilei, Liang Xiubo, Zhejiang University | Hyperchain*