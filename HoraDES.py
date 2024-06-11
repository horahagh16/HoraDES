import hashlib

# DES Initial Permutation Table
IP = [
    51, 19, 40, 36, 50, 25, 73, 42, 35, 6,
    44, 4, 8, 78, 24, 15, 7, 13, 45, 65,
    5, 32, 29, 1, 54, 34, 9, 14, 57, 46,
    53, 49, 74, 72, 12, 17, 70, 62, 22, 23,
    59, 48, 3, 69, 63, 2, 21, 60, 38, 75,
    20, 61, 67, 47, 76, 33, 66, 58, 16, 77,
    71, 55, 80, 41, 37, 52, 11, 28, 39, 68,
    10, 18, 43, 64, 27, 31, 26, 30, 56, 79
]

IP_1 = [24, 46, 43, 12, 21, 10, 17, 13, 27, 71,
         67, 35, 18, 28, 16, 59, 36, 72, 2, 51,
         47, 39, 40, 15, 6, 77, 75, 68, 23, 78, 
         76, 22, 56, 26, 9, 4, 65, 49, 69, 3, 64,
         8, 73, 11, 19, 30, 54, 42, 32, 5, 1, 66, 
         31, 25, 62, 79, 29, 58, 41, 48, 52, 38, 
         45, 74, 20, 57, 53, 70, 44, 37, 61, 34, 
         7, 33, 50, 55, 60, 14, 80, 63]

FINAL_P = [12, 11, 28, 16, 15, 31, 9, 26, 
            6, 3, 25, 37, 27, 22, 13, 4, 
            2, 33, 14, 34, 18, 10, 23, 35, 
            36, 30, 32, 21, 20, 29, 19, 24, 
            1, 32, 39, 38, 7, 5, 17, 8]

# Expansion table E
E = [
     3,  1,  2,  3,  4,  5,  3,
     8,  6,  7,  8,  9, 10,  8,
    13, 11, 12, 13, 14, 15, 13,
    18, 16, 17, 18, 19, 20, 18,
    23, 21, 22, 23, 24, 25, 23,
    28, 26, 27, 28, 29, 30, 28,
    33, 31, 32, 33, 34, 35, 33,
    38, 36, 37, 38, 39, 40, 38
]

# DES Key permutation tables PC-1 and PC-2, and number of right shifts for each round
PC1 = [1, 46, 58, 34, 60, 10, 67, 30, 
       28, 68, 2, 38, 41, 55, 56, 14, 
       24, 22, 21, 59, 11, 45, 49, 52, 
       50, 47, 13, 71, 44, 18, 57, 3, 
       51, 17, 6, 66, 15, 48, 42, 43, 
       61, 27, 54, 35, 12, 70, 29, 9, 
       16, 39, 33, 37, 32, 36, 19, 4, 
       62, 8, 26, 69, 63, 25, 53, 64]

PC2 = [16, 21, 32, 52, 53, 39, 46, 6, 14, 23, 13, 54, 0, 15,
        57, 2, 25, 42, 55, 48, 51, 8, 18, 17, 63, 38, 24, 1,
       41, 4, 26, 27, 56, 59, 45, 12, 47, 30, 11, 19, 7, 3, 
       50, 62, 28, 20, 9, 44, 37, 35, 29, 34, 10, 49, 5, 40]

SHIFTS = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2]


# Define S-boxes
S_BOXES = [[[11,32, 4, 1, 29, 30, 5, 17, 15, 10, 7, 8, 3, 26, 9, 12, 18, 2, 21, 16, 31, 6, 13, 23, 20, 14, 22, 25, 27, 24, 28, 19],
            [9, 20, 18, 15, 1, 21, 11, 10, 6, 22, 19, 31, 5, 14, 30, 7, 12, 26, 25, 4, 23, 8, 13, 24, 17, 27, 16, 3,32, 2, 28, 29], 
            [4, 16, 25, 18, 1, 31, 23, 7, 12, 6, 24, 20, 11, 9, 29, 17, 19, 14, 30, 2, 26, 21, 3,32, 5, 28, 8, 13, 15, 10, 27, 22], 
            [19, 25, 28, 6,32, 3, 5, 29, 31, 1, 18, 27, 26, 15, 30, 10, 2, 4, 13, 20, 7, 17, 24, 14, 16, 11, 23, 22, 12, 9, 21, 8]], 

           [[29, 6, 7, 8, 25, 3, 15, 13, 20, 4, 19, 14, 21, 2, 11, 23, 30, 1, 10, 27, 18, 22, 31, 5, 17, 16, 26, 12,32, 9, 28, 24], 
            [12, 27, 11, 9, 1, 19, 10, 8, 6, 18,32, 29, 30, 15, 21, 5, 28, 4, 7, 20, 17, 2, 24, 13, 23, 16, 31, 25, 26, 3, 14, 22], 
            [7, 16, 14, 30, 24, 2, 9, 26, 5, 31, 17, 12, 19, 10, 4, 29, 28, 22, 6, 1, 25, 18,32, 3, 20, 11, 8, 13, 15, 23, 21, 27], 
            [32, 22, 20, 15, 8, 18, 14, 25, 11, 2, 10, 4, 17, 7, 12, 31, 23, 19, 30, 21, 3, 29, 13, 24, 26, 28, 1, 5, 16, 9, 6, 27]], 

           [[3, 22, 12, 24, 1, 28, 6, 25, 30, 16, 10,32, 21, 8, 17, 11, 14, 13, 15, 26, 19, 27, 7, 18, 31, 20, 23, 5, 29, 2, 9, 4], 
            [8, 2, 4, 18, 30,32, 26, 9, 3, 23, 29, 14, 11, 12, 10, 28, 6, 21, 27, 1, 25, 7, 15, 17, 13, 20, 22, 31, 19, 5, 24, 16], 
            [28, 8, 7, 3, 9, 12, 24, 26, 17, 5, 29, 19, 4, 14, 25,32, 30, 27, 10, 22, 31, 23, 18, 21, 6, 1, 16, 20, 11, 13, 15, 2], 
            [12, 16, 2, 31, 11, 23, 25, 27, 20, 10, 30, 5, 19, 1, 7, 28, 29, 3,32, 26, 8, 13, 18, 4, 9, 14, 17, 15, 6, 22, 21, 24]], 

           [[19, 27, 2, 31, 30, 21, 4, 12,32, 29, 20, 9, 6, 23, 26, 13, 1, 22, 11, 5, 7, 18, 10, 3, 28, 24, 15, 25, 8, 16, 17, 14], 
            [19, 15, 6, 4, 10,32, 11, 14, 20, 8, 29, 23, 12, 21, 1, 17, 7, 22, 16, 18, 25, 5, 26, 31, 2, 3, 30, 13, 24, 27, 28, 9], 
            [12, 26, 9, 14, 21, 22, 6, 10,32, 23, 15, 17, 5, 18, 31, 13, 25, 30, 28, 11, 27, 19, 4, 16, 1, 2, 7, 29, 8, 3, 20, 24], 
            [10, 1, 4, 6, 8, 2, 26, 22, 25, 7, 11, 27, 31, 23, 9, 15,32, 29, 24, 28, 17, 21, 18, 19, 5, 3, 13, 16, 14, 20, 30, 12]], 

           [[32, 9, 1, 18, 19, 4, 28, 17, 15, 16, 3, 23, 22, 31, 12, 5, 7, 8, 10, 30, 25, 21, 14, 26, 24, 20, 13, 11, 2, 27, 6, 29], 
            [19, 22, 23, 9, 29, 10, 24,32, 17, 11, 28, 16, 14, 2, 12, 18, 6, 7, 30, 27, 4, 5, 1, 31, 20, 21, 15, 8, 3, 13, 25, 26], 
            [5, 26, 14, 21, 24, 3, 17, 9, 20, 1, 8, 19, 10, 13, 28, 31, 22, 12, 15, 4, 11, 16, 6, 2, 30, 29, 25,32, 23, 18, 27, 7], 
            [18, 4, 17, 30, 21, 16, 11, 7, 5, 13, 14, 28, 24, 27, 12, 23, 31, 9, 8,32, 3, 22, 25, 1, 19, 2, 20, 15, 10, 26, 29, 6]], 

           [[14, 11, 5, 24, 20, 31, 6, 28, 7, 4, 22, 18, 12, 27, 21, 17, 26, 8,32, 25, 2, 10, 29, 30, 19, 15, 13, 9, 1, 23, 3, 16], 
            [21, 10, 13, 30, 4, 14, 16, 1, 9, 27, 23, 12, 7, 24, 29, 6, 28, 25, 31, 17, 2, 18, 5, 26, 8, 3, 19, 20,32, 22, 11, 15], 
            [32, 3, 21, 16, 10, 4, 27, 22, 18, 31, 14, 9, 15, 12, 13, 20, 1, 8, 17, 7, 30, 2, 25, 19, 5, 23, 28, 24, 6, 29, 11, 26], 
            [18, 1, 20, 6, 31, 25, 30, 16, 26, 7, 29, 23, 9, 3, 4, 14, 15, 19, 17, 27, 24, 12, 11, 21, 22, 10, 8,32, 2, 5, 28, 13]],

           [[5, 23, 8, 28, 9, 13, 15, 16, 26, 4, 12, 11, 14, 31, 3, 25, 24, 29, 22, 6, 1, 2, 17, 30, 20, 18, 7, 21, 19, 27, 10,32], 
            [12, 31, 27, 16, 22, 26, 4, 8, 10, 2, 7, 15, 25, 13, 17, 24, 28, 5,32, 30, 23, 9, 18, 14, 6, 21, 29, 3, 1, 11, 20, 19], 
            [2, 13, 26, 23, 15, 29, 21, 1, 11, 16, 27, 19,32, 18, 30, 24, 3, 4, 17, 7, 20, 5, 25, 8, 14, 12, 31, 28, 6, 22, 9, 10], 
            [28, 30, 5, 12, 11, 17, 24, 18, 22, 26, 8, 7, 20, 2, 31, 14, 4, 9, 29, 19, 25, 16, 27, 23,32, 21, 10, 6, 13, 3, 1, 15]], 
            
           [[3, 21, 30, 24, 6, 29, 20, 13, 4, 27, 19, 31, 7, 2, 12, 16, 8, 14, 1, 22,32, 5, 28, 23, 17, 26, 18, 25, 15, 9, 10, 11], 
            [1, 21, 11, 29, 22, 17,32, 8, 14, 5, 25, 23, 28, 27, 6, 15, 20, 4, 3, 19, 13, 18, 12, 26, 30, 9, 7, 2, 24, 31, 16, 10], 
            [14, 10, 25, 24, 16, 9, 4,32, 15, 6, 20, 3, 30, 1, 18, 31, 12, 27, 7, 21, 5, 29, 17, 11, 2, 19, 26, 8, 13, 22, 23, 28], 
            [19, 7, 22, 5, 26, 24, 14, 18, 4, 11, 6, 16, 21, 20, 25, 23, 29, 2, 28,32, 27, 30, 8, 10, 31, 17, 12, 15, 3, 13, 1, 9]]]


def hash_string_to_160_bits(input_string):
    # Create a SHA-1 hash object
    sha1 = hashlib.sha1()
    
    # Update the hash object with the bytes of the input string
    sha1.update(input_string.encode())
    
    # Get the digest of the hash (SHA-1 produces 160 bits)
    full_hash = sha1.digest()
    
    # Convert the first 10 bytes (80 bits) to binary
    binary_output = ''.join(format(byte, '08b') for byte in full_hash)
    
    return binary_output

def apply_permutation(input_bits, permutation_table):
    return ''.join(input_bits[i-1] for i in permutation_table)

# Function to rotate the key halves
def rotate_right(key_half, shifts):
    return key_half[:shifts] + key_half[shifts:] 

def generate_subkey(Key_72, round = 16):
    # Apply PC-1 to reduce and permute the 64-bit key to 56 bits
    key_pc1 = apply_permutation(Key_72, PC1)
    sub_keys = []
    for i in range(round):
        # Split the key into two halves
        left_key = key_pc1[:32]
        right_key = key_pc1[32:]

        # Rotate both halves according to the first round shift count
        left_key_rot = rotate_right(left_key, SHIFTS[i])
        right_key_rot = rotate_right(right_key, SHIFTS[i])      

        # Combine the halves and apply PC-2 to generate the ith subkey
        combined_key_rot = left_key_rot + right_key_rot
        subkey_i = apply_permutation(combined_key_rot, PC2)

        sub_keys.append(subkey_i)
    return sub_keys

# Function to apply S-boxes
def apply_sbox(input_bits, sbox):
    row = int(input_bits[0] + input_bits[6], 2)  # Convert outer bits to int
    column = int(input_bits[1:6], 2)  # Convert middle 5 bits to int
    sbox_output = sbox[row][column]
    return format(sbox_output, '05b')  # Convert to 5-bit binary

# Function to calculate f(Rn-1, Kn)
def f_function(right_half_40, subkey_56):
    # Expand the right half from 40 to 56 bits
    expanded_right = apply_permutation(right_half_40, E)

    # XOR expanded right half with the subkey
    xored = ''.join(str(int(a) ^ int(b)) for a, b in zip(expanded_right, subkey_56))
    
    # Split the XORed result into 8 blocks of 6 bits and apply each S-box
    sbox_outputs = []
    for i in range(8):
        sbox_input = xored[i*7:(i+1)*7]
        sbox_output = apply_sbox(sbox_input, S_BOXES[i])
        sbox_outputs.append(sbox_output)

    # Combine all S-box outputs into one 40-bit string
    combined_sbox_output = ''.join(sbox_outputs)
    
    # Return 40-bit output
    return apply_permutation(combined_sbox_output, FINAL_P)


def HoraDES(plaintext_80, Key_72, round = 16):
    # Apply initial permutation
    permuted_plaintext = apply_permutation(plaintext_80, IP) 

    right = []
    left = [] 

    # Right half and left half of the initial permuted plaintext (last 40 bits)
    right_half = permuted_plaintext[40:]
    left_half = permuted_plaintext[:40]

    subkeys = generate_subkey(Key_72)
    for i in range(round):
        if i == 0:
            right.append(''.join(str(int(a) ^ int(b)) for a, b in zip(left_half, f_function(right_half, subkeys[i]))))
            left.append(right_half)
        else:
            right.append(''.join(str(int(a) ^ int(b)) for a, b in zip(left[i-1], f_function(right[i-1], subkeys[i]))))
            left.append(right[i-1])

    encrypted_text = left[len(left) - 1] + right[len(right) - 1]
    return apply_permutation(encrypted_text, IP_1)


plaintext = 'In cryptography a Feistel cipher also known as LubyRackoff block cipher is a symmetric structure used in the construction of block ciphers named after the German born physicist and cryptographer Horst Feistel who did pioneering research while working for IBM it is also commonly known as a Feistel network A large number of block ciphers use the scheme including the US Data Encryption Standard the Soviet Russian GOST and the more recent Blowfish and Twofish ciphers In a Feistel cipher encryption and decryption are very similar operations and both consist of iteratively running a function called a round function a fixed number of time.'
key = '011000100110010101101000011001010111001101101000011101000110100110100011'

binary_hash = hash_string_to_160_bits(plaintext)

left_half = binary_hash[80:]
right_half = binary_hash[:80]

cypher = HoraDES(plaintext_80=left_half,Key_72=key) + HoraDES(plaintext_80=right_half,Key_72=key)
print('plaintext:',plaintext, '\nEncrypted: ',cypher)
