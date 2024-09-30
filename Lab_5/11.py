# Given array of integers
array = [1, 2, 3, 4, 5]

# Use map to convert each element to an integer (if needed)
# Here it's already a list of integers, but this shows how it can be done
integer_array = list(map(int, array))

# Compute the sum of the elements
total_sum = sum(integer_array)

# Print the result
print("Array of integers:", integer_array)
print("Sum of elements:", total_sum)
