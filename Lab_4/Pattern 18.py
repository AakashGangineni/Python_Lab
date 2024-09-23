def pyramid_pattern(n):
    for i in range(1, n + 1):
        # Create the current row with asterisks
        stars = '* ' * i
        # Print the row
        print(stars.strip())

# Set the number of rows
num_rows = 5
pyramid_pattern(num_rows)
