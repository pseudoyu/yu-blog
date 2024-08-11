---
title: "Solidity Smart Contract Development - Mastering ethers.js"
date: 2022-06-08T00:25:45+08:00
draft: false
tags: ["blockchain", "solidity", "ethereum", "web3", "smart contract", "javascript", "ethers.js"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《後來的我們 - 五月天》" >}}

## Preface

In the previous article "[Solidity Smart Contract Development - Basics](https://www.pseudoyu.com/en/2022/05/25/learn_solidity_from_scratch_basic/)", we learned the basic syntax of Solidity and understood that we can debug using frameworks like [Brownie](https://github.com/eth-brownie/brownie) and [HardHat](https://github.com/NomicFoundation/hardhat). In another article "[Solidity Smart Contract Development - Mastering Web3.py](https://www.pseudoyu.com/en/2022/05/30/learn_solidity_from_scratch_web3py/)", we also interacted directly with our local Ganache node using Web3.py.

Originally, because I was more familiar with Python, I planned to use the Brownie framework for subsequent development. However, after some research, I found that the industry predominantly uses the HardHat framework, which also has more extensions. Additionally, the Solidity tutorial I'm following has updated to a [Javascript version](https://www.youtube.com/watch?v=gyMwXuJrbJQ), so I decided to learn it.

To better understand the principles and lay a good foundation for our subsequent use of the framework, this time we will use [ethers.js](https://github.com/ethers-io/ethers.js/) to interact with our Rinkeby test network deployed on the [Alchemy](https://dashboard.alchemyapi.io) platform. We will implement basic contract compilation, deployment to the Rinkeby network, and interaction with the contract.

You can click [here](https://github.com/pseudoyu/learn-solidity/tree/master/ethers_simple_storage) to access the code repository for this test demo.

## ethers.js

ethers.js is an open-source library for Javascript that can interact with the Ethereum network. Its GitHub address is [ethers.io/ethers.js](https://github.com/ethers-io/ethers.js/), and you can visit its [official documentation](https://docs.ethers.io/) for usage.

### Installation

We can install `ethers.js` using yarn, as follows:

```bash
yarn add ethers
```

![yarn_add_ethers](https://image.pseudoyu.com/images/yarn_add_ethers.png)

### Usage

Import the library using `require` to use it

```javascript
const ethers = require('ethers');
```

## Solidity Contract Compilation

### Contract Source Code

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

contract SimpleStorage {
    uint256 favoriteNumber;
    bool favoriteBool;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People public person = People({favoriteNumber: 2, name: "Arthur"});

    People[] public people;

    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public returns (uint256) {
        favoriteNumber = _favoriteNumber;
        return favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
```

This is a simple storage contract that uses a People struct object to store a person's name and their favorite number, uses an array to store information for multiple people, and provides methods for adding and searching.

### Reading the Contract Source File

After completing the Solidity contract writing and syntax checking through VSCode or other editors, we need to compile the contract into abi file and bytecode.

We can install the `solc` command-line tool through `yarn` for editing, and we can choose the corresponding version. The command is as follows:

```bash
yarn add solc@0.8.7-fixed
```

After installation, we can use the `solcjs` command for compilation. The command is as follows:

```bash
yarn solcjs --bin --abi --include-path node_modules/ --base-path . -o . SimpleStorage.sol
```

Since compiling contracts is a high-frequency operation, we can configure the `compile` script command in `package.json` as follows:

```json
"scripts": {
    "compile": "yarn solcjs --bin --abi --include-path node_modules/ --base-path . -o . SimpleStorage.sol"
}
```

After that, you only need to execute `yarn compile` to generate the contract compilation files.

### Obtaining Compilation Results

After compilation, abi and bytecode files will be generated, with `.bin` and `.abi` as suffixes respectively.

#### Obtaining bytecode and abi

The deployment and interaction of Solidity contracts require two parts: bytecode and abi. We can write them into corresponding variables for subsequent operations through the following code.

```javascript
const fs = require('fs-extra');

const abi = fs.readFileSync("./SimpleStorage_sol_SimpleStorage.abi", "utf-8");
const binary = fs.readFileSync("./SimpleStorage_sol_SimpleStorage.bin", "utf-8");
```

## Creating a Rinkeby Test Network Environment (Alchemy)

Debugging smart contracts requires deploying the contract to an actual chain. We choose to deploy to the Rinkeby test network on the Alchemy platform for subsequent debugging and development.

### Alchemy Platform

First, we visit the [Alchemy official website](https://dashboard.alchemyapi.io), register and log in, and we will see its Dashboard, which displays all created applications.

![alchemy_dashboard](https://image.pseudoyu.com/images/alchemy_dashboard.png)

After installation, select Create App to quickly create a Rinkeby test network node.

![alchemy_create_app](https://image.pseudoyu.com/images/alchemy_create_app.png)

After creation, click View Details to see the detailed information of the App we just created. Click View Key in the upper right corner to query our node information. We need to record the HTTP URL for subsequent connection use.

![alchemy_app_detail](https://image.pseudoyu.com/images/alchemy_app_detail.png)

## Creating a Rinkeby Test Account (MetaMask)

### MetaMask

After creating the Rinkeby test network environment, we need to create an account through MetaMask, get some test tokens, and record the account's private key for later use.

![metamask_private_key](https://image.pseudoyu.com/images/metamask_private_key.png)

### Obtaining Test Tokens

After creating an account, we need some test tokens for subsequent development and debugging. We can obtain them through the following URLs:

- https://faucets.chain.link
- https://rinkebyfaucet.com/

## Connecting to Test Node and Wallet

### Connecting to Node

`ethers.js` provides a library that can easily connect to our test node, where `process.env.ALCHEMY_RPC_URL` is the HTTP URL of the App we created on the Alchemy platform:

```javascript
const ethers = require('ethers');

const provider = new ethers.providers.JsonRpcProvider(process.env.ALCHEMY_RPC_URL);
```

### Connecting to Wallet

`ethers.js` also provides a method to connect to our test wallet, where `process.env.RINKEBY_PRIVATE_KEY` is the private key we copied from MetaMask.

```javascript
const ethers = require('ethers');

const wallet = new ethers.Wallet(
	process.env.RINKEBY_PRIVATE_KEY,
	provider
);
```

## Solidity Contract Deployment

### Creating Contract

We can create a contract through the `ethers.js` library.

```javascript
const contractFactory = new ethers.ContractFactory(abi, binary, wallet);
```

### Deploying Contract

Below we will introduce how to deploy a contract through the `ethers.js` library, where the ABI and BIN files of the `SimpleStorage` contract have been read in the code above.

#### Creating Contract

```javascript
const contractFactory = new ethers.ContractFactory(abi, binary, wallet);
```

#### Deploying Contract

```javascript
const contract = await contractFactory.deploy();
await contract.deployTransaction.wait(1);
```

### Interacting with Contract

We can also interact with the contract through `ethers.js`.

#### retrieve()

```javascript
const currentFavoriteNumber = await contract.retrieve();
```

#### store()

```javascript
const transactionResponse = await contract.store("7")
const transactionReceipt = await transactionResponse.wait(1);
```

### Constructing Transaction from Raw Data

In addition to directly calling methods to deploy contracts, we can also construct transactions ourselves.

#### Constructing Transaction

```javascript
const nonce = await wallet.getTransactionCount();
const tx = {
	nonce: nonce,
	gasPrice: 20000000000,
	gasLimit: 1000000,
	to: null,
	value: 0,
	data: "0x" + binary,
	chainId: 1337,
};
```

#### Signing Transaction

```javascript
const signedTx = await wallet.signTransaction(tx);
```

#### Sending Transaction

```javascript
const sentTxResponse = await wallet.sendTransaction(tx);
await sentTxResponse.wait(1);
```

## Conclusion

The above are the steps for interacting with the Rinkeby test network of Alchemy through the `ethers.js` library. In actual production project development, we generally do not directly use libraries like `ethers.js`, but instead use further encapsulated frameworks like Brownie and HardHat. However, understanding how to use libraries like `Web3.py` or `ethers.js` is also very important. I will further explain the use of the HardHat framework in the future.

## References

> 1. [Solidity Smart Contract Development - Basics](https://www.pseudoyu.com/en/2022/05/25/learn_solidity_from_scratch_basic/)
> 2. [Solidity Smart Contract Development - Mastering Web3.py](https://www.pseudoyu.com/en/2022/05/30/learn_solidity_from_scratch_web3py/)
> 3. [Solidity, Blockchain, and Smart Contract - Javascript Version](https://www.youtube.com/watch?v=gyMwXuJrbJQ)
> 4. [ethers.js Project Repository](https://github.com/ethers-io/ethers.js/)
> 5. [ethers.js Official Documentation](https://docs.ethers.io/)
> 6. [Alchemy Official Website](https://dashboard.alchemyapi.io)