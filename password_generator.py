# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

import random
import string
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
numbers = string.digits
# symbols = ["(", ")", "`", "~", "!", "@", "#", "$", "%",  "^", "&", "*", "-", "+", "=", "|",  "\ ",  "{", "}", "[", "]", ":", ";", "<", ">",  ",", ".", "?", "/"]

password = upper_case + lower_case + numbers
length = int(input("How long would you like your password to be: "))
random_password = random.sample(password, length)
new_password = None

while True:
    if new_password == None:
        new_password = random.sample(password, length)
        new_password = "".join(random.sample(password, length))
        print(new_password)
        if len(new_password) < 10:
            print (new_password + " is a weak password")
        elif len(new_password) >= 10:
            print (new_password + " is a strong passwrod")
    elif new_password == "exit" or "Exit":
        break






