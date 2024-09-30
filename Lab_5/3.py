# Given list of strings
strings = ["hello", "world", "python", "map"]

# Use map to listify each string
listified_strings = list(map(lambda s: list(s), strings))

# Print the result
print("Original strings:", strings)
print("Listified strings:", listified_strings)
