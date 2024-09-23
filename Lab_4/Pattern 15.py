def mirrored_pyramid(n):
    for i in range(1, n + 1):
        # Create spaces for alignment
        spaces = ' ' * (n - i) * 2
        # Create the current row with numbers
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        # Print the row with spaces
        print(spaces + numbers)

# Set the number of rows
num_rows = 5
mirrored_pyramid(num_rows)
