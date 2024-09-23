def simple_number_triangle(n):
    print("Pattern #1: Simple Number Triangle Pattern")
    for i in range(1, n + 1):
        # Print the number i, i times
        print((str(i) + ' ') * i)

# Set the number of rows
rows = 5

# Call the function to print the pattern
simple_number_triangle(rows)
