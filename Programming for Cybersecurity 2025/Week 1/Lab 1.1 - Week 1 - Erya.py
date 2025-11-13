#Erya Anom
#B01834949

# hello_world.py
print("Hello World!")
name = input("What is your name?")
print(f"Welcome to Programming for Cyber Security {name}")

# Arithmetic with two values
# Request two numbers and prints various of operations
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a value.")
a = read_number("Enter the first value: ")
b = read_number("Enter the second value: ")

print(f"Sum: {a + b}")
print(f"Product: {a * b}")
print(f"First minus second: {a - b}")

if b == 0:
    print("Division: undefined (division by zero)")
    print("Integer division: undefined (division by zero)")
    print("Modulo: undefined (division by zero)")
else:
    print(f"Division: {a / b}")
    #integer division makes the most sense with ints; but it show floor division result
    print(f"Integer division (//): {a // b}")
    print(f"Modulus (%): {a % b}")
