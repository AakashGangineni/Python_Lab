def equilateral_triangle(n):
    for i in range(1, n + 1):
        # Create spaces for alignment
        spaces = ' ' * (n - i)
        # Create the current row with asterisks
        stars = '* ' * i
        # Print the row with spaces
        print(spaces + stars.strip())

# Set the number of rows
num_rows = 7
equilateral_triangle(num_rows)
