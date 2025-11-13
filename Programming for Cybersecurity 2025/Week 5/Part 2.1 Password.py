# Erya Puput Anom
# B01834949
# The main purpose:
# - Read a list of passwords from a file (one password per line)
# - Check each password against rules for a strong password
# - Report which passwords are strong and which are weak

import re  # regular expressions for pattern matching

def is_valid_password(password):
    """Return True if the password meets all strength requirements."""
    # 1) length
    if len(password) < 8:
        return False
    # 2) at least one uppercase
    if not re.search(r"[A-Z]", password):
        return False
    # 3) at least one lowercase
    if not re.search(r"[a-z]", password):
        return False
    # 4) at least one digit
    if not re.search(r"\d", password):
        return False
    # 5) at least one special character (anything not a letter/number/underscore/space)
    # This is slightly broader and avoids escaping quotes inside the class.
    if not re.search(r"[^\w\s]", password):
        return False

    return True

def check_passwords_from_file(filename):
    """Read passwords from a file and check each one."""
    try:
        # Read lines, strip whitespace, skip empties
        with open(filename, "r", encoding="utf-8") as file:
            passwords = [line.strip() for line in file if line.strip()]

        for password in passwords:
            if is_valid_password(password):
                print(f" '{password}' is a strong password.")
            else:
                print(f" '{password}' does NOT meet the requirements.")
    except FileNotFoundError:
        print("Error: File not found. Please check the file name or path.")

if __name__ == "__main__":
    filename = input("Enter the filename containing passwords: ")
    check_passwords_from_file(filename)  # <- keep this line clean; nothing after it
