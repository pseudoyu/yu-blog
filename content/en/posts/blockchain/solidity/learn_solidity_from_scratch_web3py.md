---
title: "Solidity Smart Contract Development - Mastering Web3.py"
date: 2022-05-30T15:25:45+08:00
draft: false
tags: ["blockchain", "solidity", "ethereum", "web3", "smart contract", "python"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Preface

In the previous article "[Solidity Smart Contract Development - Basics](https://www.pseudoyu.com/en/2022/05/25/learn_solidity_from_scratch_basic/)", we learned the basic syntax of Solidity and understood that we can debug using frameworks such as [Brownie](https://github.com/eth-brownie/brownie) and [HardHat](https://github.com/NomicFoundation/hardhat). However, before using these pre-packaged frameworks, we can interact directly with our local Ganache node using Web3.py to better understand the principles and lay a solid foundation for our subsequent use of frameworks.

This article uses Web3.py as an example to implement basic contract compilation, deployment to the local Ganache network, and interaction with contracts.

You can click [here](https://github.com/pseudoyu/learn-solidity/tree/master/web3_py_simple_storage) to access the code repository for this test demo.

## Web3.py

Web3.py is an open-source library for Python that provides a simple API allowing us to interact with the Ethereum network through Python programs. Its GitHub address is [ethereum/web3.py](https://github.com/ethereum/web3.py), and you can visit its [official documentation](https://web3py.readthedocs.io/en/stable/) for usage.

### Installation

We can install Web3.py using the Python package management tool pip, as follows:

```bash
pip3 install web3
```

![pip_install_web3](https://image.pseudoyu.com/images/pip_install_web3.png)

### Usage

Simply import the required methods using `import` to use

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
```

## Solidity Contract Compilation

### Contract Source Code

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

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

### Reading Contract Source File

After completing the Solidity contract writing and syntax check using VSCode or other editors, we need to read the contract source file and store it in a variable for subsequent compilation.

```python
import os

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
```

The above code reads the contents of the `SimpleStorage.sol` file into the variable `simple_storage_file`.

### Compiling the Contract

#### Installing `solcx`

Contract compilation requires the prior installation of the `solcx` tool.

```bash
pip3 install py-solc-x
```

![pip_install_solcx](https://image.pseudoyu.com/images/pip_install_solcx.png)

#### Importing `solcx`

Use `import` to import the required methods for use

```python
from solcx import compile_standard, install_solc
```

#### Compilation

```python
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
```

In the above code, we installed version 0.6.0 of the Solidity compilation program, used the `compile_standard` method from the `solcx` library to compile the contract source file read earlier, and stored the compilation result in the variable `compiled_sol`.

#### Obtaining Compilation Results

After successful compilation, use the following code to write the compiled contract to a file

```python
import json

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
```

#### Obtaining bytecode and abi

The deployment and interaction of Solidity contracts require two parts: bytecode and abi. We can write them into corresponding variables for subsequent operations using the following code.

```python
# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
```

## Local Ganache Environment

Debugging smart contracts requires deploying the contract to an actual chain, but deploying to the Ethereum mainnet or testnets like Rinkeby/Koven is not convenient for debugging. Therefore, we need a local blockchain environment, and Ganache provides us with such a local debugging environment. Ganache mainly comes in two installation methods: GUI and CLI.

### Ganache GUI

In your local environment, such as Mac/Windows systems, we can choose the Ganache client with a graphical interface. The installation and use are very convenient. You can select the corresponding version on the [Ganache official website](https://trufflesuite.com/ganache/).

![ganache_download](https://image.pseudoyu.com/images/ganache_download.png)

After installation, selecting Quick Start will quickly launch a locally running blockchain network and initialize ten accounts with 100 ETH each, which can be used during development and debugging.

![ganache_account](https://image.pseudoyu.com/images/ganache_account.png)

### Ganache CLI Installation

If your system doesn't support GUI installation, we can use CLI installation. The installation method is as follows:

```bash
npm install --global yarn
yarn global add ganache-cli
```

![ganache_cli_install](https://image.pseudoyu.com/images/ganache_cli_install.png)

After waiting for it to complete installation, you can start the local test network. Consistent with Ganache GUI, it also includes initialized accounts and balances.

![ganache_cli_start](https://image.pseudoyu.com/images/ganache_cli_start.png)

### Connecting to Local Ganache Environment via web3

web3 provides a library that can easily connect to the local Ganache environment:

```python
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 5777
my_address = "0x2F490e1eA91DF6d3cC856e7AC391a20b1eceD6A5"
private_key = "0fa88bf96b526a955a6126ae4cca0e72c9c82144ae9af37b497eb6afbe8a9711"
```

## Solidity Contract Deployment

### Creating a Contract

We can create a contract using the web3 library.

```python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
```

### Deploying the Contract

Deploying a contract consists of three main steps:

1. Constructing the transaction
2. Signing the transaction
3. Sending the transaction

#### Constructing the Transaction

```python
nonce = w3.eth.getTransactionCount(my_address)

transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
```

#### Signing the Transaction

```python
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
```

#### Sending the Transaction

```python
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
```

### Interacting with the Contract

Similar to the steps for deploying a contract, we can interact with the contract using the web3 library, which also consists of three steps: constructing the transaction, signing the transaction, and sending the transaction.

#### Constructing the Transaction

```python
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

store_transaction = simple_storage.functions.store(67).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
```

#### Signing the Transaction

```python
signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
```

#### Sending the Transaction

```python
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
```

## Conclusion

The above are the steps for interacting with the local Ganache test network using the Web3.py library. In actual production project development, we generally don't directly use libraries like Web3.py, but instead use further encapsulated libraries like Brownie and HardHat. However, understanding how to use libraries like Web3.py or Web3.js is also very important.

## References

> 1. [Solidity Smart Contract Development - Basics](https://www.pseudoyu.com/en/2022/05/25/learn_solidity_from_scratch_basic/)
> 2. [ethereum/web3.py](https://github.com/ethereum/web3.py)
> 3. [Solidity, Blockchain, and Smart Contract - Beginner to Expert Full Course | Python Edition](https://github.com/smartcontractkit/full-blockchain-solidity-course-py)