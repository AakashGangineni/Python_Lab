def half_pyramid_pattern(n):
    print("Pattern #3: Half Pyramid Pattern of Numbers")
    for i in range(1, n + 1):
        # Print leading spaces
        print(' ' * (n - i) * 2, end='')  # Adjust space for alignment
        # Print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  # Move to the next line

# Set the number of rows
rows = 5

# Call the function to print the pattern
half_pyramid_pattern(rows)
