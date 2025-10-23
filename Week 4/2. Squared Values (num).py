#Erya Anom

#Part 2 - Squared Values (num)
def squared_values(num):
    squares = [x ** 2 for x in num]
    return squares

# Example usage:
numbers = [x + 1 for x in range(10)]  # [1,2,...,10]
numbers_squared = squared_values(numbers)

for n, b in zip(numbers, numbers_squared):
    print(f'{n} ^ 2 = {b}')