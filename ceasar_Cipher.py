#Caesar cipher
def caesar_cipher(text, shift, encrypt=True): # type: ignore
    result = ""
    # Adjust shift for decryption
    if not encrypt:
        shift = -shift # type: ignore

    for char in text: # type: ignore
        if char.isalpha():  # type: ignore # Check if the character is a letter
            start = ord('A') if char.isupper() else ord('a') # type: ignore
            # Perform the shift and wrap around using modulo
            new_char = chr((ord(char) - start + shift) % 26 + start) # type: ignore
            result += new_char # type: ignore
        else:
            # Keep non-alphabetic characters as they are
            result += char # type: ignore

    return result # type: ignore

def caesar_decipher(text, shift, encrypt=False): # type: ignore
    result = ""
    # Adjust shift for decryption
    if not encrypt:
        shift = -shift # type: ignore

    for char in text: # type: ignore
        if char.isalpha():  # type: ignore # Check if the character is a letter
            start = ord('A') if char.isupper() else ord('a') # type: ignore
            # Perform the shift and wrap around using modulo
            new_char = chr((ord(char) - start + shift) % 26 + start) # type: ignore
            result += new_char # type: ignore
        else:
            # Keep non-alphabetic characters as they are
            result += char # type: ignore

    return result # type: ignore

# Main program
'''choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
if choice == 'E':
    text = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_message = caesar_cipher(text, shift)
    print("Encrypted message:", encrypted_message)
elif choice == 'D':
    text = input("Enter the message to decrypt: ")
    shift = int(input("Enter the shift value: "))
    decrypted_message = caesar_decipher(text, shift)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
'''