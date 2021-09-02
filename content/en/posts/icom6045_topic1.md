---
title: "ICOM6045 Topic 1 Cryptography"
date: 2020-10-21T19:53:17+08:00
draft: false
tags: ["internet","security","hku","icmo6045"]
categories: ["Notes"]
authors:
- "Arthur"
---

# ICOM6045 Fundamentals of E-Commerce Security 

## Topic 1 Cryptography

## Definition
- Process of transforming information to make it unreadable to anyone except those possessing the key

## Purpose
- Data confidentiality

## Transpositions/Permutations
- An encryption in which the letters of the message are rearranged
- Function
  - Try to break established patterns
- Example
  - Columnar transposition
    - Rearrangement of the characters of the plaintext into columns
    - Based on characteristic patterns of pairs of adjacent letters, called digrams
    - Analysis
      - Compute the letter frequencies
    	- Break the text into columns by compare a block of ciphertext characters against characters successively farther away in the ciphertext.
    	- 1. Do common digrams appear.
    	- 2. Do most of the digram look reasonable
- Complexity
  - No additional work
  - Require storage for all characters of the message
  - Not good for long message
- Alternative
  - Permute the characters of the plaintext with a fixed period d

## Confusion

- Cipher that makes relationship between the plaintext/key pair and the ciphertext as complex as possible
- Good confusion
  - poly-alphabetic substitution with a long key
- Bad confusion
  - Caesar cipher

## Diffusion

- Cipher that spreads the information from the plaintext over the entire ciphertext
- Change in the plaintext should affect many parts of the ciphertext
- Good diffusion
  - DES
  - Transposition cipher
- Bad diffusion
  - Substitutin cipher

## Cryptanalysis
- Index of coincidence (A tool to rate how wella particular distribution
matches the distribution of letter in English)
- Procedure
  - Measure of roughness(variance)
  - If the distribution is perfectly flat
- Examine
  - Is it encrypted
  - How is it encrypted
  - What is the key

## Types

### Symmetric Key Encryption

- Procedure (Single key)
	- Original message
	- Key -> Encryption algorithm
	- Encrypted message
	- Encrypted message sent over Internet
	- Encrypted message arrives destination
	- Key -> Decryption algorithm
	- Original message
- Algorithms
	- DES(Data Encryption Standard)
		- Most commonly used block cipher
		- Purpose
			- Facilitate hardware implementation
		- Form
			- A block cipher with 56-bit key (64-bit including parity bits)
			- "Feistel" network structure
	- AES(Advanced Encryption Standard)
	- RC4
- Stream cipher
	- Definition
		- Convert one symbol of plaintext immediately into a symbol of ciphertext
	- Advantage
		- Speed of transformation
		- Low error propagation
	- Disadvantage
		- Low diffusion
		- Possible for malicious insertions and modifications
- Block cipher
	- Definition
		- Encrypt a group of plaintext symbol as one block
	- Advantage
		- Diffusion
		- Immunity to insertion
	- Disadvantage
		- Slowness of encryption
		- Error propagation
- Kasiski method
	- Search for repeated sequence of characters
	- Example
		- 3 occurrences of the 11-character sequence
		- Distance between first 2 sequence = 141- 90 = 51
		- Distance between second 2 sequences = 213 - 141 = 72
		- The common divisor between 51 and 72 is 3
		- Estimated key length is 3
- "Perfect" substitution cipher
	- Definition
		- Many alphabets for an unrecognizable distribution
		- No apparent pattern for the choice of an alphabet at a particular point
	- Function
		- Confuse the Kasiski method
		- Index of coincidence would be close to 0.038
- Application
	- Caesar cipher
		- Definition
			- The message is enciphered with a 27-symbol alphabet (A->Z) and the blank, the blank is translated to itself
		- Permutation
			- Each letter is translated to a fixed number of letters after it in the alphabet
		- The "real" Caessar cipher by Julius Caesar used a shift of 3
	- Mono-alphabetic substitutions
		- Definition
			- The alphabet is scrambled, and each plaintext letter maps to a unique ciphertext letter
		- Permutation
			- A permutation is a recording of the elements of a series
			- A permutation can be a function
			- Some permutations can't be represented as simple equation
		- Weakness
			- Frequency distribution
	- Polyalphabetic substitutions
		- Definition
			- Combine distributions that are high with ones that are low
		- Analysis
			- Use Kasiski method to predict likely numbers of enciphering alphabets
			- If no numbers emerge fairly regularly, may not a poly-alphabetic substitution
			- Compute the index of coincidence to validate the predictions from step 1
			- When step 1 and 3 indicate a promising value, separate the ciphertext into appropriate subsets and independently compute index of coincidence of each subset
		- Example
			- Rotor Machines
	- Vigenere cipher
		- Definition
			- Vigenere tableau
				- A collection of 26 permutations
				- Written in a 26*26 matrix
		- Permutation
			- Use a key (keyword) -> select  particular permutaion
	- One-time pad
		- Definition
			- Based on a large nonrepeating set of keys (written on paper and glued together into a pad)
		- Procedure
			- Sender writes key one time above the letters of the plaintext
			- Encipher the plaintext with a chart like Vigenere tableau
			- Sender destroys the key
			- Receiver takes the appropriate number of keys
			- Decipher the message
		- Example
			- Vernam cipher
				- Involves an arbitrarily long nonrepeating sequence of numbers that are combined with the plaintext
				- Possible attack
					- Random number generator

### Public Key Encryption
- Procedure (Everyone has 2 keys)
	- Original message
	- Encryption key -> Encryption algorithm
		- Plaintext <- Encryption
			- The original form of a message
		- Ciphertext <- Decryption
			- The encrypted form a message
		- Original plaintext
	- Encrypted message
	- Encrypted message sent over Internet
	- Encrypted message arrives destination
	- Decryption key -> Decryption algorithm
	- Original message
- Algorithms
	- RSA