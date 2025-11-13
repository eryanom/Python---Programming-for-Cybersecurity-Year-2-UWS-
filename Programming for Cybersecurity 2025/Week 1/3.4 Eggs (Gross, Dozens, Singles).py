# Erya Anom
# 3.4 - Eggs (Gross, Dozen, Singles)
# Program to convert a total number of eggs into gross, dozen, and single eggs.
# Question:
# There are 144 eggs in one gross and 12 eggs in one dozen.
# Write a program that accepts a whole number of eggs and outputs
# the value in terms of gross eggs, dozen eggs, and single eggs (integer division).

while True:
    # Ask the user for input
    user_input = input("Enter the number of eggs (or type 'stop' to quit): ")

    # Allow user to stop the program
    if user_input.lower() in ("stop", "exit", "quit"):
        print("Program stopped. Goodbye! 🐣")
        break  # Exit the loop

    # Validate the input (check if it's a number)
    if not user_input.isdigit():
        print("Please enter a valid whole number of eggs.")
        continue  # Ask again

    eggs = int(user_input)  # Convert input to integer

    # Perform the calculations
    gross = eggs // 144          # 1 gross = 144 eggs
    dozen = (eggs % 144) // 12   # Dozens left after removing gross
    single = eggs % 12           # Remaining single eggs

    # Display the output
    print(f"{eggs} eggs = {gross} gross + {dozen} dozen + {single} single eggs\n")


# End of program


# Comment
# - '//' is integer division (keeps only the whole number)
# - '%' is modulus (gives remainder after division)
# - The code breaks down the total eggs into:
#     Gross (groups of 144)
#     Dozen (groups of 12)
#     Single (remaining eggs)
# Example: 200 eggs → 1 gross + 4 dozen + 8 eggs