# Erya
# Lab 2 - Math Operations
# This program prints all numbers between 0 and 100 that are divisible by 6.

# Loop from 0 to 100 (inclusive)
for num in range(0, 101):     # range(0, 101) generates numbers from 0 up to 100
    # Check if the number is divisible by 6
    if num % 6 == 0:          # '%' (modulus) gives the remainder of a division
        print(num)            # If the remainder is 0, the number is a multiple of 6
