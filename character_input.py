import datetime
# asks the user to enter their name

name = input("Give me your name: ")
# print("Your name is " + name)

# ask the user to enter their age

age = int(input("Give me your age: "))
# print("Your age is " + str(age))

now = datetime.datetime.now()
year_left = str(100 - age)
def year(age):
    return str(int(year_left) + int(str(now.year)))

print("Your name is " + name)
print("Your age is " + str(age))
print("The year " + str(name) + " turns 100-year-old is " + str(int(year_left) + int(now.year)))