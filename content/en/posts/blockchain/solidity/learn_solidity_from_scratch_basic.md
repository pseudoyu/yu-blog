---
title: "Solidity Smart Contract Development - Fundamentals"
date: 2022-05-25T01:07:33+08:00
draft: false
tags: ["blockchain", "ethereum", "solidity", "smart contract", "web3"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

Last year, during my graduate studies, I took the course "COMP7408 Distributed Ledger and Blockchain Technology" at HKU. In this course, I learned about Ethereum smart contract development and created a simple library management ÐApp. For my graduation project, I chose to develop a music copyright application based on Ethereum, which can be found at [Uright - Blockchain Music Copyright Management ÐApp](https://github.com/pseudoyu/uright). Through these experiences, I gained a basic understanding of Solidity development.

After starting my career, I primarily focused on consortium blockchain and business development, and hadn't worked with contracts for a long time. As a result, my grasp of syntax and some underlying concepts became somewhat hazy. Recently, I've been involved in a project based on an EVM-compatible chain, which involves developing basic contracts for evidence storage, retrieval, and migration. Debugging these contracts has proven challenging, so I decided to undertake a systematic study of Solidity. By organizing my notes into articles, I hope to encourage myself to think deeply and summarize effectively.

This series of articles will also be included in my personal knowledge base project, "Blockchain Beginner's Guide," which can be found at [https://www.pseudoyu.com/blockchain-guide/](https://www.pseudoyu.com/blockchain-guide/). I aim to continuously improve this resource as I learn. For those interested, you can visit the [project repository](https://github.com/pseudoyu/blockchain-guide) to contribute or offer suggestions.

This article is the first in the series and will cover the fundamental knowledge of Solidity.

## Smart Contracts and the Solidity Language

Smart contracts are programs that run on the blockchain. Contract developers can use smart contracts to interact with on-chain assets and data, while users can call contracts through their on-chain accounts to access assets and data. Due to the blockchain's characteristics of maintaining historical records in a chain structure, decentralization, and immutability, smart contracts offer greater fairness and transparency compared to traditional applications.

However, since smart contracts need to interact with the blockchain, operations such as deployment and data writing consume a certain amount of fees. The cost of data storage and modification is also relatively high. Therefore, when designing contracts, it's crucial to consider resource consumption. Additionally, once deployed, regular smart contracts cannot be modified, so contract design must take into account security, upgradability, and extensibility.

Solidity is a contract-oriented high-level programming language created for implementing smart contracts. It runs on the EVM (Ethereum Virtual Machine) and has a syntax similar to JavaScript. It is currently the most popular smart contract language and is essential for those entering the blockchain and Web3 fields. Solidity provides relatively comprehensive solutions to address the aforementioned contract writing issues, which we will discuss in detail later.

## Development and Debugging Tools

Unlike conventional programming languages, Solidity smart contract development often cannot be conveniently debugged directly through an IDE or local environment. Instead, it requires interaction with an on-chain node. Development and debugging are typically not performed directly on the mainnet (the chain where real assets, data, and business reside), as this would incur high transaction fees. Currently, there are several main methods and frameworks for development and debugging:

1. [Truffle](https://github.com/trufflesuite/truffle). Truffle is a very popular JavaScript framework for Solidity contract development. It provides a complete toolchain for development, testing, and debugging, and can interact with local or remote networks.

2. [Brownie](https://github.com/eth-brownie/brownie). Brownie is a Python-based framework for Solidity contract development. It provides convenient toolchains for debugging and testing with concise Python syntax.

3. [Hardhat](https://github.com/NomicFoundation/hardhat). Hardhat is another JavaScript-based development framework that offers a very rich plugin system, suitable for developing complex contract projects.

In addition to development frameworks, to better work with Solidity, it's necessary to be familiar with some tools:

1. [Remix IDE](https://remix.ethereum.org). Debugging can be done using the browser-based Remix development tool provided by Ethereum. Remix offers a complete IDE, compilation tools, deployment debugging test node environment, accounts, etc., making it very convenient for testing. This is the tool I used most when learning. Remix can also interact directly with testnets and mainnets through the MetaMask plugin, and some production environments also use it for compilation and deployment.

2. Remix IDE is not perfect for syntax suggestions, so you can use [Visual Studio Code](https://code.visualstudio.com) with the [Solidity](https://marketplace.visualstudio.com/items?itemName=juanblanco.solidity) extension for better writing experience.

3. [MetaMask](https://metamask.io). A commonly used wallet application. During development, you can interact with testnets and mainnets through the browser plugin, which is convenient for developers to debug.

4. [Ganache](https://trufflesuite.com/ganache/). Ganache is an open-source virtual local node that provides a virtual chain network. It can interact with various Web3.js, Remix, or some framework tools, suitable for local debugging and testing of projects of a certain scale.

5. [Infura](https://infura.io). Infura is an IaaS (Infrastructure as a Service) product. We can apply for our own Ethereum node and interact through the API provided by Infura, which is convenient for debugging and closer to the production environment.

6. [OpenZeppelin](https://www.openzeppelin.com). OpenZeppelin provides numerous contract development libraries and applications that ensure security and stability while giving developers a better development experience and reducing contract development costs.

## Contract Compilation and Deployment

Solidity contracts are files with the `.sol` extension and cannot be executed directly. They need to be compiled into bytecode recognizable by the EVM (Ethereum Virtual Machine) to run on the chain.

![compile_solidity](https://image.pseudoyu.com/images/compile_solidity.png)

After compilation, the contract is deployed to the chain by the contract account. Other accounts can interact with the contract through wallets to implement on-chain business logic.

## Core Syntax

Now that we have a basic understanding of Solidity development, debugging, and deployment, let's dive into the core syntax of Solidity.

### Data Types

Like common programming languages, Solidity has several built-in data types.

#### Basic Data Types

- `boolean`: Boolean type has two values, `true` and `false`. It can be defined as `bool public boo = true;`. The default value is `false`.
- `int`: Integer type, can be specified from `int8` to `int256`, default is `int256`. It can be defined as `int public int = 0;`. The default value is `0`. You can also use `type(int).min` and `type(int).max` to check the minimum and maximum values of the type.
- `uint`: Non-negative integer type, can be specified as `uint8`, `uint16`, `uint256`, default is `uint256`. It can be defined as `uint8 public u8 = 1;`. The default value is `0`.
- `address`: Address type, can be defined as `address public addr = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;`. The default value is `0x0000000000000000000000000000000000000000`.
- `bytes`: Abbreviation of `byte[]`, divided into fixed-size arrays and variable arrays. It can be defined as `bytes1 a = 0xb5;`.

There are also some relatively complex data types, which we will discuss separately.

#### Enum

`Enum` is an enumeration type that can be defined using the following syntax:

```solidity
enum Status {
    Unknown,
    Start,
    End,
    Pause
}
```

It can be updated and initialized using the following syntax:

```solidity
// Instantiate enum type
Status public status;

// Update enum value
function pause() public {
    status = Status.Pause;
}

// Initialize enum value
function reset() public {
    delete status;
}
```

#### Arrays

Arrays are ordered collections of elements of the same type. They can be defined as `uint[] public arr;`. You can specify the array size in advance when defining, such as `uint[10] public myFixedSizeArr;`.

Note that we can create arrays in memory (the differences between `memory` and `storage` will be discussed in detail later), but they must be of fixed size, such as `uint[] memory a = new uint[](5);`.

Array types have some basic operation methods, as follows:

```solidity
// Define array type
uint[7] public arr;

// Add data
arr.push(7);

// Delete the last data
arr.pop();

// Delete data at a specific index
delete arr[1];

// Get array length
uint len = arr.length;
```

#### Mapping

`mapping` is a mapping type, defined using `mapping(keyType => valueType)`, where the key needs to be a built-in type such as `bytes`, `int`, `string`, or contract type, while the value can be any type, such as nested `mapping` type. Note that `mapping` types cannot be iterated over; if iteration is needed, you need to implement the corresponding index yourself.

Here are some operations:

```solidity
// Define nested mapping type
mapping(string => mapping(string => string)) nestedMap;

// Set value
nestedMap[id][key] = "0707";

// Read value
string value = nestedMap[id][key];

// Delete value
delete nestedMap[id][key];
```

#### Struct

`struct` is a structure type. For complex businesses, we often need to define our own structures to combine related data. It can be defined within a contract:

```solidity
contract Struct {
    struct Data {
        string id;
        string hash;
    }

    Data public data;

    // Add data
    function create(string calldata _id) public {
        data = Data{id: _id, hash: "111222"};
    }

    // Update data
    function update(string _id) public {
        // Query data
        string id = data.id;

        // Update
        data.hash = "222333"
    }
}
```

You can also define all the required structure types in a separate file and import them into the contract as needed:

```solidity
// 'StructDeclaration.sol'

struct Data {
    string id;
    string hash;
}
```

```solidity
// 'Struct.sol'

import "./StructDeclaration.sol"

contract Struct {
    Data public data;
}
```

### Variables, Constants, and `Immutable`

Variables are data structures in Solidity whose values can change. There are three types:

- `local` variables
- `state` variables
- `global` variables

`local` variables are defined within methods and are not stored on the chain, such as `string var = "Hello";`. `state` variables are defined outside of methods and are stored on the chain. They are defined as `string public var;`. Writing a value sends a transaction, while reading a value does not. `global` variables are global variables that provide chain information, such as the current block timestamp variable `uint timestamp = block.timestamp;`, and the contract caller address variable `address sender = msg.sender;`.

Variables can be declared using different keywords to indicate different storage locations.

- `storage`: Stored on the chain
- `memory`: In memory, only exists when the method is called
- `calldata`: Exists when passed as a parameter to call a method

Constants are variables whose values cannot be changed. Using constants can save gas fees. We can define them using `string public constant MY_CONSTANT = "0707";`. `immutable` is a special type whose value can be initialized in the `constructor` but cannot be changed again. Flexible use of these types can effectively save gas fees and ensure data security.

### Functions

In Solidity, functions are used to define specific business logic.

#### Permission Declaration

Functions have different visibilities, declared using different keywords:

- `public`: Can be called by any contract
- `private`: Can only be called within the contract that defined the method
- `internal`: Can only be called in inherited contracts
- `external`: Can only be called by other contracts and accounts

Contract functions that query data also have different declaration methods:

- `view` can read variables but cannot modify them
- `pure` cannot read or modify variables

#### Function Modifiers

`modifier` function modifiers can be called before/after a function runs, mainly used for access control, input parameter validation, and prevention of reentrancy attacks. These three types of modifiers can be defined using the following syntax:

```solidity
modifier onlyOwner() {
    require(msg.sender == owner, "Not owner");
    _;
}

modifier validAddress(address _addr) {
    require(_addr != address(0), "Not valid address");
    _;
}

modifier noReentrancy() {
    require(!locked, "No reentrancy");
    locked = true;
    _;
    locked = false;
}
```

To use function modifiers, you need to add the corresponding modifier when declaring the function, such as:

```solidity
function changeOwner(address _newOwner) public onlyOwner validAddress(_newOwner) {
    owner = _newOwner;
}

function decrement(uint i) public noReentrancy {
    x -= i;

    if (i > 1) {
        decrement(i - 1);
    }
}
```

#### Function Selector

When a function is called, the first four bytes of the `calldata` must be specified to confirm which function to call. This is known as the function selector.

```solidity
addr.call(abi.encodeWithSignature("transfer(address,uint256)", 0xSomeAddress, 123))
```

The first four bytes of the return value of `abi.encodeWithSignature()` in the above code is the function selector. If we pre-calculate the function selector before execution, we can save some gas fees.

```solidity
contract FunctionSelector {
    function getSelector(string calldata _func) external pure returns (bytes4) {
        return bytes4(keccak256(bytes(_func)));
    }
}
```

### Conditional and Loop Structures

#### Conditionals

Solidity uses the `if`, `else if`, `else` keywords to implement conditional logic:

```solidity
if (x < 10) {
    return 0;
} else if (x < 20) {
    return 1;
} else {
    return 2;
}
```

A shorthand form can also be used:

```solidity
x < 20 ? 1 : 2;
```

#### Loops

Solidity uses the `for`, `while`, `do while` keywords to implement loop logic, but because the latter two are prone to reaching the `gas limit` boundary value, they are rarely used.

```solidity
for (uint i = 0; i < 10; i++) {
    // Business logic
}
```

```solidity
uint j;
while (j < 10) {
    j++;
}
```

### Contracts

#### Constructor

Solidity's `constructor` can be executed when creating a contract, mainly used for initialization.

```solidity
constructor(string memory _name) {
    name = _name;
}
```

If there is an inheritance relationship between contracts, the `constructor` will also follow the inheritance order.

#### Interface

`Interface` is used to interact with contracts by declaring interfaces. It has the following requirements:

- Cannot implement any methods
- Can inherit from other interfaces
- All methods must be declared as `external`
- Cannot declare a constructor
- Cannot declare state variables

An interface is defined using the following syntax:

```solidity
contract Counter {
    uint public count;

    function increment() external {
        count += 1;
    }
}

interface ICounter {
    function count() external view returns (uint);
    function increment() external;
}
```

It can be called as follows:

```solidity
contract MyContract {
    function incrementCounter(address _counter) external {
        ICounter(_counter).increment();
    }

    function getCount(address _counter) external view returns (uint) {
        return ICounter(_counter).count();
    }
}
```

#### Inheritance

Solidity contracts support inheritance and can inherit from multiple contracts simultaneously using the `is` keyword.

Functions can be overridden. Methods that need to be inherited should be declared as `virtual`, and overriding methods should use the `override` keyword.

```solidity
// Define parent contract A
contract A {
    function foo() public pure virtual returns (string memory) {
        return "A";
    }
}
// Contract B inherits from contract A and overrides the function
contract B is A {
    function foo() public pure virtual override returns (string memory) {
        return "B";
    }
}

// Contract D inherits from contracts B and C and overrides the function
contract D is B, C {
    function foo() public pure override(B, C) returns (string memory) {
        return super.foo();
    }
}
```

There are a few points to note: the order of inheritance will affect the business logic, and `state` variables cannot be inherited.

If a child contract wants to call its parent contract, in addition to direct calling, it can also use the `super` keyword, as follows:

```solidity
contract B is A {
    function foo() public virtual override {
        // Direct call
        A.foo();
    }

    function bar() public virtual override {
        // Call using the super keyword
        super.bar();
    }
}
```

#### Contract Creation

In Solidity, you can create another contract from one contract using the `new` keyword.

```solidity
function create(address _owner, string memory _model) public {
    Car car = new Car(_owner, _model);
    cars.push(car);
}
```

After Solidity 0.8.0, the `create2` feature is supported for creating contracts:

```solidity
function create2(address _owner, string memory _model, bytes32 _salt) public {
    Car car = (new Car){salt: _salt}(_owner, _model);
    cars.push(car);
}
```

#### Importing Contracts/External Libraries

In complex business scenarios, we often need multiple contracts to work together. In this case, we can use the `import` keyword to import contracts. There are two ways: local import `import "./Foo.sol";` and external import `import "https://github.com/owner/repo/blob/branch/path/to/Contract.sol";`.

External libraries are similar to contracts but cannot declare state variables and cannot send assets. If all methods of the library are `internal`, they will be embedded in the contract. If they are not `internal`, the library needs to be deployed in advance and linked.

```solidity
library SafeMath {
    function add(uint x, uint y) internal pure returns (uint) {
        uint z = x + y;
        require(z >= x, "uint overflow");
        return z;
    }
}
```

```solidity
contract TestSafeMath {
    using SafeMath for uint;
}
```

#### Events

The event mechanism is a very important design in contracts. Events allow information to be recorded on the blockchain, and applications like DApps can implement business logic by listening to event data, with very low storage costs. Here's a simple log emission mechanism:

```solidity
// Define event
event Log(address indexed sender, string message);
event AnotherLog();

// Emit event
emit Log(msg.sender, "Hello World!");
emit Log(msg.sender, "Hello EVM!");
emit AnotherLog();
```

When defining an event, you can pass the `indexed` attribute, but at most three. After adding it, you can filter the parameters of this attribute, `var event = myContract.transfer({value: ["99","100","101"]});`.

### Error Handling

On-chain error handling is also an important part of contract writing. Solidity can throw errors in the following ways.

`require` is used to verify conditions before execution, and if not met, an exception is thrown.

```solidity
function testRequire(uint _i) public pure {
    require(_i > 10, "Input must be greater than 10");
}
```

`revert` is used to mark errors and perform rollbacks.

```solidity
function testRevert(uint _i) public pure {
    if (_i <= 10) {
        revert("Input must be greater than 10");
    }
}
```

`assert` requires that the condition must be met.

```solidity
function testAssert() public view {
    assert(num == 0);
}
```

Note that in Solidity, when an error occurs, all state changes that occurred in the transaction will be rolled back, including all assets, accounts, contracts, etc.

`try / catch` can also catch errors, but can only catch errors from external function calls and contract creation.

```solidity
event Log(string message);
event LogBytes(bytes data);

function tryCatchNewContract(address _owner) public {
    try new Foo(_owner) returns (Foo foo) {
        emit Log("Foo created");
    } catch Error(string memory reason) {
        emit Log(reason);
    } catch (bytes memory reason) {
        emit LogBytes(reason);
    }
}
```

### `payable` Keyword

We can set methods to receive `ether` from contracts by declaring the `payable` keyword.

```solidity
// Address type can be declared payable
address payable public owner;

constructor() payable {
    owner = payable(msg.sender);
}

// Declare method as payable to receive Ether
function deposit() public payable {}
```

### Interacting with `Ether`

Interacting with `Ether` is an important application scenario for smart contracts, mainly divided into sending and receiving parts, each implemented by different methods.

#### Sending

Mainly implemented through the `transfer`, `send`, and `call` methods. Among them, `call` has been optimized for defense against reentrancy attacks and is recommended for use in actual application scenarios (but generally not used to call other functions).

```solidity
contract SendEther {
  function sendViaCall(address payable _to) public payable {
    (bool sent, bytes memory data) = _to.call{value: msg.value}("");
    require(sent, "Failed to send Ether");
  }
}
```

If you need to call another function, `delegatecall` is generally used.

```solidity
contract B {
    uint public num;
    address public sender;
    uint public value;

    function setVars(uint _num) public payable {
        num = _num;
        sender = msg.sender;
        value = msg.value;
    }
}

contract A {
    uint public num;
    address public sender;
    uint public value;

    function setVars(address _contract, uint _num) public payable {
        (bool success, bytes memory data) = _contract.delegatecall(
            abi.encodeWithSignature("setVars(uint256)", _num)
        );
    }
}
```

#### Receiving

Receiving `Ether` mainly uses two methods: `receive() external payable` and `fallback() external payable`.

When a function that doesn't accept any parameters and doesn't return any parameters, when `Ether` is sent to a contract but the `receive()` method is not implemented or `msg.data` is non-empty, the `fallback()` method will be called.

```solidity
contract ReceiveEther {

    // When msg.data is empty
    receive() external payable {}

    // When msg.data is non-empty
    fallback() external payable {}

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
```

### Gas Fees

Executing transactions in EVM requires gas fees. `gas spent` indicates how much gas quantity is needed, `gas price` is the unit price of gas, `Ether` and `Wei` are price units, 1 ether == 1e18 wei.

Contracts will limit Gas. `gas limit` is set by the user initiating the transaction, indicating the maximum amount of gas to be spent. `block gas limit` is determined by the blockchain network, indicating the maximum amount of gas allowed in this block.

In contract development, we should particularly consider saving gas fees as much as possible. Here are some common techniques:

1. Use `calldata` instead of `memory`
2. Load state variables into memory
3. Use `i++` instead of `++i`
4. Cache array elements

```solidity
function sumIfEvenAndLessThan99(uint[] calldata nums) external {
    uint _total = total;
    uint len = nums.length;

    for (uint i = 0; i < len; ++i) {
        uint num = nums[i];
        if (num % 2 == 0 && num < 99) {
            _total += num;
        }
    }

    total = _total;
}
```

## Conclusion

The above is the first article in our series, covering the fundamentals of Solidity. Subsequent articles will focus on learning and summarizing its common applications and practical coding techniques. We welcome your continued attention.

## References

> 1. [Solidity by Example](https://solidity-by-example.org)
> 2. [Ethereum Blockchain! Introduction to Smart Contracts and Decentralized Web Applications (dApps)](http://gasolin.idv.tw/learndapp/)
> 3. [Blockchain Beginner's Guide](https://www.pseudoyu.com/blockchain-guide/)
> 4. [Uright - Blockchain Music Copyright Management ÐApp](https://github.com/pseudoyu/uright)