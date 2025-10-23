from hashlib import sha256

def hash_password(password: str) -> str:
    """Return a hex SHA-256 hash of the given password."""
    return sha256(password.encode('utf-8')).hexdigest()

def collect_users_and_hashes():
    """
    Use a while loop to enter username/password pairs.
    - Blank username finishes input.
    - Stores usernames and password hashes in separate lists.
    """
    usernames = []
    password_hashes = []
    print("Enter user accounts. Leave username blank to finish.")

    while True:
        username = input("Username: ").strip()
        if username == "":
            break
        password = input("Password: ")  # langsung menggunakan input() tanpa getpass
        usernames.append(username)
        password_hashes.append(hash_password(password))
        print(f"Saved user '{username}' with hashed password.")

    return usernames, password_hashes

# --- Example usage ---
if __name__ == "__main__":
    users, hashes = collect_users_and_hashes()
    print("\n--- Stored Accounts ---")
    for u, h in zip(users, hashes):
        print(f"Username: {u} | Hash: {h}")