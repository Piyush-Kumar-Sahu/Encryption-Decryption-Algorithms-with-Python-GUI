# Function to convert a letter to its corresponding index (A=0, B=1, ..., Z=25)
def char_to_num(c): # type: ignore
    return ord(c.upper()) - ord('A') # type: ignore

# Function to convert an index back to a letter
def num_to_char(n): # type: ignore
    return chr(n + ord('A')) # type: ignore

# Function to find the modular inverse of a number mod 26
def mod_inv(a): # type: ignore
    for x in range(26):
        if (a * x) % 26 == 1:
            return x
    return None

# Affine cipher encryption function
def affine_encrypt(plaintext, a, b): # type: ignore
    return ''.join([num_to_char((a * char_to_num(c) + b) % 26) for c in plaintext if c.isalpha()]) # type: ignore

# Affine cipher decryption function
def affine_decrypt(ciphertext, a, b): # type: ignore
    a_inv = mod_inv(a) # type: ignore
    return ''.join([num_to_char((a_inv * (char_to_num(c) - b)) % 26) for c in ciphertext]) # type: ignore

'''# Example usage:

# Keys for the Affine cipher
a, b = 5, 8  # 'a' must be coprime with 26

# Sample plaintext
plaintext = "HELLO"

# Encrypt the plaintext
encrypted_text = affine_encrypt(plaintext, a, b)
print(f"Encrypted text: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = affine_decrypt(encrypted_text, a, b)
print(f"Decrypted text: {decrypted_text}")'''
