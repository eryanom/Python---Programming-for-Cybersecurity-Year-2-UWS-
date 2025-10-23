#3.4 - Eggs (Gross, Dozen, Singles)
eggs = int(input("Enter the number of eggs:"))

gross = eggs // 144
dozen = (eggs % 144) // 12
single = eggs % 12
print(f"{eggs} eggs is {gross} gross eggs + {dozen} dozen eggs + {single} eggs")