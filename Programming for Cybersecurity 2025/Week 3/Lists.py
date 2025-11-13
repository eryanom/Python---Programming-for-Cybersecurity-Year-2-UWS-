# Erya Anom
# Lab - Random Phrase Generator & List Operations
# This program randomly combines Cyber Security terms to form a phrase,
# calculates the number of possible unique combinations,
# and demonstrates list generation using loops and list comprehension.

import random   # Import the random module for random selection

# 1. Given lists of Cyber Security terms
term1 = ['Advisory', 'Asset', 'Baselining', 'Block List', 'Clearance',
          'Collision', 'Competency', 'Event', 'Failover', 'Impact']

term2 = ['Manual Key Transport', 'Message Digest', 'Outside Threat',
          'Passive Attack', 'Perimeter', 'Privilege', 'Protocol', 'Resilience',
          'Sanitization', 'Tunneling']

term3 = ['Validation', 'Whitelist', 'Zeroisation', 'Threat', 'Standard',
          'Specialism', 'Rootkit', 'Risk', 'Regulation', 'Proxy']  # fixed typo "Speacialism" → "Specialism"

# 1. Randomly select one term from each list to form a phrase
# random.randint(0, len(list) - 1) picks a random index number within the list length
rand1 = term1[random.randint(0, len(term1) - 1)]
rand2 = term2[random.randint(0, len(term2) - 1)]
rand3 = term3[random.randint(0, len(term3) - 1)]

# Combine the three random words into a single phrase
phrase = f"{rand1} {rand2} {rand3}"
print("Random phrase:", phrase)

# 2. Calculate how many unique phrases can be generated
# Each phrase is made of one word from each list, so:
# total combinations = len(term1) × len(term2) × len(term3)
unique_phrases = len(term1) * len(term2) * len(term3)
print("Total unique possible phrases:", unique_phrases)
print()  # Print a blank line for readability

# 3. Initialise list x = [1, 2, ..., 10]
x = list(range(1, 11))  # Create a list of numbers from 1 to 10
print("x:", x)

# 4. Using a for loop, generate y = 2x + 3
y_loop = []             # Create an empty list to store results
for num in x:
    y_loop.append(2 * num + 3)   # Apply formula 2x + 3 to each number
print("y (using loop):", y_loop)

# 5. Using list comprehension
# Same result as above, but written in one line
y_comp = [2 * num + 3 for num in x]
print("y (list comprehension):", y_comp)
