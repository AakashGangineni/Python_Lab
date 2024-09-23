def downward_triangle(n):
    for i in range(n, 0, -1):
        # Create spaces for alignment
        spaces = ' ' * (n - i)
        # Create the current row with asterisks
        stars = '* ' * i
        # Print the row with spaces
        print(spaces + stars.strip())

# Set the number of rows
num_rows = 6
downward_triangle(num_rows)
