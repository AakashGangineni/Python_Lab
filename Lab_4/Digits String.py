# Function to check if the string contains only digits
def contains_only_digits(s):
    return s.isdigit()

# Take input from the user
user_input = input("Enter a string: ")

# Check if the string contains only digits
if contains_only_digits(user_input):
    print("The string contains only digits.")
else:
    print("The string contains non-digit characters.")
