# Erya Anom
# Lab - Fibonacci Sequence
# Program to display the first 20 numbers in the Fibonacci sequence.
# Initialise the first two Fibonacci numbers

a, b = 0, 1   # 'a' starts at 0 (first term), 'b' starts at 1 (second term)

# Display title
print("First 20 terms of Fibonacci sequence:")

# Generate and print the first 20 Fibonacci numbers
for _ in range(20):       # Loop runs 20 times
    print(a, end=" ")     # Print the current Fibonacci number on the same line
    a, b = b, a + b       # Update values: new 'a' becomes old 'b', new 'b' = old a + old b
