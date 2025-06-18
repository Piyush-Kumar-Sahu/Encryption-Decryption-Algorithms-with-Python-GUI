def auto_key_encrypt(plaintext, key): # type: ignore
    # Extend the key with the plaintext
    key = key + plaintext[:-len(key)] # type: ignore
    ciphertext = ""

    for p, k in zip(plaintext, key): # type: ignore
        if p.isalpha():  # Only encrypt alphabetic characters # type: ignore
            p_upper = p.upper() # type: ignore
            k_upper = k.upper() # type: ignore
            ciphertext += chr(((ord(p_upper) - 65) + (ord(k_upper) - 65)) % 26 + 65) # type: ignore
        else:
            ciphertext += p  # Keep non-alphabetic characters unchanged # type: ignore
    return ciphertext # type: ignore


def auto_key_decrypt(ciphertext, key): # type: ignore
    plaintext = ""

    for i, c in enumerate(ciphertext): # type: ignore
        if c.isalpha():  # Only decrypt alphabetic characters # type: ignore
            c_upper = c.upper() # type: ignore
            k_upper = key[i].upper() # type: ignore
            p = chr(((ord(c_upper) - 65) - (ord(k_upper) - 65)) % 26 + 65) # type: ignore
            plaintext += p # type: ignore
            key += p  # Update the key with the plaintext characters# type: ignore
        else:
            plaintext += c  # Keep non-alphabetic characters unchanged # type: ignore
    return plaintext # type: ignore


'''# Input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encryption
ciphertext = auto_key_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = auto_key_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
'''