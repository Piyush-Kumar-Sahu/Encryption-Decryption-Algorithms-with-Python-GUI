def encrypt_rail_fence(plaintext, num_rails): # type: ignore
    # Create a 2D list to represent the rails
    rails = [""] * num_rails # type: ignore
    rail = 0  # Current rail
    direction = 1  # Determines the direction (down or up)

    # Assign characters to the rails
    for char in plaintext: # type: ignore
        rails[rail] += char
        rail += direction
        if rail == 0 or rail == num_rails - 1:  # Change direction when hitting rail boundaries
            direction *= -1

    # Concatenate rails to form the ciphertext
    return "".join(rails) # type: ignore


def decrypt_rail_fence(ciphertext, num_rails): # type: ignore
    # Determine the pattern of traversal
    rail_lengths = [0] * num_rails # type: ignore
    rail = 0
    direction = 1

    # Calculate the length of each rail
    for char in ciphertext: # type: ignore
        rail_lengths[rail] += 1
        rail += direction
        if rail == 0 or rail == num_rails - 1:  # Change direction
            direction *= -1

    # Create 2D list to store rails with their respective characters
    rails = []
    index = 0
    for length in rail_lengths: # type: ignore
        rails.append(ciphertext[index:index + length]) # type: ignore
        index += length # type: ignore

    # Read the characters in zigzag order to form the plaintext
    plaintext = ""
    rail_pointers = [0] * num_rails  # type: ignore # Pointers to track current position in each rail
    rail = 0
    direction = 1
    for _ in range(len(ciphertext)): # type: ignore
        plaintext += rails[rail][rail_pointers[rail]] # type: ignore
        rail_pointers[rail] += 1
        rail += direction
        if rail == 0 or rail == num_rails - 1:  # Change direction
            direction *= -1

    return plaintext # type: ignore


'''# Input from the user
plaintext = input("Enter the plaintext: ")
num_rails = int(input("Enter the number of rails: "))

# Encryption
ciphertext = encrypt_rail_fence(plaintext, num_rails)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = decrypt_rail_fence(ciphertext, num_rails) # type: ignore
print("Decrypted Text:", decrypted_text) # type: ignore'''