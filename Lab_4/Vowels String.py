# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"  # Include both lowercase and uppercase vowels
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Take input from the user
user_input = input("Enter a string: ")

# Count the number of vowels
vowel_count = count_vowels(user_input)

# Print the result
print("Number of vowels in the string:", vowel_count)
