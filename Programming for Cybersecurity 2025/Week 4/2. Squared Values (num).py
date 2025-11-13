# Erya Puput Anom
# Part 2 - Squared Values (num)
# This program defines a function to calculate the square of each number in a list.

# Function definition
def squared_values(num):
    # Use list comprehension to create a new list of squared numbers
    # For every element x in the input list 'num', compute x ** 2 (x squared)
    squares = [x ** 2 for x in num]
    return squares  # Return the list of squared values

# Running the program
# Create a list of numbers from 1 to 10 using list comprehension
numbers = [x + 1 for x in range(10)]  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function and store the results in 'numbers_squared'
numbers_squared = squared_values(numbers)

# Display both the original numbers and their squared values
for n, b in zip(numbers, numbers_squared):
    # zip() pairs each element in 'numbers' with the corresponding element in 'numbers_squared'
    print(f'{n} ^ 2 = {b}')
