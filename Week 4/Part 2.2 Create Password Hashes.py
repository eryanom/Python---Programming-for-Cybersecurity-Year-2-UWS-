from hashlib import sha256

def hash_password(password: str) -> str:
    """Return a hex SHA-256 hash of the given password."""
    hashed = sha256(password.encode('utf-8')).hexdigest()
    print(f"Hashing password: '{password}' -> {hashed}")
    return hashed


def collect_users_and_hashes():
    """
    Use a while loop to enter username/password pairs.
    - Blank username finishes input.
    - Stores usernames and password hashes in separate lists.
    """
    usernames = []
    password_hashes = []
    print("Enter user accounts. Leave username blank to finish.\n")

    while True:
        username = input("Username: ").strip()
        if username == "":
            print("\nInput finished.\n")
            break

        password = input("Password: ")
        hashed_pw = hash_password(password)  # call function and show hash

        usernames.append(username)
        password_hashes.append(hashed_pw)

        print(f"Saved user '{username}' with hashed password.")
        print("-" * 60)

    return usernames, password_hashes


# usage
if __name__ == "__main__":
    users, hashes = collect_users_and_hashes()
    print("\n--- Stored Accounts ---")
    for u, h in zip(users, hashes):
        print(f"Username: {u} | Hash: {h}")
