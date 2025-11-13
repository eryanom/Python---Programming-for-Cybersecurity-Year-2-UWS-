# Erya Anom
# 3.2 - Time Zone Conversion (GMT - PST & CET)
# Convert a time given in GMT to Pacific Standard Time (PST) and Central European Time (CET)

# Ask the user for the GMT time
hours = int(input("Enter the time in GMT hours (0–23):"))  # Get the hour (24-hour format)
minutes = int(input("Enter the minutes (0–59):"))          # Get the minutes

# Compute PST and CET hours
# PST is 8 hours behind GMT
pst_hours = (hours - 8) % 24   # Use %24 so the hour wraps correctly if it goes below 0
# CET is 1 hour ahead of GMT
cet_hours = (hours + 1) % 24   # Use %24 so the hour wraps correctly if it goes above 23

# Display all three times in HH:MM format
print(f"GMT Time: {hours:02d}:{minutes:02d}")   # Original GMT time
print(f"PST Time: {pst_hours:02d}:{minutes:02d}")  # Converted PST time
print(f"CET Time: {cet_hours:02d}:{minutes:02d}")  # Converted CET time

# Comment:
# %02d → print as two digits, adding a leading zero if needed (e.g. 03 instead of 3)
# The modulo operator (%) keeps the hour within the 0–23 range
# Only the hour changes; the minutes stay the same
