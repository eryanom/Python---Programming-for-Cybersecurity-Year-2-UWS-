#First 20 Fibonacci numbers
a, b = 0, 1
print("First 20 terms of Fibonacci sequence:")
for _ in range(20):
    print(a, end=" ")
    a, b = b, a+b