# Given list of integers
integer_list = [1, 2, 3, 4, 5]

# Given tuple of integers
integer_tuple = (6, 7, 8, 9, 10)

# Convert the list of integers to a list of strings
string_list = list(map(str, integer_list))

# Convert the tuple of integers to a list of strings
string_tuple = list(map(str, integer_tuple))

# Combine both lists
combined_string_list = string_list + string_tuple

# Print the results
print("List of strings from the list:", string_list)
print("List of strings from the tuple:", string_tuple)
print("Combined list of strings:", combined_string_list)
