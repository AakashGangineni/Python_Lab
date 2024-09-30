# Given three lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Use map with a lambda function to add the lists element-wise
result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

# Print the result
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("Summed List:", result)
