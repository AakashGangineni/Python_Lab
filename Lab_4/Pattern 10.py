def unique_pyramid(n):
    for i in range(1, n + 1):
        # Generate the ascending part of the pattern
        ascending = list(range(1, i + 1))
        # Generate the descending part of the pattern
        descending = ascending[-2::-1]  # Skip the last number to avoid repetition
        # Combine both parts
        pattern = ascending + descending
        # Print the pattern
        print(" ".join(map(str, pattern)))

# Set the number of rows
num_rows = 5
unique_pyramid(num_rows)
