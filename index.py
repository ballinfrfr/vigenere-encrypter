import tkinter as tk
from tkinter import messagebox

def vigenere_cipher(text, key, decrypt=False):
    key = key.lower()
    key_index = 0
    result = ''
    for char in text:
        if char.isalpha():
            if decrypt:
                char_offset = (ord(char) - ord(key[key_index]) + 26) % 26
            else:
                char_offset = (ord(char) + ord(key[key_index]) - 2 * ord('a')) % 26
            result += chr(char_offset + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def encrypt():
    plaintext = plaintext_entry.get().lower()
    keyword = keyword_entry.get().lower()
    encrypted_message = vigenere_cipher(plaintext, keyword)
    encrypted_text.delete("1.0", tk.END)
    encrypted_text.insert(tk.END, encrypted_message)

def clear():
    plaintext_entry.delete(0, tk.END)
    keyword_entry.delete(0, tk.END)
    encrypted_text.delete("1.0", tk.END)

def about():
    messagebox.showinfo("About", "Vigenère Cipher GUI App\nCreated by [Your Name]")

# Create the main window
root = tk.Tk()
root.title("Vigenère Cipher")

# Create and place widgets
tk.Label(root, text="Plain Text:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
plaintext_entry = tk.Entry(root)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Keyword:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
keyword_entry = tk.Entry(root)
keyword_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")

tk.Label(root, text="Encrypted Text:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
encrypted_text = tk.Text(root, height=5, width=30)
encrypted_text.grid(row=3, column=1, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Start the main event loop
root.mainloop()
