a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_less_than_10 = []
list_less_than_new_number = []

new_number = int(input("Give me a number: "))


for number in a:
    if number < 5:
        list_less_than_10.append(number)
print (list_less_than_10)

for number in a:
    if number < new_number:
        list_less_than_new_number.append(number)
print(list_less_than_new_number)

