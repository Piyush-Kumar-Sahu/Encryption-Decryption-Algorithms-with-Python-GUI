def encrypt_row_transposition(plaintext, key): # type: ignore
    # Remove spaces and convert plaintext to uppercase
    plaintext = plaintext.replace(" ", "").upper() # type: ignore

    # Determine the number of rows needed
    num_cols = len(key) # type: ignore
    num_rows = len(plaintext) // num_cols + (len(plaintext) % num_cols > 0) # type: ignore

    # Fill the grid with plaintext, padding with X if necessary
    grid = [plaintext[i:i+num_cols] for i in range(0, len(plaintext), num_cols)] # type: ignore
    if len(grid[-1]) < num_cols: # type: ignore
        grid[-1] += "X" * (num_cols - len(grid[-1])) # type: ignore

    # Sort columns based on key and encrypt
    ciphertext = ""
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k]) # type: ignore
    for col in sorted_key_indices:
        for row in grid: # type: ignore
            ciphertext += row[col] # type: ignore

    return ciphertext# type: ignore


def decrypt_row_transposition(ciphertext, key): # type: ignore
    # Determine the number of rows and columns
    num_cols = len(key) # type: ignore
    num_rows = len(ciphertext) // num_cols # type: ignore

    # Create an empty grid to decrypt
    grid = ['' for _ in range(num_cols)]
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k]) # type: ignore

    # Fill the grid column by column based on the key
    index = 0
    for col in sorted_key_indices:
        grid[col] = ciphertext[index:index+num_rows]
        index += num_rows

    # Read the grid row by row to form the plaintext
    plaintext = ""
    for row in range(num_rows):
        for col in range(num_cols):
            if row < len(grid[col]):  # Avoid padding characters
                plaintext += grid[col][row]

    return plaintext.rstrip("X")  # Remove padding


'''# Input from the user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key (as a sequence of numbers, e.g., '3124'): ")

# Encryption
ciphertext = encrypt_row_transposition(plaintext, key)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = decrypt_row_transposition(ciphertext, key)
print("Decrypted Text:", decrypted_text)'''