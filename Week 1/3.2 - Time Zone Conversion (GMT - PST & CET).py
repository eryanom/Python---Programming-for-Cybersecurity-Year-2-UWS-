#3.2 - Time Zone Conversion (GMT - PST & CET)
#Request GMT Time
hours = int(input("Enter the time in GMT hours (0-23):"))
minutes = int(input("Enter the minutes (0-59):"))

#Convert to PST and CET
pst_hours = (hours - 8) % 24
cet_hours = (hours + 1) % 24

print(f"GMT Time: {hours:02d}:{minutes:02d}")
print(f"PST Time: {pst_hours:02d}:{minutes:02d}")
print(f"CET Time: {cet_hours:02d}:{minutes:02d}")