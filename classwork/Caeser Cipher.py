"""Create a Python file named caesar_cipher.py
Prompt the user to enter the plaintext message to encrypt.
Prompt the user to enter the secret key, which must be between 1 and 26 (inclusive).
For each charater in the message plaintext, do the following:
Check whether a letter using the string isalpha() method.
If not a letter, add the character unchanged to the ciphertext.
If a letter, check whether it is a capital or lowercase letter using the string isupper() and islower() methods.
Maintain the letter casing, move the letter up the alphabet (using the Caesar Cipher key), thereby substituting the letter.
For uppercase letters, start with the ASCII value or uppercase A by using the ord() function and for lowercase, start with the ASCII value for 'a' using the ord() function.
In case the movement makes it past the end of the alphabet, wrap around to the beginning.
Add the new letter to the ciphertext.
Finally, print out the final cipher text"""

plaintext_message = input ('Enter secret message')
secret_key = int(input('Enter a number from 1-26 for secret key: '))
ciphertext = ''



for char in plaintext_message:
    if char.isalpha():
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        new_pos = (ord(char) - start + secret_key) % 26 + start
        new_char = chr(new_pos)
        ciphertext += new_char
    else:
        ciphertext += char

print(f'The ciphertext is: {ciphertext}')