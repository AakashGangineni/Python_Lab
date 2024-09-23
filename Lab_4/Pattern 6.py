def reverse_pyramid(n):
    print("Pattern #6: Reverse Pyramid of Numbers")
    for i in range(1, n + 1):
        # Print leading spaces
        print(' ' * (n - i), end='')
        # Print numbers from i down to 1
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()  # Move to the next line

# Set the number of rows
rows = 5

# Call the function to print the pattern
reverse_pyramid(rows)
