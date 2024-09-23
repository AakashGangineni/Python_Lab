def even_number_pyramid(n):
    even_number = 10  # Start from 10
    for i in range(1, n + 1):
        # Create the pattern for the current row
        row = [even_number - 2 * j for j in range(i)]
        # Print the row
        print(" ".join(map(str, row)))

# Set the number of rows
num_rows = 5
even_number_pyramid(num_rows)
