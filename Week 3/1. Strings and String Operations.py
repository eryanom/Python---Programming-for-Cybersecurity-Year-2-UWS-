# Erya Anom

# 1. Declare string variable
welcome = "Welcome to Programming for Cyber Security"

# 2. Split into words
words = ['Welcome', 'to', 'Programming', 'for', 'Cyber', 'Security']
print('List of words:',words)
for w in words:
    print(w)

print(len(words))

print(words[2])

for r in range(len(words)):
    print(words[r])
words.append('Python')
print(words)

# 3a. Words containing 'm'
m_words = [w for w in words if 'm' in w]
print("Words containing 'm':", m_words)

# 3b. Words that do NOT contain 'a'
no_a_words = [w for w in words if 'a' not in w]
print("Words without 'a':", no_a_words)

# 3c. Words longer than 7 characters
long_words = [w for w in words if len(w) > 7]
print("Words longer than 7 chars:", long_words)

# 4. Slice welcome into two equal parts
half = len(welcome) // 2
part1 = welcome[:half]
part2 = welcome[half:]
print("First half:", part1)
print("Second half:", part2)
