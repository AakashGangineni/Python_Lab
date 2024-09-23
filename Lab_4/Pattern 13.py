def pyramid_of_horizontal_tables(n):
    for i in range(n + 1):
        # Create the current row by multiplying the index with the column number
        row = [i * j for j in range(i + 1)]
        # Print the row
        print(" ".join(map(str, row)))

# Set the number of rows
num_rows = 6
pyramid_of_horizontal_tables(num_rows)
