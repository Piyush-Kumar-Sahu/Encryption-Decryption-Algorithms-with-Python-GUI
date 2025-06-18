# playfair_cipher.py

def generate_key_table(key):
    key = key.upper().replace('J', 'I')
    key += "ABCDEFGHIKLMONPQRSTUVWXYZ"
    key_table = []

    for char in key:
        if char not in key_table:
            key_table.append(char)

    key_table_2d = [key_table[i:i + 5] for i in range(0, 25, 5)]
    return key_table_2d

def format_message(msg):
    msg = msg.upper().replace('J', 'I').replace(' ', '')
    formatted_msg = ""
    i = 0

    while i < len(msg):
        char1 = msg[i]
        char2 = msg[i + 1] if i + 1 < len(msg) else 'X'

        if char1 == char2:
            formatted_msg += char1 + 'X'
            i += 1
        else:
            formatted_msg += char1 + char2
            i += 2

    if len(formatted_msg) % 2 != 0:
        formatted_msg += 'X'

    return formatted_msg

def find_position(key_table, char):
    for i, row in enumerate(key_table):
        if char in row:
            return i, row.index(char)
    raise ValueError(f"Character '{char}' not found in key table.")

def encrypt_pair(key_table, pair):
    row1, col1 = find_position(key_table, pair[0])
    row2, col2 = find_position(key_table, pair[1])

    if row1 == row2:
        return key_table[row1][(col1 + 1) % 5] + key_table[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return key_table[(row1 + 1) % 5][col1] + key_table[(row2 + 1) % 5][col2]
    else:
        return key_table[row1][col2] + key_table[row2][col1]

def decrypt_pair(key_table, pair):
    row1, col1 = find_position(key_table, pair[0])
    row2, col2 = find_position(key_table, pair[1])

    if row1 == row2:
        return key_table[row1][(col1 - 1) % 5] + key_table[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return key_table[(row1 - 1) % 5][col1] + key_table[(row2 - 1) % 5][col2]
    else:
        return key_table[row1][col2] + key_table[row2][col1]

def playfair_encrypt(key, message):
    key_table = generate_key_table(key)
    formatted_message = format_message(message)
    encrypted_message = ""

    for i in range(0, len(formatted_message), 2):
        encrypted_message += encrypt_pair(key_table, formatted_message[i:i + 2])

    return encrypted_message

def playfair_decrypt(key, ciphertext):
    key_table = generate_key_table(key)
    decrypted_message = ""

    for i in range(0, len(ciphertext), 2):
        decrypted_message += decrypt_pair(key_table, ciphertext[i:i + 2])

    return decrypted_message
