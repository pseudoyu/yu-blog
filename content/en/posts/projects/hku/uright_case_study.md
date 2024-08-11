---
title: "Uright - Blockchain Music Copyright Management ÐApp"
date: 2021-05-10T19:30:25+08:00
draft: false
tags: ["blockchain", "ethereum", "ipfs", "hku"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

# Uright - Blockchain Music Copyright Management ÐApp

![uright_chain](https://image.pseudoyu.com/images/uright_chain.png)

### Introduction

A music copyright management Decentralized Application (ÐApp) based on Angular+Solidity+Web3.js, applying technologies such as IPFS, ENS, and Oracles, deployed on Ethereum using Truffle.

The Uright decentralized application allows musicians (content owners) to register their works as "Manifestations" and record them on the Ethereum blockchain.

"Manifestations" present musicians' works as content fragments to prove authorship and ownership. This is accomplished through the "Manifestations" smart contract, which records the IPFS hash displaying the work's content, title (planned additional metadata), and registration time. This information can be used to prove authorship, and the content can be retrieved from the IPFS file storage system.

However, merely registering a "Manifestation" is insufficient; supporting materials should be provided, otherwise the "Manifestation" will expire after one day. These supporting materials are typically registered by the musician (work uploader), but anyone can add supporting materials. Supporting materials can be any type of file, such as screenshots or PDF documents. The "UploadEvidences" smart contract uploads the supporting materials to the IPFS file system.

Additionally, the "YouTubeEvidences" smart contract allows musicians to declare their work "Manifestations" in the upload description on platforms like YouTube, and the smart contract will automatically detect it as supporting material.

(In development...) If someone else has already registered a musician's original work/supporting material, the musician can file an appeal. The contract functionality has been implemented but is not yet available in the Web application.

(In development...) Tokenization of musicians' works using NFT technology.

Project address: [GitHub](https://github.com/pseudoyu/uright)

### Architecture

![uright_architecture](https://image.pseudoyu.com/images/uright_architecture.png)

### Core Technologies

#### IPFS

When musicians register their works using digital files (such as .mp3 format files), the files are uploaded to IPFS, and the generated IPFS identifier (hash value) is used to register the work on the Ethereum blockchain. Users can choose to upload their works to the IPFS network or keep them private by setting the content not to be uploaded to the IPFS network, generating only the work's hash value.

Users need to retain the exact same file used to generate the work's hash, which can be used later as evidence of owning the digital file for hash verification. The IPFS hash value will also be used to retrieve the uploaded content.

#### Ethereum Naming System (ENS)

The Uright project integrates the ethereum-ens package, which can be used on the Ethereum mainnet, Ropsten, Rinkeby test networks, and local test networks. The ensdomains/ens package is used to set address names.

#### Oracles

The Oracle module is integrated into the smart contract for uploading YouTube evidence. It uses the YouTube video ID (https://www.youtube.com/watch?v=VIDEO_ID) to retrieve whether the video description contains a specific work hash.

This feature allows musicians to prove that the work exists on the YouTube platform and belongs to them (since only the uploader can edit the video description to include the work's hash value).

The online service provided by Oraclize can be used for queries: http://app.oraclize.it/home/test_query

#### Upgradability

To make the work registration contract upgradable, the AdminUpgradeabilityProxy from ZeppelinOS was introduced, implementing the delegation pattern through relay proxies.

### Design Patterns

![uright_design_architecture](https://image.pseudoyu.com/images/uright_design_architecture.png)

The smart contract design of the Uright project facilitates modularity and reusability. For example, the validation expiration functionality is implemented as an entity library; and the "Evidencable" library allows registered works to accumulate multiple supporting materials, which can also provide convenience in subsequent appeal function development.

Moreover, providing these functionalities as libraries can reduce deployment costs.

#### Circuit Breaker Pattern / Emergency Stop

The circuit breaker pattern can prevent an application from repeatedly attempting to execute an operation that is likely to fail, allowing it to continue without waiting for the failure to be corrected or wasting processor cycles while it determines that the failure is long-lasting. The circuit breaker pattern also enables an application to detect whether the failure has been resolved. If a problem occurs, the application can attempt to call the operation.

#### Automatic Deprecation

Furthermore, a pattern similar to "Automatic Deprecation" is implemented for registered works. Thus, if a user registers a work but does not provide supporting materials, their registration will expire after a set fixed time. In this case, expiration means that the work can be re-registered and overwritten by another user.

### Security Measures

All smart contracts have been code-checked using Remix and Solhint tools. These two tools check for common security issues such as reentrancy or timestamp dependency.

The SafeMath library is used to avoid integer overflow and underflow issues.

Finally, Solhint is set as a step in the defined continuous integration and deployment workflow. This way, every time code is pushed to GitHub, travis runs all tests (for contracts and Angular frontend), and if all tests pass, it is responsible for deployment.

Additionally, the Solhint tool is also executed before testing to track any potential security issues that may arise.

### Related Libraries

The Uright project imports some libraries from ZeppelinOS and OpenZeppelin packages for functionality implementation.

#### ZeppelinOS

- AdminUpgradeabilityProxy: Implements smart contract upgradability
- Initializable: Implements proxy initialization through upgradable smart contracts

#### OpenZeppelin

- Pausable: Implements the "Circuit Breaker Pattern / Emergency Stop" design pattern, extending Ownable to ensure only the owner can stop
- SafeMath: Used to avoid integer overflow and underflow issues
- OraclizeAPI package, usingOraclize, used to verify if a YouTube video belongs to a specific user and is bound to a copyrighted work

### Smart Contract Details

#### Manifestations.sol

This smart contract is used for work registration, associating the work's metadata (currently the title) and the IPFS hash of the content with the author's identity (i.e., Ethereum account address) to prove work ownership. The same work can be declared as having a single author or joint authors. Additionally, if attempting to re-register a new work with an already registered content hash, the system will detect it as a failure.

#### UploadEvidences.sol

This smart contract is mainly used for supporting material registration, registering evidence by uploading the work file content to the IPFS file system. Multiple pieces of evidence can be added for the same work (but cannot be added repeatedly).

#### ExpirableLib.sol

This smart contract is primarily used to manage the project logic for work creation and expiration times, implementing the time-effectiveness of work registration (or appeals).

### Features

The Uright ÐApp provides music copyright management services to musicians and users through a Web client.

1. Copyright Registration: Generate a unique hash value from the work file, register the musician's work on the blockchain to prove copyright ownership.

![uright_register](https://image.pseudoyu.com/images/uright_register.png)

- Register new works that have never been registered
- Register works with existing registration records and file appeals
- Add supporting materials to prove work copyright

![uright_evidence_upload](https://image.pseudoyu.com/images/uright_evidence_upload.png)

![uright_youtube_evidence](https://image.pseudoyu.com/images/uright_youtube_evidence.png)

2. Copyright Retrieval: Check if a work has been registered using its hash value

![uright_music_search](https://image.pseudoyu.com/images/uright_music_search.png)

- My Works: Find all registered works of the current musician
- Copyright Library: Find all registered works on the blockchain
- Details: Click "Details" to view detailed information, including all uploaded evidence

![uright_music_library](https://image.pseudoyu.com/images/uright_music_library.png)