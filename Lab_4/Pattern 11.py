def connected_inverted_pyramid(n):
    for i in range(n, 0, -1):
        # Create the left side of the pattern
        left_part = list(range(n, i - 1, -1))
        # Create the right side of the pattern
        right_part = list(range(i, n + 1))
        # Combine both parts
        pattern = left_part + right_part
        # Print the pattern
        print(" ".join(map(str, pattern)))

# Set the number of rows
num_rows = 5
connected_inverted_pyramid(num_rows)
