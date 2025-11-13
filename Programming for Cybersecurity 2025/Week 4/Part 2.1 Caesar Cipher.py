# Erya Puput Anom
# B01834949
# Lab - Caesar Cipher Encryption
# This program encrypts text using the Caesar cipher method
# by shifting letters in the alphabet by a user-specified amount.

# WHY:
# The Caesar cipher is one of the oldest encryption techniques.
# It works by replacing each letter with another letter
# that is a fixed number of positions further down the alphabet.
# For example, a shift of 3 changes:
# A → D, B → E, C → F, and so on.


# Define the alphabet used for encryption
# WHY: The Caesar cipher only shifts letters from 'a' to 'z'.
#      We use this to find the position (index) of each letter.
alphabet = 'abcdefghijklmnopqrstuvwxyz'



# FUNCTION: encrypt()
# WHY: This function performs the encryption process.
#      It takes a text (plaintext) and a shift value (k),
#      and returns the encrypted text (ciphertext).
def encrypt(plaintext, k):
    # plaintext: text to encrypt
    # k: shift value (number of letters to move in the alphabet)

    ciphertext = ''  # Start with an empty string to store the encrypted result
    print("\n--- Encryption Process ---")

    # Loop through every character in the plaintext (converted to lowercase)
    for char in plaintext.lower():
        # Check if the character is a letter (a–z)
        if char in alphabet:
            # Find the position (index) of the character in the alphabet
            old_index = alphabet.index(char)

            # Compute the new position after shifting by 'k'
            # WHY: We use modulo 26 so that the alphabet wraps around.
            # Example: shifting 'z' by 1 → (25 + 1) % 26 = 0 → 'a'
            new_index = (old_index + k) % 26

            # Find the new letter from the shifted index
            new_char = alphabet[new_index]

            # Show the encryption step for clarity
            print(f"'{char}' -> index {old_index} -> shifted {k} -> new index {new_index} -> '{new_char}'")

            # Add the new encrypted letter to the ciphertext
            ciphertext += new_char
        else:
            # Keep non-alphabet characters (spaces, punctuation, digits) unchanged
            # WHY: Caesar cipher only works on letters, not symbols or numbers.
            print(f"'{char}' (non-letter) remains unchanged")
            ciphertext += char

    # Return the final encrypted message
    return ciphertext



# MAIN PROGRAM: Interactive Loop
# WHY: This loop allows the user to repeatedly encrypt new messages
#      until they decide to type 'stop' and quit.
while True:
    # Ask the user for input text
    plaintext = input("\nEnter your plaintext (or type 'stop' to quit): ").strip()

    # Allow the user to exit the program gracefully
    if plaintext.lower() == "stop":
        print("Goodbye! 👋")
        break

    # Ask the user for a shift value (must be an integer)
    try:
        shift = int(input("Enter shift value (e.g., 1, 2, 3...): "))
    except ValueError:
        # WHY: To prevent the program from crashing if the user enters text instead of a number
        print("Please enter a valid number for the shift.")
        continue  # Ask again

    # Encrypt the plaintext using the Caesar cipher function
    ciphertext = encrypt(plaintext, shift)

    # Display the final result
    print("\nPlaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("-" * 40)  # Print a line for neat separation
