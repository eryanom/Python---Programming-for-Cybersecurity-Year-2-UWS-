# Erya Anom
# Lab - Input integers 1-10 until sum > 50
# This program keeps asking the user for numbers between 1 and 10,
# adds them up, and stops when the total sum is greater than 50.
# Initialise empty list and total sum variable
# ------------------------------------------------------------
values = []       # To store all valid integers entered by the user
total = 0         # To keep track of the running total sum

# Keep looping until the total becomes greater than 50
while total <= 50:
    try:
        # Ask user for input and convert it to an integer
        num = int(input("Enter an integer between 1 and 10:"))

        # Check if the input is within the allowed range (1–10)
        if 1 <= num <= 10:
            values.append(num)   # Add valid number to the list
            total += num         # Add the number to the total sum
        else:
            print("Error: Number must be between 1 and 10")  # Warn if out of range

    # Handle case when user enters non-integer (e.g., text)
    except ValueError:
        print("Error: Please enter a valid integer")

# Output the results after total > 50
print("\nResults:")  # Print a blank line and heading
print("Sum of values entered:", total)                     # Total sum of all numbers
print("Largest value entered:", max(values))               # Maximum number entered
print("Smallest value entered:", min(values))              # Minimum number entered
print("Average value entered:", sum(values) / len(values)) # Calculate and print average
