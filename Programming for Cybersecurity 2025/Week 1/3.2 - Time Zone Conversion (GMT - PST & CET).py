# Erya Anom
# 3.2 - Time Zone Conversion (GMT - PST & CET)
# Program to convert time from GMT (Greenwich Mean Time)
# to PST (Pacific Standard Time) and CET (Central European Time)

hours = int(input("Enter the time in GMT hours (0-23):"))   # Ask for hour value in 24-hour format
minutes = int(input("Enter the minutes (0-59):"))           # Ask for minute value

#Convert to PST and CET
pst_hours = (hours - 8) % 24    # Use modulo 24 to wrap around midnight (e.g., 2 - 8 = -6 → becomes 18)
cet_hours = (hours + 1) % 24    # Also use modulo 24 to keep result within 0–23 range

#Display all results in HH:MM format with leading zeros
print(f"GMT Time: {hours:02d}:{minutes:02d}")      # Print original GMT time
print(f"PST Time: {pst_hours:02d}:{minutes:02d}")  # Print PST time
print(f"CET Time: {cet_hours:02d}:{minutes:02d}")  # Print CET time

#comment:
# - %02d means "print with 2 digits, add a leading zero if needed"
# - Modulo 24 (%) ensures time stays within 0–23 hours
# - This code only shifts the hour part, minutes remain the same