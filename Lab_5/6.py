# Given sequence of characters
sequence = "Hello World!"

# Convert characters to uppercase and lowercase using map
uppercase_chars = list(map(lambda x: x.upper(), sequence))
lowercase_chars = list(map(lambda x: x.lower(), sequence))

# Eliminate duplicate letters by converting to a set and back to a list
unique_uppercase = list(dict.fromkeys(uppercase_chars))  # Preserve order for uppercase
unique_lowercase = list(dict.fromkeys(lowercase_chars))  # Preserve order for lowercase

# Print the results
print("Original sequence:", sequence)
print("Uppercase characters (unique):", ''.join(unique_uppercase))
print("Lowercase characters (unique):", ''.join(unique_lowercase))
