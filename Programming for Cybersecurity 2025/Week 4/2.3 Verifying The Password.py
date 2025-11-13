from hashlib import sha256
# Import the SHA-256 hash function from Python’s hashlib library.
# WHY: Hashing is used to securely store passwords without saving them in plain text.

# Part 2.2: Create users and store password hashes

usernames = []         # List to store usernames
password_hashes = []   # List to store SHA-256 hashed passwords

print("=== Create User Accounts ===")

# Loop for creating multiple user accounts
while True:
    username = input("Enter username (blank to stop): ").strip()
    if username == "":       # If user presses Enter with no input, stop the loop
        break

    password = input("Enter password: ").strip()

    # Convert password to bytes and hash using SHA-256
    hashed_password = sha256(password.encode('utf-8')).hexdigest()

    # Store the username and its hashed password
    usernames.append(username)
    password_hashes.append(hashed_password)

    # Display confirmation (show only the first 15 chars of the hash for privacy)
    print(f"Saved user '{username}' with hashed password {hashed_password[:15]}...")
    print("-" * 50)

# Display stored users (for demonstration purposes)
print("\nStored usernames and password hashes:")
for u, h in zip(usernames, password_hashes):
    print(f"{u}: {h}")

# Part 2.3: Verify login (check if password matches)
print("\n=== Login Verification ===")
user = input("Enter username to verify: ").strip()

if user in usernames:
    index = usernames.index(user)   # Find the user's position in the list
    entered_password = input("Enter password: ").strip()

    # Hash the entered password to compare with stored hash
    entered_hash = sha256(entered_password.encode('utf-8')).hexdigest()

    print(f"\nEntered password hash: {entered_hash}")
    print(f"Stored password hash:  {password_hashes[index]}")

    # Compare hashed passwords instead of plain text
    if entered_hash == password_hashes[index]:
        print("Password is correct! Access granted.")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Username not found.")
