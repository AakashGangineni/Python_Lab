def reverse_pattern(n):
    current_number = 1
    for row in range(1, n + 1):
        # Calculate the numbers for this row
        numbers = [current_number + i for i in range(row)]
        # Update the current number for the next row
        current_number += row
        # Print the row in reverse order
        print(" ".join(map(str, numbers[::-1])))

# Set the number of rows
num_rows = 4
reverse_pattern(num_rows)
