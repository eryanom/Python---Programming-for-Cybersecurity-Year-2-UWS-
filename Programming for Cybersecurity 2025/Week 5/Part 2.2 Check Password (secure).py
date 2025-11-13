"""
pwned_check.py

Reads username,password pairs from 'passwords.txt' (one pair per line, comma separated).
For each password:
 - evaluate a simple strength score (weak/medium/strong)
 - compute SHA1, send first 5 chars to HIBP Pwned Passwords API
 - search returned suffixes for a match and report breach count

Requires: requests
Install: pip install requests
"""

import hashlib
import requests
import time
import sys
import re

INPUT_FILE = "passwords.txt"
API_RANGE_URL = "https://api.pwnedpasswords.com/range/{}"
# polite User-Agent per HIBP API guidance
HEADERS = {"User-Agent": "pwned-check-script/1.0 (contact: none)"}

def sha1_upper(text: str) -> str:
    return hashlib.sha1(text.encode('utf-8')).hexdigest().upper()

def check_pwned_count(password: str, pause_between_requests: float = 1.6) -> int:
    """
    Returns the number of times the password has appeared in breaches (0 if not found).
    Uses k-anonymity: send first 5 chars of SHA1, compare suffixes locally.
    """
    h = sha1_upper(password)
    prefix, suffix = h[:5], h[5:]
    url = API_RANGE_URL.format(prefix)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
    except requests.RequestException as e:
        # network / timeout error: raise up so caller can decide
        raise RuntimeError(f"Error querying HIBP API: {e}") from e

    if resp.status_code != 200:
        raise RuntimeError(f"HIBP API returned status code {resp.status_code}")

    # Response is lines like: "0034A1B2C3D4E5F6...:1234"
    for line in resp.text.splitlines():
        if ':' not in line:
            continue
        suf, count = line.split(':', 1)
        if suf.strip().upper() == suffix:
            try:
                return int(count.strip())
            except ValueError:
                return 0
    # polite pause to avoid hammering (API supports high volumes but be respectful)
    time.sleep(pause_between_requests)
    return 0

def password_strength(password: str) -> str:
    """
    Simple heuristic:
     - Weak: <8 chars OR only letters or only digits OR common short patterns
     - Medium: 8-11 chars with at least two classes
     - Strong: >=12 chars and at least 3 classes (lower, upper, digit, special)
    This is a heuristic, not a full entropy calc.
    """
    length = len(password)
    classes = 0
    if re.search(r'[a-z]', password): classes += 1
    if re.search(r'[A-Z]', password): classes += 1
    if re.search(r'\d', password): classes += 1
    if re.search(r'[^A-Za-z0-9]', password): classes += 1

    # quick reject common weak patterns
    common_weak = {"password", "123456", "qwerty", "letmein", "admin"}
    if password.lower() in common_weak or length < 6:
        return "Weak"

    if length >= 12 and classes >= 3:
        return "Strong"
    if length >= 8 and classes >= 2:
        return "Medium"
    return "Weak"

def process_file(filename: str):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [ln.strip() for ln in f.readlines() if ln.strip()]
    except FileNotFoundError:
        print(f"Input file '{filename}' not found.", file=sys.stderr)
        return

    print(f"{'Username':<20} {'Strength':<8} {'PwnedCount':<10} Notes")
    print("-" * 70)

    for idx, line in enumerate(lines, start=1):
        # split on first comma only, allow commas in password if quoted isn't handled
        if ',' not in line:
            print(f"Line {idx}: malformed (no comma) — {line}", file=sys.stderr)
            continue
        user, pwd = line.split(',', 1)
        user = user.strip()
        pwd = pwd.strip()

        # local strength
        strength = password_strength(pwd)

        # check pwned status
        try:
            count = check_pwned_count(pwd)
        except RuntimeError as e:
            print(f"{user:<20} {strength:<8} {'?':<10} Error querying API: {e}")
            continue

        notes = ""
        if count > 0:
            notes = "PWNED - change immediately!"
        else:
            notes = "Not found in dataset (still may be weak)"

        print(f"{user:<20} {strength:<8} {str(count):<10} {notes}")


if __name__ == "__main__":
    process_file(INPUT_FILE)
