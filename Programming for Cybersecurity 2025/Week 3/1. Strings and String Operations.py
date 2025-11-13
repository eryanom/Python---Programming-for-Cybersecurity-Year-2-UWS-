# Erya Anom
# Lab - String and List Operations
# This program performs several string and list operations such as splitting,
# filtering, appending, and slicing text data.

# 1. Declare string variable
welcome = "Welcome to Programming for Cyber Security"
# Store a sentence (string) in a variable named 'welcome'

# 2. Split into words
words = ['Welcome', 'to', 'Programming', 'for', 'Cyber', 'Security']
# Manually create a list containing each word from the sentence

print('List of words:', words)  # Display the list of words

# Print each word one by one
for w in words:
    print(w)

print(len(words))  # Display the total number of words in the list

print(words[2])    # Display the third word (index starts from 0)

# Print words again using index-based loop
for r in range(len(words)):
    print(words[r])

# Add another word to the list
words.append('Python')
print(words)  # Display the updated list

# 3a. Words containing 'm'
m_words = [w for w in words if 'm' in w]
# Create a new list containing words that have the letter 'm'
print("Words containing 'm':", m_words)

# 3b. Words that do NOT contain 'a'
no_a_words = [w for w in words if 'a' not in w]
# Create a new list containing words that do not have the letter 'a'
print("Words without 'a':", no_a_words)

# 3c. Words longer than 7 characters
long_words = [w for w in words if len(w) > 7]
# Create a new list containing words with more than 7 characters
print("Words longer than 7 chars:", long_words)

# 4. Slice 'welcome' string into two equal parts
half = len(welcome) // 2       # Find the middle index (divide length by 2)
part1 = welcome[:half]         # Take the first half of the string
part2 = welcome[half:]         # Take the second half of the string
print("First half:", part1)
print("Second half:", part2)
