# Ask the user for a string input
input_string = input("Enter a string: ")

# Convert the input string to lowercase
input_string = input_string.lower()

# Create an empty dictionary to store letter counts
letter_counts = {}

# Iterate over characters in the string
for char in input_string:
    # Check if the character is a letter
    if char.isalpha():
        # If the character is already in the dictionary, increment its count
        if char in letter_counts:
            letter_counts[char] += 1
        # If it's not in the dictionary, add it with a count of 1
        else:
            letter_counts[char] = 1

# Print the resultant dictionary
for letter, count in letter_counts.items():
    print(f"{letter} occurs {count} times")
