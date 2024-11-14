def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Decryption is encryption with a negative shift

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to encrypt or decrypt a message? (e/d): ").strip().lower()
    if choice not in ('e', 'd'):
        print("Invalid choice. Please select 'e' for encryption or 'd' for decryption.")
        return

    message = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (0-25): "))
        if not 0 <= shift < 26:
            print("Shift value must be between 0 and 25.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for the shift value.")
        return

    if choice == 'e':
        result = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
