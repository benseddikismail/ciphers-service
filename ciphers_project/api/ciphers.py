def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            c_encoded = chr((ord(c) - base + shift) % 26 + base)
        else:
            c_encoded = c
        cipher_text += c_encoded
    return cipher_text
