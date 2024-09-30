# Define the base number
base_number = 2

# Define the range for the powers (0 to n)
n = 10
indices = range(n)

# Use map to compute base_number raised to the power of each index
powers = list(map(lambda x: base_number ** x, indices))

# Print the result
print(f"Powers of {base_number}:")
print(powers)
