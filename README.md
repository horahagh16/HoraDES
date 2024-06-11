# HoraDES
## Overview
The HoraDES encryption algorithm is an implementation of a Feistel cipher, inspired by the DES (Data Encryption Standard) structure. This algorithm operates on 80-bit blocks and uses a 72-bit key to encrypt plaintext data. It follows a symmetric encryption method, meaning the same key is used for both encryption and decryption processes.

## Features
- **Initial and Final Permutations**: The algorithm applies initial and final permutations to the plaintext and ciphertext, respectively, using predefined permutation tables.
- **Expansion Permutation**: The right half of the data block is expanded from 40 bits to 56 bits using an expansion table.
- **S-boxes**: Eight S-boxes are used to perform substitution operations, transforming the expanded right half during the encryption rounds.
- **Key Schedule**: A key schedule is used to generate 16 subkeys from the original 72-bit key. Each subkey is applied in one of the 16 rounds of the Feistel structure.
- **Feistel Rounds**: The algorithm uses a series of rounds where the right half and left half of the data block are processed. Each round involves XOR operations and substitutions using S-boxes.

## How It Works
1. **Initial Permutation (IP)**: The plaintext is permuted using the initial permutation table.
2. **Splitting**: The permuted plaintext is split into a left half and a right half, each 40 bits long.
3. **Key Generation**: The 72-bit key is permuted and split, and then subkeys are generated for each round.
4. **Feistel Rounds**: For each of the 16 rounds, the right half is expanded, XORed with the subkey, and passed through the S-boxes. The output is permuted and XORed with the left half. The halves are then swapped.
5. **Final Permutation (IP-1)**: After 16 rounds, the left and right halves are combined and permuted using the final permutation table.
6. **Output**: The result is the 80-bit encrypted ciphertext.

## Usage
To use the HoraDES encryption algorithm, follow these steps:

1. **Input Preparation**: Prepare the plaintext string and the 72-bit key. The plaintext will be padded to ensure its length is divisible by 10 characters (80 bits).
2. **Encryption**: The plaintext is converted to its binary format and split into 80-bit chunks. Each chunk is encrypted using the HoraDES function.
3. **Result**: The encrypted chunks are combined to produce the final encrypted string.

## Example
```python
plaintext = 'Your plaintext message here'
key = 'Your 72-bit key here'

encrypted_message = main(plaintext, key)
print(encrypted_message)
```

## Components
- **Permutations**: 
  - `IP`: Initial permutation table.
  - `IP-1`: Final permutation table.
  - `E`: Expansion table.
  - `PC1`: Key permutation table 1.
  - `PC2`: Key permutation table 2.
  - `FINAL_P`: Final permutation after S-box output.

- **S-Boxes**: A set of predefined S-boxes used for substitution.

- **Functions**:
  - `apply_permutation(input_bits, permutation_table)`: Applies a permutation to the input bits using the specified table.
  - `rotate_right(key_half, shifts)`: Rotates the key half to the right by the specified number of shifts.
  - `generate_subkey(Key_72, round)`: Generates subkeys from the main key for the specified number of rounds.
  - `apply_sbox(input_bits, sbox)`: Applies the S-box to the input bits.
  - `f_function(right_half_40, subkey_56)`: Computes the Feistel function for a given right half and subkey.
  - `HoraDES(plaintext_80, Key_72, round)`: Encrypts an 80-bit block of plaintext using the HoraDES algorithm.
  - `main(plaintext, key)`: Main function to handle plaintext padding, chunking, and encryption.

## Author
This script was developed by Hora Haghighatkhah. Feel free to contribute by submitting pull requests or opening issues.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
