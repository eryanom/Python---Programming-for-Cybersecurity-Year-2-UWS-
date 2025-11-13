# Erya Anom
# Lab - Prime Number Checker
# This program checks if a number entered by the user is a prime number.


# Function Definition

def isPrime(num):
    """Return True if the number is prime, otherwise False."""

    # Numbers less than 2 (0 and 1) are not prime
    if num < 2:
        return False

    # Optimized check: only loop up to the square root of num
    # WHY: If a number has a divisor larger than its square root,
    # then it must also have a smaller corresponding divisor.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If divisible, it's not prime
            return False
    return True  # If no divisors found, it's prime



# Main program: interactive user input

while True:
    # Ask the user for input
    user_input = input("Enter a number to check if it's prime (or type 'stop' to quit): ").strip().lower()

    # Allow user to exit the loop
    if user_input == "stop":
        print("Goodbye! ")
        break

    # Validate input: make sure it's a positive integer
    if not user_input.isdigit():
        print("Please enter a valid positive number or 'stop'.")
        continue

    # Convert input to integer
    num = int(user_input)

    # Call the isPrime() function
    result = isPrime(num)

    # Display result
    print(f"{num} is prime: {result}")
