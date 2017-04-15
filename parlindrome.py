string_example = input("Please type a string: ")
new_string = string_example.lower()

if new_string == new_string[::-1]:
    print("The string " + new_string + " is palindrome")
else:
    print("This string is not palindrome")
