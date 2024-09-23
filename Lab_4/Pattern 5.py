def inverted_pyramid_same_digit(n, digit):
    print("Pattern #5: Inverted Pyramid of the Same Digit")
    for i in range(n):
        # Print leading spaces
        print(' ' * i, end='')
        # Print the specified digit (n - i) times
        print((str(digit) + ' ') * (n - i))

# Set the number of rows and the digit to print
rows = 5
digit = 5

# Call the function to print the pattern
inverted_pyramid_same_digit(rows, digit)
