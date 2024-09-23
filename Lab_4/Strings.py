# A. To separate the string into comma-separated values
X = "India.is.my.country"
comma_separated_values = X.replace('.', ',')
print("Comma-separated values:", comma_separated_values)

# B. To remove a given character from a string
Y = "M.A.N.I.P.A.L"
character_to_remove = 'A'  # Example character to remove
string_without_character = Y.replace(character_to_remove, '')
print("String after removing character '{}': {}".format(character_to_remove, string_without_character))

# C. To remove the (.) dots from the string
string_without_dots = Y.replace('.', '')
print("String after removing dots:", string_without_dots)
