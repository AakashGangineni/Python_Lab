def inverted_half_pyramid(n):
    print("Pattern #7: Inverted Half Pyramid Number Pattern")
    for i in range(n + 1):
        # Print numbers from 0 to (n - i)
        for j in range(n - i + 1):
            print(j, end=' ')
        print()  # Move to the next line

# Set the number of rows
rows = 5

# Call the function to print the pattern
inverted_half_pyramid(rows)
