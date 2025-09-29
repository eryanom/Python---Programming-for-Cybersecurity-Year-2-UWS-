#Input integers 1-10 until sum > 50
values =[]
total = 0

while total <= 50:
    try:
        num = int(input("Enter an integer between 1 and 10:"))
        if 1 <= num <=10:
            values.append(num)
            total += num
        else:
            print("Error: Number must be between 1 and 10")
    except ValueError:
            print("Error: Please enter a valid integer")

#Output results
print("\nresults:")
print("Sum of values entered:", total)
print("Largest value entered:", max(values))
print("Smallest value entered:", min(values))
print("Average value entered:", sum(values) / len(values))