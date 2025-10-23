#Erya Anom

#Part 1 - Greeting with Name
def greeting(name):
    return f"Hello {name}"

# Example usage:
print(greeting("Erya"))



#Part 3 - Raised_to (num, exponent)
def rasied_to(num, exponent):
    power = [x ** exponent for x in num]
    return power

#Example usage:
numbers = [x + 1 for x in range(10)]
numbers_cubed = rasied_to(numbers, 3)

for n, b in zip(numbers, numbers_cubed):
    print(f'{n} ^ 2 = {b}')