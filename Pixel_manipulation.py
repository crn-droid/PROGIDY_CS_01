from PIL import Image
import random

# This is to load an image and convert it into a pixel-accessible format

def load_image(path):
    img= Image.open(path)
    img= img.convert('RGB')
    return img

# I will encrypt by swapping pixels based on pseudorandom sequence
# I will also use simple XOR operation on the pixel for extra security


def encrypt_image(img,key):
    pixels =img.load()
    width, height = img.size
  
#Creates a lists of  positions taking the width and the height
    positions = [(x,y) for y in range(height) for x in range(width)]

# random seed using key makes it reproduceable 
    random.seed(key)
    random.shuffle(positions)

    encrypted_img = Image.new('RGB', (width, height))
    encrypted_pixels = encrypted_img.load()

    for i, (x, y) in enumerate(positions):
        orig_x, orig_y = i % width, i // width
        r, g, b = pixels[orig_x, orig_y]
        # Apply XOR operation with key (mod 256)
        r_enc = r ^ (key & 0xFF)
        g_enc = g ^ (key & 0xFF)
        b_enc = b ^ (key & 0xFF)
        encrypted_pixels[x, y] = (r_enc, g_enc, b_enc)
    
    return encrypted_img

def decrypt_image(img, key):
    pixels = img.load()
    width, height = img.size
    
    positions = [(x, y) for y in range(height) for x in range(width)]
    
    # Use the key as seed for reproducible shuffling
    random.seed(key)
    random.shuffle(positions)
    
    decrypted_img = Image.new('RGB', (width, height))
    decrypted_pixels = decrypted_img.load()
    
    for i, (x, y) in enumerate(positions):
        r_enc, g_enc, b_enc = pixels[x, y]
        # Reverse XOR operation
        r_dec = r_enc ^ (key & 0xFF)
        g_dec = g_enc ^ (key & 0xFF)
        b_dec = b_enc ^ (key & 0xFF)
        
        orig_x, orig_y = i % width, i // width
        decrypted_pixels[orig_x, orig_y] = (r_dec, g_dec, b_dec)
    
    return decrypted_img

from colorama import init, Fore, Style
init(autoreset=True)

def get_numeric_key():
    while True:
        try:
            key_input = input( "Enter a numeric key (1-9999): " + Style.RESET_ALL)
            key = int(key_input)
            if 1 <= key <= 9999:
                return key
            else:
                print(Fore.RED + "Error: Key must be between 1 and 9999." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Error: Invalid input, enter a number." + Style.RESET_ALL)

def get_input_filename(prompt):
    while True:
        filename = input(Fore.CYAN + prompt + Style.RESET_ALL)
        try:
            with open(filename, 'rb') as f:
                return filename
        except FileNotFoundError:
            print(Fore.RED + "Error: File not found. Try again." + Style.RESET_ALL)

def menu():
    print("IMAGE ENCRYPTION")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")
    print("")

def main():
    while True:
        menu()
        choice = input(Fore.YELLOW + "Enter your choice (1-3): "  )
        
        if choice == '1':
            key = get_numeric_key()
            input_path = get_input_filename(" Enter the filename of the image to encrypt: ")
            img = load_image(input_path)
            print(Fore.YELLOW + "[INFO] Encrypting image...")
            encrypted_img = encrypt_image(img, key)
            encrypted_img.save('encrypted_image.png')
            print(Fore.GREEN + "[SUCCESS] Encrypted image saved as 'encrypted_image.png'")

        elif choice == '2':
            key = get_numeric_key()
            input_path = get_input_filename(" Enter the filename of the image to decrypt: ")
            img = load_image(input_path)
            print(Fore.YELLOW + "[INFO] Decrypting image...")
            decrypted_img = decrypt_image(img, key)
            decrypted_img.save('decrypted_image.png')
            print(Fore.GREEN + "[SUCCESS] Decrypted image saved as 'decrypted_image.png'")

        elif choice == '3':
            print(Fore.GREEN + "Exiting program. Keep your key secure!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." )

if __name__ == "__main__":
    main()
