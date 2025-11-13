# Erya Anom
# Lab - Generate Prime Numbers
# This program defines two functions:
# 1. is_prime(n): checks if a number is prime
# 2. generate_primes(count): generates the first 'count' prime numbers

# Function: Check if a number is prime
def is_prime(n: int) -> bool:
    """Return True if n is prime, else False."""

    # Numbers less than 2 are not prime (0 and 1)
    if n < 2:
        return False

    # Only check divisors up to the square root of n for efficiency
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if n % i == 0:  # If divisible by i, it's not prime
            return False
    return True  # If no divisors found, number is prime



# Function: Generate a list of prime numbers

def generate_primes(count: int) -> list[int]:
    """Return a list with the first `count` prime numbers."""

    # Validate input: count cannot be negative
    if count < 0:
        raise ValueError("count must be non-negative")

    primes = []  # Empty list to store prime numbers
    num = 2  # Start checking from 2 (the first prime number)

    # Keep looping until we have 'count' primes
    while len(primes) < count:
        if is_prime(num):  # Check if current number is prime
            primes.append(num)  # If yes, add it to the list
        num += 1  # Move to the next number

    return primes



# Main Program: User Interaction

while True:
    # Ask user for number of primes they want
    user_input = input("\nEnter how many primes you want (or type 'stop' to end): ").strip().lower()

    # Exit option
    if user_input == "stop":
        print("Program stopped. Goodbye!")
        break

    # Validate input (must be numeric)
    if not user_input.isdigit():
        print("Please enter a valid number or 'stop'.")
        continue

    # Convert input to integer
    count = int(user_input)

    # Generate prime numbers
    primes = generate_primes(count)

    # Display the result
    print(f"The first {count} prime numbers are: {primes}")
