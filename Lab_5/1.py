# Define a function to triple a number
def triple(x):
    return x * 3

# Given list of integers
numbers = [1, 2, 3, 4, 5]

# Use map to apply the triple function to each number in the list
tripled_numbers = list(map(triple, numbers))

# Print the result
print("Original numbers:", numbers)
print("Tripled numbers:", tripled_numbers)
