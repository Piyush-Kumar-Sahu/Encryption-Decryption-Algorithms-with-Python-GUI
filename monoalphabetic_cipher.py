plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Create key mapping dictionary
key_mapping = dict(zip(plain_alphabet, cipher_alphabet))

def monoalphabetic_encrypt(plaintext, key_mapping):
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += key_mapping[char]
        else:
            ciphertext += char
    return ciphertext

def monoalphabetic_decrypt(ciphertext, key_mapping):
    reverse_mapping = {v: k for k, v in key_mapping.items()}
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += reverse_mapping[char]
        else:
            plaintext += char
    return plaintext


'''mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
text = input("Enter the text: ")

if mode == 'e':
    result = monoalphabetic_encrypt(text, key_mapping)
    print("Encrypted text:", result)
elif mode == 'd':
    result = monoalphabetic_decrypt(text, key_mapping)
    print("Decrypted text:", result)
else:
    print("Invalid mode.")
'''