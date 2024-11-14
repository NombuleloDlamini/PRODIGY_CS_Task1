# Task 1: Caesar Cipher Program
This task provides a program to encrypt or decrypt text using the Caesar cipher
method.
- caesar_cipher_encrypt(text, shift): This function encrypts a given `text` by
shifting each letter by a specified `shift` value. If the character is uppercase, it shifts
within the uppercase range; if lowercase, within the lowercase range. Non-alphabetic
characters remain unchanged.
- caesar_cipher_decrypt(text, shift): This function decrypts text encrypted with the
Caesar cipher by reversing the shift. It calls the encryption function with a negative
shift.
- main(): This function is the program's entry point. It prompts the user to choose
encryption or decryption, then requests a message and a shift value (between 0 and
25). Based on the choice, it either encrypts or decrypts the message and displays
the result.
