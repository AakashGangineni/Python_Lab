# Given two lists of integers
list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]

# Use map to add the lists element-wise
added_lists = list(map(lambda x, y: x + y, list1, list2))

# Use map to find the difference between the lists element-wise
difference_lists = list(map(lambda x, y: x - y, list1, list2))

# Print the results
print("List 1:", list1)
print("List 2:", list2)
print("Added Lists:", added_lists)
print("Difference Lists:", difference_lists)
