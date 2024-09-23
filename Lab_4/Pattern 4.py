def inverted_pyramid_descending(n):
    print("Pattern #4: Inverted Pyramid of Descending Numbers")
    for i in range(n):
        # Print leading spaces
        print(' ' * i, end='')
        # Print the number (n - i), (n - i) times
        print((str(n - i) + ' ') * (n - i))

# Set the number of rows
rows = 5

# Call the function to print the pattern
inverted_pyramid_descending(rows)
