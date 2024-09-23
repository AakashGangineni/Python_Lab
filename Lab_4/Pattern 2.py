def inverted_pyramid_of_numbers(n):
    print("Pattern #2: Inverted Pyramid of Numbers")
    for i in range(n):
        # Print leading spaces
        print(' ' * i, end='')
        # Print the number (i + 1), (n - i) times
        print((str(i + 1) + ' ') * (n - i))

# Set the number of rows
rows = 5

# Call the function to print the pattern
inverted_pyramid_of_numbers(rows)
