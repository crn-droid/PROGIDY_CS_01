# Caesar Cipher Program - Advanced

def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    #So that we can work with higher number value shifts 
    shift = shift % 26  

    for char in text:
        if char.isalpha():
            if char.isupper():
               
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def brute_force_decrypt(text):
    print("\n BRUTE FORCE DECRYPTION ")
    print("Trying all possible shifts:\n")
    
    results = []
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        results.append(f"Shift {shift:2d}: {decrypted}")
        print(f"Shift {shift:2d}: {decrypted}")
    
    return results


def encrypt_file(filename, shift):
    try:
        # Reading a file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        encrypted_content = caesar_encrypt(content, shift)
        
        output_filename = f"encrypted_{filename}"
        
        # Writing into a file
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(encrypted_content)
        
        print(f"File encrypted and saved as: {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error processing file: {e}")


def decrypt_file(filename, shift):
    try:
        # Reading a file

        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        decrypted_content = caesar_decrypt(content, shift)
        
        output_filename = f"decrypted_{filename}"

        # Writing into a file

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(decrypted_content)
        
        print(f"File decrypted and saved as: {output_filename}")
    
    except FileNotFoundError:
        # Fixed: Added space in error message
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error processing file: {e}")


def get_shift_value():
    while True:
        try:
            shift = int(input("Enter shift value: "))
            return shift
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_user_choice():
    valid_choices = ['1', '2', '3', '4', '5','6','7']
    while True:
        choice = input("\nChoose an option (1-5): ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")


def display_menu():
    print("\n" + "="*40)
    print("       CAESAR CIPHER PROGRAM")
    print("="*40)
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute force decrypt (try all shifts)")
    print("4. Encrypt a File")
    print("5. Decrypt a File")
    print("6. About Caesar Cipher")
    print("7. Exit")
    print("="*40)


def show_about():
    """Displays information about the Caesar Cipher."""
    print("\n" + "="*50)
    print("              ABOUT CAESAR CIPHER")
    print("="*50)
    print("The Caesar Cipher is one of the oldest known encryption")
    print("techniques. It's named after Julius Caesar, who used it")
    print("to protect his military communications.")
    print()
    print("HOW IT WORKS:")
    print("• Each letter is shifted by a fixed number of positions")
    print("• Example: With shift 3, A→D, B→E, C→F, etc.")
    print("• Non-letters (spaces, punctuation) remain unchanged")
    print()
    print("SECURITY:")
    print("• Very easy to break (only 26 possible keys)")
    print("• Used for educational purposes and simple puzzles")
    print("• Modern encryption uses much more complex methods")
    print("="*50)


def encrypt_mode():
    print("\n--- ENCRYPTION MODE ---")
    message = input("Enter message to encrypt: ")
    if not message.strip():
        print("Error: Empty message!")
        return
    
    shift = get_shift_value()
    encrypted = caesar_encrypt(message, shift)
    
    print(f"\nOriginal message:  {message}")
    print(f"Shift value:       {shift}")
    print(f"Encrypted message: {encrypted}")


def decrypt_mode():
    print("\n--- DECRYPTION MODE ---")
    message = input("Enter message to decrypt: ")
    if not message.strip():
        print("Error: Empty message!")
        return
    
    shift = get_shift_value()
    decrypted = caesar_decrypt(message, shift)
    
    print(f"\nEncrypted message: {message}")
    print(f"Shift value:       {shift}")
    print(f"Decrypted message: {decrypted}")


def brute_force_mode():
    print("\n--- BRUTE FORCE MODE ---")
    message = input("Enter encrypted message: ")
    if not message.strip():
        print("Error: Empty message!")
        return
    
    print(f"\nTrying to crack: '{message}'")
    brute_force_decrypt(message)
    print("\nLook for the result that makes the most sense!")

def get_file_from_user():
    print("\n--- SELECT FILE ---")
    print("Enter the full path to your file:")
    print("Examples:")
    print("  Windows: C:\\Users\\YourName\\Documents\\myfile.txt")
    print("  Mac/Linux: /home/username/Documents/myfile.txt")
    print("  Same folder: just type filename.txt")
    
    filename = input("\nFile path: ").strip()
    return filename

def file_encryption_mode():
   file = get_file_from_user()
   shift = get_shift_value()
   encrypt_file(file,shift)

def file_decryption_mode():
    file = get_file_from_user()
    shift = get_shift_value()
    decrypt_file(file,shift)

def main():
    """Main program loop."""
    print("Welcome to the Caesar Cipher Program!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            encrypt_mode()
        elif choice == '2':
            decrypt_mode()
        elif choice == '3':
            brute_force_mode()
        elif choice == '4':
            file_encryption_mode() 
        elif choice == '5':
            file_decryption_mode()
        elif choice == '6':
           show_about()
        elif choice == '7':
            print("\nThank you for using Caesar Cipher Program!")
            print("Goodbye! 🔐")
            break



if __name__ == "__main__":
    main()