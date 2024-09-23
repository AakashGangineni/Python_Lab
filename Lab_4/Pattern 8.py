def pyramid_natural_numbers(max_number):
    print("Pattern #8: Pyramid of Natural Numbers Less Than 10")
    current_number = 1
    for i in range(1, max_number):
        # Print numbers in the current row
        for j in range(i):
            if current_number < 10:
                print(current_number, end=' ')
                current_number += 1
        print()  # Move to the next line

# Set the maximum number (less than 10)
max_number = 10

# Call the function to print the pattern
pyramid_natural_numbers(max_number)
