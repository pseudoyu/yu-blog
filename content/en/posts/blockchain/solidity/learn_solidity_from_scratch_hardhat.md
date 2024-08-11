---
title: "Solidity Smart Contract Development - Using the Hardhat Framework"
date: 2022-06-09T14:38:10+08:00
draft: false
tags: ["blockchain", "solidity", "ethereum", "web3", "smart contract", "javascript", "ethers.js", "hardhat", "yarn"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

After the previous articles on smart contract basics, Web3.py, and ethers.js, we have mastered the fundamental knowledge of interacting directly with blockchain networks through programs. For those unfamiliar, you can review:

- [Solidity Smart Contract Development - Basics](https://www.pseudoyu.com/en/2022/05/25/learn_solidity_from_scratch_basic/)
- [Solidity Smart Contract Development - Mastering Web3.py](https://www.pseudoyu.com/en/2022/05/30/learn_solidity_from_scratch_web3py/)
- [Solidity Smart Contract Development - Mastering ethers.js](https://www.pseudoyu.com/en/2022/06/08/learn_solidity_from_scratch_ethersjs/)

However, in real complex business scenarios, we often use some further encapsulated frameworks, such as HardHat, Brownie, Truffle, etc. HardHat is the most widely used and has the most powerful plugin expansion. This series will focus on the use and best practices of the Hardhat framework starting from this article, and this article will complete its installation, configuration, and use through a simple example.

This article is a summary of learning from [Patrick Collins](https://twitter.com/PatrickAlphaC)'s ["Learn Blockchain, Solidity, and Full Stack Web3 Development with JavaScript"](https://www.youtube.com/watch?v=gyMwXuJrbJQ) tutorial. It is strongly recommended to watch the original tutorial video for more details.

You can click [here](https://github.com/pseudoyu/learn-solidity/tree/master/hardhat_simple_storage) to access the code repository for this test demo.

## Introduction to Hardhat

![hardhat_homepage](https://image.pseudoyu.com/images/hardhat_homepage.png)

Hardhat is a JavaScript-based smart contract development environment that can be used to flexibly compile, deploy, test, and debug EVM-based smart contracts. It provides a series of toolchains to integrate code with external tools and offers a rich plugin ecosystem to improve development efficiency. In addition, it also provides a local Hardhat network node that simulates Ethereum, offering powerful local debugging capabilities.

Its GitHub address is [NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat), and you can visit its [official documentation](https://hardhat.org/getting-started) to learn more.

## Using Hardhat

### Initializing the Project

To build a Hardhat project from scratch, we need to pre-install `node.js` and `yarn` environments. This part can be installed according to the official instructions based on your system environment.

First, we need to initialize the project and install the `hardhat` dependency package.

```bash
yarn init
yarn add --dev hardhat
```

![yarn_add](https://image.pseudoyu.com/images/yarn_add.png)

### Initializing Hardhat

Then we need to run `yarn hardhat` to initialize through interactive commands. Configure according to project needs. For our test demo, we choose the default values.

![hardhat_project_init](https://image.pseudoyu.com/images/hardhat_project_init.png)

### Optimizing Code Formatting

#### VS Code Configuration

I develop code locally using VS Code. You can format code by installing the `Solidity + Hardhat` and `Prettier` plugins. You can open VS Code settings and add the following formatting configuration in `settings.json`:

```json
{
    //...

    "[solidity]": {
        "editor.defaultFormatter": "NomicFoundation.hardhat-solidity"
    },
    "[javascript]": {
        "editor.defaultFormatter": "esbenp.prettier-vscode",
    }
}
```

#### Project Configuration

To unify the code formatting styles of developers using various projects, we can also configure `prettier` and `prettier-plugin-solidity` plugin support for the project:

```bash
yarn add --dev prettier prettier-plugin-solidity
```

![yarn_add_prettier_plugin](https://image.pseudoyu.com/images/yarn_add_prettier_plugin.png)

After adding dependencies, you can add `.prettierrc` and `.prettierignore` configuration files in the project directory to unify formatting:

My `.prettierrc` configuration is:

```json
{
    "tabWidth": 4,
    "useTabs": false,
    "semi": false,
    "singleQuote": false
}
```

My `.prettierignore` configuration is:

```plaintext
node_modules
package.json
img
artifacts
cache
coverage
.env
.*
README.md
coverage.json
```

### Compiling Contracts

There's no need to customize the `compile` command like in `ethers.js`. HardHat provides a built-in `compile` command. You can place contracts in the `contracts` directory and then compile them using the `yarn hardhat compile` command:

![hardhat_compile_contract](https://image.pseudoyu.com/images/hardhat_compile_contract.png)

### Adding `dotenv` Support

Before we start writing deployment scripts, let's configure the `dotenv` plugin. This way, we can use `dotenv` to get environment variables. During development, we will deal with a lot of private information, such as private keys, etc. We would like to store them in a `.env` file or set them directly in the terminal, such as our `RINKEBY_PRIVATE_TOKEN`. This way, we can use `process.env.RINKEBY_PRIVATE_TOKEN` to get the value in the deployment script without explicitly writing it in the code, reducing the risk of privacy leakage.

#### Installing `dotenv`

```bash
yarn add --dev dotenv
```

![yarn_add_dotenv](https://image.pseudoyu.com/images/yarn_add_dotenv.png)

#### Setting Environment Variables

In the `.env` file, we can set environment variables, such as:

```plaintext
RINKEBY_RPC_URL=url
RINKEBY_PRIVATE_KEY=0xkey
ETHERSCAN_API_KEY=key
COINMARKETCAP_API_KEY=key
```

We can then read environment variables in `hardhat.config.js`:

```javascript
require("dotenv").config()

const RINKEBY_RPC_URL =
    process.env.RINKEBY_RPC_URL || "https://eth-rinkeby/example"
const RINKEBY_PRIVATE_KEY = process.env.RINKEBY_PRIVATE_KEY || "0xkey"
const ETHERSCAN_API_KEY = process.env.ETHERSCAN_API_KEY || "key"
const COINMARKETCAP_API_KEY = process.env.COINMARKETCAP_API_KEY || "key"
```

### Configuring Network Environment

Often, our contracts need to run on different blockchain networks, such as local testing, development, and production environments. Hardhat also provides a convenient way to configure network environments.

#### Starting the Network

We can directly run a script to start a network that comes with Hardhat, but this network only exists during script execution. To start a locally sustainable network, you need to run the `yarn hardhat node` command:

![hardhat_localhost_node](https://image.pseudoyu.com/images/hardhat_localhost_node.png)

After execution, test networks and test accounts are generated for subsequent development and debugging.

We can also generate our own test network nodes through platforms like Alchemy or Infura, and record their `RPC_URL` for program connection use.

#### Defining Networks

After preparing the network environment, we can define networks in the project configuration `hardhat.config.js`:

```javascript
const RINKEBY_RPC_URL =
    process.env.RINKEBY_RPC_URL || "https://eth-rinkeby/example"
const RINKEBY_PRIVATE_KEY = process.env.RINKEBY_PRIVATE_KEY || "0xkey"

module.exports = {
    defaultNetwork: "hardhat",
    networks: {
        locakhost: {
            url: "http://localhost:8545",
            chainId: 31337,
        },
        rinkeby: {
            url: RINKEBY_RPC_URL,
            accounts: [RINKEBY_PRIVATE_KEY],
            chainId: 4,

        },
    },
    // ...,
}
```

### Scripts

In a Hardhat project, we can implement functions such as deployment by writing scripts in the `scripts` directory and execute scripts through convenient commands.

#### Writing Deployment Scripts

Next, let's start writing the `deploy.js` script.

First, we need to import necessary packages from `hardhat`:

```javascript
const { ethers, run, network } = require("hardhat")
```

Then write the `main` method, which includes our core deployment logic:

```javascript
async function main() {
    const SimpleStorageFactory = await ethers.getContractFactory(
        "SimpleStorage"
    )
    console.log("Deploying SimpleStorage Contract...")
    const simpleStorage = await SimpleStorageFactory.deploy()
    await simpleStorage.deployed()
    console.log("SimpleStorage Contract deployed at:", simpleStorage.address)

    // Get current value
    const currentValue = await simpleStorage.retrieve()
    console.log("Current value:", currentValue)

    // Set value
    const transactionResponse = await simpleStorage.store(7)
    await transactionResponse.wait(1)

    // Get updated value
    const updatedValue = await await simpleStorage.retrieve()
    console.log("Updated value:", updatedValue)
}
```

Finally, run our `main` method:

```javascript
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error)
        process.exit(1)
    })
```

#### Running Scripts

After completing the script writing, you can run the script using the `run` command provided by Hardhat.

If no network parameter is added, the `hardhat` network is used by default. You can specify the network using the `--network` parameter:

```bash
yarn hardhat run scripts/deploy.js --network rinkeby
```

![hardhat_deploy_rinkeby](https://image.pseudoyu.com/images/hardhat_deploy_rinkeby.png)

### Adding Etherscan Contract Verification Support

After deploying the contract to the Rinkeby test network, you can view the contract address on Etherscan and verify it. We can do this through the website, but Hardhat provides plugin support, making it more convenient to perform verification operations.

#### Installing hardhat-etherscan Plugin

We install the plugin using the `yarn add --dev @nomiclabs/hardhat-etherscan` command.

![yarn_add_etherscan_verify_support](https://image.pseudoyu.com/images/yarn_add_etherscan_verify_support.png)

#### Enabling Etherscan Contract Verification Support

After installation, we need to configure in `hardhat.config.js`:

```javascript
require("@nomiclabs/hardhat-etherscan")

module.exports = {
    // ...,
    etherscan: {
        apiKey: ETHERSCAN_API_KEY,
    },
    // ...,
}
```

#### Defining Verify Method

Next, we need to add a `verify` method in the deployment script `deploy.js`.

```javascript
const { ethers, run, network } = require("hardhat")

async function verify(contractAddress, args) {
    console.log("Verifying SimpleStorage Contract...")
    try {
        await run("verify:verify", {
            address: contractAddress,
            constructorArguements: args,
        })
    } catch (e) {
        if (e.message.toLowerCase().includes("already verified!")) {
            console.log("Already Verified!")
        } else {
            console.log(e)
        }
    }
}
```

In this method, we call the `run` method from the `hardhat` package, pass a `verify` command, and pass a parameter `{ address: contractAddress, constructorArguements: args }`. Since our contract may have already been verified on Etherscan, we do a `try...catch...` error handling. If it's already verified, it will throw an error and output a prompt message without affecting our deployment process.

#### Setting Post-Deployment Call

After defining our `verify` method, we can call it in the deployment script:

```javascript
async function main() {
    //...

    if (network.config.chainId === 4 && process.env.ETHERSCAN_API_KEY) {
        await simpleStorage.deployTransaction.wait(6)
        await verify(simpleStorage.address, [])
    }

    // ...
}
```

Here we made two special treatments.

First, we only need to verify the contract on the `rinkeby` network, not on local or other network environments. Therefore, we judge `network.config.chainId`. If it's `4`, we perform the verification operation; otherwise, we don't. In addition, we only perform the verification operation when there is an `ETHERSCAN_API_KEY` environment variable.

Also, Etherscan may need some time after deployment to get the contract address, so we configured `.wait(6)` to wait for 6 blocks before verification.

The execution effect is as follows:

![hardhat_verify_contract_etherscan](https://image.pseudoyu.com/images/hardhat_verify_contract_etherscan.png)

![verified_contract_on_etherscan](https://image.pseudoyu.com/images/verified_contract_on_etherscan.png)

After verification through Etherscan, we can directly view the contract source code and interact with it.

![interact_with_contract_on_etherscan](https://image.pseudoyu.com/images/interact_with_contract_on_etherscan.png)

### Contract Testing

For smart contracts, most operations need to be deployed on-chain, interact with assets, consume gas, and once there are security vulnerabilities, it will cause serious consequences. Therefore, we need to conduct detailed tests on smart contracts.

Hardhat provides comprehensive testing and debugging tools. We can write test scripts in the `tests` directory and run tests using the `yarn hardhat test` command.

#### Writing Test Scripts

Let's write a `test-deploy.js` test program for our deployment script. First, we need to import the necessary packages:

```javascript
const { assert } = require("chai")
const { ethers } = require("hardhat")
```

Then write the test logic:

```javascript
describe("SimpleStorage", () => {
    let simpleStorageFactory, simpleStorage
    beforeEach(async () => {
        simpleStorageFactory = await ethers.getContractFactory("SimpleStorage")
        simpleStorage = await simpleStorageFactory.deploy()
    })

    it("Should start with a favorite number of 0", async () => {
        const currentValue = await simpleStorage.retrieve()
        const expectedValue = "0"

        assert.equal(currentValue.toString(), expectedValue)
        // expect(currentValue.toString()).to.equal(expectedValue)
    })

    it("Should update when we call store", async () => {
        const expectedValue = "7"
        const transactionRespense = await simpleStorage.store(expectedValue)
        await transactionRespense.wait(1)

        const currentValue = await simpleStorage.retrieve()

        assert.equal(currentValue.toString(), expectedValue)
        // expect(currentValue.toString()).to.equal(expectedValue)
    })
```

In Hardhat's test script, we use `describe` to wrap the test class and use `it` to wrap the test method. We need to ensure that the contract is deployed before testing, so we use the `beforeEach` method to call `simpleStorageFactory.deploy()` before each test method is executed, and assign the returned `simpleStorage` object to the `simpleStorage` variable.

We use `assert.equal(currentValue.toString(), expectedValue)` to compare the execution result with the expected result. It can be replaced with `expect(currentValue.toString()).to.equal(expectedValue)`, which has the same effect.

In addition, we can use `it.only()` to specify that only one of the test methods is executed.

#### Running Test Scripts

We run the test with `yarn hardhat test` and can specify test methods with `yarn hardhat test --grep store`.

![hardhat_run_tests](https://image.pseudoyu.com/images/hardhat_run_tests.png)

### Adding `gas-reporter` Support

As mentioned above, gas is a resource we need to pay special attention to during development, especially expensive on the Ethereum mainnet. Therefore, we need to check gas consumption during testing. HardHat also has a `gas-reporter` plugin that can conveniently output gas consumption information.

#### Installing `gas-reporter` Plugin

We install the plugin using the `yarn add --dev hardhat-gas-reporter` command:

![yarn_add_gas_reporter](https://image.pseudoyu.com/images/yarn_add_gas_reporter.png)

#### Enabling `gas-reporter` Support

We enable the plugin by adding `gasReporter: true` and additional configuration items in `hardhat.config.js`:

```javascript
require("hardhat-gas-reporter")

const COINMARKETCAP_API_KEY = process.env.COINMARKETCAP_API_KEY || "key"

module.exports = {
    // ...,
    gasReporter: {
        enabled: true,
        outputFile: "gas-reporter.txt",
        noColors: true,
        currency: "USD",
        coinmarketcap: COINMARKETCAP_API_KEY,
        token: "MATIC",
    },
}
```

We can specify output file, whether to enable colors, specify currency, specify token name, and specify CoinMarketCap API key to further control output according to the project.

According to the above configuration, running `yarn hardhat test` outputs the following effect:

![hardhat_add_gas_reporter_support_and_export](https://image.pseudoyu.com/images/hardhat_add_gas_reporter_support_and_export.png)

### Adding `solidity-coverage` Support

Contract testing is crucial for ensuring business logic correctness and security prevention. Therefore, we need to conduct coverage testing on contracts. HardHat also has a `solidity-coverage` plugin that can conveniently output coverage information.

#### Installing `solidity-coverage` Plugin

We install the plugin using the `yarn add --dev solidity-coverage` command:

![yarn_add_coverage_support](https://image.pseudoyu.com/images/yarn_add_coverage_support.png)

#### Enabling `solidity-coverage` Support

We only need to import the package in `hardhat.config.js` to add coverage test support:

```javascript
require("solidity-coverage")
```

#### Running Coverage Test

Run coverage test with `yarn hardhat coverage`:

![hardhat_coverage](https://image.pseudoyu.com/images/hardhat_coverage.png)

### Task

Above, we have used some basic functions and scripts of the `hardhat` library. In addition, we can also customize some tasks for development and debugging.

#### Writing Tasks

In Hardhat, we define tasks in the `tasks` directory. We will write a `block-number.js` task to get the block height:

```javascript
const { task } = require("hardhat/config")

task("block-number", "Prints the current block number").setAction(
    async (taskArgs, hre) => {
        const blockNumber = await hre.ethers.provider.getBlockNumber()
        console.log(`Current Block Number: ${blockNumber}`)
    }
)
```

Tasks are created using the `task()` method and the execution function is set using the `setAction()` method. Here, `taskArgs` is an object containing all parameters, and `hre` is a `HardhatRuntimeEnvironment` object that can be used to get other resources.

#### Running Tasks

After definition, our newly defined `block-number` task will appear in the `AVAILABLE TASKS` of the project command. You can run the task using the `yarn hardhat block-number` command. Similarly, we can specify a specific network to run:

```bash
yarn hardhat block-number --network rinkeby
```

![hardhat_run_tasks](https://image.pseudoyu.com/images/hardhat_run_tasks.png)

### Hardhat Console

Finally, in addition to interacting with the chain/contract through code, we can also debug projects, view chain status, contract input and output, etc. through the `Hardhat Console`. We can open the Hardhat Console and interact using the `yarn hardhat console` command.

![hardhat_console](https://image.pseudoyu.com/images/hardhat_console.png)

## Conclusion

The above is my basic configuration and use of the Hardhat framework. It is a very powerful development framework, and I will continue to delve into more of its features and usage techniques in the future. If you're interested, you can continue to follow. I hope this is helpful to everyone.

## References

> 1. [Learn Blockchain, Solidity, and Full Stack Web3 Development with JavaScript](https://www.youtube.com/watch?v=gyMwXuJrbJQ)
> 2. [NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat)
> 3. [Hardhat Official Documentation](https://hardhat.org/getting-started)
> 4. [Solidity Smart Contract Development - Basics](https://www.pseudoyu.com/en/2022/05/25/learn_solidity_from_scratch_basic/)
> 5. [Solidity Smart Contract Development - Mastering Web3.py](https://www.pseudoyu.com/en/2022/05/30/learn_solidity_from_scratch_web3py/)
> 6. [Solidity Smart Contract Development - Mastering ethers.js](https://www.pseudoyu.com/en/2022/06/08/learn_solidity_from_scratch_ethersjs/)