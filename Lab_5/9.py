# Given tuple
data_tuple = (10, 20, 30, 40, 50)

# Specify the indices of the elements you want to take from the tuple
indices_to_take = [1, 3, 4]  # Taking elements at index 1, 3, and 4

# Create a new list taking specific elements from the tuple
new_list = [data_tuple[i] for i in indices_to_take]

# Convert a string value to an integer
string_value = "123"
converted_integer = int(string_value)

# Print the results
print("New list from tuple:", new_list)
print("Converted integer from string:", converted_integer)
