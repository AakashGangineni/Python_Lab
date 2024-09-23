def pyramid_pattern_alternate_numbers(n):
    for i in range(n):
        # Calculate the number to print (odd numbers)
        number = 2 * i + 1
        # Create the current row
        row = [number] * (i + 1)
        # Print the row
        print(" ".join(map(str, row)))

# Set the number of rows
num_rows = 5
pyramid_pattern_alternate_numbers(num_rows)
