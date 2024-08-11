---
title: "Implementing Two-Phase Commit in Solidity Smart Contracts Using State Locks"
date: 2022-07-01T10:54:57+08:00
draft: false
tags: ["blockchain", "ethereum", "solidity", "smart contract", "web3"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Preface

In smart contract applications involving interactions between multiple systems or contracts, particularly in businesses where asset or data accuracy is sensitive, we need to ensure data atomicity throughout the entire business process. Therefore, we need to implement a mechanism similar to multi-phase commit at the contract level, which decomposes the state change process in the contract into two phases: pre-commit and formal commit.

This article implements a minimalistic two-phase commit model using a state lock mechanism. The complete contract code can be found at [TwoPhaseCommit.sol](https://github.com/pseudoyu/learn-solidity/blob/master/practice/two_phase_commit/TwoPhaseCommit.sol). The following will explain the core logic of this contract and strive to follow style guidelines and best practices.

> Note: This contract was primarily designed for business use in consortium chains and has not been specifically optimized for gas fees. It is intended for learning purposes only.

## Contract Logic

### Contract Structure

The two-phase commit scenario includes the following methods:
1. set: Two-phase - Pre-commit
2. commit: Two-phase - Formal commit
3. rollback: Two-phase - Rollback

Due to Solidity language limitations on string length judgment and comparison, to enhance the readability of the contract code, this contract provides some auxiliary methods, mainly including:
1. isValidKey: Check if the key is valid
2. isValidValue: Check if the value is valid
3. isEqualString: Compare if two strings are equal

### Two-Phase Commit Core Logic

In the two-phase commit scenario, this contract provides a simple set of `set`, `commit`, and `rollback` methods to store key-value pairs passed in contract calls on the chain. We use a state lock mechanism to achieve atomicity of cross-chain transactions. We define the following data structures:

```solidity
enum State {
    UNLOCKED,
    LOCKED
}

struct Payload {
    State state;
    string value;
    string lockValue;
}
```

Here, `State` is an enumeration type that records the lock status of the key on the chain, while the `Payload` structure stores the lock status, current value, and the value being locked. It is bound to the key through the following `mapping` structure:

```solidity
mapping (string => Payload) keyToPayload;
```

Thus, we can track the state of each key in the contract call based on `keyToPayload`, and check the state of the key in the following `set`, `commit`, and `rollback` methods for exception handling.

#### set()

In the `set()` method, we check the state of the key. If it is `State.LOCKED`, storage will not be performed and an exception will be thrown:

```solidity
if (keyToPayload[_key].state == State.LOCKED) {
    revert TwoPhaseCommit__DataIsLocked();
}
```

If it is `State.UNLOCKED`, the value passed in the contract call will be stored in lockValue, and its state will be set to `LOCKED`, waiting for subsequent `commit` or `rollback` to unlock.

```solidity
keyToPayload[_key].state = State.LOCKED;
keyToPayload[_key].lockValue = _value;
```

#### commit()

In the `commit()` method, we check the state of the key. If it is `State.UNLOCKED`, no operation will be performed on this key and an exception will be thrown:

```solidity
if (keyToPayload[_key].state == State.UNLOCKED) {
    revert TwoPhaseCommit__DataIsNotLocked();
}
```

If it is `State.LOCKED`, we check if the value passed in the contract call is equal to lockValue. If not equal, an exception is thrown:

```solidity
if (!isEqualString(keyToPayload[_key].lockValue, _value)) {
    revert TwoPhaseCommit__DataIsInconsistent();
}
```

If the values are equal, the value corresponding to this key will be stored on the chain, the state of the key will be set to `UNLOCKED`, the current value `value` will be updated, and `lockValue` will be emptied:

```solidity
store[_key] = _value;
keyToPayload[_key].state = State.UNLOCKED;
keyToPayload[_key].value = _value;
keyToPayload[_key].lockValue = "";
```

#### rollback()

In the `rollback()` method, we check the state of the key. If it is `State.UNLOCKED`, no operation will be performed on this key and an exception will be thrown:

```solidity
if (keyToPayload[_key].state == State.UNLOCKED) {
    revert TwoPhaseCommit__DataIsNotLocked();
}
```

If it is `State.LOCKED`, we check if the value passed in the contract call is equal to lockValue. If not equal, an exception is thrown:

```solidity
if (!isEqualString(keyToPayload[_key].lockValue, _value)) {
    revert TwoPhaseCommit__DataIsInconsistent();
}
```

If the values are equal, the state of the key will be set to `UNLOCKED`, and `lockValue` will be emptied:

```solidity
keyToPayload[_key].state = State.UNLOCKED;
keyToPayload[_key].lockValue = "";
```

### Error Handling Logic

In contract execution exception scenarios, we throw errors and perform rollbacks. To better improve the readability of error messages and facilitate error capture and handling by upper-layer application personnel, we adopted the error type definition approach, defining various exception scenarios. Since I have already included most of the information in the error naming, no additional parameter values for error types have been defined, which can be customized according to requirements.

```solidity
error TwoPhaseCommit__DataKeyIsNull();
error TwoPhaseCommit__DataValueIsNull();
error TwoPhaseCommit__DataIsNotExist();
error TwoPhaseCommit__DataIsLocked();
error TwoPhaseCommit__DataIsNotLocked();
error TwoPhaseCommit__DataIsInconsistent();
```

In specific contract logic, we throw exceptions using the `revert` method, such as:

```solidity
if (!isValidKey(bytes(_key))) {
    revert TwoPhaseCommit__DataKeyIsNull();
}

if (!isValidValue(bytes(_value))) {
    revert TwoPhaseCommit__DataValueIsNull();
}

if (keyToPayload[_key].state == State.UNLOCKED) {
    revert TwoPhaseCommit__DataIsNotLocked();
}

if (!isEqualString(keyToPayload[_key].lockValue, _value)) {
    revert TwoPhaseCommit__DataIsInconsistent();
}
```

### Generic Parameter Validation

We perform some validity checks on input parameters. To provide extensibility, we use the `isValidKey()` and `isValidValue()` methods to independently validate keys and values:

```solidity
/**
 * @notice Data key format validation
 * @param _key Data - Key
 */
function isValidKey(bytes memory _key) private pure returns (bool)
{
    bytes memory key = _key;

    if (key.length == 0) {
        return false;
    }
    return true;
}

/**
 * @notice Data value format validation
 * @param _value Data - Value
 */
function isValidValue(bytes memory _value) private pure returns (bool)
{
    bytes memory value = _value;

    if (value.length == 0) {
        return false;
    }
    return true;
}
```

This contract only performs non-null checks. You can customize business logic according to business needs and call it where validation is needed, such as:

```solidity
if (!isValidKey(bytes(_key))) {
    revert TwoPhaseCommit__DataKeyIsNull();
}

if (!isValidValue(bytes(_value))) {
    revert TwoPhaseCommit__DataValueIsNull();
}

if (!isValidValue(bytes(store[_key]))) {
    revert TwoPhaseCommit__DataIsNotExist();
}
```

### Event Mechanism

Additionally, we defined events corresponding to core methods and set indexed for events to facilitate monitoring and processing by upper-layer applications.

```solidity
event setEvent(string indexed key, string indexed value);
event getEvent(string indexed key, string indexed value);
event commitEvent(string indexed key, string indexed value);
event rollbackEvent(string indexed key, string indexed value);
```

Events are emitted in contract methods using the `emit()` method, such as:

```solidity
emit setEvent(_key, _value);
emit getEvent(_key, _value);
emit commitEvent(_key, _value);
emit rollbackEvent(_key, _value);
```

## Conclusion

The above is a best practice for my two-phase commit contract. For basic Solidity syntax, please refer to "[Solidity Smart Contract Development - Basics](https://www.pseudoyu.com/en/2022/05/25/learn_solidity_from_scratch_basic/)". I will continue to practice and explain more contract scenarios in the future, so stay tuned.

## References

> 1. [TwoPhaseCommit.sol Contract Source Code](https://github.com/pseudoyu/learn-solidity/blob/master/practice/two_phase_commit/TwoPhaseCommit.sol)
> 2. [Solidity Smart Contract Development - Basics](https://www.pseudoyu.com/en/2022/05/25/learn_solidity_from_scratch_basic/)
> 3. [Solidity Official Documentation](https://docs.soliditylang.org/en/v0.8.15/)