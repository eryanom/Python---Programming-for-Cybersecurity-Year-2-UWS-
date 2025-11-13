# Erya Puput Anom
# B01834949
# Lab - Fibonacci Sequence
# Program to display the first 20 Fibonacci numbers on request,
# then continue showing more one-by-one until the user stops.

# The first 20 terms of the Fibonacci sequence are:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

# Initialise the first two Fibonacci numbers
# WHY: The Fibonacci sequence always starts with 0 and 1.
a, b = 0, 1   # 'a' = first term (0), 'b' = second term (1)

# Display title
print("Fibonacci Sequence Viewer\n")


# Ask the user whether they want to see the first 20 terms automatically
# WHY: This gives the user control over whether to display all 20 terms at once or not.
choice = input("Do you want to display the first 20 terms of the Fibonacci sequence? (yes/no): ").lower()


# Step 1: Show the first 20 Fibonacci numbers automatically if the user says yes
if choice in ("yes", "y"):
    print("\nFirst 20 terms of the Fibonacci sequence:")
    for i in range(1, 21):  # Loop runs 20 times (for 20 terms)
        print(f"Term {i}: {a}")  # Display the current Fibonacci number
        a, b = b, a + b          # Update the two values to get the next Fibonacci number
    print("\n--- End of first 20 terms ---\n")
else:
    print("\nSkipping the first 20 terms.\n")


# Step 2: Continue showing next terms interactively
# WHY: This section lets the user continue viewing the next terms one at a time.
print("Press ENTER to see the next term, or type 'stop' to quit.\n")


# If the user viewed the first 20 terms, continue from term 21;
# otherwise, start counting from 1 if they skipped it.
count = 21 if choice in ("yes", "y") else 1


# Use a while loop so the user can keep generating terms until they choose to stop
while True:
    # Wait for user input before showing the next number
    user_input = input("Press ENTER to continue or type 'stop' to quit: ")

    # Allow the user to stop by typing 'stop', 'exit', or 'quit'
    if user_input.lower() in ("stop", "exit", "quit"):
        print("\nProgram stopped. Goodbye! 🌀")
        break  # Exit the loop

    # Display the next Fibonacci term
    print(f"Term {count}: {a}")

    # Update the Fibonacci numbers for the next term
    # WHY: Each new term is found by adding the two previous terms.
    a, b = b, a + b
    count += 1  # Move to the next term
