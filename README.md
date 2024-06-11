# HoraDES

## Overview
HoraDES is a custom implementation of a cryptographic algorithm inspired by the Data Encryption Standard (DES). It features an 80-bit plaintext input and a 72-bit key, and it incorporates elements such as initial and final permutations, expansion functions, and substitution boxes (S-boxes). This implementation showcases the principles of the Feistel network, allowing both encryption and decryption through similar processes.

## Features
- **Initial and Final Permutations**: Uses custom permutation tables for the initial and final permutations of the plaintext.
- **Key Expansion**: Generates subkeys using the provided key and permutation tables.
- **Feistel Structure**: Implements a 16-round Feistel structure for encryption.
- **S-boxes**: Utilizes custom S-boxes to perform substitution operations during the encryption rounds.
- **Custom Functions**: Includes functions for permutations, key rotations, and applying S-boxes.

## Getting Started

### Prerequisites
- Python 3.x
- No additional libraries are required.

### Installation
Clone the repository to your local machine:
```sh
git clone https://github.com/horahagh16/HoraDES.git
```
Navigate to the project directory:
```sh
cd HoraDES
```

### Usage
The main function of the script, `main`, takes a plaintext string and a key as inputs, and returns the encrypted ciphertext. The plaintext is first hashed to a 160-bit binary output, split into two 80-bit blocks, and then each block is encrypted using the HoraDES function.

#### Example
```python
plaintext = 'In cryptography a Feistel cipher...'
key = 'your-72-bit-key'
encrypted_text = main(plaintext, key)
print(encrypted_text)
```

### Functions

#### `apply_permutation(input_bits, permutation_table)`
Applies a given permutation table to the input bits.

#### `rotate_right(key_half, shifts)`
Rotates the key half to the right by a given number of shifts.

#### `generate_subkey(Key_72, round=16)`
Generates subkeys for each round of the Feistel structure using the provided 72-bit key.

#### `apply_sbox(input_bits, sbox)`
Applies an S-box to the input bits and returns the output.

#### `f_function(right_half_40, subkey_56)`
Computes the function `f` used in the Feistel structure, which includes expansion, XOR with the subkey, S-box substitution, and permutation.

#### `HoraDES(plaintext_80, Key_72, round=16)`
Encrypts an 80-bit plaintext using the HoraDES algorithm and the provided key.

#### `main(plaintext, key)`
Hashes the plaintext, splits it into  80-bit blocks, and encrypts each block using HoraDES. Returns the concatenated ciphertext.

## Author
This script was developed by Hora Haghighatkhah. Feel free to contribute by submitting pull requests or opening issues.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
