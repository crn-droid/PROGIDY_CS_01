#Caesar Cipher Program

def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
          if char.issupper():
            encrypted_char = chr((ord(char) - ord('A')))
def caesar_decrypt(text,shift):
    pass

def main():
    pass

if __name__ = "__main__":
    main()

