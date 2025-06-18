#hill cipher
import numpy as np

# Function to encrypt the plaintext
def hill_cipher_encrypt(plaintext, key_matrix): # type: ignore
    # Convert plaintext into numerical values (A=0, B=1, ..., Z=25)
    plaintext = plaintext.upper().replace(" ", "") # type: ignore
    if len(plaintext) % 2 != 0: # type: ignore
        plaintext += 'X'  # type: ignore # Padding with 'X' if the plaintext length is odd

    print(f"Processed plaintext (with padding if needed): {plaintext}")

    plaintext_segments = [
        [ord(plaintext[i]) - 65, ord(plaintext[i + 1]) - 65] # type: ignore
        for i in range(0, len(plaintext), 2) # type: ignore
    ]

    print("\nPlaintext segments:")
    for idx, segment in enumerate(plaintext_segments):
        print(f"Segment {idx + 1}: {segment}")

    ciphertext = ""
    print("\nCalculations for ciphertext:")
    for idx, segment in enumerate(plaintext_segments):
        print(f"\nStep {idx + 1}:")
        print(f"Key Matrix:\n{key_matrix}")
        print(f"Plaintext Segment: {segment}")

        # Multiply key matrix with the segment
        raw_result = np.dot(key_matrix, segment) # type: ignore
        print(f"Matrix Multiplication Result: {raw_result}")

        # Apply mod 26 to each number
        segment_vector = raw_result % 26
        print(f"Result after Mod 26: {segment_vector}")

        # Convert numerical values to letters
        ciphertext_segment = ''.join(chr(val + 65) for val in segment_vector)
        print(f"Ciphertext Segment: {ciphertext_segment}")

        ciphertext += ciphertext_segment

    return ciphertext

# Function to decrypt the ciphertext
def hill_cipher_decrypt(ciphertext, key_matrix):
    # Compute the inverse of the key matrix modulo 26
    det = int(np.linalg.det(key_matrix)) % 26
    det_inv = pow(det, -1, 26)  # Compute modular inverse of determinant
    
    adj_matrix = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inverse_matrix = (det_inv * adj_matrix) % 26

    ciphertext_segments = [
        [ord(ciphertext[i]) - 65, ord(ciphertext[i + 1]) - 65]
        for i in range(0, len(ciphertext), 2)
    ]

    decrypted_text = ""
    for segment in ciphertext_segments:
        segment_vector = np.dot(inverse_matrix, segment) % 26
        decrypted_text += ''.join(chr(val + 65) for val in segment_vector)

    return decrypted_text

# Input 2x2 key matrix as a single line
def get_key_matrix():
    print("Enter the 2x2 key matrix as 4 space-separated integers (e.g., 3 3 2 5):")
    values = list(map(int, input("Key: ").strip().split()))
    if len(values) != 4:
        raise ValueError("You must enter exactly 4 integers.")
    return np.array(values).reshape(2, 2)


# Main function
'''if __name__ == "__main__":
    try:
        # Input key matrix
        key_matrix = get_key_matrix() # type: ignore

        # Check if the determinant of the matrix is coprime with 26
        det = int(np.linalg.det(key_matrix)) % 26 # type: ignore
        if np.gcd(det, 26) != 1:
            raise ValueError("The determinant of the key matrix must be coprime with 26.")

        # Input plaintext
        plaintext = input("Enter the plaintext: ").strip()

        # Encryption
        ciphertext = hill_cipher_encrypt(key_matrix, plaintext)
        print(f"\nFinal Ciphertext: {ciphertext}")

    except ValueError as e:
        print(f"Error: {e}")'''