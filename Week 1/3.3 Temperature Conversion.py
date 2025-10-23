#3.3 - Temperature Conversion
#Celsius to Fahrenheit

celsius = float(input("Enter temperature in °C:"))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} °C = {fahrenheit:.2f} °F")

#Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in °F:"))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} °F = {celsius:.2f} °C")