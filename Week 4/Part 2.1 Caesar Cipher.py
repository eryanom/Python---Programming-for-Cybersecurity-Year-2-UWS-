#Erya Anom

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k)
    ciphertext = ''
    for char in plaintext.lower():
        if char in alphabet:
            #find the position of the character in the alphabet
            new_pos = (alphabet.index(char) + k) % 26
            ciphertext += alphabet[new_pos]
        else:
            #Non-alphabet characters remain unchanged
            ciphertext += char
        return ciphertext


#Example usage:
plaintext = "Hello Erya World"
shift = 3
ciphertext = encrypt(plaintext, shift)