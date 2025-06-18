import tkinter as tk
from tkinter import ttk, messagebox
from thame import setup_theme  # <- Theme setup imported here

import ceasar_Cipher as cc
import monoalphabetic_cipher as mc
import Playfire_Cipher as pc
import Affine_Cipher as ac
import auto_key_encryption as akc
import Hill_Cipher as hc
import rail_fence as rfc
import row_transposition as rtc

def process_cipher():
    text = plaintext_entry.get().strip()
    key = key_entry.get().strip()
    mode = mode_entry.get().strip().lower()
    selected = list_box.curselection()

    if not text or not key or not selected or mode not in ('e', 'd'):
        messagebox.showerror("Missing Info", "Fill all fields correctly and select a cipher. Use 'e' or 'd' for mode.")
        return

    cipher_name = list_box.get(selected[0])
    result = ""

    try:
        if cipher_name == "Ceasar Cipher":
            if mode == 'e':
                result = cc.caesar_cipher(text, int(key))
            else:
                result = cc.caesar_decipher(text, int(key))

        elif cipher_name == "Monoalphabetic Cipher":
            plain_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
            key_mapping = dict(zip(plain_alphabet, cipher_alphabet))
            if mode == 'e':
                result = mc.monoalphabetic_encrypt(text, key_mapping)
            else:
                result = mc.monoalphabetic_decrypt(text, key_mapping)

        elif cipher_name == "Playfair Cipher":
            if mode == 'e':
                result = pc.playfair_encrypt(text, key)
            else:
                result = pc.playfair_decrypt(text, key)

        elif cipher_name == "Affine Cipher":
            try:
                a, b = map(int, key.split(','))
            except:
                messagebox.showerror("Invalid Key", "Enter key as two comma-separated numbers (e.g., 5,8)")
                return
            if mode == 'e':
                result = ac.affine_encrypt(text, a, b)
            else:
                result = ac.affine_decrypt(text, a, b)

        elif cipher_name == "Auto-key Cipher":
            if mode == 'e':
                result = akc.auto_key_encrypt(text, key)
            else:
                result = akc.auto_key_decrypt(text, key)

        elif cipher_name == "Hill Cipher":
            if mode == 'e':
                result = hc.hill_cipher_encrypt(text, key)
            else:
                result = hc.hill_cipher_decrypt(text, key)

        elif cipher_name == "Rail Fence Cipher":
            if mode == 'e':
                result = rfc.encrypt_rail_fence(text, int(key))
            else:
                result = rfc.decrypt_rail_fence(text, int(key))

        elif cipher_name == "Row Transposition":
            if mode == 'e':
                result = rtc.encrypt_row_transposition(text, key)
            else:
                result = rtc.decrypt_row_transposition(text, key)

        else:
            result = "Cipher not implemented."

        output_var.set(result)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Encrypt-Decrypt Tool")
setup_theme(root)  # <- Apply the theme

# Plaintext
ttk.Label(root, text="Plaintext:").grid(row=0, column=0, sticky='w')
plaintext_entry = ttk.Entry(root, width=40)
plaintext_entry.grid(row=0, column=1)

# Key
ttk.Label(root, text="Key:").grid(row=1, column=0, sticky='w')
key_entry = ttk.Entry(root, width=40)
key_entry.grid(row=1, column=1)

# Mode
ttk.Label(root, text="Encrypt or Decrypt (e/d):").grid(row=2, column=0, sticky='w')
mode_entry = ttk.Entry(root, width=40)
mode_entry.grid(row=2, column=1)

# Cipher selection
ttk.Label(root, text="Choose Cipher:").grid(row=3, column=0, sticky='nw')
list_box = tk.Listbox(root, height=8, selectmode=tk.SINGLE)
list_box.grid(row=3, column=1, padx=5, pady=5)

cipher_options = [
    'Ceasar Cipher', 'Monoalphabetic Cipher', 'Playfair Cipher',
    'Affine Cipher', 'Auto-key Cipher', 'Hill Cipher',
    'Rail Fence Cipher', 'Row Transposition'
]
for i, option in enumerate(cipher_options):
    list_box.insert(i, option)

# Result
ttk.Label(root, text="Result:").grid(row=5, column=0, sticky='w')
output_var = tk.StringVar()
output_entry = ttk.Entry(root, textvariable=output_var, width=40, state="readonly")
output_entry.grid(row=5, column=1)

# Button
process_button = ttk.Button(root, text="Encrypt/Decrypt", command=process_cipher)
process_button.grid(row=4, column=1, pady=10)

root.mainloop()
