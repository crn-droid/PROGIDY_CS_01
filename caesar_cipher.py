# Caesar Cipher Program  
def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                # shift uppercase letters (A=65 to Z=90)
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift lowercase letters (a=97 to z=122)
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            encrypted_text += encrypted_char
        else:
            # keeping other characters as they are
            encrypted_text += char
    
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("CAESAR CIPHER PROGRAM")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    while True:
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == '1':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted = caesar_encrypt(message, shift)
            print(f"Encrypted message: {encrypted}")
        
        elif choice == '2':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value that was used: "))
            decrypted = caesar_decrypt(message, shift)
            print(f"Decrypted message: {decrypted}")
        
        elif choice == '3':
            print("Mission Complete!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()