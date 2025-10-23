import random

term1 = ['Advisory', 'Asset', 'Baselining', 'Block List', 'Clearance',
         'Collision', 'Competency', 'Event', 'Failover', 'Impact']

term2 = ['Manual Key Transport', 'Message Digest', 'Outside Threat',
         'Passive Attack', 'Perimeter', 'Privilege', 'Protocol', 'Resilience',
         'Sanitization', 'Tunneling']

term3 = ['Validation', 'Whitelist', 'Zeroisation', 'Threat', 'Standard',
         'Speacialism', 'Rootkit', 'Risk', 'Regulation', 'Proxy']

# 1. Generate a random phrase
word1 = random.choice(term1)
word2 = random.choice(term2)
word3 = random.choice(term3)
phrase = f"{word1} {word2} {word3}"
print("Random Phrase:", phrase)

# 2. How many unique phrases?
#   (Simply multiply the possibilities)
unique_phrases = len(term1) * len(term2) * len(term3)
print("Number of unique phrases:", unique_phrases)

# 3. Initialise list x (1 to 10)
x = list(range(1, 11))
print("x:", x)

# 4. Generate y using for loop (y = 2x + 3)
y = []
for num in x:
    y.append(2 * num + 3)
print("y (for loop):", y)

# 5. Generate y using list comprehension
y_comp = [2 * num + 3 for num in x]
print("y (list comprehension):", y_comp)
