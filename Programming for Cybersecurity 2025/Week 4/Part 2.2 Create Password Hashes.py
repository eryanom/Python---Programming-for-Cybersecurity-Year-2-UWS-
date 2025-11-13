from hashlib import sha256
# Import the SHA-256 algorithm from Python's hashlib library.
# WHY: In cybersecurity, we use hashing algorithms like SHA-256
# to securely store passwords without saving them in plain text.


# Function 1: hash_password()

def hash_password(password: str) -> str:
    """Return a hex SHA-256 hash of the given password."""

    # Convert the password (string) into bytes using UTF-8 encoding,
    # then hash it using SHA-256 algorithm.
    hashed = sha256(password.encode('utf-8')).hexdigest()

    # Display the original password and its corresponding hash
    # WHY: This helps visualize how hashing transforms text into an irreversible fixed-length value.
    print(f"Hashing password: '{password}' -> {hashed}")

    # Return the resulting hash string
    return hashed


# Function 2: collect_users_and_hashes()

def collect_users_and_hashes():
    """
    Use a while loop to enter username/password pairs.
    - Blank username finishes input.
    - Stores usernames and password hashes in separate lists.
    """

    # Initialise empty lists to store data
    usernames = []          # List for storing usernames
    password_hashes = []    # List for storing hashed passwords

    print("Enter user accounts. Leave username blank to finish.\n")

    # Start an input loop for multiple user accounts
    while True:
        username = input("Username: ").strip()

        # If the username input is empty, stop collecting users
        if username == "":
            print("\nInput finished.\n")
            break

        # Ask for password input
        password = input("Password: ")

        # Call the hash_password() function to hash the password securely
        hashed_pw = hash_password(password)

        # Store both the username and the hashed password
        usernames.append(username)
        password_hashes.append(hashed_pw)

        # Confirm data saved (only showing that password was hashed, not revealing original password)
        print(f"Saved user '{username}' with hashed password.")
        print("-" * 60)

    # Return the two lists for further use
    return usernames, password_hashes


# Running the program

if __name__ == "__main__":
    # Call the function to collect user data
    users, hashes = collect_users_and_hashes()

    # Display the stored usernames and their hashes
    print("\n--- Stored Accounts ---")
    for u, h in zip(users, hashes):
        print(f"Username: {u} | Hash: {h}")
